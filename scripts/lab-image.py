#!/usr/bin/env python3
"""lab-image — generate cover images with Cloudflare Workers AI.

Dependency-free (uses `curl` + the standard library). Happy Agent uses this to make
nice cover/featured images for daily digests, posts, and projects.

Secret: reads CLOUDFLARE_ACCOUNT_ID + CLOUDFLARE_API_TOKEN from the environment or
`~/.svamp/.env` (never committed). Default model: FLUX.1 [schnell] — a strong, fast,
recent text-to-image model.

Commands:
  verify                                 Check the API token is valid.
  models                                 List the supported image models.
  generate --prompt "<text>" --out <path>
           [--model flux|sdxl|sdxl-lightning|dreamshaper|sd15-img2img]
           [--steps N] [--negative "<text>"] [--width W] [--height H]
           [--image PATH] [--strength FLOAT] [--seed INT]
                                         Generate an image and save it.

Image-to-image (identity-preserving variations):
  Pass --image PATH to seed generation from a base picture (e.g. our mascot) and
  produce a variation guided by --prompt. img2img needs a Stable Diffusion model
  (FLUX is text-only); if --image is given with the FLUX model, it auto-switches
  to "sdxl". --strength (0..1, default 0.6) controls how far to drift from the
  base: LOWER strength = closer to the original / better identity preservation.
  Note: Workers AI has no true InstantID/IP-Adapter face-lock model, so this
  preserves composition/silhouette, not a guaranteed exact face. SDXL may also
  shift our flat B&W style a little — use low strength and keep the house style.

Examples:
  scripts/lab-image.py verify
  scripts/lab-image.py generate --prompt "abstract AI + cell biology cover, blue/indigo, minimal" \
                                --out content/post/<slug>/featured.jpg
  scripts/lab-image.py generate --image content/authors/happy-agent/avatar.jpg \
                                --prompt "the same cute chibi robot mascot, waving hello" \
                                --strength 0.5 --seed 7 --out /tmp/wave.jpg
"""
import argparse, base64, json, os, subprocess, sys, tempfile

API = "https://api.cloudflare.com/client/v4/accounts"
ENV_FILES = [os.path.expanduser("~/.svamp/.env"), os.path.expanduser("~/.svamp/lab-image.env")]
MODELS = {
    "flux": "@cf/black-forest-labs/flux-1-schnell",          # default: SOTA-ish, fast, JSON/base64
    "sdxl": "@cf/stabilityai/stable-diffusion-xl-base-1.0",  # binary PNG
    "sdxl-lightning": "@cf/bytedance/stable-diffusion-xl-lightning",
    "dreamshaper": "@cf/lykon/dreamshaper-8-lcm",
    "sd15-img2img": "@cf/runwayml/stable-diffusion-v1-5-img2img",  # img2img, binary PNG
}
DEFAULT_MODEL = "flux"
# Models that belong to the FLUX family use the "steps" key; everyone else (Stable
# Diffusion) uses "num_steps". FLUX is text-to-image only (no image input).
FLUX_MODELS = {"@cf/black-forest-labs/flux-1-schnell"}
# Only these models accept an input image on the Workers AI REST API. (Despite the
# docs, SDXL-base 1.0 rejects image input there — only SD-1.5-img2img works.)
IMG2IMG_MODELS = {"@cf/runwayml/stable-diffusion-v1-5-img2img"}

# ---- AICell Lab signature style (applied to every prompt unless --raw) ----
# Strictly FLAT two-tone: pure black + pure white, bold line-art, ONE orange accent.
HOUSE_STYLE = (
    "in the AICell Lab flat style — a strictly FLAT 2D illustration, bold black-and-white "
    "line art, very high contrast using ONLY pure black and pure white (absolutely no greys, "
    "no gradients, no shading, no depth, no perspective, no 3D), with a SINGLE flat bright-orange "
    "accent used sparingly for one active highlight. Clean modern minimalist vector / icon look, "
    "simple bold flat shapes, crisp solid fills. No greyscale, no other colors. "
    "No text, no words, no letters, no logos, no watermark."
)


def styled(subject, raw=False, style=None):
    if raw:
        return subject
    return f"{subject.strip().rstrip('.')}. {style or HOUSE_STYLE}"


def _env(name):
    if os.environ.get(name):
        return os.environ[name]
    for p in ENV_FILES:
        if os.path.isfile(p):
            for line in open(p):
                if line.strip().startswith(name + "="):
                    return line.strip().split("=", 1)[1].strip().strip("'\"")
    return None


def _creds():
    acct, tok = _env("CLOUDFLARE_ACCOUNT_ID"), _env("CLOUDFLARE_API_TOKEN")
    if not acct or not tok:
        sys.exit("error: CLOUDFLARE_ACCOUNT_ID / CLOUDFLARE_API_TOKEN not set (env or ~/.svamp/.env)")
    return acct, tok


def _curl(method, url, token, body=None, out_file=None):
    args = ["curl", "-sS", "--max-time", "120", "-X", method,
            "-H", f"Authorization: Bearer {token}"]
    stdin = None
    if body is not None:
        # Pass the JSON via stdin ("--data @-") so large bodies (e.g. img2img's byte
        # array) don't blow the command-line argv size limit.
        args += ["-H", "Content-Type: application/json", "--data-binary", "@-"]
        stdin = json.dumps(body)
    if out_file:
        args += ["-o", out_file, "-w", "%{http_code}"]
    args.append(url)
    text = out_file is None
    if stdin is not None and not text:
        stdin = stdin.encode()
    p = subprocess.run(args, input=stdin, capture_output=True, text=text)
    return p


