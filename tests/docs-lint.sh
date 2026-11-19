#!/usr/bin/env bash
# Negative tests: broken Markdown links, broken STATUS pointers, valid scripts/ and tests/.
set -euo pipefail
root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/repo"
(cd "$root" && tar --exclude=.git -cf - .) | tar -xf - -C "$tmp/repo"
check() { (cd "$tmp/repo" && bash scripts/check-docs.sh) >/dev/null 2>&1; }
check || { echo 'FAIL: baseline documentation' >&2; exit 1; }
mkdir -p "$tmp/repo/tests" "$tmp/repo/scripts"
check || { echo 'FAIL: scripts and tests must be allowed' >&2; exit 1; }
printf '\n[broken](missing-expected-target.md)\n' >> "$tmp/repo/docs/quickstart.md"
if check; then echo 'FAIL: broken link not detected' >&2; exit 1; fi
cp "$root/docs/quickstart.md" "$tmp/repo/docs/quickstart.md"
sed -i 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/not-a-real-change/@' "$tmp/repo/.agent-docs/status.md"
if check; then echo 'FAIL: missing change not detected' >&2; exit 1; fi
printf 'Documentation negative tests PASS\n'
