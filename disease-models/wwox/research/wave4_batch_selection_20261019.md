# Wave 4 study selection: W1 fresh WWOX literature and W2 metabolic gaps not yet covered

Date: 2026-10-20. Author: read-only study selector. No repository file was edited, staged or committed. Nothing here is medical advice; this is a reading list, not evidence. Absence from the registry is a statement about this repository, not about the literature.

## Method

Same method and three tests as `disease-models/wwox/research/metabolic_batch_selection_20261019.md` (abstract substantive; lawful full-text body with the route checked; a question the paper could change).

1. Discovery. PubMed E-utilities date-sorted searches (entry date from 2026-06-01, publication date from 2026-08-01, and a 2025-01 to 2026-12 sweep: 73 records) for WWOX, WOX1, Wwox, WOREE, SCAR12, EIEE28; a 400-record WWOX-neuro sweep of all years for older papers never receipted; Europe PMC title/abstract and open-access full-text searches since 2026-07-15 (found the astrocyte review and the Tunisian corpus-callosum paper, whose WWOX content is in the body only); preprint search (source PPR) for 2026. For W2: Europe PMC `WWOX AND <axis terms>` for ten axes, then PubMed counts per axis (table below), then disease-class searches for substitutes.
2. Dedup. Every candidate: `registry_records.py get --pmid <PMID> --hops 0` (only the file/mention header lines were read), the receipts ledger plus all staged receipts under `receipt_staging/*` (scan of study-id pmid), and `owed_sections.py` (best state per section across ledger and staged receipts). Queue entries were read for the cases the registry mentions (FT-017, FT-110, FT-115, FT-170, FT-197). The two large registries were never grepped.
3. Identity. Every title in the tables is the PubMed title re-fetched from NCBI esummary by PMID.
4. Body check (test 2). Europe PMC `fullTextXML` status and size for every PMC route (200 and over 40 kB = OA XML; 500 = "PMC page only"); Unpaywall for DOI-only records; the publisher or repository URL fetched for the DOI-only rows that I selected or rejected (HTTP code, size, file magic). Bodies were not read beyond counting WWOX in the XML of the ones listed.
5. Tier: 1 = WWOX-direct, or a record that directly bears on a stated gap; 2 = WWOX-adjacent (partner, locus, tumour genomics in the target tissue); 3 = transferable disease-class or method paper, labelled SUBSTITUTE where it is not WWOX evidence.

## Headline for the Orchestrator

- The fresh WWOX-direct pool (indexed since 2026-06) is almost entirely already receipted. Only five WWOX-titled records were indexed since 2026-08-01 and none is selectable: Guevara 2026 WOREE Argentina (no lawful body), Tao 2026 gastric Wnt (cancer; no DOI, no body route found), the retracted leukaemia p73 paper (excluded), Hammouz 2026 WWOX/HIF1A (receipt, owed none) and the FASD GWAS preprint (receipt, owed introduction and references). Fresh WWOX-direct bodies that exist (Steinberg organoids, Obeid gene therapy, the astrocyte review, Gao 2025 WWOX-DEE, Petrozziello preprint) all carry receipts. So W1 is mostly "never-read WWOX-direct background and verification debts", not fresh papers; it says so per row.
- Almost every un-receipted WWOX-direct clinical paper (WOREE case series, MRI, genotype-phenotype) is paywalled with no open copy: the BLOCKED table is longer than the selected one for those. Operator-supplied PDFs would unlock the highest-value items (Guevara 2026, Serin 2018, Tabarki 2015, Mignot 2015).
- W2: for 10 of the 18 requested axes there is no WWOX paper that touches them (table below). The W2 list therefore holds 6 WWOX-direct or WWOX-locus records (two are tumour genomics) and 10 disease-class SUBSTITUTE rows. A substitute is never evidence about WWOX; it says what the cofactor or axis looks like where the biology is known.
- Operator context (folates): the only WWOX-and-folate record with an open body is already fully receipted (PMID 41378749, folate interaction with genetic risk for neural-tube defects; owed none); the other title/abstract hit is an unrelated oncology paper. No WWOX paper addresses folate or B12 metabolism itself. The folate rows in W2 are therefore SUBSTITUTE (cerebral folate transport deficiency, FOLR1) and a treatable-cause umbrella review.

