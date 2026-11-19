# Verification — evidence over reported status

This template's Bash documentation CI detects broken common Markdown links and missing OpenSpec STATUS targets. **It does not run or validate a game**, and its negative tests do not substitute for application regression coverage.

In a real Godot game run relevant, approved source/build/unit tests, the actual editor/runtime, and visual/touch/device/export checks as needed. Record exact commands/procedure, revision and dirty state, Godot version/device/environment, observed PASS / FAIL / NOT RUN and actual log/screenshot evidence locations. Missing tools, stale evidence or unchecked acceptance must be labeled NOT RUN.

A successful Godot `--headless --editor` import does not prove animation appearance, collisions, touch, Android behavior or release readiness. Checklists indicate reported implementation; independent QA must inspect actual outcomes. [Godot verification rule](../.agent-docs/rules/verification.md) · [cold-start evaluation](evaluation.md).
