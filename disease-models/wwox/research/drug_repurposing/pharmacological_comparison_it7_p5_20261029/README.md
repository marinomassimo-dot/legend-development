# IT7 P5 (roadmap R5): a small pharmacological comparison across both research objectives

Scientist-a, task `ORCH-ROADMAP-IT7-20261029`, 2026-10-29. Non-canonical research material. **Not medical advice; no dose, route, schedule or individual recommendation. A computational result is not therapeutic efficacy.** The reference genotype class is a WWOX-DEE genotype class; no individual-level record is used. Nothing here edits a scientific current file, the receipt ledger, a card or a need.

Deliverable: `comparison.tsv` (9 records x 21 columns, one header, rectangular, no trailing notes). This README says how to read it.

## 1. What is compared, and why these nine

Records were chosen to cover both research objectives and several kinds of lever, not to rank them.

| Record | Hypothesis | Objective | Kind of intervention |
|---|---|---|---|
| CMP-01 | A01 chemical chaperones (phenylbutyrate and bile-acid class) | broad durable recovery | drug class, missense protein rescue |
| CMP-02 | A02 proteasome-inhibitor class | broad durable recovery | drug class, missense protein rescue |
| CMP-03 | C01 / C04 AAV9 gene addition | broad durable recovery | gene therapy, early window |
| CMP-04 | E02 LDH inhibition (stiripentol and research inhibitors) | useful partial benefit | drug, glycolysis / lactate axis |
| CMP-05 | I01 / E03 dichloroacetate, PDK inhibition | useful partial benefit | investigational drug, PDH axis |
| CMP-06 | E04 / EB-KD-01 ketogenic diet | useful partial benefit | diet (complex intervention) |
| CMP-07 | F04 NMDAR / AMPAR intervention classes | useful partial benefit | approved and clinical-stage drugs, tools |
| CMP-08 | P11 magnesium | useful partial benefit | supplement / nutrient |
| CMP-09 | J01 glial-reactivity modulators | useful partial benefit | drug classes, abstention |

The glycolysis / lactate / PDH axis has three records (CMP-04 to CMP-06) because it is the axis that P1 (typed subnetwork) and P3 (method comparison) worked on, so it is the only place where a model position exists at all.

## 2. Three things kept apart (they are separate columns on purpose)

1. **Research priority** (`PRIORITY_position_and_work_order_reason`): the F / C / P position the view assigns to the card x need link (`repurposing_view.py positions`, run on this branch) and the work-order reason for the need. It answers "where should the next study go", not "does the drug work". Positions are rule-based, one per link, never summed or best-of-needs.
2. **Model position** (`MODEL_position_P3_P2`): what the IT7 P3 comparison and the IT7 P2 usable-compound census say about the compound or class. In this iteration that is **nothing positive for any record**: P3 found no added value for a signed external network or for four duplicate HIF1A edges (labelled 'WWOX-enriched' in IT7; no test of WWOX knowledge, IT8 P4), and for the signature route an effect that was **not detected and not excluded** (rho 0.143 against a 0.15 threshold, 90 percent interval 0.039 to 0.243, minimum detectable effect about 0.157; weak positive counter-evidence: lower bound 0.039, top-decile hit rate 15 percent); exploratory; 256 families chosen by input availability. It left module transfer to the P47T deposit inconclusive (producer's draw: null 95th percentile 0.389, exact p 0.060; the verifier's draw 0.396 and 0.0595; 5 of 6 genes in the build direction). Card-linked compounds were firewalled out of every P3 method, so even the two E-axis compounds have no model score. P2 only says whether a method has the input it needs. The P3 numbers come from the `task/it7-p3` branch (commit `0d9d9879`); the P3 verifier report (`ce89192d`) reproduced every quoted number. The P2 census is integrated.
3. **Observed evidence** (`OBSERVED_wwox_specific_evidence`, plus the premise columns): what a source measured in a WWOX-deficient system, with its readout level. External precedents (other proteins, other diseases) are in their own column with the depth of reading and are never WWOX evidence. Apart from the AAV9 vector (CMP-03) and the tool compound d-APV in a knockout slice (CMP-07), no gene vector or compound of these records has been given to a WWOX-deficient system with a molecular or functional readout.

