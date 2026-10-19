# Metabolic-themes study selection for four Scientists (WWOX loss of function)

Date: 2026-10-19. Author: read-only study selector. No repository file was edited, staged or committed. Nothing here is medical advice; this is a reading list, not evidence.

## Method

1. Repo context read first: `disease-models/wwox/analysis/wwox_metabolism_reviews_audit_20260921.md`, `disease-models/wwox/research/research_lines_current.md` (RL-003), `disease-models/wwox/registries/working_model_current.md` (theme-bearing lines only, located by term counts), `framework/scripts/README.md` (tool routing).
2. Candidate discovery: Europe PMC REST (title/abstract queries `WWOX|Wwox|WOX1` crossed with ~120 theme terms per group; WWOX-partner and orthologue queries; transferable-topic queries restricted to open-access PubMed records) plus PubMed MCP `search_articles` for the four group queries. Roughly 100 WWOX-direct records and several hundred transferable records were screened by title/abstract.
3. Dedup (mandatory): every candidate PMID went through `framework/scripts/registry_records.py get --pmid <PMID> --hops 0` (never the registries whole), then a grep of the PMID in `disease-models/wwox/research/full_text_queue_current.md` and in `disease-models/wwox/registries/fulltext_read_receipts.jsonl` (a receipt line that merely cites another study was ignored; only `study_id.pmid` counts). Partial receipts were decoded section by section.
4. Identity: every PMID in the tables was re-fetched from NCBI esummary and the title column is the PubMed title; first-author surnames were compared to my notes (two accent-only differences, no real mismatch).
5. Body check (test 2): Europe PMC `fullTextXML` was fetched for every PMC route listed (200 and more than 5 kB = "OA XML"). Records in PMC but outside the open-access subset (XML 500, efetch returns no body) are labelled "PMC page/PDF only". Records with no PMCID were checked for Europe PMC full-text links; failures go to BLOCKED. One publisher PDF (Permana 2019) was fetched and served. Bodies were not read.
6. "Tier": 1 = WWOX-direct or WWOX human-genetics, or a transferable paper that directly tests a stated model gap; 2 = WWOX-pathway/partner/orthologue or strong comparator; 3 = transferable review or methods carrying one testable lesson. Registry status vocabulary: "new" = no receipt exists; "HELD-partial" = a partial receipt exists and the unread sections are named.
7. No novelty is claimed anywhere below. Absence from the registry is a statement about this repository, not about the literature.

## Headline findings for the Orchestrator

- The WWOX-direct metabolic literature is mostly already fully read here (table below). Two more are declared read with no receipt shown (Breton 2021, Obeid 2026 review) and lie outside the metabolic themes, so they are not selected. The residual new WWOX-direct metabolic pool is small (about 14 records), so the groups carry a larger share of tier-2/3 partner and transferable papers than the brief's ideal; every such row states its transfer.

### Already fully read, EXCLUDED (receipt at complete depth)

| PMID | First author, year | Theme |
|---|---|---|
| 25012504 | Abu-Remaileh 2014 | G2 WWOX/HIF1A glucose |
| 29724996 | Abu-Remaileh 2018 | G2 hepatic HIF1A |
| 30755385 | Abu-Remaileh 2019 | G2 muscle glucose metabolism / GWAS |
| 27308416 | Abu-Remaileh 2015 | G2 commentary |
| 25491415 | Abu-Remaileh 2015 | G1/G2 review |
| 36271927 | Baryla 2022 | G2 metabolic review (audited 2026-09-21) |
| 18674750 | Lee 2008 | G1 low HDL-C |
| 24871327 | Iatan 2014 | G1 HDL / Wwox hep-/- |
| 24932569 | Aldaz 2014 | G1 review |
| 24520212 | Li 2014 | G1 review |
| 18974271 | Aqeilan 2009 | G1/G4 steroidogenesis |
| 18487609 | Aqeilan 2008 | bone, hypoglycaemia lethality |
| 31340538 | Tochigi 2019 | G1 hypomyelination rat |
| 21075834 | O'Keefe 2011 | G3 Drosophila respiration/ROS |
| 21212468 | Dudekula 2010 | G3 Zfra mitochondria |
| 22193544 | Wang 2012 | G2 GSK3B |
| 32000863 | Cheng 2020 | G2 GSK3B seizure |
| 30619736 | Hussain 2018 | interactome, metabolic pathways |
| 30290271 | Hussain 2019 | G4 GABAergic interneurons |
| 36828035 | Hussain 2023 | P47T mouse |
| 34747138 | Repudi 2021 | gene therapy |
| 26499798 | Abu-Remaileh 2015 | pleiotropic functions review |
| 39101447 | You 2024 | DEE case, vigabatrin |
| 35573960 | Riva 2022 | WOREE phenotype |
| 30370248 | Tanna 2018 | models review |
| 34831305 | Steinberg 2021 | models review |
| 42422765 | Obeid 2026 | gene therapy |
| 42092735 | Serce Pehlevan 2026 | G4 neonatal parkinsonism case (every section read) |

