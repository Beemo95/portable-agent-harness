---
name: openspec-pah-handoff
description: Continue an existing repository task across AI models or computers using OpenSpec plans and Portable Agent Harness evidence.
---
# OpenSpec + PAH recovery and handoff

1. Run `python3 scripts/harness.py doctor`, `status`, and `workflow list` from the repository root. Review any executable project commands before running them.
2. If the user refers to an OpenSpec change, use `workflow status CHANGE` and `workflow context CHANGE`. `openspec/changes/CHANGE/{proposal,design,tasks}.md` and `openspec/specs/` are authoritative for requirements and implementation plan. Inspect actual files before editing.
3. OpenSpec `isPlanningComplete` reports planning progress, **not implementation success**. Checked boxes do not prove independent verification. `workflow` is a read-only projection of upstream files and never marks `implementation_verified` true.
4. If a PAH execution task also exists, run `resume TASK-ID`; reconcile the checkpoint with actual Git HEAD, working tree and environment. Never duplicate OpenSpec requirements in a competing plan.
5. For new OpenSpec changes, use upstream official Skills installed by `openspec init`, not invented slash commands. Make small changes, run **reviewed** quality gates, checkpoint, commit and push the work approved for transfer.
6. A new PC cannot reconstruct uncommitted changes never committed or otherwise transferred. Do not promise seamless recovery of secrets, external assets or local processes.
