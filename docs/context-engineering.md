# Context engineering: selective native file lookup

## Cold start
1. Read concise STATUS and the linked active OpenSpec change/handoff; if no active work exists, say so.
2. Inspect current `git status`/`git log` and affected code/tests before trusting old status or checked tasks.
3. Read only task-specific source, rules, Skills, ADR/research and exact evidence needed. Use existing `rg`, `git grep`, `find` or host native search. Prefer paths/symbols over massive context dumps.
4. Summarize implemented, unimplemented, actual QA, unverified risks and **next smallest action**. If notes conflict with code, explicitly reconcile.
5. After consequential decisions, implemented slices, major failures, or before deliberate context compaction/switching, checkpoint just those facts into canonical OpenSpec/STATUS/handoff.

No SQLite index, bespoke token-budget packet, duplicate task database or background memory process. Native retrieval can miss context, and Git cannot restore unpushed files. Only introduce optional indexers after measured retrieval failures.

[Recovery experiment](evaluation.md) · [handoff policy](../.agent-docs/rules/documentation.md).
