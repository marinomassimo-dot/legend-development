# Pre-analysis note (written before the count table was opened for any computation)

Scientist `scientist-d`, IT12 package P2-P47T, 2026-10-31 UTC. Not blind: stated in README section 1.

## What I had seen before writing this note
* The task text, which states the sign of the Fig 8b / Fig 9c enrichment (positive NES, about 1.3 to 2.3) from the repository manifest.
* I then looked at Figure 8 and Figure 9 images (so the NES bar lengths and the n = 4 v 3 dendrogram of Fig 9a were seen).
* IT10 P2.1 README (organoid selective-response pattern, mouse P17 null contrasts) and IT10 tables `maturity_stress_check_it10_p21.tsv`, `mouse_p17_hif_genes_it10_p21.tsv`; IT11 P2.3 README (NRF2 organoid rows, P47T cerebellum remarks).
* The GEO series header, sample titles and the shape of the count table (37 libraries, 55,010 rows, integer counts). **No gene-level value of any gene named below had been looked at.**

## Units and contrast
Unit = animal (a library is one animal's tissue region). Contrast = Wwox P47T/P47T vs WT/WT within one region (HPC, CTX, PFC: 5 v 5; CB: 3 v 4 as the library titles and the Fig 9a legend show). Regions are analysed separately and not pooled; the three forebrain regions come from the same 10 animals and are not three independent confirmations.

## Gene sets (fixed now)
* HIF_SEL_UP6 (up in the organoid, none of the IT7 six): Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3.
* HIF_FLAT6 (flat in the organoid): Pgk1, Aldoa, Eno1, Pkm, Pfkp, Ndrg1.
* HIF_OTHER_1: Vegfa (reported singly, not in either set).
* NRF2_5: Nqo1, Hmox1, Gclm, Srxn1, Txnrd1.
* IT7_OBS6 (observation only, never enters a decision statistic; guard IT7_READOUT6): Slc2a1, Hk2, Ldha, Ldhb, Bnip3, Pdk1.
* Regulator transcripts, observation only: Wwox, Hif1a, Epas1, Hif3a, Arnt, Egln1, Egln2, Egln3, Vhl, Nfe2l2, Keap1.
* ACTIVITY_IEG (neuronal-activity transcripts): Fos, Fosb, Junb, Jun, Egr1, Egr2, Egr4, Arc, Npas4, Nr4a1, Nptx2, Bdnf, Dusp1.
* Composition marker sets (declared by me, small, NOT BRETIGEA): ASTRO (Gfap, Aqp4, Aldh1l1, Slc1a3, Slc1a2, Gja1, Sox9, Vim, Cd44, Serpina3n, Lcn2), MICRO (Aif1, Cx3cr1, Tmem119, P2ry12, Csf1r, Hexb, Cd68, Trem2), OLIGO (Mbp, Plp1, Mog, Mobp, Mag), NEURON (Snap25, Syt1, Rbfox3, Slc17a7, Gad1, Gad2, Stmn2, Camk2a). Vim, Cd44, Serpina3n, Lcn2 are reactive-astrocyte genes and are in ASTRO on purpose: the question is how much of a set shift travels with gliosis.
* Hallmark sets: MSigDB mouse hallmark release 2023.2.Mm (`mh.all.v2023.2.Mm.symbols.gmt`). The authors cite a hallmark library without a release; the contents of HYPOXIA and GLYCOLYSIS can differ between releases (the release I use spells the ROS set "OXIGEN"; the paper writes "OXYGEN"). HYPOXIA_minus_IT7six and GLYCOLYSIS_minus_IT7six are the sets with the six IT7 genes removed (HK2 etc. sit in both hallmarks).
* Classes for the leading-edge breakdown (declared): CANON_HIF = Adm, Aldoa, Ankrd37, Bhlhe40, Bnip3, Bnip3l, Car9, Ddit4, Egln3, Ero1l, Eno1, Hilpda, Hk2, Ldha, Ndrg1, P4ha1, P4ha2, Pdk1, Pfkl, Pfkp, Pgk1, Pkm, Plod2, Slc2a1, Vegfa, Lox, Pgm1, Tpi1, Gapdh; IEG_STRESS = Fos, Fosb, Jun, Junb, Atf3, Ier2, Ier3, Egr1, Klf6, Btg1, Btg2, Ppp1r15a, Cdkn1a, Dusp1, Nr4a1, Zfp36, Sik1, Ddit3; GLIA_REACTIVE = Gfap, Vim, Cd44, Timp1, Serpine1, Serpina3n, Lcn2, S100a10, S100a6, Lgals3, Mt1, Mt2, Cp, Ccn1, Ccn2, Tgfbi, Tnfrsf12a; everything else OTHER.

## Pre-declared questions and decision rules (thresholds are mine, arbitrary, labelled as such)
Q-A. Does HIF_SEL_UP6 move up in P47T? Rule: region mean log2FC of the set >= +0.30 and exact permutation p (two-sided, over all animal label splits) <= 0.05 -> "up".
Q-B. Is the shift selective, as in the organoid? Rule: (mean HIF_SEL_UP6 - mean HIF_FLAT6) >= +0.30 with exact permutation p <= 0.05 and HIF_FLAT6 |mean| < 0.30 -> "organoid-like selective"; both sets up -> "generic glycolytic/hypoxia-type shift"; neither -> "no shift".
Q-C. NRF2_5 sign (up/down/flat) by the same thresholds, reported with HMOX1 separately (a heme/stress gene that is not NRF2-specific).
Q-D. Pre-registered expectation (informed, not blind): the CB result will be less reliable than the forebrain one because 3 v 4 gives a minimum two-sided exact p of 0.057; I do not expect any CB gene-level result to pass an exact permutation test.
Q-E. Composition: Spearman correlation across the 10 animals of the HIF_SEL_UP6 score with the ASTRO score, and the same within genotype; a set shift whose per-animal scores track ASTRO is called "travels with gliosis"; this cannot be turned into a causal statement because ASTRO is itself a consequence of genotype (n = 10, df small).
Q-F. Leading edge: for HYPOXIA and GLYCOLYSIS in each forebrain region, which class (CANON_HIF, IEG_STRESS, GLIA_REACTIVE, OTHER) supplies the leading-edge genes. A hallmark enrichment whose leading edge is mostly IEG_STRESS / GLIA_REACTIVE is "not evidence of HIF activity".
Q-G. Method check: my re-implementation of GSEA (pre-ranked by Welch t, weight 1, gene-label permutation) will be compared with the authors' bars by direction only. Their ranking metric, library release and permutation scheme are not stated, so equality of NES is not expected and is not a test.
Q-H. Validation of my edgeR-like pipeline: log2FC of genes on the authors' DEG lists (Supplementary Data, |log2FC| > 1, FDR < 0.05) against my values: correlation and sign agreement.

## Sensitivity (declared)
Sex-adjusted model (genotype + sex) beside the unadjusted one. In the deposit titles the HPC/CTX/PFC WT group is M3, M2, M1, F5, F4 (3 M 2 F) and the P47T group M7, M6, F9, F8, F10 (2 M 3 F), while Methods say "2 males and 3 females" per group: a sex imbalance of one animal and a Methods/deposit mismatch, to be reported.

## Not done / not possible here
Protein, HIF compartment, oxygen condition, lactate, flux, seizure timing per animal, age per animal (Methods give 150 to 280 days as a range), batch: none is in the deposit.

## Addendum written after the first run (disclosed deviations and post hoc steps)
1. Correction of Q-D: for the 3 v 4 cerebellar design the minimum exact two-sided permutation p is 1/35 = 0.029 (the mirror split has different group sizes), not 0.057. My expectation that no CB gene-level result would reach exact p <= 0.05 was WRONG: several named CB genes do (Ankrd37, Hmox1, Srxn1, Nfe2l2, Ldhb, Arnt, plus Gfap, Mbp, Mobp, Nptx2). These are nominal, uncorrected over about 120 named-gene tests.
2. Added after seeing the first set-level table (all post hoc, exploratory, labelled so in the README): leave-one-animal-out ranges; an expression-matched random-gene null for set means; per-animal pivot with Nptx2/Bdnf; sample-identity and genotype-separation check (`sample_identity_check_it12.py`); hallmark variants without the IT7 six and without declared glia/IEG genes; pixel measurement of the Fig 8b / 9c bars; a cross-check of my log2FC against the authors' DEG sheets (declared as Q-H beforehand).
3. The "high-activity animals" (P47T M6 and F8) are a post hoc designation from the Nptx2/Bdnf values; they are not a pre-declared stratum.
4. Q-H outcome: the authors' DEG sheets are reproduced from the deposit for CTX, PFC and CB (r 0.97 to 0.999) and NOT for HPC (r about 0.5); see README section 3.
5. Rule outcome (declared thresholds): no region meets "HIF_SEL_UP6 up" (>= +0.30 with p <= 0.05); no region meets "organoid-like selective"; HPC meets "NRF2_5 up" (+0.33, p 0.024); CTX HIF_FLAT6 (+0.25, p 0.008) is below the declared magnitude threshold and is reported as a sub-threshold observation.
