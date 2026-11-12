# IT46 P1: how much of the IT45 generation was executable

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI as in the sources.

Question: for the two IT45 cases carried end to end (S10 KEAP1/NRF2 and S3 Kv7), which step of *observation → need → relations → context → actions → compounds → comparison → experiment → open question* was produced by code, by a reader, by the agent's scientific decision, by hand into a table, or exists only in a narrative written after the result?

Provenance classes: **CODE** (a script or a table reader produced it from held inputs, and re-running reproduces it); **READER** (an independent delegate read a primary document); **DECISION** (the agent's scientific judgement, legitimate, recorded in a file); **MANUAL** (typed by hand into a shared table, no script, no test); **NARRATIVE** (present only in prose written after the result; no table or consumer carries it).

## S10 (KEAP1/NRF2), files under `generation_it45_20261111/s10_dose/`

| Step | Source of the step | Class |
|---|---|---|
| Observation (redox transcript signature; no NRF2 measurement in a WWOX neural system) | package `nrf2_inv08_20261107`, IT43 frame | CODE (carried by the package reader) |
| Need | `needs.json` link of INV-08 | CODE |
| Relations (KEAP1, NFE2L2 targets; wanted action) | `generation_it43_20261110/s10/relations.tsv` written in IT43 | DECISION (frame written before names), then CODE (read by the activity path) |
| Context (human cell line, no neuron or astrocyte) | read off the activity rows by hand into `result_it45.md` | NARRATIVE (the activity rows carry assay descriptions; nothing derives a context table from them) |
| Actions (compounds with a dose-response row) | `activity_search.py` (dose-response types, 1,587 rows, 10 catalogue-status molecules) | CODE |
| Compound identity and role | `entity_roles.py`, catalogue status | CODE |
| Pointer selection (rule fixed before reading) | `selection_it45.md` | DECISION |
| Document reading, 8 corrections | `verify_s10/VERDICTS.md` | READER |
| Comparison (same NRF2-dependent readout, not binding potency; limit rows are not measurements) | `result_it45.md`; the limit-row rule exists in the engine, the readout-class rule does not | DECISION + NARRATIVE (the readout-class rule is prose only) |
| Experiment (genetic arm first, knockdown control, target-gene set) | clause typed into INV-08 `next_test` | MANUAL |
| Open question | row IT45-Q03 typed into `open_questions_map.tsv` | MANUAL |

## S3-Kv7 (the lever case), files `p3_lever_it45.md`, `p4_filters_it45.md`

| Step | Source of the step | Class |
|---|---|---|
| Observation (depolarised rest, sag, resistance, bursts by gene dose) | INV-18 card, from package 34634460 | CODE (carried) |
| Need | NEED-INTRINSIC-EXCITABILITY | CODE |
| Relations (R1-R5 discriminating results; alternative lever "adds a conductance without knowing the cause") | `p3_lever_it45.md` section 1 | DECISION |
| Context: which cell class carries the channel | the agent opened `kchan_expression_mouse.tsv` and typed a six-row table | **NARRATIVE** (the join of a relation's target symbols to a cell-class expression table is not a script and has no consumer) |
| Attributability of each discriminating result to neurons | prose sentence "R1 needs a neuron-specific control, R2 and R5 less" | **NARRATIVE** |
| Actions / compounds (7 catalogue-status molecules, 4 only by activity) | `activity_search.py`, `pointers_it44.tsv` | CODE |
| Comparison (opener against an equal current-injection hyperpolarisation) | `p3_lever_it45.md` R5 | DECISION; its validity is audited in P4 |
| Experiment | INV-18 clause typed by hand | MANUAL |
| Open question | IT45-Q01 typed by hand | MANUAL |

Count (steps that exist in a file, per class): S10 = 3 CODE, 1 READER, 3 DECISION, 2 MANUAL, 2 NARRATIVE; Kv7 = 3 CODE, 3 DECISION, 2 MANUAL, 2 NARRATIVE. The two steps that recur as NARRATIVE in both cases, and that no consumer carries, are **context** and **the readout class of a comparison**.

## Which step to make operational

Candidates and what each would let a later case do without the session's memory:

| Candidate | Value | Executable now? |
|---|---|---|
| Join a relation's target symbols to a held cell-class expression table, with the verdict "a difference attributable to a neuron here / needs a cell-specific control / no information" | Context and attributability appear for any relation whose genes are in a held table, in the same table the generator already writes (`conditional_proposals`), and unknown genes stay unknown | yes: the inputs are two held TSVs; a consumer exists |
| Readout class of a comparison (binding vs function dependent on the target; limit rows) | high, but needs assay-description parsing across ChEMBL rows and the engine's condition vocabulary (HE46's domain) | not as a small script; hand to HE46 as a failing case |
| Distinguish cause correction from compensation | high, but depends on per-hypothesis biology, not on a table | no table to read |

Choice: the **cell-context join**. It is the smallest piece, the inputs are held, a consumer (`conditional_proposals.py`, which also feeds the reader view) can read it, and it can fail visibly on a new case (genes absent from every held table). The readout-class rule goes to Harness (HE46) with the S10 case as its failing example.
