# ADV-325 interim against HE's ADV-326 blind table (SCI bf, 2026-11-28)

Hypothesis level; not medical advice. Left: `RESULT_ADV325_INTERIM_GSK3_PHOSPHOSITE_CENSUS_SCI_20261128.md` (one reader, text only, written before HE's table). Right: `../adv326_blind_gsk3_he_20261128/TABLE_ADV326_HE.md` (HE, blind to this folder; figure pages). The interim is not edited; the corrections are here and carry into the final result.

| # | Source, figure | Interim said | HE's table | Verdict |
|---|---|---|---|---|
| 1 | Cheng 2020, PMID 32000863, Fig 7c, arms | +/+, +/-, -/- mouse cerebellum, hippocampus, cortex | the same nine arms | agree |
| 2 | Fig 7c, readout | pSer9 and total GSK3B, densitometry ratios to beta-actin printed on the blot; values not transcribed | 18 printed values (2 targets x 3 tissues x 3 genotypes) | agree; values added by HE |
| 3 | Fig 7c, replicate | "four independent experiments"; animals per genotype not stated; no per-experiment values | the same; also not printed whether a value is the shown blot or a mean of four, and no test or spread for the blot | agree |
| 4 | Fig 7c, age | legend P20, Western blotting Methods P14 | legend P20 (page 12), Methods P14 (page 4) | agree; **open premise** |
| 5 | Fig 7c, antibodies | silent | no anti-GSK3B and no anti-pSer9 antibody named; Methods names anti-WWOX, anti-DCX, anti-beta-actin and cites a previous method | addition; Methods sentence confirmed by SCI in `PMID32000863_Cheng2020_PMC.xml` |
| 6 | Fig 7c, Wwox line used | silent | not printed in the legend | addition |
| 7 | Wang 2012, PMID 22193544, pTau S396 under WWOX RNAi | "Figs 1d and 1e" | 1d is the pTau S396 blot; 1e is the percentage of differentiated SH-SY5Y cells | **differ: interim wrong.** The Results sentence cites "Figures 1d and e" for two readouts (pTau S396 and neurite outgrowth); SCI reread the sentence in `PMID22193544_Wang2012_PMC.xml` |
| 8 | Wang Fig 1d, quantification and n | not yet read | none printed, no n (blot only) | addition: **class R** (cell material) |
| 9 | Wang Fig 4b | in vitro kinase | in vitro kinase with added GST-WWOX; blot and stain only; no n | agree on content; **differ on class:** added-protein material is not WWOX-deficient, so 4b is **N** under the frozen rule |
| 10 | Wang 2012, class | "Q-cell candidate" | no quantified pTau value under WWOX deficiency in 1d | **differ: class R, not Q-cell** |

## Ratios recomputed from HE's printed values (SCI arithmetic; one value per lane, no spread, so none of these is tested)

| Fig 7c, Wwox -/- against +/+ | cerebellum | hippocampus | cortex |
|---|---|---|---|
| pSer9-GSK3B / beta-actin | 1.3 / 2.7 = 0.48 | 2.0 / 3.6 = 0.56 | 2.5 / 3.9 = 0.64 |
| total GSK3B / beta-actin | 2.4 / 2.2 = 1.09 | 2.6 / 2.3 = 1.13 | 2.6 / 2.2 = 1.18 |
| pSer9 / total, derived, **not printed** | 0.44 | 0.49 | 0.54 |

+/- against +/+ for pSer9 / beta-actin: 3.1 / 2.7 = 1.15, 3.5 / 3.6 = 0.97, 3.8 / 3.9 = 0.97.

## Consequence
No delegate was needed for the figure pages: the two differences are errors in the interim's wording and class, both settled by the legend and Results text. Figure values rest on one reader (HE) until the second reader of the final result has read them.
