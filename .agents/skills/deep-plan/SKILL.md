---
name: deep-plan
description: Investigate an unfamiliar or risky codebase change, resolve necessary user decisions, and create testable sequential implementation phases.
---
# Deep plan — substantial work only

1. **Inspect source first:** actual code/architecture, tests, prior related topic knowledge, Git changes and approved OpenSpec specs. Trace call/scene interfaces and existing reusable patterns; don't design from a summary alone.
2. Classify unknowns into directly checkable, reversible low-risk assumption, required user decision and risky blocker. Investigate checkable facts before asking; ask **focused** product/irreversible questions only. State assumptions; don't repeatedly ask already-settled questions.
3. Define user-visible acceptance, failure/edge cases, non-goals, compatibility constraints, baseline tests and real project QA needs. No fabricated result or guessed Godot API.
4. Plan **ordered, independently testable phases** in one OpenSpec proposal/design/`tasks.md`: phase goal, source boundaries, implementation slice, automated tests, runtime/visual/device verification, dependencies, pass/fail gate, rollback and approvals where applicable.
5. Do not begin a materially ambiguous or destructive phase until its required user decision is resolved. Routine reversible edits do **not** need ceremonial approval.
6. Present the phase overview and first actionable slice. Record dependencies and actual progress in canonical OpenSpec/STATUS rather than a duplicate task database. On completion distill durable knowledge per [documentation rule](../../../.agent-docs/rules/documentation.md).
