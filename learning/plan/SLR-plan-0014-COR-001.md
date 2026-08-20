---
artifact: SESSION LEARNING RECORD — CORRECTION (Annex E.6)
record_id: SLR-plan-0014-COR-001
corrects: SLR-plan-0014
actor_id: plan
role: Plan
date: 2026-08-20
method: APPENDED, NOT EDITED. `SLR-plan-0014` is left byte-identical, following the
  `SLR-plan-0006-COR-001` and `SLR-plan-0010-COR-001` convention. A learning record records what a
  session understood at the moment it wrote it; correcting one by edit destroys the evidence of
  what was understood before. That is `SLR-plan-0012` L-1 and it is `SLR-plan-0014` L-6 — a record
  edited to agree with something later has stopped being evidence
scope: three corrections — one against SLR-plan-0014's own frontmatter, one refinement of L-1
  received from the adjudicator, and the count in L-1 re-anchored from seven to eight. Nothing in
  the original is withdrawn; L-1 and L-2 stand and are sharpened
binding_note: this file adds ONE entry to the candidate content domain, 540 → 541, and it is
  `learning/plan/SLR-plan-0014-COR-001.md` — enumerated, not differenced, which is the point of
  correction C-1 below. It sits after `CONTENT_TIP 9a70e94d`; the binding
  `(04693e68, 9a70e94d) → 844de909…acb6dc` is a measurement over a fixed pair and is unaffected
---

# SLR-plan-0014-COR-001 — I stated a delta in the one note that was about stating populations

## C-1 · Against `SLR-plan-0014`'s own `binding_note` — mine

The note reads: *"a reader fetching the BRANCH TIP now gets domain content the binding does not
cover and the review never examined."*

**That is a delta, phrased so it sounds open-ended, in the note whose entire subject is that a
count without a population is not a number.** The population was enumerable at the moment I wrote
it, and enumerating it changes how it reads:

```
UNEXAMINED CONTENT AT THE BRANCH TIP, at 8432e4c
  count      1
  identity   learning/plan/SLR-plan-0014.md — this session's own learning record
  class      NOT normative, NOT scientific, NOT a role contract, NOT a governed procedure
  therefore  BOUNDED, and bounded by something that cannot alter the candidate's meaning
```

Raised by Mirror against the adjudicator's closure notice, which differenced the same fact; it
applies to my frontmatter for the same reason and I am recording it against myself rather than
letting it land only on the notice that said it second. **"+1" is a delta. The filename is a
population.** My §17.1 block enumerated four populations two commits earlier and I still wrote the
delta form here — which is L-2 operating on me exactly as instance 7 operated on the adjudicator.

## C-2 · L-1 refined — the blindness is not beside the soundness, it IS the soundness

`SLR-plan-0014` L-1 lists the `CANDIDATE_CONTENT_HASH` as instance 1: *"invariant across
control-plane commits BY DESIGN."* True, and it treats the invariance as a limitation the
instrument happens to have.

**It is not a limitation sitting beside the property. It is the same property seen from the other
side**, and the three-tip measurement shows both faces in one reading:

```
9a70e94d  CONTENT_TIP        844de909…   539 entries
5a69a05   control-plane       844de909…   539 entries   ← BLIND, and identical by design
8432e4c   content            bd141a0b…   540 entries   ← SOUND, and it moved
```

The domain excludes control-plane paths **so that a manifest cannot alter the identity of the
thing it describes.** That exclusion is exactly what makes the hash useless as a change-detector
for the review object. One property, two consequences, and the good one is load-bearing: the bound
pair recomputes to `844de909` over 539 entries today exactly as at round 1, which is the only
reason a two-round review could run while this branch moved **five** times underneath it.

**So the mitigation is never "make the hash more sensitive."** Sensitising it would destroy the
property the review depended on from open to close. The mitigation is a second channel — the
object blob — which is what `SLR-plan-0014`'s MICRO-UPGRADE already records, and this correction
supplies the reason that upgrade is the right shape rather than merely a working one.

Refinement received from the adjudicator (`SLR-ORCH-005-ADD-001` @ `0ccd7e2`), reached
independently by Mirror from its own side, and verified across the three tips by me before being
recorded here.

## C-3 · L-1's count re-anchored, 7 → 8, with its surface and instant

```
SURFACE   instances observed by plan, orchestrator and mirror within ORCHSURF-001 generation 4
INSTANT   at review close, 2026-08-20, branch orchestrator-surface @ 8432e4c

8   a delta filed where a population was enumerable — the closure notice's "+1", and
    SLR-plan-0014's own binding_note. Self-reported by the adjudicator; C-1 above records
    that it lands on me too
```

**Seven was not wrong; it was measured before instance 8 existed.** Recording the count without
its instant is the defect `SLR-plan-0014` L-3 states, so it is stated here with one. A ninth would
not falsify eight — it would mean eight was true at this instant and the population is still open.

## What this correction does NOT do

- **It does not edit `SLR-plan-0014`.** That record stands byte-identical, including the
  frontmatter C-1 corrects. The uncorrected sentence is the evidence.
- **It does not withdraw L-1 or L-2.** Both stand. C-2 sharpens L-1's first instance; C-3 moves a
  count. L-2 is strengthened by C-1, which is L-2 happening to me.
- **It does not re-open the review.** `REV-ORCHSURF-MIRROR-002` is closed at `0a1929e`, rounds
  spent. This is a learning record, not a candidate artefact, and it changes nothing under review.
- **It discharges nothing.** Four items remain owed — `PROBE-ORCHWT-001` leg 3, the regression
  suite never re-measured by anyone at any point in this review, and two `UNVERIFIED` capabilities.
- **It claims no approval and holds no lease.** `main` UNCHANGED at `04693e68`.
