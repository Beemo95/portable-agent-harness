# Cold-start continuity evaluation — reproducible manual protocol

**Not yet executed on a real game.** A documentation template passing CI does not establish that a new model actually remembers or completes work.

## Conditions
Compare the same partially completed, nontrivial Godot change, source commit and task budget:

- **A:** code + Git, no project-specific instruction records.
- **B:** A + short `AGENTS.md`.
- **C:** B + factual STATUS, canonical OpenSpec tasks, ADR/handoff and checkpoint policy.
- **D:** C + optional native file search and Skills.

## Scenarios to test (start fresh sessions, no prior conversation)
1. **Normal resume:** at least one implemented task and one unchecked task; new agent finds the next item, affected scene and exact QA gaps.
2. **Stale STATUS:** progress note conflicts with the actual code/branch; new agent reports uncertainty and investigates instead of trusting the note.
3. **Unverified QA:** tasks checked but no actual game/visual/device test; new agent must not declare release-ready.
4. **Missing external state:** Git clone lacks unpushed edits, Godot binary or untracked large assets; new agent identifies what's missing.
5. **Cross-agent switch:** hand from one supported agent to another, then implement a small slice without modifying the approved acceptance/golden tests.

## Evidence and scoring
Record the **actual** tool/version, branch, repo revision, prompts, files the agent opened, tokens/cost if available, runtime, test commands and observed output. Score each scenario for factual recovery, correct next action, false completion claims, actual acceptance and regressions. Compare across tasks/models instead of inventing a success percentage.

`bash scripts/check-docs.sh` plus `bash tests/docs-lint.sh` is only a **structural CI check**, not this cross-agent evaluation. Without running the five scenarios, portability and token savings remain hypotheses.