- The working model is silent on lipids, cholesterol, iron, ferroptosis, catecholamines, adrenal, dopamine, serotonin and glutamate (term counts in `working_model_current.md`: 0 for each; `HDL` 1; `myelin` 11; `ketogenic` 2; `glycoly` 2; `mitochond` 2). Groups 1, 3 and 4 therefore read into unmodelled territory; group 2 reads against an existing, narrowed arc.
- Paywalled/absent routes are listed per group under BLOCKED. Several (Choo 2015, Tang 2025, Chen 2005) are already recorded in the queue as `unrecoverable_by_these_routes`.
- Reads held with a partial receipt are listed per group under HELD; most owe only figure panels or the reference list, so a re-read needs a stated question and is not recommended by default.
- Two correction notes: the Ouyang 2021 mGWAS links the WWOX locus to leucine/isoleucine (suggestive, p below 1e-6), not to epinephrine (epinephrine is a separate T2D-predictive metabolite in the same paper); the Teslovich 2018 locus is WWOX with alanine.

## Group G1 lipid metabolism (plus VLCFA / peroxisome / sphingolipid)

Count selected: 15 (tier column: 1 highest priority).

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 20942981 | Saez 2010 | WWOX gene is associated with HDL cholesterol and triglyceride levels | WWOX intron-8 variants associate with HDL-C and TG in 801 Spaniards: the human-genetics anchor for a heterozygous-loss lipid trait | PMC2967537 (OA XML) | new (corpus placeholder "screened", no read, no receipt) | 1 |
| 21444760 | Leduc 2011 | The mouse QTL map helps interpret human genome-wide association studies for HDL cholesterol | Mouse HDL QTL x human GWAS converge on Wwox (with Abca1, Galnt2, Cdh13); queue note ties it to brain cholesterol and myelin | PMC3090235 (PMC page/PDF only, no XML; queue FT-019 "idIsNotOpenAccess, pdf_only") | new (not a registry record; queued FT-019 MEDIUM, abstract only) | 1 |
| 35559044 | Liu 2022 | EHBP1, TUBB, and WWOX SNPs, Gene-Gene and Gene-Environment Interactions on Coronary Artery Disease and Ischemic Stroke | EHBP1/TUBB/WWOX SNPs and gene-environment interactions on CAD and stroke (lipid and diabetes covariates): second Maonan-cohort WWOX lipid-risk paper | PMC9086287 (OA XML) | new (registry "not_processed", no receipt) | 1 |
| 39500530 | Liu S 2024 | WWOX tuning of oleic acid signaling orchestrates immunosuppressive macrophage polarization and sensitizes hepatocellular carcinoma to immunotherapy | WWOX loss raises tumour-derived oleic acid and shifts macrophage polarisation: a WWOX-to-fatty-acid-signalling arc (cancer setting, transferable question: does WWOX loss change MUFA/oleate pools?) | PMC11552608 (OA XML) | new (registry "not_processed", no receipt) | 1 |
| 25595186 | Richards 2015 | WWOX, the chromosomal fragile site FRA16D spanning gene: its role in metabolism and contribution to cancer | Review of WWOX in metabolism (SDR/NAD site, Drosophila ROS/aerobic metabolism, steroid and HDL links); route for the SDR-substrate question | PMC4935231 (PMC page/PDF only, no XML) | new (registry "not_processed") | 2 |
| 41715204 | Sun 2026 | Very long chain sphingolipids govern brain myelination by regulating oligodendrocyte differentiation and membrane microdomain integrity | Very-long-chain sphingolipids set oligodendrocyte differentiation and membrane microdomains: transferable test for the WWOX-null hypomyelination (Repudi, Tochigi, Abudiab) | PMC13094249 (OA XML) | new (not in registry) | 2 |
| 36583573 | Teo 2023 | Early microglial response, myelin deterioration and lethality in mice deficient for very long chain ceramide synthesis in oligodendrocytes | CerS2-null mice: early microglial response, myelin deterioration, lethality: a lipid-synthesis null that phenocopies WWOX-null hypomyelination plus early death | PMC10952316 (OA XML) | new (not in registry) | 2 |
| 40590574 | Wong 2025 | Biallelic ELOVL1 Variants Are Linked to Hypomyelinating Leukodystrophy, Movement Disorder, and Ichthyosis | Biallelic ELOVL1 variants: hypomyelinating leukodystrophy with movement disorder: human VLCFA-elongation comparator for WOREE/SCAR12 hypomyelination | PMC12485584 (OA XML) | new (not in registry) | 2 |
| 32123819 | Isokawa 2019 | Reduced chain length in myelin sphingolipids and poorer motor coordination in mice deficient in the fatty acid elongase Elovl1 | Elovl1-deficient mice: shortened myelin sphingolipid chains and poor motor coordination: shows what a lipid-chain-length readout in myelin looks like | PMC6996318 (OA XML) | new (not in registry) | 2 |
| 42454491 | Peeples 2026 | Sterol biosynthesis, brain development, and disease | Review: brain relies on intrinsic sterol synthesis for myelination and synaptogenesis: frames whether WWOX-null cholesterol supply is worth measuring | PMC13367958 (OA XML) | new (not in registry) | 2 |
| 39963730 | Kondo 2025 | A review of the putative antiseizure and antiepileptogenic mechanisms of action for soticlestat | Soticlestat (CH24H/CYP46A1) mechanism review: a cholesterol-turnover lever already tested in DEE; testable lesson is the cholesterol-excitability link | PMC12097479 (OA XML) | new (not in registry) | 3 |
| 41815956 | Eberhart 2026 | Dysregulated lipid metabolism and hypomyelination in postnatal peroxisome-deficient Pex2 knockout Zellweger mice | Pex2-null (Zellweger) mice: dysregulated lipid metabolism with postnatal hypomyelination: peroxisome comparator | PMC12971716 (OA XML) | new (not in registry) | 3 |
| 40997116 | Ziegler 2025 | Individual lipid alterations at the origin of neuronal Ceramide Synthase defects | Which individual lipid species drive neuronal ceramide-synthase defects: methods lesson for lipidomics in a Wwox-null brain | PMC12500085 (OA XML) | new (not in registry) | 3 |
| 41704776 | Sahu 2026 | From lipid function to dysfunction: Very long-chain fatty acids as emerging regulators of neuroinflammatory pathways | VLCFA as regulators of neuroinflammatory pathways: bridges the neuroinflammation/microglia finding (P47T, Hussain) to lipid | PMC12907123 (OA XML) | new (not in registry) | 3 |
| 36969404 | Siddiqui 2023 | Therapeutic Role of ELOVL in Neurological Diseases | Review of ELOVL enzymes in neurological disease: map of which elongase defects give epilepsy/hypomyelination | PMC10034982 (OA XML) | new (not in registry) | 3 |

