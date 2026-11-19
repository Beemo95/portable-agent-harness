# Architecture — Git-native, code-first workflow

```text
New feature: current code/tests/Git → prior topic knowledge → focused user decisions
            → one OpenSpec phased plan → implement + tests → gate → next phase
                                       ↘ durable canonical knowledge + topic pointer

Resume: STATUS → current OpenSpec phase/handoff → reconcile Git/source/QA

Later related feature: current code → topic map → ADR/architecture/spec/research
                     → revalidate with tests → reuse or update implementation
```

- **Code + Git + observed runtime** show current actual behavior; approved specs and decisions define intent.
- **OpenSpec** owns the one implementation checklist, ordered phases and accepted outcomes.
- **STATUS** points only to active work; it is **not** all historical memory.
- **Topic map** is a compact navigation layer for recurring subjects; facts remain in a single canonical spec, architecture, ADR or verified research document.
- **Worklogs and short handoffs** preserve useful one-time evidence. Only reusable findings are distilled; never copy whole conversations.
- **Bash documentation CI** checks files, common relative Markdown links and active change targets; it does not test game runtime or model adherence.

No Python runtime, SQLite DB, always-on memory service, homemade context-packet generator, or duplicate task state. Git cannot recover hidden model thought, ignored files or unpushed work.

[Detailed development lifecycle](task-lifecycle.md) · [Knowledge policy](knowledge-reuse.md) · [Real-world evaluation](evaluation.md).
