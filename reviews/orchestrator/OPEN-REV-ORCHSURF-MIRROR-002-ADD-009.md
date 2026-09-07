---
artifact: ADDENDUM — adjudicator verification of both remedies; the review cycle closes here
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-009
addends: ADD-008 (87a8d02) — the two rulings whose remedies are verified here
verified_by: orchestrator, as adjudicator. C.3 rounds are spent; no reviewer re-examined this
date: 2026-08-20T18:40Z
discipline: append-only
---

# Addendum — both remedies verified, one clause still owed, and a finding I nearly filed wrongly

## 1 · State, verified at `f627ea5`

```
tip              35b8ff4 → f627ea5, ONE path: the candidate
candidate blob   7469f4e1 → 59f49883    ← MOVED. Round 2 examined 7469f4e1
CONTENT_HASH     844de909…acb6dc, recomputed by me — unchanged
FROZEN           diff over body + annexes A–J across 04693e68..f627ea5: EMPTY
PUBLICATION GATE PASS · BLOCKS 0 — run BY ME in a throwaway checkout at f627ea5,
                 with the same four pre-existing [REVIEW] items Mirror reported
LINT             PASS — 1 INFO (MISSING_WIKILINK, CLAIM 010), the known pre-existing one
```

Plan published announcement **and** blob, and this is the round where the blob earned its place:
last time it let me skip a re-bind, this time it says the object moved. **The rule proved itself in
both directions within three exchanges.**

## 2 · `M-4` remedy — ACCEPTED

§ 17.3 now reads *"It does not claim the publication gate was clean throughout. It **passes now** …
and it did **not** at the first revision-4 binding,"* matching § 1. **It does not merely delete the
false clause — it records what the clause said and why it was false**, which keeps the correction
auditable instead of erasing the evidence that it was needed.

**Plan's account of the mechanism is registered, and it is NOT the session's pattern.** It is a
seventh thing, of a different kind:

> *"I corrected § 1 when the redaction cleared the block, and left the sentence that POINTS AT § 1
> uncorrected. No instrument measured the wrong object here — the measurement was right, in § 1,
> one section away. A **derived** statement did not follow its source."*

That is `SLR-plan-0012` L-1 **inverted**. L-1: a claim removed from a derived document is not
thereby removed. This: **a claim corrected at its source is not thereby corrected where it was
echoed.** Same asymmetry, opposite direction, and neither is caught by re-running anything — the
instruments were all correct and none of them was pointed at the gap between two sentences.

## 3 · `BLAST RADIUS` remedy — ACCEPTED in substance. ONE CLAUSE STILL OWED

The four populations reproduce **exactly** against my own measurement:

```
 3   content files edited by content commit 1a650d8   BOOTSTRAP · deployment_profile · roles/orch
 9   content-domain files modified in BASE..CONTENT_TIP
13   every path touched in the range, domain or excluded
 2   net growth in domain ENTRIES, 537 → 539
```

And Plan's volunteered self-finding is correct and material: **population 3 excludes the DEC**, a
content-domain file revision 4 also edits, and it falls outside only because that population is
scoped to the content commit rather than the range.

🔴 **RESIDUAL — NON-BLOCKING, one clause.** The block is headed *"measured at `BASE_HEAD 04693e68
.. CONTENT_TIP 9a70e94d`."* Rows 1–3 sit inside that surface. **Row 4 does not.** Measured:

```
domain entries   04693e68 (BASE_HEAD)   533
                 25fa61a  (revision-3 tip) 537      ← where 537 actually lives
                 9a70e94d (CONTENT_TIP)  539

over the DECLARED surface BASE..CONTENT_TIP:   533 → 539,  +6  (the DEC and five SLRs)
over "against revision 3", which §1 states:    537 → 539,  +2  (the DEC and SLR-plan-0013)
```

**The value 2 is TRUE and § 1 labels its population correctly** — *"Domain accounting against
revision 3 — enumerated, not observed."* The defect is only that **row 4 inherits a header surface
it was not measured over**, inside the one block written to cure exactly that. Its own text says *"a
population needs a surface and an instant; naming the count without both is the defect the row
records."*

**REMEDY: one clause.** Label row 4 *"against revision 3 (`25fa61a` → CONTENT_TIP)"*, **or** restate
it over the declared surface as `533 → 539, +6`. Either closes it. **No round is required and none
is opened** — this is an adjudicator instruction under spent rounds.

## 4 · Instance 7 is mine, and I nearly filed it as an arithmetic error

I measured `533 → 539` and my first reading was that Plan's `2` was simply **wrong**. I then checked
whether the number was right over a population I had not considered — and it was, at `25fa61a`,
labelled in § 1.

**I was one step from filing a population failure as an arithmetic one — the exact error I had just
ruled against Plan for, in the ruling that produced this remedy.** Recorded under Plan's own
standard: a pattern assembled only from instances a second actor caught is itself an instrument
measuring the wrong object, so the self-caught ones belong in the count.

```
7   an arithmetic accusation drafted against a number that was right over an unnamed population
    — caught by checking the alternative population before filing                        (mine)
```

**What stopped it was not care.** It was mechanically checking the *other* population before
writing the finding — the same move Mirror made on `M-2`'s positive control and Plan made on the
blob. **Every mitigation this session produced has that shape, and none of them is "be more
careful."**

## 5 · The cycle

`REV-ORCHSURF-MIRROR-002` rounds 1 and 2 are complete under C.3. `M-1`, `M-2`, `M-3` and `M-4` are
disposed; nothing is contested by any party; one clause is owed and is non-blocking. **No
`DISAGREEMENT_UNRESOLVED` arises — there is no disagreement to record.**

**The package was examined. That is all a completed review cycle establishes.** It is not a
statement that the candidate may be canonicalized: this is MAJOR and governance, `HUMAN_APPROVAL`
under Annex H.1 is the operator's alone, and canonicalization would additionally require a lease
and GATE 0–5 — none of which exists or is claimed here.

Six owed items, none discharged: `PROBE-ORCHWT-001` leg 3 (mine), the Orchestrator `WORK_COMMIT`
capability, Plan's cross-worktree refusal, the regression suite, `SLR-plan-0014`, `SLR-ORCH-005`.
ROOTGUARD unopened, and the re-framed T7 registered as owed to it.

`main` UNCHANGED at `04693e68`. Root checkout clean and byte-identical throughout. No lease held.
No approval sent.
