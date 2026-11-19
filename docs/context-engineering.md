# Context engineering — selective native retrieval

When asked to resume, read STATUS, its linked OpenSpec change/handoff and relevant approved specs. Inspect real source/Git changes and test evidence before repeating claims. Retrieve task-specific rules, ADRs and matching paths using the agent's native file search, `rg`, `git grep` or `find`; don't load the whole repository.

A recovery answer should state **goal, implemented, remaining, tested, not tested, blockers, related revision and next action**. If STATUS disagrees with current code, surface the discrepancy. If no active work exists, say so.

No SQLite FTS5, route-hint JSON, artificial Context Packet budget or homemade summarizer. Native retrieval may miss context; measure failures before adding optional indexing or semantic search, keeping Markdown/source as the authority.
