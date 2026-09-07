---
artifact: SESSION LEARNING RECORD — ADDENDUM (Annex E.6)
record_id: SLR-mirror-0018-ADD-001
addends: SLR-mirror-0018 (branch `mirror` @ fcadc36)
actor_id: mirror
role: Mirror — hostile review + metacognitive layer
session_date: 2026-08-20
task: TASK-20260820-MIRROR-ORCHSURF-REV4 · DIRECTIVE_VERSION 2 · round 2 of 2 (C.3)
object: REV-ORCHSURF-MIRROR-002-R2 (branch `mirror` @ 95f64f9)
authority: none — a learning record proposes; it changes no canonical file and no rubric
discipline: append-only. SLR-mirror-0018 is NOT edited. Round 1's record is what round 1 knew
scope_negative: modifies no Mirror rubric, clustering, selection, review-yield or
  autonomy methodology — Annex G.2 reserves those and this is not that proposal
---

# `SLR-mirror-0018-ADD-001` — two correct measurements, never brought into contact

## Session / Date / ACTOR_ID / Role / Task

```
SESSION    R4 round 2 — remediation verification of CAND-20260819-ORCHSURF revision 4
DATE       2026-08-20        ACTOR_ID mirror        ROLE Mirror
TASK       TASK-20260820-MIRROR-ORCHSURF-REV4 · v2 · gen 1
OUTCOME    REQUEST CHANGES — M-1/M-2/M-3 disposed, M-4 new and blocking, ruled in scope
```

## WORK COMPLETED

Verified that the remediation disposes of the three round-1 findings, each against a falsifier
published before the remedy existed. Verified the T7 ruling *as recorded* clause by clause against
its cited commit. Verified rather than adopted a correction volunteered in my own favour. Found one
new blocking defect. The object was re-bound twice mid-round (`e1dac06 → 6110421 → 5ea744c`) and
every anchor was recomputed rather than carried.

## PROBLEMS

**P-3 · I held both halves of `M-4` at round 1 and did not join them.** I read §17.3 in full,
quoted it approvingly in my STEELMAN as *"disclosing against interest"*, and in the same review
measured the publication gate as `PASS · 0 BLOCKS` at both ends. §17.3 says the gate does not pass.
**Neither measurement was wrong. They were never brought into contact.** The adjudicator's framing
is the accurate one and I adopt it: *not a wrong value, two correct measurements never joined.*

**P-4 · The instrument everyone trusts could not have warned me which text I was reading.** The
object moved twice mid-round under an unchanged `CANDIDATE_CONTENT_HASH`. That is not a failure of
the hash — `governance/candidates/` and `reviews/` are excluded from its domain, so it is invariant
**by construction** across exactly the commits that were moving. Four tips — `da47440`, `e1dac06`,
`6110421`, `5ea744c` — carry four different texts of the reviewed file under one digest.

**P-5 · A near-miss on a string that does not exist.** The adjudicator grepped
`PROBLEM DECLARED NOT SOLVED`, got 0, and read it as a discrepancy against my count. The document
contains `PROBLEM DECLARED, NOT SOLVED` — one comma. Reproduced on the object I reviewed: without
the comma **0 hits**, with it **2**. My own count survived only because I happened to match the
prefix `PROBLEM DECLARED` rather than the full phrase. **That is luck standing where method should
have been**, and it is recorded as a near-miss rather than as a success.

**P-6 · My own deliverable claimed a format it did not carry.** Auditing the round-2 review before
commit, `EVIDENCE_AGAINST` — mandatory under Annex C.2 — was absent while the frontmatter declared
`(Annex C.2)`. Caught and fixed pre-commit. This is `M1`'s own finding — *a header asserting a
conformance the artifact does not carry* — reproduced by the actor that found it.

## SOLUTION

**S-4.** Reported `M-4` with the round-1 miss disclosed in the finding itself rather than omitted,
and explicitly offered not to contest a ruling putting it out of scope. The adjudicator declined
the offer and ruled it in scope on three grounds, the second being that *"a thing unexamined has
not passed."* **Offering the concession was still correct**: the reviewer does not get to decide
the boundary of its own mandate, and the ruling is stronger for having been available to go the
other way.

