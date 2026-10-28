# P5 · RECUPERO_PROFONDO: one block per row, in card-axis order (the order is NOT a preference)

Candidates first (5), then abstentions (7); within each group the order is the cards' axis order.

## Rows

### P4-A-01 · 4-phenylbutyrate class and bile-acid chemical chaperones · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | Return of detectable, soluble, functional WWOX protein from a Q230P-class missense lesion; the proximal readout would be total, soluble and pellet WWOX plus a WWOX function assay, none of which exists for this allele. | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Function recovery of residual WWOX protein is the only contribution hypothesised; compensation, symptom and protection are not claimed. The branch (retained, cleared, insoluble) must be placed before any contribution can be stated. | `input.p4_card.expected_contribution` |
| Evidence: state | inconclusive (rationale withdrawn, not refuted; no WWOX test). | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | None for WWOX. Adjacent precedents measure protein and function together in other proteins and the two come apart in six of them (R1 question 2); no function readout for WWOX is defined in the repository. | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Potency, relevant exposure and selectivity in a WWOX system: UNKNOWN. In the sources: class not selective for the mutant; brain exposure not measured in any R1 paper. | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Not documented in the repository. | `input.p4_card.time_to_access` |
| Time to BENEFIT | UNKNOWN. Not documented; no WWOX datum exists from which to estimate it. | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | Three-fraction (soluble, pellet, total) plus an inhibitor arm, then a chase from a detectable baseline, on the exact variant, with a WWOX function readout. The result decides whether the class is even addressed to the right branch. | `input.p4_card.next_measurement` |

