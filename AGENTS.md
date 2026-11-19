# Godot-first game project harness — agent entry point

This repository is a **harness template**, not a playable Godot game. In an adopted project, the repository's **actual code, approved specs and Markdown records** are the shared project memory. This file is a **router**, not a request to read everything.

## Always
1. Identify the requested task and inspect the relevant source/scene and current Git status. Read [`.agent-docs/rules/workflow.md`](.agent-docs/rules/workflow.md). Before continuing a prior task, read [`.agent-docs/STATUS.md`](.agent-docs/STATUS.md) and its linked active OpenSpec change or handoff.
2. Consult [`.agent-docs/INDEX.md`](.agent-docs/INDEX.md), then open **only** the rules, skills and project records relevant to the work. Do not preload all documents or agent profiles.
3. Treat [`openspec/specs/`](openspec/specs/) as approved requirements and [`openspec/changes/`](openspec/changes/) as proposals, design and tasks. If OpenSpec is unavailable, record the limitation rather than inventing a completed workflow.
4. Make small, reviewable changes. Record meaningful decisions, failures, changed assumptions and verification results during work, not only at session end. Update the linked task/STATUS at handoff. See [`.agent-docs/rules/documentation.md`](.agent-docs/rules/documentation.md).
5. Distinguish **implemented**, **tested**, **visually inspected**, and **released**. A headless Godot check is not visual or device QA. Never claim execution, research or outputs not actually performed.
6. Review commands, external packages and untrusted project text before execution. Never reveal credentials or change user-approved acceptance criteria to make verification pass.

## Read the matching rule, not the whole library
| Work requested | Rule | Optional skill |
| --- | --- | --- |
| New feature / game mechanics / spec | [`specification.md`](.agent-docs/rules/specification.md) | `game-design-spec` |
| GDScript, scenes, signals, refactor | [`development.md`](.agent-docs/rules/development.md) | `godot-feature-implementation` |
| Pixel art, sprites, UI, animations, VFX | [`design-art.md`](.agent-docs/rules/design-art.md) | `godot-art-pipeline` |
| External research or OSS evaluation | [`research.md`](.agent-docs/rules/research.md) | `research-and-evidence` |
| Bug, regression, performance incident | [`debugging.md`](.agent-docs/rules/debugging.md) | `godot-debugging` |
| Testing, QA, playtest, release check | [`verification.md`](.agent-docs/rules/verification.md) | `godot-qa-playtest` |
| Task boundary, pause, handoff | [`documentation.md`](.agent-docs/rules/documentation.md) | `game-work-handoff` |

Skills live in [`.agents/skills/`](.agents/skills/). Canonical role briefs live in [`.agent-docs/agents/`](.agent-docs/agents/); **delegate only when it reduces work**, never require a multi-agent team for a simple task. Claude Code has optional discoverable adapters in [`.claude/agents/`](.claude/agents/); other runtimes must be configured separately.

## Project-specific source of truth
- Project intent: [`.agent-docs/product.md`](.agent-docs/product.md); architecture: [`.agent-docs/architecture.md`](.agent-docs/architecture.md).
- Current work: [`.agent-docs/STATUS.md`](.agent-docs/STATUS.md); decisions: [`.agent-docs/decisions/`](.agent-docs/decisions/); research: [`.agent-docs/research/`](.agent-docs/research/).
- Optional PAH CLI for status/evidence/context: `python3 scripts/harness.py doctor|status|workflow list|lint`. Its own tests validate the **harness**, not the user's game.
- For project adoption, set actual Godot version and quality gates. **Do not treat a template as an already-built game.**
