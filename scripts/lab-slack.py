#!/usr/bin/env python3
"""lab-slack — a dependency-free CLI for operating the AICell Lab Slack.

No external packages (uses only the Python standard library), so it runs anywhere
the site automations run. Talks to the Slack Web API with a bot or user token.

Tokens (loaded from the environment, or from a secrets file — see _load_env):
  SLACK_BOT_TOKEN   xoxb-...  bot user; default for posting announcements.
  SLACK_USER_TOKEN  xoxp-...  Wei's user; for posting AS Wei (--as-user),
                              reading channels the bot isn't in, and broad search.

Commands:
  whoami                                   Show the authenticated identity.
  channels [--query STR]                   List/search channels (id + name).
  users    [--query STR]                   List/search workspace members.
  post   --channel '#general' --text "…"   Post a message to a channel.
         [--blocks-file f.json] [--as-user] [--thread TS]
  dm     --to '@email|email|U123' --text "…"   Direct-message a person.
  announce --post content/post/<slug>/index.md [--channel '#general']
           [--base https://aicell.io] [--dry-run]   Announce a blog post.

Examples:
  scripts/lab-slack.py whoami
  scripts/lab-slack.py post --channel '#general' --text 'Hello from the lab bot'
  scripts/lab-slack.py dm --to wei.ouyang@scilifelab.se --text 'ping'
  scripts/lab-slack.py announce --post content/post/bioengine-preprint/index.md
"""
import argparse
import json
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request

API = "https://slack.com/api/"
DEFAULT_CHANNEL = "#general"
DEFAULT_BASE = "https://aicell.io"
POLL_STATE = os.path.expanduser("~/.svamp/lab-slack-poll.json")
# Secrets files checked in order (first existing wins) for token env vars.
ENV_FILES = [
    os.path.expanduser("~/.svamp/lab-slack.env"),
    os.path.expanduser("~/.svamp/aicell-newsletter.env"),
]


def _load_env():
    """Populate os.environ with KEY=VALUE pairs from the secrets files (no override)."""
    for path in ENV_FILES:
        if not os.path.isfile(path):
            continue
        with open(path) as fh:
            for line in fh:
                line = line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip().strip('"').strip("'")
                os.environ.setdefault(k, v)


def _token(as_user=False):
    name = "SLACK_USER_TOKEN" if as_user else "SLACK_BOT_TOKEN"
    tok = os.environ.get(name)
    if not tok:
        sys.exit(
            f"error: {name} is not set. Put it in the environment or one of: "
            + ", ".join(ENV_FILES)
        )
    return tok


def _reads_as_user():
    """Reads (list/lookup) need broad scopes the bot often lacks — prefer the user token."""
    return bool(os.environ.get("SLACK_USER_TOKEN"))


