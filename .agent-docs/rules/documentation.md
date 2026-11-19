# Documentation maintenance and handoff

## Write during meaningful work
- OpenSpec owns **what and why to build**: `openspec/specs/` (approved capability) and `openspec/changes/<id>/` (proposal/design/tasks).
- `.agent-docs/product.md` owns approved game vision. `.agent-docs/architecture.md` owns verified current technical boundaries. Keep them concise; edit only when their truths change.
- `.agent-docs/decisions/` records durable trade-offs/approval, including rejected alternatives and supersession.
- `.agent-docs/research/` records dated external evidence; `.agent-docs/worklog/` records meaningful iteration outcomes/problems, **not every tool call**.
- `.agent-docs/STATUS.md` links active changes, last verified facts, blockers and next action. It is a lightweight index, not another source for detailed specs.

## At task boundary (pause, handoff, PR, merge)
1. Reconcile source code and OpenSpec tasks: only tick completed work, leave uncertain items open.
2. Capture decisions or unexpected findings where they belong; update architecture when actual boundaries changed.
3. Update STATUS with active OpenSpec change, short outcome, **verified vs unverified**, exact next action, blockers and source/evidence links.
4. Include links to relevant logs/commits and any unresolved device/visual QA. Do not claim a Git clone will restore unpushed or ignored work.
5. Avoid dumping entire conversations, recreating the same data in several files, or overwriting historical ADRs. Archive obsolete worklog entries by link, not silent deletion.

**Minimum handoff:** goal; canonical spec/change; actual edited files; verified result and evidence; outstanding problems; next concrete step. See `.agent-docs/templates/handoff.md`.
