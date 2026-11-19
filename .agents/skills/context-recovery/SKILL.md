---
name: context-recovery
description: Recover current task state from project Markdown, source and Git on a new session, model, or computer.
---
# Recover context (without a custom CLI)

1. Read `AGENTS.md`, STATUS, `git status --short` and `git log -5 --oneline`.
2. Follow linked active OpenSpec change/tasks, decisions and handoff; if none is recorded, report that fact.
3. Reconcile checked tasks and claimed tests with actual code, revision and evidence.
4. Inspect only relevant source and task-specific guidance using native file tools. Separate verified, unverified and stale claims.
5. Report goal, implemented, remaining, tested, blockers and smallest next action.
6. At pause update canonical tasks/STATUS/handoff; commit/push non-secret work for transfer.

Never assume Git contains hidden reasoning, unpushed work, ignored assets or secrets.
