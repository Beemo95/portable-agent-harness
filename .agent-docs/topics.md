# Reusable project knowledge — topic pointers

> TEMPLATE STATE: no actual game has been inspected. No topic claims are populated.

This file is a **navigation index**, not a second knowledge database. Add a row only when a verified concept, design choice or troubleshooting lesson is likely to matter across **separate future tasks**, even after its original OpenSpec change is archived. Keep the explanation in exactly one canonical spec, architecture section, ADR or evidence-backed research record.

| Topic / search aliases | Canonical knowledge / rationale | Current code and tests | Last verified revision / status |
| --- | --- | --- | --- |

For example, in a **real** game that has implemented isometric movement, a row could point to its actual architecture section, accepted depth-sorting ADR and relevant movement/occlusion scripts and regression tests. **Do not invent those paths in this template.** Use aliases such as `isometric / 아이소메트릭 / depth sorting` only for topics that actually exist.

## Maintenance and retrieval
1. New or revisited work: identify domain terms, check matching rows, follow canonical docs and inspect **current source/tests/Git history**. If the index has no entry, search code, ADRs, research, old worklogs and archived changes before concluding no relevant history exists.
2. When work yields **durable reusable** knowledge: update its canonical owner first, then add/update a compact pointer here (subject, links/code/test and verified revision). Avoid copying the rule itself.
3. If knowledge becomes stale or conflicts with code: mark it unverified/superseded, correct the authoritative record and index after investigation. Never silently rely on an old pointer.

See [knowledge reuse workflow](../docs/knowledge-reuse.md). STATUS tracks *current* work; this topic map helps find *old but relevant* knowledge.
