# GSE126075 (WWOX-silenced H9-derived neural progenitors and day-14 neurons, CAGE): qualification and pre-declaration

Declared 2026-10-28 (file path dated for the mandate day 2026-10-29) by scientist-c, mandate IT5 step P6.
Committed BEFORE any per-gene expression value of the deposit was read. What was read before this file: the GEO series and
sample records, the directory listing, the first lines of the two processed files, the column sums of the gene matrix, and the
tag count (line count) of each raw BED file. No gene row, no WWOX row, no ATF4 row and no set member was looked at.
Exploratory. A COMPUTATIONAL RESULT on published data, not a new experiment. Not medical advice. Transcript level only.
Source and credit: GSE126075 is the deposit of Kosla et al. (PMID 31543760, Front Cell Neurosci 2019); the results derived here rest
on their work and are theirs to be credited for.

## 1. Qualification of the deposit (STEP 1)

| Item | Finding |
|---|---|
| Identity | GEO series GSE126075, title "The influence of WWOX gene on cellular pathways in neuronal differentiation of human neural stem cells", Series_pubmed_id lists 31543760 (the study) and a second id, 32581702 (a 2020 Front Neurosci paper on Wwox and neuronal migration; its relation to these data is not examined here). Match to the study: yes (same title concept, same arms, same cell source, 9,427-gene matrix equals the 9,427 genes of the paper's GSEA). |
| Technology | CAGE (library_selection CAGE, strategy RNA-Seq in GEO vocabulary), Illumina HiSeq 2000, 100 bp, EcoP15I protocol. Tag clusters (TSS) from MOIRAI, mapped hg19, lifted to hg38, clustered with CAGEr/paraclu, cross-identified with FANTOM5 hg38 "true-TSS" library. Counts normalised to tags per million (simple TPM). |
| Samples | FOUR libraries, one per arm: GSM3590948 hNSC, GSM3590949 hNSC_WWOX_del, GSM3590950 neurons, GSM3590951 neurons_WWOX_del. There is NO replicate library in the deposit. The sample records say "wwox expression: wild type" for the control arms and "native" in the series design, while every sample carries the same lentiviral treatment text; the paper's control is shScrambled. Whether the control arms are shScrambled or untransduced is therefore not settled by the deposit; they are treated here as the paper's control arm (shScrambled) with this ambiguity declared. |
| Replicates | Biological replicates: none deposited. Technical replicates: none. The paper does not state n for the transcriptome. The paper's reported differential expression (P < 0.05) and phenotype-permutation GSEA cannot be re-derived from one library per class; how it was done (possibly on TSS-level pseudo-replicates) is not stated and is not reproduced here. |
| Differentiation stage | undifferentiated progenitors (growth-factor maintained) and spontaneous differentiation by bFGF/EGF withdrawal (paper: day 14 for the transcriptome). Neurons are MAP2/TUJ1-positive, no glia (paper). |
| WWOX perturbation | lentiviral shRNA, puromycin-selected; extent never quantified in the paper; checked here only at CAGE-tag level (declared below). |
| Processed data used | (1) GSE126075_TPMexpression_all_genes_all_samples_merged.txt.gz (9,427 genes x 4 arms, gene = sum of its TSS TPM; gene symbols as FANTOM5 hg38 names); (2) GSE126075_TSScoordinates_TPMexpression_all_samples_F5mapped.txt.gz (10,725 TSS clusters with hg38 coordinates and FANTOM5 TSS names). sha256: 7e51e3cffa7491a7778a23516fd6e8bbe601b62cb5223536885a401219a392c2 and 8f93a12c9a4fdc7c8ceef08dd44f4723ea00d97948b352ddd7d3dbf121ce1970. |
| Raw data | The four sample BED files (tag-level, 300 MB to about 400 MB each, about 1.2 GB the series tar) were STREAMED once to count mapped tags (31,702,049; 14,332,108; 32,686,868; 40,730,002 for hNSC, hNSC_WWOX_del, neurons, neurons_WWOX_del) and to record their sha256 (in files/geo/GSE126075/bed_streamed_tagcounts_and_sha256.tsv), then discarded. The raw BEDs add no inference beyond a library size: with n = 1 per arm there is nothing to model, and the authors state that demultiplexed FASTQ files are not their workflow files. Local data kept: about 1.2 MB. |
| Quality finding | The gene matrix does NOT carry the same share of each library: column sums are 609,160 / 606,894 / 264,496 / 89,581 (hNSC, hNSC_WWOX_del, neurons, neurons_WWOX_del) of a nominal 1,000,000. The neuron libraries, above all neurons_WWOX_del (about 9 percent), place far fewer tags in FANTOM5-annotated gene promoters (the rest sit in unannotated clusters or are not in the gene table). Per-million values are therefore compositional and a global offset between arms is expected without any biology; the analysis is built around this. |
| Annotation | Gene-level only for the matrix (symbol per row); TSS file gives coordinates, strand and FANTOM5 promoter names (pN@gene). Symbols follow the FANTOM5 hg38 vocabulary, which may carry older HGNC names; an alias table (below) is used and every unmatched member is reported. Genome build GRCh38. |

Conclusion of the qualification: the deposit is acquirable and matches the study. It supports DESCRIPTIVE analysis of four single
libraries. It does not support statistical inference on any WWOX effect (n = 1 per arm). Everything below is written for that.

## 2. What is analysed and how (fixed now)

Contrasts: within each stage, shWWOX versus control: C_hNPC = hNSC_WWOX_del vs hNSC; C_neuron = neurons_WWOX_del vs neurons.
Stage contrast (positive control of the data, not a WWOX contrast): S_ctrl = neurons vs hNSC; S_kd = neurons_WWOX_del vs hNSC_WWOX_del.

Measurable-gene universe, per contrast: genes in the matrix whose estimated tag count (TPM x library tags / 1e6, library tags = BED
line count; an approximation because the exact normalising total used by CAGEr is not stated) is at least 10 in BOTH arms of the contrast.
This universe is the only universe for any set comparison and for the matched null. Set members outside it are reported as not
measurable and excluded from that contrast.

Effect measure: log2 ratio R = log2((TPM_kd + 0.5) / (TPM_ctl + 0.5)) per gene (0.5 TPM pseudocount). PRIMARY = R centred by
subtracting the median R of the contrast's measurable universe (removes the compositional offset). SENSITIVITY A = uncentred R.
SENSITIVITY B = TPM renormalised to the sum of the gene matrix of each arm, then centred as primary. A call is stable only if its sign
agrees across primary, A and B.
Per-gene technical-sampling interval: a Poisson 95 percent interval on the ratio from the estimated tag counts. It carries sampling noise
only and says nothing about culture, transduction or biological variance (there is no replicate to measure them).

Set statistic: mean centred R of the measurable members. Reference: 10,000 random sets of the same size drawn from the contrast's
measurable universe, each member matched to a set member by expression decile (deciles of the mean of log10 estimated tags of the two
arms), seed 20261029. Reported: the set mean, the null mean and the two-sided empirical percentile of the set. This is a RANK of the set
among matched random sets of THIS comparison of single libraries; it is NOT a p value for a WWOX effect, because the unit of replication
(the library) is one. No multiplicity correction is claimed and none is needed because nothing is called significant.

## 3. Questions, gene sets and sources (fixed now)

Source of the lists: the repository's own previously declared sets in drug_repurposing/gse156243/prediction_isr_ldh_chain_20261026.md
and prediction_hif1a_pdk_chain_20261025.md and gse156243/marker_sets_declared.tsv, extended only by the genes the mandate names (PSPH,
the PDK family, HK2, LDHA). No external list was fetched; set membership is the author's prior knowledge, not an externally validated
signature. XBP1 is not in the ISR set (it is a UPR gene).

(a) ISR / ATF4 transcript signals.
- ATF4 itself (single gene): its transcript, reported on its own. ATF4 is controlled translationally; a flat or changed ATF4 mRNA is
  not an ATF4 activity measurement.
- ISR_targets (12): ASNS, CHAC1, TRIB3, DDIT3, PHGDH, PSAT1, PSPH, SLC7A11, ATF5, PCK2, SESN2, GADD45A.
- UPR_branches (8, excluded from the ISR set on purpose): XBP1, HSPA5, HSP90B1, DNAJB9, EIF2AK3, EIF2AK4, EIF2S1, PPP1R15A.
- Per-gene table for every member of the two sets, with its Poisson interval and measurability.

(b) Mitochondrial and metabolic programmes.
- OXPHOS_nuclear: nuclear-encoded respiratory-chain subunits by explicit list, all of NDUFA1-3, NDUFA5, NDUFA6, NDUFA8-13, NDUFAB1,
  NDUFB1-11, NDUFC1-2, NDUFS1-8, NDUFV1-3, SDHA-D, UQCRB, UQCRC1, UQCRC2, UQCRFS1, UQCRH, UQCRQ, UQCR10, CYC1, COX4I1, COX5A, COX5B,
  COX6A1, COX6B1, COX6C, COX7A2, COX7B, COX7C, COX8A, and ATP synthase ATP5F1A-E, ATP5PB, ATP5MC1-3, ATP5PD, ATP5PF, ATP5PO, ATP5ME,
  ATP5MF, ATP5MG, with old names (ATP5A1, ATP5B, ATP5C1, ATP5D, ATP5E, ATP5F1, ATP5G1-3, ATP5H, ATP5J, ATP5L, ATP5O, ATP5J2) as aliases.
- Mito_translation: every measurable gene whose symbol starts with MRPL or MRPS, plus TUFM, TSFM, GFM1, GFM2, MTIF2, MTIF3, MTRF1L.
- Mito_import: TOMM20, TOMM22, TOMM40, TOMM70, TIMM8A, TIMM9, TIMM10, TIMM13, TIMM17A, TIMM17B, TIMM21, TIMM22, TIMM23, TIMM44, TIMM50,
  PAM16, DNAJC19, GRPEL1, HSPD1, HSPE1, PMPCA, PMPCB, SAMM50.
- Glycolysis_lactate: SLC2A1, HK2, PFKP, ALDOA, PGK1, ENO1, LDHA, PKM, BNIP3 (the HIF1A glycolytic set used for the organoid) and LDHB;
  PDK_family: PDK1, PDK2, PDK3, PDK4 (reported per gene because members are lowly expressed); SLC16A1, SLC16A3 per gene.
- The paper's GSEA lists mitochondrial translation and import sets on the silencing side in Supplementary Table 3, and the repository's
  two statements of the sign differ in wording (dossier: negative enrichment in the silenced line; needs.json O6: on the knockdown side).
  The sign is NOT assumed here. The analysis is two-sided and its direction is whatever the data give.

(c) Differentiation / maturation / proliferation confounders.
- gse156243/marker_sets_declared.tsv sets, unchanged: radial_glia_progenitor, cell_cycle_proliferation, neuronal_pan, glutamatergic,
  GABAergic, astrocyte_glia, regional_patterning_non_cortical, wnt_pathway.
- Positive control of the dataset: in S_ctrl (neurons vs hNSC) the neuronal_pan set should rise and radial_glia_progenitor and
  cell_cycle_proliferation should fall. If this fails, the stage labels or the matrix are suspect and the whole analysis is reported as
  unreliable.
- Differentiation progress in the knockdown line: the same stage contrast in the knockdown line (S_kd). If the progenitor/neuronal
  marker movement in S_kd is smaller or larger than in S_ctrl by a margin outside the matched null for those sets, differentiation
  efficiency differs between lines and any set shift in C_neuron is read as possibly maturation-confounded.
- Stage-coupled sensitivity: within each contrast, regress centred R on the control-line stage log2 ratio S_ctrl across the measurable
  universe (ordinary least squares, slope and intercept fixed by the whole universe), and report each set's mean residual. A set whose
  shift disappears in residual (sign flips or falls inside the matched null) is called maturation-coupled.

## 4. Controls (fixed now)
1. WWOX itself: R of the WWOX gene (and each of its TSS clusters in the TSS file) in C_hNPC and C_neuron, with Poisson interval, and its
   rank among all measurable genes. The size of the silencing at CAGE-tag level is reported; if WWOX is NOT lower in the deposit in either
   stage, the contrast is called uninformative about WWOX loss and no needs entry is made.
2. Matched random sets (above) as negative control for every set; also two control gene classes fixed now with no relation to the question:
   cytosolic ribosomal proteins (RPL*, RPS*, excluding RPLP and mitochondrial MRPL/MRPS) and a set of 12 housekeeping genes, fixed now: ACTB, GAPDH, TBP, PPIA, HPRT1, B2M, TUBA1B, EEF1A1, RPLP0, UBC, YWHAZ, GUSB.
   These show how far an unrelated set moves in the same single-library comparison.
3. The control arm of each stage is the reference of every ratio; no other control arm exists in the deposit.
4. Global distribution of R (median, spread) in each contrast is reported, so that a set shift can be read against the transcriptome.

## 5. Decision rule and what is reported

Because n = 1 per arm: DESCRIPTIVE analysis, declared. No power calculation, no significance statement, no false-discovery claim.
A set is reported as a "descriptive signal worth carrying" ONLY IF all four hold: (i) its centred set mean lies outside the central 95
percent of its matched null in BOTH C_hNPC and C_neuron with the SAME sign; (ii) the sign is the same under sensitivity A and B;
(iii) it is not maturation-coupled by the residual rule; (iv) WWOX control 1 shows silencing in both stages. A set that meets (i) in only
one stage, or fails (ii) or (iii), is reported as "inconsistent or confounded". A set inside the null in both stages is reported as "not
distinguishable from matched random sets in this deposit" (which is NOT evidence of absence: one library per arm cannot exclude an
effect). A single gene is never called differentially expressed; per-gene numbers are listed with their sampling interval only.
Expected before looking, written down so that surprise can be seen: none of the pre-lists is predicted in a direction here, because the
repository holds no prior human-neural-progenitor transcript for these sets; the organoid result (ISR targets lower than chance in WWOX
knockout organoids, glycolytic targets higher) is a different system and is reported only as a comparison of sign.

