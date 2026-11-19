# Godot project knowledge map (read selectively)

This is a directory, not a list of documents to load at startup. Start with [`../AGENTS.md`](../AGENTS.md); read `rules/workflow.md` then only relevant sections below.

## Task-specific rules
| Intent | Read |
| --- | --- |
| All work | [`rules/workflow.md`](rules/workflow.md) |
| New mechanic / design changes | [`rules/specification.md`](rules/specification.md) |
| Godot code / scene changes | [`rules/development.md`](rules/development.md) |
| Art, assets, animation, UI | [`rules/design-art.md`](rules/design-art.md) |
| Online information / libraries | [`rules/research.md`](rules/research.md) |
| Debugging | [`rules/debugging.md`](rules/debugging.md) |
| QA / release / device tests | [`rules/verification.md`](rules/verification.md) |
| Writing records, closing work | [`rules/documentation.md`](rules/documentation.md) |

## Living project records
- [`product.md`](product.md): approved game vision, player/platform constraints, non-goals.
- [`architecture.md`](architecture.md): verified scene/data boundaries, engine/version, directory map.
- [`project/STATUS.md`](project/STATUS.md): one-screen current snapshot, active change links, blockers, next step.
- [`decisions/`](decisions/): why important choices were made; preserve superseded decisions.
- [`research/`](research/): dated source evaluations and experiments; no uncited assertions.
- [`worklog/`](worklog/): concise event/iteration notes when they matter to resumption.
- [`templates/`](templates/): templates for work logs, research and handoffs; never fabricate entries to fill a template.

## OpenSpec and roles
- [`../openspec/specs/`](../openspec/specs/) owns approved requirements; [`../openspec/changes/`](../openspec/changes/) owns active proposals/design/checklists. Do not copy them into another planning database.
- [`agents/INDEX.md`](agents/INDEX.md) and [`agents/`](agents/) are optional specialist **role briefs**, not a promise that all AI runtimes spawn agents.
- [`.agents/skills/`](../.agents/skills/) holds on-demand workflows (`SKILL.md` files).

## Additional reference, only if needed
- [`../docs/open-source-stack.md`](../docs/open-source-stack.md): OSS integration boundaries.
- [`../docs/task-lifecycle.md`](../docs/task-lifecycle.md): optional PAH state/checkpoint CLI.
- [`../docs/security.md`](../docs/security.md): trust and command execution.

**Reconciliation rule:** approved spec describes intended behavior; the current Godot project and runtime logs describe observed behavior. Record conflicts; do not silently rewrite history.
