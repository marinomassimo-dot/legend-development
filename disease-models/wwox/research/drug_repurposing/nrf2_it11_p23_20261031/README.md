# IT11 P2.3: independent verification of card L01 (NRF2 axis), organoid deposit first

Scientist `scientist-c` (verifier; did not produce L01), task ORCH-ROADMAP-IT11, branch `task/it11-p23` from main `d6ccf8d1`, date 2026-10-30 UTC (communication to the operator is in Europe/Rome). Non-canonical research material. **Not medical advice; no dose, route or schedule is recommended; in-vitro concentration windows quoted below are facts of the cited sources, not recommendations.** Reference genotype: a WWOX-DEE genotype class; no individual-level record. No e-mail address, operator identity or personal datum was sent to any service. Edits no card, need, ranking, registry, ledger or current file (proposals: `l01_corrections_proposal.md`).

**Not blind.** I read the IT10 package (README, premises.tsv, candidates.tsv, organoid_nrf2_rows.tsv, L01 packet/card, selfaudit) BEFORE formulating the questions below. The comparisons are informed, not blind. The five phenotype leads and PLK1 are not used here.

## 1. Decisions (first)

| # | Decision | Datum that decides it |
|---|---|---|
| 1 | **The organoid numbers in L01 are verified.** NFE2L2 0.75x, NQO1 0.73x, HMOX1 1.67x (KO/WT), IL6 zero in all six libraries, IL1B/TNF near zero: recomputed from the GEO deposit itself (not from the IT10 tsv); the IT10 raw counts match the deposit for all 36 genes (0 mismatches). Direction is the same under a DESeq2-style size-factor normalisation (0.73, 0.71, 1.61). | `organoid_recompute_it11_output.txt`, `crosscheck_vs_it10_tsv_output.txt`; premise rows V1, V3, V5 |
| 2 | **But the 4 v 2 contrast is weaker than the card says.** The 2 WT are the survivors of a post hoc exclusion (one low-quality, one that "did not cluster with any of the other samples"); GEO calls both "failed quality control". WT is one parental line; the KO clone and batch of each library are not assigned in the deposit. Only NFE2L2 is in the authors' DE list (padj 1.43E-02, log2FC -0.58, above the paper's stated alpha 0.01); NQO1 and HMOX1 are in neither list. Exact permutation on 4 v 2 cannot go below about 0.07. The result stays descriptive. | V2, V3; `organoid_stats_it11_output.txt` |
| 3 | **"Human organoid cannot test the cytokine arm": SUPPORTED for the deposit, OVERSTATED as a statement about the model.** No microglia-like cells (P2RY12 0 in all six, CX3CR1 7 counts in total, "microglia" absent from the paper), no stimulus, bulk poly-A. But the organoid contains radial glia and astrocytes (the authors report increased astrocytes by immunofluorescence), and the authors' own count filter removed IL6 and TNF before testing. Whole-organoid GFAP transcript is 0.88x while astrocytes are reported increased: a transcript/protein/composition discordance in one system. | V5, V6 |
| 4 | **P47T cerebellum (PMID 36828035): confirmed, with corrections to the seeds.** n 6 v 6 (3 M + 3 F), qPCR, 18S, unpaired Student's t, p<0.05 (exact p not given). By the figure (by eye): IL1b about 1.9x, TNFa about 3.3x. S084's "qPCR/RNA-seq n 6" is wrong (qPCR only; the cerebellar RNA-seq figure has 4 v 3 leaves, Methods say 5 per group); its "overlap" is marginal for IL1b and absent for TNF. **The best-supported cerebellar cytokine signal is TNF, the one NRF2 activation is predicted not to change.** Cerebellum is atrophic with Purkinje loss: composition not excluded. | V7, V8, V9 |
| 5 | **Null hippocampus (PMID 30290271): recorded, not re-litigated.** n 4 v 4, 2-week-old KO vs Cre+ littermates, Gapdh, Student's two-tailed unpaired t; "Il6 significant at p < .05"; Tnf-a >1.5x in the text, no mark. The authors' abstract and Discussion claim both. No mark is not no effect. | V11 |
| 6 | **The "two chemotypes" arm of L01 is OVERSTATED and changes the selection.** Monomethyl fumarate did not activate NRF2 in primary neurons or in a microglial line while DMF did (PMID 39684792, one source); the systemic/CSF moiety is MMF (label), the NRF2-active ex vivo form is DMF. DMF and MMF are not interchangeable. Omaveloxolone and DMF are both cysteine-reactive electrophiles: agreement between them cannot separate NRF2 dependence from electrophile-class actions. Only NFE2L2 loss can. Treat DMF as a conditional comparator and MMF as a different compound with an HCAR2 rationale, not as a second NRF2 chemotype. | V14, V15, V16 |
| 7 | **Omaveloxolone stays a conditional ex vivo probe, now with a window.** NRF2-linked suppression in macrophages at low nM; NF-kB (IκBα phosphorylation), JNK and growth inhibition (also in Keap1-/- MEFs) at hundreds of nM; the NRF2-loss control in the source paper was run with bardoxolone methyl, not omaveloxolone; no NRF2-loss control for omaveloxolone on IL-6/IL-1b was found (searches run; not found is not absent). Label protein binding 97%. | V14 |
| 8 | **The only published NRF2-knockout control for IL-6/IL-1b suppression that I found in this literature is for DEM and 15d-PGJ2 (Kobayashi Fig 4b-e), not for any L01 compound; and "Tnf unchanged" is shown only in the genetic Keap1-cKO.** For the fumarates, NRF2-knockout controls exist and show NRF2-independent actions (NF-kB inhibition by DMF; EAE protection equal in Nrf2-/- mice). | V12, V16 |
| 9 | **State of L01.** KEEP-AS-PROPOSAL, research priority MEDIUM unchanged (step 0 still cheap and informative); the selection inside the card changes (item 6), the experiment gains three controls (section 5), and 12 corrections are proposed. No class is promoted. | `l01_corrections_proposal.md` |

