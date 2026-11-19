# Godot implementation rules

Use for GDScript, scenes (`.tscn`), resources (`.tres`), plugins, shaders and build changes.

## Inspect current code and prior knowledge
- Before designing or editing, read actual `project.godot`, relevant scene trees/scripts, signals/autoloads, tests, version and nearby Git history. Identify existing reusable components and contracts; do not invent nodes, paths or behavior.
- For previously visited domains (movement, isometric sorting, save formats, UI, etc.), follow [topic pointers](../topics.md), approved specs, architecture and ADR/research; **verify relevance against current source** before reusing.
- Prefer the smallest change compatible with accepted architecture. Protect scene UIDs, resources, save compatibility and test baselines; avoid solving a prior known issue again with the same rejected approach.

## Implement and test by phase
- Follow the phase acceptance and source boundaries in the linked OpenSpec change. Implement one small vertical slice at a time, with applicable **automated unit/integration or scene tests for new behavior and regressions**.
- Follow the [official GDScript style](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html). Favor typed GDScript where useful; local signals/scene ownership over unnecessary global state, and clear interfaces.
- Preserve touch/keyboard requirements, pixel and asset import rules, UI scaling, scene references and any migration constraints.
- Run installed-engine parse/import/build, relevant automated checks, and actual runtime/visual/device verification where acceptance requires it. [Verification rule](verification.md) explains limits of headless checks.
- **Do not advance past a required failed, skipped or unavailable test/QA gate.** Report FAIL / NOT RUN and blockers, fix/retest, or obtain a user decision to defer/scope; do not change golden results to hide regressions.
- After a meaningful phase, record actual code/test paths and evidence; distill any reusable contract/rationale into [canonical knowledge](../../docs/knowledge-reuse.md), not a copied changelog.

Never upgrade Godot or change approved product behavior silently; use approved decisions and actual version-matched docs.
