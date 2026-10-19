# Interventions-themes study selection (H1-H5) for WWOX loss of function

Date: 2026-10-19. Author: read-only study selector. No repository file was edited, staged or committed. Nothing here is medical advice; this is a reading list, not evidence. Class level only: WWOX-null/KO, hypomorph, biallelic LoF (WOREE/SCAR12/DEE28), heterozygous loss.

## Method (same as the metabolic-batch selector, `disease-models/wwox/research/metabolic_batch_selection_20261019.md`)

1. Context: the template's Method/Headline; the earlier selector's finding that the working model is silent on iron, ferroptosis, catecholamines, adrenal, dopamine (term counts 0). Not re-read here: `working_model_current.md`.
2. Discovery: Europe PMC REST. WWOX-direct queries were restricted to title/abstract (`TITLE_ABS:"WWOX" OR "Wwox" OR "WOX1"`) crossed with ~60 theme terms per group (full-text matching returned only cancer-genomics noise and was discarded). Transferable queries were restricted to open-access records. PubMed MCP `search_articles` was used for the PMID of WWOX records Europe PMC lists without one. About 45 WWOX-direct records and about 450 transferable records were screened by title/abstract.
3. Dedup (mandatory): every selected PMID went through `framework/scripts/registry_records.py get --pmid <PMID> --hops 0`, then `fulltext_read_receipts.jsonl` (only `study_id.pmid` counts) and `full_text_queue_current.md`. A grep of the other `disease-models/wwox/research/*.md` files for every selected PMID found one hit (36364214, see its row). Cross-batch check against the metabolic selection file: no selected PMID is also selected there (41830506, 42047543, 33520443, 41007296, 39997753 were deliberately not re-used).
4. Identity: all PMID titles in the tables are the PubMed esummary title (NCBI E-utilities), fetched per PMID in one batch; first-author surnames were compared with the Europe PMC author strings (no mismatch). Titles are shortened only by trailing truncation.
5. Body check (test 2): Europe PMC `fullTextXML` fetched for every PMCID listed (size in kB shown; "OA XML" = HTTP 200 and above 5 kB). "PMC page only" = PMCID exists but no XML returned. Bodies were not read. Test 1 (abstract substantive) was checked by abstract length in Europe PMC core records: all selected rows pass (one candidate with an empty abstract, 40841698, was dropped).
6. Tier: 1 = WWOX-direct, or a paper that directly tests a stated model gap (iron, catecholamines, oxygen/ROS, fasting/mTOR are model gaps); 2 = WWOX-pathway or the same disease class (DEE, mitochondrial, metabolic encephalopathy); 3 = transferable review/method with one testable lesson.
7. No novelty is claimed. Absence from the registry is a statement about this repository, not about the literature.

## Headline findings for the Orchestrator

- **The literature contains no WWOX evidence at all on four of the five intervention classes.** Title/abstract searches for WWOX/Wwox/WOX1 crossed with transfusion/anaemia/haemoglobin/erythro*, adrenaline/epinephrine/catecholamine/adrenergic, plasma/albumin/immunoglobulin/complement, hyperbaric/hyperoxia/oxygen therapy, and dextrose/glucose infusion/caloric restriction/fasting returned no study that tests the intervention in a WWOX-deficient system. What exists is adjacent WWOX biology (below). Every group therefore carries a stated substitute; none of the substitutes is WWOX evidence.
- Closest WWOX-direct adjacencies found: iron/ferroptosis (two 2025-2026 papers, both without a lawful body: BLOCKED), HIF1A/ROS/hypoxia-adjacent (WWOX/HIF1A axis papers, mostly already read), serum-deprivation ROS (41677633, partial receipt), high-glucose neuronal mitochondria (35984507, partial receipt), a HAPE (high-altitude pulmonary oedema) susceptibility locus list including WWOX (38940394, BLOCKED), and zebrafish wwox-knockdown oedema (25649963, partial receipt). Sepsis/neuroinflammation with partial Wwox loss (39868255) is already completely read.
- Group substitutes: H1 = DEE-class iron/ferroptosis/anaemia plus neonatal transfusion-physiology; H2 = complement/cytokine/BBB biology in epilepsy and plasma-product use in neonates/critical illness; H3 = noradrenergic/adrenergic seizure biology, autonomic/SUDEP, hypoglycaemia counter-regulation, mitochondrial-crisis physiology; H4 = hypoxia/hyperoxia/HIF in epilepsy and neonatal brain, with the WWOX-direct ROS/HIF1A anchor; H5 = fasting/calorie-restriction mTOR-AMPK seizure biology, neonatal hypoglycaemia, parenteral/dextrose safety, refeeding, fluid/sodium and cerebral oedema, Glut1 deficiency as the nearest "brain glucose supply" analogue.
- The working model is silent on iron, catecholamines and adrenal axis (earlier term counts: 0), so H1 and H3 read into unmodelled territory; H4 and H5 touch existing lines (WWOX/HIF1A, hypoglycaemia lethality of the null mouse, ketogenic responders).
- One declared-read caution (declaration is not attestation): 36364214 (WWOX ROS senescence) is named as "already read" in a discovery-ledger agenda line but has no receipt and its registry record is `not_processed`; it is selected as new.

### Already fully read, EXCLUDED (receipt at complete depth, or registry-declared full read)

