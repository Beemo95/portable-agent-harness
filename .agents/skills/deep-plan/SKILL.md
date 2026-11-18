---
name: deep-plan
description: Resolve significant unknowns and decompose risky work into verifiable vertical slices.
---
# Deep plan — only when complexity warrants it

Use for greenfield architecture, feature interactions, risky migrations or unfamiliar APIs. For trivial bug fixes, prefer a concise plan with immediate verification.

1. **Inspect** actual code, tests, approved decisions and task contract; don't design from outdated summaries alone.
2. **Classify unknowns:** checkable fact (read docs / run tool), technical hypothesis (small spike), user product choice (ask), reversible low-risk choice (choose and record).
3. **Specify observable behavior:** success criteria, edge cases, out-of-scope constraints, and evidence needed.
4. **Compare alternatives** when design is uncertain (complexity, risk, reversibility, testability). Avoid large speculative research for settled decisions.
5. **Split vertically** into independently testable slices. Include dependencies, exclusive edit owners, file areas, rollback plan and time/compute budget.
6. **Predefine verification gates** and demand coverage of all acceptance criteria before coding.
7. Save approved contract/ADR references and first actionable slice; halt if a critical unapproved product decision blocks safe work.

Never silently change approved requirements, golden fixtures or API contracts just to make tests pass.
