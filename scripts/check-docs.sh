#!/usr/bin/env bash
# Offline documentation structure checks, NOT semantic code review or a game test.
set -euo pipefail
cd "$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
errors="$(mktemp)"
trap 'rm -f "$errors"' EXIT
fail() { printf 'ERROR: %s\n' "$*" >&2; printf '%s\n' "$*" >> "$errors"; }

# Keep current-work pointers AND long-lived topic navigation discoverable.
for f in AGENTS.md README.md .agent-docs/index.md .agent-docs/status.md \
  .agent-docs/topics.md .agent-docs/rules/workflow.md \
  .agent-docs/rules/specification.md .agent-docs/rules/development.md \
  .agent-docs/rules/documentation.md .agents/skills/context-recovery/SKILL.md \
  docs/knowledge-reuse.md docs/task-lifecycle.md docs/agent-adapters.md \
  CLAUDE.md GEMINI.md openspec/config.yaml; do
  [[ -f "$f" ]] || fail "Missing required file: $f"
done

# Only the removed Python harness is disallowed. Actual game scripts/ and tests/ are welcome.
for f in harness/cli.py harness/index.py scripts/harness.py \
  .harness/context-routes.json .harness/authority-map.json project.harness.json; do
  [[ ! -e "$f" ]] || fail "Removed PAH engine file still exists: $f"
done

# Validate instruction imports: a prose instruction to read AGENTS.md is NOT an import.
if [[ -f CLAUDE.md ]] && ! grep -Fxq '@AGENTS.md' CLAUDE.md; then
  fail 'CLAUDE.md must contain the @AGENTS.md import for Claude Code'
fi
if [[ -f GEMINI.md ]] && ! grep -Fxq '@./AGENTS.md' GEMINI.md; then
  fail 'GEMINI.md must contain the @./AGENTS.md import for Gemini CLI'
fi

# The .agents/skills files are canonical; .claude/skills are portability wrappers.
# Check that every shared skill has exactly one discoverable Claude adapter and
# that wrappers point to the correct source without stale trigger descriptions.
for source in .agents/skills/*/SKILL.md; do
  [[ -f "$source" ]] || continue
  name="${source#.agents/skills/}"
  name="${name%/SKILL.md}"
  adapter=".claude/skills/$name/SKILL.md"
  [[ -f "$adapter" ]] || { fail "Missing Claude/Grok adapter: $adapter"; continue; }
  expected_desc="$(sed -n 's/^description: //p' "$source" | head -n 1)"
  adapter_desc="$(sed -n 's/^description: //p' "$adapter" | head -n 1)"
  grep -Fxq "name: $name" "$source" || fail "Canonical skill name mismatch: $source"
  grep -Fxq "name: $name" "$adapter" || fail "Adapter skill name mismatch: $adapter"
  [[ -n "$expected_desc" && "$expected_desc" == "$adapter_desc" ]] || fail "Skill description mismatch: $adapter"
  grep -Fq "(../../../.agents/skills/$name/SKILL.md)" "$adapter" || fail "Adapter points to wrong source: $adapter"
done
for adapter in .claude/skills/*/SKILL.md; do
  [[ -f "$adapter" ]] || continue
  name="${adapter#.claude/skills/}"
  name="${name%/SKILL.md}"
  [[ -f ".agents/skills/$name/SKILL.md" ]] || fail "Orphan Claude adapter: $adapter"
done

# Common relative inline Markdown links, including the topic map's links.
# Not a full CommonMark parser: reference links, link anchors and semantics aren't validated.
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
printf 'Documentation check PASS (required files, local links, STATUS pointers)\n'
