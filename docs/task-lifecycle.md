# Task lifecycle, checkpointing, resume, concurrency

```
backlog -> ready -> in_progress -> verifying -> done
    |         |             |              |
  blocked <- blocked <------ blocked   changes_requested
              ^                            |
              +---------- in_progress <---+
```

`task transition` validates legal moves. `ready` requires acceptance criteria mapped to configured gates. `done` requires latest evidence with passing gates that match current source digest and Git HEAD, no blockers, and no pending human approval. Merely passing unrelated tests is insufficient: owners must configure *meaningful* acceptance tests.

## Task contract

`contract.json` is user/owner-approved desired behavior; `plan.md` contains a lightweight optional discovery and vertical-slice plan; it has acceptance records with gate IDs. Agents must not change it to conceal implementation problems. Record significant decisions in ADRs, and only edit acceptance after explicit re-scoping.

## Revision & isolation

State writes require `--expect N`, an optimistic compare-and-swap guard. An exclusive `.write.lock` prevents some same-filesystem races; if a process is killed and a lock remains, inspect carefully before removing it. For multiple PCs, use separate Git branches/worktrees per Feature and review merges; revision checks alone do **not** solve distributed conflicts.

## Checkpoint and handoff

- Record important transitions, finished slices, actual test output references and Git changes.
- `checkpoint` stamps source content fingerprint and current Git HEAD.
- `resume` compares the current fingerprint against the last checkpoint and warns on drift.
- `handoff` generates a short restart note pointing back to structured state.
- Commit and push all current changes before expecting a clean clone to reproduce them. Local uncommitted work is not portable.

## Crash consistency

Atomic JSON writes reduce partial-file corruption, while events are append-only. There is not yet a fully transactional database spanning state, checkpoint and event log; after a crash, inspect for mismatches and re-run `lint`. Never silently infer success from a partial event.

## Integration with agents

Any terminal-capable agent reads AGENTS.md and invokes the commands. A coordinator may create an isolated worker and give only `task_id`, project root and approved scope. Task data is shared; long reasoning transcripts are not.
