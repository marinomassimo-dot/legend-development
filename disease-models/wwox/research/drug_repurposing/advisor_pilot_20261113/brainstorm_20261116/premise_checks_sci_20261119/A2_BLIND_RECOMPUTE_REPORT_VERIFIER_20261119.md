# A2 report: blind recompute of ADV-068, ADV-069, ADV-070 (hypothesis level; no dose; not medical advice)

Blindness: I read only the three frozen pre-registration files and the held data. No result, script, out-table or note of the three analyses was seen. No network. Code and raw printouts are in this folder (`common.py`, `adv068.py`, `adv069.py`, `adv069_alt.py`, `adv070.py`, `*_out.txt`; run with `python3 -I`). Transcript to symbol: `gene_symbol:` of the r92 headers, TPM summed over transcripts of a symbol (111,083 transcripts, 34,794 symbols, none unmapped; every sample sums to 1e6). All gene lists were fully present in every table (no gene missing, including H2AFX, MRE11, TP53BP1, TP53I3, RAD51AP1 in the organoid table).

## 1. Numbers

### ADV-068, primary contrast C_S (cortex, 3 KO vs 4 Ctrl, GSE158682)
| quantity | value |
|---|---|
| PV_SET reference-normalised (raw) | -0.6534 (-0.6038) |
| INT_NONPV reference-normalised (raw) | -0.0536 (-0.0040) |
| LATE_NONPV reference-normalised (raw) | -0.3337 (-0.2840) |
| OL_GUARD raw mean (Mbp, Plp1, Mog, Mobp) | -1.0230 |
| REF_STABLE raw | +0.0496 |
| other raw, descriptive | astro guard +0.297; microglia guard -0.940; Wwox -1.451 |
| KO animals, ref-normalised PV_SET (KO1, KO2, KO3) | -0.7237, -0.9458, -0.2907 (raw: -0.5069, -1.0843, -0.2201) |
| Control animals, leave-one-out ref-normalised PV_SET (C1..C4) | +0.1826, +0.1505, -0.2946, -0.0384 (raw: -0.1017, +0.3940, -0.3595, +0.0673) |
| KO ref-normalised LATE / INT | LATE -0.5067, -0.3024, -0.1919; INT -0.0614, -0.1268, +0.0273 |
| composition caveat | OL_GUARD <= -1.0 is TRUE (by 0.023); REF_STABLE move 0.05 < 0.3 FALSE. So flagged composition-confounded; verdict already on reference-normalised values |

Hippocampal contrasts, descriptive (ref-normalised PV / INT / LATE; raw OL; raw REF):
| contrast | PV | INT | LATE | OL raw | REF raw | Wwox raw |
|---|---|---|---|---|---|---|
| H_S (3 v 2) | -1.0942 | +0.0649 | -0.5856 | -2.4546 | -0.0424 | -1.562 |
| H_N (2 v 2) | -0.4880 | -0.2337 | -0.1143 | -1.4793 | +0.1560 | -1.918 |
| H_null (2 v 3) | -0.6368 | -0.0681 | -0.2456 | -2.0139 | -0.0446 | -1.875 |
(Same arithmetic would read R-B, R-C, R-D respectively; descriptive only, no verdict by the stop rule.)

### ADV-069, organoid GSE156243, primary set P53_RESP (14 genes, all present)
Null: 2000 draws, `numpy.random.default_rng(20261119)`, one stream; random sets of 14 genes drawn without replacement from genes whose six-library mean log2(CPM+1) is within 0.5 of the set's own mean (3.754; pool 2349 genes, the set's own genes excluded); the same draws give both clusters. Null of the N1-adjusted shift = null raw shift minus the cluster's PROLIF shift (PROLIF shift is constant across null sets). Band = 2.5th to 97.5th percentile; percentile = share of null <= observed.

| | cko1+cko2 | cko3+cko4 |
|---|---|---|
| raw shift | -0.1157 | -0.0177 |
| PROLIF shift | +0.2872 | -0.1397 |
| N1-adjusted shift | -0.4029 | +0.1220 |
| null band (adjusted frame, seed 20261119) | [-0.493, -0.054] | [-0.054, +0.530] |
| percentile of adjusted shift (two-sided empirical p) | 13.2 (p2 0.27) | 32.5 (p2 0.65) |
| inside the 2.5-97.5 band? | inside | inside |

Seed sensitivity (seeds 1, 2, 3, 20261119): c12 percentile 13.2 to 14.4, band lower edge -0.496 to -0.488, upper -0.054 to -0.036; c34 percentile 32.0 to 33.8. No seed moves anything outside the band.

