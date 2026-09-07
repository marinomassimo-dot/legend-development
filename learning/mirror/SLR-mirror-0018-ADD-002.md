---
artifact: SESSION LEARNING RECORD — ADDENDUM 2 (Annex E.6)
record_id: SLR-mirror-0018-ADD-002
addends: SLR-mirror-0018 (@ fcadc36) · SLR-mirror-0018-ADD-001 (@ be51119)
actor_id: mirror
role: Mirror — hostile review + metacognitive layer
session_date: 2026-08-20
task: TASK-20260820-MIRROR-ORCHSURF-REV4 — CLOSED
object: CLOSE-REV-ORCHSURF-MIRROR-002, branch `orchestrator` @ 0a1929e
authority: none
discipline: append-only. ADD-001 is not edited — its EVIDENCE_COUNT of 6 is what was true when it
  was written, and superseding it in place would destroy the instant it was measured at, which is
  the defect this very record is about
scope_negative: no rubric, clustering, selection or methodology amended (Annex G.2)
---

# `SLR-mirror-0018-ADD-002` — the count moved, and the strongest instance arrived last

## Why this exists

`ADD-001` recorded `LRN-MIRROR-UNJOINED-PAIRS-001` with `EVIDENCE_COUNT 6`. The review closed with
**seven**, plus an eighth of a different kind — and the seventh is the most informative of them.
An `EVIDENCE_COUNT` written at an instant and never re-anchored is the same defect the ID is
about, so the correction is filed as an addendum rather than as an edit.

## WORK COMPLETED

Verified the closure independently rather than accepting `disposed` on report — for findings that
were mine, which is where accepting a report is least defensible.

```
close record          orchestrator @ 0a1929e, read from durable state; agrees with the message
object at close       orchestrator-surface @ 5a69a05 · blob 92c1b7d8
CANDIDATE_CONTENT_HASH  844de909…acb6dc — recomputed, UNCHANGED
FROZEN 04693e68..5a69a05  EMPTY
publication gate      PASS · BLOCKS 0 · 4 pre-existing REVIEW items
LINT                  PASS · 1 INFO (MISSING_WIKILINK, CLAIM 010) — the pre-existing one
M-4 remedy            the false present-tense clause returns 0 hits; replaced by a past-tense
                      statement that matches §1 AND quotes what the false clause said, with its
                      diagnosis. The error is kept written down rather than erased
§8 population row     now carries BOTH surfaces, labelled
```

**Both populations re-measured, because that is the finding:**

```
BASE_HEAD  04693e68   533 included
revision 3 25fa61a    537 included
close      5a69a05    539 included
   → BASE..tip = 6      rev3..tip = 2      both correct, over different surfaces
```

**Plan's `2` was never wrong.** It was measured against revision 3 and reported without its
surface. That is the whole of it.

## PROBLEMS / LEARNING

**Instance 7, and it is the strongest — it happened to the actor holding the rule, immediately
after stating it, while applying it.** Verifying the corrected population row, the adjudicator
measured `533 → 539`, read Plan's `2` as simply wrong, and was one step from filing a **population**
failure as an **arithmetic** one — the exact error it had just ruled against Plan for, in the
ruling that produced the remedy it was verifying. What stopped it was mechanically checking the
*other* population before writing.

**L-10 · Holding the rule is not protection against the error the rule names — and stating it
immediately beforehand is not protection either.** The instance that matters most in this session
is not the one caught by a hostile reviewer; it is the one an actor caught in itself while
enforcing the rule on someone else. **A rule known, stated and being applied still requires the
mechanical step.** Knowledge of the failure mode substitutes for none of it. My own P-1 was the
same shape from the other side: I knew branch staleness was a hazard *because I was about to write
it down*, and I still had to run the diff to avoid it.

**L-11 · The structural finding outlives the candidate, and it is what the review was actually
for.** Seven instances across all three actors of **an instrument reporting faithfully about the
wrong object** — and *not one returned a wrong value*. Plus an eighth of a different kind: a
derived statement that did not follow its source. My superseded verifier is instance 3, counted as
a **near-miss caught by its own actor**, which is why it counts at all: a pattern assembled only
from externally-caught instances is itself an instrument measuring the wrong object — Plan's
argument, and it is correct.

## MICRO-UPGRADE

**Re-anchor `EVIDENCE_COUNT` at close, never only at first observation.** A learning record whose
count was taken once carries a number that decays silently while the record looks authoritative.
The rule from `ADD-001` L-7 — a population needs a surface and an instant — applies to the
laboratory's own learning records, and this addendum is the first application of it to mine.

```
LRN-MIRROR-UNJOINED-PAIRS-001   EVIDENCE_COUNT  6 → 7   (+1 of a different kind, not counted here)
                                measured at     2026-08-20, review close, CLOSE-…-002 @ 0a1929e
                                surface         all durable records of TASK-20260820-MIRROR-ORCHSURF-REV4
CONFIRMATION_CLASSES  unchanged in vocabulary; instance 7 is {orchestrator, CLOSE-…-002, REPLICATION}
```

## IMPACT

Four findings disposed, each verified at source by the reviewer that raised them. One pattern
carried out of the candidate that will outlive it. One count in my own record corrected before it
went stale unnoticed.

## SCOPE / EVIDENCE

`main` UNCHANGED at `04693e68`; no lease held — `ACTIVE` by derivation 0 at close. No capability
field moved: the `ADD-001` rider that decoupled this review from L2 promotion held after the fact,
and `M1` remains where the durable record put it. The branch-staleness hazard stays
`OWNER: UNASSIGNED`, routed and not opened; `SLR-mirror-0018` is not overridden and whether it
opens is the operator's.

```
verified at    5a69a05 (object) · 0a1929e (closure record)
by             recomputation in a throwaway checkout, removed after use
not verified   the regression suite — not re-measured at any point in this review, by anyone
```
