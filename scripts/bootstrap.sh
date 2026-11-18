#!/usr/bin/env sh
# Safe offline preflight. Does not install packages or execute unreviewed commands.
set -eu
HERE=$(CDPATH= cd -- "$(dirname -- "$0")" && pwd)
ROOT=$(CDPATH= cd -- "$HERE/.." && pwd)
printf 'Project: %s\n' "$ROOT"
if command -v git >/dev/null 2>&1; then
  printf 'Git: %s\n' "$(git --version)"
else
  printf 'BLOCKED: Git is missing; install Git using your OS package manager.\n'
fi
if command -v python3 >/dev/null 2>&1; then
  python3 "$HERE/harness.py" doctor
else
  printf 'BLOCKED: Python >=3.10 is required for the harness CLI.\n'
  printf 'Install Python using your OS package manager; then run python3 scripts/harness.py doctor.\n'
  exit 2
fi
