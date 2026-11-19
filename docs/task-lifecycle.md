# Phase-based development lifecycle — one OpenSpec checklist

## Substantial feature
1. **Discovery:** inspect actual code/scenes, tests, Git history, relevant approved specs and prior [topic knowledge](../.agent-docs/topics.md). Establish baseline and unresolved unknowns.
2. **Clarification:** investigate code-answerable questions; request only missing material product/irreversible decisions, with concise options. Low-risk reversible assumptions may proceed when stated.
3. **Plan:** write one OpenSpec proposal/design and ordered `tasks.md` phases. Each has outcome, affected code paths, dependencies, acceptance scenarios, automated tests/real runtime or visual-device QA, required gate and rollback. Get approval for material scope decisions, not every harmless edit.
4. **Execute:** implement **one phase at a time**, including suitable automated tests and regressions; run actual validation, fix/retest failures.
5. **Phase gate:** a phase is fully accepted only when every **required** check has observed PASS for the current source and scope. Failed, skipped or unavailable checks remain FAIL/NOT RUN and **block promotion**; document reason and seek a specific decision before changing the requirement or deferring a gate.
6. **Handoff:** mark implemented tasks in the one canonical checklist; STATUS links active change, current phase, verification, blockers and next action. Persist source/decision/evidence and Git-transfer state. Distill only durable reusable knowledge, with topic pointers to one canonical owner.

A tiny fix can use a short scoped plan, but still needs real verification appropriate to its impact. **Implemented ≠ tested ≠ visually/device verified ≠ released.**

## Concurrent agents
Scope separate branches/worktrees or nonoverlapping files; avoid changing the same scene/resource/STATUS concurrently. Cross-machine state is reconciled with Git, not a custom task database. A new session must inspect source and phase evidence before proceeding.

[Knowledge reuse](knowledge-reuse.md) · [Real QA](verification.md) · [Evaluation](evaluation.md).
