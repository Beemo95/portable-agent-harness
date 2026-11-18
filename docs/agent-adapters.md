# Provider adapters and realistic compatibility

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
