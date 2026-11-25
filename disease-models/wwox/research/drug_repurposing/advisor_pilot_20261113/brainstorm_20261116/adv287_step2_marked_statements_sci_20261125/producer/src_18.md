# src_18 (card H02_gabaat_inactivator_myelin_exposure, /drug_assertions/note, DR-H02-031)

## Verbatim sentence (marked word: "none" in "none of 56 unexposed children")
7 of 22 exposed children (32 percent, after excluding the index detection) against none of 56 unexposed children with infantile spasms;

## Source pointers
- Card packet: disease-models/wwox/research/drug_repurposing/cards/H02_gabaat_inactivator_myelin_exposure.packet.json, drug_assertions[30] (id DR-H02-031; reading_depth abstract_only; receipt FTR-20261106-18783433-23), field note.
- Source: PMID 18783433, "Cerebral MRI abnormalities associated with vigabatrin therapy" (2009), Europe PMC core record held at files/fulltext/adv056_it_20261118/B/PMID18783433_x2008_europepmc_core.json. Only this abstract record is held; no full text of PMID 18783433 was found under files/fulltext (listing searched for 18783433 and Pearl). Population: human children, 23 on vigabatrin with MRI during therapy and 56 with infantile spasms not given vigabatrin; unit is the patient.
- Batch table: disease-models/wwox/research/drug_repurposing/batch_sci_20261105/b1_whitematter/evidence_b1.tsv (48 data rows, B1-01 to B1-48). The row of this source is B1-40. The rows of the same table that carry an unexposed or untreated comparison group are B1-18, B1-22, B1-35, B1-40 and B1-41 (printed whole below); a text search of all 48 rows for "unexposed", "not treated", "without vigabatrin", "not exposed" and "untreated" returned exactly these five.

## PMID 18783433 abstract (verbatim, held record)
Title: Cerebral MRI abnormalities associated with vigabatrin therapy.
Authors: Pearl PL, Vezina LG, Saneto RP, McCarter R, Molloy-Wells E, Heffron A, Trzcinski S, McClintock WM, Conry JA, Elling NJ, Goodkin HP, de Menezes MS, Ferri R, Gilles E, Kadom N, Kadom N, Gaillard WD.
Year: 2009
Abstract: <h4>Purpose</h4>Investigate whether patients on vigabatrin demonstrated new-onset and reversible T(2)-weighted magnetic resonance imaging (MRI) abnormalities.<h4>Methods</h4>MRI of patients treated during vigabatrin therapy was reviewed, following detection of new basal ganglia, thalamus, and corpus callosum hyperintensities in an infant treated for infantile spasms. Patients were assessed for age at time of MRI, diagnosis, duration, and dose, MRI findings pre-, on, and postvigabatrin, concomitant medications, and clinical correlation. These findings were compared to MRI in patients with infantile spasms who did not receive vigabatrin.<h4>Results</h4>Twenty-three patients were identified as having MRI during the course of vigabatrin therapy. After excluding the index case, we detected new and reversible basal ganglia, thalamic, brainstem, or dentate nucleus abnormalities in 7 of 22 (32%) patients treated with vigabatrin. All findings were reversible following discontinuation of therapy. Diffusion-weighted imaging (DWI) was positive with apparent diffusion coefficient (ADC) maps demonstrating restricted diffusion. Affected versus unaffected patients, respectively, had a median age of 11 months versus 5 years, therapy duration 3 months versus 12 months, and dosage 170 mg/kg/day versus 87 mg/kg/day. All affected patients were treated for infantile spasms; none of 56 patients with infantile spasms who were not treated with vigabatrin showed the same abnormalities.<h4>Discussion</h4>MRI abnormalities attributable to vigabatrin, characterized by new-onset and reversible T(2)-weighted hyperintensities and restricted diffusion in thalami, globus pallidus, dentate nuclei, brainstem, or corpus callosum were identified in 8 of 23 patients. Young age and relatively high dose appear to be risk factors.

