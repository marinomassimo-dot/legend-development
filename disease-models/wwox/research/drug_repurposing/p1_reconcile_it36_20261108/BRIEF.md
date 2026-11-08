# Brief: package-to-consumer map (IT36 P1, mechanical extraction; you change no consumer)

Role: map builder. Read files only; no web, no PubMed, no new reading of any paper. Output folder `p1_reconcile_it36_20261108/output/`. Non-canonical, not medical advice.

## Packages (each has `output/README.md`, `output/evidence.tsv`, and `verify/audit_*.md`, the independent audit; the audit overrides the README where they differ)
`ttype_20261107` (T-type), `nmda_inv05_20261107`, `myelin_inv06_20261107`, `metabolic_inv07_20261107`, `nrf2_inv08_20261107`, `gsk3_inv09_20261107`, `seizure_function_inv10_20261107`, `pv_inv15_20261107`, `hdac5_inv16_20261107`, `hcn_20261107`. All under `disease-models/wwox/research/drug_repurposing/`. Also `gsk3_inv09_20261107/BRIEF.md`, `pv_inv15_20261107/BRIEF.md` mention a consumer note.

## Consumers to compare against (grep them; do not edit)
`needs/needs.json` (fields observed, inferred, counter_evidence, notes, intervention_direction, targets), `ranking_it8_p9_20261029/investigations_it20.tsv` and `investigations_context_it21.json` (rows INV-01..INV-18), `cards/`.

## One row per package conclusion that could change a consumer: `map.tsv`, tab-separated, columns
`package, inv_id, conclusion_after_audit (one sentence, using the audit's wording where it narrowed the README), audit_overturned_or_narrowed (what the audit changed, with the audit's row id), consumer_file, consumer_field_or_row, consumer_already_says (quote at most 25 words, or NONE after grep), proposed_change (exact new or changed wording, at most 60 words), change_class, source_to_check (PMID/source id the change rests on, or NONE), conflicts_with_preserve_rule (NONE or which)`

`change_class` is exactly one of: `1_editorial_narrowing` (keeps a meaning the package already verified), `2_new_scientific_conclusion`, `3_new_quantitative_analysis` (counts, p-values, effect sizes, recomputations).

## Rules the proposed changes must respect (preserve rules)
- MYC: role unresolved or context-dependent; increase is not harm; lowering is not therapy.
- Syn1-Cre recombination is partial and mosaic; percentages from another reporter do not measure Wwox excision in PV cells.
- T-type: a pharmacological result does not identify Cav3, an isoform or a genotype-specific effect.
- INV-10: the reclassification from four to three discordant children was withdrawn.
- HDAC5: HDAC5-HIF papers exist; this does not show a therapeutic link in WWOX nor equate lower protein with catalytic inhibition.
- HCN: sag, input resistance and rebound alone do not identify an Ih defect.
- NRF2: a withdrawn reference was not found in the repository; propose no canonical correction if there is nothing to correct.
- A p-value statement: record test, n, unit of observation, SD/SEM, rounding and assumptions; "not reproducible from the published statistics under these assumptions" is not "the original data are false".
- Do not carry the claim "no receipt recorded": check `disease-models/wwox/registries/fulltext_read_receipts.jsonl` by event_id only if a receipt matters to a row.

## Also deliver
`README.md` (answer first, at most one page): how many rows, how many per class, which rows are already in the consumers (`consumer_already_says` not NONE), which rows are class 2 or 3 (these go to a source check), and anything you could not map. Final message: completed / not completed, the number of rows by class, and the model and effort you see in your runtime.
