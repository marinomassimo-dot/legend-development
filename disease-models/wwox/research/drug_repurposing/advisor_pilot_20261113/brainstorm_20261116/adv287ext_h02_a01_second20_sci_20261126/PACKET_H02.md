# Packet H02: card sentences to check (25). Card files: disease-models/wwox/research/drug_repurposing/cards/<card>.packet.json

## H02-02 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: 22 percent is the prevalence in the vigabatrin-treated infants of that study (non-WWOX, infantile spasms) and 4 percent the comparator on other therapies;
printed at: /drug_assertions[4]/note
  record id: "DR-H02-005"
  record target_id: "brain_MRI_abnormality"
  record source: "US prescribing information for vigabatrin oral solution (openFDA drug label JSON, version effective 2026-06-15, set id 082d818a-4f4e-4675-98c6-91db0294e63c), sections 5.3 and 5.4; NOT WWOX EVIDENCE"
  record locator: "section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies; changes generally resolved on discontinuation; section 5.4: intramyelinic edema at post-mortem in infants; vacuolation in animals at doses within the human therapeutic range with no no-effect dose established; decreased myelination and oligodendrocyte injury in treated rats; section 8.4 states that the no-effect dos
  record endpoint: "symmetric MRI signal change (thalamus, basal ganglia, brain stem, cerebellum) in infants with infantile spasms"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (not WWOX-selected)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching
  record reading_depth: "queried_not_full_read"

## H02-03 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: 25 of 81 children imaged during but not before exposure (30.9 percent) had the finding and all 12 unexposed children were normal;
printed at: /drug_assertions[31]/note
  record id: "DR-H02-032"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human children with infantile spasms, PMID 20384718; NOT WWOX EVIDENCE"
  record locator: "Younger infants (<or=12 months) and those with cryptogenic IS were more likely to develop abnormal signal changes on MRI during VGB treatment [Abstract, Results] [evidence_b1.tsv B1-41]"
  record endpoint: "rate and risk factors with an unexposed comparison group"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (107 children, 95 exposed, 12 unexposed) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy"}
  record reading_depth: "abstract_only"

## H02-04 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: 38 of 172 imaged children (22.1 percent) had the finding;
printed at: /drug_assertions[11]/note
  record id: "DR-H02-012"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human infants and children with infantile spasms, one centre, PMID 36601084; NOT WWOX EVIDENCE"
  record locator: "The study enrolled 172 children with IS who received VGB. VABAM was observed in 38 patients (22.1%) [Abstract, Results] [evidence_b1.tsv B1-01, B1-04]"
  record endpoint: "rate of the abnormality among children imaged during exposure, by aetiology"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms, tuberous sclerosis complex (80) and other causes (92) (NOT WWOX EVIDENCE)", "genotype": "not stated (aetiology groups)", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy; exposure began at or below 12 months in most"}
  record reading_depth: "partial_fulltext_read"

## H02-05 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: 4 percent of naive infants in the controlled study).
printed at: /drug_assertions[4]/note
  record id: "DR-H02-005"
  record target_id: "brain_MRI_abnormality"
  record source: "US prescribing information for vigabatrin oral solution (openFDA drug label JSON, version effective 2026-06-15, set id 082d818a-4f4e-4675-98c6-91db0294e63c), sections 5.3 and 5.4; NOT WWOX EVIDENCE"
  record locator: "section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies; changes generally resolved on discontinuation; section 5.4: intramyelinic edema at post-mortem in infants; vacuolation in animals at doses within the human therapeutic range with no no-effect dose established; decreased myelination and oligodendrocyte injury in treated rats; section 8.4 states that the no-effect dos
  record endpoint: "symmetric MRI signal change (thalamus, basal ganglia, brain stem, cerebellum) in infants with infantile spasms"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (not WWOX-selected)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching
  record reading_depth: "queried_not_full_read"