## Batch-table rows with an unexposed or untreated comparison group (complete rows)
### B1-18
- row_id: B1-18
- role: support
- species_or_population: human, 35 children with West syndrome in three groups
- age_at_first_exposure: 9 days to 22 months across groups, medians about 5 to 6 months and not different between groups
- exposure_pattern_qualitative: oral vigabatrin; maximum daily amounts in both exposed groups below the threshold an earlier cohort proposed
- duration_class: medians about 11 months in all three groups, not different
- baseline_condition: West syndrome, no stated baseline white-matter disease
- endpoint: optic nerve fractional anisotropy and apparent diffusion coefficient
- finding: fractional anisotropy lower in the group with the deep-grey finding than in unexposed controls (p < 0.05); no difference in the exposed group without the finding; diffusion coefficient unchanged
- reversibility: fractional anisotropy rose significantly after stopping, described as normalising within three months
- cofactors: other antiseizure medicines in the control group
- direction: harm
- measure_level: MRI
- source_id: PMID40670421 (Results and Discussion)
- source_depth: partial_fulltext_read
- locator_quote: fractional anisotropy values increased significantly after vigabatrin discontinuation (P < 0.05) [Abstract, Results]
- transfer_conditions: a quantitative white-matter metric moves with exposure and recovers after stopping, which is the measurable version of the question
- transfer_breakers: 11 exposed children per group, retrospective; the optic nerve is also the retinotoxicity target, so this metric is not purely cerebral myelin

### B1-22
- row_id: B1-22
- role: counter
- species_or_population: human, 62 on long-term vigabatrin against 10 untreated comparison cases, ages not stated
- age_at_first_exposure: not stated in the abstract; the cohort is described only as refractory epilepsy before neurosurgery or death, on long-term treatment
- exposure_pattern_qualitative: long-term oral vigabatrin
- duration_class: long-term
- baseline_condition: refractory epilepsy
- endpoint: neuropathological examination for myelin microvacuolation and sheath splitting
- finding: none of the animal changes were found; no microvacuolation or sheath splitting attributable to vigabatrin; no demyelination in animal or human material
- reversibility: not applicable
- cofactors: none stated
- direction: no_harm
- measure_level: histology
- source_id: PMID1940119 (Abstract)
- source_depth: abstract_only
- locator_quote: In no case was there considered to be any evidence of myelin microvacuolation or myelin sheath splitting that could be attributed to vigabatrin treatment [Abstract]
- transfer_conditions: the rodent lesion does not transfer to the human adult brain at post-mortem
- transfer_breakers: the abstract reports no ages, so whether the myelinating window was represented at all is unknown; a sponsor-affiliated series read at abstract level

### B1-35
- row_id: B1-35
- role: context
- species_or_population: human, 80 vigabatrin-treated and 23 untreated children with tuberous sclerosis and 29 further epilepsy comparison cases
- age_at_first_exposure: infancy
- exposure_pattern_qualitative: as the source states
- duration_class: as the source states
- baseline_condition: tuberous sclerosis complex and other epilepsies
- endpoint: the MRI finding, its predictors and its resolution
- finding: vigabatrin independently associated with the finding while tuberous sclerosis and refractory epilepsy were not; the same pattern appeared in 7 of 52 untreated children; concomitant hormonal therapy was not associated with the finding but was associated with symptoms
- reversibility: the finding resolved entirely after discontinuation in all 13 treated children with a follow-up examination
- cofactors: hormonal or steroid co-therapy in eight treated children
- direction: harm
- measure_level: MRI
- source_id: PMID39641935 (held manifest, prior reading, receipt FTR-20261019-39641935-01)
- source_depth: prior_partial_fulltext_read_held
- locator_quote: Prevalence of VABAM-like MRI abnormalities not VGB-related was, therefore, 13.5% (7/52 patients) [Results 3.2.2, held manifest]
- transfer_conditions: the same imaging pattern occurs without the drug, so a WWOX child with the pattern is not thereby a drug case
- transfer_breakers: read for an earlier question by another actor; not re-read here, and the quote is carried from the held manifest

