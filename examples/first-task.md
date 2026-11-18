# Example task workflow

```sh
python3 scripts/harness.py doctor
python3 scripts/harness.py status
python3 scripts/harness.py task new DEMO-001 --title "Improve context retrieval" --goal "Make Korean query retrieval more robust" --accept "Korean task query finds relevant project files" --gate unit --gate compile
python3 scripts/harness.py task show DEMO-001
python3 scripts/harness.py task transition DEMO-001 ready --expect 0
python3 scripts/harness.py task transition DEMO-001 in_progress --expect 1
python3 scripts/harness.py context "Korean context search" --task DEMO-001
python3 scripts/harness.py task checkpoint DEMO-001 --expect 2 --note "Work started"
python3 scripts/harness.py verify DEMO-001
python3 scripts/harness.py task transition DEMO-001 verifying --expect 3
python3 scripts/harness.py task transition DEMO-001 done --expect 4
python3 scripts/harness.py resume DEMO-001
```

The example illustrates the lifecycle. In real work, implementation and its test must be completed before verification; simply passing tests unrelated to the feature is **not proof** of its acceptance. Configure feature-specific gates before marking done.
