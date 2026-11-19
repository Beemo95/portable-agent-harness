# Godot 4.7+ project profile

**Supported target:** Godot **4.7 or newer within the Godot 4.x series**. This includes 4.7.x and later compatible 4.x releases; this profile is **not pinned to 4.7.2**. A future major version such as 5.x requires separate compatibility review, not automatic inclusion. This repository is a **documentation template, not a game**.

## Before implementation in an adopted game
1. Inspect the real `project.godot`, relevant scenes/resources, current engine binary/editor version (e.g., `godot --version` or the installed executable), renderer, export targets, addons and baseline tests. Do **not** infer the exact installed patch version from project files alone.
2. If the actual executable is **below 4.7**, or the project/toolchain requires an older version, report the mismatch and the compatibility or migration choices **before making feature changes**. Never silently upgrade the engine, project format, addons or exports. A 5.x engine also needs deliberate migration approval.
3. When using engine APIs, GDScript features, resource formats or plugins, verify them against **the installed 4.7+ engine version** and version-matched official documentation. A newer API must not be assumed present in every supported 4.x release.
4. Populate `.agent-docs/product.md`, `architecture.md` and `status.md` with the **observed** project and tested engine version. Keep "target 4.7+" distinct from the actual binary/version used in each test.
5. Use the existing OpenSpec change and phase gates for substantial work, then test with the **actual Godot editor/game** and relevant device or export environment. Headless import cannot establish game visuals or device correctness.

## Handoff and adoption
Merge into a real repository without overwriting its code/tests; see [adoption](adopting-existing-project.md). Before pause, update the single tasks checklist, STATUS and relevant decision/handoff. Record the observed engine version, command, tested Git revision and any unverified version compatibility. Commit/push only authorized non-secret changes.

References: [project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html) · [scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html) · [GDScript style](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html) · [Godot CLI](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html).
