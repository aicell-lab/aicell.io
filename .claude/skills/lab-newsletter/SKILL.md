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
The digest is **grounded in what the lab does, then extends toward where the field
(and the lab's strategy) is heading.** Cover **two buckets** and mix them:

**Bucket A — the horizon** (the future the lab is building toward):
- The **virtual cell** and AI models of cells; **automated / autonomous scientific
  discovery** ("AI scientists", self-driving labs); **AI agents** for science and
  automation.
- **Advanced AI tools & development** — notable new models, frameworks, agent
  tooling, and capabilities (not just bio-specific) that the lab could build on.
- **State-of-the-art cell biology & omics** — single-cell / spatial / multi-omics,
  imaging, foundation models for biology.
- The **bigger picture**: what AI + automation could mean for science and humanity —
  problems we could *potentially solve with AI agents and automation*.
- Treat this as a **strategy radar**: when something could reshape how the lab works
  or what it should pursue, say so in one line.

**Bucket B — the lab's own focus** (keep it concrete and current):
- **Derive the focus list from the site**: read `content/project/*/index.md`
  titles+summaries and the `content/authors/aicell-lab` interests — the live priorities
  (today: ImJoy, BioImage Model Zoo, BioEngine, Hypha, Agent-Lens, REEF, the
  self-driving microscope, human/whole-cell modeling, Safe Colab, the Research Navigator).
- Track news touching those, the lab's own releases/papers, collaborators, and
  SciLifeLab / KTH / DDLS / WASP / Alpha Cell announcements, funding, and events.

Re-deriving Bucket B from `content/project/*` each run keeps the digest following the
lab's focus as projects evolve.

**Where to look:** gather from the curated source set in
[`sources.md`](./sources.md) (the lab's "information channels" — preprint servers,
journals, AI-lab blogs, virtual-cell/automated-discovery initiatives, the lab's own
GitHub/sites, funders, and events). Keep that file pruned and current as strategy shifts.

**Sweep X (Twitter)** via the `lab-x` CLI — a primary signal source:
- `scripts/lab-x.py monitor --since-hours 24 --min-likes 30` → recent high-signal posts
  from the watch-list (`x-accounts.md`: AI labs, AI-for-bio researchers, bioimaging,
  aggregators). Fold the genuinely relevant items into the digest, with their links.
- `scripts/lab-x.py search "<topic>" --max 20` for topic sweeps (e.g. "virtual cell").
- **Living watch-list:** also run `scripts/lab-x.py discover` and add any clearly
  relevant new accounts to `x-accounts.md` (verify with `lab-x.py info <h>` first).
  Every run, ask: *"is there a new person/channel worth following?"*

Use `WebSearch`/`WebFetch` (or the `deep-research` skill in `prod`). Prefer
primary sources (papers, official blogs, release notes). **Never fabricate facts,
numbers, or quotes. Every claim must trace to a source you actually fetched.**

**Tag relevant lab members.** When an item strongly matches someone's work, add a
short friendly @-mention so they see it — using the Slack IDs + keyword map in
`.claude/skills/lab-newsletter/lab-members.local.md` (gitignored). Tag sparingly
(strong matches only, ≤1–2 people per item; skip for routine lab-own news). The tag
is for the **Slack** announcement (`<@SLACK_ID>`); on the website post, name the
person in plain text instead of a Slack mention.

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
title: "Lab Newsletter — <Month D, YYYY>: <Short Descriptive Headline>"
summary: "Today in AI for life science: <one-line teaser>."
date: '<NOW>'        # the ACTUAL run time in UTC, e.g. `date -u +%Y-%m-%dT%H:%M:%SZ`
lastmod: '<NOW>'
draft: false
featured: false
authors:
  - Happy Agent
tags:
  - newsletter
categories:
  - newsletter          # the dedicated category for these AI-generated digests
---
```
> **Descriptive title:** keep the recognizable `Lab Newsletter — <Month D, YYYY>` prefix,
> then append `: <Short Descriptive Headline>` that captures the day's lead items (e.g.
> *"Thinking Microscopes & Self-Imagining Cells"*). This makes the post list and search
> results read like real stories instead of bare dates. Keep the headline punchy (≤ ~7 words).
> ⚠️ **Don't future-date the post.** Use the real current UTC time for `date`
> (`date -u +%Y-%m-%dT%H:%M:%SZ`), not a fixed hour like `06:00Z`. Hugo (and CI,
> which builds without `--buildFuture`) silently **skips future-dated content**, so
> a post stamped `06:00Z` won't render or deploy if the nightly fires earlier
> (the `0 5 * * *` cron is 05:00 *local*, ≈ 03:00 UTC).
Body: a short intro line, then 3–6 bulleted items. Each item = a bold headline,
2–4 sentences of plain-language digest, and an inline link to the source. House
voice: warm, first-person-plural, lightly linked. End with a one-line "Why it
matters for the lab." Keep it skimmable. No multi-MB images.

**Give it a cover.** Generate an on-brand featured image with the
[`lab-image`](../lab-image/SKILL.md) CLI (consistent AICell Lab signature style):
```bash
scripts/lab-image.py generate --prompt "<one line capturing today's digest>" \
  --out content/post/newsletter-<date>/index.jpg   # or featured.jpg in the folder
```
Hugo auto-processes `featured.jpg`. This makes each digest rich and recognizable.

### 5. Build & commit
**Get the correct env first.** Automations run as fresh agents/shells without the
build toolchain on PATH, and in Claude Code **each Bash call is a fresh shell** (env
does not persist between calls) — so `source scripts/setup-build-env.sh` in the SAME
command as the build. That script puts Hugo extended 0.101.0 + Go at stable paths
(`~/.cache/aicell-build`, not ephemeral `/tmp`), sets the cache vars, and loads
secrets from `~/.svamp/aicell-newsletter.env`.
```bash
# one shell: source env, then build with the resolved $HUGO_BIN (NOT bare `hugo`)
. scripts/setup-build-env.sh && "$HUGO_BIN" --gc --minify -b https://aicell.io   # must exit 0
git add content/post/newsletter-<date> data/newsletter/<date>/sources.md
git commit -m "Newsletter: <Month D, YYYY> digest"
git push origin main                          # nightly is pre-authorized routine content
```
Do **not** run `hugo mod get` (it upgrades the theme to v5.9.0 and breaks Hugo 0.101.0;
the theme is pinned in `go.mod`).

### 6. Announce to Slack #ai-digest (daily) — weekly highlights go to #general
Announce the published digest to the lab using the [`lab-slack`](../lab-slack/SKILL.md) CLI,
which formats a card linking to the post:
```bash
scripts/lab-slack.py announce --channel ai-digest --post content/post/newsletter-<date>/index.md \
  --note "<@U06DE2TPG1W> the BioEngine item might interest you · <@U082CS9FMNE> lab-automation news below"   # → #ai-digest

# Build the --note from lab-members.local.md: @-mention members whose keywords strongly
# match items in today's digest (sparingly; skip if nothing is a strong match → omit --note).
```
It loads the bot token from `~/.svamp/lab-slack.env` automatically. If Slack isn't
configured on this machine the command errors — that's non-fatal for the run: still
publish the website post and note Slack was skipped. Preview without posting via
`--dry-run`.

## Slack setup

Slack is handled by the **`lab-slack` skill** (`scripts/lab-slack.py`), which posts as the
lab bot using tokens in `~/.svamp/lab-slack.env` (`SLACK_BOT_TOKEN`, `SLACK_USER_TOKEN`) —
never committed. Use `scripts/lab-slack.py announce --post <path>` to announce a post, or
`scripts/lab-slack.py dm --to <email> --text "…"` to DM someone. (The legacy
`scripts/post-to-slack.sh` webhook helper still works as a fallback.)

## Scheduling (how the nightly run is wired)

The nightly digest runs as a **`svamp workflow`** on a cron schedule (workflows are
the single automation surface as of svamp-cli 0.2.176+):

```bash
svamp workflow add nightly-newsletter --on schedule --cron "0 5 * * *" \
  --run "svamp session send <owner-session-id> '<the pipeline prompt>'"
```
The generated yaml (`.svamp/workflows/nightly-newsletter.yaml`) is GitHub-Actions
style (`on: schedule: - cron`, `jobs: run: steps: - run`). The daemon's ~20s cron
tick fires it. Inspect with `svamp workflow list` / `svamp workflow run <name>` (manual).

History & gotchas (verified 2026-06-23/24):
- **Workflows now fire** on the daemon (cron scheduler shipped in 0.2.176). The old
  **`svamp trigger`/`routine` system was removed entirely** (#0048) — those commands now
  error. If you find references to triggers, they're stale; use workflows.
- **Never use `svamp session send .`** in an automation: `.` resolves via `SVAMP_SESSION_ID`,
  absent in the daemon/workflow shell → `No session found matching: .`. Target a real session
  id, or spawn a fresh agent.
- The step **enqueues to the owner session's message queue** (drained when that session is
  idle), so `<owner-session-id>` must be a **live** session that goes idle near the schedule
  time. **More robust alternative:** have the step spawn a fresh one-shot agent —
  `svamp session spawn claude -d /Users/weio/workspace/aicell.io --message "<pipeline prompt>"`
  — which produces and commits independently of any live session. Use this for on-demand runs
  and manual tests too.

## Guardrails
- Never invent facts or quotes; always link the real source you fetched.
- Stay on-topic for the lab's mission; respect confidentiality (no unpublished
  internal work).
- Small scoped commit; reuse the `newsletter` category and existing tags.
- The site footer already discloses AI-assisted content.