Noise floor (WT vs WT, P53_RESP): raw |d| = 0.0476 (2|d| = 0.0953). On the N1-adjusted value (PROLIF removed the same way) |d| = 0.1568 (2|d| = 0.3135).

Maturity score (NEU - PROG shift) per library: cko1 -1.153, cko2 -0.573, cko3 -1.236, cko4 -0.659, cwt1 -0.092, cwt2 +0.092.

N2 genotype term c (set value = a + b x maturity + c x KO, six libraries, 3 residual df):
| set value used | c | leave-one-library-out c (drop cko1, cko2, cko3, cko4, cwt1, cwt2) | range |
|---|---|---|---|
| raw set value (primary reading) | -0.2249 | -0.2634, -0.1653, -0.1663, -0.2832, -0.2129, -0.2293 | [-0.283, -0.165] |
| N1-adjusted set value (alternative) | -0.3292 | -0.5359, +0.1372, +0.0317, -0.6784, -0.4789, -0.2743 | [-0.678, +0.137], sign changes |
| per-cluster genotype terms, raw | c12 -0.2495, c34 -0.1644 | | |
| per-cluster genotype terms, N1 | c12 -0.4787, c34 +0.0389 | | |

Other sets, same arithmetic (adjusted shift c12 / c34; percentile in adjusted-frame null c12 / c34; N2 c on raw set value, LOLO range): REPAIR_S -0.0996 / -0.0298; 81.8 / 3.5; c -0.062 [-0.536, +0.288]. DDR_CORE -0.2861 / +0.0027; 50.3 / 8.2; c +0.139 [-0.141, +0.308]. CC_NEG -0.1462 / +0.3272; 74.6 / 84.4; c -0.068 [-0.117, -0.013]. None is outside its band in either cluster (REPAIR_S c34 at percentile 3.5, p2 0.07, is closest). Full tables in `adv069_out.txt`.

### ADV-070, cortex C_S (animals ordered Ctrl1-4, KO1-3)
| quantity | value |
|---|---|
| stage score | +0.1230, -0.2054, -0.0234, +0.1059 ; -0.5067, -0.3024, -0.1919 |
| separation (mean KO - mean Ctrl) | -0.3337 (Ctrl mean 0 by construction; sd Ctrl 0.152, sd KO 0.160); r(score, KO) = -0.78, VIF 2.6 |

| seed | Delta | c | b (score) | leave-one-animal-out c range | label by the frozen rule |
|---|---|---|---|---|---|
| Slc12a5 (self-left-out score, 4 LATE genes) | -0.6793 | -0.6473 | +0.136 | [-0.966, -0.262] | STANDS |
| Kcnq2 | -0.7113 | -0.8106 | -0.298 | [-1.114, -0.526] | STANDS |
| Grin2c | -1.0477 | -0.8666 | +0.543 | [-1.029, -0.592] | STANDS |
| Npy | +0.9499 | +1.0891 | +0.417 | [+0.779, +1.264] | STANDS |
| IEG panel (all 12 measurable) | -1.3361 | -1.3168 | +0.058 | [-1.377, -1.142] | STANDS |
| PV panel (positive reference) | -0.3540 | -0.4464 | -0.277 | [-0.873, -0.053] | NO_SHIFT (|Delta| < 0.5) |
The literal "three or fewer per arm" reading makes all of them descriptive, as the text says. Background flag not computed (see section 4).

## 2. Labels
* ADV-068 C_S: **R-B** (PV -0.653 <= -0.5; LATE -0.334 <= -0.25; the R-A animal clause also fails: KO3 -0.2907 is above control C3 -0.2946 in ref-normalised values, and raw too). Omitting one LATE_NONPV gene at a time: omit Grin2a **R-B** (LATE -0.378); omit Slc12a5 **R-D** (-0.235); omit Nrgn **R-B** (-0.465); omit Camk2a **R-B** (-0.287); omit Scn8a **R-B** (-0.303). So the label rests on the Slc12a5 contribution, and sits 0.08 log2 from the threshold.
* ADV-069 P53_RESP: **not S-ok**. Closest stop label: **S2** (see ambiguity 10); S1 does not literally apply, because no cluster has a signal that passes all tests.
* ADV-070: five seeds STANDS, PV panel NO_SHIFT (C_S only).

## 3. Ambiguities, resolution, effect

