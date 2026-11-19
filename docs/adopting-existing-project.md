# Adopting a project that already has AI docs and tests

The default `init` command refuses overwrite collisions by design. Existing mature repositories should not be rewritten to fit a template.

## Safe migration

1. On a new branch, inventory current `AGENTS.md`, `project`, test scripts and adapter files.
2. Back up project state. Run `init TARGET --dry-run` to list conflicts. If conflicts exist, stage the harness in a temporary empty directory and copy modules intentionally instead of overwriting.
3. Keep existing product docs, approved math, architecture and reference tests as their **original authoritative sources**.
4. Add `.harness/context-routes.json` hints pointing to real code and doc paths; run `lint`.
5. Configure `project.harness.json` with actual build/unit/runtime gates. Do **not** map acceptance to generic harness self-tests.
6. Convert an active feature into `.harness/tasks/ID/contract.json` and `state.json`; retain original issue/PR links.
7. Re-run baseline tests before edits; only then add agent tasks and test cross-model resume from a clean branch.

## Specific note for Godot projects

Pin the Godot version, verify headless import/tests and *separately* define real visual/runtime QA. `godot --headless` passing never proves that an animation looks correct. If Python reference fixtures are the source of truth for gameplay numbers, never rewrite the fixtures just to make Godot tests pass.

The harness library itself does not presume specific Godot versions, paths, IDEs or models.