| PMID | First author, year | Why it came up |
|---|---|---|
| 39868255 | De La Cruz 2025 | Partial Wwox loss, sepsis and neuroinflammation (H2); latest receipt complete |
| 38563965 | Zeng 2024 | Endothelial WWOX knockdown, inflammation (H2); complete |
| 33058734 | Zeng 2021 | Cigarette/nicotine vapour downregulates lung WWOX (H3 adjacency); complete |
| 41090157 | Hussain 2025 | B-cell Wwox deletion, proinflammatory signature (H2); complete |
| 40507943 | Hsu 2025 | Hyaluronan, cancer and neural diseases (H2); complete |
| 34214506 | Saadane 2021 | Photoreceptor oxidative stress, WWOX (H4); declared complete full text |
| 33919646 | Spagnoli 2021 | Neonatal-onset DEE with movement disorders (H3/H1); latest receipt complete |
| 36828035 | Hussain 2023 | P47T mouse (H2/H4) |
| 30290271 | Hussain 2019 | GABAergic interneurons |
| 32000863 | Cheng 2020 | GSK3B seizure (H5) |
| 42092735 | Serce Pehlevan 2026 | Neonatal parkinsonism (H3, dopamine) |
| 18487609 | Aqeilan 2008 | Null-mouse hypoglycaemia lethality (H5) |
| 21075834 | O'Keefe 2011 | Drosophila respiration/ROS (H4) |
| 25012504, 29724996, 30755385 | Abu-Remaileh 2014/2018/2019 | WWOX/HIF1A glucose (H4/H5) |

## Group H1 blood (red-cell) transfusion: anaemia, iron, haemoglobin, oxygen-carrying capacity

**WWOX-direct evidence on transfusion, anaemia, haemoglobin or red cells: none.** Substitute (stated, not WWOX evidence): iron/ferroptosis in epilepsy and myelination (the working model is silent on iron), anaemia-epilepsy associations, and neonatal transfusion-physiology (tissue oxygenation). Count: 14.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 40808923 | Xu 2025 | Ferroptosis and epilepsy: bidirectional pathogenic links and therapeutic implications. | Maps iron-dependent lipid peroxidation both as cause and consequence of seizures; the nearest frame for a model that has no iron line | PMC12344419 (OA XML 163k) | new | 1 |
| 42712566 | Sinha 2026 | Effect of iron supplementation on brain myelination and neurodevelopmental outcomes in children aged 0-3 years: a systematic review | Iron and myelination in infancy; tests whether iron status could modulate the hypomyelination recorded in WWOX-null models | PMC13550114 (OA XML 87k) | new | 1 |
| 37124220 | Jin 2023 | Targeting ferroptosis as novel therapeutic approaches for epilepsy. | Ferroptosis targets (GPX4, iron chelation) in epilepsy models; target list to compare with WWOX-linked ferroptosis reports | PMC10133701 (OA XML 141k) | new | 2 |
| 39239479 | Porras 2024 | Ablation of Iron Regulatory Protein 2 produces a neurological disorder characterized by motor, somatosensory, and executive dysfunction... | Neuro-phenotype of brain iron misregulation in a null mouse: comparator for a Wwox-null phenotype | PMC11372806 (OA XML 165k) | new | 2 |
| 34909297 | Padda 2021 | Association of Anemia With Epilepsy and Antiepileptic Drugs. | Anaemia is a recorded epilepsy comorbidity, largely drug-associated; separates disease from treatment effects | PMC8653853 (OA XML 51k) | new | 2 |
| 41293173 | Garcia-Delgado 2025 | Impact of iron chelation therapy on mitochondrial function, vascular integrity and inflammation in transfusion-dependent... | What transfusional iron does to mitochondria/endothelium and what chelation reverses; mitochondria is the nearest WWOX-null axis | PMC12640865 (OA XML 102k) | new | 2 |
| 42794294 | Fitz 2026 | Iron Supplementation and Neurodevelopmental Outcomes in Infancy and Early Childhood: A Review. | Iron exposure versus neurodevelopmental outcome; shows the benefit/harm window | PMC13605664 (OA XML 215k) | new | 2 |
| 37733345 | Chock 2023 | Tissue Oxygenation Changes After Transfusion and Outcomes in Preterm Infants: A Secondary Near-Infrared Spectroscopy Study... | Whether brain/tissue oxygenation measurably rises after transfusion; the measurable endpoint for any carrying-capacity question | PMC10514737 (OA XML 114k) | new | 3 |
| 42313692 | Bailey 2026 | The Effect of Liberal versus Restrictive Haemoglobin Thresholds on Cerebral Tissue Oxygenation in Preterm Infants: A Systematic Review... | Threshold effects on cerebral oxygenation; shows which readout moves | PMC13441262 (OA XML 90k) | new | 3 |
| 38463073 | Shafique 2024 | Transfusion strategies for neonates: current perspectives. | Neonatal transfusion practice and risk summary | PMC10923393 (OA XML 156k) | new | 3 |
| 41904698 | Nguyen 2026 | Beyond hemoglobin thresholds: A physiology-guided framework for red blood cell transfusion in non-bleeding critically ill patients | Physiology-based rather than threshold-based transfusion reasoning; a framework to apply to a hypomorph question | PMC13067254 (OA XML 97k) | new | 3 |
| 42794205 | De Rose 2026 | Transfusion Burden in Neonates with Hypoxic-Ischemic Encephalopathy Undergoing Therapeutic Hypothermia. | Transfusion exposure in an encephalopathic neonatal population | PMC13605100 (OA XML 97k) | new | 3 |
| 39712732 | Jadhav 2024 | Association of Iron Deficiency Anaemia With the First Episode of Febrile Seizure in Children. | Iron-deficiency anaemia and seizure threshold in children | PMC11662512 (OA XML 56k) | new | 3 |
| 32685205 | Arsyad 2020 | Long-Term Ketogenic Diet Induces Metabolic Acidosis, Anemia, and Oxidative Stress in Healthy Wistar Rats. | Anaemia as a diet-treatment side effect; ties H1 to the ketogenic responders already in the model | PMC7341377 (OA XML 72k) | new | 3 |