### HELD with a partial receipt (not selected; re-read only with a stated question)

| PMID | Note |
|---|---|
| 35460704 | Dong 2022: partial receipt FTR-20261004-35460704-02; owed = figure panels as images (captions only), reference list. A re-read would only be justified by a question about the LDLR panel; not recommended. |
| 33612478 | Liu 2021 (TUBB-WWOX, dyslipidemia): partial receipt FTR-20261003-33612478-01; owed = figures (captions only), supplementary (captions only), references. Not recommended without a stated question. |
| 33914858 | Repudi 2021 (neuronal Wwox deletion, myelin defects): latest receipt FTR-20261003-33914858-03 shows no owed section on the audited surface; an earlier surface was partial (abstract, intro, discussion, references not read). Supplementary unavailable. Re-read only to confirm myelin gene-set detail for the lipid question. |

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 24916532 | Ahmadzadeh 2014 (review, genes in low HDL-C): no PMCID, no open link; WWOX is one gene among many. |
| 30468910 | Piko 2019 (HDL-C SNPs incl. WWOX in Hungarian/Roma): no PMCID, subscription only. |
| 26238973 | Nizamuddin 2015 (THSD7A and obesity; WWOX BMI association was set aside by the authors): Unpaywall lists a Nature-hosted PDF, not verified; low value because WWOX is excluded from the analysis. |

### Questions this batch could change

1. Does Wwox-null (or P47T/hypomorph) brain show altered very-long-chain sphingolipid or cholesterol content in myelin, and is that a plausible driver of the hypomyelination already recorded (CerS2, ELOVL1, Pex2 comparators)? If lipidomics in the cited models are normal, the lipid arm of RL-003 can be closed.
2. Is the HDL-C association (Saez 2010, Lee 2008, Leduc 2011) carried by heterozygous loss, and does any human or mouse data show a lipid phenotype in biallelic LoF? This decides whether lipid biomarkers belong in a WOREE panel at all.
3. Does WWOX loss alter oleate/MUFA pools (Liu S 2024), and does that matter outside tumour macrophages?
4. Is the cholesterol-turnover route (CH24H/soticlestat) mechanistically reachable in a WWOX-LF model, or is it unrelated to the excitability defect?
5. Is the WWOX SDR domain plausibly a lipid-elongation or steroid-metabolism enzyme (Richards 2015; steroidogenesis arm already read), so that an SDR-dead hypomorph differs from a null in lipid terms?

## Group G2 simple carbohydrates, HIF1A, hypoglycaemia and ketogenic-diet angles

