# Host-specific adapters and compatibility

`AGENTS.md` is the canonical entry. `CLAUDE.md`, `GEMINI.md`, `.github/copilot-instructions.md` and `.cursor/rules/` point to it.

- **Codex:** open repository, read AGENTS/STATUS, follow relevant change and Git/source.
- **Hermes:** configure workspace/project root, read AGENTS/STATUS; chat/personal memories are not authoritative project evidence.
- **Grok, Antigravity, Gemini:** load AGENTS explicitly where not automatically discovered; confirm file/Git tool access in the actual installed version.
- **Claude Code:** pointer in CLAUDE.md; optional Claude-only agents in `.claude/agents/`.
- **Other agents:** follow the same instructions manually. No Python wrapper/MCP adapter is required.

`.agents/skills/` is an **optional** on-demand library; availability and auto-discovery vary by host. OpenSpec's upstream CLI may generate additional adapters; review changes before installing. Use one agent by default, scoped delegation when useful and separate worktrees for overlapping edits.
