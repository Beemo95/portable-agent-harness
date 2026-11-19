# Architecture — repository-native documentation

```text
User → AI agent → AGENTS.md → STATUS → linked OpenSpec/ADR/handoff
                                           ↓
                             actual Git + source + selected rules
                                           ↓
                            real project tests and honest evidence
                                           ↓
                               update Markdown, commit/push
                                           ↓
                               next session / machine / model
```

- **Git and real source:** what exists and changed; actual tests show observed behavior.
- **OpenSpec:** approved specs, feature proposals/design, **one** implementation checklist.
- **STATUS:** brief index to active work, verified facts, blockers and next concrete action. Reconcile against Git.
- **Decisions/research/worklogs:** preserve rationale, evidence and historical transitions.
- **Skills/role adapters:** optional. No promise of automatic cross-provider discovery.

No Python package, SQLite FTS5 index, `.harness/` task store, separate context packet system, custom verifier or bootstrap executor. Use agent-native file/Git lookup. Adding extra search tools is a measured future choice, not part of the default.

Git carries **committed non-secret files**, not hidden reasoning, uncommitted edits, external access or device state.