### PubMed title/abstract counts, WWOX or Wwox or WOX1 or WOREE AND axis (queried 2026-10-20)

| Axis (terms) | Records | What they are |
|---|---|---|
| thyroid | 6 | thyroid cancer and fragile-site papers, plus one thyroid-hormone GWAS (paywalled) |
| kidney or renal | 12 | tumours (Wilms, renal cell), fragile-site reviews; no renal function paper |
| bile acid | 0 | none |
| carnitine or acylcarnitine | 1 | the mGWAS (receipt staged) |
| creatine | 0 | none |
| pyridoxine or vitamin B6 | 1 | a WOREE splice-variant case (paywalled; pyridoxine mention only) |
| biotin | 0 | none |
| coenzyme Q10 or ubiquinone | 0 | none |
| folate, folic, B12 | 2 | one receipted neural-tube-defect gene-by-folate record (complete), one unrelated oncology paper |
| homocysteine, methionine, one-carbon | 3 | NCI-60 metabolomics (selected) and two PARTICLE-RNA papers; none about methylation metabolism |
| leucine, isoleucine, BCAA | 5 | mGWAS (receipt staged), ovarian-tumour and ubiquitin-ligase papers |
| vitamin D, calcium, PTH | 12 | mostly calcium signalling in cell death; no vitamin D or PTH paper |
| obesity, adipose, thermogenesis, brown fat | 13 | GWAS, livestock traits, receipted metabolic papers; no BAT or thermogenesis paper |
| steatosis, NAFLD, NASH | 2 | NASH-HCC genomics (selected) and a receipted HDL paper |
| insulin, beta cell, pancreas | 24 | mostly receipted (glucose, HIF1A, pancreatic cancer) |
| growth hormone, IGF, growth retardation | 9 | receipted Wwox-null phenotype papers and reviews |
| supplement, dietary, nutrition | 19 | oncology, livestock and GWAS hits; no supplementation report in WOREE, SCAR12 or Wwox mouse |
| temperature, hypothermia | 7 | the cold-shock bubbling-death papers (one receipted 2024, selected 2015) |

No supplementation, cofactor or nutrient report exists for WOREE, SCAR12 or Wwox mice in PubMed title/abstract. Where an axis shows 0, the honest substitute is the disease-class rows below, not any WWOX claim.

## Group W1 fresh WWOX literature and never-read WWOX-direct background

