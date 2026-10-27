# LINCS iteration 3: local level 5 (MODZ) analysis of the GSE156243 KO contrast, feasibility and declaration

Scientist-d, task SD-IT3-LINCS-20261027. Exploratory. Not medical advice; class level. Everything LINCS-derived is NOT WWOX EVIDENCE. A knockout signature is not a rescue signature; a reversal ranking never proves rescue; same-lineage resources are one vote.

## 1. Feasibility (measured 2026-10-27, HEAD and range requests on the GEO FTP, no registration, no key, no e-mail)

Base `https://ftp.ncbi.nlm.nih.gov/geo/series/GSE92nnn/GSE92742/suppl/` (GSE70138: `.../GSE70nnn/GSE70138/suppl/`). Both series serve `Accept-Ranges: bytes`. Sizes as listed by the index (gz files):

| GSE92742 file | Size | Use |
|---|---|---|
| `Level5_COMPZ.MODZ_n473647x12328.gctx.gz` | 21,328,033,748 B (20 GB) | the 473,647 level 5 signatures (compounds and genetic perturbations) x 12,328 genes |
| `Level2_GEX_epsilon_n1269922x978.gctx.gz` | 2.3 GB | landmark-only expression, not signatures |
| `Level3` / `Level4` (`...n1319138x12328`) | 49 GB / 50 GB | not needed |
| `Level1_LXB` tar | 1.2 TB | no |
| `sig_info`, `sig_metrics`, `inst_info`, `pert_info`, `cell_info`, `gene_info`, `gene_info_delta_landmark` | 11 MB, 12 MB, 11 MB, 1.1 MB, 2.5 KB, 212 KB, 18 KB | metadata, all small |
| `SHA512SUMS.txt.gz` | 1.4 KB | checksums |

GSE70138 (the 2017 expansion): level 5 `COMPZ_n118050x12328` 5.0 GB; `sig_info` 1.9 MB; `sig_metrics` 3.0 MB; `inst_info` 4.6 MB; `pert_info` 80 KB.

- **Smaller subsets on GEO: none.** The only level 5 file of each series is the single matrix (no per-cell-line, compound-only or landmark-only subsets). The matrix is gzip-wrapped HDF5: a gzip stream has no random access, so range requests cannot extract columns remotely; the file must be fetched whole and gunzipped (about 23 GB uncompressed float32 at 473,647 x 12,328 = 23.4 GB), then columns selected by `sig_id` with h5py. The CLUE `GSE92742` mirror and the CLUE API need a key or registration and were not used.
- **Public service routes (already tested in iteration 2):** SigCom LINCS `enrich/ranktwosided` is key-less, answers a ranked list with a total (`Content-Range .../693215`) and takes a `limit` (100 used; the total shows the full ranking exists server side); L1000FWD `sig_search`/`result/topn` is capped at 50 per direction by the service. Both are one lineage with this matrix. The local route removes the cap and, more importantly, makes per-signature nulls possible; the services give top-N lists only.
- **Machine:** 4 CPU threads, 15 GB RAM (about 8 GB available at start), disk 142 GB free of 193 GB. Download measured at 26 MB/s on a 100 MB range probe: 21.3 GB is about 14 minutes. Gunzip to scratch about 23 GB. Extract of the 205,034 `trt_cp` plus 36,720 `trt_sh.cgs` signature columns about 12 GB float32 on scratch (memory-mapped, not held in RAM). Scoring is one dense matrix product (rows x 12,328 against 12,328 x 2,007 weight columns), about 2e13 floating-point operations, minutes on 4 threads. Estimated total wall time under 1.5 hours; disk peak about 60 GB, all in git-ignored scratch (`files/geo/GSE92742/`, cache directory). Cost is modest.
- **Licence/terms:** GEO data are public; submitter requests citation (Subramanian et al. 2017, Cell) and the GEO terms apply (no redistribution restriction stated on the series page; nothing from the matrix is committed, only compact derived tables). Record: url, date 2026-10-27, SHA-512 against the series `SHA512SUMS.txt.gz` (level 5 expected `6a3115cf...ed0f`; the full value is in the result section).

## 2. The discriminating question

