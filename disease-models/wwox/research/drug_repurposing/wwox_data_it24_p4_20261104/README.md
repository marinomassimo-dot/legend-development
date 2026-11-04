# IT24 P4: which WWOX-perturbation data are re-analysable now, and what truly needs the bench (2026-11-04)

Non-canonical research material, not medical advice, reference genotype class only. Zero spend, no registration, no contact with anyone, no e-mail address sent anywhere.
Decision rules were written before the outcomes: `PRE_DECLARATION.md` (sha256 at the time of the last addendum: c45543a6...). Nothing here touches a card, ranking, registry or current file.

## 1. Accession truth (checked in the GEO/EBI records today)
* GSE158681 = bulk hippocampus (14 GSM: WT 3 v null 2, S-Ctrl 2 v S-KO 3, N 2 v 2), P17, mouse; GSE158682 = bulk cortex (7 GSM: S-KO 3 v S-Ctrl 4); GSE158684 = hippocampal **nuclei** snRNA (S-Control 3182 v S-KO 2920 nuclei, 8 GSM); parent GSE158685 (29 GSM). All "Public on Oct 01 2026". So "GSE158681/2" are the bulk deposits and GSE158684 is the snRNA one: both statements in the repo are right, they are different deposits. Paper link (PMID 33914858) rests on identical n, not on an accession (IT7/IT14).
* GSE215425 = P47T/P47T knock-in v WT, four brain regions (37 GSM), public since 2023-02-28, paper PMID 36828035.

