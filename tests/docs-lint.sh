#!/usr/bin/env bash
# Negative checks for broken Markdown/STATUS/topic pointers; Python not required.
set -euo pipefail
root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
mkdir -p "$tmp/repo"
(cd "$root" && tar --exclude=.git -cf - .) | tar -xf - -C "$tmp/repo"
check() { (cd "$tmp/repo" && bash scripts/check-docs.sh) >/dev/null 2>&1; }
# Portable GNU/BSD sed replacement: macOS requires different sed -i syntax.
rewrite() {
  local file="$1" expr="$2" temp
  temp="$(mktemp "$tmp/rewrite.XXXXXX")"
  sed "$expr" "$file" > "$temp"
  cat "$temp" > "$file"
  rm -f "$temp"
}


check || { echo 'FAIL: valid baseline documentation rejected' >&2; exit 1; }

# Positive cases prove that the validator does not reject valid real-project states.
mkdir -p "$tmp/repo/openspec/changes/valid-feature"
printf '# Proposal\n\nAdd a small safe feature.\n' > "$tmp/repo/openspec/changes/valid-feature/proposal.md"
rewrite "$tmp/repo/.agent-docs/status.md" 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/valid-feature/@'
check || { echo 'FAIL: valid OpenSpec change rejected' >&2; exit 1; }
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"

touch "$tmp/repo/project.godot"
rewrite "$tmp/repo/.agent-docs/status.md" 's/TEMPLATE STATE/PROJECT STATE/'
rewrite "$tmp/repo/.agent-docs/status.md" 's/not inspected; no game included/Godot 4.7.2 confirmed for this test fixture/'
rewrite "$tmp/repo/.agent-docs/status.md" 's/not initialized for a game/2026-11-19/'
check || { echo 'FAIL: initialized game STATUS rejected' >&2; exit 1; }
rm "$tmp/repo/project.godot"
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"
mkdir -p "$tmp/repo/tests" "$tmp/repo/scripts"
check || { echo 'FAIL: tests/ and scripts/ must be allowed' >&2; exit 1; }

printf '\n[broken](missing-expected-target.md)\n' >> "$tmp/repo/docs/quickstart.md"
if check; then echo 'FAIL: broken link was not detected' >&2; exit 1; fi
cp "$root/docs/quickstart.md" "$tmp/repo/docs/quickstart.md"

rewrite "$tmp/repo/.agent-docs/status.md" 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/not-a-real-change/@'
if check; then echo 'FAIL: missing OpenSpec change was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"

printf '\n[stale topic](nonexistent-architecture-reference.md)\n' >> "$tmp/repo/.agent-docs/topics.md"
if check; then echo 'FAIL: missing topic reference was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/topics.md" "$tmp/repo/.agent-docs/topics.md"

rm "$tmp/repo/.agent-docs/topics.md"
if check; then echo 'FAIL: required topic index missing was not detected' >&2; exit 1; fi

# Regression: incorrect imports must fail, not silently load a shortened pointer.
printf 'Read AGENTS.md\n' > "$tmp/repo/CLAUDE.md"
if check; then echo 'FAIL: invalid Claude import was not detected' >&2; exit 1; fi
cp "$root/CLAUDE.md" "$tmp/repo/CLAUDE.md"

printf 'Read AGENTS.md\n' > "$tmp/repo/GEMINI.md"
if check; then echo 'FAIL: invalid Gemini import was not detected' >&2; exit 1; fi
cp "$root/GEMINI.md" "$tmp/repo/GEMINI.md"

# Every canonical skill must have a discoverable Claude/Grok adapter.
rm "$tmp/repo/.claude/skills/feature-work/SKILL.md"
if check; then echo 'FAIL: missing adapter was not detected' >&2; exit 1; fi
mkdir -p "$tmp/repo/.claude/skills/feature-work"
cp "$root/.claude/skills/feature-work/SKILL.md" "$tmp/repo/.claude/skills/feature-work/SKILL.md"

rewrite "$tmp/repo/.claude/skills/feature-work/SKILL.md" 's/^description: .*/description: intentionally stale trigger/'
if check; then echo 'FAIL: stale adapter metadata was not detected' >&2; exit 1; fi
cp "$root/.claude/skills/feature-work/SKILL.md" "$tmp/repo/.claude/skills/feature-work/SKILL.md"

touch "$tmp/repo/project.godot"
if check; then echo 'FAIL: real game accepted with stale template STATUS' >&2; exit 1; fi
rm "$tmp/repo/project.godot"

mkdir -p "$tmp/repo/openspec/changes/empty-feature"
rewrite "$tmp/repo/.agent-docs/status.md" 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/empty-feature/@'
if check; then echo 'FAIL: empty active change was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"

mkdir -p "$tmp/repo/openspec/changes/archive"
rewrite "$tmp/repo/.agent-docs/status.md" 's@\*\*Active OpenSpec changes:\*\* none@**Active OpenSpec changes:** openspec/changes/archive/@'
if check; then echo 'FAIL: archived task recorded as active was not detected' >&2; exit 1; fi
cp "$root/.agent-docs/status.md" "$tmp/repo/.agent-docs/status.md"

rewrite "$tmp/repo/openspec/config.yaml" 's/^schema: spec-driven/schema: invalid-schema/'
if check; then echo 'FAIL: invalid OpenSpec schema was not detected' >&2; exit 1; fi
cp "$root/openspec/config.yaml" "$tmp/repo/openspec/config.yaml"

rewrite "$tmp/repo/docs/source-audit.md" 's/^- \*\*Next review by:\*\* .*/- **Next review by:** 2000-01-01/'
if check; then echo 'FAIL: overdue source review was not detected' >&2; exit 1; fi
cp "$root/docs/source-audit.md" "$tmp/repo/docs/source-audit.md"

printf 'Documentation negative tests PASS (links, active state, schema, import adapters, source freshness)\n'
