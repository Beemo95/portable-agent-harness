# Task lifecycle — OpenSpec, STATUS and Git

For significant work, use `openspec/changes/<slug>/` proposal/design/tasks. `tasks.md` is the **one** implementation checklist. STATUS links the active change and lists verified progress, unverified areas, blockers and the next action.

Implement a small slice → run **real project checks** → mark only implemented tasks done → record command/environment/revision/evidence → update STATUS → commit/push for cross-session transfer.

For tiny fixes, don't create elaborate proposals solely for process compliance. Keep an issue/STATUS note when sufficient.

**Concurrency:** isolate overlapping code/scenes/docs with branches/worktrees and reconcile changes through Git. There is no custom optimistic-lock task database.

**Done:** implemented, tested, visually/device-verified and released are separate labels. Neither a checked box nor an old CI run automatically establishes product acceptance. A clean clone cannot recover unpushed WIP.
