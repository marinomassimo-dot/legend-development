---
artifact: Session Learning Record (Annex E.6)
record_id: SLR-ORCH-005
learning_id: LEARN-ORCH-005
session_ref: NOT DECLARED — not observed, not inferred, not inherited. Routing remains UNRESOLVED
date: 2026-08-20
actor_id: orchestrator
role: orchestrator — NO LEASE HELD AT ANY POINT. ACTIVE by derivation 0, measured at open and close
task: open, adjudicate and close REV-ORCHSURF-MIRROR-002 (CAND-20260819-ORCHSURF r4)
  TASK-20260820-MIRROR-ORCHSURF-REV4 · DIRECTIVE_VERSION 2 · GENERATION 1
classification: FAILURE_PATTERN — five findings against my own artefacts, two of them self-caught
  and one of them the exact error I had ruled against another actor for, while applying that ruling
confirmation_class: REPLICATION of the instrument-surface class recorded independently this session
  by plan (SLR-plan-0014 L-1) and mirror (SLR-mirror-0018-ADD-002 L-10); one sub-shape proposed
contributors: mirror (O-1, O-2, the M-2 positive control), plan (D-1, the testimony/measurement
  distinction, the self-caught-instance argument)
scope: what an adjudicator's disclosed values are worth, and why every mitigation this session
  produced is mechanical rather than dispositional
status: PROPOSED — NON NORMATIVE. Curation is Mirror's under E.2; I self-certify nothing here
slr_outcome: MICRO_UPGRADE
supersedes: none
---

# EVERY CORRECTION THIS SESSION CAME FROM A MECHANICAL STEP, AND NONE FROM KNOWING BETTER

## SESSION · WORK COMPLETED

Bootstrapped as Orchestrator with no ACTIVE lease and did not acquire one, on the ground that
opening a review is not a `CANONICAL_BATCH_COMMIT` and an unused lease is the failure the lease
record already documents at #3. Verified the ORCHSURF r4 package for readiness — hash, base,
ancestry, FROZEN, the DEC's three hashes, the re-bind — opened `REV-ORCHSURF-MIRROR-002` at R4
under Annex C.3, adjudicated two questions routed to me, opened and scoped round 2, verified both
remedies myself once rounds were spent, and closed the cycle. `main` never moved. Neither peer
worktree was written to. No approval was sent.

## PROBLEMS — five findings against my own artefacts

```
O-1  mirror   the lease row said 9 records; every candidate ref carries 5. Nine exists only on
              branch `orchestrator`. The row was unreproducible by the method §4 declared
O-2  mirror   scientist fingerprint transcribed …9d1e for …9d1a
D-1  plan     line anchors valid only at CONTENT_TIP, sent to a reader the handoff directs to the
              branch tip, where 239 is a negative control and 908 is a sentence about CLAUDE.md
I-6  self     grepped `PROBLEM DECLARED NOT SOLVED` against a document containing
              `PROBLEM DECLARED, NOT SOLVED`. The comma was the whole finding
I-7  self     measured 533 → 539, read plan's `2` as wrong, and was one step from filing a
              POPULATION failure as an ARITHMETIC one — the exact error I had ruled against plan
              for, in the ruling that produced the remedy I was verifying
```

## SOLUTION

Each was corrected append-only. **The opening was never edited** — nine addenda and a closure sit
on top of it, including the three findings against it, because a record edited to agree with its
own correction has stopped being evidence of what was originally claimed.

`O-1`'s correction is the substantive one: the safety conclusion (`ACTIVE = 0`) reproduced in both
universes and did not move; what broke was that **I used two surfaces, declared one, and reported
the result of the other.**

## LEARNING

**L-1 · An instrument reporting faithfully about the wrong object is invisible to running it more
carefully.** Seven instances, three actors, and not one returned a wrong value: the hash blind by
construction across control-plane commits; anchors valid only against an uncarried surface; a
superseded verifier on a reviewer's own branch; testimony where measurement was available; a window
published as a population; a query for a string the document does not contain; a right number read
as wrong because its population was unnamed. **`CONFIRMATION_CLASS: replication`** — plan and mirror
recorded this independently and the three records should be clustered, not merged.

