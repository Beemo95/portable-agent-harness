# Game specification and phase planning

Use for meaningful changes to gameplay, UI flow, save data, balancing or cross-module behavior. For trivial bugs, keep the plan short.

1. **Code-first:** read relevant `project.godot`, source scenes/scripts, signals/interfaces, tests, product intent, approved specs and past related decisions. Search [topic map](../topics.md) and current code, not just STATUS.
2. Classify unknowns: inspect/research what is answerable; make explicit reversible low-risk assumptions; ask focused questions **only** for user-controlled product choices, conflicting acceptance or blocking/irreversible decisions. Provide alternatives and consequences instead of open-ended questionnaires.
3. Define player-visible behavior, inputs/transitions, failures, restart/save semantics, compatibility, accessibility/platform (including touch/aspect ratio if applicable), and non-goals. Define measurable acceptance scenarios rather than vague implementation tasks.
4. For substantial work, write proposal/design and **ordered, bounded phases** in the canonical `openspec/changes/<slug>/tasks.md`. Each phase names code area, acceptance, test method/expected result, dependencies, rollback and approvals if needed. The official OpenSpec CLI/Skills may author these files; no second planning store.
5. Verify baseline and identify risks *before* large edits. When scope/UX/product choice is materially ambiguous, obtain a decision before implementing it; do not demand an approval ceremony for routine reversible fixes.
6. After each phase, reconcile implementation and actual evidence before moving on. At closure, update approved specs following the actual OpenSpec workflow and distill reusable architecture/rationale with evidence and [topic pointers](../topics.md).

**Minimum substantial plan:** what/why, relevant existing code, accepted behavior, out of scope, phases and dependencies, acceptance/tests/required QA per phase, risks/rollback, unresolved decisions and next action. Checked boxes are not proof of tests.
