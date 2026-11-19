# Agent adapters — evidence, precedence, and discovery limits

**Source of project guidance:** AGENTS.md. This is a file-layout compatibility profile, **not a tested guarantee** that each agent will load or obey every instruction. Compare current host versions and trusted workspace settings before claiming success.

| Agent | Project instruction location | Skills | Verify on the installed client |
| --- | --- | --- | --- |
| Codex CLI / IDE | AGENTS.md | .agents/skills/ | Fresh project session; check loaded instruction sources |
| Cursor | AGENTS.md | .agents/skills/ (also may discover .claude/skills/) | Inspect applied rules and Skills; confirm duplicates are not selected |
| Claude Code | CLAUDE.md imports @AGENTS.md | .claude/skills/ forwarding files | /context all; inspect invoked skill path |
| Grok Build | AGENTS.md **and CLAUDE.md may both load** | .agents/skills/ and .claude/skills/ supported in repo documentation; .grok/skills/ is primary in xAI's concise docs | grok inspect in a trusted repo, inspect actual chosen same-name Skill and loaded rule files |
| Google Antigravity | AGENTS.md | .agents/skills/ (legacy .agent/skills/ supported) | Check workspace Customizations/skills and actual loaded paths |
| Gemini CLI | GEMINI.md imports @./AGENTS.md | Host installation/version dependent | /memory show, confirm included instructions |
| Hermes Agent | Check workspace and trust; older versions differ | Shared project Skills conditional on version/trust | Inspect actual loaded instructions/Skills |

## Conflicts and duplicate discovery

- The 12 canonical project Skills live at .agents/skills/. For Claude compatibility, the 12 files at .claude/skills/ are **short adapters** pointing to the canonical body. They do not define independent workflows.
- Grok's detailed upstream repo documentation says it can scan .grok/, .agents/ and .claude/ and deduplicates same-name Skills by priority; its concise public documentation lists .grok/ and plugin/config paths. **Do not guess which Skill won** in an untested Grok version. Run grok inspect; if necessary disable a duplicate discovery location in host configuration, not by rewriting the canonical Skill.
- Grok also discovers both AGENTS.md and CLAUDE.md. The latter contains only the import @AGENTS.md, so there is no distinct policy to conflict with AGENTS.md; however, Grok's actual import expansion/deduplication must be observed rather than assumed. Avoid new host-specific normative instructions inside adapters.
- Claude Code now has native AGENTS.md support on supported versions; its official guidance says keeping @AGENTS.md in CLAUDE.md is a valid compatibility fallback and does not duplicate that file within Claude's own context. This does **not** imply Grok behaves the same way.
- Current user-approved acceptance and version-matched actual source take precedence over obsolete docs as evidence; host/security policies always govern actions. Surface real conflicts for review rather than silently choosing one.

## Optional OpenSpec and runtime tests

OpenSpec's current **default is machine-global Skills**. For a portable repo install, explicitly use project scope and review generated changes; see [OpenSpec setup](openspec-workflow.md). Its own generated openspec-* Skills are not bundled here.

After adopting this template, start fresh sessions using only a simple feature request. Check instruction and skill discovery, source-code inspection before design, phase gates, and claimed vs actual tests. These checks have **not been run** in Codex/Cursor/Claude/Grok/Antigravity in this template.

References: [Claude memory](https://code.claude.com/docs/en/memory) · [Claude Skills](https://code.claude.com/docs/en/skills) · [Cursor Skills](https://cursor.com/help/customization/skills) · [Antigravity Skills](https://antigravity.google/docs/skills) · [Grok public Skills](https://docs.x.ai/build/features/skills-plugins-marketplaces) · [Grok upstream implementation docs](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md) · [OpenSpec supported tools](https://openspec.dev/docs/supported-tools).
