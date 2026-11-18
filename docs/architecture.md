# Architecture — control plane inside the repository

## Separation of concerns

```
User request -> Agent (any provider)
            -> AGENTS.md minimal entry
            -> Harness CLI (deterministic)
               + project config & route hints
               + Git-backed task state, events, decisions
               + disposable local FTS5 index
               + actual project tools and test gates
            -> context packet (bounded excerpts + file refs)
            -> execution in scoped workspace
            -> tool-produced evidence + checkpoint
            -> next agent / next machine
```

The harness cannot transfer hidden model reasoning. It transfers explicit decisions, artifacts, facts, execution state and proof references.

## Source of truth

- User-approved intention: product documentation, task acceptance criteria, decision records.
- Actual system behavior: current files, live environment and executable tests.
- Task progress: `.harness/tasks/ID/state.json`, verified against Git and source fingerprint.
- Tool execution: machine-produced gate records; a status narrative is not evidence.
- Search cache: generated from repository; never the source of truth.

If design and code conflict, do not silently choose code over intent or edit golden tests to match broken behavior. Record and resolve discrepancy.

## Why not one huge memory file?

A single multi-writer shared document risks conflicts and drift. Divide knowledge by project concern and approved decision. Each task owns a separate state file, evidence and checkpoint. A new agent retrieves only what the task needs.

## Portability boundaries

Git contains textual state and small evidence. Git ignores local index and temporary files. A clean clone also needs platform dependencies, authentication, access to external systems, and possibly separately hosted large assets. All such needs must be declared and assessed, not silently inferred.

## v1 technical scope

- Pure Python 3.10+ standard library.
- SQLite FTS5 lexical retrieval, optional route hints, no embeddings dependency.
- Optimistic task revisions and filesystem locks: basic protection against concurrent writers on one filesystem. Cross-machine Git conflicts still require review/merge.
- Source fingerprint hashes local non-ignored files, including untracked code. For giant repos this is O(total bytes); incremental hashing can be added after measurement.
- CLI is a portable integration boundary. Adding an MCP adapter later should not change task or evidence formats.