Count selected: 14 (tier 1 highest). Nine rows are WWOX-direct (40327201, 35883580, 27075929, 29581896, 27773744, 25802472, 35107375, 36979157; 41510857 is a gene-list cohort that carries a WWOX negative); five are transferable rows. None is a paper first indexed after 2026-08-01, because every such WWOX-direct paper is receipted or blocked (see Headline); 41510857 (2026-01) and 40327201 (2025-05) are the most recent.

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 41510857 | Kılıç, 2026 | An Overview of Drug-Resistant Epilepsies Based on Advances in Genetics: A Cohort Study | The only PubMed record joining WWOX to any T-type calcium-channel gene sits in a ~45-gene list; the queue says the 'no T-type evidence' negative rests on it. Opening it either confirms the negative or inverts it. | OA publisher HTML (ovid mirror; ~19k chars incl. methods/results/references, fetched); no PMCID | queued FT-115 (LOW; negative-bearing), no receipt | 1 |
| 40327201 | Hammouz, 2025 | Twenty-five years of WWOX insight in cancer: a treasure trove of knowledge | 2025 review of WWOX over 25 years, indexed 2025-05; the newest single-source WWOX synthesis without a receipt; check what it says about non-cancer tissues and partners (class-level map for W2). | PMC12055895 (OA XML, CC BY-NC-ND) | new (identity record only, no receipt) | 1 |
| 35883580 | Liu, 2022 | WWOX Controls Cell Survival, Immune Response and Disease Progression by pY33 to pS14 Transition to Alternate Signaling Partners | Review of the pY33-to-pS14 switch between signalling partners: tests whether the phospho-state model in the working model is current. | PMC9323965 (OA XML, CC BY) | new (identity record, no receipt) | 1 |
| 27075929 | Chang, 2016 | Bubbling cell death: A hot air balloon released from the nucleus in the cold | WOX1 'bubbling cell death' from the nucleus in the cold; background to the temperature axis (see W2) and to the nuclear WWOX/TRAF2 switch already read in the 2024 paper. | PMC4950269 (PMC page only, XML 500) | new (no registry record) | 1 |
| 29581896 | Kuo, 2018 | Chasing the signaling run by tri-molecular time-lapse FRET microscopy | Time-lapse FRET of the WWOX/p53/TRAF2 tri-molecular signalling run: method lesson for any live-cell WWOX interaction assay. | PMC5864757 (OA XML, CC BY) | new (no registry record) | 2 |
| 27773744 | Schrock, 2017 | Fhit and Wwox loss-associated genome instability: A genome caretaker one-two punch | Fhit and Wwox loss-associated genome instability: the fragile-site caretaker frame behind the DNA-damage preprint (HELD) and the organoid paper. | PMC7213024 (PMC page only, XML 500) | new (queue/ledger mention only) | 2 |
| 25802472 | Chang, 2015 | Introduction to a thematic issue for WWOX | Editorial of the 2015 thematic WWOX issue: a map of the issue's articles, useful as a source of un-read WWOX-direct citations. | PMC4935221 (PMC page only, XML 500) | new (identity record only) | 2 |
| 35107375 | Liang, 2022 | WWOX-Mediated Degradation of AMOTp130 Negatively Affects Egress of Filovirus VP40 Virus-Like Particles | WWOX degrades AMOTp130 and impairs viral PPxY-mediated egress: a PPxY-partner mechanism in a non-cancer setting; the WW1 domain's partner range. | PMC8941927 (PMC page only, XML 500) | new (identity record only) | 2 |
| 36979157 | Kałuzińska-Kołat, 2023 | Antineoplastic Nature of WWOX in Glioblastoma Is Mainly a Consequence of Reduced Cell Viability and Invasion | WWOX in glioblastoma lines: antineoplastic effect is viability/invasion only; the only brain-cell-line WWOX expression study without a receipt. | PMC10045224 (OA XML, CC BY) | new (no registry record) | 2 |
| 42720877 | Schatz, 2026 | Genetic Diagnosis in Epilepsy: Implications for Clinical Management | 2026 genetic-diagnosis review with a WWOX-DEE28/SCAR12 row marked 'trial of gene replacement': check what the table claims against the Obeid gene-therapy read. | PMC13562175 (OA XML, CC BY-NC-ND) | new (no record) | 3 |
| 42738851 | Pozhitnova, 2026 | The Fragile Site Landscape of Induced Pluripotent Stem Cells: Hierarchy, Variability, Tissue Specificity, and Links to Culture-Acquired Rearrangements | Fragile-site landscape of iPSCs (FRA16D/WWOX named among neural-linked loci): decides whether iPSC/organoid WWOX models carry culture-acquired instability. WWOX is mentioned once; read only the fragile-site tables. | PMC13564719 (OA XML, CC BY) | new (no record) | 3 |
| 42650175 | Delahanty, 2026 | 4-Phenylbutyrate Plus Wildtype GAT-1 Augmentation: A Dual Therapy to Rescue SLC6A1 Variant-Associated Developmental and Epileptic Encephalopathy | 4-phenylbutyrate with wild-type GAT-1 for an SLC6A1 DEE: a chaperone/rescue-of-misfolding design (NOT WWOX evidence; transferable to Q230P-class proteostasis hypotheses). | PMC13512211 (OA XML, CC BY) | new (no record) | 3 |
| 42587736 | Song, 2026 | 4-Phenylbutyrate Rescue in GABRA1 Variants Associated with Developmental Epileptic Encephalopathies: From Cell and Mouse Models to Humans | 4-phenylbutyrate rescue of GABRA1 DEE variants from cells and mouse to humans: the same chaperone class with a human arm (NOT WWOX evidence). | PMC13465587 (OA XML, CC BY) | new (no record) | 3 |
| 42846717 | Samanta, 2026 | Ketogenic diet therapy in developmental and epileptic encephalopathies: toward syndrome- and gene-informed precision therapy | 2026 review of ketogenic diet by DEE gene: sets the prior for the 3-of-5 WOREE responders (WWOX is not named in the body; fetched and counted). | PMC13643383 (OA XML, CC BY) | new (no record) | 3 |

