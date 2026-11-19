# Minimum viable stack

| Concern | Authority | Optional helper |
| --- | --- | --- |
| Source and history | Git + real project files | Native Git/search tools |
| Current work | `.agent-docs/status.md` | Agent's built-in file reader |
| Requirements and tasks | `openspec/specs/` + `openspec/changes/` | Official [OpenSpec](https://github.com/Fission-AI/OpenSpec) CLI |
| Decisions/evidence/handoff | `.agent-docs/decisions/`, `research/`, `worklog/` | [Agent Skills](https://agentskills.io/specification) |
| Testing | Actual game/toolchain/CI/device | Godot, existing test runner |
| Instructions | `AGENTS.md` | Host-specific pointer files |

Default architecture requires **no Python, SQLite, external database, homemade context engine, or MCP server**. Optional OpenSpec authoring CLI should follow its own current documentation; review any generated skill/config changes to avoid overwrites. Spec Kit is an alternative, not a second task tracker. Add Serena/ripgrep/semantic search only if real recall failures justify it.

This is a template, not a measured best-performing agent harness.
