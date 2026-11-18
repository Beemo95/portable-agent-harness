# Portable Agent Harness (PAH) v0.1.0

**A working, model-neutral project harness.** Clone this repository onto a different computer, install Python 3.10+ and your preferred AI agent, and recover project tasks **from the files**, not from its chat history or personal memory.

> This is an independent, reusable **template + executable CLI**, not a preconfigured GrokBot/Hermes agent. No proprietary model API, SaaS, package installation or database server is required. For a new project, verification gates and domain knowledge must be configured using that project's real commands and facts.

## What it actually implements

| Area | Working implementation |
|---|---|
| Cold entry | Short `AGENTS.md`, CLI doctor, clear docs index |
| Search | SQLite FTS5 lexical search with route hints; rebuilds locally on a fresh machine |
| Context packets | Task-specific sources + current Git HEAD with conservative excerpt budget |
| Durable task state | Versioned `contract.json` / `state.json`, optimistic revision check, append-only events |
| Checkpoints and handoff | SHA-256 source fingerprint, Git state, generated recovery instructions |
| Verification | Run configured commands without shell, detect zero tests, store output hashes, block stale evidence |
| Lifecycle | Guarded state transitions; `done` blocked unless current required tests pass |
| Harness lint | Broken route hints, missing gates, stale pointer issues |
| Fresh-machine simulation | Clean isolated copy with no index/agent state: doctor + lint + context |
| Adaptation | Install same tooling into a separate repository without overwriting existing files |

This **does not** claim semantic task correctness, fully automated product approvals, cloud credentials/secret migration, UI testing without a GUI, guaranteed token savings, or out-of-the-box integration with every agent runtime.

## 60-second start (macOS/Linux)

If only an agent and the Git checkout are available, `sh scripts/bootstrap.sh` reports missing prerequisites without installing anything. On Windows use `scripts/bootstrap.ps1`.

```bash
# unzip the distribution or clone a repository containing these files
cd portable-agent-harness
python3 scripts/harness.py doctor
python3 scripts/harness.py lint
python3 scripts/harness.py status
python3 scripts/harness.py context 'How are task checkpoints restored?'
python3 scripts/harness.py search 'checkpoint Git source fingerprint'
python3 scripts/harness.py verify
python3 scripts/harness.py eval cold-start
```

Windows PowerShell:

```powershell
py scripts/harness.py doctor
.\scripts\harness.ps1 context "task resume"
.\scripts\harness.ps1 verify
```

For Python environments that expose the executable as `python` instead of `python3`, replace accordingly.

## Add the harness to another project

```bash
python3 scripts/harness.py init ../my-new-project --name "My Project" --dry-run
python3 scripts/harness.py init ../my-new-project --name "My Project"
cd ../my-new-project
python3 scripts/harness.py doctor
python3 scripts/harness.py lint
```

`init` refuses collisions; it never overwrites an existing `AGENTS.md`, codebase or work history. For an existing project that has its own `AGENTS.md`, see `docs/adopting-existing-project.md` for safe manual migration. A new project begins with **zero verification gates**, intentionally preventing a generic harness self-test from being mistaken for application correctness. Add actual project gates to `project.harness.json` before moving tasks to `ready`.

## Create, execute, checkpoint, verify, resume

```bash
python3 scripts/harness.py task new F-001 \
  --title "Reliable context lookup" \
  --goal "Find related files for the requested task" \
  --accept "Relevant files are returned for the query" \
  --gate unit --gate compile
python3 scripts/harness.py task transition F-001 ready --expect 0
python3 scripts/harness.py task transition F-001 in_progress --expect 1
python3 scripts/harness.py context "context search behavior" --task F-001
# edit code + tests in small slices
python3 scripts/harness.py task update F-001 --expect 2 --next "run updated tests" --completed "identified relevant files"
python3 scripts/harness.py task checkpoint F-001 --expect 3 --note "context lookup implementation in progress"
python3 scripts/harness.py task handoff F-001
python3 scripts/harness.py resume F-001
python3 scripts/harness.py verify F-001
python3 scripts/harness.py task transition F-001 verifying --expect 4
python3 scripts/harness.py task transition F-001 done --expect 5
```

The `--expect` number is a **current state revision**, not a scripted magic value. Re-read `task show` whenever another agent may have modified it. `done` requires the last verification run to pass all mapped gates on the **same current source fingerprint and HEAD**. A passing command proves the command succeeded, **not** that each natural-language acceptance criterion was meaningfully tested; write appropriate project-specific tests and review the diff.

### Recovery on another PC

1. Save and commit task state, source changes, relevant evidence and required non-secret artifacts. Push the branch. WIP changes that are not committed or otherwise transferred **cannot** be reconstructed from Git alone.
2. Clone on the new machine, install Python 3.10+ and Git, run `doctor` and `bootstrap` (explicit configured commands only).
3. Run `status`, `resume TASK-ID` and `context 'requested work' --task TASK-ID`.
4. **Reconcile** the checkpoint with actual sources, Git status, tools, tests and unavailable external services.
5. Continue work, then `verify` and `checkpoint`; repeat until the required gates and product acceptance criteria have been satisfied.

## Key design choices

- **Source of truth:** code/runtime for actual current behavior; approved product requirements for intent; ADR for rationale; evidence for proof of command execution.
- **Portable:** Markdown/JSON+Git are authoritative; `.harness/cache/` SQLite index is disposable.
- **Cheap by default:** keyword/symbol retrieval before embeddings; no LLM tokens are consumed by CLI itself.
- **No false completion:** zero tests fail a gate that specifies `min_tests`; code drift invalidates evidence; unconfigured gates block task closure.
- **Scoped information:** task contracts, route hints, retrieved file paths; no mass injection of `ai-docs` into every prompt.
- **Agent-independent:** every provider can invoke the same command via a terminal; provider-specific instruction files are pointers.

## Docs

- [Quickstart and commands](docs/quickstart.md)
- [Architecture and authority](docs/architecture.md)
- [Context retrieval and budgets](docs/context-engineering.md)
- [Task lifecycle and concurrency](docs/task-lifecycle.md)
- [Verification and limitations](docs/verification.md)
- [Security and permissions](docs/security.md)
- [Adopting an existing codebase](docs/adopting-existing-project.md)
- [Agent compatibility and adapters](docs/agent-adapters.md)
- [Evidence, methodology and research references](docs/research-basis.md)
- [Evaluation playbook](docs/evaluation.md)

## License

MIT. See `LICENSE`.