### HELD with a partial receipt (not selected; re-read only with a stated question; owed sections from `owed_sections.py`)

| PMID | Note |
|---|---|
| 42523332 | Aragon-Ramirez 2026, Golgi CATCHR complexes (bioRxiv PREPRINT, not peer reviewed): owed abstract, introduction, limitations, methods not read; supplementary captions only. Receipt FTR-20260921-42523332-01. WWOX relevance is a protein-interaction mention; a re-read needs a stated question on tethering complexes. |
| 41228229 | Yang 2025, The Role of WWOX in Cancer Progression (review): owed abstract, discussion, limitations not read. Re-read only if the cancer-to-neural partner question needs the discussion. |
| 42807679 | Khadija 2026, corpus callosum abnormalities in 107 Tunisian patients (16q23 microdeletion rows include WWOX): owed figures captions only. Not recommended. |
| 42395553 | Petrozziello 2026 PREPRINT, WWOX and DNA damage but not somatic instability in Huntington's disease: owed figures and supplementary captions only. |
| 42818975 | Ruhela 2026 PREPRINT (Research Square), FASD GWAS: staged receipt PPR1316475 owes introduction and references not read; WWOX is a locus hit. Low value. |
| 41254692 | Qin 2025, WWOX/THBS2 in T/NK lymphoma: owed figures and supplementary captions only. |
| 40875931 | Gao 2025, WWOX-related DEE clinical spectrum (Neurology): owed figures captions only. Not recommended. |
| 42397075 | Steinberg 2026, WWOX-MYC organoids: owed none after FTR-20261004-42397075-05; excluded (complete). |

### Excluded with a complete or nothing-owed receipt (no re-read stated)

42558002 (astrocytes in genetic epilepsies, complete), 42422765 (Obeid 2026), 42589397 (Hammouz 2026 HIF1A, owed none), 41677633, 41378749, 41984841, 42082822, 42128308, 42135313, 42193054, 41562193, 41153369, 41124647, 41090157, 39868255, 39952983, 40507943 (all owed none). Not selected for other reasons: 42464650 (retracted notice, WWOX-mediated apoptosis), 42231860 (dog sex-development copy-number paper, WWOX not in the abstract), 42266427 (LATE-NC locus list; queue FT says it carries nothing to the paediatric genotype), 42654085 (WWOX appears once in an organoid sentence).

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 42721537 | Guevara 2026, WOREE case series from Argentina (Seizure): not in Europe PMC, Unpaywall is_oa false, queue FT-110 (no PMCID). Highest-value blocked item: five homozygous patients with a canonical donor-site allele, never examined at RNA level. Needs an operator-supplied PDF. |
| 41442931 | Choi 2026, vigabatrin-associated MRI abnormalities in two WOREE children: not open access. |
| 42190144 | Riccardi 2026, burst-suppression EEG in early DEE (WWOX named once in the abstract): Unpaywall lists a HAL submitted version, but HAL says openAccess false and both document URLs return the 12 kB landing page (embargoed). |
| 40139278 | Yuan 2025, WWOX/MAF and cognition in Parkinson disease: open access, but the publisher returns HTTP 403 to every automated route (queue FT-197 notes the cascade); needs an interactive fetch. |
| 39933386 | Martin 2025, infantile epileptic spasms series from Argentina (WWOX in the variant list): queue FT-017 unrecoverable_by_these_routes; the DOI resolves to a 2.7 kB stub. |
| 30094525, 26345274, 34034642, 38407561, 39039877, 25411445, 25716914, 25403906 | Serin 2018, Tabarki 2015, Havali 2021, Nishino 2024, Wang 2024 (Chinese), Mignot 2015, Valduga 2015, Ben-Salem 2015: WWOX-DEE clinical series; Europe PMC has no body, Unpaywall is_oa false. The first two are queued (genotype-phenotype correlation, five-case severity series). |
| 40088508 | Thanuja 2025, infant-onset genetic epilepsy cohort in India: not open access. |
| 38902482 | Chen 2025, WWOX and Hippo in esophageal cancer: not open access (queue FT-110 co-record). |
| 42790938 | Tao 2026, WWOX in gastric cancer Wnt/beta-catenin: no DOI and no body route found. |
| 39894307, 41443103, 40198927, 40263068 | Already recorded in the earlier metabolic selection as BLOCKED (toosendanin ferroptosis, lung-injury ferroptosis, gallbladder glycolysis and its corrigendum). |

