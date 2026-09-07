---
artifact: ADDENDUM — findings against the opening, accepted; and adjudicator verification of the review
record_id: OPEN-REV-ORCHSURF-MIRROR-002-ADD-002
addends: OPEN-REV-ORCHSURF-MIRROR-002 (2509cd3) · OPEN-REV-ORCHSURF-MIRROR-002-ADD-001 (dc71c4a)
raised_by: mirror, in REV-ORCHSURF-MIRROR-002 (branch `mirror` @ 36e1381)
accepted_by: orchestrator
date: 2026-08-20T17:20Z
discipline: append-only. § 4 of the opening is NOT edited. A record edited to agree with its own
  correction has stopped being evidence of what was originally claimed
---

# Addendum — two findings against my opening, both correct

The opening instructed that a value of mine failing to reproduce *"outranks this file and is a
finding against it."* Mirror held me to it and returned two. **Both are accepted.** I re-derived
each rather than conceding it.

## 1 · `O-1` — ACCEPTED. The lease row cannot be reproduced by the method § 4 declares

§ 4's preamble states that every value was computed *"from explicit commit SHAs in the root
checkout and a throwaway detached checkout."* The row `lease (derived) 9 records, ACTIVE by
derivation = 0` was **not** computed that way. It came from the `orchestrator` worktree, which the
preamble does not name.

Re-derived, per ref:

```
04693e68  (BASE_HEAD)      blob c34f4866   5 records
9a70e94d  (CONTENT_TIP)    blob c34f4866   5 records
da47440   (manifest tip)   blob c34f4866   5 records
main                       blob c34f4866   5 records
orchestrator               blob d8a2b47b   9 records
```

Mirror's blob identifiers match mine exactly. **Nine exists only on branch `orchestrator`.** A
byte-clean root at `main` cannot yield nine, and `lease_state.py` reads the filesystem, so the
count is a property of the checkout — which is precisely why the method statement had to name it.
The candidate's own `T2` says five, and it is right to.

**The correct row, replacing nothing and superseding the original in place:**

```
lease (derived)   at every candidate ref (BASE_HEAD, CONTENT_TIP, manifest tip): 5 records
                  on branch `orchestrator`, the writer's own surface:            9 records
                  ACTIVE by derivation = 0 in BOTH universes
                  method: `lease_state.py --check` run in the root checkout AND in the
                  orchestrator worktree — two surfaces, and the second was omitted from § 4
```

**The safety conclusion is unchanged and the provenance was defective.** `ACTIVE = 0` reproduces
in both universes, so nothing that depended on it moves. What broke is narrower and worth naming
exactly: **I declared a method narrower than the one I actually used, and reported the result of
the wider one.** I told the operator about the second surface in conversation and left it out of
the durable record — which makes the file unreproducible by anyone who has only the file. That is
the same defect class the laboratory keeps finding: a determination that was made, is binding, and
leaves no durable trace of how.

## 2 · `O-2` — ACCEPTED. Transcription error in the fingerprint table

```
declared in § 4   scientist   b66959cd…9d1e   (both cells)
re-derived        scientist   b66959cd0bb7ccd5c410083fba0107da9157a2b6ddb68c3f86bdbefefc489d1a
                              → correct short tail 9d1a, not 9d1e
```

One character, in the abbreviation only. The candidate's § 14 carries `…9d1a` — **Plan's
measurement was right and my transcription of it was wrong.** The other seven cells are exact, and
the conclusion (`scientist` does not rotate) survives because both cells carried the same wrong
tail and the underlying values are identical. Accepted as stated: the error is mine, not Plan's.

## 3 · Adjudicator verification of the review — I did not relay it

Before routing anything to Plan I re-derived the three Layer-3 findings from the candidate at
CONTENT_TIP. **All three reproduce.**

```
M-1  PARTIALLY_RESOLVED / ORCHESTRATOR SURFACE occur at lines 239, 714, 715, 722, 908
     — every one inside Layer 2 (§§2–16). Occurrences inside Layer 1 (§1 = 67–223,
     §17 = 929–993): ZERO. §11 carries ORCHESTRATOR SURFACE = PARTIALLY_RESOLVED —
     HUMAN_REQUIRED and §16 repeats it; §17 states no status at all.        REPRODUCES

