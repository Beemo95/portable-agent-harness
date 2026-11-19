# Documentation maintenance, knowledge distillation and checkpoints

## One authoritative home per fact
- `openspec/specs/`: accepted product/interface requirements; `openspec/changes/<slug>/`: one change's proposal/design and **only** implementation checklist.
- `.agent-docs/architecture.md`: observed current architecture, invariants and important code entry points.
- `.agent-docs/decisions/`: why a durable trade-off was chosen, alternatives and supersession.
- `.agent-docs/research/`: verified reusable external facts or technical findings with sources/versions.
- `.agent-docs/worklog/`: temporary investigation progress, failures and implementation history; `status.md`: active-work pointer, verified/untested, blockers, next action.
- [`.agent-docs/topics.md`](../topics.md): **pointer-only topic index** for recurring domains. It is **not** a memory dump or a second source of truth.

## Distill at meaningful boundaries
After a consequential design decision, implemented slice, proven bug fix, failed experiment, changed assumption, or before deliberate context compaction/agent switch:
1. Ask whether any verified finding will matter in a later task **even after this change closes**. If not, keep it only in the change/worklog; do not manufacture a topic.
2. For reusable findings, record the minimal **rule/constraint, why, scope, code/test paths, version and observed evidence**, plus rejected approaches if future mistakes are likely. Distinguish observed, approved and hypothetical.
3. Update the **one canonical document** for that fact; reference it from other records rather than copying. E.g., isometric world/screen transform in architecture, chosen occlusion strategy in an ADR, measured artifact/import findings in research.
4. For recurring or cross-feature topics add/update a **short pointer** in [topics](../topics.md). That index links to canonical docs and relevant code/tests, with last-verified revision or an explicit unknown; no duplicate explanation.
5. If behavior changed, update/supersede stale knowledge rather than silently leaving conflicting guidance. Verify source and tests before declaring prior decisions still valid.

## Preserve operational checkpoints
STATUS and the canonical OpenSpec change identify what is **active**, not all historical topics. Before handing off, reconcile Git/source and current tasks; capture scope/phase, implemented/remaining, exact real QA results (PASS/FAIL/NOT RUN), affected files, blockers and **next smallest action**. A [handoff](../templates/handoff.md) is for substantial transitions, not every trivial edit.

Do not record transcripts, unverified research as proven, private secrets or entire source files in Markdown. Commit/push authorized non-secret artifacts for new-PC transfer. A new agent must reconcile notes with the current checkout.
