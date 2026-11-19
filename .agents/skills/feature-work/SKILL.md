---
name: feature-work
description: Safely execute a small feature slice against a durable task contract.
---
# Feature work

1. `status` / `resume TASK-ID` / `context "requested change" --task TASK-ID`.
2. Compare checkpoint to Git and working tree; inspect relevant current source files.
3. Confirm task is ready, acceptance criteria map to real tests, no unresolved blockers, and branch/worktree edit ownership is clear.
4. Implement one vertical slice with minimally scoped changes. Add or adapt relevant tests without changing protected expected outputs to conceal failure.
5. Run targeted checks, update task state with `--expect` current revision, then checkpoint.
6. Submit source diff, test command/results, unresolved risks and short next action. Do not claim GUI success without GUI execution.

Escalate to `deep-plan` when architecture or product requirements change. Use a second worker only for genuinely independent work.