def _call(method, params=None, json_body=None, as_user=False, soft=False):
    """Call a Slack Web API method. GET for reads (params), POST JSON for writes.

    soft=True returns the raw (possibly not-ok) response instead of exiting — used by
    poll() so one missing scope doesn't abort the whole sweep.
    """
    tok = _token(as_user=as_user)
    headers = {"Authorization": f"Bearer {tok}"}
    if json_body is not None:
        data = json.dumps(json_body).encode()
        headers["Content-Type"] = "application/json; charset=utf-8"
        req = urllib.request.Request(API + method, data=data, headers=headers)
    else:
        qs = urllib.parse.urlencode(params or {})
        req = urllib.request.Request(API + method + ("?" + qs if qs else ""), headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            out = json.loads(resp.read().decode())
    except urllib.error.URLError as e:
        if soft:
            return {"ok": False, "error": f"network:{e}"}
        sys.exit(f"error: network failure calling {method}: {e}")
    if not out.get("ok") and not soft:
        sys.exit(f"error: Slack API {method} failed: {out.get('error')} {out.get('response_metadata','')}")
    return out


# ---- read helpers ----------------------------------------------------------

def _list_all(method, key, params=None, as_user=False):
    items, cursor = [], None
    while True:
        p = dict(params or {})
        p["limit"] = 200
        if cursor:
            p["cursor"] = cursor
        out = _call(method, params=p, as_user=as_user)
        items.extend(out.get(key, []))
        cursor = out.get("response_metadata", {}).get("next_cursor")
        if not cursor:
            return items


def resolve_channel_id(ref, as_user=False):
    ref = ref.strip()
    if ref[:1] in ("C", "G", "D") and ref.isupper() is False and ref[1:2].isalnum():
        # Looks like a raw ID (C…/G…/D…)
        if ref[0] in "CGD" and len(ref) >= 8:
            return ref
    name = ref.lstrip("#")
    for ch in _list_all("conversations.list", "channels",
                        {"types": "public_channel,private_channel,mpim,im", "exclude_archived": "true"},
                        as_user=as_user):
        if ch.get("name") == name or ch.get("id") == ref:
            return ch["id"]
    sys.exit(f"error: channel '{ref}' not found (is the bot a member? try --as-user)")


def resolve_user_id(ref, as_user=False):
    ref = ref.strip().lstrip("@")
    if ref.startswith("U") and len(ref) >= 8:
        return ref
    if "@" in ref:  # email
        out = _call("users.lookupByEmail", {"email": ref}, as_user=as_user)
        return out["user"]["id"]
    for u in _list_all("users.list", "members", as_user=as_user):
        prof = u.get("profile", {})
        if ref.lower() in (
            u.get("name", "").lower(),
            (u.get("real_name") or "").lower(),
            (prof.get("display_name") or "").lower(),
            (prof.get("email") or "").lower(),
        ):
            return u["id"]
    sys.exit(f"error: user '{ref}' not found")


# ---- message send ----------------------------------------------------------

def send(channel_id, text=None, blocks=None, as_user=False, thread_ts=None):
    body = {"channel": channel_id}
    if blocks:
        body["blocks"] = blocks
        body["text"] = text or "New update from the AICell Lab"
    elif text:
        body["text"] = text
    else:
        sys.exit("error: need --text or --blocks-file")
    if thread_ts:
        body["thread_ts"] = thread_ts
    # Posting to a channel the bot isn't in fails with not_in_channel; retry as user.
    tok_name = "SLACK_USER_TOKEN" if as_user else "SLACK_BOT_TOKEN"
    if not os.environ.get(tok_name) and not as_user and os.environ.get("SLACK_USER_TOKEN"):
        as_user = True
    out = _call("chat.postMessage", json_body=body, as_user=as_user)
    return out


# ---- announce --------------------------------------------------------------

def _parse_front_matter(path):
    with open(path) as fh:
        txt = fh.read()
    if not txt.startswith("---"):
        sys.exit(f"error: {path} has no YAML front matter")
    fm = txt.split("---", 2)[1]
    meta = {}
    for line in fm.splitlines():
        if ":" in line and not line.startswith((" ", "-", "#")):
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip('"').strip("'")
    return meta


def announce(post_path, channel, base, dry_run=False, as_user=False, note=None):
    meta = _parse_front_matter(post_path)
    title = meta.get("title", "New post")
    summary = meta.get("summary", "")
    slug = os.path.basename(os.path.dirname(os.path.abspath(post_path)))
    url = f"{base.rstrip('/')}/post/{slug}/"
    blocks = [
        {"type": "section", "text": {"type": "mrkdwn",
            "text": f":newspaper: *<{url}|{title}>*"}},
    ]
    if summary:
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": summary}})
    if note:  # member @-mentions / highlights, e.g. "<@U…> this BioEngine item is for you"
        blocks.append({"type": "section", "text": {"type": "mrkdwn", "text": note}})
    blocks.append({"type": "context", "elements": [
        {"type": "mrkdwn", "text": f"aicell.io · <{url}|Read the full post →>"}]})
    fallback = f"{title} — {url}" + (f"\n{note}" if note else "")
    if dry_run:
        print(json.dumps({"channel": channel, "text": fallback, "blocks": blocks}, indent=2))
        return
    # chat.postMessage resolves '#name' server-side, so no channels:read needed.
    out = send(channel, text=fallback, blocks=blocks, as_user=as_user)
    print(f"posted to {channel} (ts={out.get('ts')})")


# ---- poll (receive) --------------------------------------------------------

_USER_CACHE = {}


def _user_label(uid):
    if not uid:
        return "someone"
    if uid in _USER_CACHE:
        return _USER_CACHE[uid]
    out = _call("users.info", {"user": uid}, soft=True)
    prof = (out.get("user") or {}).get("profile", {}) if out.get("ok") else {}
    label = prof.get("display_name") or prof.get("real_name") or uid
    _USER_CACHE[uid] = label
    return label


def _respond_spawn(msgs, repo="/Users/weio/workspace/aicell.io"):
    """Spawn a fresh Happy Agent responder per inbound message (robust 'respond in time')."""
    for m in msgs:
        where = "a direct message" if m["kind"] == "dm" else f"#{m['channel_name']}"
        thread = f" --thread {m['ts']}" if m["kind"] == "mention" else ""
        prompt = (
            f"You are Happy Agent, the AICell Lab's AI agent. A lab member ({m['user_label']}) "
            f"sent you this Slack message in {where}:\n\n\"{m['text']}\"\n\n"
            f"Respond helpfully, concisely, and on-brand. Reply by running:\n"
            f"  python3 {repo}/scripts/lab-slack.py post --channel {m['channel']}{thread} --text \"<your reply>\"\n"
            f"You can use the website repo and the lab-slack/aicell-website skills to answer. "
            f"If the message isn't actually addressed to you or needs a human, reply briefly saying so "
            f"(or do nothing). When done, stop."
        )
        try:
            subprocess.run(["svamp", "session", "spawn", "claude", "-d", repo, "--message", prompt],
                           timeout=60, capture_output=True, text=True)
        except Exception as e:
            print(f"warn: could not spawn responder: {e}", file=sys.stderr)


def poll(state_path=POLL_STATE, notify_session=None, respond=False, mark=True, lookback_hours=12, as_json=False):
    """Find new DMs to the bot and @mentions of the bot since the last poll."""
    bot_id = _call("auth.test")["user_id"]
    try:
        state = json.load(open(state_path)) if os.path.isfile(state_path) else {}
    except Exception:
        state = {}
    floor = time.time() - lookback_hours * 3600
    new = []

    def scan(cid, kind, channel_name=None, mention_only=False):
        last = float(state.get(cid, 0)) or floor
        h = _call("conversations.history", {"channel": cid, "oldest": str(last), "limit": 50}, soft=True)
        if not h.get("ok"):
            return
        newest = float(state.get(cid, 0))
        for m in h.get("messages", []):
            ts = float(m["ts"]); newest = max(newest, ts)
            # skip the agent's own messages and channel-join/system events; keep human msgs
            if ts <= last or m.get("user") == bot_id or m.get("subtype"):
                continue
            text = m.get("text", "")
            if mention_only and f"<@{bot_id}>" not in text:
                continue
            files = [{"id": f.get("id"), "name": f.get("name"), "mimetype": f.get("mimetype"),
                      "url_private": f.get("url_private")} for f in m.get("files", [])]
            new.append({"kind": kind, "channel": cid, "channel_name": channel_name,
                        "ts": m["ts"], "user": m.get("user"), "user_label": _user_label(m.get("user")),
                        "text": text, "files": files})
        state[cid] = newest

    # 1) Direct messages to the bot
    ims = _call("conversations.list", {"types": "im"}, soft=True)
    for im in ims.get("channels", []) if ims.get("ok") else []:
        scan(im["id"], "dm")
    # 2) @mentions in channels the bot belongs to
    chs = _call("conversations.list", {"types": "public_channel,private_channel",
                                       "exclude_archived": "true"}, soft=True)
    for ch in chs.get("channels", []) if chs.get("ok") else []:
        if ch.get("is_member"):
            scan(ch["id"], "mention", channel_name=ch.get("name"), mention_only=True)

    new.sort(key=lambda x: float(x["ts"]))
    if mark:
        os.makedirs(os.path.dirname(state_path), exist_ok=True)
        json.dump(state, open(state_path, "w"))

    if notify_session and new:
        _notify(notify_session, new)
    if respond and new:
        _respond_spawn(new)
    if as_json:
        print(json.dumps(new, indent=2))
    else:
        for m in new:
            where = "DM" if m["kind"] == "dm" else f"#{m['channel_name']}"
            print(f"[{where}] {m['user_label']}: {m['text']}  (channel={m['channel']} ts={m['ts']})")
    return new


def download_files(channel, since_ts=0.0, out_dir="data/slack-files", as_user=False):
    """Download file attachments from a channel's messages since `since_ts` (bot token)."""
    os.makedirs(out_dir, exist_ok=True)
    tok = _token(as_user=as_user)
    h = _call("conversations.history", {"channel": channel, "oldest": str(since_ts), "limit": 100}, soft=True)
    saved = []
    for m in h.get("messages", []):
        for f in m.get("files", []):
            url = f.get("url_private_download") or f.get("url_private")
            if not url:
                continue
            name = f"{f.get('id')}_{f.get('name', 'file')}"
            dest = os.path.join(out_dir, name)
            req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
            try:
                with urllib.request.urlopen(req, timeout=60) as r:
                    data = r.read()
                if data[:15].lstrip().lower().startswith(b"<!doctype html") or b"<html" in data[:200].lower():
                    print(f"warn: {name} came back as HTML — the bot likely lacks 'files:read' scope", file=sys.stderr)
                    continue
                with open(dest, "wb") as fh:
                    fh.write(data)
                saved.append(dest)
                print(f"saved {dest} ({len(data)} bytes, {f.get('mimetype')})")
            except Exception as e:
                print(f"warn: failed to download {name}: {e}", file=sys.stderr)
    if not saved:
        print("(no files downloaded)")
    return saved


def _notify(session, msgs):
    """Forward new inbound Slack messages to a Svamp session so the agent can reply."""
    lines = []
    for m in msgs:
        where = "a DM" if m["kind"] == "dm" else f"#{m['channel_name']}"
        att = ""
        if m.get("files"):
            att = f" [{len(m['files'])} attachment(s): " + ", ".join(f.get("name", "?") for f in m["files"]) + \
                  f" — download with: scripts/lab-slack.py files --channel {m['channel']} --since {m['ts']}]"
        lines.append(f"- From {m['user_label']} in {where} (channel={m['channel']}, thread_ts={m['ts']}):\n  \"{m['text']}\"{att}")
    body = (
        "📨 New Slack message(s) for Happy Agent — please read and respond in time.\n\n"
        + "\n".join(lines)
        + "\n\nReply with the lab-slack CLI: for a DM use `scripts/lab-slack.py post --channel <channel> --text \"…\"`; "
          "for a channel @mention reply in-thread with `--channel <channel> --thread <thread_ts>`. "
          "Be helpful, concise, and on-brand as Happy Agent. Ignore anything not actually addressed to you."
    )
    try:
        subprocess.run(["svamp", "session", "send", session, body], timeout=30,
                       capture_output=True, text=True)
    except Exception as e:
        print(f"warn: could not notify session {session}: {e}", file=sys.stderr)


# ---- CLI -------------------------------------------------------------------

def main():
    _load_env()
    ap = argparse.ArgumentParser(prog="lab-slack", description="Operate the AICell Lab Slack")
    sub = ap.add_subparsers(dest="cmd", required=True)

    sub.add_parser("whoami")

    pc = sub.add_parser("channels"); pc.add_argument("--query", default="")
    pu = sub.add_parser("users"); pu.add_argument("--query", default="")

    pp = sub.add_parser("post")
    pp.add_argument("--channel", default=DEFAULT_CHANNEL)
    pp.add_argument("--text"); pp.add_argument("--blocks-file")
    pp.add_argument("--as-user", action="store_true"); pp.add_argument("--thread")

    pd = sub.add_parser("dm")
    pd.add_argument("--to", required=True); pd.add_argument("--text", required=True)
    pd.add_argument("--as-user", action="store_true")

    pa = sub.add_parser("announce")
    pa.add_argument("--post", required=True)
    pa.add_argument("--channel", default=DEFAULT_CHANNEL)
    pa.add_argument("--base", default=DEFAULT_BASE)
    pa.add_argument("--dry-run", action="store_true")
    pa.add_argument("--as-user", action="store_true")
    pa.add_argument("--note", help="extra mrkdwn line (e.g. member @-mentions '<@U…> …')")

    pf = sub.add_parser("files", help="download file attachments from a channel/DM")
    pf.add_argument("--channel", required=True)
    pf.add_argument("--since", type=float, default=0.0, help="only files in messages after this ts")
    pf.add_argument("--out", default="data/slack-files")
    pf.add_argument("--as-user", action="store_true")

    pl = sub.add_parser("poll", help="discover new DMs + @mentions since last poll")
    pl.add_argument("--notify-session", help="forward new messages to this Svamp session id")
    pl.add_argument("--respond", action="store_true", help="spawn a fresh Happy Agent to reply to each new message")
    pl.add_argument("--no-mark", action="store_true", help="don't advance the seen-cursor (dry peek)")
    pl.add_argument("--lookback-hours", type=float, default=12)
    pl.add_argument("--json", action="store_true")

    a = ap.parse_args()

    if a.cmd == "whoami":
        out = _call("auth.test")
        print(f"team={out.get('team')} user={out.get('user')} id={out.get('user_id')} url={out.get('url')}")
    elif a.cmd == "channels":
        for ch in _list_all("conversations.list", "channels",
                            {"types": "public_channel,private_channel", "exclude_archived": "true"},
                            as_user=_reads_as_user()):
            if a.query.lower() in ch.get("name", "").lower():
                mark = "🔒" if ch.get("is_private") else "#"
                print(f"{ch['id']}  {mark}{ch.get('name')}")
    elif a.cmd == "users":
        for u in _list_all("users.list", "members", as_user=_reads_as_user()):
            if u.get("deleted") or u.get("is_bot"):
                continue
            prof = u.get("profile", {})
            hay = " ".join([u.get("name", ""), u.get("real_name") or "", prof.get("email") or ""]).lower()
            if a.query.lower() in hay:
                print(f"{u['id']}  {u.get('name')}  {prof.get('real_name','')}  <{prof.get('email','')}>")
    elif a.cmd == "post":
        blocks = None
        if a.blocks_file:
            with open(a.blocks_file) as fh:
                blocks = json.load(fh)
        out = send(a.channel, text=a.text, blocks=blocks, as_user=a.as_user, thread_ts=a.thread)
        print(f"posted to {a.channel} (ts={out.get('ts')})")
    elif a.cmd == "dm":
        uid = resolve_user_id(a.to, as_user=_reads_as_user())
        opened = _call("conversations.open", json_body={"users": uid}, as_user=a.as_user)
        cid = opened["channel"]["id"]
        out = send(cid, text=a.text, as_user=a.as_user)
        print(f"DM sent to {a.to} (ts={out.get('ts')})")
    elif a.cmd == "announce":
        announce(a.post, a.channel, a.base, dry_run=a.dry_run, as_user=a.as_user, note=a.note)
    elif a.cmd == "files":
        download_files(a.channel, since_ts=a.since, out_dir=a.out, as_user=a.as_user)
    elif a.cmd == "poll":
        poll(notify_session=a.notify_session, respond=a.respond, mark=not a.no_mark,
             lookback_hours=a.lookback_hours, as_json=a.json)


if __name__ == "__main__":
    main()
