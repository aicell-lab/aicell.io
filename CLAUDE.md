# AICell Lab Website — Agent Guide

This repository is the website for the **AICell Lab** (Wei Ouyang's group at KTH
Royal Institute of Technology / SciLifeLab), served at **https://aicell.io**.

## Purpose

This is an **AI-maintained lab website**. Beyond being a normal Hugo site, the
goal is for AI agents to keep it alive and current with minimal human effort:

1. **Lab material** — keep the core content accurate and well-presented: the
   team, projects, publications, recruiting positions, and the about page.
2. **Relevant news, daily** — agents collect news relevant to the lab (the field,
   the lab's papers/software, collaborators, funding, events), **digest** it into
   short, on-brand posts, and publish them to the site's news section so the front
   page always reflects what's current.

The site should feel maintained and timely without a person hand-editing Markdown.

## How it works (orientation)

- **Generator:** Hugo + Wowchemy "Academic" theme v5.8.1 (Hugo Module).
- **Content-as-data:** nearly all changes are Markdown + YAML front matter under
  `content/`. The homepage is assembled from page-builder widgets in `content/home/`.
- **Deploy:** push to `main` → GitHub Actions (`.github/workflows/build.yml`,
  Hugo 0.101.0) builds and publishes to the `gh-pages` branch → served at aicell.io.
  A pull request builds in CI but does **not** deploy — so a PR is a safe dry run.

**Full operating manual + content templates live in the
[`aicell-website` skill](.claude/skills/aicell-website/SKILL.md).** Read it before
editing — it has the exact front-matter for each content type and the known quirks.

## Content map

| What | Where |
|---|---|
| Homepage sections | `content/home/*.md` |
| Team members | `content/authors/<name>/_index.md` (+ `avatar.png`) |
| News / blog posts | `content/post/<slug>/index.md` |
| Projects | `content/project/<slug>/index.md` |
| Publications | `content/publication/<slug>/index.md` (generated from `assets/publications.bib`) |
| Recruiting | `content/recruiting/<slug>/index.md` (tag `open` to list it) |
| About page | `content/about/index.md` |

## Daily news digest (the autonomous part)

The intended loop, run by a scheduled agent:

1. **Collect** — gather candidate items from sources relevant to the lab: AI-for-
   biology / bioimaging research, the lab's own papers and open-source projects
   (ImJoy, BioImage Model Zoo, BioEngine, AI4Life…), collaborators, SciLifeLab /
   KTH / DDLS announcements, and major venues.
2. **Filter & dedup** — keep only items genuinely relevant to the lab's mission;
   drop anything already covered (check existing `content/post/` slugs).
3. **Digest** — write a short, accurate, on-brand post per item (house voice:
   warm, first-person-plural, lightly linked; cite the source). Front-matter per
   `templates/post.index.md`. Prefer one well-curated post over many thin ones.
4. **Verify** — `hugo --gc --minify` (or rely on the PR build) must pass.
5. **Publish** — open a PR (default) or, if pre-authorized for routine news,
   commit to `main`. Merge → auto-deploy.

Guardrails: never invent facts or fabricate quotes; always link the source; stay
on-topic for the lab; small scoped commits; reuse existing tags/categories; don't
add multi-MB images. The site footer already discloses AI-assisted content.

## Working conventions

- Branch for changes (`git switch -c website/<task>`); open a PR; CI green before merge.
- Going live = merge to `main`. Do that only when the user approves or has
  pre-authorized routine content updates.
- Don't touch `modules/`, `layouts/`, `config/`, or `go.mod` unless the task is
  explicitly about theme/config — preview locally before any such PR.
