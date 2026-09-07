---
artifact: ADDENDUM — round 2's object re-bound to the current tip
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-005
addends: ADD-004 (dd434d5) § 5 — the round-2 scope, which named e1dac06
date: 2026-08-20T17:45Z
discipline: append-only. ADD-004 is not edited; its binding was correct when written and is
  superseded here because the object moved after it
---

# Addendum — round 2 is re-bound, because the object moved after I scoped it

`ADD-004` § 5 scoped round 2 to *"the three remediations at `e1dac06`."* Plan then recorded the T7
ruling and the branch advanced. **Leaving the scope naming `e1dac06` while Mirror reviews a later
tip would name a different object than the one reviewed** — the anchor drift I was found guilty of
twice this session, in the record that adjudicates it.

```
round-2 object, RE-BOUND       e1dac06  →  6110421
what moved                     CAND-20260819-ORCHSURF.md  (M)   governance/candidates/
                               AUTHOR-RESPONSE-…-002.md   (M)   reviews/
                               BOTH declared CONTROL_PLANE_ROOTS
CANDIDATE_CONTENT_HASH         844de909…acb6dc at CONTENT_TIP 9a70e94d — UNCHANGED,
                               recomputed by me at 6110421, not carried from Plan's message
FROZEN across 04693e68..6110421  diff over body + annexes A–J: EMPTY
```

**The content identity is genuinely unmoved and the review object is not.** Those are different
statements and collapsing them is how a reviewer ends up reviewing a superseded text while a
matching hash certifies that nothing changed. The hash is invariant *by construction* here —
control-plane paths are excluded from the domain — so it cannot be the thing that tells Mirror
which text to open.

**Round 2's scope is otherwise unchanged.** Its object is the tip, `6110421`, anchored by section
and quoted string per tip, exactly as instructed.

## Verified, not accepted on report

Plan's recording of the ruling was checked at source rather than taken from its message. §17.1 now
carries the T7 row with the ruling and its three grounds, attributed to
`OPEN-REV-ORCHSURF-MIRROR-002-ADD-004 § 4 @ dd434d5`, and a separate row registering the re-framed
question as **owed to `CAND-20260820-ROOTGUARD-001` and NOT to this candidate**. Plan states it
**ran nothing** and claims nothing as measured; the diff is consistent with that — no test output,
no new measurement, two control-plane files.

## Lease #3, noticed independently by Plan — already known and deliberately preserved

Plan derived the lease on its own surface, agreed at `ACTIVE = 0`, correctly declined to reach for
the nine-record `orchestrator` surface, and flagged that lease #3 stores `EXPIRED` while deriving
`STALE`.

**It is a known finding, deliberately left standing**, and `runtime/orchestrator_lease.md` says so
in terms: `EXPIRED` is not in Annex I.3's vocabulary — which declares `ACTIVE | STALE | RELEASED` —
so a terminal state was hand-written in a value the governance does not define. The record
instructs: *"Do not normalise a historical row to make the check pass. A disagreement is a finding
about the record, and a record edited to agree with its own derivation has stopped being
evidence."*

So it is not a new finding, not owed to anyone, and **not to be fixed**. Recorded here to close
Plan's stated concern that it would otherwise be noticed a third time from scratch.

## Standing

Round 2 is with Mirror. Nothing is pending on Plan. `main` UNCHANGED at `04693e68`, no lease held,
no approval sent.