## 2. Item 1: the dataset actually used (GSE156243), depth and method

Access: GEO key-less (series text view at `www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243&targ=self&form=text&view=full`; FTP `ftp.ncbi.nlm.nih.gov/geo/series/GSE156nnn/GSE156243/soft/` and `/suppl/`), Europe PMC REST for the paper (PMC8350905). **GEO access succeeded**; digests in `geo_files_sha256.txt`. Files were put in an empty scratch directory outside the repo and read with `python3 -I`. The shared `files/geo/` copy was not used.

| Question | Answer from the deposit and paper | Locator |
|---|---|---|
| Contrast | KO (CRISPR WWOX exon 1) vs WT parental hESC line WiBR3, cerebral organoids, 15 weeks, polyA RNA, NextSeq 500 single-read 75; Salmon 1.2.1 on GRCh38 cDNA release 99, tximport + DESeq2 per the authors | sample records `!Sample_characteristics_ch1 = age: 15 weeks`, `!Sample_data_processing` |
| Which libraries | GSM4727525, 526 = "Cerebral Organoids untreated 1, 2" (CWT1, CWT2) = WT; GSM4727527-530 = "Cerebral Organoids KO/WWOX 1-4" (CKO1-4) = KO. Count-table column order cko1-4, cwt1-2 | soft file |
| 4 v 2 design | "4 KO samples and 2 WT samples were included in final analysis, after 2 WT samples failed quality control"; paper: 8 sequenced (4 WT + 4 KO), one WT low read count/mapping, "Another WT sample that did not cluster ... (neither WWOX-KO nor WT)" removed | series design; paper Methods |
| Clones, replicates, batches | Paper: two KO clones (KO1 = WKO-1B, KO2 = WKO-A2); WT is the WiBR3 line only ("at least two hPSC lines ... with the exception of the WiBR3 WT line"). Which clone each KO library came from, and the batch of each library, are not in the deposit or in the passages read: **UNVERIFIED**. GEO says "age- and batch-matched". Number of organoids per library not stated | deposit; paper |
| Normalisation | The count file is Salmon estimated gene counts (non-integer), not normalised; library sizes 29.98-41.15 M; IT10 used CPM; I recomputed CPM (ratios 0.752, 0.730, 1.667) and median-of-ratios (size factors 1.057, 1.113, 1.100, 0.953, 1.006, 0.809 on 18,208 genes with all-nonzero counts; ratios 0.732, 0.707, 1.612) | `organoid_recompute_it11_output.txt` |
| Authors' tests | DE lists (1,246 up, 1,021 down; max padj 0.0684 in both, although Methods state alpha 0.01). Filter: "minimal overall count of 10 on all six samples". NFE2L2 is in the down list (p 9.32E-04, padj 1.43E-02, log2FC -0.58); NQO1, HMOX1, KEAP1, IL6, IL1B, TNF are in neither list (IL6, TNF fail the filter) | DE files; paper Methods |
| KO verification at transcript level | WWOX transcript is not lower in KO (CPM ratio 1.39; KO libraries 11.9-16.5 vs WT 9.6-10.1 cpm): expected for an exon-1 indel with protein loss shown by immunoblot (paper, Fig EV1A); the transcript cannot confirm the KO | table |
| Cytokine, microglia, inflammasome rows | IL6 0 x6; IL1B 1,0,1,0,1,11; TNF 1,0,1,0,0,0; IL1A 5,0,3,1,0,0; IL18 15,4,2,1,0,0; NLRP3 14-33; CASP1 0-32; P2RY12 0 x6; CX3CR1 7 total; PTPRC 29 total; AIF1 1,742 total; CD68 4,488; GFAP 30,862; SLC1A3 23,011; S100B 1,369 | stats output |
| Rows not in IT10's list | TMEM119 sum 284, but 168 of them in cko1 alone (3.8x ratio is one library); this is an outlier library, not a microglia signal (P2RY12 and CX3CR1 absent) | stats output |

