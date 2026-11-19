# Current architecture

- `harness/cli.py`: terminal entry point; stdlib Python >=3.10.
- `harness/tasks.py`: atomic task state, revisions, checkpoints, append-only task events, handoffs.
- `harness/index.py`: rebuildable SQLite FTS5 index. A cache, **never** an authority.
- `harness/context.py`: selective path/keyword retrieval and bounded Context Packets.
- `harness/verification.py`: subprocess gate execution, evidence, source fingerprint validation.
- `harness/checks.py`: doctor + link/config lint, no hardcoded agent provider.
- `.harness/tasks/`: durable project task state; commit to Git.
- `.harness/evidence/`: small machine-produced verification records; commit to Git when appropriate.
- `.harness/cache/`: local rebuildable index, intentionally ignored by Git.

Boundaries: task state changes use revision checks and locks; evidence gates must match current workspace fingerprint; approved decisions should not be overwritten to fit implementation.
