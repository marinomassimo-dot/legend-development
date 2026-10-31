# IT12 P2-P47T: what the P47T knock-in brain deposit says about the HIF and NRF2 target sets (K01 reopening question)

Scientist `scientist-d`, 2026-10-31 UTC (communication to the operator is in Europe/Rome), package P2-P47T, branch `task/it12-p47t` from main `0243d452`. Non-canonical research material. **Not medical advice; no compound, dose, route or schedule is recommended or scored.** Reference genotype: a WWOX-DEE genotype class; no individual-level record. No account, registration, contact address or personal datum was used or sent to any service; the submitter contact details in the GEO record were not copied. Nothing outside this folder was edited; edits to cards, needs and registries are proposed in `proposals/` only. Guard tags bind (`IT7_READOUT6`, `ISR_SIGN_UNRESOLVED`, `HELD_OUT_ENDPOINT`): SLC2A1, HK2, LDHA, LDHB, BNIP3 and PDK1 appear as observations only and decide nothing.

## 0. Decision (first)

| Question | Result |
|---|---|
| What do Fig 8b and Fig 9c show? | **Enrichment, not depletion.** All hallmark bars are positive. Pixel-measured NES (about +/-0.03): HYPOXIA HPC 2.01, CTX 1.53, PFC 1.50; GLYCOLYSIS 1.48, 1.27, 1.36; APOPTOSIS 1.77, 1.33, 1.41 (Fig 8b); cerebellum (Fig 9c): ROS pathway 2.04 (4th of ten bars), APOPTOSIS 1.78, GLYCOLYSIS 1.27, HYPOXIA 1.21 (the lowest of the ten). **Not stated anywhere:** the sign convention of Fig 8b (supported indirectly), adjusted p, ranking metric, hallmark release, permutations. No hallmark table exists in the paper or its supplements. |
| Does the deposit allow a limited reanalysis? | **Yes, with stated limits.** GSE215425 holds integer count tables for all 37 libraries (HPC, CTX, PFC 5 v 5; CB 4 v 3; homozygote vs WT; animals are the units). It supports transcript-level questions only. No HIF protein, hydroxylation, oxygen condition, lactate, per-animal seizure record or age (150-280 d range) exists. |
| Is the organoid's selective hypoxia-response pattern present in P47T? | **No.** Of the organoid-up non-IT7 genes only Adm is higher in all four regions (+0.4 to +1.2 log2, 1.7-2.4 CPM, p 0.04-0.18). Bhlhe40 and Ndrg1 fall (-0.2 to -0.8), Ddit4, Ankrd37 flat, Egln3 mixed. Set HIF_SEL_UP6: HPC +0.22, CTX +0.11, PFC -0.07, CB +0.19 (exact p 0.32, 0.70, 0.67, 0.057); selectivity contrast not met anywhere. The one organoid-like hippocampal signal is carried by one animal (drop P47T M6: +0.05). |
| What drives the hallmark HYPOXIA/GLYCOLYSIS enrichment then? | **A broad, modest shift of many hallmark members, led by glycolytic-enzyme transcripts** (Aldoa, Pgk1, Pfkp, Pkm, Tpi1, Hk2, Ldha: +0.1 to +0.6 log2; the six "flat in organoid" genes have set means +0.12, +0.25, +0.12 in the forebrain) with extracellular-matrix/reactive genes among the larger changes (Serpine1, Cd44, Ccn2, Lox, Cav1, Stc2). Opposite to the organoid (flat) and to the P17 contrasts (lower). My independent re-run of GSEA reproduces the authors' bars (HYPOXIA 2.07/1.63/1.81, bars 2.01/1.53/1.50). This is a broad modest shift, not HIF-selective; it also survives removal of the IT7 six and of declared glia/IEG genes. |
| NRF2 set | **Modestly higher in all four regions** (set +0.33 HPC, +0.19, +0.19, +0.17; Hmox1 and Srxn1 up in all four, Nqo1 mixed, Gclm/Txnrd1 flat) and it **tracks the astrocyte marker score** across animals (Spearman 0.56-0.88 forebrain). Hallmark ROS pathway is a cerebellar (4 v 3) finding with an oligodendrocyte/myelin component. |
| Does this satisfy the K01 reopening condition? | **No in substance, yes in form.** None of (i)-(vi) of IT10 section 5.3 is met (no protein, activity, lactate, single-cell, replicated hNPC, HIF-2alpha report). It is "a different question on a deposit never analysed with these sets". The documentary search for HIF protein/activity **stays closed**; the transcript datum is integrated. |
| Does it change K01 / L01? | **K01: NARROW and SEPARATE the hypotheses; no strengthening, no change of the experiment's structure.** The premise "a HIF-linked selective shift exists in WWOX-deficient neural tissue" now rests on one human organoid dataset (4 v 2) against five in-vivo mouse transcript contrasts (4 P17 deletion, 1 P47T hypomorph) that do not reproduce it. Three hypotheses stay apart: H-org (organoid state/oxygen/MYC or a WWOX-HIF effect), H-act (activity/seizure-linked metabolic programme, which would raise glycolytic enzymes and immediate-early genes: seen), H-glia (composition). **L01: nothing changes** in selection or priority; a datum is added (modest NRF2-target increase, composition-confounded). |
| What would distinguish them? | Section 6: HIF-1alpha/2alpha protein by compartment with hydroxylation, pimonidazole and lactate, in mutant vs WT hippocampus fixed by perfusion, with per-animal seizure count as covariate, a pre-onset age group, and tetrodotoxin-silenced tissue; and, in human neural cells, 5% O2 with HIF1A/EPAS1 knockdown. |

