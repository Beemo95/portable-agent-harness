---
name: deep-plan
description: Plan risky changes in small verifiable slices without a duplicate task contract.
---
# Deep plan
1. Inspect source, tests, approved specs, ADRs and the active OpenSpec change.
2. Classify checkable facts, hypotheses and user product decisions; request approval when necessary.
3. Specify observable acceptance, failures, non-goals and important compatibility constraints.
4. Compare alternatives only as needed, then split into verifiable slices with ownership and rollback.
5. Record proposal/design/tasks in **one** OpenSpec change. Do not duplicate them in a task database.
6. Keep STATUS short with current slice, blockers and next action; never rewrite acceptance because tests failed.
