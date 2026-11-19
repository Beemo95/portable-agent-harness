# Scene + GDScript change checklist (open only for Godot scene edits)

- Godot version and renderer confirmed from `project.godot` or actual runtime.
- Affected `.tscn`/`.tres` resources, UIDs, node paths, signals and autoloads inspected.
- Main scene and ownership of child scenes understood; reusable components avoid duplicate source of truth.
- Scene load/parse tested with real Godot editor where available; output captured.
- Input actions and camera/UI scaling checked on relevant platform.
- Game state/save migration considered if persistent resources change.
- Evidence linked in task/STATUS; headless cannot certify appearance or touch behavior.