### HELD with a partial receipt (not selected)

| PMID | Note |
|---|---|
| 40875931 | Gao 2025 (WWOX DEE clinical spectrum): latest partial receipt FTR-20260804-40875931-02; owed = figures (captions only), supplementary (unavailable). Only worth reopening with a question such as "does any cohort record haemoglobin, anaemia or transfusion?" |
| 36537114 | Chong 2023 (WWOX epileptic encephalopathy): partial receipt FTR-20260929-36537114-02; most sections unavailable (non-open-access, Scholar Gateway chunks). Not recommended without an acquired body. |

### BLOCKED (no lawful body found)

| PMID | Note |
|---|---|
| 41443103 | Wang 2026, WWOX and ferroptosis in acute lung injury via p53 deacetylation: no PMCID, publisher DOI only; registry stub `not_processed`. Closest WWOX-direct iron/ferroptosis record. |
| 39894307 | Yang 2025, WWOX-mediated p53/SAT1 and NRF2/FPN1 axis in toosendanin-induced ferroptosis (HCC): no PMCID; FPN1 = ferroportin, the iron exporter. |
| 39955305 | Not blocked but not selected: Luo 2025, WWOX is one of seven genes in a cell-death signature (abstract mention only). |

### Questions this batch could change

1. Does a model with no iron line need one? Does WWOX loss alter ferroptosis susceptibility in neurons (two lung/liver WWOX papers say it is protective), and is that testable from a brain-iron readout?
2. Is hypomyelination in WWOX-null modifiable by iron status, or is iron irrelevant to the mechanism (Sinha 2026, Fitz 2026)?
3. If tissue oxygen delivery is the endpoint, which readout moves after transfusion in infants (NIRS, Chock 2023, Bailey 2026) and would any of it be detectable in a mitochondrially stressed brain?
4. Does transfusional iron overload damage mitochondria (Garcia-Delgado 2025) in a way that overlaps with the WWOX respiratory-complex findings?
5. Is the anaemia-epilepsy association driven by disease or by antiseizure drugs (Padda 2021), and which applies to a DEE population?

## Group H2 plasma, fresh frozen plasma, plasma exchange, albumin, IVIG

**WWOX-direct evidence on plasma, FFP, plasma exchange, albumin or IVIG: none.** Substitute (stated, not WWOX evidence): complement and cytokine biology in epilepsy, albumin/BBB effects, and clinical use of plasma products in neonates and critical illness. One WWOX-direct inflammation record is selected as the nearest anchor (psoriasis, NF-kB). Count: 16.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 38203337 | Shin 2023 | Mechanistic Investigation of WWOX Function in NF-kB-Induced Skin Inflammation in Psoriasis. | WWOX-direct: WWOX expression versus NF-kB inflammatory signalling and cytokines (non-neural) | PMC10779412 (OA XML 132k) | new (registry stub, no receipt) | 1 |
| 42652171 | Karayanni 2026 | Targeting the Complement-Microglia Axis for Neuroprotection in Pediatric Epilepsy. | Complement-microglia axis in paediatric epilepsy; the model records microglial activation but nothing on complement | PMC13509543 (OA XML 122k) | new | 1 |
| 41118244 | Jeong 2026 | C1q neutralization during epileptogenesis attenuates complement-mediated synaptic elimination and epileptiform activity. | Complement tag on synapses as a mechanism; a circulating-factor-sensitive pathway | PMC12927691 (OA XML 128k) | new | 1 |
| 39934240 | Pinzon-Hoyos 2025 | Drug-resistant epilepsy associated with peripheral complement decreases and sex-specific cytokine imbalances: a pilot study | Human peripheral complement and cytokines in epilepsy: the readout a plasma product would perturb | PMC11814292 (OA XML 153k) | new | 1 |
| 39055621 | Wang 2024 | Application of peripheral blood cytokine and immunoglobulin detection in ACTH therapy for the treatment of infantile spasms | Cytokine/immunoglobulin profile in an infantile epileptic encephalopathy; same disease class | PMC11270505 (OA XML 92k) | new | 2 |
| 41346378 | Jiang 2025 | Dynamic astrocytic complement C3 activation in the epileptic hippocampus. | Astrocytic C3 over time in epilepsy; neuroinflammation arm | PMC12672298 (OA XML 114k) | new | 2 |
| 37234916 | Veremeyko 2023 | Complement C4-deficient mice have a high mortality rate during PTZ-induced epileptic seizures... | Complement loss is not protective: a counter-lesson for any complement-lowering intervention | PMC10206007 (OA XML 162k) | new | 2 |
| 42064976 | Ebdalla 2026 | Efficacy of intravenous immunoglobulin in children with drug-resistant epilepsy. | Direct clinical use of IVIG in paediatric refractory epilepsy | PMC13127252 (OA XML 108k) | new | 2 |
| 39006838 | Hu 2024 | Col4a2 Mutations Contribute to Infantile Epileptic Spasm Syndrome and Neuroinflammation. | Neuroinflammation in a genetic infantile epilepsy model; disease-class comparator | PMC11241092 (OA XML 105k) | new | 2 |
| 41591075 | Suleymanova 2025 | The Role of Blood-Brain Barrier Disruption in Epilepsy: Mechanisms and Consequences. | BBB leakage lets albumin and plasma factors reach the parenchyma | PMC12845512 (OA XML 428k) | new | 2 |
| 36606305 | Preininger 2023 | Blood-brain barrier dysfunction promotes astrocyte senescence through albumin-induced TGF-beta signaling activation... | Albumin as an astrocyte-activating factor | PMC9924950 (OA XML 171k) | new | 2 |
| 42509933 | Sahin 2026 | Therapeutic Plasma Exchange in Critically Ill Children with Neuroimmunological Disorders: A Single-Center Cohort Study. | Practice, indications and adverse-event profile of plasma exchange in children | PMC13407348 (OA XML 121k) | new | 3 |
| 41393164 | Zamith 2025 | Plasma Exchange Transfusion for Refractory High Anion Gap Metabolic Acidosis. | Plasma exchange used in a metabolic crisis | PMC12698179 (OA XML 47k) | new | 3 |
| 33238649 | Houben 2020 | Changes in the Use of Fresh-Frozen Plasma Transfusions in Preterm Neonates: A Single Center Experience. | Neonatal FFP indications and trends | PMC7700187 (OA XML 77k) | new | 3 |
| 42769206 | Tang 2026 | Effect of fresh-frozen plasma transfusion on intraventricular hemorrhage risk in preterm infants with prolonged APTT: a... | FFP and IVH risk in neonates (safety literature) | PMC13590724 (OA XML 158k) | new | 3 |
| 36719667 | Abergel 2023 | Fresh Frozen Plasma Increases Hemorrhage in Blunt Traumatic Brain Injury and Uncontrolled Hemorrhagic Shock. | FFP increased haemorrhage in a TBI model (safety literature) | PMC9888485 (OA XML 79k) | new | 3 |

