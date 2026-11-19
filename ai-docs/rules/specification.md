# Game specification and feature planning

Use for new mechanics, balancing, UI flows, persistent data changes and scope decisions. Prefer official OpenSpec files rather than a second requirements tracker.

1. Read `ai-docs/product.md`, current relevant specs in `openspec/specs/`, and affected scene scripts; state player problem and target platform.
2. Describe the player-visible behavior, inputs, transitions, fail/edge cases, restart/save semantics, accessibility where relevant and performance constraints.
3. Define acceptance scenarios with observable outcomes, not only implementation steps. Include mobile touch/rotation/aspect ratio if applicable.
4. For significant changes, keep proposal/design/tasks under `openspec/changes/<slug>/`; use actual upstream CLI when available and record when unavailable.
5. Mark decisions requiring user approval (creative direction, monetization, non-reversible content) instead of silently choosing.
6. After implementation, update the approved specs per the project's OpenSpec workflow; checked tasks are not proof of QA.

**Spec minimum:** goal; player flow; non-goals; acceptance criteria; compatibility/saves; risks; affected scenes; validation approach. Small defect fixes do not require an elaborate proposal.