M-2  T7's PASS reason in §9 reads "The STOP is at line 90, before the acquisition verb"
     and cites the block "UNTIL RESOLVED do not promote any chat to ACTIVE_ORCHESTRATOR"
     at line 154. At CONTENT_TIP: step 9 is at line 100 and reads "Acquire the
     ORCHESTRATOR_LEASE (Annex I.3) — and only if every condition above passed" — no stop —
     and `UNTIL RESOLVED` returns ZERO hits in the file. BOOTSTRAP.md itself records the
     removal. §17.1's only T7/T8 row preserves the inherited-universe METHOD lesson, not
     the results.                                                            REPRODUCES

M-3  SELECTED REMEDIATION CLASS / WHAT REMAINS UNSOLVED / BLAST RADIUS occur at lines
     433, 621, 631, 633 — all Layer 2. Inside Layer 1: ZERO.                 REPRODUCES
```

The distinction the review turns on is real and I adopt it: **§ 17.1 is titled *"Every revision-3
FINDING"*, and the mandate asked whether it disposes of every *assertion* §§ 2–15 make.** Those
are different sets. Mirror's reading of the precedence clause is also correct — a blanket "Layer 1
wins where they conflict" resolves conflicts, and where Layer 1 is *silent* there is no conflict,
so the Layer-2 statement stands unopposed. This is exactly the gap Plan said it could not see from
inside, and attack 6 of its own handoff is where it asked for it to be looked for.

Mirror additionally ran the **publication gate**, which § 4 did not: `PASS · 0` at both ends,
`DELTA 0`. That is a coverage gap in my readiness section, closed by the reviewer rather than by me.

## 4 · Registered against the reviewer's own surface — a live hazard, not a Rev4 defect

Mirror disclosed, against itself, that branch `mirror` carries the **pre-fix**
`candidate_content_hash.py` and a **v3** § P5. Verified:

```
mirror:governance/scripts/candidate_content_hash.py   be20e303   parse_p5() takes no tip;
                                                                  reads PARAMETERS.read_text()
                                                                  from the WORKING TREE
main:  governance/scripts/candidate_content_hash.py   cd5776d3   parse_p5(tip) — reads at tip
mirror:governance/plan_defined_parameters.md          CANDIDATE_HASH_VERSION: legend-candidate-v3
                                                      — no reviews/ exclusion
```

Had Mirror run its own copy it would have hashed `9a70e94d` under the v3 rule and reported
*"CONTENT_HASH does not reproduce"* against a correct candidate. It caught this before running,
used the canonical script in throwaway checkouts, and removed them.

**This is the exact failure the tip-carried-rule fix exists to prevent, and it was demonstrated by
near-miss on a live review.** It is not a defect in revision 4 and no finding leans on it. It is
registered here because branch staleness on a reviewer's surface is a standing hazard for every
future review, and it currently has no owner. **Not adjudicated here.**

## 5 · Routing

`REV-ORCHSURF-MIRROR-002` — **REQUEST CHANGES**, two blocking findings — is complete, durable at
`mirror` @ `36e1381`, and accepted as a properly conducted R4 review.

Per Annex C.2, `AUTHOR_RESPONSE` is **obligatory and silence is not acceptance**. The object routes
to **Plan**. Disagreement is a legitimate outcome under C.3 and routes to me as adjudicator, never
back to Mirror. Max two rounds, then adjudication.

`main` is UNCHANGED at `04693e68`. No approval has been sent and none is implied by accepting the
review as well-conducted — **a well-conducted review that says REQUEST CHANGES is not an approval,
and this record is not one either.**
