---
name: godot-debugging
description: Investigate Godot scene, resource, GDScript, animation, crash or performance regressions. Use for bug reproduction, root cause analysis and targeted fixes.
---

# Diagnose Godot bug

1. Read `.agent-docs/rules/debugging.md`; reproduce the specific issue with environment/version, steps and expected/actual outcome.
2. Capture logs and inspect affected `.gd`, `.tscn`, `.tres`, imports and recent diffs; keep guesses clearly labeled.
3. Compare one hypothesis at a time; avoid unrelated refactors while fixing.
4. Implement minimal fix and verify regression in the relevant runtime or with explicit manual steps if no automation is possible.
5. Report reproduced evidence, root cause, fix paths, tests, device/visual gaps, and follow-up. Update linked issue/worklog and STATUS.