**L-2 · Recording a rule does not cause it to be applied.** At `ADD-003` I wrote that a zero with no
positive control cannot distinguish an absent text from a blind instrument. At `ADD-006`, one record
later, I asserted an identity from one end with no control. At `ADD-008` I ruled that a population
failure must not be filed as an arithmetic one; at `ADD-009` I was one step from doing exactly that.
**The failure is not ignorance of the rule.** It happened to the actor holding the rule, immediately
after stating it, while applying it to someone else. **So "record the rule" is not the mitigation** —
and this is the load-bearing learning, because the laboratory's standard response to a defect is to
write it down.

**L-3 · A scope statement decays into a device for retiring true findings unless it is read
against its purpose.** `M-4` was reachable at round 1 and my round-2 scope excluded "anything that
passed at round 1." Mirror offered not to contest a ruling that used my own line to bury a false
sentence. **A thing unexamined has not passed**, and a scope is a tool for focus, never a
disposition.

**L-4 · A test whose answer is entailed by the design under test cannot be repaired by re-framing.**
T7 asked whether the procedure could *silently* seat a root Orchestrator; revision 4 seats one
openly by ratified intent. Re-running it returns PASS for a reason unrelated to the recorded one —
a second wrong-reason pass, curing nothing. **Withdrawal was the only honest disposition**, and the
question that would still discriminate belonged to a candidate the operator had placed out of scope.

**L-5 · ORIGINAL_OBSERVATION, proposed.** A population needs a **surface** and an **instant**. The
session found the second half by accident: plan's corrected population of `19` measured `27` hours
later because my own commits moved it. `19` was never wrong — it was underspecified in a dimension
nobody had named, including the actor correcting an underspecification.

## MICRO-UPGRADE — taken, not promised

**Before filing a finding against a number, enumerate the alternative population and check the
number there.** Two lines of shell, and it is what stopped `I-7`. Filed as an adjudicator's
pre-filing step because the adjudicator is the last party to check anything and the first whose
error travels unchallenged to the operator.

Two more, adopted from other actors and recorded as theirs: **announce a tip change AND publish the
object blob** (plan — announcement is testimony, the blob is measurement, and the blob works when
the sender does not); and **verify the object, not the envelope** — the blob check fired in both
directions inside three exchanges, permitting a skipped re-bind at `5ea744c` and forbidding one at
`f627ea5`, which is why it is kept rather than because it sounded right.

## IMPACT

The `ADD-001` rider decoupling the review from `M1`'s L2 promotion removed the reviewer's interest
in its own deliverable's form **before it had one** — Mirror published a self-audit finding against
its own C.2 conformance at zero cost, and no capability field moved on the strength of a review that
would have verified it. That is the one structural thing I contributed that the cycle would have
been worse without.

Twice a rule I issued was improved rather than complied with, and both improvements were against
me. **A laboratory where the coordinating actor's rules are returned sharper is working**; the
alternative outcome — compliance — would have left the announce-only rule in place, and it fails
silently exactly when the sender stops existing.

## CLASSIFICATION · SCOPE

`FAILURE_PATTERN` + `MICRO_UPGRADE`. Scope: adjudicator conduct, disclosed-value discipline, and
review scoping. **Not** scientific, **not** governance-amending. Nothing here is normative and
nothing here approves anything.

## EVIDENCE

```
reviews/orchestrator/OPEN-REV-ORCHSURF-MIRROR-002.md            2509cd3
  + ADD-001 dc71c4a · ADD-002 0179235 · ADD-003 2a28009 · ADD-004 dd434d5 · ADD-005 a22fd28
  + ADD-006 c6c4548 · ADD-007 46e833a · ADD-008 87a8d02 · ADD-009 4657b1c
reviews/orchestrator/CLOSE-REV-ORCHSURF-MIRROR-002.md           0a1929e  (+ ADD-001)
reviews/mirror/REV-ORCHSURF-MIRROR-002.md · -R2                 36e1381 · 95f64f9
reviews/plan/AUTHOR-RESPONSE-ORCHSURF-MIRROR-002.md             on orchestrator-surface
learning/plan/SLR-plan-0014.md · learning/mirror/SLR-mirror-0018(-ADD-002)
```

Every value in this record was recomputed from explicit commit SHAs in the root checkout and in
throwaway detached checkouts, all removed. **The root checkout was byte-identical and clean at open
and at close**, which is a claim about a surface I have now learned to name.