Not selected, for the record: 39523291 (dialysis in inborn errors, review: relevant to H2 crises but dialysis is not plasma); 41721191 (plasma-rejuvenation perspectives: no epilepsy data).

### HELD with a partial receipt

None relevant. (31543760 and 33919646 are not plasma-related.)

### BLOCKED

| PMID | Note |
|---|---|
| 36621327 | Wang 2023, WWOX activates autophagy in LPS lung injury via mTOR: queued in `full_text_queue_current.md`, no PMCID, body unavailable (queue says unread). WWOX-direct inflammation/mTOR; also relevant to H5. |
| 41014440 | Riva 2025, pathophysiological mechanisms of DEE (inflammation review): no PMCID; Europe PMC lists no free body. |

### Questions this batch could change

1. Which circulating-factor pathways (complement C1q/C3, cytokines, albumin) are plausibly active in a WWOX-null brain with documented microglial activation, and is there any readout that distinguishes a plasma-borne from a locally produced factor?
2. Does the sepsis/neuroinflammation sensitivity of partial Wwox loss (already read, 39868255) make complement a candidate mediator? Complement-lowering is not protective in C4-null mice (37234916): is the sign of the effect uncertain?
3. What is the clinical evidence base for IVIG or plasma exchange in refractory paediatric epilepsy (Ebdalla 2026, Sahin 2026), and does any of it cover genetic DEE rather than immune epilepsy?
4. Does BBB leakage (41591075) matter in WWOX-null models, and is albumin-driven astrocyte activation (36606305) a testable link?
5. In a metabolic crisis, what is the documented place of plasma exchange (41393164) compared with dialysis and glucose?

## Group H3 adrenaline/epinephrine and adrenergic stimulation