## H02-06 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: Averages as printed: 180 in control against 55 in the neuron-specific knockout (about 3.3 times fewer;
printed at: /disease_assertions[0]/note
  record id: "DA-H02-001"
  record target_id: "CNS_myelination"
  record source: "Repudi 2021 (PMID 33914858), Figure 5B and its legend, as carried by needs NEED-MYELINATION observation O1"
  record locator: "deepdive_manifests/PMID33914858.json verbatim_locators entry 0 (Results, myelination section, printed page 27 of 48); the plotted unit is the field of view, not the mouse (entries 15 to 17)"
  record endpoint: "myelinated axons per field of view in the corpus callosum (electron microscopy)"
  record direction: "DECREASE"
  record context: {"disease_id": "Wwox neuron-specific deletion (Synapsin-Cre) against control", "genotype": "Wwox conditional knockout, neuron-specific", "species": "mouse", "cell_type": "CNS axons, corpus callosum", "developmental_stage": "P17"}
  record reading_depth: "partial_fulltext_read"

## H02-07 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: Genetic epilepsy was more frequent in the VABAM-positive group (9/18, 50.0%), whereas structural epilepsy predominated in the VABAM-negative group (34/46, 73.9%) [Abstract, Results] [evidence_b1.tsv B1-11]
printed at: /drug_assertions[15]/locator
  record id: "DR-H02-016"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human children with at least two examinations before and during exposure, PMID 42735667; NOT WWOX EVIDENCE"
  record locator: "Genetic epilepsy was more frequent in the VABAM-positive group (9/18, 50.0%), whereas structural epilepsy predominated in the VABAM-negative group (34/46, 73.9%) [Abstract, Results] [evidence_b1.tsv B1-11]"
  record endpoint: "aetiology class of children with and without the abnormality"
  record direction: "UNKNOWN"
  record context: {"disease_id": "epilepsy of genetic or structural aetiology (64 children) (NOT WWOX EVIDENCE)", "genotype": "not stated (genetic aetiology in 9 of 18 positives)", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "not reported in the abstract"}
  record reading_depth: "abstract_only"