1. ADV-068 R-B "(the same sign and at least half the PV shift)" vs "LATE at most -0.25". Primary: -0.25 threshold. Alternative: also require |LATE| >= half |PV| (= 0.327 here). Full set: R-B either way (0.3337 vs 0.327, margin 0.007). Omit Camk2a (-0.287) and omit Scn8a (-0.303) would become R-D under the alternative. Label change in two of five leave-one-gene-out labels; numbers unchanged.
2. ADV-068 R-A third clause: "PV_SET value" raw or reference-normalised. Both computed: it fails either way; moot because R-B applies.
3. ADV-068 "moves by at least 0.3": taken as absolute value; no effect (0.05).
4. ADV-068 OL_GUARD "mean at most -1.0": taken as mean of the four oligodendrocyte genes raw log2 shift (-1.023); one could read the guard over the OL genes weighted differently or on mean log2 FC of the mean-TPMs; at -1.023 it is 0.023 from the threshold. Verdict unaffected (rules always use ref-normalised values).
5. ADV-068 control animal value: control animal vs mean of the other 3 controls, ref-normalised with the same animal's own LOO REF. Alternative (ref LOO of whole arm) not computed; differences would be of the order of the control spread (0.1 to 0.2), do not change the label.
6. ADV-068/070 TPM summing over transcripts of a symbol: ADV-070 says "as in ADV-068"; ADV-068 itself says only "deposited TPM table" and does not mention the summation or the Ensembl map (only ADV-070 does). Implemented as ADV-070 states. No alternative was tried.
7. ADV-069 expression: CPM from the sum of all gene counts including genes outside the panels; used as written. Set value for the N2 fit: "set value" is not defined as raw or N1-adjusted; primary raw, alternative N1 (table above). Under the alternative, c = -0.329 passes |c| >= 0.3 but LOLO changes sign, so the "keeps its sign" clause still fails. No label change.
8. ADV-069 "c" is a single genotype term over all four KO libraries; the rule says "in both clusters ... c has the same sign" which a single c cannot test per cluster. Alternative: a separate c per cluster (table above): raw c12 -0.25 / c34 -0.16 (both below 0.3 in magnitude); N1 c12 -0.48 / c34 +0.04 (opposite signs). No label change; the difference in numbers is > 0.05 log2.
9. ADV-069 null "genes within 0.5 of the set's own mean": primary literal (gene mean within 0.5 of the set mean); alternative per-gene matching (each random gene within 0.5 of one set gene). Alternative gives c12 percentile 7.4 to 8.7, band [-0.46, -0.03]; c34 24.6 to 25.5. No label change; the band edges move by up to 0.04. Also whether the set's own genes are excluded from the pool: excluded in the primary; including them changes percentiles by about 1 point.
10. ADV-069 which stop applies. c34 has N1 adjusted +0.122 (opposite sign, below 0.3), c12 has -0.403 but inside the null band. Raw P53_RESP shifts are -0.116 and -0.018, below 0.3 before any normalisation. S1 ("signal in one cluster only") needs a signal in one cluster; I read c12 as inside the null band, so not a signal; S2 ("lost after normalisation") is the nearest fit but the signal was never present raw. I report "not S-ok, S2 (nearest), with the note that neither stop strictly describes a set with no raw signal". If c12 is read as a signal in one cluster, label would be S1 instead. Moderate label risk.
11. ADV-069 noise floor: "absolute difference between the two WT libraries' set values (each against the other)": the two values are +d and -d, so the difference is 2|d|; natural reading |d|. Both given (0.048 vs 0.095 raw; 0.157 vs 0.314 on the N1-adjusted value). Under 2|d| on the adjusted value c12 (0.403) still exceeds it; c34 does not under either. No label change. Which quantity the floor applies to (raw or N1-adjusted) is not stated; I applied to both.
12. ADV-069 "two-sided empirical percentile": reported as share <= observed (percentile) and p2 = 2 x min(tail); the rule compares to the 2.5th to 97.5th percentile band, which I used.
13. ADV-069 what the observed shift is placed against: the N1-adjusted shift in the null of adjusted shifts (null minus the PROLIF shift of the cluster). If someone places the adjusted shift in the unadjusted null, c12 sits at percentile 0.0 (outside) and c34 at 70.0, i.e. this choice could flip c12 to "outside the band". I take the like-for-like reading, but the text does not say which; this is the most label-relevant ambiguity in ADV-069 (it would move c12 to a signal in one cluster, therefore S1).
14. ADV-070 stage score uses log2(TPM+1), the statistic uses log2(TPM+0.5): used as written. Alternative pseudocount 1.0 for y: Delta and c change by <= 0.03, no label change.
15. ADV-070 leave-one-animal-out: whether the score baseline is recomputed after dropping a control animal. The baseline is a gene-wise constant, so it adds a constant to every animal's score and is absorbed by the intercept: c is identical. No effect.
16. ADV-070 leave-self-out for Slc12a5: removed from LATE (4 genes). Without removing, c = -0.469 (change 0.18 log2, label unchanged STANDS).
17. ADV-070 "not measurable" rule: mean TPM < 1 in both arms; all 12 IEG genes and the others were measurable (Bdnf 2.47 TPM in both arms is kept).
18. ADV-070 "|c| at least half of |Delta|" where c has the sign of Delta, but c can exceed Delta in magnitude (here for Kcnq2, Npy and the PV panel, where |c| > |Delta| because the within-arm slope b has the opposite sign to the arm difference of the score). The text does not say what to call c larger than Delta; the rules give STANDS.

