---
name: openspec-handoff
description: Continue OpenSpec change work across sessions with native file/Git inspection.
---
# OpenSpec handoff
1. Read AGENTS/STATUS and inspect Git. Follow the active `openspec/changes/<id>/` and relevant approved specs.
2. Read proposal/design/tasks; checked items are not independent QA proof.
3. Reconcile actual files with recorded work and test evidence. The official OpenSpec CLI is optional; plain Markdown stays readable.
4. Continue the smallest unfinished slice, verify with actual project tools, record PASS/FAIL/NOT RUN honestly.
5. Update the **one** checklist, STATUS, meaningful handoff/ADR, and commit/push for transfer.

No PAH task store or Python CLI; do not promise recovery of unpushed state or secrets.