### B1-40
- row_id: B1-40
- role: support
- species_or_population: human, 23 exposed children, 7 of 22 with the finding after excluding the first-detected case, against 56 unexposed with infantile spasms
- age_at_first_exposure: not stated (the median 11 months against 5 years is the age at the time of MRI)
- exposure_pattern_qualitative: oral vigabatrin; higher peak amount and shorter therapy in those with the finding
- duration_class: median 3 months in those with the finding against 12 months in those without
- baseline_condition: mixed aetiology; all with the finding were treated for infantile spasms
- endpoint: new reversible T2 hyperintensity with restricted diffusion in basal ganglia, thalamus, brainstem, dentate nucleus or corpus callosum
- finding: 7 of 22 (32 percent) after excluding the index detection; none of 56 unexposed children with infantile spasms showed the same abnormalities
- reversibility: all findings reversible following discontinuation
- cofactors: concomitant medicines assessed; aetiology restricted to infantile spasms among those affected
- direction: harm
- measure_level: MRI
- source_id: PMID18783433 (Abstract)
- source_depth: abstract_only
- locator_quote: Young age and relatively high dose appear to be risk factors [Abstract, Conclusion]
- transfer_conditions: age and exposure intensity move together here, and duration moves the other way, which matches the intensity-not-accumulation condition
- transfer_breakers: 23 exposed children at abstract level, with the first-detected case excluded post hoc and the comparison group unimaged for the same indication

### B1-41
- row_id: B1-41
- role: support
- species_or_population: human, 107 children with infantile spasms, 95 exposed, 81 imaged during but not before exposure, 12 unexposed
- age_at_first_exposure: younger infants, 12 months or less, more likely to develop the finding
- exposure_pattern_qualitative: oral vigabatrin above a stated threshold in the exposed group
- duration_class: follow-up examinations in 15 of the 25 with the finding
- baseline_condition: cryptogenic against other aetiology
- endpoint: abnormal signal or restricted diffusion in deep grey nuclei and brainstem
- finding: 25 of 81 (30.9 percent) exhibited the finding, all 12 unexposed children were normal, and younger infants and those with cryptogenic infantile spasms were more likely to develop it
- reversibility: reversible on withdrawal in the follow-up subset; of fourteen imaged before, during and after, four had the abnormality: two reversed on cessation, one reversed without cessation and one persisted during weaning
- cofactors: aetiology; no co-therapy analysis in the abstract
- direction: harm
- measure_level: MRI
- source_id: PMID20384718 (Abstract)
- source_depth: abstract_only
- locator_quote: Younger infants (<or=12 months) and those with cryptogenic IS were more likely to develop abnormal signal changes on MRI during VGB treatment [Abstract, Results]
- transfer_conditions: a fourth independent rate with an unexposed comparator, an age signal and an aetiology signal, all three relevant to a WWOX-DEE count
- transfer_breakers: retrospective, abstract level; follow-up scans were done in 15 of 25 (reversible on withdrawal); in the separate before-during-after subset of 14, four had the abnormality and one of them reversed without stopping, so cessation is not the only route to resolution


## Abstract of PMID 20384718 (row B1-41; held Europe PMC record, verbatim)
Title: Vigabatrin-associated reversible MRI signal changes in patients with infantile spasms.
Abstract: <h4>Purpose</h4>To evaluate the magnetic resonance imaging (MRI) of pediatric patients with infantile spasms (IS) treated with vigabatrin (VGB) in order to investigate whether VGB affects the brain.<h4>Methods</h4>One hundred seven pediatric patients diagnosed with IS and treated with (n = 95) >or=120 mg/kg/day VGB or without (n = 12) VGB were included. MRI and diffusion-weighted imaging (DWI) were retrospectively analyzed.<h4>Results</h4>Of the patients who had MRI scans during, but not before, VGB treatment (n = 81), 25 (30.9%) exhibited abnormal MRI signal intensity and/or restricted DWI in the deep gray nuclei and brainstem. Follow-up scans (performed in 15 of the 25 patients) revealed that these changes were reversible upon withdrawal of the medication. Analysis of patients undergoing scans before, during, and after VGB treatment (n = 14) revealed that four patients had abnormal MRI signal during treatment with VBG, two of whom reversed with cessation of VGB, one reversed without cessation of VGB, and another had persistent abnormal signal while being weaned from the VGB. Patients who had not received VGB treatment (n = 12) displayed normal imaging. Younger infants (<or=12 months) and those with cryptogenic IS were more likely to develop abnormal signal changes on MRI during VGB treatment.<h4>Discussion</h4>In pediatric patients, VGB induces reversible MRI signal changes and reversible diffusion restriction in the globi pallidi, thalami, brainstem, and dentate nuclei. The risk for this phenomenon was greater in younger infants and patients with cryptogenic IS.

