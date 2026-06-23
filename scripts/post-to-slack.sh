#!/usr/bin/env bash
# Post a message to Slack #general for the lab newsletter pipeline.
# Usage: scripts/post-to-slack.sh "message text"
# Requires SLACK_WEBHOOK_URL (Incoming Webhook) or SLACK_BOT_TOKEN (+ SLACK_CHANNEL, default #general).
# Exits 0 and SKIPS gracefully (no failure) when no credential is configured.
set -euo pipefail
msg="${1:?usage: post-to-slack.sh \"message\"}"
if [[ -n "${SLACK_WEBHOOK_URL:-}" ]]; then
  curl -fsS -X POST -H 'Content-type: application/json' \
    --data "$(printf '{"text":%s}' "$(printf '%s' "$msg" | python3 -c 'import json,sys;print(json.dumps(sys.stdin.read()))')")" \
    "$SLACK_WEBHOOK_URL" >/dev/null && echo "slack: posted via webhook"
elif [[ -n "${SLACK_BOT_TOKEN:-}" ]]; then
  curl -fsS -X POST https://slack.com/api/chat.postMessage \
    -H "Authorization: Bearer $SLACK_BOT_TOKEN" -H 'Content-type: application/json; charset=utf-8' \
    --data "$(python3 -c 'import json,os,sys;print(json.dumps({"channel":os.environ.get("SLACK_CHANNEL","#general"),"text":sys.argv[1]}))' "$msg")" \
    >/dev/null && echo "slack: posted via bot token"
else
  echo "slack: SKIPPED (no SLACK_WEBHOOK_URL or SLACK_BOT_TOKEN set)"; exit 0
fi
