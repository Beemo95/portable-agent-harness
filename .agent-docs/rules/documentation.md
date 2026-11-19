# Documentation maintenance and checkpoint policy

## One authority per fact
- OpenSpec `specs/` owns approved requirements; `openspec/changes/<slug>/` owns proposal/design and the **only** implementation checklist.
- `.agent-docs/product.md` and `architecture.md` own approved vision and observed architecture.
- `.agent-docs/decisions/` records consequential rationale and supersession, `research/` verified reusable findings and `worklog/` meaningful progress/problems.
- `.agent-docs/status.md` links current work; it is not an event log or copied task list.

## Write before losing useful context
Update the canonical change and STATUS after a meaningful decision, implemented slice, test failure, before deliberate context compaction/model change, and before a risky operation where interruption could lose the next step. Do **not** journal every command or whole conversation.

Minimum checkpoint: goal/change path; code/scene paths and branch/revision; implemented vs remaining; actual checks, including NOT RUN; unresolved decisions/blockers; **next smallest action**. Note dirty/unpushed work explicitly.

## Transfer or close
1. Compare STATUS and OpenSpec checkboxes with the actual diff/source; only tick implemented tasks, never unverified QA.
2. Record changed assumptions and tests with command, revision, environment and evidence locations.
3. Keep STATUS short and add a [handoff](../templates/handoff.md) for substantial work.
4. Check internal links with `bash scripts/check-docs.sh` if present; then commit/push non-secret context and source when authorized and needed for another PC.
5. A new agent re-checks Git and actual code; uncommitted work, ignored assets or credentials never transfer automatically.

Do not rewrite user-approved acceptance or claim unrun tests passed.
