---
name: verify-and-handoff
description: Independently check acceptance and create portable next-session handoff.
---
# Verify, classify and hand off

1. Read the *original* user-approved acceptance criteria and the current source diff, not only the implementer's completion narrative.
2. Run task-specific automated gates with `python3 scripts/harness.py verify TASK-ID`.
3. Check saved evidence corresponds to the current HEAD and workspace fingerprint.
4. For UI, design, multimedia or external actions, evaluate actual rendered/runtime artifacts and mark unobserved criteria `NOT_VERIFIED`.
5. Fail with reproduction instructions and evidence rather than broad unsupported claims; do not rewrite tests to match broken behavior.
6. Only transition `verifying -> done` after required project-specific checks and approvals; record blocked or changed requirements explicitly.
7. Create `task checkpoint` and `task handoff`; commit and push non-secret task artifacts if another PC must resume.

Independent QA review should be read-only to application source and golden expected data wherever technically enforceable.
