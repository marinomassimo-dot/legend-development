# Brief: comparators for the priority hypotheses (IT39 P8; extraction and arrangement of what the repository already holds)

Role: table builder. Read files only; no web, no PubMed, no new reading of any paper; you add no fact that no file below states. Output folder `comparators_it39_20261109/output/`. Non-canonical, not medical advice; no dose, schedule or route anywhere.

## Inputs (all under `disease-models/wwox/research/drug_repurposing/`)
`nmda_inv05_20261107/output/probes.tsv` and `README.md`; `gsk3_inv09_20261107/output/probes.tsv` and `separation.tsv`; `hcn_20261107/output/probes.tsv` and `hypotheses.tsv`; `ttype_20261107/output/probes.tsv` and `chain.tsv`; `seizure_function_inv10_20261107/output/README.md` and `questions.tsv`; `needs/needs.json` entries NEED-SEIZURE-CONTROL-SYMPTOMATIC, NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, NEED-T-TYPE-CALCIUM, NEED-INTRINSIC-EXCITABILITY, NEED-GSK3B-DEREPRESSION; `ranking_it8_p9_20261029/investigations_it20.tsv` rows INV-03, INV-05, INV-09, INV-10, INV-18. Their `verify/` audits override a README where they differ.

## Deliver `comparators.tsv`, one row per (investigation, comparator), columns
`inv_id, comparator, role, target_and_action, context_of_the_measurement (species, preparation, age or stage), selectivity_limits, exposure_or_development_note, what_it_separates, what_it_does_not_separate, source_file_and_row`

`role` is exactly one of: `functional_outcome` (a comparator for the functional result: does the burst, the sag, the seizure score change) or `mechanism_separating` (a comparator whose purpose is to tell mechanisms apart, e.g. a matched-current reduction by an unrelated mechanism, a second chemotype, a genetic perturbation of the same target).

## And deliver `antiseizure.tsv`
For the antiseizure drugs that appear in these files, one row each: `drug, target_and_action_as_stated, general_anticonvulsant_activity (what the files say), wwox_specific_rationale (only if a file states one; otherwise write NONE_STATED), kept_separate_note, source_file_and_row`. Do not assume that two drugs used for seizures share a mechanism. Keep seizure control apart from development, function and quality of life: a separate column `outcome_domain_reported` with values `seizure`, `development`, `function`, `quality_of_life`, `not_stated`.

## And `README.md`
Answer first (one page): how many rows per role per investigation; which investigation has no `mechanism_separating` comparator in the files; which cells you left `NOT_IN_FILES`. Never fill a cell from memory. Final message: completed or not, the row counts, and the model and effort you observe.
