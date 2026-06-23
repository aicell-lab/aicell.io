---
name: lab-newsletter
description: >-
  Produce the AICell Lab's recurring AI-generated newsletter — a nightly
  deep-research digest of news relevant to the lab (AI-for-biology, bioimaging,
  the lab's own software/papers, collaborators, funding, events). Collects
  sources locally, writes an on-brand digest post in the `newsletter` category,
  builds, commits to main, and posts to Slack #general. Use when running the
  nightly newsletter pipeline (svamp workflow `nightly-newsletter`) or when asked
  to generate/test a lab newsletter issue.
---

# Lab Newsletter Pipeline

This skill is the reusable procedure the nightly `nightly-newsletter` svamp
workflow runs. It turns "what's new and relevant to the lab" into a short,
cited, on-brand post on aicell.io and a Slack notice.

The website operating conventions (front matter, build, deploy) are in the
sibling [`aicell-website` skill](../aicell-website/SKILL.md) — read it for the
exact post front matter and the build/commit/deploy flow.

## Modes

- **`prod`** (default, nightly): full deep research, ~3–8 sources, one digest post.
- **`test`**: a fast smoke run that exercises the whole pipeline end-to-end with a
  minimal real post (1–2 quick sources). Use it to verify the workflow plumbing
  (scheduler → spawn → produce → commit) without a long research run.

## Pipeline (run top to bottom)

### 1. Research
Gather candidate items relevant to the lab's mission. Topics of interest:
- AI for cell & molecular biology, bioimage analysis, augmented microscopy,
  whole-cell modeling, foundation models for biology.
- The lab's own software & initiatives: ImJoy, BioImage Model Zoo / bioimage.io,
  BioEngine, AI4Life, Hypha, agent-lens, HPA.
- Collaborators, SciLifeLab / KTH / DDLS / WASP announcements, major venues,
  relevant funding calls and events.

Use `WebSearch`/`WebFetch` (or the `deep-research` skill in `prod`). Prefer
primary sources (papers, official blogs, release notes). **Never fabricate facts,
numbers, or quotes. Every claim must trace to a source you actually fetched.**

### 2. Collect sources locally
Save the raw source material into a dated folder so the digest is reproducible:
```
data/newsletter/<YYYY-MM-DD>/
  sources.md        # list: title — url — 1-line why-relevant — fetched-at
  *.txt / *.pdf     # optional saved copies of key sources
```
`data/newsletter/` is git-ignored for the bulky raw captures (see .gitignore);
keep `sources.md` small and commit it with the post if useful for provenance.

### 3. Filter & dedup
- Keep only items genuinely relevant to the lab. Quality over quantity — one
  well-curated digest beats many thin items.
- Drop anything already covered: check existing `content/post/` slugs and recent
  `newsletter` posts.

### 4. Write the digest post
Create `content/post/newsletter-<YYYY-MM-DD>/index.md`:
```yaml
---
title: "Lab Newsletter — <Month D, YYYY>"
summary: "This week in AI for life science: <one-line teaser>."
date: '<YYYY-MM-DD>T06:00:00Z'
lastmod: '<YYYY-MM-DD>T06:00:00Z'
draft: false
featured: false
authors:
  - aicell-lab
tags:
  - newsletter
categories:
  - newsletter          # the dedicated category for these AI-generated digests
---
```
Body: a short intro line, then 3–6 bulleted items. Each item = a bold headline,
2–4 sentences of plain-language digest, and an inline link to the source. House
voice: warm, first-person-plural, lightly linked. End with a one-line "Why it
matters for the lab." Keep it skimmable. No multi-MB images.

### 5. Build & commit
```bash
# hugo extended 0.101.0 (matches CI); see aicell-website skill for binary/cache setup
hugo --gc --minify -b https://aicell.io      # must exit 0
git add content/post/newsletter-<date> data/newsletter/<date>/sources.md
git commit -m "Newsletter: <Month D, YYYY> digest"
git push origin main                          # nightly is pre-authorized routine content
```

### 6. Publish to Slack #general
Post a short teaser + link to the live post. Slack delivery requires a configured
credential — see **Slack setup** below. If no credential is configured, SKIP Slack,
still publish the website post, and note in the commit/run output that Slack was
skipped (do not fail the whole run).

## Slack setup

Set one of these (checked in order); the pipeline no-ops Slack if none is present:
- `SLACK_WEBHOOK_URL` — an Incoming Webhook for #general. Post with:
  `curl -fsS -X POST -H 'Content-type: application/json' --data '{"text":"<msg>"}' "$SLACK_WEBHOOK_URL"`
- `SLACK_BOT_TOKEN` (+ channel `#general`) — `chat.postMessage` via the Slack API.

Store the secret outside the repo (e.g. the daemon/session environment), never commit it.

## Guardrails
- Never invent facts or quotes; always link the real source you fetched.
- Stay on-topic for the lab's mission; respect confidentiality (no unpublished
  internal work).
- Small scoped commit; reuse the `newsletter` category and existing tags.
- The site footer already discloses AI-assisted content.
