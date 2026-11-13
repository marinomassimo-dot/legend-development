# Verifier brief (IT50): do the cells of three restated hypotheses say what their cited sources say?

Not medical advice. Public edition. Zero spend; no network is needed; read only local files; write only into this folder. English files.

## What is being checked
`../output/hypotheses.tsv` has three rows (ISR1, ISR2, ISR3). They were written by the Orchestrator from records already on disk; every cell names its source. The risk is a cell that says MORE or LESS than its source, a prediction or a direction that no source states, a favourable compound, or a rival or premise the sources do not record.
Sources (read the ORIGINALS in full, not summaries): `../../isrib_discrim_20261108/output/cards.tsv` (CARD-A1, CARD-A2), `../../isrib_discrim_20261108/output/design.tsv`, `../../isrib_discrim_20261108/output/README.md`, the INV-02 row of `../../ranking_it8_p9_20261029/investigations_it20.tsv` (all fields: question, evidence_available, decisive_uncertainty, next_test, feasibility), `../../identity_isrib_20261108/README.md`, `../../generation_it49_20261112/p5_case_inv02/result_it49.md` and `search/search_rows.tsv` (for the counts of target-search rows).

## What to do
For each of the three rows and each non-id cell (wwox_observation, explanation_and_rivals, hypothesised_action, probe_or_compound, preparation_context, unresolved_premise, discriminating_result, prediction_stated, reopen_or_abandon) give: verdict SUPPORTED / PARTLY / NOT_SUPPORTED; the verbatim source sentence(s) with file and field or line; and every clause that goes beyond or falls short of the source. Check specifically: (1) no direction of benefit and no predicted result is stated that a source does not state; (2) ISRIB is never called a candidate or a treatment; (3) the counts of the target search (12 rows, 0 for eIF2B activation, 6 not primary-target, two PERK primary-target rows) against search_rows.tsv; (4) the discriminating outcomes of ISR1 against design.tsv step 1; (5) the identity statement against the identity README; (6) that ISR3 does not assert that any potentiator works.
Finish with a short table and one paragraph: which cells must change, and whether any row is more than a restatement.
Deliverable: `VERDICTS.md` in this folder. Do not edit any other file. A bounded "cannot determine" is acceptable; say why.