## 1. What I had read before forming my questions (not blind)

* Before the task: CLAUDE.md, the common brief, state manifest READY (read at start), IT10 P2.1 README in full (`hif_it10_p21_20261031/`), its tables `maturity_stress_check_it10_p21.tsv` and `mouse_p17_hif_genes_it10_p21.tsv`, IT11 P2.3 README (`nrf2_it11_p23_20261031/`), the K01 card, `guards.tsv`, S027 in `seeds.tsv`.
* The task text gave the sign and range of the NES (from the repository manifest). I then **viewed Figures 8 and 9 before any gene-level computation** and wrote `PRE_ANALYSIS.md` (committed first) before opening gene values. I had also seen the organoid and P17 values for the same genes in the IT10 tables, so the comparison with them is informed, not blind. The six IT7 genes' IT7-era HPC values (S027) were in the seeds file I had read.
* After the first run I added exploratory checks (listed in the PRE_ANALYSIS addendum). One pre-stated expectation was wrong (Q-D, minimum exact p for 3 v 4 is 0.029, and several CB genes reach it).

## 2. Task 1, at the source

Depth: **FULL-TARGETED** for the paper (Europe PMC fullTextXML of PMC10835625: Results 2.8, 2.9, Methods 4.14, Data availability, legends of Figs 6, 8, 9 read in full; remaining sections not read for this question); figures **viewed at full resolution and measured**; supplements read as listed.

**Access limits (recorded, not circumvented).** The PMC article page, PMC supplement links and the GEO disclaimer page returned a reCAPTCHA challenge to default-agent requests; Europe PMC image and supplement routes returned HTTP 403; the Europe PMC supplementaryFiles endpoint returned a one-member zip whose docx member is zero bytes. Figures and supplements were therefore read from the PMC-origin copies already in the shared corpus, read-only; the four NIHMS supplements there are md5-identical to the md5 values printed in the Europe PMC XML (`raw_hashes_it12.tsv`). Reopening condition: a plain fetch of the PMC page that returns the article instead of the challenge.