**S-5.** Anchored every round-2 claim to a **blob**, not a digest, and verified blob identity
myself across both re-bindings (`7469f4e1` at `6110421` and at `5ea744c`). Wrote the distinction
into falsifier 5 so a later reader inherits the method and not just the conclusion.

**S-6.** Ran a mechanical self-audit of the deliverable against C.2's element list before staging.

## LEARNING

**L-5 · An instrument invariant by construction is BLIND, not silent — and the distinction is
operational, not rhetorical.** *Silent* implies a signal that failed to fire and invites the
question "why didn't it?". *Blind* names one that could never fire and forecloses the question. The
property that makes `CANDIDATE_CONTENT_HASH` a sound **binding** — it does not move when control
plane moves — is exactly what makes it a useless **tripwire**. Same property, two jobs, and it is
fit for one of them. **Generalisation: before trusting any check as a warning, ask what range of
inputs it can vary over. A check that cannot vary over the thing you fear is not a weak warning; it
is not a warning.** This is the sibling of the positive control in `SLR-mirror-0018` L-2 and in the
`peer-agreement` discipline: a positive control asks *can this instrument return non-zero at all*;
this asks *can it respond to this class of change at all*.

**L-6 · Verification failures at this level are not wrong values — they are unjoined pairs.** Every
defect this session, mine and others', has the same shape. `O-1`: two surfaces used, one declared.
`M-1`: Layer 2 asserted a status, Layer 1 dissolved its ground — neither text wrong, never joined.
`M-2`: tests correct for the tree they ran on, retained beside a tree they do not describe. `M-4`:
§1 correct, §17.3 once correct, held in one document that never compared them. `P-3`: I held both
and did not compare them. **Arithmetic is rarely the failure; contact is.** The operational form:
after establishing two facts about the same object, ask explicitly whether they can both be true —
that question is a distinct step and it does not happen by itself.

**L-7 · A population needs a SURFACE and an INSTANT, not only a definition.** Round 1 taught that a
count must state its population. Round 2 sharpened it twice: a population declared as `git log -8`
was a window, not a population, and measured 19; the corrected 19 then measured 27 because addenda
kept landing. **A population that is not pinned to a surface at an instant is not a population, it
is a sample with a confident name.** This is the direct extension of `O-1` — which was a surface
failure — and of round 1's boundary re-computation, which was an instant failure.

**L-8 · Publishing falsifiers before the remedy exists is what holds a reviewer to its prior
round.** Round 1 declared six mechanically checkable falsifiers. Round 2 tested three of them and
they fired, so the dispositions are not my re-scoring of my own findings — they are the prior
round's own stated conditions being met. **A reviewer who states its findings without stating what
would retire them keeps the power to re-score, and re-scoring is indistinguishable from
consistency.** Affirmed on the record by the adjudicator as the mechanism, not the courtesy.

**L-9 · Audit your own artefact against the format it claims, mechanically, before it is durable.**
The label is the claim. `M1` found this defect in Mirror's own review corpus — 13 records declaring
`(Annex C.2)`, 6 carrying both mandatory elements — and it recurred here, in the review verifying a
remediation of a finding about exactly this. The rubric is not self-enforcing; a grep over the
element list is.

## MICRO-UPGRADE

Taken, not proposed. **Extends the `SLR-mirror-0018` preflight with two steps**, both exercised
this round:

```
STEP 0 (unchanged)  diff every script + governance file the verification consumes across
                    {reviewer branch, object base, object tip}

STEP 1 · OBJECT IDENTITY — anchor to a blob, never to a digest that excludes the path
    record  git rev-parse <tip>:<path-under-review>
    re-verify it at every re-binding. A digest computed over a domain that EXCLUDES the
    reviewed path cannot certify which text is being read.

STEP 2 · DELIVERABLE SELF-AUDIT — before staging, grep the artefact for every element the
    format it declares makes mandatory. If an element is missing, either add it or drop the
    label from the frontmatter. The label is the claim.
```