## H02-08 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: In Table 2 the exposed group with normal imaging is not significantly below controls (right median 0.463 against 0.427;
printed at: /drug_assertions[18]/note
  record id: "DR-H02-019"
  record target_id: "optic_nerve_diffusion_metric"
  record source: "vigabatrin, human children with West syndrome, PMID 40670421; NOT WWOX EVIDENCE"
  record locator: "fractional anisotropy values increased significantly after vigabatrin discontinuation (P < 0.05) [Abstract, Results] [evidence_b1.tsv B1-18]"
  record endpoint: "optic-nerve fractional anisotropy during exposure and after stopping"
  record direction: "DECREASE"
  record context: {"disease_id": "West syndrome (35 children in three groups) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "optic nerve, diffusion imaging", "developmental_stage": "9 days to 22 months at first exposure across groups"}
  record reading_depth: "partial_fulltext_read"

## H02-09 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: PubMed abstract: ERG reductions at doses 20 to 40 times those needed in the cocaine model, smaller than those with vigabatrin at the dose needed for that model
printed at: /drug_assertions[10]/locator
  record id: "DR-H02-011"
  record target_id: "retinal_function_ERG"
  record source: "CPP-115 compared with vigabatrin, rat, PMID 22128851, abstract; NOT WWOX EVIDENCE"
  record locator: "PubMed abstract: ERG reductions at doses 20 to 40 times those needed in the cocaine model, smaller than those with vigabatrin at the dose needed for that model"
  record endpoint: "electroretinogram response amplitude in rats"
  record direction: "DECREASE"
  record context: {"disease_id": "rat cocaine-addiction pharmacology (NOT WWOX EVIDENCE)", "genotype": "wild-type adult rat", "species": "rat", "cell_type": "retina", "developmental_stage": "adult"}
  record reading_depth: "abstract_only"

## H02-10 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: The sign is the plasma taurine fall under vigabatrin (67 percent lower);
printed at: /drug_assertions[36]/note
  record id: "DR-H02-037"
  record target_id: "plasma_taurine"
  record source: "vigabatrin, albino rats and mice and six exposed infants, PMID 19194884; NOT WWOX EVIDENCE"
  record locator: "These results indicate that vigabatrin generates a taurine deficiency responsible for its retinal phototoxicity [Abstract, Interpretation] [evidence_b1.tsv B1-47]"
  record endpoint: "retinal lesion components, plasma taurine, and the effect of darkness and of taurine supplementation"
  record direction: "DECREASE"
  record context: {"disease_id": "retinal toxicity (albino animals); the endpoint is retinal, not cerebral (NOT WWOX EVIDENCE)", "genotype": "albino animals", "species": "rat, mouse and human", "cell_type": "retina and plasma", "developmental_stage": "animals treated daily; infant ages not stated in the abstract"}
  record reading_depth: "abstract_only"

## H02-11 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: The spectroscopic ratio did not differ significantly between children with and without the abnormality (p = 0.31, two against eleven children);
printed at: /drug_assertions[17]/note
  record id: "DR-H02-018"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human children, PMID 35183975; NOT WWOX EVIDENCE"
  record locator: "CSF levels of free GABA were significantly higher in VABAM (5.26 ± 1.95 μmol/L) than in non-VABAM (0.59 ± 0.63 μmol/L) cases (P = 0.03) [Abstract] [evidence_b1.tsv B1-17]"
  record endpoint: "cerebrospinal and spectroscopic GABA concentration in children with and without the abnormality"
  record direction: "INCREASE"
  record context: {"disease_id": "children treated with vigabatrin (15 treated, 13 imaged, 2 with the finding) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "cerebrospinal fluid and brain spectroscopy", "developmental_stage": "not stated; both cases with the finding were very low birth weight preterm infants"}
  record reading_depth: "abstract_only"

## H02-12 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: The synthesis in 'mechanism', both registered predictions, and the comparison of a denominator-free case report with the label's 22 versus 4 percent are INFERENZA and owed a blind audit by someone other than the producer.
printed at: /p4_card/scope_of_checks/card_inferences_owed_audit
printed at: /p4_roadmap_fields/verification_scope

## H02-13 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: This row has no denominator, so it cannot be shown to exceed (or fall below) any rate, including the label's 22 percent in non-WWOX infants.
printed at: /drug_assertions[6]/note
  record id: "DR-H02-007"
  record target_id: "brain_MRI_abnormality"
  record source: "Choi 2026 (PMID 41442931), abstract only"
  record locator: "PubMed abstract: 'Brain magnetic resonance imaging during vigabatrin treatment revealed new symmetrical signal changes in the globus pallidi and thalami consistent with VABAM'; 'Further research is warranted to investigate whether children with genetic epilepsy related to the GABAergic pathway or delayed myelination are more susceptible to VABAM'"
  record endpoint: "new symmetrical MRI signal change in the globus pallidi and thalami during vigabatrin (VABAM)"
  record direction: "INCREASE"
  record context: {"disease_id": "WWOX-related epileptic encephalopathy (two children)", "genotype": "biallelic WWOX (alleles not stated in the abstract)", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (age not stated in the abstract)"}
  record reading_depth: "abstract_only"

## H02-14 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: Transient hyperintensity of basal ganglia and brainstem, maximal 3 to 6 months after the start of exposure;
printed at: /drug_assertions[32]/note
  record id: "DR-H02-033"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human infants, PMID 19258289; NOT WWOX EVIDENCE"
  record locator: "Such transient hyperintensity is likely to be age-dependent and time-dependent because it has never been observed in adult patients [Abstract, Conclusion] [evidence_b1.tsv B1-42]"
  record endpoint: "time course of the abnormality after the start of exposure"
  record direction: "INCREASE"
  record context: {"disease_id": "epileptic infants of mixed aetiology (22 infants, 34 examinations) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy"}
  record reading_depth: "abstract_only"

## H02-15 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: Two children selected for having the finding, with no denominator, cannot be shown to exceed (or fall below) the label's figures: 22 percent MRI changes in vigabatrin-treated non-WWOX infants with infantile spasms against 4 percent on other therapies (retrospective, N=205, arm sizes not stated).
printed at: /p4_card/evidence_for_and_against/against[0]
printed at: /evidence_against[0]

## H02-16 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: VABAM was observed in 38 patients (22.1%) [Abstract, Results] [evidence_b1.tsv B1-01, B1-04]
printed at: /drug_assertions[11]/locator
  record id: "DR-H02-012"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human infants and children with infantile spasms, one centre, PMID 36601084; NOT WWOX EVIDENCE"
  record locator: "The study enrolled 172 children with IS who received VGB. VABAM was observed in 38 patients (22.1%) [Abstract, Results] [evidence_b1.tsv B1-01, B1-04]"
  record endpoint: "rate of the abnormality among children imaged during exposure, by aetiology"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms, tuberous sclerosis complex (80) and other causes (92) (NOT WWOX EVIDENCE)", "genotype": "not stated (aetiology groups)", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy; exposure began at or below 12 months in most"}
  record reading_depth: "partial_fulltext_read"

## H02-17 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: by aetiology 8 of 80 with tuberous sclerosis against 30 of 92 with other causes.
printed at: /drug_assertions[11]/note
  record id: "DR-H02-012"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human infants and children with infantile spasms, one centre, PMID 36601084; NOT WWOX EVIDENCE"
  record locator: "The study enrolled 172 children with IS who received VGB. VABAM was observed in 38 patients (22.1%) [Abstract, Results] [evidence_b1.tsv B1-01, B1-04]"
  record endpoint: "rate of the abnormality among children imaged during exposure, by aetiology"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms, tuberous sclerosis complex (80) and other causes (92) (NOT WWOX EVIDENCE)", "genotype": "not stated (aetiology groups)", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy; exposure began at or below 12 months in most"}
  record reading_depth: "partial_fulltext_read"

## H02-21 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: left 0.390 against 0.410);
printed at: /drug_assertions[18]/note
  record id: "DR-H02-019"
  record target_id: "optic_nerve_diffusion_metric"
  record source: "vigabatrin, human children with West syndrome, PMID 40670421; NOT WWOX EVIDENCE"
  record locator: "fractional anisotropy values increased significantly after vigabatrin discontinuation (P < 0.05) [Abstract, Results] [evidence_b1.tsv B1-18]"
  record endpoint: "optic-nerve fractional anisotropy during exposure and after stopping"
  record direction: "DECREASE"
  record context: {"disease_id": "West syndrome (35 children in three groups) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "optic nerve, diffusion imaging", "developmental_stage": "9 days to 22 months at first exposure across groups"}
  record reading_depth: "partial_fulltext_read"

## H02-23 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: only the cerebrospinal free GABA difference (p = 0.03) and the higher ratio under the drug than in controls (p = 0.02) were significant.
printed at: /drug_assertions[17]/note
  record id: "DR-H02-018"
  record target_id: "brain_MRI_abnormality"
  record source: "vigabatrin, human children, PMID 35183975; NOT WWOX EVIDENCE"
  record locator: "CSF levels of free GABA were significantly higher in VABAM (5.26 ± 1.95 μmol/L) than in non-VABAM (0.59 ± 0.63 μmol/L) cases (P = 0.03) [Abstract] [evidence_b1.tsv B1-17]"
  record endpoint: "cerebrospinal and spectroscopic GABA concentration in children with and without the abnormality"
  record direction: "INCREASE"
  record context: {"disease_id": "children treated with vigabatrin (15 treated, 13 imaged, 2 with the finding) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "cerebrospinal fluid and brain spectroscopy", "developmental_stage": "not stated; both cases with the finding were very low birth weight preterm infants"}
  record reading_depth: "abstract_only"

## H02-24 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: recasts the WWOX VABAM signal as numerator-only (no denominator), set beside the label's 22 versus 4 percent in non-WWOX infants;
printed at: /p4_card/value_added

## H02-25 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies;
printed at: /drug_assertions[4]/locator
  record id: "DR-H02-005"
  record target_id: "brain_MRI_abnormality"
  record source: "US prescribing information for vigabatrin oral solution (openFDA drug label JSON, version effective 2026-06-15, set id 082d818a-4f4e-4675-98c6-91db0294e63c), sections 5.3 and 5.4; NOT WWOX EVIDENCE"
  record locator: "section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies; changes generally resolved on discontinuation; section 5.4: intramyelinic edema at post-mortem in infants; vacuolation in animals at doses within the human therapeutic range with no no-effect dose established; decreased myelination and oligodendrocyte injury in treated rats; section 8.4 states that the no-effect dos
  record endpoint: "symmetric MRI signal change (thalamus, basal ganglia, brain stem, cerebellum) in infants with infantile spasms"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (not WWOX-selected)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching
  record reading_depth: "queried_not_full_read"

## H02-26 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: the cited study itself was not read, so the 22 and 4 percent figures are the label's statement of it.
printed at: /drug_assertions[4]/note
  record id: "DR-H02-005"
  record target_id: "brain_MRI_abnormality"
  record source: "US prescribing information for vigabatrin oral solution (openFDA drug label JSON, version effective 2026-06-15, set id 082d818a-4f4e-4675-98c6-91db0294e63c), sections 5.3 and 5.4; NOT WWOX EVIDENCE"
  record locator: "section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies; changes generally resolved on discontinuation; section 5.4: intramyelinic edema at post-mortem in infants; vacuolation in animals at doses within the human therapeutic range with no no-effect dose established; decreased myelination and oligodendrocyte injury in treated rats; section 8.4 states that the no-effect dos
  record endpoint: "symmetric MRI signal change (thalamus, basal ganglia, brain stem, cerebellum) in infants with infantile spasms"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (not WWOX-selected)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching
  record reading_depth: "queried_not_full_read"

## H02-27 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: the diffusion coefficient did not differ significantly (right median 1209 in the finding group against 1280 in controls, left 1427 against 1366;
printed at: /drug_assertions[18]/note
  record id: "DR-H02-019"
  record target_id: "optic_nerve_diffusion_metric"
  record source: "vigabatrin, human children with West syndrome, PMID 40670421; NOT WWOX EVIDENCE"
  record locator: "fractional anisotropy values increased significantly after vigabatrin discontinuation (P < 0.05) [Abstract, Results] [evidence_b1.tsv B1-18]"
  record endpoint: "optic-nerve fractional anisotropy during exposure and after stopping"
  record direction: "DECREASE"
  record context: {"disease_id": "West syndrome (35 children in three groups) (NOT WWOX EVIDENCE)", "genotype": "not stated", "species": "human", "cell_type": "optic nerve, diffusion imaging", "developmental_stage": "9 days to 22 months at first exposure across groups"}
  record reading_depth: "partial_fulltext_read"

## H02-28 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: the direction (CPP-115 a more efficient inactivator than vigabatrin, OV329 a lower KI than CPP-115 in one same-assay pig comparison) is reproduced, the magnitude is not: two incompatible derivations of the 187-fold efficiency ratio are in print (the 2012 article attributes it to the 2003-type values, which give about 52-fold;
printed at: /p4_card/pharmacology

## H02-29 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: the neuron-specific Wwox deletion has about 3.3 times fewer myelinated callosal axons at P17.
printed at: /p4_fields/cellular_context/cells_tissue_stage

## H02-30 (card H02_gabaat_inactivator_myelin_exposure)
SENTENCE: vacuolation in animals at doses within the human therapeutic range with no no-effect dose established;
printed at: /drug_assertions[4]/locator
  record id: "DR-H02-005"
  record target_id: "brain_MRI_abnormality"
  record source: "US prescribing information for vigabatrin oral solution (openFDA drug label JSON, version effective 2026-06-15, set id 082d818a-4f4e-4675-98c6-91db0294e63c), sections 5.3 and 5.4; NOT WWOX EVIDENCE"
  record locator: "section 5.3: retrospective epidemiologic study in infants with infantile spasms (N=205), prevalence of MRI changes 22 percent with vigabatrin against 4 percent with other therapies; changes generally resolved on discontinuation; section 5.4: intramyelinic edema at post-mortem in infants; vacuolation in animals at doses within the human therapeutic range with no no-effect dose established; decreased myelination and oligodendrocyte injury in treated rats; section 8.4 states that the no-effect dos
  record endpoint: "symmetric MRI signal change (thalamus, basal ganglia, brain stem, cerebellum) in infants with infantile spasms"
  record direction: "INCREASE"
  record context: {"disease_id": "infantile spasms (not WWOX-selected)", "genotype": "not stated", "species": "human", "cell_type": "whole organism, brain MRI", "developmental_stage": "infancy (infantile spasms; the labelled indication age is 1 month to 2 years; the label does not state the age range of the N=205 study and cites no source; the study its figures match (205 infants, 22 percent against 4 percent), PMID 19054414, gives infants aged 24 months or less, an identification inferred from the three matching
  record reading_depth: "queried_not_full_read"

