# Git-native documentation harness

```text
New agent -> AGENTS.md -> short STATUS -> exact active OpenSpec change
                                      \-> relevant rules/Skills/ADRs/handoff
                                      \-> actual Git/source and QA evidence
                 execute project tests -> checkpoint Markdown + commit/push
                                      -> next session/model/PC
```

- **Code, Git and observed runtime** define what currently exists; spec/accepted decisions define intended behavior.
- **OpenSpec changes** own one implementation checklist (`tasks.md`); approved specs live in `openspec/specs/`. The official CLI/Skills are optional and not bundled.
- **STATUS** is a one-screen pointer to active work, tested/untested facts, blockers and next action, not the source of task history.
- **ADRs, research, worklogs and targeted handoffs** preserve durable rationale, with meaningful milestone checkpoints.
- **Bash CI** checks required docs, common local Markdown links and STATUS→change paths; it cannot test games or semantic truth.

No Python/SQLite/task DB/context-packet engine. **`scripts/` and `tests/` are explicitly allowed** because real games need them. Git clones transfer only pushed non-secret state; actual cross-agent continuity remains to be tested.

[Official OpenSpec workflows](openspec-workflow.md) · [evaluation](evaluation.md).