| Item | Fig 8b (forebrain) | Fig 9c (cerebellum) |
|---|---|---|
| Contrast | P47T/P47T vs WT/WT per region (legend of Fig 8a; convention for 8b not stated) | same; CB samples n = 4 WT, 3 P47T (Fig 9a legend), Methods say 5 per group |
| Animals | 5 v 5; Methods: "150-280 days of age, n = 5 mice/group (2 males and 3 females)"; deposit titles: WT 3M 2F, mutant 2M 3F | M3, M2, F5, F4 v M6, F8, F10 |
| Method | GSEA hallmark, clusterProfiler/enrichplot; metric, release, permutations not stated | same |
| Hallmark: NES | HYPOXIA 2.01 / 1.53 / 1.50 (HPC/CTX/PFC); APOPTOSIS 1.77 / 1.33 / 1.41; GLYCOLYSIS 1.48 / 1.27 / 1.36; TNFA 2.24/1.86/1.85; IL6 1.83/1.90/1.89; INFLAMMATORY 2.02/1.30/1.84 | OXPHOS 2.84, FATTY_ACID 2.60, ADIPOGENESIS 2.05, **REACTIVE_OXYGEN_SPECIES 2.04**, CHOLESTEROL 1.96, APOPTOSIS 1.78, INFLAMMATORY 1.78, IL6 1.36, GLYCOLYSIS 1.27, HYPOXIA 1.21 |
| Direction | positive NES = enriched in the mutant by convention; my re-run (P47T minus WT ranking) agrees | same |
| Adjusted p | **not reported** (no axis, no table, no supplement) | **not reported** |
| Counted as | one dataset: the three forebrain regions are the same 10 animals; the cerebellum libraries are from 7 of the same animals; DEG lists, Fig 8b/9c, the deposit and my re-run are one observation, not four | |

Text locators are in `premises.tsv` (P1-P5). The paper itself states the finding in the sentence: "hallmark gene set analysis also revealed hypoxia, apoptosis, and glycolysis pathways enrichment in all three brain regions (Fig. 8b)".

## 3. Usability check (before any analysis; `usability_check.tsv`)

