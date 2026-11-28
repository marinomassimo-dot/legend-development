# Self-evaluation, capability scout and takeaways, IT Orchestrator window IT35 (1c914d1b), 2026-11-28

Public, disease-level, de-identified; nothing here is medical advice. **Written by the successor window IT36 (b095e80e)
from IT35's record** (checkpoint 35, `RESULT_ADV328_IT_20261128.md`, the landed commits `80f76390f` and `6794836c8`),
not by the window it grades and not from its transcript: friction that IT35 did not write down is not seen.

## Scope and executable verdict
- Work: INV-06 Crawford sentence applied (both TSVs, ranking, titles, view trio, i18n collect; `80f76390f`);
  ADV-325 GSK3 census judged as second reader (no register or working-model edit); a dream pass (population marker
  against functional phenotype); ADV-328 (metabolic confound and conditional alleles) closed and landed (`6794836c8`,
  line 23 of `meta_gaba_paradox_current.md` reworded); the IT34 self-evaluation landed in the same push.
- Run by IT36 on `599e71244`: `session_self_eval.py` PASS (declared gaps are old PMIDs, none from this window);
  receipts chain OK (3905); `growth_anchors.py check` PASS. CI of the landing commits was still in progress when this was
  written (14 runs open, oldest 45 minutes); run 291 of the shareable-view publication failed in its `deploy` job
  (the Pages deploy action) and the next publication, 292, succeeded.

## Diagnosis
| Dimension | Answer with anchor | Grade |
|---|---|---|
| Source depth | Repudi 2021 Brain and EMBO Mol Med read by a delegate (sonnet 5.5, effort HIGH stated) before the notes file; the EMBO Appendix S1C and D glucose plot read from the supplement that had been held since 2026-10-19. | strong |
| First composition | Round 2 on the composed clauses: 3 of 15 MUST CHANGE (20 percent; Brain 1 of 7, EMBO 2 of 8). Round 3 on the repaired clauses: 3 of 11 (27 percent; Brain 2 of 6, EMBO 1 of 5): the repairs carried new errors. The last repair (E7, the delegate's own wording) was not re-read. | partial |
| Claim separation | "Acidotic" narrowed to reduced total CO2 at P18; "leukopenic" rests on two animals per group; glucose record from day 10 (plot reading, one pooled line); a bulk transcript was not counted as a marker read and both readings were reported because the frozen rule did not say. | strong |
| First reading of a table | File013 was first taken for a systemic-null table; the blind read showed three pooled knockout lines (7 against 7). The comparison with HE's ADV-329 table (identical RNA-seq cells) kept File013 as "not stated". | partial |
| Where results landed | Line 23 of the GABA-paradox meta page; the INV-06 sentence in both tables and the view. Dated pointers from the live copies of the old line-23 sentence are **not yet written** (checkpoint item 2, open at IT36). | partial |
| Friction | Context was stated as 215k to a peer without measuring; the measured peak was 330k (`session_model_census.py`). One claim, "the suite is not in the gate", was wrong: the workflow calls `run_release_regressions.py`. | partial |

## Dream pass
Material change: a first reading of a supplementary table can be wrong in its unit (pooled lines taken for a systemic
null), and a repair of a flagged clause is itself a first composition (3 of 11 again). Both are already in checkpoint
35's rules and in memory `it35-pitfalls`; no new claim.

## Capability scout
| Gap | Evidence | Decision |
|---|---|---|
| A frozen rule that does not say whether a bulk transcript counts as a marker read | ADV-328 round 3: both readings reported, none picked | CHANGE = NONE: fix the wording in the next PREREG that touches transcript against protein markers |
| Delegates cannot write report files, so only non-OK rows are reproduced | the README of the previous windows states it | CHANGE = NONE (same decision as IT33 and IT34) |

## Takeaways
| What | Lead or limit | Next |
|---|---|---|
| Blood chemistry of the systemic Wwox-null mouse is held at P18 only; glucose from day 10; the conditional-allele marker response is transcript-level only | A cell-restricted deletion does not separate a cell-autonomous marker change from one secondary to seizures and growth failure; nobody has measured glucose in the same animals before P9 | RP-019 design requirement is ADV's row |
| INV-06 Crawford sentence applied | The N2 intervals correspond to about 40 percent of the single-pulse response | none owed |
| Dated pointers from copies of the old line-23 sentence | Four analysis files and two dossiers carry it | IT36, narrow edit with a second reader |

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 4
machine: 0   blind_auditor: 3   peer: 0   self: 1
severity_high: 0   of which self: 0
undetected_known: 0
```
Blind auditor: B6, E4/E7 (round 2) and the three round-3 repairs counted once as one finding class. Self: the unmeasured
context figure sent to ADV. "Undetected" is bounded by the record IT36 read.

## Section 21c output
- `DEFAULTS_TAKEN` (from the record): the E7 repair kept as the delegate's wording without a re-read; named in the result.
- `STOP_LOG`: none recorded.
