---
artifact: MIRROR delta verification record (Annex C.2)
review_id: REV-GOV311-MIRROR-003
task: delta verification of manifest revision 5.1 — RC-6…RC-10 only
reviewer: mirror
author: plan
adjudicator: operator
level: R4 — MIRROR_REQUIRED, MAJOR (delta scope)
review_date: 2026-08-16
disposition: PASS_WITH_NOTES
scope: RC-6…RC-10 and the conditions that caused REVISION_REQUESTED. R-1…R-7 NOT repeated — see §1.
---

# MIRROR DELTA VERIFICATION — manifest revision 5.1

## 0 · Binding — unchanged, and that is the precondition of this scope

```
CANDIDATE_ID:            CAND-20260816-GOV311
MANIFEST_REVISION:       5.1   (content revision 5, unchanged)
CANDIDATE_CONTENT_HASH:  c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239   VERIFIED UNCHANGED
BASE_HEAD:               749a9a9b8f29c855f803a43b979c591532557561                            VERIFIED
BRANCH_TIP:              9720a0cd1dddfe457f8e4eec1ebe47bd627512cc
BRANCH HEAD AT DELTA:    evidence-index @ a87506a0109a7d167fd195cf41b3c937e28bacf4
DISPOSITION:             PASS_WITH_NOTES
```

## 1 · Why R-1…R-7 were not repeated — established, not assumed

The narrow scope is only legitimate if nothing in the content moved. Verified before anything
else, in this order:

| Check | Result |
|---|---|
| Files changed since the reviewed head `6b3c038` | **exactly one**: `governance/candidates/CAND-20260816-GOV311.md` |
| Its classification against the declared `CONTROL_PLANE_ROOTS` | control plane — no content path touched |
| Hash recomputed at `BRANCH_TIP 9720a0cd` | `c39ecae8…30c239` |
| Hash recomputed at the **new** head `a87506a` | `c39ecae8…30c239` — identical |
| Domain | 504 included / 8 excluded — unchanged |
| Four role fingerprints | unchanged (`37c3b863`, `84d2b841`, `6b55605d`, `ce3c0d94`) |

The object reviewed in `REV-GOV311-MIRROR-002` and the object described by manifest 5.1 are the
**same content under the same hash**. The R-1…R-7 verdicts therefore remain bound to it and are
not re-litigated. Had any content path appeared in that diff, this pass would have stopped and a
full review would have been mandatory.

## 2 · RC-6…RC-10 — each verified independently

| RC | Required | Verified state | Verdict |
|---|---|---|---|
| **RC-6** | Three unresolvable `SOURCE_COMMITS` oids | All **14** entries now carry full 40-character oids; `git cat-file -e` resolves **14/14, zero unresolvable**. The stronger of the two options I offered was taken — full oids cannot be mistyped into a valid-looking prefix | **RESOLVED** |
| **RC-7** | Declare `HUMAN_APPROVAL_QUEUE` and `OPERATOR_DAILY_BRIEF` | Both now in `PENDING_IMPLEMENTATION`, each with its frozen-text clause (J.3/§4/§49.P; §10.4/§49.L) and an eligibility threshold, plus an explicit note that they were missing from the census entirely | **RESOLVED** |
| **RC-8** | Repair the section structure | Headings now run `1, 2, 3, 4, 5, 5b, 6, 7` — no duplicate `## 6`, no orphan table header | **RESOLVED** |
| **RC-9** | Derive the migration-map counts or drop them | **Removed, not corrected**, with the reasoning recorded and a `grep` recipe so a reader derives them from the map itself. This is the stronger fix: it removes the second source of truth rather than resynchronising it | **RESOLVED** |
| **RC-10** | Branch position stale | Now `0 behind / 14 ahead` at `BRANCH_TIP` and `0 behind / 16 ahead` at the head — **matching my own measurements exactly**, with the load-bearing `0 behind` stated as the GATE 0 condition | **RESOLVED** |

Gates re-run at 5.1: `LINT VERDICT: PASS` (1 INFO, unchanged) · `publication gate VERDICT: PASS,
BLOCKS: 0`.

## 3 · New material in 5.1, reviewed because it was not in scope before

Revision 5.1 adds a **§7 · ESCALATIONS**. It is manifest-local and therefore did not change the
hash, but it is text I had not seen, so I reviewed it rather than waving it through.

**It represents this review accurately.** It records PID-09 as `CONFIRMED` and PID-10 as
`REFINED`, states that Mirror recommends `ACCEPT` for both, and states explicitly that *"what
Mirror will not do is ratify them by passing the candidate."* That is exactly my position, not a
softened version of it. For ESC-3 it records that Mirror declines to set `N` alone under G.2, and
takes no position on which option the operator should choose.

