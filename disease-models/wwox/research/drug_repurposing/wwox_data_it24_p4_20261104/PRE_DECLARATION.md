# IT24 P4 pre-declaration (written before any per-gene value of the new tables was computed)

Date 2026-11-04. Non-canonical, not medical advice. Reference genotype class only. No contact, no registration, no e-mail sent.
Already seen before this file (so not blind): the IT7 E1 summary (6-gene module in P47T, per-region D), the IT6 P4 set results for GSE158681/2, and the GSE215425 sample titles.
NOT yet seen: any whole-genome P47T value, any whole-genome per-gene mouse P17 contrast.

## Contrasts (fixed)
A. GSE215425, counts, P47T/P47T vs WT/WT, one contrast per region: PFC 5v5, HPC 5v5, parietal CTX 5v5, CB 3v4. Unit = animal. Age of animals not stated in the deposit.
B. GSE158681/2 (transcript TPM summed to Ensembl-92 gene): H_S 3v2, H_N 2v2, H_null 2v3, C_S 3v4 (KO minus control). Unit = animal.
   B-ctl (background control): WT vs S_Ctrl, WT vs N_Ctrl, S_Ctrl vs N_Ctrl (no Wwox difference expected).

## Methods (fixed)
A: gene filter CPM>=1 in >=3 libraries of the region; size factors by median-of-ratios on filtered genes; y = log2(count/sf + 0.5) (counts scaled by the size factor); OLS y ~ genotype + sex; t test on genotype
   (df = n - 3); Benjamini-Hochberg within region. No variance moderation (stated). Effect = log2FC median-centred over tested genes (also uncentred reported).
   Sensitivity: model without sex term.
B: n 2-4 per arm: NO inference. Descriptive only: mean TPM per arm, log2 ratio (pseudocount 0.5, median-centred), animal separation (every KO animal on one side of every control), universe mean TPM >= 1.
Thresholds (three, all declared now; none chosen after looking):
   A: T1 BH-FDR<0.10; T2 FDR<0.05 and |centred log2FC|>=0.585; T3 FDR<0.05 and |centred log2FC|>=1.
   B: T1 |cLFC|>=0.585 and separated; T2 |cLFC|>=1 and separated; T3 |cLFC|>=2 and separated (all with mean TPM>=1 in the higher arm).
Controls (declared): (1) Wwox transcript level per arm (P47T is a missense knock-in: no mRNA fall expected; a fall would signal NMD/allele effect); (2) sex check: Xist and Ddx3y/Uty separate all females/males in A;
   (3) reproduction of the IT7 E1 six-gene module signs in HPC (SLC2A1, HK2, LDHA, BNIP3 up; LDHB down, PDK1 ~0) with this independent code; failing it = my code differs, reported, not tuned;
   (4) B-ctl: genes passing a B threshold that ALSO pass it in a control-vs-control contrast are flagged BACKGROUND_CONFOUNDED.
Sets (extension of the named missing comparison): the IT5 declared sets (hnpc_gse126075_it5 per_gene_in_sets.tsv) in A, centred mean log2FC with 10,000 decile-matched random sets (seed 20261104). Verdict wording only descriptive.
Stop rules: if the sex-check or the Wwox control cannot be computed, report and stop. Nothing here is a WWOX-loss claim: P47T is partial loss with protein present.

## Addendum C (written 2026-11-04 after the MTBLS12344 release was discovered, before any abundance value was read)
Seen so far: the public listing, the sample sheet (design 4 cells x 5 pools of 10 heads, 14-day-old, pan-neuronal), and the names of the 14 identified features (no pyruvate; lactate, citrate, 2-hydroxyglutarate, itaconate present).
Contrast C1 (primary): Wwox RNAi vs RNAi Control, LacZ background, 5v5 pools (D1-5 vs C1-5). C2 (secondary): Wwox RNAi vs RNAi Control, Abeta42 background, 5v5 (H1-5 vs G1-5). CRISPRa (OE) arms: descriptive, not evaluated here.
Method: log2 of the abundance (floor: zero or missing values reported, not imputed); Welch t on log2 values; BH across the 14 features (4 features are duplicate ions of lysine and methionine and are kept, stated). Effect = difference of mean log2 (KD minus control) with Welch 95% CI.
Thresholds (three, fixed now): FDR<0.10 any size; FDR<0.05 and |log2FC|>=0.2; FDR<0.05 and |log2FC|>=0.585. Metabolites of declared interest (not a filter): L-lactate, citrate, 2-hydroxyglutarate, itaconate.
Perturbation control: Wwox depth in the fly head is NOT in this deposit (IT6: sequenced-head Wwox counts equal across arms); this stays a stated limit. A pool of 10 heads is the unit (N=5); metabolite pools are not flux or enzyme activity.

## Addendum D (written 2026-11-04 after finding that the MAF holds only pooled-QC and blank columns; the 40 experimental columns are empty; before any KD-sample peak area was computed)
The deposit has NO per-sample abundance table, but has centroided mzXML (negative polarity, orbitrap, 64-bit uncompressed) for every sample. Re-analysis possible now = own extracted-ion chromatograms.
Features: [M-H]- of L-lactate 89.0245, citrate 191.0199, 2-hydroxyglutarate 147.0299, itaconate 129.0194 (m/z and RT from the deposited MAF). EIC window +-5 ppm; area = trapezoid over RT apex +-15 s.
RT apex is located ONLY on the 12 pooled-QC files (never on KD samples) and frozen in results/mtbls_windows.json before the samples are integrated. QC control: my pooled-QC areas must rank-correlate (Spearman >= 0.7) with the deposited MAF pooled-QC peak values for the same feature; if not, the sample analysis is not run for that feature.
Normalisation: raw area (primary) and area / total ion current of the file (sensitivity). Contrasts, statistics, thresholds as in Addendum C (14 features reduced to the 4 declared ones: BH across 4).

## Addendum E (written 2026-11-04 after the QC gate was run on pooled-QC files only; no KD-sample area exists yet)
Gate result as declared in D, after correcting my own pool-name mapping error (attempt 1 assumed a column order; the assay sheet pairs MS Assay Name with raw file, which gives the mapping; attempt 1 kept in results/): Spearman citrate 0.97, 2-hydroxyglutarate 0.98 PASS; L-lactate 0.66 and itaconate 0.64 FAIL (< 0.7).
Per D the two failing features are not analysed in the samples. One amendment is declared here, decided on pooled-QC data only: recompute the same gate after subtracting the mean blank area (matrix_blank_1, matrix_blank_2, same window) from each pooled-QC area (lactate has a high blank). Same threshold 0.7, applied to all four features. A feature that passes ONLY after this amendment is analysed and labelled 'passed after blank-subtraction amendment'; one that still fails is not analysed. The sample analysis then uses the gate-appropriate area (blank-subtracted if that is what made it pass; raw otherwise for features that passed raw, with the blank-subtracted value as sensitivity).
Sample-sheet caveat declared: the assay sheet's Sample Name column is shifted against its MS Assay Name / raw-file columns (e.g. sample C1_KDExp is paired with raw file pooled_2_04). Group labels are therefore taken from the letter-number code of the raw file (C=RNAi control+LacZ, D=Wwox RNAi+LacZ, G=RNAi control+AB42, H=Wwox RNAi+AB42), which matches the sample sheet s_ file and the 5-per-cell design; this is an assumption, UNVERIFIED against the paper's supplement.
