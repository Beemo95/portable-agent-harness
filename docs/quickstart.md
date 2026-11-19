# Quickstart — no Python harness

**Core requirements:** Git and an agent with access to this repository's files. An actual Godot game must also have its own Godot installation, dependencies and test commands. OpenSpec's CLI is optional.

1. Clone/pull the actual project (`main` or the intended active branch), open it in Codex/Hermes/Grok or another code-capable agent.
2. Ask: “Read AGENTS.md. What work is active, what is implemented, what has actually been tested and what is the next action?”
3. The agent reads STATUS, active OpenSpec change/handoff and Git/source. If STATUS says `none`, it reports that and does not invent a feature.
4. Continue the first unfinished task using native file search and the original spec. Test with real game tooling.
5. At an important milestone or before a deliberate context switch, record compact facts, known failures, next action and transfer state. Commit/push non-secret changes as authorized.

Read-only Git inspection:

```sh
git status --short
git log -5 --oneline
git diff
```

Optional documentation-only integrity checks:

```sh
bash scripts/check-docs.sh
bash tests/docs-lint.sh
```

These are Bash checks **inside the template**, not required to run the harness in every adopted project. A missing test runner, stale Markdown or unpushed work must be reported rather than assumed good.

[Adoption](adopting-existing-project.md) · [Official OpenSpec optional setup](openspec-workflow.md) · [Recovery evaluation](evaluation.md).