Count selected: 16 (tier column: 1 highest priority).

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 33520443 | Baryla 2021 | Identification of a novel association for the WWOX/HIF1A axis with gestational diabetes mellitus (GDM) | WWOX/HIF1A transcript ratio in leukocytes of 135 pregnant women, GDM vs not: the only human glycaemia-state measurement of the axis | PMC7811782 (OA XML) | new (mentioned in queue/registry as GDM association record; own receipt: none) | 1 |
| 31145772 | Permana 2019 | East Asian Genome-wide association study derived loci in relation to type 2 diabetes in the Han Chinese population | WWOX rs17797882 associates with lower HOMA-beta and higher TG/HDL in Han Chinese: a beta-cell/insulin-secretion trait for WWOX variation | publisher PDF at frontierspartnerships (served; EPMC licence field CC BY-SA); no PMC | new (not in registry) | 1 |
| 29481666 | Teslovich 2018 | Identification of seven novel loci associated with amino acid levels using single-variant and gene-based tests in 8545 Finnish men from the METSIM study | WWOX rs9937914 associates with serum alanine in 8545 Finnish men: alanine = glucose-alanine cycle readout | PMC5905595 (PMC page only, no XML) | new (registry mention only) | 2 |
| 33854788 | Ouyang 2021 | Metabolome-Genome-Wide Association Study (mGWAS) Reveals Novel Metabolites Associated with Future Type 2 Diabetes Risk and Susceptibility Loci in a Case-Control Study in a Chinese Prospective Cohort | Prediabetic metabolome GWAS: WWOX locus (rs72487966) associates with leucine/isoleucine, which predict T2D | PMC8025395 (OA XML) | new (not in registry) | 2 |
| 36530994 | Chu 2022 | WWOX-rs13338697 genotype predicts therapeutic efficacy of ADI-PEG 20 for patients with advanced hepatocellular carcinoma | WWOX-rs13338697 genotype predicts response to ADI-PEG 20 (arginine deprivation): a WWOX-genotype-dependent metabolic vulnerability | PMC9756969 (OA XML) | new (registry "not_processed", no receipt) | 3 |
| 41007296 | Baryla 2025 | Prognostic Significance of WWOX/HIF1A Ratio in Cancer Subtypes: Insights into Metabolism, ECM, and EMT | WWOX/HIF1A ratio across tumours with metabolism/ECM/EMT pathway analysis: extends the ratio idea; tests how ratio-driven metabolic states differ by tissue (incl. glioma) | PMC12467568 (OA XML) | new (log "background_only, abstract-only"; no receipt) | 2 |
| 40831798 | Hu 2025 | Progress of ketogenic diet in the treatment of developmental epileptic encephalopathy | Review: ketogenic diet in DEE by aetiology: sets the prior against which the 3-of-5 WOREE responders should be read | PMC12358386 (OA XML) | new (not in registry) | 1 |
| 40659031 | Joshi 2025 | A primary mechanism for efficacy of the ketogenic diet may be energy repletion at the tripartite synapse | Proposes KD acts by energy repletion at the tripartite synapse: the competing mechanism to a Warburg-correcting rationale | PMC12288115 (OA XML) | new (not in registry) | 1 |
| 41830506 | Klepper 2026 | "Not always the magic bullet"-Insufficient seizure control by ketogenic dietary therapies in Glut1 Deficiency Syndrome | KD fails to control seizures in a share of GLUT1-DS: limits of KD even when the energy defect is known | PMC13238889 (OA XML) | new (not in registry) | 2 |
| 42047543 | Pain 2026 | Energy metabolism, adenosine, and glutamate signaling reprogramming by decanoic acid in Glut1 disorder syndrome | Decanoic acid reprograms energy, adenosine and glutamate signalling in a Glut1 model: non-ketone route to KD-like effect | PMC13238624 (OA XML) | new (not in registry) | 2 |
| 33363507 | Fei 2020 | Metabolic Control of Epilepsy: A Promising Therapeutic Target for Epilepsy | Review: metabolic control of epilepsy (glycolysis, lactate, mTOR, AMPK): checklist of metabolic nodes to test in Wwox-null | PMC7753014 (OA XML) | new (not in registry) | 3 |
| 39876842 | Kuang 2024 | The lactate metabolism and protein lactylation in epilepsy | Lactate metabolism and lactylation in epilepsy: lactate is the one WWOX-loss readout that held across conditions (audit s10) | PMC11772370 (OA XML) | new (not in registry) | 2 |
| 39997753 | Beltran-Velasco 2025 | Brain Glycogen-Its Metabolic Role in Neuronal Health and Neurological Disorders-An Extensive Narrative Review | Brain glycogen review: glycogen is the unprobed buffer in WWOX-null hypoglycaemia (GSK3B arm of WWOX biology) | PMC11857135 (OA XML) | new (not in registry) | 3 |
| 37907746 | Li 2023 | Ketohexokinase-dependent metabolism of cerebral endogenous fructose in microglia drives diabetes-associated cognitive dysfunction | Ketohexokinase-dependent fructose metabolism in microglia drives cognitive dysfunction: fructose arm for a model with microglial activation | PMC10689812 (OA XML) | new (not in registry) | 3 |
| 40500435 | Wang 2025 | Early life high fructose impairs microglial phagocytosis and neurodevelopment | Early-life high fructose impairs microglial phagocytosis and neurodevelopment: developmental-window fructose effect | PMC7617807 (OA XML) | new (not in registry) | 3 |
| 42171828 | Cornelio-Martinez 2026 | Hypoxia inducible factor-1α-driven signaling networks regulating adult neurogenesis via Notch, Wnt, and MAPK pathways | HIF-1a networks in adult neurogenesis via Notch, Wnt, MAPK: neural HIF1A biology missing from the fibroblast/muscle/liver arc | PMC13197301 (OA XML) | new (not in registry) | 3 |

### HELD with a partial receipt (not selected; re-read only with a stated question)

| PMID | Note |
|---|---|
| 35328751 | Baryla 2022 (WWOX/HIF1A axis, fibroblasts): partial; owed = figure panels (captions only), Figures S1-S6 (unavailable: Europe PMC supplementaryFiles returned HTTP 500), references. |
| 42589397 | Hammouz 2026 (WWOX/HIF1A balance, breast/ovarian): partial; owed = figures and supplementary not read (latest receipt FTR-20260928-42589397-04 lists more sections not read; check the ledger before any claim). |

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 40198927 | Tang 2025 (WWOX/P73/HIF-1a in gallbladder cancer glycolysis) and its corrigendum 40263068: queue FT-015 = `unrecoverable_by_these_routes`; licence field says CC BY but no body was reachable. |
| 23765596 | Dayan 2013 (FRA16D/WWOX and metabolic reprogramming): no PMCID, subscription. |
| 21767287 | Chang 2012 (T2D GWAS replication including MAF/WWOX): no PMCID; the Unpaywall link returned was an unrelated contract PDF. |

### Questions this batch could change

1. Is the WWOX/HIF1A glycolytic shift measurable in any human state (GDM leukocytes, Baryla 2021) or neural cell, and does the direction match the fibroblast result? A negative would narrow the ketogenic rationale further.
2. Do the WWOX human-genetics hits (HOMA-beta, alanine, leucine/isoleucine, TG/HDL; Permana, Teslovich, Ouyang) point to insulin secretion or amino-acid handling, which suggest different biomarkers than lactate?
3. Against which prior should the 3-of-5 WOREE ketogenic responders be read (Hu 2025 by-aetiology review; Klepper 2026 limits)? Is energy repletion at the synapse (Joshi 2025) a better rationale than Warburg reversal?
4. Is brain glycogen/GSK3B (glycogen synthase kinase arm of WWOX biology) a missed buffer in the hypoglycaemic Wwox-null mouse?
5. Does fructose/KHK metabolism in microglia (Li 2023, Wang 2025) matter for a Wwox-null brain with activated microglia, or is it only a diet-exposure question?

