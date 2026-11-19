# ADR-0002 — Documentation-first, no custom task engine

**Status: Accepted. Supersedes ADR-0001's Python/SQLite implementation.**

## Decision
Keep `AGENTS.md` short, route selectively to Markdown and Skills, use `.agent-docs/status.md` for current recovery, and keep the canonical OpenSpec tasks, decisions and evidence in Git. Agents use **native file/Git search and actual project tests**.

Remove the Python CLI, SQLite index, `.harness/` task store, standalone context packet generator, custom verifier, bootstrap scripts and Python self-tests. No automatic multi-provider skill discovery is assumed.

## Rationale and trade-offs
A fresh clone with an agent should need no extra installed harness. A bespoke execution database creates duplicated progress and maintenance. The cost: STATUS can go stale and requires disciplined updates; uncommitted work isn't portable; native search might miss context; concurrent writers resolve through Git. Measure failures before adding optional tooling.