### Questions this group could change

1. Is the "no T-type calcium evidence in WWOX deficiency" negative real? Read 41510857 end to end: does it report CACNA1H in a patient with a WWOX variant, or only list both genes in one cohort? An inversion changes the ethosuximide mechanism statement.
2. Does the 2025 25-year WWOX review (40327201) and the phospho-switch review (35883580) agree with the working model on the pY33/pS14 states and the partner list, and do they describe any non-cancer tissue phenotype not already modelled? Gaps found here become W2 reading targets.
3. Is the cold-shock bubbling-death mechanism (27075929, with 25779665 in W2) a cell-death curiosity or a plausible link to temperature-triggered seizures in WOREE? A negative closes the temperature thread.
4. Do iPSC and organoid WWOX models carry culture-acquired fragile-site instability (42738851), so that FRA16D events could confound organoid phenotypes (Steinberg 2026 is receipted)?
5. Does a chaperone design such as 4-phenylbutyrate (42650175, 42587736) rescue a loss-of-function missense class at a stated dose in a DEE gene, so that a Q230P-type misfolding hypothesis has a precedent worth a stated test? These are transferable rows, not WWOX evidence.

## Group W2 metabolic gaps not yet covered

Count selected: 16 (tier 1 highest). Rows marked SUBSTITUTE are disease-class papers and are not WWOX evidence. The WWOX-direct rows are tumour genomics or locus records unless stated.

