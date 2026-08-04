# Axis 3 — second blind review, and what it says about the first

> **Non-canonical.** A second independent human judgement on the corrected set, run to test
> the first one rather than to confirm it. It changes no canonical file.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Reviewer:** fresh session, no repository access, new seed (`20260805`)
**Prompt:** [`dismech_axis3_blind_reviewer_prompt_round2.md`](dismech_axis3_blind_reviewer_prompt_round2.md)
**Scope:** 11 anchors · 40 propositions · 3 anchors repaired between rounds, 8 untouched

---

## The result that matters, and it is not the headline

Overall correspondence rose from 20/37 to **27/40 (68 %)**. That number should be ignored:
three anchors were edited using round 1's diagnosis, so agreement there was arranged.

**The eight untouched anchors are the measurement**, and they say the human step is less
reliable than the first round made it look.

| Comparison | Agreement |
|---|---:|
| Exact verdict, per anchor and side | **8 / 16 (50 %)** |
| Collapsing `SUBSUMES` into `DIFFERENT`, round 1's vocabulary | 10 / 16 (62 %) |
| Correspondence yes/no — the level a decision actually rests on | **11 / 16 (68 %)** |

Two independent readers, the same unchanged pairs, agree on whether two propositions
correspond **about two times in three**. That is not nothing, and it is not a measurement
anyone should build a contract on without saying so.

**Some of the gap is my defect, not theirs.** Round 1 had no `SUBSUMES`, so containments were
forced into `DIFFERENT`; supplying the missing value recovers 2 of the 8 disagreements. The
remaining five are genuine differences of reading.

### Where two competent readers genuinely disagreed

| Anchor | Round 1 | Round 2 |
|---|---|---|
| 9 — *"detectable between endogenous proteins in mouse brain"* vs *"reciprocally co-immunoprecipitate from mouse brain extract"* | `SAME` both sides | `SUBSUMED` / `SUBSUMES` |
| 2 — the de-repression reading | `SUBSUMED` | `DIFFERENT` |
| 7 — residue requirement vs motif homology | `SUBSUMED` ×2 + `DIFFERENT` | `SPLIT` ×2 + `SUBSUMED` |
| 11 — epistasis and the linear-pathway reading | `SPLIT` | `DIFFERENT` |

Anchor 9 is the clean case: is a specific method the same assertion as the general fact it
demonstrates, or does it contain it? Both answers are defensible. **That is the ambiguity, and
no amount of instrument design removes it** — it is a question about what an assertion is,
and it will recur at every anchor where one reader states a result and the other states how
it was obtained.

## Independent confirmation, again

The reviewer recorded split agreement at **9 of 11**. The mechanical count after the repair
was **9 of 11**, on the same anchors. Round 1 recorded 7 of 11 against a mechanical 7 of 11.
Two rounds, two blind reviewers, two exact matches with a computation neither saw.

**The split metric is reliable; the semantic verdict is not.** That asymmetry is the most
useful thing either round produced, and it points at what to trust: granularity can be
measured, equivalence must be judged.

---

## Did the repair work?

Partly, and round 2 found what round 1 could not.

**Anchor 8 — the main repair.** Split now agrees, 3 versus 3. But the verdicts are
`SUBSUMED`, `SUBSUMED`, `DIFFERENT` — not `SAME`. The reference propositions are contained in
the independent ones, which additionally attribute the phosphorylation to GSK3β and name the
L404A control. **The granularity was fixed; the precision was not.** Two of the three repaired
propositions say less than the source supports.

**Anchor 5.** Split agrees now, 2 versus 2, where it did not before. But `α7`/`β7` came back
`DIFFERENT`, with a reason that is a finding against my wording:

> *"'Requires a short engineered linker' is stronger than [the] observation that the largest
> contribution occurred with such peptides."*

The source says the interaction *grew stronger* with a shorter linker. **I wrote "requires",
which is a modal claim the source does not make.** Round 1 never saw this, because the
proposition it judged was a fused two-clause statement in which the overstatement was buried.
Splitting it exposed the error — the repair was worth doing for a reason other than the one it
was done for.

**Anchor 10.** Moved from `DIFFERENT` in round 1 to `SUBSUMED`/`SUBSUMES`. The restatement was
correct; the reference version is simply less complete than the independent one, which names
the differentiation context.

**Anchor 16 / the differentiation wording.** `α16` vs `β16` came back `DIFFERENT`: *retinoic-
acid-induced differentiation* against *RA-induced neurite outgrowth*. The source measures
differentiation by scoring neurite outgrowth, so this may be over-strict — but it is exactly
the kind of call a human step exists to make, and it is recorded rather than resolved here.

---

## What this changes

1. **The 9-of-11 split improvement is real** and independently confirmed. The atomization
   repair was correct as a repair.
2. **Two of the three repaired propositions are under-specified**, and one overstates its
   source. The repair fixed how many assertions there are, not how well each is stated.
3. **The human step has ~68 % inter-rater agreement on correspondence.** Any future claim
   resting on a single reviewer's verdict must carry that number with it.
4. **Round 1's conclusions stand, with one correction**: its ten `SAME` verdicts included at
   least one — anchor 9 — that a second reader read as a containment. The claim *"axis 3
   measures wording, not meaning"* survives; the specific count does not.

## What must not be concluded

That agreement rose. It rose because three anchors were edited toward the other side. Every
number in this document that matters is computed on the eight anchors nobody touched.

## Next

1. Repair the precision, not just the granularity: `α14`, `α15` need the GSK3β attribution
   and the L404A control they omit, and `β7` must drop *"requires"* for what the source says.
   All three have locators already extracted.
2. A third round is not worth running. Two rounds establish that the split metric is
   reproducible and the semantic verdict is roughly two-thirds reproducible; a third would
   refine an estimate rather than answer a question.
3. Axis 4 can now run — a correspondence set exists in both rounds — but only over pairs
   both reviewers agreed on, which is a small and openly biased universe.

## Raw reply

[`data/dismech_axis3_review_raw_reply_round2.md`](data/), verbatim.

## Related

[`dismech_axis3_review_result.md`](dismech_axis3_review_result.md) (round 1) · [`dismech_independent_comparison_rev13.md`](dismech_independent_comparison_rev13.md) · [`dismech_independent_derivation_design.md`](dismech_independent_derivation_design.md)
