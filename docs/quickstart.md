# Quickstart — code first, minimal setup

Use Git and an agent with file access. This is a **template**; the actual Godot version, code and runtime/tests come from the real game repository. Python/SQLite are **not** required.

## New feature request
1. Ask “implement this feature.” Agent reads [AGENTS.md](../AGENTS.md), inspects relevant code/scenes, tests, Git and previous topic-specific decisions. It should **not** immediately ask generic questions already answered by the project.
2. Agent shares grounded understanding, clarifies only unresolved material user/product decisions, and proposes phase-by-phase acceptance/tests/rollback for nontrivial work.
3. After required decisions, the agent implements each phase **with tests**, runs actual required QA, fixes failures or reports a blocker; it does not mark an unverified phase complete.
4. At meaningful boundaries, OpenSpec/STATUS capture current work and [reusable knowledge](knowledge-reuse.md) is distilled into one canonical document and an optional topic pointer.

## Resume or revisit an old subject
- **Resume:** STATUS → active OpenSpec tasks → Git/code → next unfinished verified phase.
- **Revisit:** relevant code/tests → [topic map](../.agent-docs/topics.md) and old ADR/research/specs/history → verify relevance → extend existing design.

Read-only inspection examples:

```sh
git status --short
git log -5 --oneline
git diff
```

Optional documentation-only checks:

```sh
bash scripts/check-docs.sh
bash tests/docs-lint.sh
```

[Safe adoption](adopting-existing-project.md) · [Phases](task-lifecycle.md) · [Official OpenSpec](openspec-workflow.md) · [QA](verification.md). No missing tool result may be reported as PASS.
