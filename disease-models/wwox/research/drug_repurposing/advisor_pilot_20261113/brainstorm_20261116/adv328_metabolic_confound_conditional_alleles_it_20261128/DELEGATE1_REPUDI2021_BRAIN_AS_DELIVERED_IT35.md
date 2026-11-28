# ADV-328 delegate 1: Repudi 2021 Brain (PMID 33914858), independent read, as delivered (IT35, 2026-11-28)

Hypothesis level; not medical advice. `legend-delegate`, sonnet 5.5, **effort HIGH stated in the dispatch**; no census numbers in the brief; the delegate cannot write report files, so this is the reply, condensed by IT35 without changing any value (tables Q1, Q2, Q4, Q5 and the disagreements; the Fig 3A 94-label list and the full quotes are in the transcript only). Sources opened by the delegate: text, supplement PDF File009, xlsx File012, File013, File014, Fig 1 to 7 and Fig 3 panels as images (300 dpi crops).

## Q1 What the two supplementary tables are (confidence high)
| | File012 = Supplementary Table 1 | File013 = Supplementary Table 2 |
|---|---|---|
| Sheet name | `SKO_vs_S_Crtl_6_6_Crtx,hippo` | `KO_WT_7_vs_7_unBatch` |
| Comparison | S-KO (Synapsin-Cre) vs S-Control, cortex and hippocampus pooled, P17, 6 vs 6 samples (S-KO 3 cortex + 3 hippocampus; S-Control 4 cortex + 2 hippocampus) | hippocampus only, P17, **7 KO-group vs 7 control-group samples pooled across genotypes** (KO: Wwox-null 2, N-KO 2, S-KO 3; controls: WT 3, N-Control 2, S-Control 2) |
| Evidence | text counts 730 up and 579 down (P < 0.01, fold change > 1.5) reproduced from raw `pvalue`; matches the Fig 3A legend n | matches Supp Fig 4A legend (n = 14 hippocampi) and the text sentence on Wwox-null and N-KO compared with S-KO |
| Sign | log2FoldChange = log2(KO / control); Wwox itself -1.86 (File012, padj 5.06E-6) and -3.14 (File013, padj 2.51E-28) | same |
IT35 note: my first reading of File013 as "systemic null against wild type" was wrong; it pools three knockout lines. It is not a systemic-null table.

## Q2 Marker rows as stored (padj / log2FC; positive = higher in KO group)
| Gene | File012 (S-KO, cortex+hippocampus, 6 v 6) | File013 (pooled KO lines, hippocampus, 7 v 7) |
|---|---|---|
| Npy | 4.34E-10 / +1.89 | 1.16E-7 / +1.62 |
| Gfap | 1.13E-2 / +1.68 | 3.68E-8 / +1.65 |
| Cd68 | 4.95E-3 / +0.94 | 5.33E-6 / +1.05 |
| Sst | 2.64E-3 / +1.06 | 7.82E-2 / +0.65 |
| Pvalb | 3.44E-2 / -0.75 | 4.07E-6 / -0.99 |
| Vim | 4.58E-2 / +0.98 | 0.428 / +0.49 |
| Gad1, Gad2, Vip, Aif1 | 0.543/-0.18; 0.117/+0.52; 0.898/+0.08; 0.69/+0.30 | 0.989/0; 0.21/+0.23; 0.922/+0.04; 0.491/+0.35 |
| Pdgfra, Cspg4 | 0.185/-0.30; 0.984/+0.01 | 5.87E-2/-0.26; 2.4E-5/-0.45 |
mRNA only; DESeq2 alpha 0.1 in the methods. Fig 3B (12 genes, "selected genes known to be upregulated in epileptic models") draws Npy and Gfap; Fig 3A draws Gfap and Npy.

## Q4 Protein or section readout of interneuron or glial-reactivity markers
None. No IF/IHC/Western/count for PV, NPY, SST, GAD65/67, VIP, Iba1, or GFAP intensity/morphology/count in N-KO, S-KO, O-KO, G-KO or Wwox-null. GFAP is used only to validate the deletion (Supp Fig 1F, G-KO P18, n not stated). Antibody list (File014) has no PV/NPY/SST/GAD/VIP/Iba1 antibody; primer list is oligodendrocyte-lineage only. The paper says (p. 3073) the excitation/inhibition balance was not quantified.

## Q5 Blood chemistry, weights, death
Blood chemistry and counts: not found anywhere (glucose/bicarbonate/calcium occur only in slice recipes). Body weight: Fig 1H S-KO vs S-Control four mice per genotype, day 16 about 6.5 g vs 11.3 g (read from plot); Fig 1B Wwox-null WT 3, KO 3, day 16 about 5.8 vs 10.4 g. Survival: S-KO n = 15, first death about day 17, last about day 28 (legend P 0.0001); Wwox-null n = 11, about day 19 to 25. S-KO seizures begin P9 (n = 6, 68.5 +/- 13.4 s, P14-18).

