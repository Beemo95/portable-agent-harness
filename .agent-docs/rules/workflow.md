# Workflow — every project task

## Start / resume
1. For “where did we stop?”, read STATUS, its active OpenSpec change and handoff, then inspect `git status`, recent commits, actual code and recorded test evidence. Report stale/missing pointers instead of guessing.
2. Load task-specific rules/Skills from `AGENTS.md` only when relevant; never preload all documentation.
3. Inspect the real project's `project.godot`, engine version and relevant scenes/tests. This template is not a game.
4. Use **one** OpenSpec change for substantial work; tiny fixes need no fabricated contract.

## Work / verify
- Work in reviewable slices; preserve approved acceptance and existing tests. Avoid overlapping agent edits without separate branches/worktrees.
- Run actual project checks; record PASS / FAIL / NOT RUN and distinguish headless parsing from visual or device QA.
- **Checkpoint meaningfully** after decisions, finished slices, important failures, and before deliberate context compression, session switch or risky operation. Update the existing OpenSpec checklist and small STATUS, not a duplicate state store. See [documentation](documentation.md).

## Finish / pause
- Check off only implemented OpenSpec tasks; record revision, evidence, remaining work, blockers and the next smallest action.
- Use the [handoff template](../templates/handoff.md) for complex work.
- Run `bash scripts/check-docs.sh` when present (documentation integrity only, not game QA).
- Commit/push non-secret work when authorized for handoff. Another session must reconcile source and tests rather than trusting old summaries.
