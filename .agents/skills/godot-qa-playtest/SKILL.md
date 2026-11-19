---
name: godot-qa-playtest
description: Independently validate Godot gameplay, scenes, animation, touch/UI, regressions and Android export readiness. Use when verifying a game change or assessing release quality.
---

# Game QA / Playtest

1. Read `.agent-docs/rules/verification.md` and acceptance criteria. Independently inspect the current files and running environment.
2. Select gates by impact: engine import/parse, automated scenario tests, running scene visuals, touch/device, export, crashes, performance.
3. Run only available checks; report PASS / FAIL / NOT RUN for each. Record Godot binary/version, command, logs, revision, device or screenshots.
4. Headless editor success is **not** visual or real-device acceptance. Never turn missing binary, skipped tests or mock output into PASS.
5. Return reproducible bugs, coverage gaps, highest-risk unsolved issues and handoff to Director/Developer.

For mobile work, load [mobile QA matrix](references/mobile-qa-matrix.md) as needed.