## Group G3 mitochondria and iron

Count selected: 16 (tier column: 1 highest priority).

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 26355344 | Sze 2015 | A cascade of protein aggregation bombards mitochondria for neurodegeneration and apoptosis under WWOX deficiency | Wwox-null aggregation cascade (TRAPPC6A-delta, TIAF1, tau) bombards mitochondria: the primary WWOX-null mitochondria-in-neurons paper | PMC4650446 (OA XML) | HELD-partial: receipt FTR-20260920-26355344-01 covers introduction+discussion only; results, methods, figures, tables not read | 1 |
| 36364214 | Liu 2022 | WWOX Modulates ROS-Dependent Senescence in Bladder Cancer | WWOX regulates ROS and ROS-dependent senescence in bladder cancer models: direct WWOX-ROS intervention data | PMC9657618 (OA XML) | new (registry "not_processed", no receipt) | 1 |
| 35571988 | Li 2022 | Mitochondrial 1555 G>A variant as a potential risk factor for childhood glioblastoma | Nuclear-encoded mitochondrial gene variant in WWOX (rs62036057) associates with childhood glioblastoma (OR 2.99) alongside mtDNA 1555G>A: a human-genetics WWOX-mitochondria hit | PMC9092641 (OA XML) | new (not in registry) | 1 |
| 25595191 | Lo 2015 | Regulation of cell signaling and apoptosis by tumor suppressor WWOX | Review of WWOX in cell signalling and apoptosis (mitochondrial translocation, pTyr33): consolidates the mitochondrial-localisation claims | PMC4935227 (PMC page/PDF only, no XML) | new (registry "not_processed") | 2 |
| 42434280 | Ganapathy 2026 | A hub for an herb: is STAT3 blockade at the epicenter of toosendanin-induced NCOA4-dependent ferritinophagy and ferroptosis in cancer cells? | Commentary on toosendanin-induced NCOA4-dependent ferritinophagy; the toosendanin-WWOX ferroptosis arc (PMID 39894307, paywalled) is the one iron/WWOX link; WWOX is not in the abstract, check body | PMC13350003 (OA XML) | new (not in registry) | 2 |
| 40808923 | Xu 2025 | Ferroptosis and epilepsy: bidirectional pathogenic links and therapeutic implications | Review: ferroptosis and epilepsy, bidirectional links: frames iron/lipid-peroxide readouts for a seizure phenotype | PMC12344419 (OA XML) | new (not in registry) | 1 |
| 41822170 | Petrillo 2026 | Molecular mechanisms underlying the ferroptosis-induced epileptiform activity in mouse cortical slices | RSL3 ferroptosis induction produces interictal discharges in cortical slices: ferroptosis can itself be excitatory, an assay transferable to Wwox-null slices | PMC12975598 (OA XML) | new (not in registry) | 2 |
| 42601505 | Puertas-Frias 2026 | Polyunsaturated fatty acid sequestration protects against mitochondrial dysfunction-induced ferroptosis | OXPHOS deficiency drives PUFA-triacylglycerol storage in lipid droplets that protects against ferroptosis: joins mitochondria, lipid droplets and ferroptosis in one testable chain | PMC13601559 (OA XML) | new (not in registry) | 2 |
| 39995090 | Liang 2026 | Hypoxia-inducible factor 1α inhibitor reduces hippocampal neuronal ferroptosis | HIF-1a inhibitor reduces hippocampal neuronal ferroptosis: links the HIF1A axis of WWOX to ferroptosis in hippocampus | PMC13211804 (OA XML) | new (not in registry) | 2 |
| 38570643 | Kawabata 2024 | Chronic replication stress invokes mitochondria dysfunction via impaired parkin activity | Replication stress at the fragile-site gene PARK2 impairs parkin and mitochondrial homeostasis: closest structural analogue to WWOX (fragile-site gene, mitochondria) | PMC10991263 (OA XML) | new (not in registry) | 1 |
| 34354738 | Munk 2021 | Large Intronic Deletion of the Fragile Site Gene PRKN Dramatically Lowers Its Fragility Without Impacting Gene Expression | Large intronic deletion lowers PRKN fragility without changing expression: asks whether fragility itself, not loss, matters | PMC8329550 (OA XML) | new (not in registry) | 3 |
| 27066568 | Schule 2015 | Is PARKIN parkinsonism a cancer predisposition syndrome? | Is PARKIN parkinsonism a cancer predisposition syndrome? Fragile-site gene with neuro and tumour phenotypes: same two-sided question as WWOX | PMC4811379 (OA XML) | new (not in registry) | 3 |
| 25833766 | Ambroziak 2015 | Genomic instability in the PARK2 locus is associated with Parkinson's disease | Genomic instability in the PARK2 locus associates with Parkinson disease: fragile-site instability as a neuro risk | PMC4617850 (OA XML) | new (not in registry) | 3 |
| 41002898 | Truong 2025 | Mitochondria-Associated Membrane Dysfunction in Neurodegeneration and Its Effects on Lipid Metabolism, Calcium Signaling, and Cell Fate | Mitochondria-associated membrane dysfunction in neurodegeneration (lipid metabolism, Ca2+ signalling): MAM frame for the WWOX Ca2+ and mitochondrial findings | PMC12471380 (OA XML) | new (not in registry) | 2 |
| 34937577 | Zhang 2021 | Mitophagy in neurological disorders | Mitophagy in neurological disorders: baseline for the open mitophagy-versus-senolytic hypothesis (WM item 010) | PMC8693476 (OA XML) | new (not in registry) | 3 |
| 42219438 | Bjorklund 2026 | Iron dysregulation in the central nervous system: implications for autism spectrum disorder | Review of CNS iron dysregulation (ASD): the only iron-in-neurodevelopment review found; iron is entirely absent from the repo | PMC13518416 (OA XML) | new (not in registry) | 3 |

