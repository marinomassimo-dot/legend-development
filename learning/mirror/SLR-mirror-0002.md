---
artifact: Session Learning Record (Annex E.6)
learning_id: LEARN-MIRROR-002
session_ref: b26b34cc-275a-42fe-a8c9-95dcb28849de
date: 2026-08-16
actor_id: mirror
role: hostile / governance / epistemic / metacognitive reviewer
task: GOV311-MIRROR-REVIEW-002 / directive 1 / generation 2
classification: FAILURE_PATTERN
confirmation_class: ORIGINAL_OBSERVATION
scope: Mirror's own verification method
status: OBSERVED
supersedes: none — LEARN-MIRROR-001 stands and is reinforced
---

# Session Learning Review — full hostile review of revision 5

## WORK COMPLETED

R-1…R-7 under Annex C.2 on `CAND-20260816-GOV311` rev. 5; ten assigned binding checks; 19 PIDs
adjudicated individually; 8 PENDING and 10 UNRESOLVED censused; disposition
`REVISION_REQUESTED` with five manifest-local required changes, two escalations, four notes and
two governance-defect candidates.

## PROBLEMS ENCOUNTERED

1. **My own tests were wrong twice, in opposite directions.**
   - Testing whether the fingerprint composer *fails loudly*, I renamed `### P2.2 · Pertinence
     sets` to `### P2.2-BROKEN · …`. The composer returned exit 0 with a changed hash, which looks
     exactly like a silent fallback — a serious defect if reported. It was my error: the parser
     matches the substring `### P2.2`, which my "broken" heading still contained. Re-tested
     properly (`### P2-2`), it failed loudly, as claimed.
   - Checking the migration map's destinations, I called 14 of 27 paths missing. They were
     basenames — this repository's own wikilink convention — and all 27 resolve.
2. Revision 5 supplied a *diagnosis* of the revision-4 defect. Accepting an author's account of
   their own failure is the softest moment in any review.

## SOLUTION APPLIED

For (1): both errors were caught by the same reflex — before reporting a negative, reproduce a
positive with the same instrument. The composer produced a correct fingerprint on an unmodified
copy, which meant "exit 0" could not be a fallback; the path check resolved 13 of 27, which meant
the 14 "missing" ones were a resolution problem, not an absence.

For (2): I re-executed the author's stated mechanism instead of reading it. `$(…)` without the
terminating newline returns `2e7da13f…` — the exact value revision 4 recorded — and
`printf '%s' "$LIST" | wc -l` returns 507, the exact count it printed. One byte explains both
symptoms. Verified, not believed.

## LEARNING

**A test of a guard is itself untested until it has been seen to pass and to fail.** I wrote
`LEARN-MIRROR-001` about carrying a positive control through the instrument before reporting a
negative. This session showed the symmetric half: when the *test* is the artifact — a deliberately
broken input meant to trigger a refusal — a test that fails to break anything is
indistinguishable from a guard that does not guard. Both times the error pointed the same way:
toward reporting a defect that did not exist.

The generalisation, and the reason it is a `FAILURE_PATTERN` rather than a tip: **a hostile
reviewer's errors are asymmetric.** A missed defect is embarrassing; a fabricated defect is
expensive — it sends an author to repair something that was never broken, and it spends the
credibility that makes the next real finding actionable. So the burden of proof on a *negative*
finding is higher than on a positive one, and the cheapest way to discharge it is to demonstrate
that the instrument distinguishes the two states.

**Secondary — the finding I could not have made in review 001.** Because the manifest is now
outside the content domain, all five required changes leave the hash untouched. That converts
what would have been a third full review into a four-field re-check. The classification
introduced to fix a *defect* (PID-19) turns out to also fix the *cost of reviewing*: control-plane
corrections stop invalidating content approvals. Worth watching as a general property, not just a
local repair.

## MICRO-UPGRADE

Proposed for Mirror's binding-verification step: when testing a fail-loud claim, require **two**
executions — one that must succeed on unmodified input, one that must fail on broken input — and
treat a single-sided result as inconclusive rather than as evidence.

🔴 Proposed, **not adopted**. Annex G.2 keeps Mirror's rubric outside Mirror's own authority:
`MIRROR_UPGRADE_PROPOSAL → Plan candidate → independent reviewer chosen by Orchestrator →
validation`. Recorded as learning; it does not become method by being written here. This is the
second session in which the same route applies, which is itself worth noting for the retrospective.

## IMPACT

Two blocking manifest defects surfaced before `HUMAN_APPROVAL`; two required artifacts recovered
from omission; the candidate's own account of its prior failure independently confirmed; the
manifest's `UNRESOLVED #9` discharged by independent reproduction of all four fingerprints. Two
false findings were caught before they reached the report.

## EVIDENCE

`reviews/mirror/REV-GOV311-MIRROR-002.md` §1 (binding, ten checks, the tested account), §3
(fail-loud, four ways), §4 (19 literals, 27 destinations), §6.2 (the omission), NBN-6 (my own
non-exhaustive sweep in review 001).

## DEDUP CHECK

`LEARNING_INDEX` still does not exist (E.2; declared PENDING). This record is adjacent to
`LEARN-MIRROR-001` — same domain, different half of the same discipline — and should be clustered
with it, not merged, once the index exists. Recorded as `ORIGINAL_OBSERVATION`; re-check for
duplication when the index is built.
