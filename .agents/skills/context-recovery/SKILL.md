---
name: context-recovery
description: Recover active work in a new session and retrieve relevant older domain knowledge even if the original task is closed.
---
# Context recovery — current status and older related knowledge

1. Read `AGENTS.md` and, when resuming, STATUS, `git status --short` and `git log -5 --oneline` in the **actual** project.
2. Follow linked active change/handoff for in-flight work. For a **new** request or a return to an old topic, inspect actual related code/tests, [topic map](../../../.agent-docs/topics.md), approved specs/architecture/ADRs, research and related Git history, even if STATUS now points elsewhere.
3. Reconcile old knowledge, completed checklist items and claimed PASS results against current source/engine/real evidence. Identify stale, superseded and missing material instead of trusting prior model memory.
4. Report grounded understanding, completed/remaining/verified/NOT RUN, blockers and relevant previously solved approaches. Ask only for user decisions after inspecting what can already be established.
5. For substantial changes write a short OpenSpec phase plan with per-phase gates. Before context compaction or agent switch checkpoint meaningful state and newly verified reusable facts in **their canonical owners**; keep a short topic pointer, not a second task database.
6. Commit/push relevant non-secret work if authorized; do not claim to retrieve hidden reasoning, ignored/unpushed state or unavailable assets.

Use official OpenSpec workflows when installed, and native file/Git lookup without a bespoke Python engine.
