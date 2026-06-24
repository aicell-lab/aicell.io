---
name: aicell-website
description: >-
  Operate and maintain the AICell Lab website (aicell.io) — a Hugo + Wowchemy
  (Academic theme) static site. Use this when asked to add/update/remove team
  members, write news posts, add or edit projects, refresh publications from
  Google Scholar, open or close recruiting positions, edit homepage sections,
  preview the site locally, or deploy. Covers the exact content/frontmatter
  conventions, the build/deploy pipeline, and known data quirks.
---

# AICell Lab Website Operations

This skill is the operating manual for **aicell.io**, the website of the AICell
Lab (Wei Ouyang's group at KTH / SciLifeLab). It tells you how the site is built
and exactly how to perform every common maintenance task safely.

## 1. Architecture at a glance

- **Generator:** [Hugo](https://gohugo.io) static site generator.
- **Theme:** [Wowchemy](https://wowchemy.com) "Academic" theme **v5.8.1**, pulled
  in as a **Hugo Module** (not a git submodule) — see `go.mod` / `config/_default/config.yaml`.
- **Content is data, not code.** Almost everything you'll change lives under
  `content/` as Markdown files with YAML front matter. You rarely touch HTML.
- **Homepage = page builder.** The front page is assembled from "widget" sections
  in `content/home/*.md`. Each file is one section; its `weight` sets the order.
- **Custom bits** (only edit if explicitly asked):
  - `modules/wowchemy-plugin-imjoy-slides/` — local Hugo module for interactive
    ImJoy slides used by some project pages.
  - `layouts/partials/blocks/v1/people.html`, `.../about.html`, `views/compact.html`
    — theme overrides. The people block uses a **case-sensitive** group match.
  - `assets/scss/custom.scss` — site-wide style overrides.

### Deploy pipeline (important)

The live site is **GitHub Pages**, not Netlify (the `netlify.toml` is legacy/unused).

```
push to `main`  →  .github/workflows/build.yml  →  hugo --gc --minify
                →  publishes ./public to the `gh-pages` branch  →  served at aicell.io (CNAME)
```

- CI builds with **Hugo extended 0.101.0** (see `build.yml`). Match this locally.
- `pull_request` events build but **do not deploy** (deploy is gated on `main`).
- Therefore: **opening a PR is a safe dry run** — CI proves the site builds before
  anything goes live. Merging to `main` is what actually publishes.

### Content map

| Section | Path | What it is |
|---|---|---|
| Homepage sections | `content/home/*.md` | Page-builder widgets (about, people, projects, posts, …) |
| Team members | `content/authors/<username>/_index.md` (+ `avatar.png`) | One folder per person |
| Projects | `content/project/<slug>/index.md` | Portfolio cards on homepage + detail pages |
| News posts | `content/post/<slug>/index.md` | Blog/news (welcomes, awards, announcements) |
| Publications | `content/publication/<slug>/index.md` (+ `cite.bib`) | Generated from BibTeX |
| Recruiting | `content/recruiting/<slug>/index.md` | Open positions |
| About page | `content/about/index.md` | Long-form about page (`/about`) |
| Slides | `content/slides/` | ImJoy/reveal slide decks |
| CMS | `content/admin/index.md` | Wowchemy/Netlify CMS at `/admin` (optional, web editor) |

Templates for the common content types live next to this file in `templates/`.

## 2. Before you start (every session)

1. **Branch.** Never commit directly to `main` unless the user explicitly asks.
   Create a feature branch: `git switch -c website/<short-task>`.
2. **Know the deploy gate.** Changes go live only when merged to `main`. Default
   workflow: branch → PR → (CI green) → user merges. Confirm before pushing to `main`.
3. **Preview locally when feasible** (see §8). If Hugo isn't installed and can't be,
   rely on a PR build as the verification step and say so.

## 3. Add / update / remove a team member

Each person is a folder under `content/authors/`. Steps to **add**:

1. `mkdir content/authors/<username>` (lowercase, no spaces, e.g. `jane`).
2. Create `_index.md` from `templates/author._index.md`. Key fields:
   - `title:` — display name.
   - `role:` — position (e.g. `PhD Student`, `Postdoc`, `Research Engineer`).
   - `user_groups:` — **controls placement on the People section.** See the quirk below.
   - `superuser: true` + `weight: 1` only for the PI (Wei). Lower `weight` = earlier.
   - `bio:`, `social:` (icons: `envelope`, `twitter`, `github`, `circle-info`,
     `graduation-cap`/`google-scholar`), and the body Markdown = the person's blurb.
3. Add a square portrait as `content/authors/<username>/avatar.png` (the theme
   crops to a 270×270 circle; ~600×600+ is plenty — avoid giant multi-MB files).

> ⚠️ **People-group quirk (verify this).** The People homepage section
> (`content/home/people.md`) only shows these groups, in this order:
> **`PI`**, **`lab members`**, **`Alumni`** — and the match is **case-sensitive**
> (`layouts/partials/blocks/v1/people.html` uses `intersect`). Current data is
> inconsistent: some alumni use lowercase `alumni` (won't render), and the PI is
> currently filed under `lab members` rather than `PI`. When adding/moving people,
> use the **exact** strings `PI`, `lab members`, or `Alumni`. If asked to "fix the
> team page," normalizing these groups is the fix.

**Move to alumni:** change `user_groups` to `Alumni` (exact case). **Remove:** delete
the folder (prefer moving to Alumni unless the user wants them gone entirely).

When a member joins, the lab convention is also to publish a **welcome news post**
(see §5) — offer to do both.

## 4. Add or edit a project

Projects are portfolio cards (homepage `projects` widget) plus a detail page.

1. `mkdir content/project/<slug>` and create `index.md` from `templates/project.index.md`.
2. Fill `title`, `summary` (shown on the card), `tags` (also drive the portfolio
   filter buttons — reuse existing tags so filters stay tidy), and `links`.
3. Add `featured.png`/`featured.jpg` in the folder for the card image.
4. `external_link:` — if set, the card links straight out and **no detail page** is
   generated. Leave empty to build a detail page from the Markdown body.
5. Advanced: ImJoy-interactive projects (e.g. `imjoy`) use an `imjoy:` block + a
   `slides:` reference into `content/slides/`. Copy an existing one as a model.

## 5. Write a news post

Posts under `content/post/<slug>/index.md` power the "Recent Posts" section.

1. `mkdir content/post/<slug>` (e.g. `welcome-jane`, `paper-in-nature-methods`).
2. Create `index.md` from `templates/post.index.md`. Set `title`, `summary`,
   `date` (ISO, e.g. `'2026-06-23T00:00:00Z'`), `authors: [Wei Ouyang]`,
   `tags`, `categories` (e.g. `news`). `featured: true` surfaces it more prominently.
3. Add a `featured.jpg`/`png` for the header image (optional but expected).
4. Write the body in Markdown. House style: warm, first-person-plural, a few links.

## 6. Recruiting (open positions)

Positions live in `content/recruiting/<slug>/index.md`.

- The homepage "Open Positions" section (`content/home/recruiting.md`) lists only
  pages tagged **`open`**. To **close** a position, change its tag from `open` to
  `closed` (and usually update the `links` button to "Application Closed"). To
  **open** one, copy `templates/recruiting.index.md`, set tag `open`, add the
  application/contact `links`.

## 7. Update publications from Google Scholar

Publications are generated from BibTeX — don't hand-write the per-paper folders.

1. Export the lab's citations to `assets/publications.bib`. Either:
   - Download from the PI's Scholar profile (user `bJBzM18AAAAJ`) via the EXPORT →
     BibTeX button, save as `assets/publications.bib`; **or**
   - use the `curl` export URL documented in `README.md` (the `citsig` token in it
     expires, so the manual EXPORT is the reliable path).
2. Convert to Hugo content:
   ```bash
   pip3 install -U academic
   academic import --bibtex assets/publications.bib
   ```
   This regenerates folders under `content/publication/`.
3. Review the diff — `academic` can overwrite manual tweaks (abstracts, images,
   `featured: true`). Keep intentional edits; don't blindly commit the whole regen.
4. **Preprint guard (confidentiality — do this on every refresh).** Do **not**
   auto-publish preprints blindly. For any *new* entry that is a preprint
   (`publication: '*bioRxiv*'`/`'*arXiv*'`, `publication_types: ['3']`):
   - **Verify it is genuinely public**: resolve the `doi:` and confirm the title it
     returns matches the lab's paper. DOIs can be conflated — a near-identical DOI may
     point to a *different* paper. If you cannot independently verify (e.g. the host
     blocks fetching), treat it as unverified.
   - **When unsure, confirm before publishing** with the responsible project agent
     (`svamp session list`) or the corresponding author (Wei Ouyang). Never publish an
     entry that cites an in-preparation/unpublished manuscript.
   - **Flag, don't auto-commit** uncertain preprints — hold them out of the commit and
     surface them for review, rather than letting an unverified citation go live.
   - *Precedent:* an auto-imported BioEngine preprint (`mechtel-2026-bioengine`) was
     briefly pulled when its DOI couldn't be verified, then restored once the PI
     confirmed it was public. Verify, don't assume — in either direction.

## 8. Preview locally

CI uses **Hugo extended 0.101.0**. Newer Hugo can break Wowchemy v5, so prefer a
matching version.

```bash
# macOS (Homebrew installs current Hugo — usually fine for a quick look, but if the
# build errors with template/module issues, fall back to a pinned 0.101.0 binary):
brew install hugo

hugo server           # live preview at http://localhost:1313
hugo --gc --minify    # production build into ./public (what CI runs)
```

On this remote machine, share the preview instead of localhost:
```bash
hugo server --bind 0.0.0.0 --port 1313 --baseURL http://localhost &
svamp service expose aicell-preview --port 1313
svamp session set-link "<printed-url>" "Site preview"
```

Known build hiccup (from README): if you see
`unknown output format "redirects"`, clear the module cache and refetch:
```bash
rm -rf $TMPDIR/hugo_cache/ && hugo mod get && hugo server
```

If Hugo/Go can't be installed in the sandbox, skip local preview and rely on the
**PR build** as verification — state clearly that you did so.

## 9. Commit & deploy

1. Stage only what you changed; keep commits scoped (one member, one post, etc.).
2. Commit message: imperative, specific (`Add Jane Doe to team`, `Close AI4Life postdoc`).
3. Push the branch and open a PR — CI build is the safety check.
   ```bash
   git push -u origin website/<short-task>
   gh pr create --fill
   ```
4. **Going live = merge to `main`.** Do this only when the user approves (or has
   pre-authorized routine content updates). The `gh-pages` deploy runs automatically
   on merge; no manual publish step.

Co-author trailer for commits made by this agent:
`Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`

## 10. Guardrails

- Treat `modules/`, `layouts/`, `config/`, and `go.mod` as infrastructure — only
  touch when the task is explicitly about layout/config/theme, and preview before PR.
- Don't commit huge images. The repo already has at least one oversized avatar
  (~13 MB `content/authors/wei/avatar.png`); don't add more — downscale to ~600px.
- Reuse existing `tags`/`categories` rather than minting near-duplicates.
- Match the existing voice in posts/bios (warm, first-person-plural, lightly linked).
- The site footer already discloses AI-assisted content — no need to add disclaimers.
- After any task that produces a viewable result, set a session link to the preview/PR.
