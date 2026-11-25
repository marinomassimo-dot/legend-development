# Blind check of the ADV-278 n arithmetic (SCI, 2026-11-25)

One delegate (`legend-delegate`; asked sonnet, effort high stated in the dispatch). It saw only two extracted files (protein values, transcript contrasts), not my numbers or the spec. Its report as delivered: `REPORT.md` in the job scratch folder (not kept); summary below.

| Item | Mine | Blind reader | Effect |
|---|---|---|---|
| Minimum detectable fold, n = 3, 4, 6, 8; s = 0.25, 0.43, 0.60 | e.g. n = 8, s = 0.43: 1.41 up / 0.71 down; n = 6: 1.54 | 1.41 / 0.71; n = 6: 1.53 (200,000 draws, exact t values by bisection, type I error 0.05) | agree to Monte Carlo error (largest gap 0.02 in fold) |
| Power at 1.5-fold (n = 8, s = 0.43) | 0.91 | 0.908 | agree |
| H1-0 line ratios | file ratios 1.82 to 3.54 | the file's ratios are **arithmetic**-mean ratios; geometric: D50 BIONi 2.15, HMGU1 1.82, KOLF2 2.76; KOLF2 D35 has one control pool, not evaluable | spec table now carries both: D50 SD 0.30 (geometric) vs 0.26; D35 0.26 on two lines vs 0.43 with the one-control line |
| Within-arm SD, mouse Wwox | 0.25 and 0.05 | 0.251 and 0.052 (control); treated 0.065 and 0.069 | agree |
| Transcript spread | 5 up-called deposits: mean 1.53, SD 0.22 | 8 eligible rows (not-distinguished included): mean 1.435, SD 0.262 | **my selection narrowed the spread**; spec now gives both |

Anomalies it listed that do not change a number: the transcript file carries no drug label (valproate supplied by the dispatch); the WWOX row label is "51741" in some rows; two deposits have two unlabelled rows each; GSE166297 is a mixed neuron-astrocyte co-culture; one striatum H1-0 row has p = 0.031 but the call is "not distinguished" (the call rule is IT's, not restated here).

Class of correction: **a spread taken from rows selected by their outcome is narrower than the spread of the eligible rows** (same family as "derived arithmetic is one error class"). Same model family: blind to the analysis, not independent of the model.
