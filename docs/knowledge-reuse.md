# Reuse project knowledge across unrelated tasks

Purpose: a future request about an **old topic** should benefit from previously validated code, design constraints, test cases and failed approaches even if STATUS now points elsewhere. This works through **normal file search and Git**, not a Python/SQLite engine or automatic permanent model memory.

## Before planning a new feature or revisiting a domain
1. **Inspect current code first:** repository/branch, relevant scene/script interfaces, existing tests, actual dependency/engine version and recent changes.
2. Identify technical terms and synonyms (e.g., `isometric`, `아이소메트릭`, `depth sorting`, `Y-sort`, `pixel snap`). Open [topic index](../.agent-docs/topics.md) **only if related domain knowledge is relevant**. Follow its actual code/test/ADR/spec references.
3. Search canonical docs and code for the topic with native tools (when available): `rg` or `git grep` over code/docs, then past research/worklogs, completed/archived OpenSpec changes and targeted `git log -- path`. A missing topic pointer does **not** mean no earlier work exists.
4. **Reconcile old findings:** check against current source, real tests and engine versions. Mark stale guidance, unverified assumptions and superseded approaches; don't uncritically copy old decisions.
5. Use verified constraints and existing implementations in the new proposal/phase plan. Link canonical records rather than duplicating them.

## After a meaningful finding
Distill **only reusable** conclusions that can inform a later, distinct task:

| Finding | Canonical owner |
| --- | --- |
| Approved required gameplay or data contract | `openspec/specs/` |
| Current code structure, coordinate conventions, runtime invariants | `.agent-docs/architecture.md` |
| Architectural decision and rejected alternatives | `.agent-docs/decisions/` (ADR) |
| Tested technical finding, external version/license or experiment | `.agent-docs/research/` with actual source/evidence |
| Temporary debugging output or task progress | `.agent-docs/worklog/` / active change |
| Current work, blocker and next action | `.agent-docs/status.md` |
| Topic discovery only | `.agent-docs/topics.md`, **pointers**, not copied facts |

For each durable fact, capture **what was verified / scope / why it matters / relevant code and tests / engine or dependency version / observation or source / last-verified revision**. Revisit after changes to associated contracts. If evidence is missing, label it **hypothesis/NOT VERIFIED**, not a reusable invariant.

## Hypothetical isometric → combat → isometric example
- First task: implement directional motion and depth ordering. After real tests, record any stable coordinate convention in architecture, rationale for an occlusion strategy in an ADR, and a topic-index pointer to those **actual** records and code/tests.
- Next task: combat changes the character animation system. Check affected isometric invariants; update the canonical record and relevant regression tests if the behavior changes.
- Later task: add isometric NPCs. Even though STATUS is about combat, use the topic pointer and repository search to recover old code, decisions, known bad approaches and regression tests; verify they still describe the current code before adapting them.

**Not a guarantee of total memory:** ignored/uncommitted information, undocumented discoveries, model-only reasoning and stale notes cannot be reliably recovered. Automated promotion of every chat message would create noise; keep distillation selective and evidence-driven.
