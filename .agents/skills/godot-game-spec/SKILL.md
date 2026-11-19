---
name: godot-game-spec
description: Define a Godot game mechanic, gameplay loop, UI flow or acceptance criteria using OpenSpec. Use when planning or changing game features, balancing or save semantics.
---

# Spec-driven game feature

1. Read `ai-docs/rules/specification.md` and relevant `ai-docs/product.md`/`openspec/specs/`; inspect current scene interfaces.
2. Clarify player-visible goal, flow, constraints, non-goals and testable acceptance scenarios. Avoid code-first implementation before requirement review when scope is material.
3. Create or update the canonical OpenSpec change in `openspec/changes/<slug>/` with proposal, design and tasks using official CLI when installed; do not invent output or mark tasks done.
4. Flag product/game-feel choices needing user approval, then hand off a precise scene/file scope to Developer or Artist.
5. Output: change path, acceptance bullets, open questions, and first small implementation slice. Keep STATUS linked.
