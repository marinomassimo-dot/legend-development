# Brief A1 (label `sb-a1`): published WWOX-related DEE reports, intervention outcomes and denominators

Read `BRIEF_COMMON.md` first; it binds. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/a1_wwox_reports/`. Receipt `NN` = `21`. Scratch (downloads, outside the repository): `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/sb-a1/`.

## Challenge `CH-SB-CONCORDANCE` (task record `ORCH-SCIBATCH-DR-20261105`, part 1)

**Question.** In the published reports of WWOX-related developmental and epileptic encephalopathy (WOREE, SCAR12, other biallelic WWOX epileptic encephalopathy), for each intervention class (vigabatrin; ketogenic diet; hormonal regimens: ACTH, corticosteroids; cannabidiol; other antiseizure drugs only as co-therapy context), (1) how many patients does each report give as tried, continued, stopped, responded and not responded, (2) for how many of them is a developmental outcome recorded, and (3) among patients with both a symptomatic outcome and a developmental outcome recorded, do the two move together or apart? Fill the denominators the module declares missing: the number of patients exposed to the ketogenic diet in the five-patient series (CLAIM 042 says the denominator is not stated); for the vigabatrin MRI-signal cases (Choi 2026, PMID 41442931, abstract only in the module), the number of children on vigabatrin, the number with the MRI change, age band at exposure, duration class, and whether hormonal therapy was co-administered when the MRI changed.

**Decision at stake.** Whether the C2 flag stays on the vigabatrin and ketogenic-diet case series (work order `NEED-SEIZURE-CONTROL-SYMPTOMATIC`); what the investigation `INV-10` may say about "what the published symptomatic response predicts about development" (its next test is exactly this assembly and it has not been executed); the wording of CLAIM 001, 031 and 042; what the physician-facing view may say about a symptomatic response.

## Done: reuse by id, do not re-read from scratch

* Complete reads exist for PMIDs 30361190, 37583270, 39101447, 35573960 (and partial for 42092735, 36537114): their verbatim locators are in `disease-models/wwox/research/deepdive_manifests/PMID<N>.json`; assemble per-case rows from those entries. Re-open a passage only for a datum the manifest does not hold, and then set `reread_reason` = `new_question_outside_prior_coverage` with `prior_receipt`.
* Existing assertion table: `disease-models/wwox/research/drug_repurposing/catalogue_funnel_it18_p2_20261101/vigabatrin_sources_resolved.tsv` (A-VGB-1 to A-VGB-11). Cards: `cards_early/EB-VGB-01`, `EB-KD-01`, `EB-CBD-AX-01`, `EB-HORM-AX-01`, `EB-DEV-AX-01`; `typed_assertions_20261023.tsv`; `cards/H02_gabaat_inactivator_myelin_exposure.packet.json` (Choi 2026 at abstract level).
* Claims as carried (read them in `disease-models/wwox/registries/claim_registry_current.md`, the claim registry may be read whole): CLAIM 001 (status `conflicting evidence`), CLAIM 031 (the qualifier "in some of these cases" is ambiguous in the source; do not resolve it by assertion, resolve it from the source text if you can reach it), CLAIM 042.

## New work

1. Full text of Choi 2026 (PMID 41442931) and of Chong 2023 (PMID 36537114: per-patient narratives and Table 1) by an open route; if only part is reachable, say which part.
2. A bounded search for WWOX-related DEE reports that state an intervention and an outcome and are not yet in the module. Run at least: PubMed and Europe PMC for `WWOX AND (epilep* OR encephalopath* OR WOREE OR SCAR12)` combined with each of `vigabatrin`, `ketogenic`, `ACTH`, `corticosteroid OR prednisolone`, `cannabidiol`, `hormonal`; plus the cohort papers (a 2025 cohort lists vigabatrin among the most used drugs without efficacy data). For each hit check `registry_records.py get --pmid <PMID> --hops 1`: known and read -> assemble from its manifest; known but `queried_not_full_read` or absent -> read it now.
3. For every case, record the symptomatic outcome and the developmental outcome as the paper states them, with the instrument or the absence of one ("clinical report", "video-EEG", "parent report", "not stated"), the time course if stated, and co-therapy. Do not infer a developmental outcome from an age or a diagnosis label.

## Tables

`cases_a1.tsv` columns, in this order: `row_id, source_id, source_depth, case_label_as_printed, genotype_class, onset_age_as_stated, intervention_class, intervention_status, co_therapy_stated, symptomatic_outcome, symptomatic_instrument, developmental_outcome, developmental_instrument, concordance, imaging_finding, locator_quote, role`.
* `intervention_class`: vigabatrin | ketogenic_diet | hormonal | cannabidiol | other_context. `intervention_status`: tried | continued | stopped | added_on | not_stated. `symptomatic_outcome`: resolved | partial | none | worsened | not_reported. `developmental_outcome`: improved | stable | regressed | severe_impairment_unchanged | not_reported. `concordance`: concordant | discordant | not_assessable (say why in `locator_quote` context or in the README). `role`: support | counter | context.
`denominators_a1.tsv` columns: `intervention_class, source_id, n_patients_in_report, n_tried, n_continued, n_stopped, n_symptomatic_response, n_no_response, n_with_developmental_outcome, n_with_both_endpoints, n_concordant, n_discordant, denominator_stated_by_source, note`. Use `NA` where the source gives no number; never back-fill from another paper.

## Consequences fixed before you search (the Orchestrator will apply them to what you return)

| Return | Consumer action |
|---|---|
| 5 or more patients with both endpoints for an intervention class | `INV-10` evidence text gets the counts with sources; no percentage under n = 10 |
| fewer than 5, or endpoints never recorded together | statement becomes "not computable from the public record: k of N"; C2 stays; the next test is reworded as a request for denominators (no contact is made) |
| Choi 2026 states exposure counts | `NEED-MYELINATION` / H02 "human MRI denominators" line is filled; if hormonal therapy was co-administered at the time of the MRI change in any case, the H02 caveat names it as a confounder |
| any claim wording looks wider than its source | goes to `module_inputs.md` as a proposed narrowing with the quote; nothing is edited |

Breadth: at most 12 sources in full text. Stop when your queries are exhausted and say so.
