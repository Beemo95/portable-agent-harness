# Context engineering — recover status or related historical knowledge

## Two entry paths, one set of actual source facts
- **Continue active task:** read STATUS and linked OpenSpec change/handoff, current branch/diff, code, tests and evidence.
- **New or recurring subject:** start with relevant current source and tests, then [topic map](../.agent-docs/topics.md) and native search across approved specs, architecture, ADRs, evidence-backed research, related worklogs, archived/completed changes and Git history. STATUS might point to a different topic and is **not** the complete project memory.

Before asking the user, resolve checkable technical unknowns through source/doc/tool inspection. Flag stale decisions, branch mismatches and missing actual evidence. For small reversible choices record the assumption; for material product decisions ask focused alternatives. [Code-first phased workflow](../.agent-docs/rules/workflow.md).

## Efficient selection
Use exact path/symbol searches first; broaden with aliases, including Korean/English variants (e.g. isometric/아이소메트릭, depth sorting/Y-sort), as needed. Use native `rg`/`git grep`/`git log` or host search. Don't read all Skills/docs. Where stable reusable findings exist, follow **pointers to one authoritative source**, not multiple copied summaries.

At key decisions, implemented phases, failures or before deliberate context compaction/switching, distill only durable verified knowledge to a canonical spec/architecture/ADR/research owner and update a small topic pointer if recurring. Capture operational progress in STATUS/OpenSpec.

Native search can miss context; a Git clone cannot restore ignored/unpushed state. No Python/SQLite/embeddings or magic model memory guarantees.

[Knowledge reuse](knowledge-reuse.md) · [Evaluation](evaluation.md).