**WWOX-direct evidence on adrenaline, epinephrine, catecholamines or adrenergic signalling: none.** The WWOX-adjacent facts are indirect: steroidogenic/adrenal arm already read (18974271), neonatal parkinsonism case with dopamine/neurotransmitter differential already read (42092735). Substitute (stated): adrenergic seizure biology, autonomic dysfunction/SUDEP, hypoglycaemia counter-regulation, epinephrine and mitochondria/lactate. Count: 14.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 35339181 | Biagioni 2023 | Noradrenaline and Seizures: A Perspective on the Role of Adrenergic Receptors in Limbic Seizures. | Receptor-subtype map of adrenergic effects on seizures; fills a model gap (catecholamines term count 0) | PMC10556380 (OA XML 53k) | new | 1 |
| 38073616 | Sitnikova 2023 | Adrenergic mechanisms of absence status epilepticus. | Adrenergic signalling in status epilepticus | PMC10703303 (OA XML 139k) | new | 1 |
| 40183510 | Sugiyama 2025 | Decreased homovanillic acid and 5-hydroxyindoleacetic acid levels in the cerebrospinal fluid of patients with Dravet syndrome... | Monoamine metabolites in a DEE; a CSF panel comparable to a WWOX neurotransmitter work-up | PMC12163531 (OA XML 65k) | new | 1 |
| 32905056 | Conlon 2020 | Hypoglycemia is not a defining feature of metabolic crisis in mitochondrial 3-hydroxy-3-methylglutaryl-CoA synthase deficiency. | Mitochondrial-disease metabolic crisis without hypoglycaemia; tests assumptions about the glucose/counter-regulation signal | PMC7463059 (OA XML 50k) | new | 2 |
| 39505840 | Sun 2024 | Enhancing glymphatic fluid transport by pan-adrenergic inhibition suppresses epileptogenesis in male mice. | Adrenergic inhibition and epileptogenesis via glymphatic flow | PMC11541706 (OA XML 229k) | new | 2 |
| 36686527 | Bauer 2022 | Autonomic dysfunction in epilepsy mouse models with implications for SUDEP research. | Autonomic/sympathetic measures in genetic epilepsy mice | PMC9853197 (OA XML 300k) | new | 2 |
| 41584903 | Wenker 2026 | Unraveling SUDEP: Mechanisms of Seizure-Induced Cardiac and Respiratory Impairment. | Seizure-linked cardiorespiratory failure; relevant to catecholamine surge | PMC12823373 (OA XML 136k) | new | 2 |
| 38397994 | Holzen 2024 | Hypoglycemia Unawareness-A Review on Pathophysiology and Clinical Implications. | Counter-regulatory (epinephrine) blunting; the null mouse dies hypoglycaemic | PMC10887081 (OA XML 119k) | new | 2 |
| 38542290 | Oulehri 2024 | NButGT Reinforces the Beneficial Effects of Epinephrine on Cardiac Mitochondrial Respiration, Lactatemia and Cardiac Output... | Epinephrine's effects on mitochondrial respiration and lactate | PMC10970273 (OA XML 125k) | new | 3 |
| 39000139 | Zhang 2024 | Chronic Epinephrine-Induced Endoplasmic Reticulum and Oxidative Stress Impairs Pancreatic beta-Cells Function and Fate. | Chronic epinephrine produces ER and oxidative stress; the ROS arm | PMC11241606 (OA XML 102k) | new | 3 |
| 39597089 | Williams 2024 | Use of Epinephrine in Cardiac Arrest: Advances and Future Challenges. | Epinephrine and neurological outcome after arrest (safety literature) | PMC11596809 (OA XML 175k) | new | 3 |
| 42260675 | Idrees 2026 | Evaluating intramuscular epinephrine in pediatric out-of-hospital cardiac arrest (the PRIME trial): study protocol... | Paediatric epinephrine trial design (route, timing) | PMC13471612 (OA XML 116k) | new | 3 |
| 41885587 | Dhillon 2026 | Alpha-adrenergic mediated changes in blood pressure variability after hypoxia-ischaemia in preterm fetal sheep. | Alpha-adrenergic effects in the injured developing brain | PMC13082192 (OA XML 160k) | new | 3 |
| 41169199 | Li 2026 | Beta 2-adrenergic pathway combats Alzheimer's disease: Restoring cognition and synaptic integrity. | Beta-2 receptor effects on synapses in a neurological disease model | PMC13568679 (OA XML 372k) | new | 3 |

Cross-reference: 35134125 (AMPK, hypoglycaemia-provoked spike-wave seizures) is listed under H5 and bears on H3 as well. Not eligible: the Dravet locus-coeruleus norepinephrine paper has a PMC id (PMC13648387) but no PMID in PubMed (preprint record).

### HELD with a partial receipt

| PMID | Note |
|---|---|
| 31543760 | Kosla 2019 (WWOX in neuronal differentiation of human neural progenitors): partial; owed = abstract, introduction, references not read; figures captions only. Pathway-level, no adrenergic content known. Not recommended without a stated question. |

### BLOCKED

None found for H3 (no WWOX-direct candidate exists to block).

### Questions this batch could change

1. Does the model need an adrenal/catecholamine line at all? WWOX has a steroidogenic arm (already read) but nothing on catecholamines.
2. Is hypoglycaemia lethality in the null (already read) accompanied by a counter-regulatory (epinephrine) failure, and is "hypoglycaemia unawareness" biology (38397994) a usable template?
3. Which adrenergic receptor subtypes raise or lower seizure threshold (35339181, 38073616), and does the answer differ in a DEE with interneuron loss (30290271, already read)?
4. Does epinephrine act on mitochondria and lactate (38542290) in a way that interacts with a WWOX respiratory-complex deficit?
5. Is there a CSF monoamine pattern in WWOX encephalopathy comparable to the Dravet pattern (40183510) and the neonatal parkinsonism case (42092735, read)?

## Group H4 oxygen: supplemental oxygen, hypoxia/hyperoxia, intermittent hypoxia, HBO, oxidative stress, HIF1A