### P4-A-02 · proteasome-inhibitor class · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | Return of Q230P protein from an undetectable baseline by blocking its degradation, read as total, soluble and pellet protein and then function. | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Recovery of residual protein only if Q230P is lost at the proteasome; function of any recovered protein is the unanswered question. | `input.p4_card.expected_contribution` |
| Evidence: state | not verified for this disease; and exposure-or-toxicity limit shown by its own precedent (other windows toxic to controls). | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | None for WWOX. In the closest precedent, a localisation and a myelin-marker readout moved with a partial protein return; a second precedent returned insoluble protein in which no activity could be measured. | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | UNKNOWN for WWOX; toxicity-bounded exposure window in the closest precedent (values not reproduced). | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Not documented in the repository. | `input.p4_card.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | Inhibitor-first arm on the exact variant from a detectable baseline, read as soluble/pellet/total protein, with the proteasome and lysosome arms side by side, before any chase. | `input.p4_card.next_measurement` |

### P4-B-01 · amlexanox (PTC alleles only) · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | Production of full-length WWOX protein from an allele carrying a premature stop codon, then function; proximal readout: full-length versus truncated protein on N- and C-terminal reagents plus a WWOX function assay. | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Full-length protein from a PTC allele, function of it unmeasured; no contribution is stated for the missense class. | `input.p4_card.expected_contribution` |
| Evidence: state | not verified for WWOX; elsewhere partial and a relevant negative on phenotypic rescue. | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | None for WWOX. Elsewhere: partial in one gene, a relevant negative on phenotypic rescue in the only comparator-controlled study. | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | The entire safety argument in the originating paper is historic use for other indications; no paediatric, CNS or pharmacokinetic datum. [cut: the card's field continues] | `input.p4_card.evidence_for_and_against.against` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. | `input.p4_card.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | For PTC alleles: a transcript-level NMD measurement on a recorded nonsense allele (the sequence-based enumeration exists since 2026-10-28 as a prediction only), then a function measurement on any protein produced. [cut: the card's field continues] | `input.p4_card.next_measurement` |

### P4-C-01 · AAV9-delivered human WWOX · CANDIDATE · bridge `directional_summary` = OPPOSES_DISEASE_CHANGE

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | Restoration of WWOX function by neuron-directed replacement; the single useful endpoint carried is spike-wave discharge rate. [cut: the card's field continues] | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Recovery of function by replacement (R-class demonstrated in the null mouse); nothing is stated for clinical benefit. | `input.p4_card.expected_contribution` |
| Evidence: state | partial: the only measured rescue in the corpus, complete on several R-class endpoints, with no S, C or D datum. | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | In the Wwox-null mouse, by one laboratory: SWD rate to wild-type level (single vector level); survival to 300 days at the higher vector level; a graded motor score; graded glycaemia at one age; WWOX protein graded; myelination qualitative only; [cut: the card's field continues] | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | No tumour surveillance of any kind in a pro-apoptotic tumour suppressor delivered irreversibly; no measured ceiling. [cut: the card's field continues] | `input.p4_card.evidence_for_and_against.against` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. The census records a programme with a gene-therapy objective at grant level; no registered WOREE study; sponsor-declared authorisation, enrolment and first dose UNKNOWN. | `input.p4_card.time_to_access` |
| Time to BENEFIT | UNKNOWN in humans. In the mouse the SWD effect was recorded over one week starting about two weeks after birth; no earlier ECoG timepoint exists. | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | An intermediate-level arm, defined as a fraction of the primary's higher level (never in absolute quantity), carried to 300 days with survival, weight, glycaemia, ECoG and quantified myelin in the same animals; and an independent replication. [cut: the card's field continues] | `input.p4_card.next_measurement` |

### P4-D-01 · A51, multi-kinase inhibitor · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | Restoration of cortical neurogenesis in a WWOX-deficient neural model; progenitor identity is restored, layer-neuron production is not. | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Compensation of a downstream signal; not recovery of WWOX function. | `input.p4_card.expected_contribution` |
| Evidence: state | partial (progenitors yes, layer neurons no), with an exposure-or-toxicity limit that is unmeasured rather than favourable. | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | Cell-identity markers only; no WWOX-function biomarker, no electrophysiology, no seizure endpoint, no myelin readout. | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | one grade 3 hepatic failure with encephalopathy at the highest tested level, a level the study then discontinued for potential serious liver injury although its maximum-tolerated-dose criteria were not met. [cut: the card's field continues] | `input.p4_card.evidence_for_and_against.against` |
| BLOCK-1 status | BLOCK-1 open; causal attribution ambiguous; no paediatric record; direction of benefit not signed. | `input.p4_card.status_reason` |
| Time to ACCESS | UNKNOWN. Not documented; no registered WOREE study and no paediatric exposure. | `input.p4_card.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | A dose-by-timing series in a developing-cortex model with a treated wild-type arm, progenitor and layer-neuron endpoints and an electrographic endpoint; a selective MYC inhibitor to separate Wnt from MYC; and a brain-region exposure level in a young animal. | `input.p4_card.next_measurement` |
| Exposure versus dose in the cited adult study (class-level fact of a cited study, NOT WWOX EVIDENCE) | The paper states plasma exposure was dose-proportional between its lowest and highest levels; its printed table, with N per cohort 1, 1, 3, 3, 3, 8, 5 across seven levels and printed CVs of 4.1 to 79 percent (only for cohorts of three or more), gives day 5 exposure (AUC) roughly proportional to dose from the second to the sixth cohort (log-log slope about 0.95 by the two end points, about 0.98 over the five points, a span that still begins at a cohort of one), supralinear only when the lowest cohort, a single patient, is included (slope about 1.38), and 1.27-fold higher at the top cohort than at the one below for a 2.0-fold dose ratio; the day 1 exposure cell of the top cohort is blank. [cut: the card's field continues] | `input.p4_card.evidence_for_and_against.against` |

### P4-A-03 · client-binding pharmacological chaperone · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 8 and R1 § 1 (39216838, 32023956) | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | A measured thermal-stability or binding assay of the exact variant and a candidate-ligand screen; each would turn this abstention into a card. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | A ligand known to bind the WWOX SDR domain, and a measured instability of Q230P that such a ligand could stabilise. No experimental structure of the SDR domain exists in the repository (CLAIM 019: AlphaFold and in-silico values only, IPOTESI). | `input.abstention_card.missing_datum` |

### P4-A-04 · ER-proteostasis regulators · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | R1 § 1 (41178115, 38731820); known-roads § 2.8 (DIS-004 wrong compartment) | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | The three-fraction plus inhibitor design on the exact variant would place it; the answer decides whether this axis exists for a cytosolic enzyme. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | Where Q230P is surveilled: WWOX is cytosolic, and no measurement places the variant in ER or cytosolic quality control. Without that, a UPR or ERAD modulator has no stated target in this lesion. | `input.abstention_card.missing_datum` |

### P4-A-05 · HSP70-axis modulation · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 2.8 (D-03); R1 § 1 (33914734, 42875792) | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | A chase paired with a chaperone-function perturbation on the exact variant from a detectable baseline. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | The direction of effect of HSP70-axis modulation on Q230P: amplifying the axis may accelerate delivery of the mutant to degradation (HSC70 delivers it to the lysosome in the P252A bridge hypothesis), and blocking it stabilised an insoluble protein, with no [cut: the card's field continues] | `input.abstention_card.missing_datum` |

### P4-B-02 · PTC read-through class · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 4.4, § 5 | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | A transcript-level NMD assay on a recorded nonsense allele; the sequence-based enumeration (prediction only) is done. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | A transcript-level NMD measurement on a recorded WWOX nonsense allele (with and without an NMD-discriminating arm). [cut: the card's field continues] | `input.abstention_card.missing_datum` |

### P4-C-02 · splice-correcting ASO / editing · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 2.8, § 6 | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | Junction-spanning RT-PCR with and without an NMD block on material carrying a canonical splice allele. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | A baseline: no aberrant-to-normal transcript ratio exists for any WWOX splice allele in any tissue, no WWOX splice allele has had its RNA examined with an NMD inhibitor, and no intragenic precedent exists. [cut: the card's field continues] | `input.abstention_card.missing_datum` |

### P4-C-03 · endogenous boost (CRISPRa or equivalent) · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 2.8 | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | Synthesis and fate of the exact variant (the same fractionation-and-inhibitor design) decides whether raising its expression can help. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | Whether Q230P synthesis is translation-limited and whether the variant protein folds: a non-allele-specific boost raises both alleles, so the sign of the benefit depends on a folding fate that is unknown. Never attempted in any WWOX system. | `input.abstention_card.missing_datum` |

### P4-D-02 · Wnt-lowering agents and GSK3 modulation · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | **UNKNOWN** | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | **UNKNOWN** | `input.p4_card.expected_contribution` |
| Evidence: state | known-roads § 2.4(c), § 2.2; R3 §§ 1.2, 8 | `input.p4_card.state_of_known_roads` |
| Evidence: functional evidence available | **UNKNOWN** | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | **UNKNOWN** | `input.p4_card.pharmacology` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | **UNKNOWN** | `input.p4_card.time_to_access` |
| Time to BENEFIT | **UNKNOWN** | `input.p4_card.time_to_benefit` |
| Feasibility: what must exist to test it | Activation-step measurement (reporter, nuclear beta-catenin) in a WWOX-deficient neural system, then the dose-by-timing series. | `input.p4_card.next_measurement` |
| ABSTENTION: the missing datum | A dose-by-timing series of Wnt/GSK3/CK1 modulation in a developing cortex with progenitor, layer-neuron and electrographic endpoints, in any WWOX system; and a measured activation step (reporter or nuclear/cytosolic beta-catenin). [cut: the card's field continues] | `input.abstention_card.missing_datum` |

