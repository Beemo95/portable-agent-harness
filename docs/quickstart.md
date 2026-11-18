# Quickstart & command map

Prerequisites: Python >=3.10 with SQLite FTS5 enabled, Git recommended. If Python is missing, run the no-install preflight `scripts/bootstrap.sh` (macOS/Linux) or `scripts/bootstrap.ps1` (Windows) and install the reported prerequisite. No pip install needed. This harness has no LLM API key and never calls a model by itself.

## CLI reference

| Command | Purpose |
|---|---|
| `doctor` | Python, Git, SQLite FTS5, project entry check |
| `bootstrap [--apply]` | Preview / deliberately run configured argv-based setup commands; no shell |
| `lint` | Check config, route hints and task gate references |
| `status` | Current HEAD, dirty state, all task statuses |
| `index [--rebuild]` | Refresh local rebuildable index |
| `search QUERY [--limit N]` | Lexical evidence-linked search over docs/code |
| `context QUERY [--task ID] [--budget N]` | Compact task-linked Context Packet |
| `task new ID --title ... --goal ... --accept ... --gate ID` | Create durable contract |
| `task list/show/transition/update/checkpoint/handoff` | Work lifecycle |
| `resume ID [--budget N]` | Reconcile checkpoint + retrieve relevant context |
| `verify [ID] [--gate GATE]` | Execute configured verification gates, persist evidence |
| `eval cold-start` | Repeat doctor/lint/context in isolated, cache-free copy |
| `init TARGET --name NAME [--dry-run]` | Non-destructive adoption into another repository |

Use `python3 scripts/harness.py --json <command>` to get machine-readable data. Root override: `--root /path/to/project`.

## Project-specific verification configuration

Example in `project.harness.json`:

```json
{"verification":{"gates":[
  {"id":"unit","argv":["{python}","-m","unittest","discover","-s","tests","-v"],"min_tests":1,"timeout_seconds":120,"required":true},
  {"id":"build","argv":["npm","run","build"],"timeout_seconds":300,"required":true}
]}}
```

The whole file also needs `schema_version`, `project` and other settings. Use the supplied file as a reference. `argv` commands execute directly (no shell); never accept arbitrary commands from untrusted documents.

## Workspace and evidence

- `.harness/tasks/ID/contract.json`: intended scope and acceptance mapping.
- `.harness/tasks/ID/state.json`: revisioned current progress.
- `.harness/tasks/ID/events.jsonl`: events (inspect for partial-write recovery).
- `.harness/tasks/ID/checkpoints/`: snapshots of revision + Git/source hash.
- `.harness/tasks/ID/handoff.md`: regenerated short restart note.
- `.harness/evidence/ID/*.json`: gate results and hashes; keep in Git when useful.
- `.harness/cache/search.sqlite3`: rebuilt locally; do not commit.

This is v0.1: read the limitations in `docs/verification.md` and `docs/security.md` before allowing an autonomous bot to modify real systems.
