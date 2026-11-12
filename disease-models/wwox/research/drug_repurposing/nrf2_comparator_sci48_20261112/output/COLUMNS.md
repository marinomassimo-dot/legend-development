# Column names and vocabularies (SCI48)

Plain snake_case names in the TSV headers; the original header text, with its vocabulary, is below.

## matrix.tsv

- `row_id`: row_id
- `reagent`: reagent (RA839 | sulforaphane | KI-696 reused | other)
- `source`: source
- `cell_class_and_system`: cell_class_and_system
- `what_was_measured`: what_was_measured
- `loss_arm_and_adequacy`: loss_arm_and_adequacy
- `explanation_supported`: explanation_supported (H1-H6 of S0)
- `explanation_weakened`: explanation_weakened
- `what_it_does_not_allow`: what_it_does_not_allow
- `transfer_to_wwox_context`: transfer_to_WWOX_context (claim 1 acts through NRF2 / claim 2 useful in WWOX loss / claim 3 transferable)
- `role`: role (with rule)
- `missing_datum_that_changes_role`: missing_datum_that_changes_role

## sfn_table.tsv

- `row_id`: row_id
- `pmid_or_doi`: pmid_or_doi
- `authors_year`: authors_year
- `neural_class`: neural_class (and line/primary/in vivo)
- `species_age_prep`: species_age_prep
- `sfn_identity`: sfn_identity (racemic or R, vendor/purity if stated)
- `sfn_conc`: sfn_conc
- `sfn_time_and_vehicle`: sfn_time_and_vehicle
- `exposure_toxicity_control`: exposure_toxicity_control
- `loss_type`: loss_type (germline KO, siRNA, shRNA, dominant negative, inhibitor, none)
- `loss_verified`: loss_verified (protein, mRNA, target gene, none; at the endpoint time? yes/no/unstated)
- `endpoint_class`: endpoint_class (molecular, viability, function)
- `endpoint`: endpoint (what is read)
- `result_wild_type`: result_wild_type
- `result_under_loss`: result_under_loss (with units and n)
- `remaining_effect`: remaining_effect
- `keap1_loss_or_nrf2_gain_arm`: keap1_loss_or_nrf2_gain_arm (yes/no)
- `second_reagent_class_in_same_design`: second_reagent_class_in_same_design (yes/no, which)
- `authors_interpretation`: authors_interpretation (<=25 words verbatim)
- `independence_note`: independence_note (same group or dataset as another row)
- `locator`: locator
- `depth`: depth
- `kind`: kind
