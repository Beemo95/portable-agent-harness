# Methodology & references

Design principles distilled from public engineering practice; this implementation itself must be assessed with the included evals. Neither source popularity nor a paper by itself proves this is the optimal project harness.

- Anthropic, **Effective harnesses for long-running agents**: explicit initialization, feature status, and handing work to a fresh session. https://www.anthropic.com/research/effective-harnesses-for-long-running-agents
- Anthropic, **Building effective agents**: start simple; add orchestration/worker patterns only when useful. https://www.anthropic.com/research/building-effective-agents
- Anthropic, **Context engineering for AI agents**: retrieve relevant context instead of repeatedly loading all available text. https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- GitHub **Spec Kit**: specify -> plan -> tasks -> implement. https://github.com/github/spec-kit
- Fission AI **OpenSpec**: change contracts separate from permanent specs. https://github.com/Fission-AI/OpenSpec
- Obra **Superpowers**: structured design, debugging, tests and verification. https://github.com/obra/superpowers
- **AGENTS.md** convention: provider-neutral project entry. https://agents.md/
- **Dev Containers**: reproducible container-based development toolchains. https://containers.dev/
- SQLite **FTS5**: built-in local search index. https://www.sqlite.org/fts5.html

## Why these principles?

1. Short entry instructions reduce accidental always-on context.
2. Source files and Git artifacts provide durable, inspectable cross-session state.
3. Disposable search indexes avoid coupling portable state to local caches.
4. Small task contracts make intent and quality criteria explicit.
5. Execution-backed evidence reduces unsupported "done" claims.
6. Isolated verification and model replacement should be measured rather than assumed to improve quality.

The files in this project are a **new, original implementation**, not copied from the listed projects. Before claiming improvements, run the comparative experiments in `docs/evaluation.md` on your own work.
