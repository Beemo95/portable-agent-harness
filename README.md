# Portable Agent Harness — documentation-first, Godot-oriented

A small **Git-native Markdown profile** so a new AI agent can ask “what was done, what is left, what was tested?” and navigate the same code, specs and decisions without a custom Python agent server, SQLite database or generated Context Packets.

> **Template, not a game.** The included STATUS says no game project or tests were inspected. It must be populated from an **actual** Godot repository before claiming any real-game continuity.

## How a new session recovers context
1. [AGENTS.md](AGENTS.md) routes into the short [STATUS](.agent-docs/status.md).
2. The agent follows the **active OpenSpec change**, related handoff/ADRs, then checks real Git/source, tests and affected scenes.
3. The next unfinished work slice is found in the **one canonical `tasks.md`**; only relevant [rules](.agent-docs/index.md) and [Skills](.agents/skills/) are opened.
4. Decisions, implemented slices, failures and impending context switches trigger a short STATUS update; non-secret source/context is committed and pushed for cross-PC handoff.

| Concern | Home |
| --- | --- |
| Entry / task-specific instructions | `AGENTS.md`, `.agent-docs/rules/` |
| Snapshot and next action | `.agent-docs/status.md` |
| Requirements, feature proposal/design/tasks | `openspec/specs/`, `openspec/changes/` |
| Architectural decisions / research / handoff | `.agent-docs/decisions/`, `research/`, `worklog/` |
| Verification | Actual Godot/project test commands and observed evidence |
| Optional roles and workflows | `.agent-docs/agents/`, `.agents/skills/` |

## Documentation safety checks (Bash, not a Python harness)
```sh
bash scripts/check-docs.sh
bash tests/docs-lint.sh
```

GitHub Actions runs these to catch missing required docs, common broken relative Markdown links, and a STATUS pointer to a missing OpenSpec change. **`scripts/` and `tests/` are allowed**, including real game scripts/tests. These checks do **not** validate semantic accuracy or run the game.

## Adoption & optional upstream workflow
- [Quickstart](docs/quickstart.md) and [safe adoption into a real game](docs/adopting-existing-project.md)
- [Official OpenSpec workflows/setup](docs/openspec-workflow.md) — separately installed only if wanted; do not copy or reimplement its generated Skills
- [Agent adapter limits](docs/agent-adapters.md) and [Godot profile](docs/godot-profile.md)
- [Recovery evaluation](docs/evaluation.md), [verification boundaries](docs/verification.md) and [research background](docs/research-basis.md)

The `main` branch contains the latest docs. Older feature branches may still contain the obsolete Python architecture; don't treat them as current without reviewing differences. Git cannot transfer uncommitted edits, secrets, ignored assets or hidden model state. Actual Codex/Hermes/Grok end-to-end cold-start tests remain to be run on a real game.

MIT: [LICENSE](LICENSE).