**WWOX-direct evidence on oxygen as an intervention (supplemental, hyperbaric, nocturnal CPAP, intermittent hypoxia): none.** WWOX-direct adjacency that does exist: the WWOX/HIF1A axis (mostly read), ROS-dependent senescence (36364214), serum-deprivation ROS (41677633, partial), a HAPE locus list (38940394, BLOCKED), OSA susceptibility gene list (39087877, WWOX is one of seven genes). Substitute (stated, not WWOX evidence): hypoxia/hyperoxia/HIF biology in epilepsy and developing brain. Count: 16.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 36364214 | Liu 2022 | WWOX Modulates ROS-Dependent Senescence in Bladder Cancer. | WWOX-direct: WWOX controls ROS and senescence; the ROS arm for oxidative stress. Declared read in an agenda line, no receipt | PMC9657618 (OA XML 76k) | `not_processed` stub; no receipt | 1 |
| 42420651 | Garg 2026 | Hypoxia rescues complex 1-associated disease caused by proteostatic defects. | Hypoxia as therapy in a complex I disease; WWOX loss is reported to moderate respiratory complexes (Choo 2015, unavailable) | PMC13489956 (OA XML 162k) | new | 1 |
| 39087877 | Zhao 2025 | Novel susceptibility genes and biomarkers for obstructive sleep apnea: insights from genetic and inflammatory proteins. | WWOX named among seven OSA-susceptibility genes (abstract mention only); intermittent-hypoxia disease | PMC11808066 (OA XML 148k) | new | 2 |
| 26578889 | Lopez-Ramos 2015 | Role of brain glycogen in the response to hypoxia and in susceptibility to epilepsy. | Glycogen buffers hypoxia and sets seizure susceptibility; joins H4 to the GSK3B arm | PMC4621300 (OA XML 93k) | new | 2 |
| 38074156 | Ma 2023 | Intermittent hypoxia: linkage between OSAS and epilepsy. | Intermittent hypoxia as an epilepsy mechanism | PMC10701596 (OA XML 339k) | new | 2 |
| 37726428 | Villa 2023 | Repeated episodes of postictal hypoxia are a mechanism for interictal cognitive impairments. | Seizure-induced hypoxia as the harm; clarifies why oxygen is discussed | PMC10509159 (OA XML 76k) | new | 2 |
| 37876811 | Liang 2023 | The role of HIF-1alpha/HO-1 pathway in hippocampal neuronal ferroptosis in epilepsy. | HIF1A in epileptic neurons, linking H1 iron to H4 | PMC10590818 (OA XML 146k) | new | 2 |
| 41324728 | Kuang 2025 | The Role of HIF-1alpha/BNIP3 Pathway in Hippocampal Neuronal Autophagy in Epilepsy. | HIF1A and autophagy in epilepsy, the neural HIF1A biology missing from the fibroblast/liver arc | PMC12669306 (OA XML 159k) | new | 2 |
| 41039661 | Huang 2025 | MeCP2 at the crossroads of hypoxia, oxidative stress, and gene regulation in Rett syndrome. | Developmental-encephalopathy comparator in which hypoxia and oxidative stress are central | PMC12674224 (OA XML 178k) | new | 2 |
| 42428241 | Khaksari 2026 | Impaired task-dependent cerebral cortex oxygenation in Glut1 deficiency. | Cortical oxygenation measured in a brain-energy disorder; a measurable oxygen readout in a DEE analogue | PMC13346240 (OA XML 88k) | new | 2 |
| 28119904 | Perrone 2016 | Oxygen Use in Neonatal Care: A Two-edged Sword. | Benefit/harm of oxygen in neonates | PMC5220090 (OA XML 102k) | new | 3 |
| 40022130 | Serdar 2025 | Prenatal inflammation exacerbates hyperoxia-induced neonatal brain injury. | Hyperoxia injures the developing brain, worse with inflammation (the P47T mouse shows neuroinflammation) | PMC11871844 (OA XML 205k) | new | 3 |
| 42763430 | Moore 2026 | Hyperoxia Inhibits the Growth of Mouse Forebrain Oligodendrocyte Progenitors but Promotes Their Differentiation. | Oxygen effect on oligodendrocyte lineage (hypomyelination link) | PMC13596923 (OA XML 157k) | new | 3 |
| 42652189 | Alekseeva 2026 | Distinct Roles of NMDA and AMPA Receptors in the Pathogenesis of Hyperbaric Oxygen-Induced Seizures. | Hyperbaric oxygen can itself provoke seizures (safety literature) | PMC13509269 (OA XML 135k) | new | 3 |
| 39965572 | Blume 2025 | HypoxyStat, a small-molecule form of hypoxia therapy that increases oxygen-hemoglobin affinity. | Chemical route to the same lever as H1 (haemoglobin affinity) and H4 | PMC12186697 (OA XML 110k) | new | 3 |
| 38206902 | June 2024 | Acute seizure activity in neonatal inflammation-sensitized hypoxia-ischemia in mice. | Neonatal seizures after hypoxia-ischaemia with an inflammatory hit | PMC10783742 (OA XML 141k) | new | 3 |

### HELD with a partial receipt

| PMID | Note |
|---|---|
| 41677633 | Su 2026 (WWOX induced by serum deprivation/oxidative stress; Bcl-xL/Mcl-1): FTR-20261003-41677633-02; owed = figures captions only. WWOX-direct ROS under nutrient stress, also H5. A re-read needs a question on the ROS panel. |
| 25649963 | Tsuruwaka 2015 (zebrafish wwox knockdown, oedema, Ca2+): FTR-20261003-25649963-02; owed = references, no supplementary present. Relevant to H5 fluid/oedema too. |
| 35984507 | Carvalho 2022 (Zfra1-31, mitochondrial homeostasis, high glucose): FTR-20260921-35984507-02; owed = figure captions only. Also H5. |
| 37897534 | Cheng 2023 (loss of WWOX, senescence escape): FTR-20261004-37897534-02; abstract, introduction, references not read. Not recommended without a question. |
| 35328751, 42589397 | WWOX/HIF1A papers (Baryla 2022; Hammouz 2026): partial, same status as in the metabolic batch; not repeated. |

### BLOCKED

