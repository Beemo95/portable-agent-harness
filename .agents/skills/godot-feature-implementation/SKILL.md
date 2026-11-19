---
name: godot-feature-implementation
description: Implement Godot 4.7+ scenes, signals and GDScript in testable phases, reusing the project's previously verified contracts.
---
# Implement Godot feature

1. Target **Godot 4.7+ within 4.x**; verify the real editor binary version (e.g., `godot --version`) and inspect `project.godot`, relevant scenes/scripts, signal/autoload ownership, tests, Git and prior architecture decisions. Report older or major-version mismatches before editing; do not upgrade silently. Check APIs against the observed version. For recurring topics follow [topic index](../../../.agent-docs/topics.md) and verify conventions against current code.
2. Identify exact approved behavior, current OpenSpec phase, file boundaries, scene UIDs/resource references, migration constraints, baseline tests and regression risks. Resolve material ambiguity before editing; choose reversible assumptions for minor details.
3. Implement a **small planned vertical slice**, adding/updating suitable automated gameplay/unit/integration tests for new behavior and regressions. Preserve existing accepted tests and save contracts.
4. Run installed-engine parse/import (e.g. `godot --headless --editor --path <project> --quit`) and relevant tests. Check GUI/visual/device behavior where acceptance requires it; a headless PASS is not a visual PASS.
5. **Phase gate:** if a required check fails or is unrun, fix/retest or record blocked and request a necessary user decision. Do not mark the phase fully accepted or advance on an assumed PASS.
6. Record actual commands/results, relevant file paths, revision, NOT RUN gaps, blockers and next slice; update canonical OpenSpec/STATUS. Distill reusable architecture/logic decisions into their established owner and [topic pointers](../../../.agent-docs/topics.md).

Use [development rule](../../../.agent-docs/rules/development.md), [verification rule](../../../.agent-docs/rules/verification.md) and [scene checklist](references/scene-checklist.md) selectively.