| PMID | First author, year | Title (PubMed) | Axis | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|---|
| 25779665 | Chen, 2015 | UV irradiation/cold shock-mediated apoptosis is switched to bubbling cell death at low temperatures | body temperature | UV/cold shock switches apoptosis to bubbling death at 4 C with nuclear WWOX/p53/TRAF2 (WWOX 49 body mentions): the only WWOX-direct temperature paper. A cell-death paper, not a thermoregulation paper; it bounds what 'WWOX and temperature' can mean. | PMC4480731 (OA XML, CC BY) | new (no record) | 1 |
| 29481666 | Teslovich, 2018 | Identification of seven novel loci associated with amino acid levels using single-variant and gene-based tests in 8545 Finnish men from the METSIM study | amino-acid metabolism | WWOX rs9937914 and serum alanine in 8545 Finnish men: the only amino-acid association with WWOX at genome-wide level; listed in the metabolic selection G2 but no receipt is staged, so confirm it is unassigned. | PMC5905595 (PMC page only, XML 500) | new (discovery-ledger mention only) | 1 |
| 36587184 | Friemel, 2022 | Single-cell resolved ploidy and chromosomal aberrations in nonalcoholic steatohepatitis-(NASH) induced hepatocellular carcinoma and its precursor lesions | liver steatosis | NASH-associated HCC: WWOX loss in 36% of tumours (36 body mentions) with whole-genome duplication; the only steatosis-setting WWOX record. Tumour genomics, so it says nothing about hepatocyte WWOX function in steatosis. | PMC9805444 (OA XML, CC BY) | new (no record) | 2 |
| 41141138 | Sharma, 2025 | Intertwined Relationship of WWOX and RUNX2 Proteins as a Biomarker for Predicting Response and Survival in Patients With Childhood Bone Cancer in North India: A Pilot Study | bone | WWOX and RUNX2 immunohistochemistry in 7 Ewing/bone-tumour cases vs 5 controls: partner of the known Wwox-RUNX2 osteoblast arm (Aqeilan 2008, read). Tiny pilot; useful for the RUNX2 link only. | PMC12552799 (OA XML, CC BY) | new (identity record, no receipt) | 2 |
| 37686047 | Rushing, 2023 | Multi-Omics Analysis of NCI-60 Cell Line Data Reveals Novel Metabolic Processes Linked with Resistance to Alkylating Anti-Cancer Agents | one-carbon/amino-acid | NCI-60 multi-omics: WWOX copy-number loss in alkylating-agent-resistant lines flagged under 'metabolic changes'; check whether the metabolic link is more than a gene-list line (WWOX 9 body mentions). | PMC10487847 (OA XML, CC BY) | new (no record) | 2 |
| 22842668 | Płuciennik, 2012 | Genetic alterations of WWOX in Wilms' tumor are involved in its carcinogenesis | kidney | WWOX genetic alterations in Wilms' tumour: the only kidney-setting WWOX record without a receipt. Tumour, not renal function. | publisher PDF served (1.4 MB, application/pdf) at the Spandidos download link; no PMCID | new (no record) | 2 |
| 29899766 | Mastrangelo, 2018 | Actual Insights into Treatable Inborn Errors of Metabolism Causing Epilepsy | umbrella: B6, folate, biotin, creatine, CoQ10, serine | Review of treatable inborn errors of metabolism causing epilepsy: the checklist that says which cofactor assays belong in any DEE work-up. SUBSTITUTE (disease class), not WWOX evidence. | PMC5982487 (OA XML, CC BY-NC-SA) | new (no record) | 3 |
| 36980111 | Mastrangelo, 2023 | Epilepsy Phenotypes of Vitamin B6-Dependent Diseases: An Updated Systematic Review | vitamin B6 | Systematic review of epilepsy phenotypes across vitamin B6-dependent diseases (PDE-ALDH7A1, PNPO, PLPHP): names which seizure phenotypes respond to B6. SUBSTITUTE, not WWOX evidence; WWOX reports mention pyridoxine only once (Nishino 2024, paywalled). | PMC10047402 (OA XML, CC BY) | new (no record) | 3 |
| 38978529 | Girgis, 2024 | Cerebral Folate Transport Deficiency in 2 Cases with Intractable Myoclonic Epilepsy | folate | Cerebral folate transport deficiency in two cases with intractable myoclonic epilepsy: shows what a folate-pathway DEE looks like in practice. SUBSTITUTE, not WWOX evidence. | PMC11227922 (OA XML, CC BY-NC) | new (no record) | 3 |
| 34258135 | Papadopoulou, 2021 | Cerebral folate deficiency in two siblings caused by biallelic variants including a novel mutation of FOLR1 gene: Intrafamilial heterogeneity following early treatment and the role of ketogenic diet | folate | FOLR1 biallelic cerebral folate deficiency in two siblings: second folate-transport report; both together say what CSF 5-methyltetrahydrofolate would show. SUBSTITUTE. | PMC8260484 (OA XML, CC BY) | new (no record) | 3 |
| 42563882 | Lai, 2025 | A Rare and Treatable Cause for Generalized Epilepsy: Biotinidase Deficiency | biotin | Biotinidase deficiency as a treatable generalised epilepsy: the biotin end of the cofactor list. SUBSTITUTE. | PMC13359203 (OA XML, CC BY-NC-ND) | new (no record) | 3 |
| 42660645 | Ribeiro-Constante, 2026 | Treating a Disorder Caused by an Overactive Enzyme: BCKD-Kinase Deficiency | BCAA / leucine-isoleucine | BCKD-kinase deficiency, an overactive-enzyme disorder with low branched-chain amino acids: the BCAA comparator for the WWOX-locus leucine/isoleucine mGWAS (Ouyang 2021, receipt staged). SUBSTITUTE. | PMC13521751 (PMC page only, XML 500) | new (no record) | 3 |
| 39543202 | Nassar, 2024 | Impact of L-carnitine supplementation on gastric emptying and bowel function in pediatric ketogenic diet therapy: a clinical trial | carnitine | L-carnitine supplementation in children on ketogenic diet therapy (gastric emptying, bowel function): what carnitine supplementation measures in the exact diet the WOREE responders used. SUBSTITUTE. | PMC11564695 (OA XML, CC BY) | new (no record) | 3 |
| 33406758 | Merlotti, 2021 | Energy Metabolism and Ketogenic Diets: What about the Skeletal Health? A Narrative Review and a Prospective Vision for Planning Clinical Trials on this Issue | bone / calcium / vitamin D | Narrative review of ketogenic diets and skeletal health: Wwox-null mice have bone defects and ketogenic diet is the main WOREE-relevant diet, so this sets the bone-monitoring prior. SUBSTITUTE. | PMC7796307 (OA XML, CC BY) | new (no record) | 3 |
| 36619921 | Nóbrega, 2022 | Cerebrotendinous Xanthomatosis: A practice review of pathophysiology, diagnosis, and treatment | bile acids | Cerebrotendinous xanthomatosis practice review (CYP27A1 bile-acid synthesis, chenodeoxycholic acid therapy): the one bile-acid-treatable neurological class; no WWOX bile-acid record exists. SUBSTITUTE. | PMC9816572 (OA XML, CC BY) | new (no record) | 3 |
| 38074073 | Agarwala, 2023 | Early-infantile developmental and epileptic encephalopathy: the aetiologies, phenotypic differences and outcomes-a prospective observational study | DEE aetiology / treatable causes | Early-infantile DEE: aetiologies, phenotype differences and outcomes: gives the share of treatable metabolic causes against which WOREE is a structural-genetic class. SUBSTITUTE. | PMC10702464 (OA XML, CC BY) | new (no record) | 3 |

