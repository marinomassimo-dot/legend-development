---
artifact: REVIEW CLOSURE — Annex C.3 (`opening, ownership and closing` is Orchestrator's)
record_id: CLOSE-REV-ORCHSURF-MIRROR-002
closes: REV-ORCHSURF-MIRROR-002, rounds 1 and 2
object: CAND-20260819-ORCHSURF r4 · CANDIDATE_CONTENT_HASH 844de909…acb6dc @ BASE_HEAD 04693e68
  CONTENT_TIP 9a70e94d · closing manifest tip 5a69a05 · candidate blob 92c1b7d8
reviewer: mirror · author: plan · adjudicator: orchestrator
closed_by: orchestrator
closed_at: 2026-08-20T18:55Z
outcome: FINDINGS RAISED AND DISPOSED. No DISAGREEMENT_UNRESOLVED — nothing was contested
approval: NONE. Not sought, not granted, not implied by this closure
---

# Closure — `REV-ORCHSURF-MIRROR-002`

## 1 · What this closure does and does not mean

**It means the package was examined.** Two rounds under Annex C.3, four findings raised by the
reviewer and one residual raised by the adjudicator, all disposed, nothing contested by any party.

🔴 **It is not an approval and not a readiness certificate.** This is MAJOR and governance:
`HUMAN_APPROVAL` under Annex H.1 is the operator's alone. Canonicalization would additionally
require an `ACTIVE` `ORCHESTRATOR_LEASE` and `GATE 0–5`. **No lease was acquired at any point in
this session and none is claimed.** Approval is not authorization, and a completed review is
neither.

## 2 · Final state, measured by the adjudicator at the closing tip

```
branch orchestrator-surface   5a69a05   candidate blob 92c1b7d8
CANDIDATE_CONTENT_HASH        844de909c6b0d1cef4ce4014e9fef3870aeb8729e8b3c6ac029a12dfcaacb6dc
                              recomputed at the closing tip — unchanged since 9a70e94d
BASE_HEAD                     04693e68 == canonical main, verified from git refs
FROZEN                        diff over body + annexes A–J across 04693e68..5a69a05: EMPTY
PUBLICATION GATE              PASS · BLOCKS 0        run by me, throwaway checkout at 5a69a05
LINT                          PASS · 1 pre-existing INFO   run by me, same checkout
lease (derived)               ACTIVE by derivation: 0
root checkout                 main @ 04693e68, 0 dirty entries — byte-identical all session
peer worktrees                mirror and evidence-index clean; neither written to by me
```

## 3 · Findings and disposition

```
M-1  BLOCKING   no operative status for the package's own subject          DISPOSED · §17.1a
M-2  BLOCKING   T7/T8 PASS on reasons revision 4 deleted                   DISPOSED · results
                                                                          withdrawn + §17.3 discloses
M-3             §8 remediation accounting absent from Layer 1              DISPOSED · row withdrawn
M-4  BLOCKING   §17.3 asserted the gate does not pass; §1 records PASS      DISPOSED · past tense,
                (raised at round 2, ruled IN SCOPE)                        and the correction recorded
R-1             row 4 inherited a surface it was not measured over         DISPOSED · both deltas
                (raised by the adjudicator after rounds were spent)        now carry their surface
```

**Two adjudications were required and both are recorded with grounds**, at `ADD-004` § 4 (T7
withdrawn — the answer is entailed by the design under test) and `ADD-008` § 2–3 (`M-4` in scope;
the `BLAST RADIUS` diagnosis corrected from arithmetic to population).

## 4 · Findings against the adjudicator — this file's own author

Recorded because a closure written only about other actors would be the same selection error this
session spent itself finding.

```
O-1   the lease row could not be reproduced by the method §4 declared   raised by mirror
O-2   scientist fingerprint transcribed …9d1e for …9d1a                 raised by mirror
D-1   line anchors valid only at CONTENT_TIP, not at the fetched tip    raised by plan
I-6   grep for a string the document does not contain, read as absent   self-caught
I-7   a population failure one step from being filed as arithmetic —
      the exact error I had just ruled against, while applying it       self-caught
```

## 5 · The structural finding, which outlives the candidate

Seven instances, across all three actors: **an instrument reporting faithfully about the wrong
object.** Not one returned a wrong value. The hash blind by construction; anchors valid only
against an uncarried surface; a superseded verifier on a reviewer's own branch; testimony where
measurement was available; a window published as a population; a query for a string the document
does not contain; an unnamed population read as a wrong number.

**An eighth, of a different kind**, contributed by Plan at `M-4`: a *derived* statement that did not
follow its source — `SLR-plan-0012` L-1 inverted. A claim corrected at its source is not thereby
corrected where it was echoed.

**The mitigation is not "be more careful."** Every correction this session produced came from one of
two mechanical acts: **a second actor who did not share the first's assumption about the surface**,
or **checking the other population before writing the claim**. Instance 7 is the strongest evidence,
because it happened to the actor holding the rule, immediately after stating it, while applying it.
**If a rule cannot survive contact with the person who just wrote it, recording the rule is not the
mitigation.**

## 6 · Owed, and not discharged by this closure

```
1  PROBE-ORCHWT-001 leg 3      orchestrator. Not taken. No verdict here discharges it
2  Orchestrator WORK_COMMIT    UNVERIFIED. CONFIGURED != PROVEN, applied to its enforcer
3  Plan cross-worktree refusal UNVERIFIED. Not authorised, not attempted, not assumed
4  regression suite            NOT re-measured at revision 4
5  SLR-plan-0014               plan. Trigger: review close — which is NOW. Survives the close
6  SLR-ORCH-005                orchestrator. Trigger: session close
```

`CAND-20260820-ROOTGUARD-001` remains unopened, with the re-framed T7 registered as owed to it.
The branch-staleness hazard is registered with `OWNER: UNASSIGNED` and routed but not opened.

## 7 · To the operator

Four decisions are the operator's and none was taken here:

1. **Canonicalization** of ORCHSURF r4 — `HUMAN_APPROVAL`, then lease + `GATE 0–5`.
2. **The redacted identifier** remains reachable in branch history at `ec4bf60` and `1a650d8`, both
   ancestors of the tip. A non-squash merge carries it into `main`'s history, where the publication
   gate does not look because it reads a tree at a tip.
3. **`PROBE-ORCHWT-001` leg 3** — mine to run, not run, awaiting instruction.
4. **The branch-staleness stream** — narrow (G.2, Mirror's instrument) and general (Plan's
   reconciliation domain) were routed separately; opening either is outside this task.