Why this matters for L01: the organoid row contributes a *direction hint* (NFE2L2, NQO1, G6PD, SLC7A11, BACH1, CUL3 lower in all four KO libraries; HMOX1, SRXN1, GSR higher) and a *floor* (no cytokine transcripts at baseline). Neither is a test: two WT libraries, post hoc selection, clone unassigned, transcripts not activity.

## 3. Items 2 and 3: the two mouse cytokine contrasts (summary; detail and locators in `premises_verified.tsv`)

* **P47T cerebellum (V7-V10).** Verbatim: "a significant ≥ 2-fold upregulation of mRNA of both cytokines (p-value < 0.05) in CB samples from WwoxP47T/P47T mice (n = 6) compared to WT mice (n = 6) (Fig. 9d and e)". Legend: "unpaired Student's t-test", error bars SEM. Figure 9d,e read by eye from the repo image (not digitised): IL1b 2.0 vs 3.8, TNFa 1.0 vs 3.3 (plotted units; the WT IL1b bar is not 1.0). Seeds: S084 SUPPORTED with corrections; S085 P47T clause SUPPORTED. New, not in L01: the same figure shows the hallmark REACTIVE_OXYGEN_SPECIES_PATHWAY among the top enriched sets in the cerebellum (direction of enrichment not stated in the text read).
* **Null hippocampus (V11), recorded only.** n 4 v 4; "Il6 significant at p < .05"; Tnf-a >1.5x without a mark in Fig 4E per IT10; abstract and Discussion claim both; the sentence "increased expression of inflammatory cytokines Tnf-a and Il6" is verbatim in the Discussion. Absence of a mark in a 4 v 4 t-test is not absence of an effect.

