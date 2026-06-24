---
name: lab-image
description: >-
  Generate stunning, on-brand cover images for the AICell Lab site (daily digests,
  posts, projects) with Cloudflare Workers AI. Use when a post/digest needs a
  featured image, or to refresh a project cover. Backed by scripts/lab-image.py
  (dependency-free) with a baked-in signature visual style for consistency.
---

# Lab Image — cover generation

`scripts/lab-image.py` turns a one-line subject into a polished cover using
**Cloudflare Workers AI** (default model **FLUX.1 [schnell]** — a strong, fast,
recent text-to-image model). Every image carries the **AICell Lab signature style**
so the whole site looks cohesive.

## Setup (already configured)
Credentials live in `~/.svamp/.env` (never committed):
`CLOUDFLARE_ACCOUNT_ID`, `CLOUDFLARE_API_TOKEN` (token has Workers AI scope; verified).
The CLI auto-loads them.

## Commands
```bash
scripts/lab-image.py verify                      # check the token
scripts/lab-image.py models                      # list image models
scripts/lab-image.py generate --prompt "<subject>" --out <path.jpg> [--model flux|sdxl|...] [--steps N]
scripts/lab-image.py generate --prompt "…" --out … --raw      # skip the house style
scripts/lab-image.py generate --image <base.jpg> --prompt "…" --out … [--strength 0..1] [--seed N]   # img2img
```
You pass only the **subject** (what the cover is about) — the signature style is
appended automatically. FLUX returns a 1024×1024 JPEG; the CLI saves it and fixes
the extension to match the real format.

## The AICell Lab signature style (our visual trail)
**Flat, black & white, with orange as the only accent.** One recognizable look across the
whole site: clean flat minimalist illustration / line-art, strictly monochrome (black on
white), with a *single* bright-orange highlight used sparingly for the active accent — no
gradients, no shading, no 3D, no other colors, no text. It's baked into `HOUSE_STYLE` in
`scripts/lab-image.py`; keep it consistent. For icons, also ask the subject to *fill the
frame*. Examples: the Happy Agent avatar and the newsletter/BioEngine covers.

## Use it for posts / digests
Generate the cover **into the post folder** as `featured.jpg`; Hugo auto-processes it:
```bash
scripts/lab-image.py generate \
  --prompt "<one line capturing the post's topic>" \
  --out content/post/<slug>/featured.jpg
```
Then make sure the post front matter has an `image:` block (the templates already do).
Keep covers < 1 MB (FLUX JPEGs are ~0.4–0.6 MB — fine).

## Image-to-image / identity preservation (mascot variations)
Pass a **base image** with `--image PATH` to generate a variation of an existing
picture (e.g. our Happy Agent mascot in a new pose) instead of a fresh image from
text. The `--prompt` then *guides* the change.

```bash
# Make the mascot wave hello while keeping its identity (low strength = stays on-model)
scripts/lab-image.py generate \
  --image content/authors/happy-agent/avatar.jpg \
  --prompt "the same cute chibi robot mascot character, now waving hello with one hand" \
  --strength 0.4 --seed 7 --out /tmp/wave.png
```

Knobs:
- **`--strength` (0..1, default 0.6)** — how far to drift from the base.
  **LOWER preserves identity better.** In our tests **~0.4 kept the mascot clearly
  recognizable** (antennae, masked face, big eyes, blush, orange flask, silhouette);
  0.6 started to lose the face; 0.75 produced a *different* robot. Start at **0.35–0.45**.
- **`--seed INT`** — fix it for reproducible runs / A/B comparisons across strengths.

Honest limits (read before promising "same face"):
- **There is no true InstantID / IP-Adapter identity-lock model on Workers AI.** This
  img2img mode preserves **composition / pose / silhouette**, not a guaranteed exact
  face. Expect a *family-resemblance* variation, not a pixel-faithful clone. Re-roll
  seeds / nudge strength down until it looks like us; pick the best of a few.
- **Model:** only `@cf/runwayml/stable-diffusion-v1-5-img2img` (`sd15-img2img`) actually
  accepts image input on the REST API. **FLUX is text-only**, and despite the docs
  **SDXL-base rejects image input** — so `--image` with any non-img2img model
  **auto-switches to `sd15-img2img`** (it prints a note). Output is a **512×512 PNG**.
- **Style drift:** SD-1.5 may soften our strictly-flat black-&-white look (faint
  background texture, muted orange). Mitigate by keeping the **house-style prompt**
  (don't use `--raw`) and using **low strength**. For a crisp on-brand cover from
  scratch, prefer plain text-to-image with FLUX.

## Matching writing flavor (so words + image feel like one voice)
The digest/post voice is the verbal half of the same identity: **warm and
first-person-plural, curious and optimistic but grounded, concrete and lightly witty,
generous with links**, each item a bold headline + 2–4 plain-language sentences, ending
with a one-line *"why it matters for the lab."* Stunning visuals, clear human words —
consistently ours.