## Disagreements and unread items (delegate)
Fig 3A "top 100" has 94 readable labels and Gfap sits at padj rank 344 among upregulated genes in File012 (selection rule not reproduced); Pdgfra and Cspg4 are "slightly higher" by qPCR (Supp Fig 5C) but not in RNA-seq; Fig 2 text and legend disagree on slice and animal counts; death age "3-4 weeks" vs first S-KO death about day 17; Fig 3C GO text too small; videos not played; Supp Figs 2-4, 6-9 read from legends and text only.

## Round 2 (same delegate resumed, effort HIGH, clauses B1 to B7 judged against this paper only; condensed by IT35)
Rate: **1 of 7 clauses MUST CHANGE (14 percent)**; 6 of 7 SUPPORTED with ADD. All first-composition clauses were IT35's.
| # | Verdict | What changed in the wording |
|---|---|---|
| B1 drivers | SUPPORTED + ADD | allele provenance: the flox allele was documented earlier (ref Abdeen 2013), this paper used it; conditional lines mixed C57BL6/J;129sv, Rosa26-tdTomato reporter; Wwox-null line (FVB) studied alongside |
| B2 S-KO seizures, growth, death | SUPPORTED + ADD | "day 17 to 28" is the delegate's reading of the Fig 1I survival steps (about +/-1 day); the paper says 3 to 4 weeks; seizures from P9 are text only, duration quantified at P14-18 (68.5 +/- 13.4 s, n = 6); ataxia (clasping, Supp Fig 2C) |
| B3 RNA-seq | SUPPORTED + ADD | the 6 v 6 is tissue-unbalanced (S-KO 3 cortex + 3 hippocampus; S-Control 4 cortex + 2 hippocampus); Pvalb, Npy, Sst baselines differ several-fold between tissues; the stored L2FC may not be tissue-adjusted (not stated); delegate's own split of normalised counts (log2 of group means, not DESeq2): cortex Gfap +1.15, Npy +1.21, Sst +0.69, Pvalb -0.34; hippocampus Gfap +2.47, Npy +2.92, Sst +1.60, Pvalb -1.35; Pvalb padj 0.034 and Gfap padj 0.011 modest |
| B4 no protein/section/chemistry | SUPPORTED + ADD | also holds for Wwox-null; GFAP IF exists only as deletion check (Supp Fig 1F); videos not played |
| B5 O-KO, G-KO no phenotype | SUPPORTED as the authors' wording, says MORE than the data | what was examined: gross appearance P17, weight P4-16 (O-Control 11, O-KO 10; G-Control 8, G-KO 9), survival, O-KO clasping and MBP only; no RNA-seq, EEG or seizure monitoring; deletion by IF only, efficiency not quantified |
| B6 inference "secondary to seizures and systemic illness" | **MUST CHANGE** | "systemic illness" goes beyond the data (growth retardation and neurological signs, no blood chemistry); the authors do not draw the inference; O-KO and G-KO (healthy) have no transcript data, so no healthy cell-restricted RNA-seq comparison exists |
| B7 negative | SUPPORTED for interneuron-restricted deletion; partly wrong as a conjunction | no glucose anywhere; body weights do exist at P4 and P7 (before P9) but it is not stated that the same animals were followed; every molecular or electrophysiology readout is P13 or later |

## Round 3 (same delegate, effort HIGH; repaired clauses B2', B3', B4', B5', B6', B7')
Rate: **2 of 6 repaired clauses MUST CHANGE (33 percent)**: the repairs themselves carried new errors.
* B2': "Nestin- and Synapsin-Cre deletion reproduce seizures from P9" was wrong for Nestin-Cre. P9 onset is stated for S-KO only; the N-KO statement is "tremors/seizures and ataxia" with no onset age (p. 3065); the Introduction groups both, which makes P9 read as shared. N-KO first death about day 19, last about day 26 (n = 14); S-KO about 17 to 28 (n = 15).
* B6': "have no marker data" for O-KO and G-KO was too wide: O-KO has MBP immunostaining at P17 ("no major changes", Supp Fig 8); G-KO has no marker readout beyond the WWOX deletion check. What is true: no transcriptome and no interneuron or reactivity-marker data. Also: one route not secondary to seizures or growth exists but covers OPC differentiation only (Wwox-null DRG neurons co-cultured with wild-type OPCs, Fig 6, n = 4 vs 4, two experiments).
* B3', B4', B5', B7' SUPPORTED with ADD (by-tissue Pvalb figures are descriptive, no within-tissue test; glucose is absent at every age; GFAP IF exists only as a deletion check; weights at P4 and P7 exist for null, N-KO and S-KO and the legend does not say whether the same mice were followed).
