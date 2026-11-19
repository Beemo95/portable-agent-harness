# Provider adapters and realistic compatibility (v0.2)

Official OpenSpec tool generators provide Agent Skills to supported tools including Claude, Codex, Gemini, Hermes and vendor-neutral `agents`. PAH does **not** reproduce vendor-specific skill templates. See `docs/open-source-stack.md`; run upstream `openspec init --tools claude,codex,gemini,hermes,agents` only after reviewing its changes and installation requirements.

The robust contract is the CLI and repo state, not a particular bot runtime.

## Codex CLI

From the repository root, direct the agent to `AGENTS.md`; `python3 scripts/harness.py doctor`; `status`/`resume`; task-specific `context`; then the appropriate verify gate. This project does **not** install Codex plugins or invoke OAuth.

## Grok CLI / Antigravity / Gemini CLI

A thin `GEMINI.md` pointer and explicit tool commands are provided. Verify the actual agent reads the pointer and has terminal permission. No promise is made that all products auto-discover `.agents/skills/`.

## Hermes / generic terminal agents

Provide repository root and task ID. Use the CLI to discover progress and retrieve context. Hermes personal memory is optional, not the source of truth. Worker jobs should return structured gate evidence and paths, not the entire transcript.

## Claude Code / other assistants

The `CLAUDE.md` pointer sends users to canonical `AGENTS.md`. Verify which startup file the installed version actually reads. For an agent that cannot run terminal commands, use a trusted wrapper to expose the same CLI methods; a future MCP adapter can help but is not included in v0.1.

## Multi-agent policy (platform-independent)

- Only one writer to a task state revision at a time; `--expect` enforces freshness.
- Independent workers use separate worktrees and nonoverlapping file ownership when modifying code.
- QA should read original acceptance criteria and actual artifacts; avoid sharing only developer-produced summary.
- The orchestrator routes tasks, while command execution and status guards belong to deterministic tools.
- Every agent must compare repository status on resume; never trust an old context packet blindly.

## Godot-first specialist profiles

The canonical optional roles are in `.agent-docs/agents/`. Claude Code project subagents are in `.claude/agents/godot-*.md` with frontmatter and a short pointer to the canonical role brief. Other runtimes do not automatically read `.claude/agents/`; configure their own adapters explicitly. The `.agents/skills/` entries follow Agent Skills conventions but discovery and invocation depend on the installed host.

Do not spawn all agents for every task. Director defines acceptance, Developer implements, Artist supplies actual sources and visual evidence, QA independently checks, Researcher verifies external facts; handoffs reference the same OpenSpec change and STATUS.