## Abstract of PMID 39641935 (row B1-35; held full text files/fulltext/PMID39641935_Stevering2025_PMC.xml, abstract converted)
ABSTRACT

## Abstract

## Objective
Previous retrospective studies have reported vigabatrin‐associated brain abnormalities on magnetic resonance imaging (VABAM), although clinical impact is unknown. We evaluated the association between vigabatrin and predefined brain magnetic resonance imaging (MRI) changes in a large homogenous tuberous sclerosis complex (TSC) cohort and assessed to what extent VABAM‐related symptoms were reported in TSC infants.

## Methods
The Dutch TSC Registry and the EPISTOP cohort provided retrospective and prospective data from 80 TSC patients treated with vigabatrin (VGB) before the age of 2 years and 23 TSC patients without VGB. Twenty‐nine age‐matched non‐TSC epilepsy patients not receiving VGB were included as controls. VABAM, specified as T2/fluid‐attenuated inversion recovery hyperintensity or diffusion restriction in predefined brain areas, were examined on brain MRI before, during, and after VGB, and once in the controls (at approximately age 2 years). Additionally, the presence of VABAM accompanying symptoms was evaluated.

## Results
Prevalence of VABAM in VGB‐treated TSC patients was 35.5%. VABAM‐like abnormalities were observed in 13.5% of all patients without VGB. VGB was significantly associated with VABAM (risk ratio [RR] = 3.57, 95% confidence interval [CI] = 1.43–6.39), whereas TSC and refractory epilepsy were not. In all 13 VGB‐treated patients with VABAM for whom posttreatment MRIs were available, VABAM entirely resolved after VGB discontinuation. The prevalence of symptoms was 11.7% in patients with VABAM or VABAM‐like MRI abnormalities and 4.3% in those without, implicating no significant association (RR = 2.76, 95% CI = .68–8.77).

## Significance
VABAM are common in VGB‐treated TSC infants; however, VABAM‐like abnormalities also occurred in children without either VGB or TSC. The cause of these MRI changes is unknown. Possible contributing factors are abnormal myelination, underlying etiology, recurrent seizures, and other antiseizure medication. Furthermore, the presence of VABAM (or VABAM‐like abnormalities) did not appear to be associated with clinical symptoms. This study confirms that the well‐known antiseizure effects of VGB outweigh the risk of VABAM and related symptoms.
Keywords: brain MRI, epilepsy, tuberous sclerosis complex, vigabatrin

## Key points
VGB is associated with characteristic brain abnormalities on MRI in infants with TSC, but these MRI lesions disappear over time.
T2/FLAIR hyperintensities in predefined areas are not exclusive for VGB or TSC, and the cause of these MRI abnormalities is unknown.
The presence of VABAM did not appear to be associated with predefined clinical symptoms.
The antiseizure effects of VGB outweigh the risk of VABAM.


## Stevering 2025 results sentence on the untreated groups (held full text, verbatim)
In two of 23 TSC patients without VGB treatment and in five of 29 epilepsy patients without TSC and VGB treatment, VABAM-like MRI abnormalities were seen on MRI at approximately 2 years of age. Prevalence of "VABAM-like MRI abnormalities not VGB-related" was, therefore, 13.5% (7/52 patients).
