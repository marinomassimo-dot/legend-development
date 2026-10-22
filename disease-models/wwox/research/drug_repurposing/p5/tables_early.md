# P5 · BENEFICIO_PRECOCE: one block per row, in card order (the order is NOT a preference)

Candidates first (3), then abstentions (6).

## Rows

### EB-KD-01 · ketogenic diet · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | clinician-reported seizure control, symptomatic only (the endpoint type the only WOREE therapeutic report used); no count, score, latency, duration or exposure denominator on the delivered surface | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Symptom (seizure control), to be verified. No compensation, function recovery or protection is claimed. Not disease modification. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Inconclusive (known-roads note 2.7): the exposed denominator is absent, 'responded' is undefined, and a DEE base-rate comparison spans 0 to 100 per cent. [cut: the card's field continues] | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none for the gene: no WWOX read-out of any kind in the source, so whatever changed in those children nothing measured WWOX; a clinician statement only | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Paediatric suitability is not presumed: a diet is not safe because it is food (early-benefit note). Adverse effects: UNKNOWN in the records read. Interaction with antiseizure co-medication: UNKNOWN (co-medication not reported in the retrieved passages). | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Documented obstacles to administrability were assessed in no record read. CLAIM 042 calls the diet a «clinically available intervention»; that phrase is not an access assessment and not paediatric suitability. [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN, separately from access. No latency or duration appears on the delivered surface; the narratives where it would appear are not covered. [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Does the Results narrative of the series give the number of children placed on the diet, a seizure count before and after, the interval to response and the co-medication? Closing that needs a native surface of the article (on the operator's PDF list); [cut: the card's field continues] | `input.p4_roadmap_fields.next_measure` |

### EB-VGB-01 · vigabatrin · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | clinical cessation of epileptic spasms with a stated criterion (one report used cessation for at least four weeks); symptomatic only; electrographic confirmation is absent in the reports | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Symptom (spasm control) to be verified against an exposure limit. Not disease modification (CLAIM 031). | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Partial plus exposure-or-toxicity limit; CLAIM 001 status is conflicting evidence and is confirmed as correctly conflicting: efficacy on spasms (n = 2 and n = 1) against MRI toxicity (n = 2). | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none for the gene. Clinical spasm control in n = 1 reports; at least one report shows clinical freedom with persisting electrographic attacks | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Paediatric safety is the limit itself (VABAM). Interactions: concurrent hormonal therapy is a candidate confounder or co-factor for the MRI finding in non-WWOX cohorts. Suitability is not presumed. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Not assessed in any record read. Clinical census 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven unfiltered queries on ClinicalTrials.gov API v2 returned no registered WOREE interventional study; [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. No latency is recorded in the reports; one report defines response as cessation of at least four weeks, which is a definition, not a time. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Was hormonal therapy given concurrently in the WWOX reports of MRI abnormality, and was the MRI repeated after withdrawal? The anchor paper has no receipt in the ledger: reading it is the cheapest closing step. | `input.p4_roadmap_fields.next_measure` |

### EB-ETX-01 · ethosuximide (T-type contrast) · CANDIDATE · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | late-phase PTZ-provoked behavioural seizure score in a three-genotype design with an explicit drug-by-genotype interaction test and a concurrent same-day PTZ-alone control (the falsifier of DL-MECH-170); no human endpoint is yet defined for this candidate | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Symptom (provoked seizure). Not disease modification: in a digenic absence mouse (NOT WWOX EVIDENCE) the ethosuximide effect and a Cav3.1 deletion suppressed the seizure and left a quantified comorbidity untouched (R2 section 6). | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Partial (known-roads note 2.3), now narrowed by the R2 note: not a clean genotype-specific effect. The lithium arm of the same figure suppressed in all three genotypes (relevant negative on specificity). | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | one mouse experiment, one laboratory, symptomatic class; no T-type current measured in any Wwox system; [cut: the card's field continues] | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | UNKNOWN. Class-level signal only: T-type blockers reduce progenitor viability in vitro (research compounds, rat, Cav3.1-dependent), significance unknown. [cut: the card's field continues] | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Not assessed in any record read. Clinical census 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven unfiltered queries on ClinicalTrials.gov API v2 returned no registered WOREE interventional study; [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. No human age-at-treatment datum of any kind exists; no experiment in any WWOX model varies age at treatment beyond mouse P5 (early-benefit note, section 4). | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Is the late-phase ethosuximide effect in the null reproduced, with a drug-by-genotype interaction test, a concurrent same-day PTZ-alone control in every cell and a per-genotype baseline stated? The R2 design sketch says power depends mainly on which control [cut: the card's field continues] | `input.p4_roadmap_fields.next_measure` |

### EB-GROWTH-AX-01 · growth (endpoint axis, not an intervention) · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | head circumference, height and weight against age-expected SD scores at a stated age, repeated | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Quantitative as a kind of measurement, repeatable, already collected in routine care, with an age-expected trajectory as comparator. A good early-benefit endpoint and a bad specificity argument: it moves with feeding route, infection, diet and seizure burden. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | No intervention has a growth measurement in WOREE. UNKNOWN. | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none for any intervention; the only human values sit on a surface that strips signs and ranges | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Not applicable. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | Not applicable to an endpoint; the intervention that would be measured has UNKNOWN access. | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Can a native surface of the series be acquired so that the growth values, the exposure denominator and the seizure-count question are all read in one acquisition? | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: the growth values and any intervention measured against them. | `input.p4_roadmap_fields.status` |

