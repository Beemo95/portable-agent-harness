---
name: game-work-handoff
description: Hand off a Godot scene/asset/game feature with accurate visual/device QA and next-step context.
---
# Godot-specific handoff

1. Read the [documentation rule](../../../.agent-docs/rules/documentation.md), STATUS, active OpenSpec change, actual scene/code and Git diff.
2. Reconcile implemented and unfinished work, scene/asset changes and actual game QA. Headless checks never prove animations or devices work.
3. Update **one** OpenSpec checklist and STATUS after meaningful decisions, completed slices or failures. For complex work use [handoff template](../../../.agent-docs/templates/handoff.md).
4. Record exact revision, modified files, commands/evidence, unverified visual/device cases, blockers, next action and whether work is pushed.
5. Commit/push non-secret artifacts when authorized. Use `context-recovery` when *starting* a new session and `verify-and-handoff` for independent QA.
