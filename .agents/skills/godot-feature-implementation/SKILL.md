---
name: godot-feature-implementation
description: Implement or refactor Godot 4 GDScript, scenes and resources under an approved game change. Use for player movement, controls, gameplay systems, signals, UI and serialization.
---

# Implement Godot feature

1. Read `ai-docs/rules/development.md`, active OpenSpec change and only affected scenes/scripts. Confirm engine version and actual scene tree.
2. Plan a small slice, file ownership and regression checks; preserve scene UIDs/resource references and data migration constraints.
3. Modify code/assets to match accepted behavior. Prefer type-safe GDScript, local signals and stable node ownership; no unnecessary autoload.
4. Validate syntax/import with the **installed** editor (`godot --headless --editor --path <project> --quit`) when available. Add focused tests and visual/device inspection for relevant behaviors.
5. Report exact changed files, command/log/evidence, untested cases and next action; update STATUS and architecture if boundaries changed.
6. When uncertain about Godot API semantics, read `ai-docs/rules/research.md` and the version-matched official docs; don't guess.

For scene considerations, load [scene-checklist](references/scene-checklist.md) only when applicable.
