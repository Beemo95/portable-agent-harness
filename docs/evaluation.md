# Evaluation playbook — falsifiable harness quality

## Compare strategies on identical tasks

- A: project files only, no harness cues.
- B: short AGENTS.md and docs index.
- C: B + task/checkpoint/handoff.
- D: C + lexical retrieval/context routing.
- E: D + meaningful verification gates.

Use the same starting Git commit, same task spec, same agent/model budget and tools where possible. Repeat across diverse tasks: tiny bug, new feature, cross-module refactor, UI change, factual research, paperwork. Have an independent assessor evaluate completion.

## Metrics

- Recovery correctness (what was actually completed / what remains).
- Critical context recall, false assumptions, stale-document reliance.
- End-to-end acceptance success rate.
- Accepted-task cost (tokens, retries, human intervention, runtime).
- Retrieval precision/recall and tokens consumed during initialization.
- Wrongly declared completion, regressions, authorization problems.

## Built-in smoke evaluation

`python3 scripts/harness.py eval cold-start` makes an isolated copy without `.git` and cached index; it runs doctor, lint and context. This tests **basic portability**, not complete replacement-PC or cross-model performance.

## Stronger manual acceptance

1. Commit a partly completed feature, including its checkpoint and task state.
2. Push branch and clone to a genuinely separate PC or clean VM.
3. Use a different model/agent with no prior conversation and only the cloned repo.
4. Ask it to retrieve the task, reconcile current files, correctly identify the next slice and implement it.
5. Compare actual output to independently held-out tests and assess artifacts.
6. Measure cost/tokens and repeat for baseline without structured task state.

Don't report "100% continuation" or "80% token reduction" without executing this protocol on multiple realistic tasks.