## 4. Statements I could not implement as written
* ADV-070 background flag: "from P3a, read not recomputed": P3a's table is outside the permitted files, so BACKGROUND_CONFOUNDED is not applied; I did not compute control-vs-control contrasts either.
* ADV-070 sign agreement "in the number of the four deletion contrasts in which Delta and c share a sign" for non-C_S contrasts and the comparison with P3a's per-gene log2 ratio: not asked of me and P3a not available; only the contrast C_S was done.
* ADV-070 "sha256 identical to IT13's pins and ADV-068's": checksums not verifiable without those files.
* ADV-068 whether one GEO sample is one animal: assumed, as stated.

## 5. Design observations that could change a label (not run errors)
* ADV-068 R-B outcome is marginal on two thresholds: LATE -0.3337 vs -0.25 and (alternative text) vs half-PV 0.327; omitting Slc12a5 alone flips it to R-D, and the oligodendrocyte guard (-1.023 vs -1.0) trips the composition caveat by 0.023. The cortex deposit also shows a large microglia guard fall (-0.94) and astrocyte guard +0.30, i.e. glial composition moves, not just oligodendrocytes. The reference set barely moves (+0.05), so ref-normalisation does not correct a composition change.
* ADV-068 control values use a 3-animal baseline (LOO) and KO values a 4-animal baseline: noise floor for control animals is not on the same footing; control spread (-0.29 to +0.18) is comparable to the lowest KO animal (KO3 -0.29), which is why the R-A animal clause could not hold even for a true PV-specific effect at this n.
* ADV-069 N1 subtracts the PROLIF shift, which has opposite signs in the two clusters (+0.287 and -0.140); an adjusted shift for a set with no raw shift (P53_RESP raw -0.12 and -0.02) is therefore manufactured by the PROLIF difference (c12 adj -0.403 is the PROLIF shift, not the set). The null band is shifted by the same amount, which the like-for-like reading handles; the unadjusted-null reading (ambiguity 13) would mistake it for a signal. N1 also doubles the noise (set minus PROLIF).
* ADV-069 N2 has 6 points and 3 parameters (3 residual df), and the maturity score is nearly collinear with KO (WT +/-0.09 vs KO -0.57 to -1.24); c is unstable (LOLO sign changes for the N1 version). One c over four libraries cannot demonstrate "both clusters". Rules name no stop for "no raw signal".
* ADV-070 stage covariate: within-arm sd of the score (0.15) is half its between-arm separation (0.33); r(score, KO) = -0.78. The slope b is estimated from 7 points and takes both signs across seeds (Slc12a5 +0.14, Kcnq2 -0.30, Grin2c +0.54, Npy +0.42, IEG +0.06, PV panel -0.28), so c deviates from Delta by noise, not by a stage effect; the PV positive reference gets c larger than Delta (the adjustment moves it away from zero, the opposite of the expected partial explanation), which the pre-registration did not anticipate. All five seeds STAND because the score has little leverage, not because they are demonstrably stage-independent. In addition, the covariate (LATE minus REF) is computed from the same animals' expression and includes Slc12a5 and Camk2a, which are themselves part of the PV/Kv/ion channel biology under test (leave-self-out only handles the seed itself, not correlated genes such as Kcnq2).
* Cross-analysis: ADV-070's stage score for KO animals equals ADV-068's reference-normalised LATE value of those animals (same baseline for KO animals) -> not independent of ADV-068's R-B numbers (-0.5067, -0.3024, -0.1919 here equal ADV-068's KO LATE values).
