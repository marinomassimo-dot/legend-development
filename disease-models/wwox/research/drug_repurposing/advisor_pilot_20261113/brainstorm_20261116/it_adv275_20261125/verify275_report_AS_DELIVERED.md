# verify275: WWOX after HDAC-inhibitor (VPA) exposure in four GEO series (blind re-reading)

Fold = treated mean / control mean (linear normalised values). p = two-sided Welch on log2 values,
unadjusted across contrasts. Call criterion: "up"/"down" if p < 0.05 (direction from the fold);
otherwise "not distinguished". Scripts: scripts/analyze.py; full output: data/analysis_output.txt.
All samples are Homo sapiens bulk RNA-seq.

## Summary

| contrast | n ctrl/trt | H1F0 fold (p) | CDKN1A fold (p) | WWOX fold (p) | call |
|---|---|---|---|---|---|
| GSE241903 VPA vs vehicle | 3/3 | 1.64 (0.035) | 0.60 (0.0056) | 1.81 (0.011) | up |
| GSE166297 VPA IC5 vs no exposure | 8/8 | 1.54 (6e-10) | 0.50 (8e-6) | 1.45 (3.0e-4) | up (technical replicates only) |
| GSE129241 VPA day 1 vs Ctrl day 1 | 4/4 | 2.14 (3e-4) | 1.90 (0.040) | 1.21 (0.020) | up, small |
| GSE305320 VPA vs Ctrl | 3/3 | 2.62 (0.060) | 2.05 (0.19) | 0.86 (0.25) | not distinguished |

## Cross-check on NCBI-generated raw counts (median-of-ratios computed here on the arms only / CPM)

| series | H1F0 | CDKN1A | WWOX | WWOX p |
|---|---|---|---|---|
| GSE241903 | 1.61 / 1.66 | 0.59 / 0.61 | 1.86 / 1.92 | 0.026 / 0.028 |
| GSE166297 | 1.53 / 1.57 | 0.50 / 0.52 | 1.59 / 1.63 | 2e-8 / 1e-8 |
| GSE129241 | 2.15 / 2.27 | 1.91 / 2.02 | 1.21 / 1.28 | 0.040 / 0.018 |
| GSE305320 | no NCBI counts (HTTP 404) | | | |

## Per contrast

### 1. GSE241903
- System: whole spinal cord organoids, WTC line, WT; 96 h. Replicate unit: "in triplicate" (C4, C5, C6; type not further stated).
- Vehicle: GSM7745343-45 (C4_FGF, C5_FGF, C6_FGF). VPA: GSM7745346-48 (C4_VPA, C5_VPA, C6_VPA).
- File: GSE241903_FGFvsVPA_deg.txt.gz, row ENSG00000186153, deposited normalised count columns.
- WWOX vehicle 156.74, 137.78, 112.47; VPA 227.58, 270.83, 236.41. FPKM: 1.958, 1.718, 1.403 / 2.831, 3.370, 2.942 (fold 1.80).
- Deposited DEG: log2FC(FGF/VPA) = -0.851, padj 7.9e-4.

### 2. GSE166297
- System: H9 hESC-derived NPCs differentiated 10 days to neuron-astrocyte co-culture, exposed over those 10 days.
- Replicate unit: 8 "technical replicates from one experiment" (deposited wording). The p value does not describe biological reproducibility.
- Controls: control-1..8 = GSM5067976-83. VPA IC5: Valproic_acid_IC5-1..8 = GSM5068064-71. Run (batch) labels are matched between arms.
- File: GSE166297_counttable.txt.gz (DESeq2-normalised), row ENSG00000186153.17.
- WWOX ctrl 118.29, 170.98, 109.50, 132.77, 162.86, 132.59, 108.93, 133.94; VPA 213.63, 227.08, 158.43, 178.83, 226.03, 159.34, 201.79, 186.59.

### 3. GSE129241
- System: hESC-derived NGN2 induced neurons, FACS-isolated; VPA added day 1, analysed after 72-96 h (source name "day4"). "4 independent batches".
- Ctrl day1 Rep1-4 = GSM3703362-65; VPA day1 Rep1-4 = GSM3703366-69.
- File: GSE129241_Supplementary_Table_T1_final.xlsx, sheet "Day 1_All Genes" (FPKM), row WWOX; columns Ctrl1/Ctrl2/Ctrl_3/Ctrl_4, VPA1/VPA2/VPA_3/VPA_4.
- WWOX ctrl 9.481, 7.885, 8.642, 9.630; VPA 10.824, 10.112, 10.231, 11.994.

### 4. GSE305320
- System: H9 hESC organoids (hPCOs), harvested day 20. VPA dose and duration are not in the series matrix. Extraction text says "2-3 biological replicates per group"; three samples are deposited for these arms.
- Ctrl: hPCO_Ctrl_109/178/92 = GSM9168690-92 (columns Ctrl_109, Ctrl_178, Ctrl_92). VPA: hPCO_VPA_168/178/77 = GSM9168693-95.
- File: GSE305320_counts_final_drug.xlsx, sheet counts_final (raw counts), rows WWOX, H1-0, CDKN1A; median-of-ratios on the six samples (computed here).
- WWOX ctrl (92, 109, 178) 198.14, 147.83, 181.58; VPA (77, 168, 178) 148.20, 169.64, 136.20. CPM fold 0.88 (p 0.30).

## Odd points
- CDKN1A goes DOWN (about 0.5-0.6) in GSE241903 and GSE166297 although H1F0 goes up. The two sentinels disagree there; H1F0 alone indicates the exposure acted.
- GSE305320 sentinels move up in the mean but neither reaches p < 0.05 and per-sample spread is large (CDKN1A raw control counts 360, 670, 2470). Exposure action is less firmly shown there, so the WWOX null is weak evidence of no effect.
- GSE305320 series summary says "bulk-RNA sequencing ... using 10x Genomics"; library prep text says TruSeq.
- GSE129241 GPL18573 (day 21, not used): sample "Ctrl day21 Rep4" is annotated "treatment: Valproic acid"; titles say day21 while source names say day28. Day-1 annotations are consistent.
- GSE129241 NCBI raw-count file lacks some non-day-1 samples; all eight day-1 samples are present.
- GSE166297: exposure spans differentiation, so a change in cell composition could contribute to any fold. The text states 0.25% DMSO as final concentration but VPA was dissolved in medium; whether controls and VPA wells contained DMSO I cannot tell from the matrix.
- No missing samples in the four contrasts.
