# Provider adapters — verify real host behavior

`AGENTS.md` is canonical. `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` and `.cursor/rules/` point to it. These files do not install software or magically enforce handoff.

- **Codex:** open the repository and read AGENTS/STATUS and actual Git/source. Official OpenSpec generates Codex Skills in `.agents/skills/openspec-*/` if you install them separately; check actual discovery.
- **Hermes:** set the workspace/project root; read AGENTS/STATUS, inspect Git and appropriate Skills. Messenger/chat memory is not authoritative. Verify installed Hermes version and Skill loading.
- **Grok / Antigravity / Gemini:** verify project file access, AGENTS routing, host skill location and actual command support. OpenSpec officially documents Antigravity's `.agent/skills/`; don't claim the same path works automatically in every Grok integration.
- **Claude Code:** `CLAUDE.md` points to AGENTS; optional specialist agents under `.claude/agents/` are Claude-specific.
- **Other agents:** use native file/Git tools and the same readable Markdown manually.

Use official [OpenSpec setup](openspec-workflow.md) instead of generating homemade copies of its workflow. No Python wrapper or MCP is required for the basic handoff. Keep one agent for simple work; isolate overlapping writers in separate branches/worktrees. Compare a fresh session against the original source and evidence before claiming portability.
