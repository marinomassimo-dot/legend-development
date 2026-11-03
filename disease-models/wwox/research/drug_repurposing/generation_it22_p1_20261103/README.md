# IT22: from unused knowledge to better generation (2026-11-03)

Non-canonical. Not medical advice. Actor `orchestrator` (producer), independent reverse analysis and qualification by separate agents. Baseline: `main` = `d6de0a5a`.
Every proposal stays conditional; nothing in this package is qualified. Counts carry their unit (ROW, FAMILY, COMPOUND, CLUSTER, HAND-OVER; see `measure_it22.py`).

## 1. What was wrong and what was fixed

| Defect | Reproduced case | Minimal fix | Test |
|---|---|---|---|
| Decision transfer (rule H8): one member's decision vetoed every member of its cluster | nanatinostat rejected for its own potency profile; pracinostat, CUDC-101, quisinostat held "examined earlier" | scope table `decision_scope_it22.tsv` + `decision_effect()` in `run_generation_it21.py` | `test_decision_scope_it22.py` (10) |
| Pharmacology compared across unlike measures | fedratinib Kd v IC50, colchicine Kd v IC50, umbralisib EC50 v IC50; synthetic EC50 v Ki gave WEAK and `mixed_measure=no` (reproduced on the old code) | typed measures, same-type ratio only, `NOT_COMPARABLE_MEASURES`, secondary-activity tier | `test_attribution_it21.py` (45) |
| Knowledge present but not consumed | NFE2L2/NQO1/HMOX1 in no seed table; failed second-system control attached to nothing; cell-type marker set one ortholog-table edit from becoming a seed | `build_inputs_it22.py`, Q8, seed guards and annotations consumed into proposal limits and hand-over order, incremental engine runs | `test_inputs_it22.py` (7) |

## 2. Measured, stage by stage ([`measures_it22.json`](measures_it22.json))

| Stage | rows | clusters | eligible rows | hand-overs |
|---|---:|---:|---:|---:|
| IT21 as published | 980 | 150 | 154 | 11 |
| + P1 scoped decisions | 980 | 150 | 199 | 14 |
| + P2 typed pharmacology | 980 | 150 | 212 | 14 |
| + P3 inputs | 1,000 | 154 | 217 | 16 |
| + reverse-test fixes | 1,000 | 154 | 217 | 16 |

P1 and P2 changed **selection and eligibility, not generation** (the 980 rows are the same rows); only the new input changed generation (20 new rows, one new question). P1 released 45 of 69 blocked rows (24 stay
closed on a refuted premise); P2 moved 20 weak-attribution blocks to 4 and 38 attribution states. Sensitivity: weak-attribution rows at stage S2 if the secondary band ended at 300 / 1,000 / 3,000 nM: 13 / 6 / 6.
Dependence on the failed second system: without the rows resting on the shWWOX hNPC library, Q2 keeps 0 of 8 placed seed rows, Q3 keeps 1 of 6, Q8 0 of 1; Q4 to Q7 are unaffected (engine re-run of that arm: `eng_arm`).

## 3. Executed, reasoned, observed

Executed by code: the three corrections, the amended inputs, 4 incremental engine runs (Q8 new; Q4 control numerically identical, only the guard column differs; Q2/Q3 hNPC arm), the stage tables.
Agent reasoning (not engine steps): the seed-row proposals of the four input audits, the dossiers' mechanism arguments, the TR-alpha isoform argument. Observed: nothing prospective; no hypothesis is qualified.

## 4. Limits

`SECONDARY_MAIN_NM` (1,000 nM) and the 10x rule are stated conventions. The chain edges of the new Q8 rows are context-free network edges. Assay class is unknown for most catalogue values. Pracinostat's HDAC5 value is 47 nM in the
Guide to Pharmacology and 5,113 nM in one ChEMBL document (109-fold apart): attribution is undecidable until the sources are reconciled. Reverse-test fixes not yet applied: class-limit scope (G2), phase and route from the catalogue beyond ATC (G4).
