# Safe adoption in a real Godot project

This repository is **only a documentation template**. Do not overwrite an established game's source/tests or pretend the template's STATUS describes that game.

1. Create a review branch. Inspect the game's current `AGENTS.md`, Skills, tool-specific adapters, actual source/`project.godot`, Git, existing tests and observed Godot executable version. This template targets **Godot 4.7+ within 4.x**. If the game runs on an older or different major version, report the mismatch and plan a reviewed migration rather than silently changing the game.
2. Merge relevant files from this profile: `AGENTS.md` guidance, `.agent-docs/`, `.agents/skills/`, necessary host adapters (`CLAUDE.md`, `GEMINI.md`, `.claude/skills/`), and `openspec/`. Reconcile conflicts manually, preserving existing decisions and scene/test baselines. Keep source `.agents/skills/` and Claude wrapper names/descriptions in sync; don't copy adapters without their referenced source files.
3. Fill product intent, observed architecture/version/platform, known test commands and **real** work state. **Before adding or keeping `project.godot`, replace the placeholder STATUS**: remove `TEMPLATE STATE`, record actual engine/revision, a dated `Last updated` and concrete `Next action`. The integrity CI now rejects a real Godot project with template STATUS. Use `Active OpenSpec changes: none` or exact existing `openspec/changes/<slug>/` paths with a real proposal/tasks file.
4. Keep **one** implementation checklist under the change's `tasks.md` and link real issues/PRs, decisions, worklogs and evidence. Record actual PASS/FAIL/NOT RUN separately.
5. Optionally copy `scripts/check-docs.sh`, `tests/docs-lint.sh` and the CI workflow, reviewing their assumptions for that project. They should **not** block a normal `tests/` or `scripts/` directory. Run the project's actual Godot tests independently.
6. If desired, set up the **official OpenSpec Skills** via its own CLI after reviewing generated changes; see [OpenSpec workflow](openspec-workflow.md).
7. Commit/push non-secret source and context, then run [cold-start evaluation](evaluation.md) in a new session/clone. Report actual outcome and unresolved missing state.

Older non-main branches of this template may contain the deprecated Python architecture. Inspect branch differences before copying files; don't silently rewrite or delete branches.

This process preserves existing project knowledge. It does not automatically install a Godot engine, configure OAuth, create a game or recover unpushed work.
