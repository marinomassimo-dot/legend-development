# IT24 P4 pre-declaration (written before any per-gene value of the new tables was computed)

Date 2026-11-04. Non-canonical, not medical advice. Reference genotype class only. No contact, no registration, no e-mail sent.
Already seen before this file (so not blind): the IT7 E1 summary (6-gene module in P47T, per-region D), the IT6 P4 set results for GSE158681/2, and the GSE215425 sample titles.
NOT yet seen: any whole-genome P47T value, any whole-genome per-gene mouse P17 contrast.

## Contrasts (fixed)
A. GSE215425, counts, P47T/P47T vs WT/WT, one contrast per region: PFC 5v5, HPC 5v5, parietal CTX 5v5, CB 3v4. Unit = animal. Age of animals not stated in the deposit.
B. GSE158681/2 (transcript TPM summed to Ensembl-92 gene): H_S 3v2, H_N 2v2, H_null 2v3, C_S 3v4 (KO minus control). Unit = animal.
   B-ctl (background control): WT vs S_Ctrl, WT vs N_Ctrl, S_Ctrl vs N_Ctrl (no Wwox difference expected).

## Methods (fixed)
A: gene filter CPM>=1 in >=3 libraries of the region; size factors by median-of-ratios on filtered genes; y = log2(count/sf scaled to mean library + 0.5... see script) ; OLS y ~ genotype + sex; t test on genotype
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
