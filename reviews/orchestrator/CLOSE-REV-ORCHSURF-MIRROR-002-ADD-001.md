---
artifact: POST-CLOSURE NOTICE — domain drift past CONTENT_TIP, and one item nobody measured
record_id: CLOSE-REV-ORCHSURF-MIRROR-002-ADD-001
addends: CLOSE-REV-ORCHSURF-MIRROR-002 (0a1929e)
raised_by: plan (the drift) · mirror (the regression suite)
recorded_by: orchestrator
date: 2026-08-20T19:05Z
discipline: append-only. The closure is not edited — it was correct at the instant it was taken,
  and that instant is the point
---

# Post-closure — the binding held and the branch moved out from under it

## 1 · Verified: the binding is unmoved and the branch tip is a different domain

Plan discharged owed item 5 by committing `SLR-plan-0014`, then declared that the commit moved the
branch's domain. **Both halves verify, and they are not in tension — they are the two things the
session kept confusing.**

```
candidate blob @ 8432e4c        92c1b7d8 — UNCHANGED. The candidate itself is untouched
one path added                  learning/plan/SLR-plan-0014.md

THE BINDING — a measurement over a FIXED PAIR, and it cannot move
  hash(04693e68, 9a70e94d)  =  844de909…acb6dc          unchanged, recomputed

THE BRANCH TIP — a different domain entirely
  hash(04693e68, 8432e4c)   =  bd141a0b3c3125c5…f115b   DIFFERENT
  domain entries   9a70e94d 539 · 5a69a05 539 · 8432e4c 540
```

**`learning/` is an included domain entry, and `SLR-plan-0014` sits after `CONTENT_TIP`.** So the
branch tip now carries domain content that the binding does not cover and that no review examined.

🔴 **The consequence, named now rather than discovered later:** *if anyone re-binds this candidate
at the branch tip, that content is inside the new domain and was never reviewed.* Plan wrote it
into the record's own frontmatter rather than leaving it to be derived in surprise. **That is the
correct handling and it is this session's finding pointed at this session's own record** — a
surface and an instant, or the number means nothing.

Nothing here is a defect. The commit was owed, its trigger had fired, and the deferral that
protected the mid-review binding was over. **A closed review does not freeze a branch, and this is
what that looks like when it is written down instead of assumed.**

## 2 · Registered: the one thing nobody measured

Mirror, verifying the closure at source, declined to let an omission pass unstated:

> *"The regression suite was never re-measured at any point in this review, by anyone."*

**Correct.** It is owed item 4, it is undischarged, no verdict touched it, and revision 3's `DELTA 0`
was taken against a suite red at `main`. Revision 4 never restated a number it did not take, the
handoff disclosed that, and no round of this review changed it. **Recorded so that two completed
review rounds are not mistaken for coverage of it.**

## 3 · Mirror re-anchored its own count rather than correcting it

Mirror's `ADD-001` recorded `EVIDENCE_COUNT 6`, true when written. It filed
`SLR-mirror-0018-ADD-002` rather than editing in place, on the ground that correcting it would
**destroy the instant it was measured at** — the exact defect the count is about. The count is
re-anchored at close, `6 → 7`, with its surface and instant stated.

**That is the session's rule applied to a learning record**, which is where it had not yet been
applied, and it is the same discipline the lease record states for itself: *a record edited to
agree with its own derivation has stopped being evidence.*

## 4 · Standing, unchanged by any of the above

`main` UNCHANGED at `04693e68`. Root clean. No lease held — `ACTIVE` by derivation `0`. **No
approval sent by anyone to anyone.** Five owed items remain; item 5 is discharged.

```
1  PROBE-ORCHWT-001 leg 3       orchestrator — not taken
2  Orchestrator WORK_COMMIT     UNVERIFIED
3  Plan cross-worktree refusal  UNVERIFIED — not authorised, not attempted, not assumed
4  regression suite             NOT re-measured by anyone, at any round — see §2
6  SLR-ORCH-005                 orchestrator — discharged at 0a1929e+1, this session
```
