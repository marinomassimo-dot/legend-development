# CC-20261019-SCIENTIST-A-LIPID-05 — sterol review (PMID 42454491) and a caution for the statin seed

`context_policy: QUESTION_DRIVEN`. **Author:** ACTOR_ID `scientist-a`, metabolic batch G1, 2026-10-19, task `METAB-G1-A-20261019`.
**Status:** `PROPOSED — NOT PROPAGATED`. **Change class: MINOR** (a caution line on a research-layer lead plus an identity record). `target_wm_version`: next MINOR after the integrator's current value.
**Nothing here is medical advice.** Numbering is provisional.

## 1 · Landings

| # | Source | Receipt (staged) | Landing proposed |
|---|---|---|---|
| 1 | PMID 42454491 (Peeples 2026, J Clin Invest, review: sterol biosynthesis, brain development and disease) | `FTR-20261019-42454491-01` | New `PAPER` record (none exists), review, T3, relevance LOW (WWOX absent); caution line on `DL-THER-080` (section 3) |

## 2 · Record content

What it is: a narrative review; WWOX zero occurrences. Premise: after the blood-brain barrier forms the brain depends on its own sterol synthesis; myelin growth needs very high cholesterol; statins and several psychotropic and cardiovascular drugs inhibit the pathway; inborn errors of the pathway present with callosal hypoplasia and, for two of nine, seizures.

Note text to carry:
🔴 **A framing and safety-screen source, not WWOX evidence.** It supports nothing and refutes nothing about a WWOX sterol defect. Peripheral lipid associations (plasma HDL, triglycerides) cannot speak to brain sterol on the review's own premise. The epidemiological headline (hazard ratio 1.47, and 2.33 for four or more inhibitors) is the authors' separate database study cited as in press, without a confounding-by-indication discussion in the review.

## 3 · Op list for `discovery_ledger_current.md` (record-scoped; dry run executed at this branch's base, nothing written)

```json
[
 {
  "op": "replace-within",
  "id": "DL-THER-080",
  "old": "nessuna delle due condizioni è soddisfatta.",
  "new": "nessuna delle due condizioni è soddisfatta. 🔴 **Caution attached by `CC-20261019-SCIENTIST-A-LIPID-05` (source: PMID 42454491, a 2026 narrative review, read in full, WWOX absent):** statins are named there as sterol-biosynthesis-inhibiting medications, and the review states that after the blood-brain barrier forms the developing brain depends almost entirely on its own sterol synthesis and that cholesterol is needed for myelin growth. Any CNS-directed or paediatric reading of this seed therefore carries a developing-brain sterol question that the source (an osteosarcoma bone paper) never raises; it belongs in the BLOCK-1 screen if the seed is ever promoted. IPOTESI; the review's own epidemiological association rests on its authors' separate database study and is not evidence about statins in any WWOX setting. Not medical advice."
 }
]
```

Dry run: `scope 'DL-THER-080': span 468933→470539`, `DRY RUN — nothing written; 1 op(s)`. The `old` string occurs once in the record. Status, tag and the existing three limits are unchanged.

## 4 · Method note proposed for RL-003 (no claim change)

If brain sterol is ever measured in Wwox-null or P47T brain: a post-lanosterol profile (cholesterol, desmosterol, lathosterol, 7-dehydrocholesterol, lanosterol) by GC- or LC-MS, as the review names; plasma cholesterol is not a proxy. IPOTESI; no such measurement exists in the repository.

## 5 · What must NOT be written

- No statement that WWOX loss alters brain cholesterol or sterol intermediates.
- No medication recommendation or statement about statins in any person; the caution is a screening prompt for a discovery seed.
- No individual-level content.

## 6 · Registry statements to re-check at integration

`DL-THER-080` text (caution only). Nothing else touched.

### LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. The brain depends on intrinsic sterol synthesis | Once the blood-brain barrier forms, isolating the CNS from circulating lipoprotein-bound cholesterol, the embryonic and postnatal brain depends almost entirely on intrinsic sterol synthesis (3, 36). | Section: Cholesterol and the developing brain, `files/fulltext/PMID42454491_Peeples2026_PMC.xml`
2. Statins and other drugs are named as inhibitors | This second group includes medications such as aripiprazole, trazodone, amiodarone, cariprazine, buspirone, haloperidol, nebivolol, propranolol, and other compounds (39, 85–93). | Section: Sterol biosynthesis-inhibiting side effects, same
3. The cumulative-burden idea is a hypothesis | Because polypharmacy is common in psychiatry, neurology, and pain management, we hypothesize that cumulative SBIM burden may exceed the threshold for physiologic compensation in the developing fetus. | same section
4. Not all exposed pregnancies lead to the outcome | Not all pregnancies prescribed SBIMs resulted in a child with ASD, and it is not yet clear which factors may exacerbate the sterol-inhibiting effects (or side effects) of these medications. | Conclusions and future directions, same
