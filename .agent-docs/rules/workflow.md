# Workflow — every task

## Start
1. Identify the request. If resuming, inspect `.agent-docs/status.md`, its linked OpenSpec change/handoff, `git status`, recent Git commits, actual source and verification evidence. If status is stale, report the discrepancy.
2. Read matching rules/Skills only as needed; inspect real `project.godot`/scenes/version in an adopted game. This template has no playable project.
3. For substantial features, confirm approved acceptance and use a **single** OpenSpec change. Tiny changes need no invented task contracts.

## Work
- Make small changes and run relevant real tool/tests; report skipped or unavailable visual/device QA.
- Do not change approved goals or golden test expectations to conceal a failure.
- Store meaningful decisions, research and failures in canonical docs, not duplicated checklists.
- Avoid concurrent overlapping edits; isolate using branches/worktrees when appropriate.

## Finish or pause
- Check only implemented items in OpenSpec `tasks.md`. A checked box is not independent QA.
- Update STATUS with active change, verified/unverified facts, blockers, next concrete action and source/evidence links.
- Add a [handoff](../templates/handoff.md) if needed. Commit/push relevant non-secret work for a new PC; no uncommitted/ignored state will transfer.

Implementation, automated tests, visual/device verification and release are separate states.