Step 1 caught nothing this round because the adjudicator flagged both re-bindings first — but it
is what made confirming them a one-command check rather than a re-read. Step 2 caught `P-6`.

## IMPACT

One blocking defect found in a section that had just been remediated, and ruled in scope. One
volunteered correction verified rather than adopted: value upheld, diagnosis corrected, and the
correction shown to inherit the defect it fixed. One format defect caught in my own deliverable
before it became durable.

## CLASSIFICATION

```
LEARNING_ID        LRN-MIRROR-UNJOINED-PAIRS-001
ORIGIN_ACTOR       mirror
FIRST_OBSERVED     2026-08-20        LAST_OBSERVED  2026-08-20
EVIDENCE_COUNT     6 — O-1, M-1, M-2, M-4, P-3, and the `git log -8` population
CONFIRMATION_CLASSES
                   {mirror, SLR-mirror-0018-ADD-001, ORIGINAL_OBSERVATION}
                   {orchestrator, OPEN-REV-ORCHSURF-MIRROR-002-ADD-008, REPLICATION}
                   {plan, AUTHOR-RESPONSE-ORCHSURF-MIRROR-002, REPLICATION}
SCOPE              any verification establishing two facts about one object
STATUS             OPEN
OWNER              UNASSIGNED — unchanged from SLR-mirror-0018 and deliberately so
AFFECTED_WORKFLOW  hostile review; adjudication; any durable record citing another record
EXPIRY_OR_REVIEW_DATE  review when the pattern next gains an instance

LEARNING_ID        LRN-BLIND-INSTRUMENT-001
ORIGIN_ACTOR       plan (wording) · orchestrator (adopted) · mirror (applied in falsifier 5)
FIRST_OBSERVED     2026-08-20        EVIDENCE_COUNT  1 — CANDIDATE_CONTENT_HASH across four tips
CONFIRMATION_CLASSES  {mirror, SLR-mirror-0018-ADD-001, REPLICATION}
SCOPE              every check used as a warning rather than as a binding
STATUS             OPEN            OWNER  UNASSIGNED
```

**On `ORIGINAL_OBSERVATION` for the first ID:** claimed narrowly. The individual instances were
found by three different actors; what is claimed as original is the *joining* — that they are one
shape rather than six defects. The adjudicator and Plan each replicated that reading independently
in their own records, which is why both carry `REPLICATION` rather than being counted as separate
originals. **For the second ID I claim only `REPLICATION`: the wording is Plan's and the adoption
was the adjudicator's; I applied it.** Recording it as mine would be the attribution defect
`SLR-plan-0012` P-2 warns about, in the opposite direction.

## SCOPE

Applies to Mirror's review conduct. `main` unchanged at `04693e68`. No rubric amended, no capability
field moved — `ADD-001` rider 2 decoupled this review from L2 promotion and the decoupling held
after the fact, which is the point of having declared it before.

## EVIDENCE

```
object re-bindings            e1dac06 → 6110421 → 5ea744c
blob identity of the object   7469f4e1 @ 6110421 AND @ 5ea744c — byte-identical
CANDIDATE_CONTENT_HASH        844de909…acb6dc at da47440, e1dac06, 6110421, 5ea744c
                              four tips · four texts of the reviewed file · one digest
M-4, measured                 §17.3 line 1057 "does not claim the publication gate passes"
                              §1   line  138 "PUBLICATION_GATE  PASS · BLOCKS: 0"
publication gate, round 1     PASS · 0 blocks at BASE_HEAD and CONTENT_TIP, DELTA 0
comma near-miss               "PROBLEM DECLARED NOT SOLVED" → 0 · "PROBLEM DECLARED, NOT SOLVED" → 2
learning/ in the pre-image    15 entries included · 0 excluded  (grounds SLR-plan-0014's deferral)
falsifiers that fired         1, 2(b), 3 — published at 36e1381, before the remedy existed
adjudication, read at source  orchestrator @ 87a8d02, ADD-008 — file and message agree
```
