# Empirical evaluation — real phased work and cross-topic knowledge reuse

**Not executed on an actual game yet.** CI for Markdown links/pointers is not proof that agents follow development gates or recall all knowledge.

## Same-source comparison
Keep the same partially complete real Godot task, branch/commit, model and tool constraints:
- A: code and Git alone
- B: A + short `AGENTS.md`
- C: B + factual STATUS, one OpenSpec plan, relevant knowledge/ADR/handoff
- D: C + topic pointers, selective native search and task-specific Skills

## Instruction / Skill discovery smoke tests

On actual installed versions of **Cursor, Codex, Claude Code, Grok Build and Antigravity**, create a fresh session in a trusted project checkout and verify *which exact path* loaded `AGENTS.md` or its import and whether the domain Skills can be discovered. Check that a single generic request triggers code inspection without having to say "read AGENTS.md." The template's Bash CI only checks structural imports and adapter files; it cannot execute these model sessions. Record version, observed discovery output and missing capabilities.

## Real scenarios (fresh sessions, no prior chat)
1. **Baseline discovery:** agent inspects real code, test setup and relevant old decisions **before** designing a new feature; identifies what already exists rather than inventing a new implementation.
2. **Useful clarification:** a technically answerable question should be resolved from code; an ambiguous product decision should produce a focused question rather than an unsupported guess.
3. **Phase gates:** plan a nontrivial feature in ordered acceptance/test phases. Inject a failed or missing required test and check that the agent fixes/retests or reports blocked rather than advancing falsely.
4. **Normal resume:** some work done and next phase pending; a new agent identifies the right phase, affected files and real QA gaps.
5. **Stale state:** STATUS/old ADR conflicts with current code; agent flags contradiction rather than trusting obsolete notes.
6. **Unverified visual/device QA:** automated/headless success without actual rendered/device evidence must not be marked product acceptance.
7. **Missing external state:** no Godot binary, ignored assets or local unpushed edits; agent identifies what's missing.
8. **Long-range topic return:** implement isometric movement, work on a different feature, then return to isometric NPCs. Can a fresh agent find the older conventions, rejected approaches, actual code/tests and correct stale information **even when STATUS points elsewhere**?
9. **Cross-model handoff:** switch Codex/Hermes/Grok or other available agents mid-change and inspect whether source/acceptance/next phase are recovered without prior chat.

## Evaluate evidence, not fluent explanations
Record exact revision, project snapshot, prompts, agent/version, opened files, actual tool execution, original acceptance, phase gates, test commands/outcomes and unexpected edits. Score correct code/knowledge retrieval, false completions, proportion of required gates verified, duplication avoided, regressions, time and tokens/cost if measurable. Repeat over several diverse tasks before claiming reliability or improvement.

`bash scripts/check-docs.sh` and `bash tests/docs-lint.sh` cover only **structural** files/links, not semantic truth, code tests, human approvals or actual agent compliance.
