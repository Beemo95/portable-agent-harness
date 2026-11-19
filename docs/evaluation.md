# Evaluate real cross-session continuation

Compare on the **same real partly completed feature**, source revision, model/tool budget and held-out acceptance:
- A: code + Git alone
- B: A + AGENTS router
- C: B + STATUS + OpenSpec tasks/decisions/handoff
- D: C + optional native search/Skills

Commit/push source and context; start a new session/model on a clean clone with no prior chat. Ask “What was done? What remains? What was verified? What's next?” Check against the actual files/test evidence, continue one slice and evaluate correctness, hallucinated completion, missing context, tokens, retries and QA gaps.

This is a **manual protocol, not completed benchmark evidence**. Do not claim universal token savings, automated continuation or cross-model correctness without running the test.
