---
name: feature-work
description: Execute planned code changes by small tested phases, preserving source evidence and reusable project knowledge.
---
# Feature work — implementation with gates

1. For any new/revisited feature inspect **actual** source, tests, Git, relevant prior decisions and [topic map](../../../.agent-docs/topics.md); for continuation read STATUS and the linked OpenSpec change.
2. Confirm acceptance, phase order and prerequisites. If a material product decision is unresolved, ask concisely after investigating; choose a documented reversible assumption for trivial details.
3. For substantial work use one OpenSpec `tasks.md` with bounded phases. Implement one vertical slice and add/update **appropriate automated unit/integration/scene tests and regression checks**.
4. Run the phase's applicable real checks and inspect outcomes. Fix/retest FAILs. Missing required evidence = NOT RUN / blocked, **not** successful completion or permission to skip to the next phase. Ask before formally deferring/scope-changing a required gate.
5. Update the **canonical** checklist for implemented work and STATUS for actual tests, changed code, pending risks and next phase; distinguish implementation and acceptance.
6. Distill long-lived findings into one authoritative architecture/ADR/spec/research record, then a pointer in [topics](../../../.agent-docs/topics.md) for recurring domains. Keep temporary iteration details in the worklog.
7. Commit/push non-secret changes when authorized for cross-PC handoff. Escalate to `deep-plan` only when real risk/unknowns justify it.