## 4. Item 4: distinctions that decide, and the compound checks

| Distinction | Verdict | Basis |
|---|---|---|
| WWOX data vs macrophage precedent (PMID 27211851) | SUPPORTED as separate; the precedent is murine BMDM (and THP-1 for DEM), LPS/M1-stimulated, no microglia string in the text | V12, V13 |
| Transcript vs protein vs maturation vs activity | SUPPORTED as unresolved: every WWOX cytokine datum is a transcript; the macrophage precedent adds secreted IL-6/IL-1b only for DEM (with alum); no caspase-1 maturation, no NRF2 protein or activity datum in any WWOX system | V7, V11, V12 |
| Neural effect vs composition | UNVERIFIED either way: cerebellar atrophy with Purkinje loss, null-hippocampus interneuron loss and astrogliosis, organoid astrocyte increase with GFAP transcript 0.88x | V6, V9 |
| Adaptive activation vs insufficient compensation | UNRESOLVED and kept open: organoid NFE2L2/NQO1 lower with HMOX1/SRXN1 higher fits either | V4, V17 |
| NRF2 modulation vs alternative compound actions | OVERSTATED as a single mechanism for both compounds | V14-V16 |

**Omaveloxolone (one concrete thing: NRF2-loss control and off-target window).** Source read: Probst 2015, PMC4405374, full text; label via openFDA. Result in decision 7. What would change selection or the next experiment: the concentration series with NQO1 readout and an NFE2L2-knockdown arm at both ends of it; a result only above the low-nM window, or that survives NFE2L2 knockdown, reclassifies the effect as not NRF2-mediated. UNVERIFIED: brain unbound concentration (L01 already lists it), microglial IL-6/IL-1b effect, NRF2-loss data for omaveloxolone in any cell type.

**Fumarates (one concrete thing: active moiety and NRF2-independence).** Sources: Sanchez-Sanz 2024 full text (Results/Discussion windows); Gillard 2015, Schulze-Topphoff 2016, Kornberg 2018, Parodi 2015, Brennan 2016, Zhang 2026 at abstract depth; Bafiertam label. Findings in decisions 6 and 8. What it changes: split DMF and MMF into separate rows; add NF-kB p65 translocation, HCAR2 and GAPDH-activity controls; NFE2L2 knockdown remains the only arm that separates NRF2 dependence. Whether a non-electrophilic KEAP1-pathway tool would be a true second chemotype was NOT examined (UNVERIFIED; no compound named).

## 5. Next experiment: additions only (L01 step 0 and step 1 stand)

1. Step 0 system: keep the microglia-containing and primary neuron-glia systems; add an astrocyte-containing challenged arm (LPS, with and without ATP) so the organoid-type model can be used for the astrocytic cytokine route; report which clone and batch each sample comes from and keep both clones.
2. Step 1: DMF and MMF as two separate arms; omaveloxolone as a concentration series spanning the NRF2-linked and IKK/JNK windows with NQO1 at each point; NFE2L2 knockdown crossed with every compound; readouts add NF-kB p65 translocation, TNF (prediction: NRF2-only action leaves TNF unchanged; a TNF fall indicates NF-kB-type action), HCAR2 dependence for MMF.
3. Fix predictions before the run (as L01 already does) and keep research priority, directional compatibility, development requirements and observed benefit separate.

## 6. What could change the priority

| Up | Down |
|---|---|
| Step 0 shows raised ROS or low NRF2 tone (NQO1 activity, nuclear NRF2) in WWOX-deficient neural cells; the organoid direction hint (NFE2L2, NQO1 lower) replicates with clones separated | No KO-vs-corrected difference in ROS or NRF2 tone and cytokine protein under the assay floor in every system |
| Cytokine protein above the floor in a microglia- or astrocyte-containing WWOX-deficient culture after challenge | Compound effects appear only at the NF-kB/JNK/growth window, or survive NFE2L2 knockdown |
| Omaveloxolone effect on NQO1 and cytokine protein at low nM that NFE2L2 knockdown abolishes | MMF inactive, DMF effect NFE2L2-independent (the fumarate arm collapses to an electrophile effect) |
| Cerebellar ROS hallmark confirmed as increased in P47T (Supplementary data) with an oxidative readout | TNF, not IL6/IL1B, is the dominant WWOX cytokine signal and compounds change IL6/IL1B only (the lever misses the best-supported seed) |

