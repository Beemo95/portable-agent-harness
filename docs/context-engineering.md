# Context engineering: relevant information, not maximal information

## Pipeline

1. Identify task ID if given; read `contract.json` and state before search.
2. Match route hints (`.harness/context-routes.json`); never treat hints as exhaustive.
3. Refresh SQLite FTS5 cache from current repository files and search source/doc chunks.
4. Prefer exact path/symbol references; surface path + line range + short excerpt.
5. Inspect current full source (when actually modifying it); identify contradictions.
6. Expand search only when necessary; do not load whole `project` into every agent turn.

## Token budget

CLI `--budget` applies a conservative character heuristic to retrieved excerpts. It is **not** a tokenizer-accurate hard context limit, and task metadata outside excerpts can be longer. Calibrate against your actual model tokenizer and measure retrieval recall. Default 1,800 tokens is a *starting heuristic*, not experimentally proven universal optimum.

## Index behavior

- `.harness/cache/search.sqlite3`: optional disposable cache; regenerated if missing or changed local metadata.
- Exact identifier/path search works well; FTS5 in particular may miss Korean substrings, synonyms, or semantic relations. Route hints and broader query variants help. Do not assume hybrid semantic retrieval is included in v1.
- `AGENTS.md` is not indexed because the agent already has its rules; secret-like files (.env/key/pem) and binary assets are excluded from lexical index.
- In shared or sensitive repos, configure access controls **outside** the indexer. File exclusion rules alone are not an authorization boundary.

## Future extensions, based on benchmark need

Hybrid semantic retrieval, symbol graph and git-diff-aware indexing should be added only after measuring failed retrievals on realistic queries. Keep them replaceable and cache-only.
