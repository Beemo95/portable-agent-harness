# Godot implementation rules

Use when editing GDScript, scenes (`.tscn`), resources (`.tres`), plugins, shaders, and build configuration.

- Read `project.godot`, related nodes/scenes, signals/autoloads and version before changing architecture. Never invent existing node paths.
- Follow [Godot GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html): `snake_case` files/functions/signals, `PascalCase` node names/classes, `CONSTANT_CASE` constants. Prefer typed GDScript where it improves correctness.
- Prefer scene ownership and local resource placement suited to the project (see [Godot organization guide](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)); avoid global singletons unless justified.
- Avoid hardcoded fragile node paths, unnecessary `_process`, oversized scripts and duplicate mutable state. Use clear signal/data boundaries and clean scene ownership.
- Keep input logic compatible with the requested platform (touch and keyboard/gamepad when specified); inspect anchors, stretch modes, safe areas and scaling for mobile UI.
- When scene, asset import, save data format or autoload changes, inspect `.tscn`/`.tres` references and migration needs; keep relevant source assets in Git and ignore generated `.godot/` cache only when appropriate.
- Before saying "works", run the applicable Godot editor/headless checks and tests if available, then GUI/device checks when the change needs them. Record exact commands and outputs. Headless-only is not a visual test.
- For new reusable components, document purpose/entry points only if they are not self-evident from code and add/update the architecture map if a boundary changes.

No automatic engine upgrade: Godot version changes require migration review and a recorded decision.
