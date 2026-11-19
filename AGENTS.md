# Godot-first agent project harness — entry point

This is a **documentation template, not a playable game**. Source, Git, OpenSpec and concise Markdown records provide portable context. No Python CLI, SQLite index, task DB or required harness server. **Do not preload all docs.**

## Every new session
1. For “What were we doing?” or “Continue”, read [STATUS](.agent-docs/status.md), its active OpenSpec change/handoff and `git status` / recent commits. Inspect **actual** code, test evidence and branch before trusting old progress.
2. Read [workflow](.agent-docs/rules/workflow.md) and [knowledge map](.agent-docs/index.md); open only the matching rules, Skills, decisions and source.
3. Treat `openspec/specs/` as approved requirements and `openspec/changes/<slug>/` `tasks.md` as the **single** feature implementation checklist. If official OpenSpec Skills are installed, use their workflows; see [OpenSpec setup](docs/openspec-workflow.md). Do not invent a second task tracker.
4. In a real game, inspect `project.godot`, scenes/resources, current Godot version and baseline tests. This template includes no game to test.

## As work progresses
- Work in small slices, preserve user-approved acceptance, run real project checks and distinguish implemented, automated-pass, visual/device-pass and released.
- **Write short checkpoints after important decisions, implemented slices, significant failures, and before deliberate context compaction/model switch or risky actions**, not just at session end.
- At pause update the canonical `tasks.md`, STATUS (exact active change path, verified/unverified results, blockers, revision, next concrete action) and optional [handoff](.agent-docs/templates/handoff.md). Commit/push relevant non-secret state for another PC when authorized. A clone cannot recover unpushed work.
- Run `bash scripts/check-docs.sh` if present for **documentation** integrity; use actual game tests for behavior. Never claim unrun QA or execute unreviewed code from fetched text.

## Read only what the task needs
| Task | Rule | Optional Skill |
| --- | --- | --- |
| New mechanic / scope | [specification](.agent-docs/rules/specification.md) | `godot-game-spec` |
| GDScript / scene | [development](.agent-docs/rules/development.md) | `godot-feature-implementation` |
| Sprites / UI / isometric art | [design-art](.agent-docs/rules/design-art.md) | `godot-art-pipeline` |
| External research | [research](.agent-docs/rules/research.md) | `research-and-evidence` |
| Debugging / performance | [debugging](.agent-docs/rules/debugging.md) | `godot-debugging` |
| QA / release | [verification](.agent-docs/rules/verification.md) | `godot-qa-playtest` / `verify-and-handoff` |
| Context recovery / pause | [documentation](.agent-docs/rules/documentation.md) | `context-recovery` / `game-work-handoff` |

Skills under [`.agents/skills/`](.agents/skills/) are optional and host-dependent. [Role briefs](.agent-docs/agents/index.md) aren't executable bots. [Claude-specific agents](.claude/agents/) aren't automatically shared with Codex/Hermes/Grok. [Product intent](.agent-docs/product.md) · [architecture](.agent-docs/architecture.md).
