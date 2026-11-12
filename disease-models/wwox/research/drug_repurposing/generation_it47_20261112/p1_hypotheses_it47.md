# IT47 P1: the generator consumes the hypotheses HE46 made reachable

Non-canonical working note. Not medical advice; no dose, schedule or route. Reference genotype class only. IPOTESI throughout; a package row is a hypothesis someone wrote, not an approval.

## The limit, checked on the tree
HE46 (README section 3) registered three packages of INV-18 and one of INV-08 as `hypotheses_only` (own layouts), reachable through `hypothesis_package.hypotheses_for`. IT46 did not close the step: `generation_it40_20261109/conditional_proposals.py` read only `record_for`. Checked on main cff57777: 19 rows reachable (13 for INV-18, 6 for INV-08), **0 used**.

## What was done (in the existing path)
`conditional_proposals.py` now also calls `hypotheses_for(INV-18)` and `hypotheses_for(INV-08)` and maps the rows of two packages of different structure, cell by cell, onto the seven things a conditional proposal keeps (`PKG_MAP`, reviewable in the file). Output: `conditional_proposals_packages_it47.tsv` (11 rows). The loader maps nothing; the meaning is decided here.
| Slot of the proposal | `ph_k2p_sci45` (INV-18, KP1-KP5; columns initial_observation, mechanistic_relation, context, action, compound_or_class, ...) | `nrf2_inv08` (INV-08, H1-H6; columns hypothesis, what_supports, what_refutes, what_separates, status, transfer_note) |
|---|---|---|
| observation and source | initial_observation + file:line | what_supports + file:line (an observation list that includes the package's own audit notes) |
| proposed relation | mechanistic_relation | hypothesis |
| biological and experimental context | context | transfer_note |
| pharmacological action | action; compounds kept apart (compound_or_class), named not ranked | **no cell**: taken from relation S10 and labelled "not stated by the package" |
| unresolved premise | counter_evidence (what is unmeasured) | status + what_refutes |
| competing explanations | the other rows of the same package, by id | the other rows (H1..H6 are exactly the rivals) |
| discriminating measure | experiment_that_rejects_it | what_separates |
| expected result | possible_functional_outcome | what_supports |
Added fields: `package_ref` (row id and file:line), `direction_stated` (always "none": neither package states a therapeutic direction), `unmapped_cells` (cells of the package the mapping does not use), `package_title`, and the cell-class context of the channels or genes involved (`cell_context`, IT46). A premise that is unresolved becomes the proposal's stated premise and its measure; nothing is promoted to a direction. Two further packages (SCI43 K-branch KH1-KH5, HCN HY1-HY3) are reachable and **not mapped**: the run reports them (8 rows) instead of silently ignoring them.

## Before and after (run: `python3 generation_it40_20261109/conditional_proposals.py`)
| | before | after |
|---|---|---|
| hypothesis rows read from hypotheses_only packages | 0 of 19 | 11 of 19 (8 reported as reachable and unmapped) |
| output rows | 6 (INV-05, INV-18; record_for) | 6 + 11 (INV-18 5, INV-08 6) |
| INV-08 conditional proposals | 0 | 6 |
| context for the K2P proposals | none | KCNK2 (TREK-1) shared between neurons and other classes in both tables; KCNK3 shared in mouse, not detected in the human sample; KCNK9 neuron-enriched in mouse: an effect attributed to the first two cannot be assigned to neurons without a cell-specific control |
| context for the NRF2 proposals | none | KEAP1 mouse shared, human enriched elsewhere; NFE2L2 enriched elsewhere in both: neuron-attributable readouts need a cell-specific control |
| action for the NRF2 rows | none | taken from relation S10 and labelled as not the package's |
| dashboard consumer | 6 conditional hypotheses (INV-05, INV-18) | + KP1 (INV-18) and NRF2-H1, NRF2-H2 (INV-08) in the reader table that the page renders under each investigation (`generation_it40_20261109/reader_view.tsv`, built by `build_reader_rows.py`; no compound name in the text) |
The final consumers are the conditional-proposal table (generation) and the investigation cards (dashboard).

## Boundary with Harness
Harness owns the generic reader (`hypothesis_package.py`: layouts, keys, states); this step owns which cell answers which question and the link in the generator. No change was made to `framework/scripts/hypothesis_package.py`.

## Limits
The mapping is a judgement per package, not derived; `what_supports` is used as the observation for the NRF2 package although it mixes observations with audit remarks; the expected-result cell for NRF2 repeats `what_supports`; the compound cells of the K2P rows name tools of the package (not ranked, not shown on the page); the context join is RNA class means (not protein or current).
