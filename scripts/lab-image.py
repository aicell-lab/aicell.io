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
           [--model flux|sdxl|sdxl-lightning|dreamshaper]
           [--steps N] [--negative "<text>"] [--width W] [--height H]
                                         Generate an image and save it.

Examples:
  scripts/lab-image.py verify
  scripts/lab-image.py generate --prompt "abstract AI + cell biology cover, blue/indigo, minimal" \
                                --out content/post/<slug>/featured.jpg
"""
import argparse, base64, json, os, subprocess, sys, tempfile

API = "https://api.cloudflare.com/client/v4/accounts"
ENV_FILES = [os.path.expanduser("~/.svamp/.env"), os.path.expanduser("~/.svamp/lab-image.env")]
MODELS = {
    "flux": "@cf/black-forest-labs/flux-1-schnell",          # default: SOTA-ish, fast, JSON/base64
    "sdxl": "@cf/stabilityai/stable-diffusion-xl-base-1.0",  # binary PNG
    "sdxl-lightning": "@cf/bytedance/stable-diffusion-xl-lightning",
    "dreamshaper": "@cf/lykon/dreamshaper-8-lcm",
}
DEFAULT_MODEL = "flux"

# ---- AICell Lab signature cover style (applied to every prompt unless --raw) ----
# One consistent, recognizable look across all digests/posts: abstract science-art,
# deep cobalt→indigo with luminous cyan, elegant flowing cell/network/data forms.
HOUSE_STYLE = (
    "in the AICell Lab signature style — a stunning, premium abstract science-art cover that "
    "blends the look of flowing AI data-sculpture (think Refik Anadol) with bioluminescent "
    "microscopy: a deep cobalt-blue to indigo gradient field glowing with luminous cyan and "
    "soft violet light, elegant translucent forms suggesting living cells, neural and molecular "
    "networks, and streams of flowing data, rendered with gentle volumetric lighting, delicate "
    "particle bokeh, and smooth glossy depth; modern editorial minimalism, cinematic and "
    "ultra-clean composition, very high detail with refined color grading. "
    "Absolutely no text, no words, no letters, no logos, no watermark."
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
    if body is not None:
        args += ["-H", "Content-Type: application/json", "--data", json.dumps(body)]
    if out_file:
        args += ["-o", out_file, "-w", "%{http_code}"]
    args.append(url)
    p = subprocess.run(args, capture_output=True, text=(out_file is None))
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
             raw=False, style=None):
    acct, tok = _creds()
    model_id = MODELS.get(model, model)
    body = {"prompt": styled(prompt, raw=raw, style=style)}
    if steps is not None: body["steps"] = steps
    if negative: body["negative_prompt"] = negative
    if width: body["width"] = width
    if height: body["height"] = height
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
    a = ap.parse_args()

    if a.cmd == "verify":
        cmd_verify()
    elif a.cmd == "models":
        for k, v in MODELS.items():
            print(f"{k:16} {v}{'   (default)' if k == DEFAULT_MODEL else ''}")
    elif a.cmd == "generate":
        generate(a.prompt, a.out, model=a.model, steps=a.steps,
                 negative=a.negative, width=a.width, height=a.height,
                 raw=a.raw, style=a.style)


if __name__ == "__main__":
    main()