### HELD with a partial receipt (not selected)

| PMID | Note |
|---|---|
| 33854788 | Ouyang 2021 mGWAS (WWOX locus with leucine/isoleucine, T2D metabolites): owed supplementary captions only (staged receipt FTR-20261019-33854788-01, scientist-b). Do not re-read; use it as the WWOX anchor for the BCAA rows above. |
| 33520443 | Baryla 2021 GDM: owed supplementary captions only (staged). |
| 40191585 | Robertson 2025 shared-haplotype inference (WWOX among genes): owed supplementary captions only. |

Already complete or nothing owed, excluded from W2: 31145772 (Permana, beta-cell HOMA), 20942981 (Saez, HDL), 35328751, 33195192, 36271927, 18487609 (bone and hypoglycaemia lethality), 39420317 (2024 WWOX/TRAF2 cold-shock bubbling death, which is why the 2015 precursor is selected for the temperature axis).

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 34533693 | Huang 2022, genome-wide association of thyroid-related hormones in a Chinese population (WWOX among hits): not open access. The only WWOX endocrine-axis GWAS found. |
| 21520031 | Cancemi 2011, WWOX Pro282Ala polymorphism and differentiated thyroid carcinoma: Unpaywall lists a Wiley PDF, but it returns HTTP 403 (open access but bot-blocked); needs an interactive fetch. |
| 38056170 | Carcass and meat-quality GWAS in livestock with a WWOX-region hit (adiposity analogue): the DOI resolves to a 2.7 kB stub. Low value. |
| 36729635 | Tangeraas 2023, BCKDK deficiency as a treatable neurodevelopmental disease (Brain): open access per Unpaywall, but the publisher PDF returns HTTP 403. The PMC-page row 42660645 covers the same disease class. |
| 34972654 | Fernandes-Pires 2022, treatment of creatine deficiency syndromes: DOI resolves to a stub. Creatine has no PMC-open substitute found; the umbrella review 29899766 covers GAMT and the transporter. |
| 26238973 | Nizamuddin 2015 THSD7A and obesity: already BLOCKED in the earlier selection. |

