# Quickstart — no custom runtime

Core requirements: Git and an AI agent capable of reading project files. Godot is needed only to test a **real** Godot game. Python/SQLite/Node are **not** required for task recovery.

1. Clone/pull the game repository and open it in your agent.
2. Ask: “Read AGENTS.md. What was being done, what is verified, what is unfinished, and what next?”
3. The agent reads `.agent-docs/status.md`, follows its active OpenSpec change, inspects code and `git status` / `git log`, and distinguishes reported progress from observed facts.
4. Continue the smallest pending work; use matching rules/Skills selectively.
5. At a pause, update the single OpenSpec checklist, short STATUS and any meaningful handoff/decision; commit/push code and context.

Useful read-only inspections:

```sh
git status --short
git log -5 --oneline
git diff
find openspec/changes -type f
```

If no active change is recorded, **say so**. A clean clone cannot reconstruct unpushed changes, local processes or secrets. For new project setup see [adoption](adopting-existing-project.md).
