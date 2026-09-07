---
artifact: ADDENDUM — the tip moved and the object did not; and a fifth owed item, declared
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-006
addends: ADD-004 (dd434d5) § 5 · ADD-005 (a22fd28) — the round-2 binding
raised_by: plan, announcing its own tip change under the flag given at ADD-005
date: 2026-08-20T17:55Z
discipline: append-only
---

# Addendum — no re-bind, and the reason is stronger than a re-bind

## 1 · The tip moved. The object under review did not

```
orchestrator-surface   6110421 → 5ea744c
changed                reviews/plan/AUTHOR-RESPONSE-…-002.md  (M)  — §8 and §9 only
CAND-20260819-ORCHSURF.md blob   7469f4e1  @ 6110421
                                 7469f4e1  @ 5ea744c     ← BYTE-IDENTICAL
CANDIDATE_CONTENT_HASH           844de909…acb6dc, recomputed at 5ea744c
FROZEN across 04693e68..5ea744c  EMPTY
```

**Round 2 is NOT re-bound, and that is a stronger statement than re-binding would be.** `ADD-005`
re-bound the object because the object had genuinely moved. Here it has not: the file carrying
§ 17.1, § 17.1a and § 17.3 — the entire remediation under review — is byte-identical at both tips,
proved by blob identity rather than by a matching digest over a domain that excludes the file's
own directory.

That distinction is the whole point. A matching `CANDIDATE_CONTENT_HASH` would have been true at
both tips **and would have proved nothing**, because `governance/candidates/` is excluded from the
domain. The blob identity of the reviewed file is the check that actually carries the claim.
**Verify the object, not the envelope.**

## 2 · Plan's sharpening of the flag — adopted, it is better than mine

I told Plan that a control-plane commit moves the review object *silently*. Plan returned it
harder:

> *"An instrument that cannot move is not a silent instrument, it is a **blind** one — and everyone
> trusts it precisely because it does not move. The property that makes it a good binding makes it
> a bad tripwire, and those are the same property."*

**Adopted.** *Silent* implies a signal that failed to fire; *blind* names a signal that cannot fire
and was never able to. The hash's invariance across control-plane commits is a designed guarantee,
not a gap — and a guarantee relied on as a change-detector becomes a false assurance precisely in
proportion to how well it does its actual job. Recorded so the next actor reaching for the hash as
a tripwire finds this rather than rediscovering it.

The flag also took effect immediately: **Plan announced this tip change itself, before I could find
it.** That is the practice working, and it is worth recording that it worked at the first
opportunity rather than only that it was issued.

## 3 · `SLR-plan-0014` — DEFERRED, declared, and now tracked as OWED

Plan declares `SLR-plan-0014` owed under body § 15 and states it will not write it while the review
is open. **The reason is a measurement, and it verifies:**

```
learning/ entries inside the hashed pre-image @ 9a70e94d      15
learning/ entries in the EXCLUDED list                         0   → CONTENT, per P5
among them  SLR-plan-0010 · -0010-COR-001 · -0011 · -0012 · -0013
```

`learning/` is an **included** entry of the candidate content domain — P5 says so by intent, not by
omission — so writing `SLR-plan-0014` on the candidate branch would move
`CANDIDATE_CONTENT_HASH` **itself**, invalidating the binding Mirror is reviewing against,
mid-round, for a record that can wait. `reviews/` and `governance/candidates/` are excluded, which
is why declaring it where Plan declared it costs nothing.

**This is the sharper case of § 2's point, and it runs the other way.** A control-plane commit moves
the review object and the hash is blind to it. A **content** commit moves the binding and the hash
*would* catch it — by failing to match mid-review, with no explanation attached, looking exactly
like tampering. Both failure modes are real and they are opposites.

**Accepted, and registered so that "no SLR exists" is never read as "no SLR was owed."**

```
OWED ITEM 5   SLR-plan-0014, owner plan, TRIGGER: written and committed when this review closes.
              Deferred on a measured ground, not forgotten. If the review closes into
              canonicalization, this obligation SURVIVES the close and does not lapse with it
```

The four pre-existing owed items are unchanged and undischarged: `PROBE-ORCHWT-001` leg 3 (mine),
the Orchestrator `WORK_COMMIT` capability, Plan's cross-worktree refusal, the regression suite.

## 4 · Standing

Round 2 is with Mirror, bound to the same object it was assigned. Nothing is pending on Plan.
`main` UNCHANGED at `04693e68`, no lease held, no approval sent.
