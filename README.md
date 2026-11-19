# Portable Agent Harness — documentation-first Godot profile

A **Git-native Markdown template** for AI agents to recover a project's work across sessions, models, and computers. **This is not a Godot game.** No Python, SQLite, custom task database, server or executable context engine is required.

## When you ask “What were we working on?”

1. The agent starts at [AGENTS.md](AGENTS.md), then reads the short [STATUS](.agent-docs/status.md).
2. It follows the linked [OpenSpec change](openspec/changes/) and relevant spec, decisions and handoff; compares notes with **real source, Git diff/log and test evidence**.
3. It opens only relevant [rules](.agent-docs/index.md) and optional [Skills](.agents/skills/), identifies verified/unverified work and the next concrete action.
4. At a pause it updates the canonical task checklist, STATUS and meaningful handoff; **commits and pushes** non-secret context and source for another machine.

| Concern | Source of truth |
| --- | --- |
| Agent instructions | `AGENTS.md` |
| Current state / next action | `.agent-docs/status.md` |
| Approved requirements and change tasks | `openspec/specs/`, `openspec/changes/` |
| Decisions, research and handoffs | `.agent-docs/decisions/`, `research/`, `worklog/` |
| What actually works | Source, real tests and captured evidence |
| Provider-specific extras | `.claude/agents/`, `CLAUDE.md`, `GEMINI.md` |

See [quickstart](docs/quickstart.md), [architecture](docs/architecture.md), [adoption](docs/adopting-existing-project.md), [Godot profile](docs/godot-profile.md) and [verification limits](docs/verification.md). The official OpenSpec CLI is **optional** for spec authoring; the Markdown remains readable without it.

**Limits:** Git cannot transfer uncommitted changes, hidden model reasoning, ignored assets, credentials or runtime state. A status file can be stale. No generic template self-test proves actual game behavior or token savings. [Evaluation protocol](docs/evaluation.md).

MIT: [LICENSE](LICENSE).
