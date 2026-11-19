# Official-source and freshness audit — checked 2026-11-19

- **Reviewed on:** 2026-11-19
- **Next review by:** 2026-12-19
- **Status:** Official public docs inspected for the specific claims below. Their future state, all versions, and actual local agent behavior remain **NOT VERIFIED**. This is a manual review record, not evidence of test execution.

| Area | Official evidence consulted | Verified scope on date | Residual risk / trigger |
| --- | --- | --- | --- |
| Godot 4.7+ | [Godot 4.7 docs](https://docs.godotengine.org/en/4.7/) · [4.7.2 release](https://godotengine.org/article/maintenance-release-godot-4-7-2/) | 4.7 docs exist; 4.7.2 release dated 2026-08-18 | No game or engine executable has been run; newer 4.x APIs need version-specific checking |
| Claude Code | [Memory/imports](https://code.claude.com/docs/en/memory) · [Skills](https://code.claude.com/docs/en/skills) | @AGENTS.md supported; Claude can also read AGENTS.md natively in supported versions; .claude/skills recognized | Org/user settings and exact client versions can override; test /context all |
| Gemini CLI | [GEMINI.md imports](https://geminicli.com/docs/cli/gemini-md/) | @./AGENTS.md import syntax and /memory show documented | No actual CLI load observed |
| Cursor | [Rules](https://cursor.com/docs/rules) · [Skills](https://cursor.com/help/customization/skills) | AGENTS.md and .agents/skills/ project discovery supported | Also scans some compatibility folders; check duplicate named Skills |
| Antigravity | [Skills](https://antigravity.google/docs/skills) | Workspace .agents/skills/ current; .agent/skills/ legacy | Workspace trust/host variant not exercised |
| Grok Build | [Public Skills](https://docs.x.ai/build/features/skills-plugins-marketplaces) · [upstream detailed Skills](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/08-skills.md) · [rules](https://github.com/xai-org/grok-build/blob/main/crates/codegen/xai-grok-pager/docs/user-guide/12-project-rules.md) | Public page lists .grok/skills/; upstream details additional .agents/ and .claude/ paths and deduplication; trust needed | Differences are version/document-surface dependent: use grok inspect, do not assume the winner or import de-dup |
| OpenSpec 2.x | [Setup](https://openspec.dev/docs/setup) · [Supported tools](https://openspec.dev/docs/supported-tools) · [Config](https://openspec.dev/docs/configuration/config-yaml) | Global Skills are default for init; --scope project needed for repo portability. Invalid config fields can be skipped with warning | No OpenSpec CLI installed or official validation run here; verify before adoption |
| Agent Skills format | [Specification](https://agentskills.io/specification) | name/description/frontmatter constraints described | CI performs a narrow subset of format checks, not a complete schema validator |
| Engineering principles | [OpenAI Harness Engineering](https://openai.com/index/harness-engineering/) · [Anthropic long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) | Supports concise entry, durable state and test feedback as useful design patterns | Research claims do not establish actual outcomes for this repository |

## Review process

Before extending the due date, **reopen official docs, compare the exact claims above, inspect release/compatibility changes, and update relevant project guidance**. Review sooner for release changes, API breakage, contradictory host behavior, or failed CI. The scheduled GitHub Action only checks this deadline and structure: **it cannot fetch current content or verify its meaning**.

Stable design principles do not require a weekly rewrite, but rapidly evolving CLI/tool discovery facts deserve frequent review. The date check exists to prevent silent indefinite staleness, not to certify current accuracy.