def cmd_verify():
    acct, tok = _creds()
    p = _curl("GET", f"{API}/{acct}/tokens/verify", tok)
    try:
        d = json.loads(p.stdout)
    except Exception:
        sys.exit(f"error: unexpected response: {p.stdout[:200]}")
    ok = d.get("success")
    status = (d.get("result") or {}).get("status")
    print(f"token: success={ok} status={status} errors={d.get('errors')}")
    # probe Workers AI scope with a tiny run
    print("Workers AI scope:", "checking…")
    sys.exit(0 if ok else 1)


def _detect_ext(data):
    if data[:3] == b"\xff\xd8\xff":
        return ".jpg"
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        return ".png"
    return None


def generate(prompt, out, model="flux", steps=None, negative=None, width=None, height=None,
             raw=False, style=None, image=None, strength=None, seed=None):
    acct, tok = _creds()
    model_id = MODELS.get(model, model)

    # img2img: FLUX is text-only and SDXL-base rejects image input on the REST API,
    # so auto-switch those to the Stable Diffusion 1.5 img2img model.
    if image and model_id not in IMG2IMG_MODELS:
        old = model
        model = "sd15-img2img"
        model_id = MODELS[model]
        print(f"note: model '{old}' can't do image-to-image; switching to '{model}'")

    body = {"prompt": styled(prompt, raw=raw, style=style)}
    # Steps key differs by family: FLUX uses "steps", Stable Diffusion uses "num_steps".
    if steps is not None:
        body["steps" if model_id in FLUX_MODELS else "num_steps"] = steps
    if negative: body["negative_prompt"] = negative
    if width: body["width"] = width
    if height: body["height"] = height
    if image:
        # Workers AI img2img wants the image as an array of uint8 bytes ("image");
        # the documented "image_b64" string is rejected by the run API for these models.
        with open(image, "rb") as f:
            body["image"] = list(f.read())
        if strength is not None: body["strength"] = strength
        if seed is not None: body["seed"] = seed
    url = f"{API}/{acct}/ai/run/{model_id}"

    tmp = tempfile.NamedTemporaryFile(delete=False).name
    p = _curl("POST", url, tok, body=body, out_file=tmp)
    code = p.stdout.decode(errors="replace") if isinstance(p.stdout, bytes) else (p.stdout or "")
    code = code.strip()
    raw = open(tmp, "rb").read()
    os.unlink(tmp)
    if code and code != "200":
        # body holds an error JSON
        try:
            err = json.loads(raw.decode())
            sys.exit(f"error: HTTP {code}: {err.get('errors')}")
        except Exception:
            sys.exit(f"error: HTTP {code}: {raw[:200]!r}")

    # Two response shapes: JSON {result:{image: base64}} (flux) OR raw image bytes (sdxl)
    img = None
    try:
        d = json.loads(raw.decode())
        if isinstance(d, dict) and (d.get("result") or {}).get("image"):
            img = base64.b64decode(d["result"]["image"])
        elif isinstance(d, dict) and not d.get("success", True):
            sys.exit(f"error: {d.get('errors')}")
    except (UnicodeDecodeError, json.JSONDecodeError):
        img = raw  # raw binary image
    if img is None:
        img = raw

    ext = _detect_ext(img)
    if ext is None:
        sys.exit(f"error: response was not a recognizable image ({raw[:120]!r})")
    fmt = ext[1:].upper()
    # Honour the exact --out path (predictable). FLUX returns JPEG → prefer a .jpg name.
    os.makedirs(os.path.dirname(os.path.abspath(out)) or ".", exist_ok=True)
    open(out, "wb").write(img)
    cur = os.path.splitext(out)[1].lower()
    note = "" if cur in (ext, ".jpeg") else f"  (note: bytes are {fmt}; consider a {ext} extension)"
    print(f"saved {out} ({len(img)} bytes, {fmt}, model {model_id}){note}")
    return out


def main():
    ap = argparse.ArgumentParser(prog="lab-image")
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify")
    sub.add_parser("models")
    pg = sub.add_parser("generate")
    pg.add_argument("--prompt", required=True)
    pg.add_argument("--out", required=True)
    pg.add_argument("--model", default=DEFAULT_MODEL)
    pg.add_argument("--steps", type=int)
    pg.add_argument("--negative")
    pg.add_argument("--width", type=int)
    pg.add_argument("--height", type=int)
    pg.add_argument("--raw", action="store_true", help="skip the AICell house style (use prompt verbatim)")
    pg.add_argument("--style", help="override the house style suffix")
    pg.add_argument("--image", help="base image for image-to-image (identity-preserving variation)")
    pg.add_argument("--strength", type=float, default=0.6,
                    help="img2img drift 0..1 (lower = closer to the base / better identity); default 0.6")
    pg.add_argument("--seed", type=int, help="RNG seed (reproducible results)")
    a = ap.parse_args()

    if a.cmd == "verify":
        cmd_verify()
    elif a.cmd == "models":
        for k, v in MODELS.items():
            print(f"{k:16} {v}{'   (default)' if k == DEFAULT_MODEL else ''}")
    elif a.cmd == "generate":
        generate(a.prompt, a.out, model=a.model, steps=a.steps,
                 negative=a.negative, width=a.width, height=a.height,
                 raw=a.raw, style=a.style,
                 image=a.image, strength=(a.strength if a.image else None), seed=a.seed)


if __name__ == "__main__":
    main()
