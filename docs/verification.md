# Verification — what "pass" actually proves

## Gate configuration

`project.harness.json` declares commands as argv arrays. The CLI calls `subprocess.run(..., shell=False)`, captures exit status/output hashes, and checks `min_tests` where configured. At present `min_tests` recognizes Python unittest `Ran N tests in...` output. For other test runners, add adapter logic or use custom gate commands with verified nonzero exit on no-test cases.

## Evidence lifecycle

A verification run writes `.harness/evidence/TASK-ID/<run>.json` containing timestamps, argv, exit code, stdout/stderr SHA-256 hashes, detected test count, source fingerprint, current Git HEAD and per-gate status. Failing output has a short diagnostic tail. Evidence created by the tool does not prevent a malicious agent from editing the file; use CI protections and independent review for high-trust environments.

## `done` checks

- Task must already be `verifying`.
- All acceptance criteria must refer to configured gate IDs.
- Latest run must include every mapped gate with `pass` and `all_passed=true`.
- Source fingerprint and HEAD must still match.
- Blockers must be empty; human approval is **never automatically signed by this version**.

This is stronger than trusting a prose completion message, but it cannot establish that natural-language goals were correctly mapped to the automated tests. Require human review or independent QA for critical and visual tasks.

## Known v0.1 limitations

- CLI does **not** record GUI screenshots, human aesthetic approvals, performance profiles or deployments unless external test scripts do.
- Source hashing is expensive for huge repos, and .gitignore-like excludes in the index are not comprehensive authorization boundaries.
- No cryptographic signing/remote trust of evidence; CI and branch protection must enforce provenance.
- No automatic separation between tester and implementation author; enforce via workspaces and permissions.
- No automatic task-dependency DAG executor; a manager can track dependencies in contracts and agents can orchestrate at a higher layer.
