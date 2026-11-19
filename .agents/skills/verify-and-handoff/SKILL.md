---
name: verify-and-handoff
description: Independently check project acceptance and record a factual Markdown/Git handoff.
---
# Verification + handoff
1. Read original approved spec/change and inspect actual code/Git diff, not only developer claims.
2. Run **real project** tests, runtime, visual or device checks as appropriate. Missing tools = NOT RUN.
3. Record exact commands, revision, environment, observed PASS/FAIL/NOT RUN, evidence and remaining gaps.
4. Do not rewrite tests or approved acceptance simply to claim PASS.
5. Update implemented items in the canonical OpenSpec checklist and STATUS; link a short handoff if needed.
6. Commit/push non-secret artifacts for future sessions. No custom Python verifier or task checkpoints.