Iteration 2 left three things the services cannot answer because they return only a top-N list and no null: (a) whether the S1 reversal ranking survives a **per-signature permutation null built from the same matrix** (not from three hand-drawn controls), (b) whether any compound reversal survives the **paired controls together**: label-permuted S1, content-matched random sets, the two KO pseudo-contrasts (K1 reached the strength of S1 in SigCom), a transcriptional-activity / general-stress covariate adjustment, cell-line recurrence and a frequent-hitter rate computed over 1,000 random sets rather than 8, with **both tails** read, and (c) whether the one **direct genetic comparator in the same library** agrees: the 10 `trt_sh.cgs` WWOX knockdown signatures (A375, A549, ASC, HA1E, HCC515, HEPG2, MCF7, NPC, PC3 x2), including a neural-progenitor line.

Would the answer change anything? (b) could change a counter-evidence entry or the status of "LINCS reversers" as a portfolio source (if no compound survives, LINCS reversal drops out as a source of candidates for this contrast, which iteration 2 already argued; if some survive they become hypotheses to be tested, not candidates). (c) could add a first independent genotype-contrast check (WWOX loss in a different system), the reopening condition of iteration 2 section 7. A priority or an experiment changes only if (b) leaves survivors that also have a mechanistic link; otherwise the result is a recorded limit. The expected outcome, stated before the run, is that it does not change a priority.

## 3. Declaration, fixed BEFORE the level 5 matrix was opened

Seen offline before this declaration: nothing from level 5; the iteration 2 results (section 1.3 of the iteration 2 note), the sig_info `pert_type` counts and the list of WWOX signatures in `sig_info` (10 `trt_sh.cgs` signatures; the 3 hairpin-level `trt_sh` signatures per cell are not used).

Method (script `lincs_it3_local_level5.py`, stages `extract`, `score`, `report`; seeds 20261201 and the sets in `derived/query_sets*.json`):
- Score of signature s for query set X: mean z over X's up genes minus mean z over X's down genes, using only genes in the 12,328-gene space (S1: 587 of 834). Reversal = negative; mimic = positive. Compound signatures = `pert_type trt_cp` (205,034). Genetic comparator rows = `trt_sh.cgs` (36,720).
- Nulls, per signature: 1,000 **matched random** sets (per in-space S1 gene, a random L1000 gene of the same organoid expression decile, arms disjoint, S1 genes excluded) and 1,000 **label permutations** of S1's own in-space genes between the arms. zM and zP = (score minus null mean) / null SD for that signature.
- Hit: zM <= -3 (reverse) or >= +3 (mimic) over compound signatures. Denominator of every hit count: the 205,034 compound signatures.
- Funnel per compound and tail, identical for S1, S3, K1, K2, N1-N3 and 30 matched random sets: C1 at least 2 distinct cell lines with zM hit; C2 and also zP hit in those signatures; C3 and also a hit after regressing zM on transcriptional-activity covariates (TAS, number of modulated landmark genes, mean |z|, share |z| > 2, first three principal components of the compound signatures, log dose, time); C4 not hit (same tail) in the other pseudo-contrast(s) K1/K2; C5 frequent-hitter rate below 5 percent (share of the 1,000 random matched sets whose top-100 compounds by best zM include it).

Predictions (each falsifiable by the summary JSON):
- **P1.** S1's count of reverse hits exceeds the 99th percentile of the same count over the 1,000 random matched sets (S1 differs from content; iteration 2 already saw the family concentration vanish with shuffled direction).
- **P2.** K1's reverse or mimic hit count also exceeds that 99th percentile (within-KO heterogeneity yields a pattern, as the K1 q-values suggested).
- **P3.** The Pearson correlation of raw scores over compound signatures between S1 and K1 or K2 is at least 0.3 (a shared axis); for random matched sets the median stays below 0.1.
- **P4.** The covariates explain at least 30 percent of the variance of S1's zM over compound signatures (R-squared).
- **P5.** Fewer than 5 compounds survive C1-C5 in the reverse tail for S1, and S1's survivor count is within the range of the random matched sets and of K1/K2 (the paired control). 5 or more survivors, above every control: INCONCLUSIVE-to-USEFUL as hypothesis seeds, no candidate. Fewer: DISCARD as a priority changer.
- **P6.** At most 2 of the 10 WWOX CGS signatures show S1 zM >= 2 in the mimic direction (a knockdown resembling the knockout contrast); at least 5 would be a real signal to follow up. Background rate is taken from all 36,720 CGS signatures.
Absence from a ranking is "not returned", never "ineffective". A survivor is a query output of a knockout contrast in tumour and non-tumour lines, not a candidate.
