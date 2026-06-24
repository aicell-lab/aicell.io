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
```
You pass only the **subject** (what the cover is about) — the signature style is
appended automatically. FLUX returns a 1024×1024 JPEG; the CLI saves it and fixes
the extension to match the real format.

## The AICell Lab signature style (our visual trail)
One recognizable look across the site — *abstract science-art blending flowing AI
data-sculpture (à la Refik Anadol) with bioluminescent microscopy*: deep cobalt→indigo
gradients, luminous cyan and soft-violet glow, elegant translucent cells / molecular
networks / streams of data, gentle volumetric light, particle bokeh, premium editorial
minimalism — **no text**. It's baked into `HOUSE_STYLE` in `scripts/lab-image.py`; keep
it consistent (edit there if the brand evolves). Examples live on the newsletter and
BioEngine post covers.

## Use it for posts / digests
Generate the cover **into the post folder** as `featured.jpg`; Hugo auto-processes it:
```bash
scripts/lab-image.py generate \
  --prompt "<one line capturing the post's topic>" \
  --out content/post/<slug>/featured.jpg
```
Then make sure the post front matter has an `image:` block (the templates already do).
Keep covers < 1 MB (FLUX JPEGs are ~0.4–0.6 MB — fine).

## Matching writing flavor (so words + image feel like one voice)
The digest/post voice is the verbal half of the same identity: **warm and
first-person-plural, curious and optimistic but grounded, concrete and lightly witty,
generous with links**, each item a bold headline + 2–4 plain-language sentences, ending
with a one-line *"why it matters for the lab."* Stunning visuals, clear human words —
consistently ours.
