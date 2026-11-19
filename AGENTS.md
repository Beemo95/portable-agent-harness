# Godot-first project harness — agent entry

This is a **documentation template**, not a playable Godot game. The actual project source, Markdown records and Git history are shared memory. No Python task CLI, SQLite index or custom task database is needed. This file routes context; **do not load every document**.

## Start or resume
1. Identify the request. For “Where did we stop?” / “Continue”, read [STATUS](.agent-docs/status.md) first and follow its active OpenSpec change/handoff. Compare with `git status`, recent commits, actual source and test evidence. If there is no active task or STATUS is stale, say so; never invent completion.
2. Read [workflow](.agent-docs/rules/workflow.md) and use the [knowledge map](.agent-docs/index.md) for **only the task-specific** rules, Skills, decisions and source.
3. Treat `openspec/specs/` as approved requirements and `openspec/changes/` as the canonical change plan/tasks. Do not duplicate checklists in a second task system. Checked tasks aren't independent QA proof.
4. Inspect real `project.godot`/scenes/assets and engine version when working in an adopted game. The template has no game or runnable tests.

## During work / handoff
- Make small scoped edits; preserve original acceptance and record actual verification and unverified visual/device gaps.
- Update OpenSpec `tasks.md` only for implemented items; keep STATUS short: active change, verified facts, blockers, next action and related revision. Record meaningful ADR/worklog findings, not every command.
- For substantial handoffs use [handoff template](.agent-docs/templates/handoff.md). Commit/push non-secret source and docs for cross-PC recovery; uncommitted/ignored work cannot be recovered by cloning.
- Review untrusted commands or dependencies; don't reveal credentials or claim tests you did not run.

## Task-specific routing
| Work | Rule | Optional Skill |
| --- | --- | --- |
| Gameplay / new specs | [specification](.agent-docs/rules/specification.md) | `godot-game-spec` |
| GDScript / scene | [development](.agent-docs/rules/development.md) | `godot-feature-implementation` |
| Art / pixel / UI | [design-art](.agent-docs/rules/design-art.md) | `godot-art-pipeline` |
| Research | [research](.agent-docs/rules/research.md) | `research-and-evidence` |
| Bugs / performance | [debugging](.agent-docs/rules/debugging.md) | `godot-debugging` |
| QA / release | [verification](.agent-docs/rules/verification.md) | `godot-qa-playtest` |
| Recovery / pause | [documentation](.agent-docs/rules/documentation.md) | `context-recovery` / `game-work-handoff` |

[Skills](.agents/skills/) are optional and discovery depends on the actual host. [Specialist roles](.agent-docs/agents/index.md) are briefs; [Claude-only adapters](.claude/agents/) do not configure other tools. Project intent: [product](.agent-docs/product.md); architecture: [architecture](.agent-docs/architecture.md).
