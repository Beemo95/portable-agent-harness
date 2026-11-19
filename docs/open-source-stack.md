# Minimal project stack (not a new agent runtime)

| Responsibility | Canonical authority | Optional helper |
| --- | --- | --- |
| Current behavior/history | Actual code and Git | Native repository search |
| Short current status/next action | `.agent-docs/status.md` | Context recovery Skill |
| Approved requirements and tasks | `openspec/specs/`, `openspec/changes/` | Official [OpenSpec](https://github.com/Fission-AI/OpenSpec) CLI and generated Skills |
| Decisions/research/handoff | `.agent-docs/decisions/`, `research/`, `worklog/` | Optional task-specific Skills |
| Actual correctness | Project tests, real Godot runtime/device QA | Existing test runner and game CI |
| Document structural integrity | Markdown/Git | `bash scripts/check-docs.sh` in this template |

Python CLI, SQLite FTS, separate task DB, bespoke context packet engine and mandatory SaaS APIs are absent. There is **no claim** that every host auto-discovers the same Skills. [OpenSpec setup](openspec-workflow.md) is optional; its current upstream profiles and generated tools should be checked before installing. Spec Kit is an alternative rather than a second tracker.

Add more tooling only after measuring actual cold-start/QA failure against [evaluation](evaluation.md).
