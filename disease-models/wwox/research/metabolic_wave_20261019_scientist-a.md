# Metabolic wave 2026-10-19 — Scientist A, group G1 (lipids, very-long-chain fatty acids, peroxisome, sphingolipids)

Actor `scientist-a` · task `METAB-G1-A-20261019` · context_policy `QUESTION_DRIVEN` for every paper (the selection file's questions were held; no prior dossier or claim for any paper in the lot). Not medical advice. This note is the running per-paper record; the end-of-lot synthesis is the last section.

Lot order: tier 1 first (Saez 2010, Leduc 2011, Liu 2022 CAD/stroke, Liu S 2024 oleic acid), then tier 2, then tier 3, as listed in `metabolic_batch_selection_20261019.md`.

## Per-paper record

### PMID 20942981 — Saez 2010 (human genetics, HDL-C and TG, 801 Spanish adults)

Measures: common-variant association of 1045 WWOX-region SNPs (894 imputed) with HDL-C, TG and TG/HDL in one population sample; no multiple-comparison correction; haplotype tests in four regions. Does not measure: any loss-of-function allele, WWOX expression or protein, any carrier phenotype. Depth `complete_fulltext_read`, receipt `FTR-20261019-20942981-01`, 18 locators.
Findings that matter: the lead HDL variant of the 2008 study did not replicate (P 0.299); no intron-8 region is HDL-associated in the haplotype test; the smallest P anywhere is 2.4e-4 on an imputed SNP; Tables S2-S4 carry 39, 46 and 46 nominal hits of 1045 SNPs, no excess over the 5 percent chance expectation (descriptive; LD); Table S2 betas for two HDL SNPs differ from the body text with no unit stated. Changes: nothing in the working model; keeps the human lipid anchor at ESPANSIONE and argues for a DO_NOT_CITE note against any dose-effect reading. Selection question 2 (is the HDL association carried by heterozygous loss): this paper cannot speak to it. Commit candidate `CC-20261019-SCIENTIST-A-LIPID-01`.

### PMID 21444760 — Leduc 2011 (mouse QTL map x human HDL GWA; Wwox as candidate)

Measures: overlap of 92 human HDL GWA loci with mouse HDL QTL, and for Wwox a resequencing and liver-expression comparison of inbred strains (B6, CAST, CASA). Does not measure: any Wwox loss of function, brain, myelin, sterol. Depth `complete_fulltext_read` (PMC HTML, four figures, supplementary tables and figure via the PMC proof-of-work tool), receipt `FTR-20261019-21444760-01`, 20 locators.
Findings: the Wwox case rests on one SIFT-only, non-conserved missense change that does not segregate in the second cross, inside a 184-gene interval; qPCR shows no liver expression difference, yet Supplementary Table S10 prints a Wwox probe set at about +2.1 to +2.3 fold in both sexes that the footnote does not explain, and the Discussion claims the mouse confirms cis-regulation; the Discussion's "Wwox knockout is hypercholesterolemic" cites a paper whose own text says lipids "data not shown", while Saez 2010 states the opposite sign citing another paper. Changes: closes queue entry FT-019; withdraws the queue's brain-cholesterol/myelin rationale for this paper; adds a caution that secondary descriptions of the null mouse's cholesterol disagree. Selection question 2: no dosage test. Commit candidate section 5 of `CC-20261019-SCIENTIST-A-LIPID-01`.
