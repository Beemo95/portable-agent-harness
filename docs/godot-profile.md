# Godot-first documentation profile

This is a **template, not a game**. Copy/merge into a real Godot repository without overwriting established docs/tests. See [adoption](adopting-existing-project.md).

1. Inspect real `project.godot`, scene tree, Godot version, renderer, platform and baseline test commands.
2. Fill `.agent-docs/product.md`, `architecture.md` and `status.md` from observed project state.
3. Use OpenSpec's Markdown changes for significant features and the matching task rule/Skill for work. Its official CLI is optional.
4. Before pausing, update the one tasks checklist, STATUS and meaningful decision/handoff; commit/push.
5. Test using the **actual** Godot editor/game and applicable device. No bundled Python tests can establish game readiness.

References: [project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) · [scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html) · [GDScript style](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) · [Godot CLI](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html).
