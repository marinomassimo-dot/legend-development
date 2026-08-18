---
artifact: BENCH-AB-001 — assignment
actor_id: scientist-b
task_id: BENCH-AB-001-B
mode: INDEPENDENT_CRITICAL_READ
benchmark_id: BENCH-AB-001
parallel_read_group: BENCH-AB-001
---

# ASSIGNMENT — `scientist-b`

```
ACTOR_ID              scientist-b
ROLE                  scientist            contract: roles/scientist.md (in this surface)
TASK_ID               BENCH-AB-001-B
MODE                  INDEPENDENT_CRITICAL_READ   → benchmark/MODE_DIRECTIVE.md
PARALLEL_READ_GROUP   BENCH-AB-001         two readings on one paper, intended and declared
INTERACTION_MODE      AUTONOMOUS_COMPLETE  do not ask questions to proceed
SOURCE                PMID 42397075 · doi 10.1093/brain/awag239
WORKING SURFACE       this directory — its own git repository, its own branch
```

**Your ACTOR_ID is permanent and is not this session.** The session reference that routes
messages to you is ephemeral and changes with every restart; it is never the identity under
which your work is recorded. Everything you produce is attributed to `scientist-b`.

**Two readers are reading this paper on purpose.** `PARALLEL_READ_GROUP: BENCH-AB-001` is the
declaration that makes it intentional rather than a duplicated assignment. You are not to know,
infer, or ask what the other reader is doing — and in particular, your critical axes are aimed
at **the paper**, never at a reconstruction of another reading.

Read, in order — paths relative to this directory:
`CLAUDE.md` → `benchmark/BENCHMARK_INSTRUCTIONS.md` → `benchmark/MODE_DIRECTIVE.md` →
`benchmark/OUTPUT_SCHEMA.md`.

When you declare completion your reading is **frozen immediately, before its content is read by
anyone**. Corrections after that point are separate dated files and are reported as corrections.