### HELD with a partial receipt (not selected; re-read only with a stated question)

| PMID | Note |
|---|---|
| 35984507 | Carvalho 2022 (Zfra1-31, mitochondria, high glucose): two partial receipts, owed = figure panels only. Revival trigger recorded in the registry: a report of total WWOX beside pTyr33-WWOX. |
| 41677633 | Su 2026 (WWOX induction, Bcl-xL/Mcl-1 degradation, ROS under serum deprivation): partial; owed = figure panels (captions only). |
| 27551439 | Chang 2015 (TRAPPC6A-delta aggregation, mitochondrial shuttling): partial; owed = supplementary (captions only). |
| 26355344 | Sze 2015 is listed in the main table because its receipt covers only introduction and discussion. |

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 26390919 | Choo 2015 (WWOX moderates the mitochondrial respiratory complex, Drosophila): queue FT-006 = `unrecoverable_by_these_routes`. Highest-value blocked item for this group. |
| 39894307 | Yang 2025 (WWOX p53/SAT1 and NRF2/FPN1 axis, toosendanin ferroptosis in HCC; FPN1 = ferroportin): no PMCID, subscription. The only WWOX-iron-export link found. |
| 41443103 | Wang 2026 (WWOX protects against ferroptosis in acute lung injury via p53 deacetylation): subscription. |
| 36621327 | Wang 2023 (WWOX, autophagy and mTOR in acute lung injury): subscription. |
| 15664696 | Chen 2005 (light-induced retinal damage, WOX1 mitochondrial translocation): queue = `unrecoverable_by_these_routes`. |
| 18403180 | Hsu 2008 (Zfra inhibits Bcl-2 and cytochrome c release): subscription. |

### Questions this batch could change

1. Is the Sze 2015 mitochondrial aggregation cascade (the only neuronal WWOX-null mitochondria data) supported by its Results and figures, which no receipt covers? This decides how much weight the mitochondrial arm of claim 009 can carry in neurons.
2. Does WWOX loss sensitise to ferroptosis (toosendanin arc, lung injury papers: body access needed) and is there any iron readout at all in WWOX-LF models? The model is currently silent.
3. Does fragile-site gene biology (PARK2/PRKN: replication stress to mitochondrial dysfunction) offer a testable template for WWOX, and does the WWOX rs62036057 mitochondrial-gene hit replicate?
4. Can ferroptosis itself drive epileptiform activity (Petrillo 2026) in a way testable in Wwox-null slices?
5. Is the MAM/Ca2+ frame (Truong 2025) a better explanation of WWOX Ca2+ and bubbling-death findings than direct mitochondrial dysfunction?

## Group G4 catecholamines and neurotransmitters

Count selected: 19 (tier column: 1 highest priority).

