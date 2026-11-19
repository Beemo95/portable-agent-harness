# Workflow — code-first discovery, clarification, phases, verification

## 0. Choose the right entry
- **Resume active work:** inspect STATUS and linked change/handoff, current Git branch, diff, commits and affected code before answering what's next.
- **New work or revisit an old domain:** inspect relevant source, existing tests, `project.godot`/tool versions, approved specs, project architecture and [topic pointers](../topics.md). Search earlier ADRs, research, worklogs, completed/archived OpenSpec changes and Git history **when relevant**, even if STATUS currently points to unrelated work.
- Use [knowledge retrieval and distillation](../../docs/knowledge-reuse.md). Read the matching rule/Skill only as needed, not every file. Report unavailable source access as a blocker; do not invent a codebase analysis.

## 1. Discover and resolve only blocking unknowns
1. Trace feature paths, data flow/interfaces, ownership, dependencies, existing tests and affected regression areas. Establish what the current code actually does.
2. Check whether previous verified decisions/implementations already answer the request. Compare those records against current code and dependency versions; flag stale or superseded facts.
3. List outstanding unknowns as **checkable fact / reversible assumption / user decision / unsafe blocker**.
4. Investigate checkable facts. Ask **focused user questions only for materially ambiguous product/creative decisions, conflicting acceptance, destructive or irreversible changes, or unsafe missing prerequisites**. Offer options with impact. Do not ask for already recorded answers. If minor and reversible, state an assumption and proceed.
5. Do not silently implement a materially ambiguous outcome while awaiting an essential user decision.

## 2. Plan substantial work before modifying it
- For nontrivial features, create or update **one** OpenSpec change with proposal/design and `tasks.md`. Show a short phase overview first when important scope or irreversible decisions need approval. Small bug fixes can use a compact inline plan.
- Each **phase** must specify: goal and observable acceptance, relevant code/assets, dependencies and order, implementation tasks, tests/regressions (and visual/device QA where appropriate), completion gate, risks/rollback and any user approvals.
- Each phase should produce an independently checkable vertical slice. Do not front-load a large speculative architecture or duplicate OpenSpec checklists in STATUS.
- Baseline verification comes before risky edits. A plan is **ready to implement** once required user decisions are resolved and acceptance/validation are clear. Don't require ceremonial approval for every harmless edit.

## 3. Implement one phase at a time
1. Check the phase's prerequisites and original acceptance; inspect real current files and any previous phase's evidence.
2. Implement the smallest useful slice. Add/update appropriate automated tests (unit, integration or scene/gameplay) for new behavior and regressions; when code is not testable automatically, give a concrete manual verification procedure and mark automation limitations.
3. Run relevant real tests, import/build checks, then GUI/device checks for changes needing them. Fix failures and re-run. **Never replace a visual/device requirement with headless-only evidence.**
4. **Gate:** do not label a phase PASS or advance if a required check failed, was skipped or cannot run. Record FAIL/NOT RUN and reason; resolve blocker or request a scoped acceptance/plan decision. An intentionally deferred optional device/release test may remain open only if explicitly classified as such, not silently passed.
5. Update canonical `tasks.md` only for genuinely implemented items; record verified vs unverified, commands, environment, code revision, blockers and next phase in STATUS/handoff. Continue sequentially unless the user paused or a blocker requires input.

## 4. Distill useful project knowledge
- At meaningful decisions, discoveries, regressions or completed phases, extract **reusable** facts that will help future unrelated tasks. Examples: coordinate/depth-sorting rules, save format contracts, proved bug causes, platform constraints, test procedures.
- Store each fact in **one canonical place**: approved behavior in OpenSpec specs, current technical boundary in architecture, rationale in ADR, sourced findings in research. Reference actual code, tests, version and evidence. Keep incidental execution in worklog and a *pointer only* in [topics](../topics.md).
- Do not document trivial details, record speculative guesses as proven, or duplicate source code into large memory files. When revisiting a topic, verify prior knowledge against current implementation and mark outdated decisions as superseded.

## 5. Handoff
- Check Git + code + OpenSpec, update factual STATUS and (for substantial work) a concise [handoff](../templates/handoff.md).
- Before deliberate session/model switch or context compaction, capture next smallest action and unresolved questions.
- Commit/push required non-secret work only when authorized; explicitly report uncommitted/ignored/external state. A fresh agent must reconcile claims with evidence.

**Completion is multidimensional:** implemented ≠ automated tested ≠ visually/device verified ≠ shipped. Never claim tool execution without evidence.