### EB-DEV-AX-01 · development / disease modification (axis) · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | a within-patient developmental measure (growth-scale or raw-score form) across an intervention, against a repeated pre-intervention baseline | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | None claimable. 'Protection' is not licensed. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Every disease-modification cell in the known-roads census is empty. [cut: the card's field continues] | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | not established here: the early-benefit note's title-and-abstract-level query found no WWOX paper indexed for a standardised developmental, motor or seizure-severity instrument; [cut: the card's field continues] | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Not applicable. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | Not applicable. | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN; the shortest sufficient follow-up in the precedents is 12 months for instrument change and 24 to 36 months for developmental trials, none WOREE. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | What is the visit-to-visit scatter of a growth-scale developmental instrument in an untreated WOREE child? | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: any within-patient developmental measurement in WOREE. | `input.p4_roadmap_fields.status` |

### EB-PDANCHOR-AX-01 · pharmacodynamic anchor (axis) · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | UNKNOWN: engagement of a WWOX-directed target cannot be shown at all today | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | None. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | UNKNOWN. | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none: the three direct read-outs (transcript, immunoblot, tissue stain) have no limit of detection, linear range or calibrator, and the tissue read-out reached only fair inter-rater agreement; canine tumour matrix, no WWOX variant, no CNS tissue, no body fluid | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | Not applicable. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | Not applicable. | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | Not applicable. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Can a WWOX assay report a concentration against a recombinant calibrator, with a stated limit of detection, in a matrix obtainable from a living patient? | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: a calibrated WWOX read-out in a living-patient matrix. | `input.p4_roadmap_fields.status` |

### EB-HORM-AX-01 · ACTH, corticosteroids, phenobarbital regimens · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | clinical cessation of epileptic spasms, if and only if a comparator separates a WWOX-genotype response from ordinary West-syndrome pharmacology | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Symptom, to be verified; unseparated from standard care. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Partial, confounded by West-syndrome pharmacology (known-roads note 2.7); visible only in the supplement while the running text calls the regimens flatly not effective. | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none for the gene: six explicit responders in a per-patient supplement column of one curation, 'Yes' undefined, no control arm, dosing, duration or standardised follow-up | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | UNKNOWN. Suitability not presumed. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Clinical census 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven unfiltered queries on ClinicalTrials.gov API v2 returned no registered WOREE interventional study; [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | In a matched non-WWOX West-syndrome series, what fraction responds to hormonal therapy, and how many WWOX responders would that fraction already explain? | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: a defined response and a matched West-syndrome base rate. | `input.p4_roadmap_fields.status` |

### EB-CBD-AX-01 · cannabidiol · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | clinician-reported seizure control, if a response is first defined | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | Symptom, if shown. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | Inconclusive (known-roads note 2.7). | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none: continuation in 4 of 4 patients who started it in one cohort is a continuation pattern, not an efficacy measure; ineffective in one severe case | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | UNKNOWN. Suitability not presumed. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Clinical census 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven unfiltered queries on ClinicalTrials.gov API v2 returned no registered WOREE interventional study; [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Did any WWOX organoid or animal paper test cannabidiol? One registry query answers it. | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: any WWOX-system test of cannabidiol and a defined response. | `input.p4_roadmap_fields.status` |

### EB-MTOR-AX-01 · mTOR-inhibitor class · ABSTENTION · bridge `directional_summary` = UNRESOLVED

| Dimension | Cell (the card's own field, verbatim, or UNKNOWN) | Card field |
|---|---|---|
| Benefit: the ONE endpoint | UNKNOWN: no WOREE-relevant endpoint is supported for this class | `input.p4_fields.endpoint_pursued` |
| Benefit: symptomatic or modifying (card's expected contribution) | None claimed. | `input.p4_roadmap_fields.expected_contribution` |
| Evidence: state | UNKNOWN. | `input.p4_roadmap_fields.known_roads_state` |
| Evidence: functional evidence available | none in a WWOX system; the class evidence comes from genetic mTOR-pathway reduction in a Tsc1 model (NOT WWOX EVIDENCE) | `input.p4_fields.functional_evidence_available` |
| Risk (class-level, as the card carries it) | A paediatric record exists for this class in another disease; it is not an authorisation for this one and not a suitability statement. Interactions: UNKNOWN. | `input.p4_roadmap_fields.paediatrics_and_interactions` |
| BLOCK-1 status | **UNKNOWN** (no BLOCK-1 field or statement on this card; UNKNOWN is not a pass) | `(none)` |
| Time to ACCESS | UNKNOWN. Clinical census 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven unfiltered queries on ClinicalTrials.gov API v2 returned no registered WOREE interventional study; [cut: the card's field continues] | `input.p4_roadmap_fields.time_to_access` |
| Time to BENEFIT | UNKNOWN. | `input.p4_roadmap_fields.time_to_benefit` |
| Feasibility: what must exist to test it | Does the blocked WWOX/mTOR paper (full text unread) report a direction of mTOR activity in a WWOX-deficient system? | `input.p4_roadmap_fields.next_measure` |
| ABSTENTION: the missing datum | ASTENSIONE. Missing datum: a direction of mTOR activity in a WWOX system and any WOREE endpoint. | `input.p4_roadmap_fields.status` |

