# Godot QA and release verification

## Engine-version gate
- Supported target is **Godot 4.7+ within the 4.x series**. Establish the actual binary/editor version (e.g., `godot --version`) and check required addons and project format before execution. Record the observed version and command in QA evidence.
- If unavailable, mark version-dependent verification **NOT RUN**. If an installed engine is older than 4.7 or is an unapproved major-version change, report **BLOCKED / mismatch** rather than claiming compatibility or silently upgrading.
- Testing on one 4.x release proves only that observed environment, not every future 4.x patch/minor. Validate any claimed range with appropriate version-specific evidence.

## Test choice
- Validate the acceptance criteria, then choose an appropriate check: static/parse, automated gameplay, real editor/runtime, visual/playtest, platform/device and export.
- No game is created by the harness template. If `project.godot` or Godot binary is missing, mark the gate **not run** (not PASS).
- For a real Godot game, a useful import/parse smoke check is `godot --headless --editor --path <project-dir> --quit` (choose the installed Godot editor binary); this proves neither gameplay nor visual appearance.
- Record Godot version, exact command/parameters, target scene/device, exit code, log path and tested commit. See [official CLI reference](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html).
- For 2D/isometric/visual tasks, inspect the **running** scene and capture an actual screenshot/video or explain inability. Check movement directions, occlusion, pixel seams, sizing, animations and touch inputs when relevant.
- For Android export, confirm export preset, SDK/signing and actual device behavior separately. Headless editor launch does not establish Play Store readiness.
- No test case, skipped-only tests, parser output text without real execution, missing binary, or old evidence must not be reported as passed QA.

## Evidence & closure
Write expected, observed, test environment, PASS/FAIL/NOT RUN, outstanding risks and evidence references into the active OpenSpec change or concise worklog. Checked `tasks.md` items and an AI's claim are not themselves evidence.
