---
name: project-bootstrap
description: Initialize a real project's status from inspected code, tools and history without an extra harness runtime.
---
# First entry or adoption

1. Read AGENTS, STATUS, project files, Git branch and recent commits. Do not assume this template contains a game.
2. Inspect real `project.godot`, engine/version/platform, scenes, existing tests and external tool/asset blockers.
3. Merge documentation and Skills without overwriting existing product decisions, scripts or tests.
4. Replace TEMPLATE STATE with observed facts and links to actual OpenSpec change(s); include date, verifiable evidence and next action.
5. Run `bash scripts/check-docs.sh` if present, and real project baseline checks separately; record NOT RUN honestly.
6. Commit/push non-secret state as authorized, then test fresh-session recovery.
