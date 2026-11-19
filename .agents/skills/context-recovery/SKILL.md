---
name: context-recovery
description: Recover current task state on a new session, model or computer with minimal context.
---
# Context recovery

1. Obtain the project root and (if available) Task ID; run `doctor`, `status`, then `resume TASK-ID`.
2. Compare checkpoint fingerprint/HEAD to current source and inspect working tree. Treat drift as a question to investigate, not as proof of completion.
3. Call `context "current work" --task TASK-ID --budget 1800`. Read cited files in full only when needed.
4. Separate explicit approved decisions, verified facts, outdated notes, unverified assumptions and missing external dependencies.
5. Confirm next safe slice and which tests apply. If missing essential context cannot be recovered, record a blocker or ask the user instead of inventing it.
6. Save a new checkpoint and short handoff when switching agents or ending a meaningful stage.

Do not try to reconstruct hidden model deliberations; recover observable state, artifacts and rationale instead.
