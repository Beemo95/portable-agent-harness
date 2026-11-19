# Workflow — every project task

## Start (brief)
1. Identify task type, priority, requested outcome, acceptance criteria, and whether a linked OpenSpec change already exists. For an ongoing task, read `.agent-docs/status.md` and only its linked task/decision/handoff documents.
2. Check the actual `project.godot`, scenes/scripts/assets affected, Git diff and relevant Godot version. Do **not** assume `project.godot` exists in the harness template.
3. Follow the task-specific rule from `AGENTS.md`. Avoid unrelated research or reading the entire rules library.
4. Small reversible tasks may proceed with a brief plan; significant UX, performance budget, monetization, platform or gameplay changes need a spec/change proposal and explicit decision where intent is ambiguous.

## While working
- Work in reviewable slices: source/scene changes + relevant test/preview + a short record of nonobvious decisions or issues.
- Make uncertain assumptions explicit; preserve source links and actual command output paths.
- Prefer one active writer per overlapping scene/resource; other agents provide findings or isolated worktrees. Subagent requests need scoped input and a concise handback, not whole-session transcripts.
- Do not claim scene/asset visual fidelity based solely on code or a headless engine check. If visual verification is unavailable, report that gap.

## Finish / pause
- Update any authoritative OpenSpec `tasks.md` **only for work actually done**; it is not QA evidence.
- Update `.agent-docs/status.md`: next action, blockers, tested/untested, change ID, related commits/paths.
- Update ADR, research, architecture, or worklog **only if material facts changed**. Do not log trivial edits or every command.
- Preserve reproducible evidence and unresolved risks. If transfer to another PC matters, commit/push the relevant work and linked documents; never claim uncommitted edits are recoverable from Git.

## Done means
Requirement/acceptance status, actual implementation, tests, visual/device QA, and delivery are separate states. Mark only what the available evidence supports.
