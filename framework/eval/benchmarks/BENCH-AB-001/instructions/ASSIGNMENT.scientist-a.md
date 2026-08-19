---
artifact: BENCH-AB-001 — assignment
actor_id: scientist-a
task_id: BENCH-AB-001-A
mode: PRIMARY_EVIDENCE_READ
benchmark_id: BENCH-AB-001
parallel_read_group: BENCH-AB-001
---

# ASSIGNMENT — `scientist-a`

```
ACTOR_ID              scientist-a
ROLE                  scientist            contract: roles/scientist.md (in this surface)
TASK_ID               BENCH-AB-001-A
MODE                  PRIMARY_EVIDENCE_READ    → benchmark/MODE_DIRECTIVE.md
PARALLEL_READ_GROUP   BENCH-AB-001         two readings on one paper, intended and declared
INTERACTION_MODE      AUTONOMOUS_COMPLETE  do not ask questions to proceed
SOURCE                PMID 42397075 · doi 10.1093/brain/awag239
WORKING SURFACE       this directory — its own git repository, its own branch
```

**Your ACTOR_ID is permanent and is not this session.** The session reference that routes
messages to you is ephemeral and changes with every restart; it is never the identity under
which your work is recorded. Everything you produce is attributed to `scientist-a`.

**Two readers are reading this paper on purpose.** `PARALLEL_READ_GROUP: BENCH-AB-001` is the
declaration that makes it intentional rather than a duplicated assignment. You are not to know,
infer, or ask what the other reader is doing.

Read, in order — paths relative to this directory:
`CLAUDE.md` → `benchmark/BENCHMARK_INSTRUCTIONS.md` → `benchmark/MODE_DIRECTIVE.md` →
`benchmark/OUTPUT_SCHEMA.md`.

When you declare completion your reading is **frozen immediately, before its content is read by
anyone**. Corrections after that point are separate dated files and are reported as corrections.
