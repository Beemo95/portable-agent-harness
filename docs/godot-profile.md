# Godot-first harness profile — adoption and intent

This repository is a reusable **harness template**, not a playable Godot game. It is deliberately centered on progressive rule routing and durable Markdown work records rather than forcing a new agent runtime.

## Authority and editing flow
- `AGENTS.md` routes tasks to `ai-docs/rules/*.md`, with `ai-docs/INDEX.md` as the larger map.
- `ai-docs/agents/*.md` defines optional specialist responsibilities; `.claude/agents/*.md` is a Claude Code adapter, not a universally executable subagent system.
- `.agents/skills/godot-*/SKILL.md` implements optional on-demand workflows following the Agent Skills specification. An agent runtime must actually discover/use them; paths alone do not guarantee invocation.
- OpenSpec owns **requirements, proposal, design, task checklist**. Project Markdown owns **current snapshot, architecture, decisions, research and operational handoff**. Git owns history.
- PAH's Python CLI is optional support for context/search/task/evidence; default documentation workflow should not require extra infrastructure.

## Start a new game
1. Install into a **separate actual Godot repository** through `python3 scripts/harness.py init PATH --name "Your Game"` (inspect available flags; installation refuses collisions). Existing game projects require manual review of overlapping files.
2. Inspect `project.godot`, set Godot version and platform in `ai-docs/architecture.md`, set approved intent in `ai-docs/product.md`, and initialize `ai-docs/project/STATUS.md` with observed facts.
3. If using OpenSpec, install its official CLI separately and initialize its agent adapters after reviewing proposed diffs; never overwrite these bundled roles/skills without review.
4. Begin work from `AGENTS.md`. For feature work create a change; for bug fixes use appropriate focused rules. Update persistent records during meaningful changes and at task boundaries.
5. Add real **game** verification gates based on installed engine and devices. Harness unit tests are **not** game QA.

## Version-appropriate official guidance
- [Godot project organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/project_organization.html)
- [Godot scene organization](https://docs.godotengine.org/en/stable/tutorials/best_practices/scene_organization.html)
- [GDScript style guide](https://docs.godotengine.org/en/stable/tutorials/scripting/gdscript/gdscript_styleguide.html)
- [Godot command line](https://docs.godotengine.org/en/stable/tutorials/editor/command_line_tutorial.html)
- [Agent Skills specification](https://agentskills.io/specification)
- [Claude Code project subagents](https://code.claude.com/docs/en/sub-agents)
