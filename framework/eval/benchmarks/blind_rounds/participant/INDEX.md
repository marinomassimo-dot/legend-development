---
artifact: BLIND ROUNDS — participant surface index
audience: PARTICIPANT
status: PROPOSED — authorizes no run. A case begins when an assignment names it, not when
  it appears here.
normative: no
---

# Blind rounds — participant surface

Everything in this directory is **participant material**, and nothing evaluator-side is
permitted to reach it. That is a check, not a promise:
`check_participant_surface.py`, one directory up, enumerates the vocabulary a participant file
may not contain, verifies each handoff carries the six permitted fields and no seventh, and
verifies no file here points outside this directory. It runs its own positive control first and
declares itself void if that control does not fail.

**This page states the rule and deliberately does not restate the vocabulary the checker
forbids** — a page that lists the forbidden words contains them, and would either fail its own
check or force the check to be weakened around it.

**Nothing else about these cases is participant material.** If you are a reader, this directory
and your own assignment are the whole of what you are entitled to hold about a blind case.

| Case | Round | Status |
|---|---|---|
| [`BLIND-R1-001`](BLIND-R1-001.md) | 1 | `RELEASED` |
| [`BLIND-R2-001`](BLIND-R2-001.md) | 2 | `NOT_RELEASED` |
| [`BLIND-R3-001`](BLIND-R3-001.md) | 3 | `NOT_RELEASED` |

`NOT_RELEASED` means *do not begin*. It says nothing about the case.

---

## Two conditions that are not properties of any case

1. **The reading is not run inside a LEGEND checkout.** `controlled_benchmark_ab.md` §2.1–§2.3
   builds an allowlisted surface outside every checkout, and that is where a blind case is read.
   A case read inside `lettore`, `lettore-b`, or any worktree of this repository is not blind and
   its result is void.
2. **The actor who builds the surface is not the actor who reads it** (`controlled_benchmark_ab.md`
   §2.2, one writer per surface, transferred once).

> **Nothing here is medical advice.**
