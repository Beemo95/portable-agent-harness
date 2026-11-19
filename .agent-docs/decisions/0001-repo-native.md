# ADR-0001 — Repository-native durable state

Status: Accepted

Decision: Keep portable task state, approved design decisions, and compact verification manifests in the repository. Treat local SQLite search indexes as disposable caches. Use only Python standard library in v1.

Why: A fresh machine and a new agent must work from a Git clone with minimal setup. Avoid central database and model-specific memory as mandatory dependencies.

Trade-off: Git commit/push discipline is required to transfer pending work; large assets, secrets and OS permissions remain external dependencies.
