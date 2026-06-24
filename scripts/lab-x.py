#!/usr/bin/env python3
"""lab-x — monitor X (Twitter) for the AICell Lab newsletter.

Dependency-free (uses `curl` + the standard library). Talks to the getxapi.com X API.

Secret: reads `X_API_KEY` from the environment or `~/.svamp/.env` / `~/.svamp/lab-x.env`
(never committed). API base: https://api.getxapi.com (Bearer auth, ~$0.001/call).

Commands:
  info  <handle>                       Verify a handle (name, followers, bio).
  user  <handle> [--max N] [--since-hours H] [--json]
                                       Recent tweets from one account.
  search "<query>" [--max N] [--json]  Advanced search (e.g. 'AI virtual cell').
  monitor [--accounts-file F] [--since-hours H] [--min-likes N] [--max-per N] [--json]
                                       Sweep the watch-list → recent, high-signal tweets
                                       for the daily digest (default list: x-accounts.md).

Examples:
  scripts/lab-x.py info karpathy
  scripts/lab-x.py user karpathy --since-hours 48
  scripts/lab-x.py monitor --since-hours 24 --min-likes 50
"""
import argparse, json, os, subprocess, sys, time
from datetime import datetime, timezone, timedelta

BASE = "https://api.getxapi.com"
ENV_FILES = [os.path.expanduser("~/.svamp/.env"), os.path.expanduser("~/.svamp/lab-x.env")]
DEFAULT_ACCOUNTS = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "..", ".claude", "skills", "lab-newsletter", "x-accounts.md")


def _key():
    if os.environ.get("X_API_KEY"):
        return os.environ["X_API_KEY"]
    for p in ENV_FILES:
        if os.path.isfile(p):
            for line in open(p):
                if line.strip().startswith("X_API_KEY="):
                    return line.strip().split("=", 1)[1].strip().strip("'\"")
    sys.exit("error: X_API_KEY not set (env or ~/.svamp/.env)")


def _get(path):
    """GET via curl (the host resets python-urllib TLS; curl is reliable)."""
    url = BASE + path
    for attempt in range(3):
        p = subprocess.run(
            ["curl", "-sS", "--max-time", "40", "-H", f"Authorization: Bearer {_key()}",
             "-H", "Accept: application/json", url],
            capture_output=True, text=True)
        if p.returncode == 0 and p.stdout.strip().startswith(("{", "[")):
            try:
                return json.loads(p.stdout)
            except json.JSONDecodeError:
                pass
        time.sleep(2)
    sys.exit(f"error: X API call failed for {path}: {(p.stderr or p.stdout)[:200]}")


def _parse_time(s):
    # "Tue Jan 24 20:14:18 +0000 2023"
    try:
        return datetime.strptime(s, "%a %b %d %H:%M:%S %z %Y")
    except Exception:
        return None


def _q(s):
    import urllib.parse
    return urllib.parse.quote(s, safe="")


def fetch_user_tweets(handle, since_hours=None, max_n=20):
    out = _get(f"/twitter/user/tweets?userName={_q(handle)}")
    tweets = out.get("tweets", []) if isinstance(out, dict) else []
    rows = []
    cutoff = datetime.now(timezone.utc) - timedelta(hours=since_hours) if since_hours else None
    for t in tweets:
        if t.get("isReply"):
            continue
        dt = _parse_time(t.get("createdAt", ""))
        if cutoff and dt and dt < cutoff:
            continue
        rows.append({
            "handle": handle, "text": t.get("text", ""), "url": t.get("url"),
            "created": t.get("createdAt"), "dt": dt.isoformat() if dt else None,
            "likes": t.get("likeCount", 0), "retweets": t.get("retweetCount", 0),
            "views": t.get("viewCount", 0),
        })
    rows.sort(key=lambda r: r["dt"] or "", reverse=True)
    return rows[:max_n]


def load_accounts(path):
    handles = []
    if not os.path.isfile(path):
        return handles
    for line in open(path):
        line = line.strip()
        # take @handles from a markdown list/table: lines containing @name
        if line.startswith("#") or not line:
            continue
        for tok in line.replace("|", " ").replace(",", " ").split():
            if tok.startswith("@") and len(tok) > 1:
                h = tok[1:].strip("`*_)(")
                if h and h not in handles:
                    handles.append(h)
    return handles


def cmd_monitor(args):
    handles = load_accounts(args.accounts_file)
    if not handles:
        sys.exit(f"error: no @handles found in {args.accounts_file}")
    allrows = []
    for h in handles:
        try:
            rows = fetch_user_tweets(h, since_hours=args.since_hours, max_n=args.max_per)
        except SystemExit:
            print(f"warn: failed {h}", file=sys.stderr); continue
        allrows.extend([r for r in rows if r["likes"] >= args.min_likes])
        time.sleep(0.2)
    allrows.sort(key=lambda r: r["likes"], reverse=True)
    if args.json:
        print(json.dumps(allrows, indent=2)); return
    print(f"# X monitor — {len(handles)} accounts, last {args.since_hours}h, >= {args.min_likes} likes\n")
    for r in allrows:
        print(f"@{r['handle']} · {r['likes']}❤ {r['retweets']}🔁 · {r['created']}\n  {r['text'][:240]}\n  {r['url']}\n")