## 6. What the result can and cannot say
CAN say: whether, in these four CAGE libraries, the transcript levels of the pre-listed ISR/ATF4 targets, mitochondrial programmes and
glycolysis genes differ between shWWOX and control by more than matched random sets do, and whether that is explained by differentiation
state, in a human neural lineage, WITH the knockdown of unquantified depth and n = 1.
CANNOT say: that the integrated stress response is active or inactive (no eIF2alpha phosphorylation, no ATF4 protein, no GCN2/PERK
measure exists in this deposit; ATF4 mRNA is not ATF4 activity; ISR target mRNA is an inferred, indirect signal); that respiration,
ATP, complex I activity or flux changes (transcript is not flux); that any shift is WWOX-dependent rather than line, transduction,
culture or composition (no replicate, no rescue, scrambled arm possibly native); anything about a WWOX allele (a knockdown is not a
biallelic null or a missense allele); anything about patients.

## 7. What would change or not change the needs
NEED-ISR-ATTENUATION and NEED-MITOCHONDRIAL-RESPIRATION receive one added observation each (evidence_scope COMPUTATIONAL_RESULT,
readout_level transcript, model type human_neural_progenitor_shrna_knockdown) IF AND ONLY IF the control checks pass (WWOX lower in the
data in both stages; the stage positive control behaves). The entry records the result whatever its direction, including a null, with
the n = 1 limit stated. Nothing in the needs' ranks, inferred text, track/goal or the "unmeasured" status of GCN2/PERK/eIF2alpha
phosphorylation changes: a transcript result cannot move them. A "descriptive signal worth carrying" in the ISR targets would be recorded as
a lead to be tested with a protein or phospho measure; its absence leaves the need as it is. If the controls fail, no needs file is edited.
No receipt is staged (data analysis, not a paper reading).

## 8. Reproducibility
Script analyse_gse126075.py (this directory), run with python3 -I; inputs are the two processed files by sha256 above and the tag counts
file; outputs (results tables, figures, a JSON of parameters and hashes) are written to this directory. Seed 20261029.
Deviations from this declaration, if any, will be listed in RESULTS.md as deviations and not edited in here.