**No added line claims a Mirror `PASS`, clearance, or ratification.** The `MIRROR_REVIEW` field
still reads `REVISION_REQUESTED`, citing both reviews by commit — it does not pre-record the
outcome of this pass.

One trivial imprecision, recorded and not actioned: §7 calls `N` *"declined by a third actor"*,
counting the annexes as an actor. Rhetorical, harmless.

## 4 · Annex C.2 verdict

```
REVIEW_ID:   REV-GOV311-MIRROR-003
OBJECT:      manifest revision 5.1 @ a87506a, over CANDIDATE_CONTENT_HASH c39ecae8…30c239
LEVEL:       R4 (delta)   REVIEWER: mirror   AUTHOR: plan   ADJUDICATOR: operator

STEELMAN
  The remediation did the harder thing twice. RC-6 could have been fixed by correcting three
  characters; instead every oid became a full 40-character object name, removing the class of
  error rather than its instance. RC-9 could have been fixed by recomputing five numbers; instead
  the numbers were deleted and replaced by the command that derives them, which is the repair the
  repository's own rule prescribes and the harder one to write, because it admits the summary
  should never have been there. And the whole revision was executed without touching a single
  content path — the discipline that let this pass be six commands instead of a third full review.

EVIDENCE_FOR      RC-6…RC-10 each verified mechanically (§2); hash, domain and fingerprints
                  unchanged (§1); both gates re-run green; §7 represents my verdicts faithfully.
EVIDENCE_AGAINST  Nothing blocking. Residual items are the ones I already classified non-blocking
                  in review 002 and did not ask to be changed: NBN-3, NBN-4.
ALTERNATIVES_CONSIDERED
                  Re-running R-1…R-7 in full. Rejected on evidence, not convenience: the content
                  hash is identical and no content path appears in the diff, so a full pass would
                  re-derive verdicts over bytes already reviewed.

VERDICT: CONFIRMED — all five required changes resolved; no new defect introduced by 5.1.
REVIEWER_CONFIDENCE: HIGH. Every claim in this record is a command output, not a reading.
RESIDUAL_UNCERTAINTY: unchanged from review 002 — verbatim fidelity to the operator's transmitted
                  frozen text remains unverifiable by me (R-2), and NBN-3's unbounded exclusion
                  remains a theoretical risk deliberately left unfixed.
EVIDENCE_NEEDED:  none for this disposition.
WHAT_WOULD_CHANGE_MY_MIND:
                  Any content path in `git diff 6b3c038 a87506a` — which would invalidate the
                  scope of this pass entirely and force a full review.
AUTHOR_RESPONSE:  PENDING_OPERATOR_ROUTING
```

## 5 · DISPOSITION

```
MIRROR_REVIEW: PASS_WITH_NOTES

CANDIDATE_ID:           CAND-20260816-GOV311 — content revision 5, manifest revision 5.1
CANDIDATE_CONTENT_HASH: c39ecae89677363802c8c7d24b704da185fc568fed360b08ad01adb39730c239
BASE_HEAD:              749a9a9b8f29c855f803a43b979c591532557561
MANIFEST_COMMIT:        a87506a0109a7d167fd195cf41b3c937e28bacf4
REVIEW_DATE:            2026-08-16      REVIEWER: mirror

REQUIRED_CHANGES:             none outstanding — RC-6…RC-10 all RESOLVED and verified
ESCALATE_TO_OPERATOR:         ESC-2, ESC-3 — decisions, not defects (see below)
NON_BLOCKING_NOTES:           NBN-3, NBN-4, NBN-5, NBN-6 (carried from review 002, unchanged)
GOVERNANCE_DEFECT_CANDIDATES: GDC-1, GDC-2 (carried, for the evidence-driven cycle)
```

**No change is required before `HUMAN_APPROVAL`.** `PASS_WITH_NOTES` is not being used to carry a
required change: there is none outstanding, and every note above is one I explicitly recommended
*not* be fixed in this candidate.

🔴 **One thing the operator should know before approving.** ESC-2 is not a defect and blocks
nothing — but **approving this candidate as written ratifies both declared deviations from the
frozen text** (PID-09's shared scientist contract; PID-10's pointer table in place of a replica).
I recommend ACCEPT for both, and I decline to ratify them myself, because H.1 puts deviations
from frozen governance with the operator. Approval is the act that settles them; it should be
made knowing that.

ESC-3 (`MIRROR_RETROSPECTIVE N`) blocks nothing and can cross the canonical commit unresolved:
retrospectives cannot run before there are batches to retrospect.

**No file of the candidate was modified. No canonical commit was executed. Plan was not contacted.
No approval was granted. No lease was acquired.**
