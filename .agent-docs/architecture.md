# Architecture — template state

This repository is **not a playable Godot project** and has **no executable harness control plane**. In an adopted game, replace these bullets with inspected engine, scene, resource, platform and toolchain facts.

- `AGENTS.md`: minimal agent entry/router.
- `.agent-docs/status.md`: current work pointer + verification gaps, blockers and next step.
- `openspec/specs/` / `openspec/changes/`: approved requirements, change design and single task checklist.
- `.agent-docs/rules/` / `agents/` / `.agents/skills/`: selective guidance and optional specialist workflows.
- `.agent-docs/decisions/`, `research/`, `worklog/`: durable rationale and meaningful handoff evidence.
- Git and real source: current observable state. Actual project tools/QA: verification.
- `.claude/agents/`, `CLAUDE.md` and `GEMINI.md`: optional host-specific adapters.

No `harness/` Python package, SQLite cache, `.harness/` task state, custom verifier or Context Packet generator. Native file/Git lookup and Markdown handoffs replace them. Git only transfers committed non-secret files.
