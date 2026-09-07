---
artifact: Session Learning Record (Annex E.6)
learning_id: LEARN-MIRROR-001
session_ref: b26b34cc-275a-42fe-a8c9-95dcb28849de
date: 2026-08-16
actor_id: mirror
role: hostile / governance / epistemic / metacognitive reviewer
task: GOV311-MIRROR-REVIEW-001 / directive 1 / generation 1
classification: FAILURE_PATTERN
confirmation_class: ORIGINAL_OBSERVATION
scope: candidate preparation (Plan) + review procedure (Mirror)
status: OBSERVED
---

# Session Learning Review — first MAJOR hostile review of the v3.1.1 materialization

## WORK COMPLETED

Rehydration under the bridge protocol; TASK_ACK and claim; M1 binding verification of
`CAND-20260816-GOV311` rev. 4; disposition `REVISION_REQUESTED`; review parked at M1 per the
task's own non-retryable condition. R-2…R-7 not performed.

## PROBLEMS ENCOUNTERED

1. The candidate's recorded `CANDIDATE_CONTENT_HASH` did not reproduce. Distinguishing "my
   procedure is wrong" from "the recorded value is wrong" was the whole difficulty, and a wrong
   call in either direction would have been expensive: a false BLOCKER halts a MAJOR migration,
   a missed one lets an unverifiable identity reach `HUMAN_APPROVAL`.
2. The governance artifacts I am required to load at rehydration live only on the branch that
   carries the object under review. The law and the defendant arrived in the same envelope.

## SOLUTION APPLIED

For (1): rather than assert the mismatch from one failed command, I swept 16 serialization
variants across 9 commits and **searched for a known-good value to reproduce**. Revision 1's
superseded hash reproduced exactly under P5 v1. That single positive control converted "my
computation disagrees" into "my computation is correct and three recorded values are not
reproducible" — a claim of an entirely different evidential class.

For (2): loaded them, and declared the provenance and its non-canonical status explicitly at
rehydration instead of silently treating a branch artifact as ratified law.

## LEARNING

**A negative finding about a hash is worthless until the same tooling has reproduced a positive
one.** The failure mode this avoids is not being wrong — it is being *unfalsifiably* right: a
reviewer who reports "does not match" without a positive control has produced a claim that
cannot be distinguished from their own error, and the author's rational response is to doubt the
reviewer. The positive control is what makes a hostile finding actionable rather than arguable.

This generalises past hashes to every mechanical verification a reviewer performs: **carry a
known-good case through the same instrument before reporting a failure.** It is the reviewer's
equivalent of the repository's existing discipline that a validator must be mutation-tested —
a check nobody has seen succeed is not evidence when it fails.

**Secondary observation (candidate-side, for Plan's benefit, not a directive).** The defect
survived three revisions in an artifact that is otherwise exemplary — and it survived precisely
*because* the manifest published its reproduction command while nobody re-ran it. A recipe that
is executable but never executed is weaker than the repository assumes: it converts a silent
decay into a *detectable* one, which is real progress, but detection still requires that someone
run it. The candidate's own `UNRESOLVED #8` names the same gap from the other side ("the script
has been exercised only by its author"). Both point at one pattern: **authored-and-never-
independently-run is the state in which this system's self-checks fail.**

## MICRO-UPGRADE

Proposed for Mirror's own review procedure: a binding-verification step that is **not complete**
until the instrument has reproduced at least one independently-recorded value. Where a candidate
declares superseded hashes, those are the free positive controls — this candidate handed me
three, and one of them worked.

🔴 This is *proposed*, not adopted. Annex G.2 places Mirror's review rubric outside Mirror's own
authority: material changes route `MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent
reviewer chosen by Orchestrator → validation`. Recorded here as a learning; it does not become
method by being written down, and it is deliberately not applied to the rubric in this session.

## IMPACT

Prevented a MAJOR governance candidate with an unverifiable binding object from reaching
`HUMAN_APPROVAL`, where gate 5 would have bound an approval to a hash no tree produces.

## EVIDENCE

`reviews/mirror/REV-GOV311-MIRROR-001.md` §1.2 (144 combinations, one positive control),
§1.1 (the manifest's own command), §4 (fingerprint cascade demonstrated on a scratchpad copy).

## DEDUP CHECK

`LEARNING_INDEX` does not exist (Annex E.2; listed as PENDING_IMPLEMENTATION in the candidate),
so no dedup against prior records was possible. Recorded as `ORIGINAL_OBSERVATION`; it must be
re-checked for duplication once the index is built. This is itself a small instance of the same
pattern: the machinery that would catch a duplicate is designed, approved in principle, and not
yet running.
