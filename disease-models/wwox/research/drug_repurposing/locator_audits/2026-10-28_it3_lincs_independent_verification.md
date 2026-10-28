# Independent verification: LINCS iteration 3 local level 5 run (GSE92742)

Actor scientist-a (did not produce the work). 2026-10-28. Subject: `gse156243/lincs_it3_local_level5_20261027.md`, `lincs_it3_local_level5.py`, `derived/lincs_it3_local_level5_summary.json`, `derived/lincs_it3_S1_survivors.tsv`, at main 67da3e93. Not WWOX evidence. Constraints kept: no registration, no contact, no spend; GEO HEAD/GET of the 1.4 KB checksum file only; nice 15 / ionice idle, 2 BLAS threads.

My own code is `2026-10-28_it3_lincs_independent_verification.py` (this directory). It reads the gunzipped raw gctx (`0/DATA/0/matrix`), `sig_info`, `gene_info` and the GSE156243 counts, uses the producer's query-set gene lists only as input, and builds its OWN 1,000 matched random sets (own implementation of the decile matching, seed 777, not the producer's seed or cache). It does not read the producer's `scores.npy` or `extract.npy`.

## Verdicts

| # | Item | Verdict |
|---|---|---|
| 1 | SHA-512 of the level 5 gz | **Reproduced** |
| 2 | 10 WWOX CGS signatures: S1 score, zM, same-line percentile (HCC515, MCF7, PC3-144h) | **Reproduced** (within null sampling noise) |
| 3 | Hit definition and the 205,034 denominator, two sets (S1, K2) | **Reproduced** (counts within 1.1 percent) |
| 4 | Amendment did not change threshold/null/funnel/prediction; declaration text unchanged | **Reproduced for the declaration and for the thresholds; two disclosure gaps** (below) |
| 5 | Interpretive statements | **Mostly supported; two overstatements (plus the K2 factor)** (below) |

## 1. Checksum
I hashed the cached `GSE92742_Broad_LINCS_Level5_COMPZ.MODZ_n473647x12328.gctx.gz` (21,328,033,748 B) with `sha512sum` and compared it with the line for that file in `GSE92742_SHA512SUMS.txt.gz` fetched fresh from GEO today: identical (`6a3115cf3aaa402b...f4c5f6e010208a2a`), and identical to the value in the md. The 23,380,287,022 B gctx was the object used below; it opens with shape 473,647 x 12,328, contiguous (no chunking), and all 473,647 column ids are in `sig_info`. Whether the gctx is a faithful gunzip of the verified gz was not separately hashed; its size matches the md and every number below reproduces from it.

## 2. WWOX CGS signatures
Selection from `sig_info`: exactly 10 `trt_sh.cgs` rows with `pert_iname == WWOX` (A375, A549, ASC, HA1E, HCC515, HEPG2, MCF7 144 h, NPC, PC3 96 h, PC3 144 h), as the md says. The 3 hairpin-level `trt_sh` rows per line (plus HT29 and VCAP, which have no CGS row) are correctly excluded. Mine versus reported (S1 in-space 372 up / 215 down reproduced):

| Signature | S1 raw (mine / md) | S1 zM (mine / md) | Same-line percentile (mine / md) |
|---|---|---|---|
| HCC515 96 h | 0.253 / 0.253 | 5.02 / 5.12 | 0.985 (n 2,408) / 0.984 (2,408) |
| MCF7 144 h | 0.060 / 0.060 | 0.95 / 0.91 | 0.502 (5,064) / 0.497 (5,064) |
| PC3 144 h | -0.261 / -0.261 | -5.28 / -5.21 | 0.015 (5,166) / 0.015 (5,166) |
| PC3 96 h | -0.024 / -0.024 | -1.26 / -1.30 | 0.276 / 0.274 |