| PMID | First author, year | Title (PubMed) | Why it matters | Body route | Registry status | Tier |
|---|---|---|---|---|---|---|
| 37328865 | Wainberg 2023 | Shared genetic risk loci between Alzheimer's disease and related dementias, Parkinson's disease, and amyotrophic lateral sclerosis | WWOX is one of five loci shared by ADRD and Parkinson disease: human-genetics link from WWOX to the dopaminergic/PD axis | PMC10273745 (OA XML) | new (not in registry) | 1 |
| 35053314 | Ferraro 2022 | Correcting Differential Gene Expression Analysis for Cyto-Architectural Alterations in Substantia Nigra of Parkinson's Disease Patients Reveals Known and Potential Novel Disease-Associated Genes and Pathways | Substantia-nigra expression in PD, corrected for cell composition: WWOX among genes retained as neurodegeneration players | PMC8774027 (OA XML) | new (registry mention only) | 2 |
| 40139278 | Yuan 2025 | Influence of WWOX/MAF genes on cognitive performance in patients with Parkinson's disease | WWOX/MAF variants and cognition in Parkinson disease: WWOX genotype in a dopamine-deficit population | DOI landing (EPMC licence field CC BY-NC-ND; body fetch NOT tested; no PMC) | new (registry "not_processed") | 2 |
| 17909041 | Aqeilan 2007 | Association of Wwox with ErbB4 in breast cancer | Wwox-ErbB4 association: ErbB4 is the WWOX partner that organises GABAergic interneuron synapses | Unpaywall-reported free publisher PDF (AACR); not fetched here; no PMC | new (corpus placeholder "screened", no receipt) | 3 |
| 37443770 | Ng 2023 | Dopamine Transporter Deficiency Syndrome (DTDS): Expanding the Clinical Phenotype and Precision Medicine Approaches | Dopamine transporter deficiency syndrome: infantile parkinsonism-dystonia phenotype and precision approaches; the differential for the neonatal parkinsonism-like WWOX case | PMC10341083 (OA XML) | new (not in registry) | 1 |
| 40291937 | Al Sari 2025 | A comparative exploration of monoamine neurotransmitter transport disorders: mechanisms, clinical manifestations, and therapeutic approaches | Comparison of monoamine transport disorders (dopamine, norepinephrine, epinephrine, serotonin): reference list of CSF/biochemical signatures | PMC12022732 (OA XML) | new (not in registry) | 2 |
| 42483444 | Naranjo-Lobo 2026 | Pediatric parkinsonism: clinical review and a proposed clinical algorithm | Pediatric parkinsonism review and algorithm: where a WWOX-LF child sits in the work-up | PMC13387017 (OA XML) | new (not in registry) | 2 |
| 40183510 | Sugiyama 2025 | Decreased homovanillic acid and 5-hydroxyindoleacetic acid levels in the cerebrospinal fluid of patients with Dravet syndrome with parkinsonism | CSF HVA and 5-HIAA are low in Dravet syndrome with parkinsonism: a DEE with a measured monoamine deficit, template for a WWOX CSF panel | PMC12163531 (OA XML) | new (not in registry) | 2 |
| 42643745 | Nikkhah 2026 | Identification of a Novel SLC18A2 Splicing Variant in a Case of Infantile Parkinsonism-Dystonia Type 2 | Novel SLC18A2 (VMAT2) splice variant, infantile parkinsonism-dystonia 2: vesicular monoamine storage disorder | PMC13505190 (OA XML) | new (not in registry) | 3 |
| 42245405 | Almutair 2026 | Case Report: Two siblings with a novel homozygous SLC18A2 variant causing parkinsonism-dystonia-2: a case series from Saudi Arabia | Two siblings with homozygous SLC18A2 variant, parkinsonism-dystonia 2: second VMAT2 phenotype series | PMC13233055 (OA XML) | new (not in registry) | 3 |
| 38330420 | Bian 2024 | Hypothalamic-Pituitary-Adrenal Axis and Epilepsy | HPA axis and epilepsy: stress-axis review (stress hormones as seizure triggers); WWOX-null mice have impaired steroidogenesis (Aqeilan 2009, read) | PMC10921057 (OA XML) | new (not in registry) | 2 |
| 41470225 | Abdygalyk 2025 | Infantile Spasms (West Syndrome): Integrating Genetic, Neurotrophic, and Hormonal Mechanisms Toward Precision Therapy | Infantile spasms: genetic, neurotrophic and hormonal mechanisms (ACTH/steroid axis; GRIN, STXBP1 genes) | PMC12734430 (OA XML) | new (not in registry) | 2 |
| 42782811 | Bagyinszky 2026 | ERBB4 and Neurodegeneration: Association Between Hypothalamic-Pituitary-Adrenal (HPA) Axis: Associated Neurodegenerative Pathogenesis | ERBB4, the WWOX partner, linked to HPA-axis-associated neurodegeneration: joins partner biology to the stress axis | PMC13605197 (OA XML) | new (not in registry) | 2 |
| 32546684 | Shi 2020 | Neuregulin 1: an intriguing therapeutic target for neurodevelopmental disorders | Neuregulin-1 (ErbB4 ligand) as a target in neurodevelopmental disorders: interneuron/synaptic arm of the WWOX-ErbB4 partnership | PMC7297728 (OA XML) | new (not in registry) | 3 |
| 39641935 | Stevering 2025 | Vigabatrin-associated brain magnetic resonance imaging abnormalities and clinical symptoms in infants with tuberous sclerosis complex | VABAM in infants with tuberous sclerosis on vigabatrin: risk and course; comparator for the WWOX VABAM reports (Choi 2026, read) | PMC11827727 (OA XML) | new (not in registry) | 2 |
| 39570186 | Sathe 2025 | Symptomatic vigabatrin-associated MRI toxicity is associated with simultaneous hormonal therapy among patients with infantile spasms | Symptomatic VABAM is associated with concurrent hormonal (ACTH/steroid) therapy in infantile spasms: ties the vigabatrin safety signal to the adrenal axis | PMC11803263 (OA XML) | new (not in registry) | 1 |
| 41573381 | Alammary 2026 | Identification of Additional Cases of Severe Neonatal GABA-Transaminase Deficiency | Severe neonatal GABA-transaminase deficiency: the genetic mirror of vigabatrin (GABA excess) and a neonatal GABA-excess phenotype | PMC12820413 (OA XML) | new (not in registry) | 2 |
| 41977367 | Dumitrescu 2026 | Chloride Homeostasis Failure in Human Disease: KCC2/NKCC1 Microdomain Dysfunction as a Driver of Cortical Network Collapse | KCC2/NKCC1 microdomain failure in human disease: the working model records depolarising GABA as unmeasured (2026-09-27) | PMC13073762 (OA XML) | new (not in registry) | 2 |
| 41914335 | Li 2026 | Serotonin Associated Mechanisms in Sudden Unexpected Death in Epilepsy: A Review | Serotonin mechanisms in SUDEP: serotonergic/respiratory arm of early death in WOREE | PMC13036788 (OA XML) | new (not in registry) | 3 |

### HELD with a partial receipt (not selected; re-read only with a stated question)

| PMID | Note |
|---|---|
| 33958783 | Liu 2021 (survival GWAS, TMEM108/WWOX progression loci): partial; owed = supplementary data; WWOX locus is an AD progression signal, not a neurotransmitter finding. Not selected. |
| 24308844 | Schuchardt 2013 (WWOX WW1 binding to ErbB4 ICD): partial, two receipts; owed = figures, limitations, methods, tables. Not selected (binding biophysics; would not change a model question). |
| 38542478, 33195192, 37897534, 30158849 | partial with figures-only debt; outside the four themes. |