| PMID | Note |
|---|---|
| 38940394 | Zhao 2024, HAPE susceptibility loci including WWOX: no PMCID; the only link is a publisher DOI (subscription not verified). |
| 26390919 | Choo 2015, WWOX moderates the mitochondrial respiratory complex: queued, no PMCID; recorded elsewhere as unrecoverable. |

### Questions this batch could change

1. Does the WWOX/HIF1A axis (read) predict that a Wwox-null or hypomorphic neuron responds differently to hypoxia or hyperoxia than a normal one, and is neural HIF1A (41324728, 37876811) measurable in the existing mouse tissue?
2. Is ROS the intermediate (36364214, 41677633) between WWOX loss and mitochondrial stress, and what would a ROS readout in a null neuron predict for an oxygen exposure?
3. Is nocturnal or ictal hypoxia (37726428, 38074156) a real part of the DEE phenotype, as opposed to a feature of other epilepsies? Is there any oximetry or sleep-study data in a WWOX encephalopathy cohort?
4. Does hyperoxia perturb oligodendrocyte maturation (42763430) in a model that is already hypomyelinated?
5. Hypoxia rescues complex I disease in one system (42420651). Does anything similar apply when the defect is a possible respiratory-complex modulator (WWOX), or is the result specific to proteostasis?

## Group H5 hypocaloric diet with dextrose solution and large fluid volumes

**WWOX-direct evidence on glucose infusion, dextrose, hypocaloric/very-low-calorie feeding or fluid load: none.** Closest WWOX-direct facts are already read or held (null-mouse hypoglycaemia lethality 18487609, GSK3B 32000863, WWOX/HIF1A glucose papers; high-glucose neuronal mitochondria 35984507 held; serum deprivation 41677633 held; zebrafish oedema 25649963 held; autophagy/mTOR in LPS lung injury 36621327 blocked). Substitute (stated, not WWOX evidence): fasting/calorie-restriction mTOR-AMPK seizure biology, neonatal hypoglycaemia, dextrose and parenteral nutrition safety, refeeding, fluid/sodium and cerebral oedema, Glut1 deficiency as brain-glucose analogue. Count: 16.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 36044864 | Yuskaitis 2022 | DEPDC5-dependent mTORC1 signaling mechanisms are critical for the anti-seizure effects of acute fasting. | Fasting's anti-seizure effect needs intact mTORC1 control; tests the mTOR route for a fasting rationale | PMC9508617 (OA XML 188k) | new | 1 |
| 25814935 | Phillips-Farfan 2015 | Caloric restriction protects against electrical kindling of the amygdala by inhibiting the mTOR signaling pathway. | Calorie restriction lowers kindling via mTOR; direct test of the calorie lever | PMC4356078 (OA XML 89k) | new | 1 |
| 35134125 | Salvati 2022 | AMPK-mediated potentiation of GABAergic signalling drives hypoglycaemia-provoked spike-wave seizures. | Hypoglycaemia provokes seizures via AMPK-GABA; fits a model with interneuron loss and hypoglycaemic null mice | PMC9337815 (OA XML 200k) | new | 1 |
| 42360174 | Hahn 2026 | Intermittent fasting with medium-chain triglycerides in drug-resistant epilepsy: A pilot crossover trial. | Human fasting-with-MCT trial in refractory epilepsy | PMC13592486 (OA XML 108k) | new | 2 |
| 40589985 | Sun 2025 | Effect of visual stimulation on epilepsy susceptibility in neonatal hypoglycemic brain injury rats during development. | Neonatal hypoglycaemic brain injury raises later epilepsy susceptibility | PMC12206811 (OA XML 93k) | new | 2 |
| 40119223 | Garg 2025 | Exploring the long-term impacts of neonatal hypoglycemia to determine a safe threshold for glucose concentrations. | Glucose-threshold evidence and uncertainty in neonates | PMC11928350 (OA XML 75k) | new | 2 |
| 42638834 | Sobrinho 2026 | Glucose Transporter Deficiency Syndrome Type 1 (Glut1-DS): New Insights From a Brazilian Cohort of Patients. | Glut1-DS cohort: brain glucose supply failure, seizure phenotype and diet response | PMC13500214 (OA XML 126k) | new | 2 |
| 36117414 | Dienel 2023 | Potential new roles for glycogen in epilepsy. | Brain glycogen and epilepsy; links H5 to the GSK3B arm | PMC10952408 (OA XML 292k) | new | 2 |
| 38681648 | Tao 2024 | Wernicke encephalopathy induced by glucose infusion: A case report and literature review. | Glucose infusion without thiamine as a recorded cause of encephalopathy (safety literature) | PMC11053267 (OA XML 56k) | new | 2 |
| 42087252 | Funayama 2026 | Parenteral dextrose during refeeding is associated with electrolyte deficiencies in anorexia nervosa: a route-specific analysis | Dextrose-route electrolyte shifts in refeeding (safety literature) | PMC13312573 (OA XML 272k) | new | 3 |
| 39871710 | Abbas 2025 | Prevention of refeeding syndrome: Evaluation of an enteral refeeding protocol for severely undernourished children. | Paediatric refeeding protocol | PMC11959107 (OA XML 113k) | new | 3 |
| 42384016 | Trico 2026 | Ketone Bodies Derived From Medium-Chain Triglycerides Support Brain Metabolism and Function Under Hypoglycemia in Type 1 Diabetes... | Ketones as an alternative fuel during hypoglycaemia | PMC13493211 (OA XML 120k) | new | 3 |
| 41069084 | Burst 2026 | Severe Hyponatremia in the Emergency Department Incidence of Cerebral Edema and Risk of Osmotic Demyelination Syndrome. | Cerebral oedema and osmotic demyelination with hyponatraemia (safety literature for dilute fluid loads) | PMC12820600 (OA XML 141k) | new | 3 |
| 40944047 | Ziaka 2025 | A Comprehensive Review of Fluid Resuscitation Strategies in Traumatic Brain Injury. | Fluid type/volume effects on brain oedema | PMC12428941 (OA XML 382k) | new | 3 |
| 39861362 | Tesser 2025 | Early Optimal Parenteral Nutrition During NICU Stay and Neurodevelopmental Outcomes in Very Preterm Infants: State of the Art... | Parenteral nutrition quantity versus neurodevelopment | PMC11767679 (OA XML 168k) | new | 3 |
| 36235546 | Morris 2022 | Randomized Trial of Early Enhanced Parenteral Nutrition and Later Neurodevelopment in Preterm Infants. | Randomised comparison of nutrition dose and outcome | PMC9570539 (OA XML 125k) | new | 3 |

