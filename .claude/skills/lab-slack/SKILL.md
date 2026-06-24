---
name: lab-slack
description: >-
  Operate the AICell Lab Slack from the command line — post to channels, DM lab
  members, and announce new blog posts (e.g. the daily newsletter digest) to
  #general. Use when asked to notify the lab on Slack, share a post, DM someone,
  or wire Slack into an automation. Backed by scripts/lab-slack.py (dependency-free).
---

# Lab Slack

`scripts/lab-slack.py` is a **dependency-free** CLI (Python standard library only)
for the **AICell Lab** Slack workspace (`aicell-lab.slack.com`). It posts as the
bot **happyagent**, or as Wei with `--as-user`.

## Setup (already configured on this machine)

Tokens are loaded from `~/.svamp/lab-slack.env` (outside the repo, never committed):

```
SLACK_BOT_TOKEN=xoxb-…    # bot user; default for posting
SLACK_USER_TOKEN=xoxp-…   # Wei's user; for reads + posting AS Wei (--as-user)
```

The script auto-loads that file (and `~/.svamp/aicell-newsletter.env`) — no manual
`source` needed. The original tokens live in `~/workspace/weis-happy-agent/.env`
(see its `docs/setup-slack.md` / `docs/SLACK_USER_TOKEN.md` to rotate/recreate).

> Scope note: the bot token lacks `channels:read`/`users:read`, so **reads**
> (`channels`, `users`, DM target lookup) automatically use the user token. **Posting**
> uses the bot token. To post to a channel as the bot, the bot must be a member —
> invite `@happyagent` to the channel, or post with `--as-user` (as Wei).

## Commands

```bash
scripts/lab-slack.py whoami                       # show identity (sanity check)
scripts/lab-slack.py channels [--query general]   # list/search channels (id + name)
scripts/lab-slack.py users [--query ouyang]       # list/search members (for DMs)

# Post a message to a channel (bot must be in it; else add --as-user)
scripts/lab-slack.py post --channel '#general' --text "…"
scripts/lab-slack.py post --channel '#general' --blocks-file blocks.json --text "fallback"

# Direct-message a person (by email, @handle, display name, or U-id)
scripts/lab-slack.py dm --to wei.ouyang@scilifelab.se --text "…"

# Announce a blog post (formats a Block Kit card linking to aicell.io)
scripts/lab-slack.py announce --post content/post/<slug>/index.md   # → #general
scripts/lab-slack.py announce --post content/post/<slug>/index.md --dry-run   # preview JSON
```

## Receiving — discover & respond to DMs and @mentions

The bot can **receive** too. `poll` reads new direct messages to the bot and new
`@happyagent` mentions in channels it belongs to, since the last check (cursor stored
in `~/.svamp/lab-slack-poll.json`), and can act on them:

```bash
scripts/lab-slack.py poll                       # print new inbound messages (advances cursor)
scripts/lab-slack.py poll --no-mark --json      # peek without advancing the cursor
scripts/lab-slack.py poll --respond             # spawn a fresh Happy Agent to reply to each
scripts/lab-slack.py poll --notify-session <id> # forward new messages to a live session instead
```

**Background loop (respond in time).** A `svamp workflow` named **`slack-watch`** runs
`poll --notify-session high-frog-dzjybt` **every 2 minutes**, forwarding any new DM or
`@happyagent` mention into the **main Happy Agent session** (`high-frog-dzjybt`), which
reads it and replies — everything is handled in that one session (no spawning extra
sessions). Manage it with `svamp workflow show slack-watch` / `svamp workflow run slack-watch`.
(`poll --respond`, which spawns a fresh responder per message, exists as an alternative but
is **not** used here — keep handling in the single main session.)

> How it works: there's no public webhook — this is **pull-based polling** via the Slack
> Web API (`conversations.history` over the bot's DMs + member channels), deduped by a
> per-channel timestamp cursor. The bot has the needed scopes (`im:history`,
> `channels:history`, `app_mentions:read`). Latency ≈ the poll interval.

A spawned responder replies with:
`scripts/lab-slack.py post --channel <channel> [--thread <thread_ts>] --text "…"`.

## Primary use — announce new blog posts

Whenever a new post is published (especially the **daily newsletter digest**),
announce it to **#general**:

```bash
scripts/lab-slack.py announce --post content/post/newsletter-<YYYY-MM-DD>/index.md
```

`announce` reads the post's front matter (`title`, `summary`) and the folder slug,
builds the `https://aicell.io/post/<slug>/` link, and posts a clean card. This is
what the `lab-newsletter` skill calls in its Slack step.

## DMing people

DM sparingly and only when it's genuinely useful (e.g. a result someone asked for):
```bash
scripts/lab-slack.py dm --to <email> --text "<short, actionable note>"
```
Find a person's handle/email with `scripts/lab-slack.py users --query <name>`.

## Guardrails

- **#general reaches the whole lab.** Announce real, on-topic posts; never test or
  spam there — use `--dry-run`, a DM to Wei, or a quiet channel to verify first.
- Keep messages concise and linked; let the blog post carry the detail.
- Never commit tokens. They live only in `~/.svamp/lab-slack.env` (chmod 600).
- If a post to a channel fails with `not_in_channel`, invite `@happyagent` to that
  channel or re-run with `--as-user`.
