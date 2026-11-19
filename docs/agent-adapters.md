# Agent adapters — tested configuration contracts, not tested model behavior

**Source of truth:** `AGENTS.md`. Every agent must use the **actual game repository root**, current Git/code, canonical OpenSpec changes and project evidence. No chat-side memory is the project's source of truth. The templates do not guarantee that an agent will honor every instruction.

| Agent | Always-on project instructions | Project Skills | Verify in the actual client |
| --- | --- | --- | --- |
| Codex CLI / IDE | `AGENTS.md` | Shared `.agents/skills/<name>/SKILL.md` | New project session; ask it to describe the loaded instructions and available Skills |
| Cursor | Root `AGENTS.md` (native support) | Shared `.agents/skills/<name>/SKILL.md` | New project Agent session; inspect applied rules and Skills |
| Claude Code | `CLAUDE.md` contains `@AGENTS.md` (native import) | Portable forwarding adapters at `.claude/skills/<name>/SKILL.md` | Run `/context all` (and inspect the Skills menu); confirm root guidance is present |
| Grok Build | `AGENTS.md` | Claude-compatible `.claude/skills/` forwarding adapters; do not assume automatic repo-local `.agents/skills/` scanning | Run `grok inspect` in a **trusted** project; check listed instructions/Skills |
| Google Antigravity (AGY) | Root `AGENTS.md` | Shared `.agents/skills/` (current location; `.agent/skills/` is legacy) | Open workspace Customizations → Rules/Skills; confirm loaded project paths |
| Gemini CLI (extra) | `GEMINI.md` imports `@./AGENTS.md` | Verify active client and installation separately | Use `/memory show` to verify imported instructions |
| Hermes Agent (extra) | Requires correct workspace root and instruction discovery | May require a tool-specific linked skill path/initialization | Inspect Hermes's actual loaded instructions and Skills; don't infer from filenames |

**Why there are 2 Skill folders:** `.agents/skills/` holds the **canonical 12 Skills**. Claude Code discovers project Skills under `.claude/skills/` instead. Each checked-in Claude adapter has the same name/description and **points to the canonical SKILL.md**, avoiding symlinks (which are unreliable in Windows clones) and avoiding duplicated full instructions. Some Grok versions also discover those Claude adapters. Changes to a Skill's trigger description should be mirrored in its adapter; CI checks names/paths, not semantic equivalence.

**No ceremonial prompt needed:** in a correctly configured workspace, the user can simply ask for a feature. A fresh-session test must verify which rules and Skills actually loaded. Host settings, versions, workspace trust and higher-priority instructions may change behavior.

**OpenSpec:** the upstream CLI and generated `openspec-*` workflows are **optional and not bundled**. See [official setup](openspec-workflow.md); avoid assuming the 12 project Skills are replacements for upstream OpenSpec workflows.

Official references: [Claude memory](https://code.claude.com/docs/en/memory) · [Claude Skills](https://code.claude.com/docs/en/skills) · [Cursor rules](https://cursor.com/docs/rules) · [Antigravity Skills](https://antigravity.google/docs/skills) · [Grok Build Skills](https://docs.x.ai/build/features/skills-plugins-marketplaces) · [OpenSpec supported tools](https://openspec.dev/docs/supported-tools).