The other six raw scores also match to 3 decimals (A375 0.149, A549 0.407, ASC 0.107, HA1E 0.214, HEPG2 0.395, NPC 0.378); zM differs by at most 0.2 (A549 4.91 vs 4.95, HEPG2 4.51 vs 4.42, NPC 3.59 vs 3.78), which is the sampling noise of an independent 1,000-set null. Percentile is "among all CGS signatures of the same cell line" (PC3 pools 96 h and 144 h, as the md's n = 5,166 shows).

## 3. Hit counts and denominator
Denominator: `sig_info` has 205,034 `trt_cp` rows and the matrix has the same 205,034 (also 36,720 `trt_sh.cgs`); reproduced. Definition re-implemented: score = mean z over up genes minus mean z over down genes, zM = (score - null mean) / null SD per signature, hit at zM <= -3 / >= +3. Note the producer's nulls for every set (including K1, K2) are S1-sized matched random sets; I followed that design.

| Set | Reverse (mine / md) | Mimic (mine / md) |
|---|---|---|
| S1 | 18,431 / 18,629 (-1.1 %) | 30,649 / 30,786 (-0.4 %) |
| K2 | 10,540 / 10,619 (-0.7 %) | 9,507 / 9,362 (+1.5 %) |

Differences are of the size expected from different null draws. I did not rebuild the per-compound funnel (C1-C5), the covariate regression or the PCA; those are "not checked" here. I only read the summary: the S1 / K1 / K2 / S3 funnel numbers in the JSON agree with the md text (109 / 306 / 123 / 117 reverse; 124 mimic for S1; 233 rows in the survivors tsv = 109 + 124).

Also reproduced from my pass over all 36,720 CGS signatures: share with S1 zM >= 2 is 36.1 % (md 36.1 %), zM >= 3 is 24.8 % (md 24.9 %); K2 >= 2 is 17.0 % (md 16.8 %), K2 >= 3 is 7.4 % (md 7.4 %).

## 4. Amendment and declaration
- `git diff 072639eb 2c0e8f1f` on the md: 35 added lines and zero deleted or changed lines. Sections 1 to 3 (feasibility, question, declaration, predictions P1-P6) are byte-identical to the first commit; what was added is section 3a and the RESULT block. Reproduced.
- Script diff: the amendment hunks are exactly PCA subsample 30,000 -> 10,000, chunk 4,000 -> 2,000, scores through `open_memmap`. No threshold (|z| 3, 2-cell, 5 percent), null (1,000 matched + 1,000 permuted, seed 20261201), funnel step or prediction line is touched. Reproduced.
- Gap 1 (disclosure). The script diff has a second change in the report stage that section 3a does not list: the same-cell-line percentile (`prc`, comment "cross-context control, added 2026-10-28") and the `pct_zM_ge_2` background. It is an analysis added after the first results were seen (the withdrawal of the P6 reading depends on it). R2 describes the quantities, but 3a states "no result had been seen" and "operational changes only"; the cell-line control is neither. It does not change a declared threshold, and it makes the verdict more conservative, but it is a post-hoc control and should be labelled as such.
- Gap 2 (unquantified). The PCA subsample reduction can change PC1-PC3, hence the C3 covariate step (957 survivors), the P4 R-squared and the downstream 109 / 124. "No threshold changed" is true; "does not change the result" is not tested (no run with 30,000 rows). The negative verdict does not hinge on it (C0-C2 counts and the K-control comparison are independent of the PCs), but the exact survivor numbers are conditional on the 10,000-row PCA.

## 5. Interpretive statements
- "Every real DE list exceeds matched random sets by an order of magnitude": **supported for S1, S3, K1 (14x, 14x, 17x the random 99th percentile 1,325); slightly overstated for K2** (10,619 / 1,325 = 8.0x reverse, 9,362 / 1,255 = 7.5x mimic; versus the random maximum 2,330 / 3,292 it is 4.6x / 2.8x; versus the median about 50x). Its use is correct: the md itself says the random-gene null shows only that coherent lists differ from incoherent ones and is not WWOX specificity. That caveat is adequate; P1 "held" should not be read as a WWOX-specific finding. Also N1 / N3 (random sets with the same gene content as S1's size) correlate 0.63 / 0.69 with S1 in raw score, a sign that much of S1's score is a gene-expression-level axis, not a contrast axis.
- "Negative result limited to this contrast and method": **supported**. The md states it three times (header, R3, R4) and lists the undone work (GSE70138, hairpin-level, efficiency, only two K controls). One refinement: the verdict is a negative on "survives the paired controls" with only two real-contrast controls whose survivor counts are themselves high (K1 306); it is not a negative on LINCS reversal in general, which the md does not claim.
- Declared rule "above every control" (P5): **correctly applied, and the md understates it slightly.** S1 reverse survivors 109 are not above K1 (306), K2 (123) or S3 (117), so the rule is not met and DISCARD follows. Wording "inside the range of the real-contrast controls" is true, but S1 is in fact the lowest of the four real contrasts in the reverse tail. S3 is a near-duplicate of S1 (raw correlation 0.999), so it is not an independent control; only K1 and K2 are.
- "36.1 % of CGS signatures have zM >= 2 withdraws the real-signal reading": **reproduced and logically sound.** With a background of 36.1 % (and 24.8 % at >= 3), 5 of 10 WWOX signatures at >= 2 is close to the background-expected count of 3.6; the binomial probability of 5 or more of 10 at p = 0.361 is about 0.27. So P6 "at least 5 = real signal" cannot be read as signal. Two further points go beyond the md: (a) the background itself is cell-line dependent, which the same-line percentile addresses; (b) with the same-line percentile, only HCC515 (0.985) is conspicuous and PC3-144h is strongly opposite.
- **Overstatement A (R4 point 3):** "8 of 10 above their cell line's median". By the md's own table, MCF7 is 0.497 (0.502 in my run), a coin flip, so the count is 7 of 10 clearly above, 1 at the median, 2 below. R2's "eight of ten on the positive side, two very weakly" is the more careful wording; R4 should say 7 of 10 (plus MCF7 at the median). With a sign test, 7 of 10 has two-sided p about 0.34; nothing here is a tilt that can be separated from chance, and the md's "weak, heterogeneous tilt" is, if anything, generous. A tilt across HCC515, A549 and HEPG2 (percentiles 0.82-0.98) is the only substantive part.
- **Overstatement B (R4 point 1):** "the iteration-2 service-based picture is reproduced on the whole matrix without a cap". I could not check iteration 2's list against the local run; the overlap with iteration 2's survivors is explicitly "not claimed" in R3, so "reproduced" in R4 is stronger than R3 supports. Not checked.

## Net
Everything numeric that I rebuilt from the raw files reproduces (checksum, signature set, S1 scores, zM, percentiles, hit counts within about 1.5 percent, background 36.1 / 24.8 percent). The negative decision stands. Wording fixes suggested: R4 "8 of 10" -> "7 of 10 plus MCF7 at the median"; add the cell-line-matched percentile to section 3a as a post-result control; state that the survivor counts depend on the 10,000-row PCA.
