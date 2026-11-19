---
name: godot-game-spec
description: Design Godot mechanics from existing code and prior decisions, clarify blocking choices, then plan independently testable phases.
---
# Spec-driven Godot change

1. Inspect [spec rule](../../../.agent-docs/rules/specification.md), actual source/scenes/tests, accepted product intent, existing specs and previously verified [topic knowledge](../../../.agent-docs/topics.md).
2. Separate factual unknowns (investigate) from user decisions (ask focused questions). Do not re-ask settled design choices or guess irreversible gameplay/monetization changes.
3. Describe player-visible behavior, failure/edge cases, save/compatibility, platform needs and acceptance scenarios. Define baseline tests and any necessary visual/device QA.
4. For substantial work use official OpenSpec Skills if available to create **one** proposal/design/`tasks.md` with ordered phases: affected files, prerequisites, implemented outcomes, tests, completion gates, risk/rollback.
5. Obtain decisions only for material ambiguity or approval boundaries. Routine small fixes need no ceremony. Preserve original acceptance when implementation fails.
6. Link STATUS to the active change and first safe slice. After completed phases, distill reusable product/technical decisions to the proper owner with topic pointers; never duplicate the entire task history.
