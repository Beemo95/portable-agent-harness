#!/usr/bin/env bash
# Negative checks for broken Markdown/STATUS/topic pointers; Python not required.
set -euo pipefail
root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/repo"
(cd "$root" && tar --exclude=.git -cf - .) | tar -xf - -C "$tmp/repo"
check() { (cd "$tmp/repo" && bash scripts/check-docs.sh) >/dev/null 2>&1; }

check || { echo 'FAIL: valid baseline documentation rejected' >&2; exit 1; }
mkdir -p "$tmp/repo/tests" "$tmp/repo/scripts"
check || { echo 'FAIL: tests/ and scripts/ must be allowed' >&2; exit 1; }

printf '\n[broken](missing-expected-target.md)\n' >> "$tmp/repo/docs/quickstart.md"
if check; then echo 'FAIL: broken link was not detected' >&2; exit 1; fi
cp "$root/docs/quickstart.md" "$tmp/repo/docs/quickstart.md"

sed -i 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/not-a-real-change/@' "$tmp/repo/.agent-docs/status.md"
if check; then echo 'FAIL: missing OpenSpec change was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"

printf '\n[stale topic](nonexistent-architecture-reference.md)\n' >> "$tmp/repo/.agent-docs/topics.md"
if check; then echo 'FAIL: missing topic reference was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/topics.md" "$tmp/repo/.agent-docs/topics.md"

rm "$tmp/repo/.agent-docs/topics.md"
if check; then echo 'FAIL: required topic index missing was not detected' >&2; exit 1; fi

printf 'Documentation negative tests PASS (links, active change, topic map, required files)\n'
