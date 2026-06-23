#!/usr/bin/env bash
# Reproducible build environment for the aicell.io site automations.
# Source this (`. scripts/setup-build-env.sh`) at the start of any nightly/weekly
# automation so it has the correct env regardless of which fresh agent/shell runs it.
#
# It makes Hugo (extended 0.101.0, == CI) and Go available at STABLE paths
# (not ephemeral /tmp), exports the cache/env vars the build needs, and loads
# optional secrets (e.g. SLACK_WEBHOOK_URL) from outside the repo.
#
# Idempotent: safe to source on every run. Prints what it resolved.

set -u
AICELL_BUILD_HOME="${AICELL_BUILD_HOME:-$HOME/.cache/aicell-build}"
HUGO_VERSION="0.101.0"          # must match .github/workflows/build.yml
GO_VERSION="1.21.6"
mkdir -p "$AICELL_BUILD_HOME"

_arch() { case "$(uname -m)" in arm64|aarch64) echo arm64;; *) echo amd64;; esac; }

# --- Hugo (extended) -------------------------------------------------------
HUGO_BIN="$AICELL_BUILD_HOME/hugo"
if [ ! -x "$HUGO_BIN" ]; then
  if [ -x /tmp/hugo ] && /tmp/hugo version 2>/dev/null | grep -q "v${HUGO_VERSION}.*extended"; then
    cp /tmp/hugo "$HUGO_BIN"                       # reuse already-downloaded binary
  else
    a=$(_arch); [ "$a" = arm64 ] && ha="ARM64" || ha="64bit"
    url="https://github.com/gohugoio/hugo/releases/download/v${HUGO_VERSION}/hugo_extended_${HUGO_VERSION}_macOS-${ha}.tar.gz"
    curl -fsSL -o "$AICELL_BUILD_HOME/hugo.tgz" "$url" \
      && tar xzf "$AICELL_BUILD_HOME/hugo.tgz" -C "$AICELL_BUILD_HOME" hugo \
      || echo "setup-build-env: WARN could not fetch Hugo $HUGO_VERSION ($url)"
  fi
fi

# --- Go (needed for Hugo Modules to fetch the theme) -----------------------
GO_ROOT="$AICELL_BUILD_HOME/go"
if [ ! -x "$GO_ROOT/bin/go" ]; then
  if [ -x /tmp/go/bin/go ]; then
    cp -R /tmp/go "$GO_ROOT"
  else
    url="https://go.dev/dl/go${GO_VERSION}.darwin-$(_arch).tar.gz"
    curl -fsSL -o "$AICELL_BUILD_HOME/go.tgz" "$url" \
      && tar xzf "$AICELL_BUILD_HOME/go.tgz" -C "$AICELL_BUILD_HOME" \
      || echo "setup-build-env: WARN could not fetch Go $GO_VERSION ($url)"
  fi
fi

# --- Export the env the build relies on ------------------------------------
export HUGO_BIN
export PATH="$AICELL_BUILD_HOME:$GO_ROOT/bin:$PATH"
export GOPATH="$AICELL_BUILD_HOME/gopath"
export GOCACHE="$AICELL_BUILD_HOME/gocache"
export HUGO_CACHEDIR="$AICELL_BUILD_HOME/hugo_cache"
mkdir -p "$GOPATH" "$GOCACHE" "$HUGO_CACHEDIR"

# --- Optional secrets (never committed) ------------------------------------
# Put SLACK_WEBHOOK_URL=... (or SLACK_BOT_TOKEN=...) in ~/.svamp/aicell-newsletter.env
[ -f "$HOME/.svamp/aicell-newsletter.env" ] && set -a && . "$HOME/.svamp/aicell-newsletter.env" && set +a

echo "setup-build-env: hugo=$( ($HUGO_BIN version 2>/dev/null || echo missing) | head -c 60 )"
echo "setup-build-env: go=$( (go version 2>/dev/null || echo missing) )"
echo "setup-build-env: slack=$([ -n "${SLACK_WEBHOOK_URL:-}${SLACK_BOT_TOKEN:-}" ] && echo configured || echo not-set)"
# IMPORTANT: build with "$HUGO_BIN --gc --minify"; do NOT run 'hugo mod get'
# (it upgrades the theme to v5.9.0 which breaks Hugo 0.101.0). Theme is pinned in go.mod.