### BLOCKED (no lawful body found; do not select)

| PMID | Note |
|---|---|
| 18371080 | Lo 2008 (MPP+ neuronal death involves WOX1 Tyr33 phosphorylation; dopaminergic toxin): no PMCID, subscription. Highest-value blocked item for this group. |
| 16061658 | Aqeilan 2005 (WWOX and YAP compete for ErbB4): no PMCID, no free route found. |
| 39322821 | Liu 2025 (HTR3 serotonin-receptor genes and childhood ALL; WWOX appears only as a prior GWAS gene): subscription and off-theme. |

### Questions this batch could change

1. Is the neonatal-parkinsonism-like WWOX case a neurotransmitter-disorder mimic with a measurable CSF monoamine (HVA/5-HIAA) signature, as in Dravet with parkinsonism (Sugiyama 2025), or a structural/hypomyelinating phenotype? A CSF panel result would split the two.
2. Does the WWOX locus' presence among the ADRD/PD shared loci (Wainberg 2023) and in nigral expression data (Ferraro 2022) imply a dopaminergic vulnerability, or is it a general neurodegeneration signal?
3. Does the vigabatrin safety signal (VABAM) track with concurrent ACTH/steroid therapy (Sathe 2025), and is the WWOX-null impairment of steroidogenesis relevant to that interaction?
4. Can the competing accounts of GABAergic vulnerability be separated using chloride-homeostasis (KCC2/NKCC1) and GABA-transaminase biology, given the model records depolarising GABA as unmeasured?
5. Is the WWOX partner ErbB4 (NRG1 signalling, HPA-axis link) the missing mechanistic bridge between interneuron loss and the stress/adrenal axis?

## What the repo already holds per theme

- Glucose / HIF1A (group 2): the fullest coverage. `disease-models/wwox/analysis/wwox_metabolism_reviews_audit_20260921.md` concludes the HIF1A/glycolysis arc holds only at HYPOTHESIS strength: measured in fibroblasts, muscle, liver, flies and cancer lines, never in neural tissue or development; lactate is the one readout that held in all four conditions (s10.1); OXPHOS suppression was not shown in human cells (s10.2); the ketogenic and dichloroacetate hypotheses may not assume it. `research_lines_current.md` RL-003 ("WWOX as bioenergetic governor") lists its own next action as "look for CNS-specific data and useful metabolic biomarkers". Working model: metabolic branch (line 79), claims 009, 025, 042 (WWOX/HIF1A state marker; ketogenic-diet case series, 3 of 5 responders, number exposed not stated). Reading depth is already complete for Abu-Remaileh 2014/2015/2018/2019 and Baryla 2022 (review); partial (figures/supplement) for Baryla 2022 (axis paper) and Hammouz 2026.
- Mitochondria (group 3): working model claim 009 (mitochondrial quality control, redox, energy efficiency: inference, with counter-directional evidence recorded as CLAIM 034) and item 010 (mitophagy versus senolytics: hypothesis). The audit s7 treats mitochondria as secondary, a fly result and a review sentence. Read: O'Keefe 2011 (Drosophila respiratory chain), Dudekula 2010 (Zfra). Iron, ferroptosis, heme, anaemia: no hit in the working model; the only repo trace is the unread toosendanin papers (Yang 2025; Wang 2026).
- Lipids (group 1): the working model has no lipid or cholesterol text (one `HDL` hit). The HDL genetics papers (Lee 2008, Iatan 2014, Aldaz 2014, Li 2014) are fully read; Dong 2022 carries a DO_NOT_CITE note (four heterozygous WWOX "occurrences" are three distinct missense alleles, no LoF, burden test not significant, no lipid values for carriers). Myelin is modelled (11 hits; Repudi 2021, Tochigi 2019, Abudiab 2025 preprint, all read or partially read) but its lipid composition is not. Queue entry FT-019 (Leduc 2011, MEDIUM) has waited since 2026-07-26.
- Neurotransmitters (group 4): GABA and vigabatrin are modelled (working model ACTIVE 2, claim 001 conflicting VABAM evidence, Choi 2026 versus You 2024; line 115: GABA-depolarising rationale is "unmeasured", competing accounts of GABAergic vulnerability). Hussain 2019 (GABAergic interneuron loss) and Breton 2021 (hyperexcitability) are read; the neonatal-parkinsonism WWOX case (Serce Pehlevan 2026) is read (every section; only citations partial). Dopamine, catecholamine, adrenal, serotonin and glutamate: no working-model text.

## Caveats

- Abstracts and metadata were read; no full text was read in this selection. "Why it matters" lines are abstract-level and mark what the Scientist should test, not what the paper has shown.
- Group 4's transferable rows (tier 2-3) are comparators and differential-diagnosis references; the WWOX-direct neurotransmitter reading is largely complete in the repo, so G4 is the weakest group for new WWOX evidence. The Orchestrator may reasonably merge its tier-3 rows into a shorter list.
- PMC page/PDF only routes (Leduc 2011, Richards 2015, Lo 2015, Teslovich 2018) have no XML; the Scientist may need a browser or operator-supplied PDF, with the usual `FULLTEXT_READ_RECEIPT` rules.
- Yuan 2025 (EPMC licence field CC BY-NC-ND) and Aqeilan 2007 (Unpaywall-reported free PDF) were not body-fetched; treat their routes as unconfirmed.
