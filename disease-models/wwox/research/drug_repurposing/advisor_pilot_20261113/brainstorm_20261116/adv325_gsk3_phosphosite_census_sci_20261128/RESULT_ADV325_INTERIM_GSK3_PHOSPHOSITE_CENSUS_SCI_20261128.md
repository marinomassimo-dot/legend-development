# ADV-325 interim result (SCI bd, 2026-11-28T12:49:39Z): GSK3-substrate phosphosite census, text screen and first readings

Hypothesis level; not medical advice. Frozen rule: `PREREG_ADV325_GSK3_PHOSPHOSITE_CENSUS_SCI_20261128.md` (sha256 0983cfd7e3660537d9f43f7d28878d885d2d3fba860aad89448308098bf3585d, frozen 2026-11-28T12:48:22Z, pushed before any hit was read). **Status: OPEN.** One reader only; no second reader yet; no figure image opened; no delegate.

## Method and limits
Script `census_strict.py` (run with `python3 -I`): strict regex for GSK3 pSer9/21 and pTyr216/279, beta-catenin Ser33/Ser37, CRMP2 Thr514, glycogen synthase Ser641 and Tau sites, over every held text under `files/fulltext` that mentions WWOX or WOX1 (508 files, 394 distinct ids; the earlier loose screen of 400 files had silently cut the list at its first 400). It reads TEXT (main text, legends, Methods, supplement text); a phosphosite shown only in an image or only in a supplementary figure without legend text is invisible to it. Ledger lookup by PMID before any "not held": not needed here (every item below is a held file).

## Screen result
19 files (13 distinct PMIDs) have a strict site-term hit. Reading the matched sentences:
| Text | What the hit is | Class (frozen rule) |
|---|---|---|
| Cheng 2020, PMID 32000863, Fig 7c (also three further held copies) | Wwox-/- against +/+ and +/- brain (cerebellum, hippocampus, cortex): dephosphorylation of GSK3B Ser9; densitometry ratios of phospho or total GSK3B to beta-actin printed on the blot; "representative results of four independent experiments"; animals per genotype not stated; no per-experiment values | **R**. Age: the Fig 7c legend says postnatal day 20, the Methods (Western blotting) say tissue isolated at postnatal day 14: a held contradiction inside one paper |
| Wang 2012, PMID 22193544 | SH-SY5Y WWOX RNAi raises pTau S396 (Figs 1d and 1e); WWOX overexpression lowers GSK3B-stimulated Tau S396 and S404 (cells; Fig 4b in vitro kinase); mouse-brain co-immunoprecipitation | Cell or in-vitro material: **Q-cell candidate**, never H1; quantification and n of Figs 1d, 1e, 4b NOT YET READ |
| Liu 2018, PMID 30158849 | review sentences on Akt phosphorylating GSK3B Ser9 | no data (**N**) |
| Taouis 2021, Pascual 2025, 40327201, 36572560 (N-GID paper) | hit on the beta-catenin phospho term or an antibody list only; no WWOX-deficient phosphosite readout in the matched sentences | **N** on the text read |
| Carvalho 2022, Wainberg 2023, PMID 41135097, Tang 2026, Karaer 2026, Lee 2017, Liu S 2024 | Tau-site terms; WWOX appears as a risk gene or a mention; no WWOX-deficient material identified in the matched sentences | **not read to the end**; open |

## Against the pre-registration
* Predicted passes 3 (range 1 to 6): so far 0 firm passes, 2 candidates (Cheng Fig 7c class R, Wang 2012 cell class, unquantified in my reading); within the range once the Tau papers are read, outside it from below if they hold no WWOX-deficient material.
* Class Q in Wwox-null brain at P7 to P28 (the strong counterexample to H2): **not observed**. The only held same-tissue developmental readout is Cheng Fig 7c, class R with an age printed as both 14 and 20 days.
* H2 favoured on the text screen; H1 not supported at this point.

## What it changes (provisional until a second reader confirms)
* GSK3 same-animal panel: stays a NEW laboratory observation. Cheng Fig 7c can serve as a qualitative pointer (direction: reduced Ser9 in three regions), not as a baseline comparator: n of animals absent, age ambiguous (14 against 20 days).
* Lithium-also-lowers-WT confound: unchanged; no held phosphosite readout exists in lithium-treated tissue of any genotype.
* RP-026: no change of order from this census; the lab dependency stays (same-animal substrate panel).

## Open
1. Read Wang 2012 Figs 1d, 1e, 4b (quantification, n, unit); read the seven Tau-term texts for WWOX-deficient material.
2. Image-only phosphosite panels: one blind delegate on the whole Cheng Fig 7c and Wang Fig 1 pages (effort stated, no numbers named) if ADV wants the counts.
3. Second reader on every sentence before IT uses any of them.