### HELD with a partial receipt

| PMID | Note |
|---|---|
| 35984507 | Carvalho 2022 (Zfra1-31 and high glucose): FTR-20260921-35984507-02; figure captions only. Directly about neurons under glucose load. Re-read only to tabulate the glucose concentrations used. |
| 41677633 | Su 2026 (serum deprivation, ROS in Wwox+/+ versus -/- MEFs): FTR-20261003-41677633-02; figure captions only. The only WWOX-direct fasting-like stress paper; shared with H4. |
| 25649963 | Tsuruwaka 2015 (zebrafish oedema and Ca2+): references not read. |
| 35328751 | Baryla 2022 (WWOX/HIF1A, glucose metabolism): partial, same as in the metabolic batch. |

### BLOCKED

| PMID | Note |
|---|---|
| 36621327 | Wang 2023, WWOX/mTOR autophagy (LPS lung injury): queued, no PMCID, unread. |
| (no PMID) | Lucas-Clarke 2025, "Alzheimer's disease risk gene Wwox protects against amyloid pathology through metabolic reprogramming": preprint with an open body but no PubMed record; not eligible for PMID-keyed ledgers until indexed. Worth watching for indexing. |

### Questions this batch could change

1. Is the anti-seizure effect of fasting/calorie restriction (36044864, 25814935) independent of mTOR/AMPK, and does Wwox loss alter either node (the GSK3B and Zfra papers already touch mTOR-adjacent kinases)?
2. The null mouse dies hypoglycaemic (read). Is hypoglycaemia in the null an energy failure or a counter-regulatory failure (cross-reference H3), and what glucose range is documented as safe for the developing brain (40119223)?
3. Is a Glut1-deficiency analogy (42638834) useful for WOREE (brain-glucose supply as the limiting step), or does the WWOX/HIF1A glycolytic shift argue against it?
4. Does a high fluid-volume, low-calorie regimen carry documented osmotic or oedema risk in encephalopathic children (41069084, 40944047), and is a WWOX-null brain, with the zebrafish oedema phenotype (25649963, held), more or less exposed?
5. Is thiamine/refeeding risk (38681648, 42087252, 39871710) a documented class-level concern when dextrose is given to chronically undernourished or ketogenic-adapted children?

## Safety-relevant (BLOCK-1) cautions at class level (literature observations, not advice)

- **H1.** Transfusional iron loading and its mitochondrial/endothelial toxicity are documented (41293173); transfusion burden is high in encephalopathic neonates (42794205). Iron supplementation effects on neurodevelopment cut both ways (42794294).
- **H2.** FFP exposure is associated with higher haemorrhage in a TBI model (36719667) and with IVH risk questions in prolonged-APTT preterm infants (42769206). Plasma exchange in critically ill children has an adverse-event profile (42509933). Complement-deficient mice have higher seizure mortality (37234916), so lowering a circulating factor is not uniformly protective.
- **H3.** Epinephrine's effect on neurological outcome is contested in cardiac-arrest data (39597089); chronic epinephrine exposure produced ER and oxidative stress in beta-cells (39000139); sympathetic surges are part of SUDEP mechanisms (36686527, 41584903); hypoglycaemia unawareness blunts the epinephrine counter-regulation (38397994).
- **H4.** Hyperbaric oxygen can provoke seizures (42652189); hyperoxia injures the developing brain, more so with inflammation (40022130, 28119904); hypoxia therapy is being studied as a treatment in mitochondrial disease (42420651, 39965572), so the direction of effect depends on context.
- **H5.** Glucose infusion without thiamine is a recorded cause of Wernicke encephalopathy (38681648); dextrose route and refeeding are linked to electrolyte deficiency (42087252, 39871710); hypotonic or large-volume fluids are linked to hyponatraemia, cerebral oedema and osmotic demyelination (41069084); neonatal hypoglycaemia is linked to later epilepsy susceptibility (40589985); long-term ketogenic diets produced anaemia and acidosis in rats (32685205).

## Counts

H1 14, H2 16, H3 14, H4 16, H5 16 (76 studies, no PMID repeated across groups). Tier 1 rows: H1 2, H2 4, H3 3, H4 2, H5 3. WWOX-direct selectable studies with a lawful body: H2 1 (38203337), H4 1 (36364214) plus 1 mention-only (39087877); none in H1, H3, H5. Every other row is pathway, disease-class or transferable and is labelled as such.
