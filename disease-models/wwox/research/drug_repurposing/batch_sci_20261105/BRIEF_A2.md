# Brief A2 (label `sb-a2`): transfer baseline for symptomatic response versus developmental outcome

Read `BRIEF_COMMON.md` first; it binds. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/a2_baseline/`. Receipt `NN` = `22`. Scratch (downloads, outside the repository): `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/sb-a2/`.

## Challenge `CH-SB-CONCORDANCE` (task record `ORCH-SCIBATCH-DR-20261105`, part 2)

**Question.** In infantile epileptic spasms syndrome (IESS) and in other early-onset developmental and epileptic encephalopathies, how tightly do the short-term symptomatic response (spasm cessation, hypsarrhythmia resolution, seizure freedom) and the later neurodevelopmental outcome move together, by treatment (vigabatrin, hormonal therapy, ketogenic diet, others) and by stratum (aetiology: unknown, structural, genetic; lead time from onset to treatment; age at onset)? Which published trials or cohorts report both endpoints for the same participants and give an association, or the numbers needed to compute one?

**Why it matters.** The records carry a WWOX observation that seizure control did not rescue development (CLAIM 031, n = 2 children, qualifier ambiguous) and the investigation `INV-10` asks what a symptomatic response predicts about development. That observation can only be read as WWOX-specific if the base rate of "responder with poor development" in comparable DEEs is known. Your table is the baseline against which the WWOX cases (package A1) are read: if the baseline coupling is weak in genetic/structural strata, discordance in WWOX is the expected case and not a distinguishing feature; if it is strong, discordance in WWOX would be informative.

## Done: cite, do not repeat

* The IT29 reader P3-E found UKISS and its 4-year follow-up at abstract level (rows E39 to E41) and stated that the infantile-spasms vigabatrin early-treatment literature beyond UKISS was not searched in depth. Read it with `git -C /home/desktop/legend-development show task/it29:disease-models/wwox/research/drug_repurposing/phenotype_first_it29_20261105/p3_E/README.md` (and `evidence_it29_E.tsv` beside it). Do not read the IT30 worktree.
* Nothing on this baseline was read at full-text level by the module.

## New work (hints only: verify every identifier in PubMed; a remembered PMID is not evidence)

1. UKISS (hormonal therapy versus vigabatrin, 14-month and 4-year development), ICISS (hormonal therapy alone versus combined with vigabatrin; development at 18 months and later), the lead-time-to-treatment literature, the US National Infantile Spasms Consortium cohorts, guideline evidence tables, and the Cochrane reviews as pointers to the primary trials (the primary trial or cohort is the unit, a review is not).
2. A bounded second axis outside IESS: in other early-onset DEEs (for example Dravet syndrome, CDKL5, STXBP1, SCN2A/SCN8A), is cognitive or developmental outcome reported to follow seizure control, to follow genotype, or to be independent of both? Three to four primary sources are enough.
3. For each source: which participants have both endpoints; how the symptomatic endpoint is defined and timed; the developmental instrument and age; the reported effect on each endpoint; the association between them (correlation, odds ratio, concordance table) or the data to compute it; modifiers (aetiology, lead time, age); funding or design features that affect reading (open label, outcome assessor blinding, loss to follow-up).

## Table

`evidence_a2.tsv` columns, in this order: `row_id, role, population, aetiology_stratum, intervention_arms, n_per_arm, symptomatic_endpoint_definition, symptomatic_endpoint_time, developmental_instrument, development_assessment_age, effect_on_symptomatic, effect_on_development, association_between_endpoints, modifiers, design_limits, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`. `role`: support | counter | context. `association_between_endpoints`: the number the source gives, or `computable` with the cells, or `not_reported`.

## Consequences fixed before you search

| Return | Consumer action |
|---|---|
| trial data show an early spasm-control difference between arms that does not carry to development in genetic/structural/unknown strata | the base rate of "responder with unchanged development" is stated with its sources; A1's discordance is read against it and `INV-10` is reworded as a generic DEE feature, not a WWOX finding |
| development tracks lead time or aetiology more than treatment arm | `INV-10` gets a transfer condition (time to treatment, aetiology stratum) |
| association is never reported | stated as "not reported in the primary sources read", with the list of trials checked |

Breadth: 6 to 12 sources read at full text (methods and results of the primary reports). Stop when the sub-question is answered or the routes are exhausted and say which.
