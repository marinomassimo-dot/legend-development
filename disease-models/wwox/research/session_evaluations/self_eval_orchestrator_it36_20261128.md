# Self-evaluation, capability scout and takeaways, IT Orchestrator window IT36 (b095e80e), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. **Written by the successor window IT37 (c1c43605)
from IT36's record** (checkpoint 36 `CHECKPOINT_IT_20261128_10.md`, `RESULT_ADV330_IT_20261128.md`,
`COMPARE_ADV331_HE_IT_20261128.md`, the landed commits `037f8d556` and `44654d981`), not by the window it grades:
friction that IT36 did not write down is not seen.

## Scope and executable verdict
- Work: IT35's self-evaluation written (`bb2f57fa5`); ADV-328 dated pointers from live copies of the old line-23
  sentence (`080146f2f`, landed with `037f8d556`); ADV-330 (P47T knock-in blood chemistry) frozen, read, repaired and
  landed (`44654d981`); HE's blind table ADV-331 compared cell by cell; checkpoint 36.
- Run by IT37 on `de64d685a`: `session_self_eval.py` PASS (declared gaps are old PMIDs); receipts chain OK (3921);
  `growth_anchors.py check` PASS.
- CI read by IT37: run 2907 (`6794836c8`) success; runs 2909, 2912, 2914, 2918 and 2925 still in progress at that read.
- Measured cost (`session_model_census.py`, read by IT37): 96 turns, peak context 240,344, one context drop, effort
  high on every counted turn. The checkpoint's 221,143 was the peak at the time of writing.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Source depth | Supplementary Tables 2 and 3 of PMID 36828035 and the Methods and Results text read from held bytes; the PREREG frozen before the tables; the second reader read the sources before judging. | strong |
| Independent check | HE's blind table, compared after it reached main: 42 of 42 items agree. | strong |
| First composition | ADV-330: 3 of 50 clauses MUST CHANGE (6 percent); re-read of repaired clauses 1 of 27. ADV-328 pointers: 5 of 46, 3 of 56, 1 of 53 across three rounds. Last repairs were applied without a further read. | partial |
| Claim separation | "Neither E1 nor E2" kept under the frozen informativeness rule; the stage mismatch (mean survival 393 d for the homozygote) is stated as an inference, not a printed draw age. | strong |
| Prior-art status | Two ADV-074 notes said held supplements were not held; dated corrections landed with the result. | repaired |
| Where results landed | RP-019 line (ADV's row); six pointers from copies of the old line-23 sentence. | strong |
| Friction | A response was stopped by the safety classifier while reading a claim-registry record; recorded, not retried, not passed to a peer for the same action. | recorded |

## Clauses re-read after IT36 closed
A fresh reader (sonnet 5.5, effort high stated) judged, on IT37's brief, the clauses checkpoint 36 listed as not re-read
(the last four ADV-330 repairs, its stage sentence, and the ADV-328 pointer clauses P1-2 and P1-3), against the held
sources: **26 clause parts, 2 MUST CHANGE (8 percent), 6 ADD, 18 OK.** Both MUST CHANGE were checked at the source by
IT37 before repair: the stage sentence said "P14 to P18" for a blood chemistry held at P18 only (CLAIM 036), and
"denominator undefined" was false for Fig 2G of PMID 34747138 (legend: percentage of neurons showing the transgene);
the same wording stood in line 23 of `meta_gaba_paradox_current.md` and was repaired there. A re-read of the repairs:
11 items, 8 OK, 3 ADD, 0 MUST CHANGE. The two ADV-328 clauses recorded as "quoted from line 23, fine" were therefore
not fine: a copied sentence is as wrong as its original. IT37 then found two more live copies of the P14 to P18 chemistry stage that IT36's six pointers had not covered (`metabolic_differential_vulnerability_reposed_20260922.md`, `earliest_lesion_developmental_timeline_20260921.md`) and added dated pointers; a third read of those pointers returned 4 OK, 3 ADD per paragraph (row named, white-cell count has no age, glucose day by panel), 0 MUST CHANGE, applied to the pointers, line 23 and the copies, and not re-read. Line 422 of `peripheral_phenotype_denominator_audit_20260922.md` proposes a blood gas at P14 to P18 on new animals: a design, not a statement of what is held, left unchanged. A "not re-read" repair is a debt, not a result.

## Dream pass
Material change: a "not significant" panel with no draw age and no fasting state supports neither the presence nor the
absence of a derangement, and the cohort's survival can make the comparison one between life stages. Both are in the
result and in checkpoint 36; no new claim, no new rule.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| A pointer wording is a first composition, and each repair adds new text to check | ADV-328: three rounds, errors in each | CHANGE = NONE: quote the old sentence, then narrow (checkpoint 36 rule) |
| Delegates cannot write report files | reports exist only as replies | CHANGE = NONE (same decision as IT33 to IT35) |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| P47T homozygote serum panel (n = 16 header, mouse): a null-sized BUN rise is excluded and a null-sized glucose fall marginally excluded, at an unstated draw age | Total CO2 and pH not tabulated; age at draw and fasting not stated; half-sized glucose fall not excluded | The missing observation is registered; RP-019 is ADV's row |
| Blood chemistry of the systemic null is held at P18 only | Does not separate a cell-autonomous change from one secondary to seizures and growth failure | none owed by IT |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 4
machine: 1   blind_auditor: 3   peer: 0   self: 0
severity_high: 0   of which self: 0
undetected_known: 0
```
Blind auditor: the first-composition errors of ADV-330, its re-read finding and the ADV-328 pointer rounds, counted
once per class. Machine: the classifier stop. "Undetected" is bounded by the record IT37 read.

## Section 21c output
- `DEFAULTS_TAKEN` (from the record): the last repairs applied without a further read, named in the result; the BUN
  reading kept as a labelled judgement.
- `STOP_LOG`: one classifier stop (claim-registry record); not retried.