Accessible (GEO FTP/HTTP key-less, public); terms page unreadable (captcha), series record has no licence field, use is public re-analysis with citation; sample identity consistent (animal names recur across regions and animal-level Nptx2/Bdnf patterns agree across regions, so no sign of swaps); perturbation is a partial-loss missense knock-in (Wwox transcript unchanged: -0.02 to -0.17 log2); contrast homozygote vs WT only, no rescue/add-back/age series; units animals, 5 v 5 and 4 v 3; tissue bulk dissected regions; confounders: gliosis and composition (authors' own BRETIGEA scores up for astro/micro, down for oligo), chronic seizures with no per-animal record, sex imbalance, age range, batch unknown, modest genotype separation (between/within distance ratio 1.2-1.4). Endpoint it can support: transcript pattern of target sets in a partial-loss epileptic brain. **Discrepancy found:** my edgeR-like log2FC reproduces the authors' DEG sheets for CTX, PFC and CB (r 0.97, 0.97, 0.999) but not for HPC (r 0.52; no relabelling of the 10 libraries reaches 0.50); the authors' HPC GSEA bars are nonetheless reproduced from the deposited HPC counts. Cause unresolved (different processing, sample set or ordering). HPC results here are from the deposit as deposited.

## 4. Task 2, the reanalysis (`results/`, script `p47t_reanalysis_it12.py`, deterministic seed 20261031, stdlib + numpy)

Method: TMM-style normalisation per region, log2 CPM (prior 2), per-animal set score = mean over set genes of centred log2 CPM; group difference with Welch t, **exact permutation over all animal label splits** (floor 0.008 for 5 v 5, 0.029 for 3 v 4), sex-adjusted OLS as sensitivity (conclusions unchanged), expression-matched random-gene null, leave-one-animal-out. Gene-level p are nominal and uncorrected over about 120 named-gene tests. GSEA is my re-implementation (pre-ranked Welch t, weight 1, gene-label permutation: anti-conservative with correlated genes, so I use direction and size, not q).

**Table A. Set means, P47T minus WT, log2 (exact permutation p)**

| Set | HPC | CTX | PFC | CB (4 v 3) |
|---|---|---|---|---|
| HIF_SEL_UP6 (Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3) | +0.22 (0.32) | +0.11 (0.70) | -0.07 (0.67) | +0.19 (0.057) |
| HIF_FLAT6 (Pgk1, Aldoa, Eno1, Pkm, Pfkp, Ndrg1) | +0.12 (0.071) | +0.25 (0.008) | +0.12 (0.063) | +0.04 (0.71) |
| SEL minus FLAT | +0.10 (0.68) | -0.14 (0.44) | -0.19 (0.22) | +0.14 (0.14) |
| NRF2_5 (Nqo1, Hmox1, Gclm, Srxn1, Txnrd1) | +0.33 (0.024) | +0.19 (0.135) | +0.19 (0.032) | +0.17 (0.029) |
| IT7 six (observation only) | +0.21 (0.032) | +0.14 (0.29) | +0.14 (0.008) | +0.12 (0.17) |

Declared rules (PRE_ANALYSIS): "HIF_SEL_UP6 up" (>= +0.30, p <= 0.05) not met in any region; "organoid-like selective" not met; "NRF2_5 up" met in HPC only; CTX HIF_FLAT6 (+0.25, p 0.008) is below the declared magnitude and reported as sub-threshold. Matched-null percentiles (`matched_null_it12.tsv`): CTX HIF_FLAT6 p 0.021, HPC 0.078; HPC NRF2_5 0.024; others above 0.05.

**Table B. Per gene, log2FC P47T over WT, HPC / CTX / PFC / CB, beside organoid (4 v 2) and P17 (carried values, `compare_it12.tsv`)**

| Gene | HPC / CTX / PFC / CB | Organoid log2 | P17 (4 contrasts; * animal-separated) |
|---|---|---|---|
| Adm | +0.96 / +1.19 / +0.81 / +0.36 | +2.60 | +0.54, +0.71*, -0.45, -0.63* (mixed) |
| Bhlhe40 | -0.22 / -0.43 / -0.77 / +0.04 | +1.26 | -0.81, -0.90*, -0.13*, -0.28 |
| P4ha1 | +0.31 / +0.27 / +0.33 / +0.12 | +1.48 | -0.99*, -0.68*, -1.28*, -1.04* |
| Ddit4, Ankrd37 | about 0 / +0.2 (Ankrd37 +0.29 CB) | +0.75, +0.91 | not in the P17 table |
| Egln3 | +0.37 / -0.11 / -0.27 / +0.13 | +0.82 | -0.65*, -0.06, -0.39*, -0.38* |
| Pgk1 | +0.27 / +0.39 / +0.23 / +0.22 | -0.09 | -0.26, -1.02*, -1.17*, -0.56 |
| Aldoa, Pkm, Pfkp, Eno1 | up in forebrain (+0.1 to +0.6) | +0.0 to +0.23 | not in the P17 table |
| Ndrg1 | -0.43 / -0.43 / -0.47 / +0.16 | +0.15 | -1.26*, -1.11*, -0.90*, -1.26* |
| Hmox1, Srxn1 | up in all four (+0.3 to +0.7) | +0.74, +0.41 | not in the table |
| Nqo1 | +0.35 / -0.16 / -0.01 / +0.42 | -0.45 | not in the table |
| Hif1a, Epas1 | flat (Epas1 -0.15, -0.23, +0.10, -0.19) | -0.24, +1.41 | Hif1a -0.20, -0.17, +0.03, +0.06*; Epas1 -0.43, -0.58*, -0.53*, -0.21* |

The three systems disagree at the level of which genes move (Adm is the exception: up in P47T and in two of four P17 contrasts): organoid = selective hypoxia-response genes up with glycolytic enzymes flat; P17 deletion = HIF targets flat to lower; P47T = glycolytic enzymes modestly up, selective genes not. No single HIF-activity account fits all three; I do not count the P47T and P17 datasets as confirmations of each other (different alleles, ages, background controls).

**Leading edge** (`leading_edge_it12.tsv`): HYPOXIA NES HPC 2.07, CTX 1.63, PFC 1.81, CB 1.06; of the 49-84 leading-edge genes in each forebrain region, 10-12 are in my declared canonical-HIF/glycolysis list (mostly enzymes), 1-6 glia-reactive, 2-5 immediate-early/stress, and the large majority (36-61) are other hallmark members (Gpc1, Chst2, Pam, Sdc2, Mif, ...); the enzymes and reactive genes are the top-ranked, not the bulk. Without the IT7 six: 2.03/1.59/1.70; also without declared glia/IEG genes: 1.94/1.60/1.68, so the enrichment is diffuse rather than carried by a few glial genes. It does not exclude a composition contribution spread over many genes.

## 5. Rivals kept apart

* **Transcript vs protein.** Everything here is mRNA. HIF stabilisation is post-translational and HIF1A/EPAS1 transcripts are flat or lower, which neither supports nor excludes it. The tissue was flash-frozen for RNA: HIF protein could not be recovered from it.
* **Hypoxia/stress/seizure vs WWOX-specific HIF stabilisation.** Two of five mutants (M6, F8) have Nptx2 and Bdnf 20-30 fold above WT in all three forebrain regions (identity check), and Nptx2 and Bdnf are in the authors' own DEG lists. The HPC HIF_SEL_UP6 shift disappears without M6 (+0.05), M6 also has the highest astrocyte score; across animals HIF_SEL_UP6 correlates with the activity-gene score (Spearman 0.75-0.84 in forebrain; within mutants 0.8-1.0, n = 5). This fits the activity rival (neuronal activity itself drives HIF-1alpha and glycolytic enzymes) and cannot be separated from it in this deposit: seizure timing before euthanasia is unrecorded. Designation of M6/F8 as high-activity is post hoc.
* **Partial loss vs null.** P47T keeps Wwox mRNA and the SDR domain and loses WW1-domain binding (the paper's "hypomorphic mutation"); it is not a model of the null-like lesions and its allele differs from the reference genotype class, so transfer is not warranted.
* **Composition vs intracellular change.** The authors report higher astrocyte/microglia and lower oligodendrocyte signatures (HPC, PFC; Fig 6c). In my small marker sets ASTRO is +0.59 in HPC, MICRO +0.26 PFC, OLIGO -0.51 CTX and -0.56 PFC. Ndrg1 and Bhlhe40 are, in my background knowledge (not verified here), expressed in oligodendroglia, so their decrease may be composition. The NRF2 target score tracks ASTRO across animals. In cerebellum, Mbp/Mobp and the OLIGO score are higher, and the hallmark ROS set leading edge includes Mbp.
* **Single dataset.** Fig 8b, Fig 9c, the DEG sheets, GSE215425 and my re-run are the same 10 animals (cerebellum 7 of them).
* **Nominal statistics.** n = 5 v 5; gene-level p are uncorrected; the HPC DEG-list discrepancy is unresolved; HIF_SEL_UP6 has 6 genes, two of them below 3 CPM.

## 6. Task 3, conclusion for K01 and L01, and what would distinguish the alternatives

**K01.** Reopening condition: not satisfied in substance (section 0). Effect on the decision: **narrow the statement and separate three hypotheses; keep step 0 and arms A-C as they are; add an in-vivo anchor.** The K01 premise "a HIF-dependent glycolytic shift exists in WWOX-deficient neural cells" now stands on one human organoid transcript set (4 v 2 libraries, one WT line), with five in-vivo mouse transcript contrasts that do not reproduce its selective pattern. That moves the weight toward "system-specific or activity/composition-driven" without proving it. It does not strengthen H-harm or H-protect: the direction question is untouched. No change of research priority is proposed. Candidate text is in `proposals/`.

**L01.** Nothing changes in selection or priority; the P47T in-vivo datum adds a modest NRF2-target increase (Hmox1, Srxn1) that is composition-confounded, and mixed against the organoid (NFE2L2 and NQO1 lower, HMOX1 and SRXN1 higher). Cerebellar ROS hallmark: leading edge is antioxidant enzymes plus myelin genes.

**Measurements that distinguish (research priority, proposals, not performed):**

| Alternative | Decisive measurement | Prediction if true / against |
|---|---|---|
| WWOX-specific HIF stabilisation | HIF-1alpha and HIF-2alpha protein, nuclear v cytoplasmic fractions, plus hydroxylated HIF, in mutant v WT hippocampus fixed by perfusion or frozen in situ; in human neural cells KO v isogenic add-back at 5 percent O2 (beside 21 and 1) with HIF1A/EPAS1 knockdown | nuclear HIF up and the selective set (Bhlhe40, Ddit4, Ndrg1, Egln3, Ankrd37, Adm) following HIF knockdown; against: protein flat while glycolytic enzymes stay up |
| Seizure/neuronal activity | per-animal video-EEG seizure counts in the preceding 24 h as covariate; a pre-onset age group; tetrodotoxin-silenced or activity-clamped tissue/cultures from the mutant | signature tracks seizure count and disappears under silencing |
| Tissue hypoxia (oxygen supply) | pimonidazole adducts, vascular density, tissue oxygen | pimonidazole higher without WWOX-specific HIF protein change |
| Composition | single-nucleus RNA of mutant v WT hippocampus; cell-type-resolved Ndrg1/Bhlhe40/Pgk1/Aldoa | change persists within each cell type vs shifts with cell proportions |
| Glycolytic flux | lactate (in-situ freezing or MRS), glucose uptake; not mRNA | enzyme transcripts up with higher lactate vs flat lactate |

## 7. Disclosures, deviations, UNVERIFIED

* **Non-blind**, section 1. Q-D prediction wrong (PRE_ANALYSIS addendum). Post hoc, exploratory: leave-one-out, matched null, per-animal pivot, identity check, hallmark variants, high-activity designation of M6/F8, pixel measurement.
* **Deviation from the task wording:** the PMC page and PMC supplement links were not viewed (captcha); Figures 8, 9 and the supplements were read from the PMC-origin copies in the shared corpus (read-only), which also supplied the derived text of the DEG sheets. The brief forbids circumventing access controls.
* NES values are pixel measurements of a raster JPG (about +/-0.03); no vector source exists on the PMC surface. My GSEA is a re-implementation with a different hallmark release (2023.2.Mm) from the authors' unnamed one; equality of NES was not expected and is not a test.
* **UNVERIFIED:** GEO terms text; sign convention of Fig 8b (stated nowhere); the authors' ranking metric and permutations; cause of the HPC DEG-list mismatch; why Methods say 5 per group for cerebellum while the legend and deposit show 4 v 3; per-animal age, batch, seizure timing; oligodendroglial expression of Ndrg1/Bhlhe40 (background knowledge); the P17 and organoid values in Table B are carried from IT10/IT11 tables, not recomputed here (the HPC S027 values were recomputed and agree: Ldha +0.49, Hk2 +0.77, Slc2a1 +0.18, Ldhb -0.10).
* Not done: heterozygote or other deposits (GSE229210 was not examined); no supplementary-file reading beyond the lists named in `premises.tsv`.

## 8. For the batch path (proposals only)

* Card K01: replace the last sentence of `functional_evidence_available`, append to `temporal_or_model_limit`, add three step-0 additions and one assertion (`proposals/k01_card_text_proposal.md`).
* Needs: NEED-PDH-PYRUVATE-AXIS observed/counter_evidence/notes, NEED-LACTATE-LDH one sentence, L01 note (`proposals/needs_text_proposal.md`).
* Receipts proposed (not recorded): PMC10835625 full-targeted read; GSE215425 dataset read (digests in `raw_hashes_it12.tsv`).
* Census: the entry for GSE215425 in `census_reconciliation_it7_20261029.md` ("transcript only; not adequate") should read "counts accessible; reanalysed for HIF/NRF2 target sets in IT12; HPC authors' DEG list not reproducible".

## 9. Files

`PRE_ANALYSIS.md` (+ addendum), `README.md`, `premises.tsv` (16 rows with locators and depth), `usability_check.tsv`, `raw_hashes_it12.tsv`, scripts `p47t_reanalysis_it12.py`, `compare_it12.py`, `sample_identity_check_it12.py`, `per_animal_table_it12.py`, `measure_bars_it12.py`; `results/` (`genes_it12.tsv`, `sets_it12.tsv`, `set_scores_per_animal_it12.tsv`, `per_animal_it12.tsv`, `composition_correlations_it12.tsv`, `gsea_reimpl_it12.tsv`, `leading_edge_it12.tsv`, `leave_one_animal_out_it12.tsv`, `matched_null_it12.tsv`, `validation_vs_authors_it12.tsv`, `identity_it12.tsv`, `compare_it12.tsv`, `bars_it12.tsv`, `run_log.txt`); `proposals/`. Inputs live in the scratchpad (digests listed); re-run: `python3 -I p47t_reanalysis_it12.py run --counts GSE215425_processed_data.csv.gz --hallmark mh.all.v2023.2.Mm.symbols.gmt --authors-deg Supplementary_data_all_sheets_derived.txt --out DIR`.