Two further columns are independent of each other and of the three above: **genotype / lesion applicability** (Track A allele-blind, or Track B lesion-specific) and **depth of benefit** (deep restoration or partial benefit). Gene addition is Track A and deep; a missense chaperone is Track B and deep; every metabolic, excitability and glial lever here is Track A and partial. Track says to whom a lever could apply; depth says how much it could change; neither says that it works.

## 3. Columns

`record_id`, `hypothesis_cards`, `intervention_and_type`, `research_objective`, `genotype_lesion_applicability_track`, `depth_of_benefit_sought`, `biological_effect_sought`, `need_link`, `PRIORITY_position_and_work_order_reason`, `MODEL_position_P3_P2`, `OBSERVED_wwox_specific_evidence`, `premise_demonstrated`, `premise_missing`, `external_precedents_with_reading_depth`, `potentially_opposed_effects`, `potency_with_assay_context`, `human_exposure`, `brain_penetration`, `next_decision_changing_experiment`, `experiment_status`, `sources`.

Paths in `sources` are relative to `disease-models/wwox/research/drug_repurposing/`. `UNKNOWN` means the repository holds no datum; it is never a zero.

## 4. What the comparison shows (and does not)

* **No record is dominated, and none is ahead.** The nine differ in what is missing, not in how much is known: the three broad-recovery records wait on a measurement (fate and function of the missense protein; dose, threshold and post-onset window for gene addition), the six partial-benefit records wait on a WWOX-system premise (PDH phosphorylation, LDH activity, isolated NMDAR current, Mg2+ titration, pre-spike glial sign). Only gene addition (a null mouse, an early window, one laboratory) and the tool compound d-APV (one slice experiment) have an observed WWOX-system result.
* **Opposed effects are listed beside the desired ones and are not netted.** Examples: dichloroacetate is expected to lower glucose while hypoglycaemia is the Wwox-null phenotype; stiripentol acts on complex I at lower concentrations than on LDH; NMDAR block in a developing brain has an apoptosis and a myelination concern; a chaperone class raises wild-type protein as well; AAV9 over-expresses a tumour suppressor with no measured ceiling. No row carries a combined score.
* **Potency is quoted with its assay, and rarely transfers.** The numbers are source assays (cell-free, oocyte, HEK293, CHO flux, HeLa extract) with voltage, Mg2+, auxiliary subunit and species stated where known; a median across them describes the literature, not a drug. Exposure at the target tissue is `UNKNOWN` for every small molecule here. A first ChEMBL activity query for dichloroacetate failed with HTTP 500 (a failed source, not absence); the re-query on 2026-10-29 answered, and CMP-05 now carries the dichloroacetate rows: censored enzymatic IC50 above 1,000,000 nM and a cell EC50 of 130,000 nM, whose gap between cell and enzyme is stated there.
* **The proposed experiments were not run.** The NMDAR isolated-current and Mg2+ titration, the ISR measurements of iteration 6 and every other experiment in `next_decision_changing_experiment` are PROPOSED (column `experiment_status`). Their absence does not block the computational work, and no row implies a result.

## 5. Limits

* Track and depth are shown independent in three of four cells (A-deep: gene addition; B-deep: chaperone and proteasome classes; A-partial: the six others); **B-partial is not represented** among the nine.
* Nine records are a small sample; the choice is by coverage of objective and lever type, not a screening of all the cards.
* Positions come from the rules of `priority_rules_it5_20261029.md` as implemented on this branch; they describe the shape of the evidence on one need, not the merit of an intervention. C01 shows F2 on this branch (one experiment, n 5, flagged) while C04 shows F1 for the same need; older prose that calls C01 F1 is historical.
* Several external precedents are abstract- or review-level (stated per cell). Where a sentence rests on a card note without a re-opened source it inherits the card's depth; this comparison opened no new paper.
* Model-position statements depend on the P3 result (verified, not necessarily integrated) and the integrated P2 census; re-read them if either changes.

## 6. UNVERIFIED

Whether P3 is revised after its verification (its numbers are quoted from commit `0d9d9879`); the exact label text of phenylbutyrate and dichloroacetate (label lookup NOT_ATTEMPTED / no match in openFDA on 2026-10-29); that the human use of the magnesium preparations named in the supplement record matches any preparation tested in the cited animal study; whether the recording bath of the NMDAR source equals its incubation solution.