def cmd_discover(args):
    """Find accounts that many of our trusted seeds follow but we don't yet — for the
    living watch-list. Traverses /user/following of seed accounts and ranks by overlap."""
    current = set(h.lower() for h in load_accounts(args.accounts_file))
    seeds = [s.strip().lstrip("@") for s in args.seeds.split(",")] if args.seeds else list(current)[: args.max_seeds]
    tally = {}  # handle -> {count, name, followers, desc}
    for s in seeds:
        out = _get(f"/twitter/user/following?userName={_q(s)}")
        for u in (out.get("following", []) if isinstance(out, dict) else []):
            h = (u.get("userName") or "").lower()
            if not h or h in current:
                continue
            e = tally.setdefault(h, {"count": 0, "name": u.get("name"),
                                     "followers": u.get("followers") or 0,
                                     "desc": (u.get("description") or "")})
            e["count"] += 1
        time.sleep(0.2)
    cand = [(h, v) for h, v in tally.items()
            if v["count"] >= args.min_overlap and (v["followers"] or 0) >= args.min_followers]
    cand.sort(key=lambda kv: (kv[1]["count"], kv[1]["followers"]), reverse=True)
    cand = cand[: args.top]
    if args.json:
        print(json.dumps([{"handle": h, **v} for h, v in cand], indent=2)); return
    print(f"# Discover — {len(seeds)} seeds → {len(cand)} new candidates "
          f"(followed by >= {args.min_overlap} seeds, >= {args.min_followers} followers)\n")
    for h, v in cand:
        print(f"@{h}  ·  {v['count']} of our seeds follow  ·  {v['followers']} followers  ·  {v['name']}\n  {v['desc'][:160]}\n")
    print("Review these; add the genuinely relevant ones (AI / agents / automation / "
          "cell biology / bioimaging / omics) to x-accounts.md after `lab-x.py info <h>`.")


def main():
    ap = argparse.ArgumentParser(prog="lab-x")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pi = sub.add_parser("info"); pi.add_argument("handle")
    pu = sub.add_parser("user"); pu.add_argument("handle")
    pu.add_argument("--max", type=int, default=20); pu.add_argument("--since-hours", type=float)
    pu.add_argument("--json", action="store_true")
    ps = sub.add_parser("search"); ps.add_argument("query")
    ps.add_argument("--max", type=int, default=20); ps.add_argument("--json", action="store_true")
    pm = sub.add_parser("monitor")
    pm.add_argument("--accounts-file", default=DEFAULT_ACCOUNTS)
    pm.add_argument("--since-hours", type=float, default=24)
    pm.add_argument("--min-likes", type=int, default=20)
    pm.add_argument("--max-per", type=int, default=10)
    pm.add_argument("--json", action="store_true")
    pdsc = sub.add_parser("discover", help="find new accounts our seeds follow (living watch-list)")
    pdsc.add_argument("--accounts-file", default=DEFAULT_ACCOUNTS)
    pdsc.add_argument("--seeds", help="comma handles to traverse (default: current watch-list)")
    pdsc.add_argument("--max-seeds", type=int, default=20)
    pdsc.add_argument("--min-overlap", type=int, default=3)
    pdsc.add_argument("--min-followers", type=int, default=3000)
    pdsc.add_argument("--top", type=int, default=30)
    pdsc.add_argument("--json", action="store_true")
    a = ap.parse_args()

    if a.cmd == "info":
        out = _get(f"/twitter/user/info?userName={_q(a.handle)}")
        u = out.get("data") or out
        name = u.get("name") or u.get("userName")
        followers = u.get("followers") or u.get("followersCount") or u.get("followers_count")
        print(f"@{a.handle}: {name} · followers={followers}\n  {(u.get('description') or '')[:200]}")
    elif a.cmd == "user":
        rows = fetch_user_tweets(a.handle, since_hours=a.since_hours, max_n=a.max)
        if a.json:
            print(json.dumps(rows, indent=2))
        else:
            for r in rows:
                print(f"@{r['handle']} · {r['likes']}❤ · {r['created']}\n  {r['text'][:240]}\n  {r['url']}\n")
    elif a.cmd == "search":
        out = _get(f"/twitter/tweet/advanced_search?q={_q(a.query)}&product=Latest")
        tweets = out.get("tweets", []) if isinstance(out, dict) else []
        if a.json:
            print(json.dumps(tweets[:a.max], indent=2))
        else:
            for t in tweets[:a.max]:
                au = (t.get("author") or {}).get("userName", "?")
                print(f"@{au} · {t.get('likeCount',0)}❤ · {t.get('createdAt')}\n  {t.get('text','')[:240]}\n  {t.get('url')}\n")
    elif a.cmd == "monitor":
        cmd_monitor(a)
    elif a.cmd == "discover":
        cmd_discover(a)


if __name__ == "__main__":
    main()
