---
name: verify-and-handoff
description: Independently check real feature acceptance with test evidence before recording handoff.
---
# Independent verification / handoff

1. Read original accepted spec/change and current source/Git diff; ignore unsupported previous PASS claims.
2. Run real project tests, visual/game runtime/device checks as warranted. Missing tools = NOT RUN.
3. Record exact command/procedure, environment, revision, observed evidence and PASS/FAIL/NOT RUN per criterion.
4. Preserve approved acceptance and golden test fixtures; never edit them to conceal a failure.
5. Update only genuinely implemented checklist items, STATUS and meaningful handoff.
6. Run `bash scripts/check-docs.sh` when present (docs integrity, **not** game QA). Commit/push non-secret evidence when authorized.
