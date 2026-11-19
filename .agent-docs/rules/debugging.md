# Godot debugging and performance investigation

1. Capture reproducible steps, expected vs actual result, engine version, platform, scene, logs and recent changed commits. If an issue is intermittent, state uncertainty.
2. Choose the smallest repeatable reproduction. Check Godot debugger/runtime and imported resource errors before adding speculative fixes.
3. Establish a hypothesis, inspect relevant code/data, perform one controlled change and re-test. Save actual evidence for confirmed causes, not guesses.
4. For performance, record device/rendering mode, baseline and measurement method; distinguish CPU/GPU, `_process` allocations, draw calls, physics, import time and startup.
5. Add a regression test or explicit manual verification procedure when it is reproducible and meaningful.
6. Document confirmed root cause, fix, affected files, regression outcome, risks and remaining unknowns in the linked worklog/issue. Only make a new ADR if the fix changes architectural policy.