## 2. Opportunity table (full columns in `opportunities.tsv`)
| # | Deposit | System / perturbation | Unit, n | Wwox down in data? | Class |
|---|---|---|---|---|---|
| O1 | GSE156243 | human organoid, WWOX exon-deletion KO, mixed tissue, wk 15, RNA | library, 4 v 2 | mRNA not lower (expected) | ALREADY_ANALYSED_AND_CONSUMED |
| O2 | GSE158681 | mouse P17 hippocampus, S/N/null deletion, RNA | animal, 2-3 per arm | yes, 85-94 pct (TPM) | ANALYSED_NOT_CONSUMED (set level consumed; per-gene now made) |
| O3 | GSE158682 | mouse P17 cortex, S deletion, RNA | animal, 3 v 4 | yes but noisy, 68 pct | ANALYSED_NOT_CONSUMED |
| O4 | GSE158684 | mouse P17 hippocampal nuclei, S deletion, cell-resolved | ONE pool per arm | yes (also falls in glia) | ANALYSED_NOT_CONSUMED (no seed cites it); raw reads `hup` |
| O5 | GSE215425 | mouse P47T missense knock-in, 4 regions, RNA | animal, 5 v 5 (CB 3 v 4) | mRNA unchanged (missense; protein present) | ANALYSED_NOT_CONSUMED (6-gene module only); **now fully re-analysed, section 3** |
| O6 | GSE126075 | human H9 NSC shWWOX, CAGE, progenitors and d14 neurons | ONE library per arm | **control FAILED in the progenitors (this deposit only)**; 3-4 fold in neurons, noisy | ALREADY_ANALYSED_AND_CONSUMED (guarded arm) |
| O7 | E-MTAB-14792 | human organoid scRNA incl. AAV9-WWOX add-back | 1 library per condition | unknown | PUBLIC_FILE_NOT_YET_FETCHED (HTTP 403 today; access is the operator's call) |
| O8 | **MTBLS12344** | fly head, pan-neuronal Wwox RNAi x Abeta42, metabolite pools | pool of 10 heads, 5 per cell | not in the deposit | **was "not public"; PUBLIC since 2026-11-02; re-analysed here, section 4** |
| O9 | E-MTAB-14948/9 | fly head RNA-seq, same design | pool, 4 per cell | no (15.7 v 15.9 CPM) | ANALYSED_NOT_CONSUMED (Wwox depth only) |
| O10-12 | GSE229210; GSE22689; endothelial TMT proteome (figshare) | glioma OE; fly embryo; non-neural WWOX-silenced PROTEIN table | - | - | PUBLIC_FILE_NOT_YET_FETCHED (outside the neural-deficiency perimeter; the TMT table is the only protein-level WWOX perturbation found) |
| O13-14 | proteome/phospho, translation, eIF2a-P/ATF4 protein, PDH/LDH activity, NAD(H), flux in a WWOX-deficient neural system; per-cell-type or protein-level P47T | - | - | - | NEW_MEASUREMENT_NEEDED |

Axes kept separate in every row: RNA (O1-O6, O7, O9) v metabolite pools (O8) v protein (none neural); quantity v activity (no activity anywhere); complete (O1 reported, O2-O4 near complete in tissue) v partial loss (O5 missense, O6 knockdown, O8 RNAi); neurons v progenitors v glia v mixed tissue (O4 only is cell-resolved; O6 progenitors/neurons are cell lines; the rest are mixed tissue).
The failed library control of O6 limits O6 and the rows resting on it (IT22 ablation: Q2 0 of 8, Q3 1 of 6, Q8 0 of 1 placed seed rows survive without it); it is not a veto on O1-O5.

## 3. The advance: per-gene contrasts for the two mouse RNA deposits (never made before; earlier work was set-level or 6 genes)
Code `analyse_it24_p4.py` (numpy only, 75 s). Method A (GSE215425, integer counts, n 5 v 5): CPM filter, median-of-ratios size factors, log2(count/sf+0.5), OLS genotype + sex, t test (df 7), BH within region, no variance moderation, effect centred on the median; sensitivity without the sex term. Method B (GSE158681/2, TPM summed to Ensembl-92 genes, n 2-4): **descriptive only**, no p-values, effect + animal separation + a control-vs-control flag.
Pre-stated thresholds A: FDR<0.10 / FDR<0.05 and |cLFC|>=0.585 / FDR<0.05 and |cLFC|>=1. B: |cLFC|>=0.585 / 1 / 2 with animal separation and mean TPM>=1.

GSE215425 P47T v WT, genes called (up/down), with sex term (without sex term in `p47t_summary.json`):
| Region | n | tested | FDR<0.10 | FDR<0.05, >=1.5x | FDR<0.05, >=2x |
|---|---|---|---|---|---|
| PFC | 5v5 | 15,008 | 813 / 607 | 212 / 71 | 128 / 28 |
| Hippocampus | 5v5 | 15,114 | 0 / 0 (min FDR 0.27) | 0 / 0 | 0 / 0 |
| Parietal cortex | 5v5 | 15,408 | 297 / 129 | 44 / 9 | 31 / 2 |
| Cerebellum | 3v4 (df 4) | 14,789 | 2 / 4 | 0 / 1 | 0 / 0 |
Controls run: (1) sex genes Xist/Ddx3y/Uty separate all females from all males in all four regions; (2) Wwox mRNA is unchanged (cLFC -0.13, -0.16, +0.03, -0.12), as expected for a missense, so the genotype is not a transcript-loss model; (3) my code reproduces the IT7 E1 six-gene module signs in hippocampus (SLC2A1 +0.18 v +0.18, HK2 +0.82 v +0.66, LDHA +0.52 v +0.48, LDHB -0.14 v -0.10, BNIP3 0.00 v +0.03, PDK1 -0.10 v -0.08); (4) PFC and parietal cortex agree: of 39 genes called in both at the middle threshold, 39 have the same direction. The strongest PFC calls are large and consistent in all five mutants (e.g. Glra1, Mybpc3, Aldh3a1 up 8-15 fold, counts 20-40 v 280-560); they are not single-animal outliers.
IT5 sets on P47T (centred mean vs 10,000 decile-matched sets): ISR targets PFC -0.05, HPC +0.16, CTX +0.11, CB +0.21 (inside null in the three 5v5 regions; CB outside but 3v4); OXPHOS +0.00/+0.05/+0.14(out)/+0.32(out); glycolysis_lactate +0.17/+0.21/+0.26/+0.08, all inside. The cytosolic-ribosome control set sits outside its null in PFC and HPC (-0.10, -0.07), so small set shifts are not specific. Reading: a partial-loss missense does **not** resolve the ISR-sign conflict either; hippocampus shows no gene-level change at n 5 v 5.
GSE158681/2 (descriptive, `mouse_p17_summary.json`): genes at |cLFC|>=0.585, separated, TPM>=1 (up/down): H_S 549/1160, H_N 1405/1578, H_null 260/469, C_S 316/564; at >=1: 324/319, 462/515, 87/122, 128/143; at >=2: 85/56, 77/85, 15/10, 19/11. Of the hippocampal calls at 0.585, 865 of 1709 (S), 1436 of 2983 (N), 292 of 729 (null) also differ between control groups (flag BACKGROUND_CONFOUNDED; the cortex has no control-vs-control contrast, so its flag is NA, not "none"). At n 2 v 2 animal separation happens by chance in 1 of 3 genes, so these lists are a candidate pool for a replicated test, not findings. Median shifts -0.2 to -0.4 log2 (composition: oligodendrocyte transcripts fall).
Files: `results/p47t_{PFC,HPC,CTX,CB}_genes_FDR10.tsv`, `results/p47t_all_regions_tested_genes.tsv.gz` (all tested genes, 4 regions), `results/mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv`.

## 4. The second finding: MTBLS12344 became public (it was 404/401 in IT6-IT7) but without a per-sample table
Public since 2026-11-02. The deposited MAF has 14 identified features, but all 40 experimental columns are EMPTY (values exist only in pooled-QC and blank columns); the assay sheet's Sample Name column is shifted against its MS Assay Name / raw-file columns (sample C1 is paired with raw file pooled_2_04). Per-sample centroided mzXML and RAW files are public (neg 10 MB, pos 15 MB each). So the metabolite question is computable by own peak integration, not by reading a table.
What I did (`mtbls_eic.py`, `mtbls_stats.py`): extracted-ion chromatograms (+-5 ppm, apex +-15 s, apex located on the 12 pooled-QC files only), declared QC gate = rank correlation with the deposited pooled values >=0.7. After correcting my own pool-name mapping error (attempt 1 kept in results/), the gate: citrate 0.97 and 2-hydroxyglutarate 0.98 PASS; **L-lactate 0.66 and itaconate 0.64 FAIL, so they were not analysed** (my blank-subtraction amendment could not change a rank correlation: it was vacuous, stated). Itaconate m/z 129.0194 is also the water-loss fragment of 2-hydroxyglutarate (co-elution at 750.5 s), an identity doubt of its own. Group labels come from the raw-file letter code (C ctrl-LacZ, D Wwox RNAi-LacZ, G ctrl-Abeta42, H Wwox RNAi-Abeta42): an assumption, UNVERIFIED against the paper.
Result (Welch t on log2 area, 5 v 5 pools of 10 heads, BH over the 2 passing features; `results/mtbls_wwox_rnai_contrasts.tsv`): LacZ background: citrate -0.39 log2 (CI -0.82 to +0.04, FDR 0.14), 2-HG +0.11 (FDR 0.63): no call. Abeta42 background: citrate -0.21 (FDR 0.28), **2-hydroxyglutarate +0.92 log2 (CI +0.37 to +1.47, FDR 0.013; TIC-normalised +0.93, FDR 0.010; passes all three thresholds)**. Reading: in the Abeta42 fly head, neuronal Wwox RNAi raises a TCA-adjacent metabolite pool about 1.9-fold; it is a metabolite POOL (not flux, not activity), in a mixed fly head, with the RNAi depth not in the deposit, in one of four tested cells (no interaction test, two contrasts x two features tested, not corrected across contrasts), single lab. **The lactate and pyruvate readout that mattered most is NOT answered**: lactate failed my gate, pyruvate is not among the 14 identified features.

## 5. What remains wet-lab, and the precise locus of each missing datum
* Protein or activity in any WWOX-deficient neural system (proteome, phospho-eIF2a, ATF4 protein, translation, PDH/LDH activity, NAD(H), flux): no deposit; O13.
* Per-animal protein/activity for P47T and a replicated neuron-targeted deletion (n 2-3 now): O14; GSE158684 raw reads (SRX9206272-79) are `hup`.
* Lactate/pyruvate in MTBLS12344: not wet-lab; needs a targeted re-integration (lactate gate failure is the locus: pooled-QC order disagrees with the deposit; fixing it requires the authors' integration table, which the deposit lacks) or the RAW files with a vendor tool. Do not ask the authors for it without the operator.
* E-MTAB-14792: access decision (403), not a computation.

## 6. Not verified / limits
Nothing here read a paper in full text, so there are no receipts (`receipts/` is empty). Age of GSE215425 animals is not in the deposit. P47T is a missense with protein present: its contrasts are not a WWOX-absence model. No variance moderation (n 5v5 power is modest; hippocampus null result is "no call at this power", not "no effect"). MTBLS12344 group assignment, RNAi depth and the lactate identity are unverified. Spearman on 12 near-identical pools is a weak gate (CV 5-14 percent).

## 7. Reproduce (inputs by sha256 in `sources.tsv`; fetch to any directory)
```
python3 -I analyse_it24_p4.py GSE215425_processed_data.csv.gz GSE158681_Wwox_mutant_Hippo_RNA_TPM_Table.txt.gz GSE158682_Wwox_neuronal_Del_Cortex_RNA_TPM_Table.txt.gz Mus_musculus.GRCm38.cdna.all.fa.gz ../hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv results
python3 -I mtbls_eic.py qc <dir_of_negative_mzXML> m_MTBLS12344_..._v2_maf.tsv results      # then:
python3 -I mtbls_eic.py samples <dir_of_negative_mzXML> s_MTBLS12344.txt results
python3 -I mtbls_stats.py results/mtbls_sample_areas.tsv results/mtbls_wwox_rnai_contrasts.tsv
```

## Integrator status (2026-11-04)

Produced by one delegate, not independently verified in IT24 (the verifier covered P1, P2, P6 and P12). Not consumed by the generator: the P47T per-region lists and the mouse descriptive lists are candidate pools with their stated limits; the MTBLS12344 result is two metabolite pools in a mixed fly head, with two of four metabolites failing the QC gate, and is not evidence of a WWOX effect on lactate, pyruvate or flux. Older documents that call MTBLS12344 "not public" are superseded by this folder (pointer lines appended to the census documents).

## IT27 verification of section 4 (`verification_it27_p2_20261104`, a different actor, metadata and integration done before reading the producer numbers)

Verdict: VERIFIED with a narrower perimeter. Group letters C/D/G/H confirmed by the ISA sample sheet (MS Assay Name matches the raw-file code in 40 of 40 rows; the Sample Name column is the corrupted one); unit = one pool of 10 heads, n=5 per cell. All 34 checksums match. Corrections: the lactate gate is not a robust fail (0.74 here, 8 of 20 window variants pass) but lactate is unusable anyway (blank is 50 percent of a median sample); itaconate is a 2-HG in-source water-loss fragment (constant ratio 0.098); the MS-only assay cannot separate L- from D-2-HG or isomers. 2-HG rises 1.9-fold with Wwox RNAi inside the Abeta42 background (Holm-6 0.006) but the genotype x background interaction is nominal (p 0.027, Holm 0.13, leave-one-out 0.005-0.054, authors' own adjusted p 0.53) and the authors had already published these effects (Supp. Table 4): a re-derivation, not a new finding. Use: a conditional modifier in a stress state, low pertinence to the reference genotype, an abundance (not flux or activity); it cannot guide a pharmacological selection, it can narrow a question (stress-state readout versus primary WWOX-loss readout) and points to chiral 2-HG, clean targeted lactate/pyruvate and a Wwox-null or ISR-inhibited neuronal model.
