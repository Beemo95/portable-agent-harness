# Research basis, vintage and review boundary

This project uses concise instructions, progressive code/knowledge retrieval, explicit progress, verifiable phase gates and durable handoffs. **These sources don't prove that our Markdown-only implementation is optimal or that models follow it.** The choice not to add a Python/SQLite task engine is an architectural trade-off, not an experimental conclusion.

## Primary engineering / research references
- [OpenAI — Harness engineering](https://openai.com/index/harness-engineering/) (published February 2026): small AGENTS.md router, repository knowledge and machine-checked constraints
- [OpenAI — Long-horizon tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex) (2026): plan, edit, validate, repair, checkpoint
- [Anthropic — Effective harnesses for long-running agents](https://www.anthropic.com/research/effective-harnesses-for-long-running-agents) (November 2025): persistent progress records and small steps across sessions
- [Anthropic — Effective context engineering](https://www.anthropic.com/research/effective-context-engineering-for-ai-agents) (September 2025): scoped retrieval and useful context selection
- [Agent Skills specification](https://agentskills.io/specification): frontmatter and skill structure
- [OpenSpec project configuration](https://openspec.dev/docs/configuration/config-yaml): schema/context/rules and validation limits

[Source audit and recheck dates](source-audit.md) classify which **tool instructions** can go stale rapidly. [Evaluation protocol](evaluation.md) measures actual portability when applied to real source; no cross-agent or real Godot tests have run here.