## 7. Disclosures, deviations, UNVERIFIED

* Non-blind (see top). The verifier role is independent of the producer, not blind to the producer's conclusions.
* Access: GEO and Europe PMC REST succeeded; `pmc.ncbi.nlm.nih.gov` returned a reCAPTCHA page and Europe PMC returned HTTP 500 for PMC4855599 and PMC7104842, so Schulze-Topphoff 2016 was read at abstract depth through the PubMed tool and PMID 30290271 was read from the repo XML copy (`files/fulltext/PMID30290271_Hussain2019_PMC_r2.xml`), Fig 4E image NOT re-viewed by me. Abstract-only reads: 27078105, 29599194, 25920452, 26980071, 26004161, 42019494 (abstracts retrieved through PubMed; DOIs: 10.1073/pnas.1603907113, 10.1126/science.aan4665, 10.1007/s00401-015-1422-3, 10.1089/ars.2015.6622, 10.1016/j.jneuroim.2015.04.006, 10.1016/j.chembiol.2026.03.016, 10.3390/ijms252313082).
* Deviation: while converting an XML to text I accidentally wrote one derived text file into the shared gitignored `files/fulltext/` of the root checkout; I deleted it at once; the source XML was not modified and no tracked file in root changed.
* Figure values for Fig 9d,e are by eye, not digitised; fold values are approximate; point-overlap statements are by eye.
* My permutation and Welch figures are descriptive of 4 v 2 libraries, not a test of a claim; no multiple-testing correction was applied or implied.
* UNVERIFIED: KO clone and batch per library; number of organoids per library; exact p-values for Fig 9d,e and Fig 4E; age of the P47T qPCR mice; direction of the cerebellar ROS enrichment; whether Il1b/Tnf are significant in the cerebellar RNA-seq (Supplementary File 1 not opened); full text of Schulze-Topphoff, Kornberg, Parodi, Brennan, Gillard, Zhang; whether any NRF2-loss control of omaveloxolone on IL-6/IL-1b exists (not found in the searches run); brain unbound concentrations of any compound; whether a non-electrophilic KEAP1-pathway tool exists with human exposure; PR9 reactivity valence (carried, not re-read); IT10 rat and Drosophila premises PR3 and PR6 (not re-read here).
* Services: GEO (HTTPS, FTP over HTTPS), Europe PMC REST, openFDA, PubMed (via the connector). All key-less, no personal data, no contact-address parameter.
* Proposed receipts: see end of `l01_corrections_proposal.md`; the ledger was not touched.

## 8. For the batch path (nothing edited here)

1. Record this folder as IT11 P2.3 verification material for card L01.
2. Consider the 12 corrections in `l01_corrections_proposal.md` (items 1-4 change selection or the experiment).
3. Annotate IT10 P2.2 `organoid_nrf2_rows.tsv` consumers (DA-L01-003) with the post hoc WT exclusion and the unassigned clone; the numbers need no change.
4. Seeds S084 (remove "qPCR/RNA-seq"; fold wording) and S085 (P47T clause stands).
5. Ranking U59: split DMF and MMF; keep the genetic arm; no class promotion.

## 9. Files

README.md, premises_verified.tsv, l01_corrections_proposal.md, organoid_recompute_it11.py, organoid_recompute_it11_output.txt, organoid_stats_it11.py, organoid_stats_it11_output.txt, crosscheck_vs_it10_tsv_output.txt, geo_files_sha256.txt.
