# Brief B1 (label `sb-b1`): vigabatrin and CPP-115 white-matter safety, and what transfers to a hypomyelinating brain

Read `BRIEF_COMMON.md` first; it binds. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/b1_whitematter/`. Receipt `NN` = `23`. Scratch (downloads, outside the repository): `/tmp/claude-1000/-home-desktop-legend-development/9400b253-25a0-4b03-8822-96361325fc16/scratchpad/sb-b1/`.

## Challenge `CH-SB-VGB-WHITEMATTER` (task record `ORCH-SCIBATCH-DR-20261105`)

**Question.** What do human and animal studies show about white-matter and MRI abnormalities with vigabatrin (MRI signal change in the basal ganglia, thalamus and brainstem; intramyelinic oedema; myelin loss; gliopathy) and with its sibling GABA-aminotransferase inactivator CPP-115: incidence in infants and children; dependence on age at first exposure, exposure duration and cumulative exposure (qualitative only), concurrent hormonal therapy, and underlying aetiology; reversibility after stopping; clinical correlates and their absence; and which of those conditions transfer, or break, in a brain with a hypomyelinating baseline (the neuron-deleted Wwox mouse; WWOX-DEE children with delayed myelination and callosal hypoplasia)?

**Decision at stake.** The position and caveat of card H02 and the work order `NEED-MYELINATION` ("does vigabatrin or CPP-115 exposure add myelin injury in a Wwox-deficient juvenile model, given the baseline white-matter loss in the human cases?"); whether the statement "start age decides" is supported at full-text level; the shape of an exposure-window series if an animal experiment is ever designed (windows, readouts, recovery arm), stated qualitatively; whether the unit needs a harm tag at card level.

## Done: cite, do not repeat

Card H02 (`disease-models/wwox/research/drug_repurposing/cards/H02_gabaat_inactivator_myelin_exposure.packet.json`) holds, mostly at abstract level: juvenile rat studies (PMIDs 21473881, 25554247), a juvenile dog study (PMID 26157036), a single-child neuropathology report (PMID 19773459), the US prescribing information sections on abnormal MRI signal changes in infants and on intramyelinic oedema (captured from the openFDA label JSON, set id 082d818a-4f4e-4675-98c6-91db0294e63c, version effective 2026-06-15), the two WWOX children with the MRI finding (Choi 2026, PMID 41442931, abstract only), and CPP-115 sources (PMIDs 24321005, 27668180, 28741622, 22128851). Package A1 reads the WWOX reports (including Choi 2026) for denominators: do not duplicate that; if you need a WWOX datum, cite A1's directory once its table exists, else say it is pending.

## New work (hints only: verify every identifier in PubMed)

1. Convert the abstract-level toxicology sources into full-text readings where an open route exists, focusing on the design facts that decide transfer: species and strain, age at first exposure, dosing window and duration (qualitative: "from postnatal day 4 for 9 weeks"), the dose-response ordering without reproducing administered doses, the lesion definition, EM or light microscopy, recovery period and what recovered.
2. The human literature on vigabatrin-associated MRI abnormality in infants (case series and cohorts from the 2000s and 2010s): incidence, age at onset of exposure, duration and dose class, risk factors (young age, high dose, hormonal co-therapy), reversibility on follow-up MRI, clinical correlates (movement disorder, hypotonia) and the proportion asymptomatic; also the argument that hormonal therapy can cause its own MRI changes (confounding). A systematic review is a pointer to the primary series, not the unit.
3. Anything on vigabatrin or GABA-aminotransferase inhibition in a model with a myelin deficit or an immature oligodendrocyte compartment (search without WWOX in the string). A bounded null is a deliverable.
4. CPP-115: preclinical safety on the white-matter endpoint, if any; its retinal data are context only.

## Table

`evidence_b1.tsv` columns, in this order: `row_id, role, species_or_population, age_at_first_exposure, exposure_pattern_qualitative, duration_class, baseline_condition, endpoint, finding, reversibility, cofactors, direction, measure_level, source_id, source_depth, locator_quote, transfer_conditions, transfer_breakers`. `direction`: harm | no_harm | undetermined | context_dependent. `measure_level`: histology | EM | MRI | clinical | label_text. `role`: support | counter | context. Never an administered-dose number in any field.

## Consequences fixed before you search

| Return | Consumer action |
|---|---|
| human risk concentrated in the first two years, with duration or dose-class dependence and mostly reversible changes | H02 carries a transfer condition "WWOX-DEE infants are inside the risk window by age; the interaction with a hypomyelinating baseline is unstudied; do not assume protective or additive" |
| rodent or dog start-age series confirmed at full text | the "start age decides" sentence is kept with its sources and its species limits; the exposure-window series is written qualitatively into the work order text proposal |
| the human series do not separate hormonal therapy from vigabatrin as the cause | named as an unresolved confounder on H02 and in the A1 reading of Choi 2026 |
| nothing on a myelin-deficient baseline | stated as "not found after: <queries>"; the work order question stays open |

Breadth: 8 to 12 sources read at full text (design and results). Stop when answered or exhausted and say which.
