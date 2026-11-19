# Optional specialist roles — Godot game development

Each file here is a canonical **role brief**. The main agent may act alone or delegate a scoped part of the work. Files here are not executable agents by themselves.

| Specialist | Role brief | When useful |
| --- | --- | --- |
| Director / game designer | [`director.md`](director.md) | game loop, priorities, scope, spec/acceptance |
| Godot developer | [`developer.md`](developer.md) | GDScript, scene logic, integration |
| Artist / UI | [`artist.md`](artist.md) | assets, direction sprites, visuals, VFX/UI |
| QA / playtest | [`qa.md`](qa.md) | independent evidence and regressions |
| Researcher | [`researcher.md`](researcher.md) | Godot docs, addons, license/version evaluation |

**Delegation contract:** provide task, source paths, change ID, acceptance criteria, boundary of allowed edits and requested artifact; receive concise result, evidence links, risks and next action. Prefer no subagent for a simple edit. Never run separate agents concurrently on the same Godot scene/resource without isolation.

Claude Code project adapters exist in [`../../.claude/agents/`](../../.claude/agents/). Other runtimes require separate configuration or can follow these role briefs manually; no universal agent auto-discovery claim.