### Axes with no WWOX evidence and the honest substitute (substitutes are NOT WWOX evidence)

| Axis | WWOX evidence found | Substitute in the table |
|---|---|---|
| adipose, BAT, thermogenesis | none (obesity GWAS hits, livestock; one blocked) | none worth reading; the temperature thread is carried by 25779665 only |
| liver steatosis | NASH-associated HCC copy-number loss (tumour genomics) | 36587184 |
| bone, calcium, vitamin D, PTH | Wwox-null osteoblast and RUNX2 arm (read); a 7-case pilot | 41141138; 33406758 (ketogenic diet and skeleton) |
| thyroid and endocrine axes | thyroid-cancer papers, one blocked GWAS | none (only blocked rows); stated as a gap |
| pancreas, beta cell | read (Permana, GDM, pancreatic-cancer paper) | not needed |
| kidney | Wilms' tumour genetics | 22842668 |
| growth, IGF | Wwox-null growth retardation (read) | not needed |
| bile acids | none | 36619921 (cerebrotendinous xanthomatosis) |
| amino acids, BCAA, alanine | two GWAS (mGWAS owed none; alanine unread) | 29481666; 42660645 |
| one-carbon, folate, B12 | none (complete NTD record is genetic risk only) | 38978529, 34258135, 29899766 |
| carnitine, acylcarnitine | one mGWAS line | 39543202 |
| creatine | none | blocked; covered by 29899766 |
| vitamin B6 | one case report mention (paywalled) | 36980111, 29899766 |
| biotin | none | 42563882 |
| coenzyme Q10, mitochondrial cofactors | none | 29899766 (covers CoQ10 as a treatable cause); no CoQ10-specific open paper selected |
| supplementation in WOREE, SCAR12 or Wwox mouse | none | none; the rows above only say what cofactor work-ups exist for DEE |

### Questions this group could change

1. Does the temperature thread have any basis in WWOX biology beyond cell-death assays (25779665)? A body that only describes 4 C bubbling death closes it; a mention of in vivo cold or fever sensitivity opens a monitored question.
2. Is the NASH-HCC WWOX loss (36587184) and the NCI-60 copy-number line (37686047) just tumour genomics, or does either paper report a metabolic readout tied to WWOX? If neither, liver steatosis and one-carbon stay "no WWOX evidence" in the working model.
3. Is the WWOX-alanine association (29481666) the glucose-alanine cycle, or only a transaminase locus artefact? Together with the receipted leucine/isoleucine mGWAS this decides whether an amino-acid panel belongs in a WOREE biomarker list.
4. Which treatable cofactor causes (B6, folate, biotin, creatine, CoQ10) does a DEE work-up exclude before a WWOX diagnosis (29899766, 36980111, 38074073)? This states what a negative cofactor screen can and cannot say about a WOREE case; it is a screening-logic question, not a therapy claim.
5. Do the two cerebral-folate-transport reports (38978529, 34258135) define a CSF folate readout that a WWOX-LF model could be tested against, given that no WWOX folate data exist? A "no" leaves folate as a pure substitute.

## Operator-facing notes

- Selected counts: W1 14, W2 16. Routes: OA XML for 24 rows; PMC page only for 6 (W1: 27075929, 27773744, 25802472, 35107375; W2: 29481666, 42660645); one publisher PDF (22842668); one publisher HTML (41510857). Check the route per row before assigning.
- Several W1 rows (35883580, 29581896, 27773744, 25802472, 35107375, 36979157) are WWOX-direct background with no stated urgency; assign them last. The highest-yield W1 reads are 41510857 and 40327201; the highest-yield W2 read is 25779665 and 29481666.
- The most valuable single unlock is an operator-supplied PDF of 42721537 (FT-110 debt).
