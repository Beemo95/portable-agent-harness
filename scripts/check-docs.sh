#!/usr/bin/env bash
# Offline checks, not a Markdown parser or proof that source and STATUS agree.
set -euo pipefail
cd "$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
errors="$(mktemp)"
trap 'rm -f "$errors"' EXIT
fail() { printf 'ERROR: %s\n' "$*" >&2; printf '%s\n' "$*" >> "$errors"; }
for f in AGENTS.md README.md .agent-docs/index.md .agent-docs/status.md .agent-docs/rules/workflow.md .agent-docs/rules/documentation.md .agents/skills/context-recovery/SKILL.md openspec/config.yaml; do
  [[ -f "$f" ]] || fail "Missing required file: $f"
done
# Do NOT forbid tests/ or scripts/: a game may need both.
for f in harness/cli.py harness/index.py scripts/harness.py .harness/context-routes.json .harness/authority-map.json project.harness.json; do
  [[ ! -e "$f" ]] || fail "Removed PAH engine file still exists: $f"
done
# Common inline [label](relative/path#anchor) links; remote/reference-style links not checked.
while IFS= read -r file; do
  while IFS= read -r link; do
    target="$(printf '%s\n' "$link" | sed -e 's/^](//' -e 's/)$//' -e 's/[?#].*$//')"
    case "$target" in
      ''|http://*|https://*|mailto:*|tel:*|//*|/*) continue ;;
    esac
    [[ -e "$(dirname "$file")/$target" ]] || fail "Broken Markdown link: $file -> $target"
  done < <(grep -oE '\]\([^)]*\)' "$file" || true)
done < <(find . \( -name .git -o -name .godot -o -name node_modules -o -name .venv \) -prune -o -type f -name '*.md' -print)
status='.agent-docs/status.md'
if [[ -f "$status" ]]; then
  for field in 'Active OpenSpec changes' 'Next action' 'Last updated' 'Verification'; do
    grep -Fq -- "**$field:**" "$status" || fail "STATUS missing: $field"
  done
  active="$(sed -n 's/^- \*\*Active OpenSpec changes:\*\* //p' "$status" | head -n 1)"
  if [[ -z "$active" ]]; then
    fail 'STATUS active changes must be none or exact OpenSpec paths'
  elif [[ "$active" != 'none' ]]; then
    refs="$(printf '%s\n' "$active" | grep -oE 'openspec/changes/[A-Za-z0-9._-]+/?' || true)"
    [[ -n "$refs" ]] || fail "Missing concrete OpenSpec reference: $active"
    if [[ -n "$refs" ]]; then
      while IFS= read -r ref; do
        [[ -d "$ref" ]] || fail "STATUS points to missing change: $ref"
      done <<< "$refs"
    fi
  fi
  if ! grep -Fq 'TEMPLATE STATE' "$status"; then
    grep -Eq '^- \*\*Last updated:\*\* [0-9]{4}-[0-9]{2}-[0-9]{2}' "$status" || fail 'Project STATUS needs dated Last updated'
    grep -Eq '^- \*\*Next action:\*\* .+' "$status" || fail 'Project STATUS needs concrete Next action'
  fi
fi
if [[ -s "$errors" ]]; then
  printf 'Documentation check FAILED: %s issue(s)\n' "$(wc -l < "$errors" | tr -d ' ')" >&2
  exit 1
fi
printf 'Documentation check PASS (files, links, STATUS pointers)\n'
