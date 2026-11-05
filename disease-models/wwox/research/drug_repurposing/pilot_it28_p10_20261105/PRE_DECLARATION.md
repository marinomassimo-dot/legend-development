# IT28 P10 pilot, declared before any statistic was computed (2026-11-05)

Non-canonical research material, not medical advice. A verification of function and a plausibility check, NOT a validation and NOT a probability of benefit.

**Question.** Do the directions that the generator's seed rows carry (taken from human neural systems and fibroblast/MEF data, not from the mouse) show up with the same sign in the partial-loss P47T mouse (PFC, parietal cortex, hippocampus), more often than expression-matched decoy genes given a random direction?
**Input.** The seed rows with `direction in (up, down)`, `direction_status = defined`, kind gene, in `generation_it22_p1_20261103/inputs_it22/seeds_p1/Q{2,3,8}_expression_tiersAB.tsv`; mouse contrast: `verification_it27_p1_20261104/results/p1a_all_regions_own_results.tsv.gz` (DESeq2 `~ sex + genotype`, 5 v 5).
**Unit.** The gene (a seed is one gene; regions are repeated measures of the same ten animals, so a gene counts once). Seeds that share one origin count once per gene.
**Statistic.** A gene is CONCORDANT when its log2FC has the seed's sign with |log2FC| >= 0.15 in all three regions. Observed = number of CONCORDANT seed genes.
**Reference.** Decoys: genes tested in all three regions, matched to each seed gene by decile of mean baseMean; each decoy gets a random direction (up or down, 50/50) for the same test. Null = the number of concordant genes among n decoys, 100,000 draws; the one-sided p is P(null >= observed). A second reference, 'no change' (a prediction of zero), cannot be scored by sign and is not used.
**Dependence stated.** The mouse contrast was already used (IT27) to annotate these same seeds; no seed was built from it. Seeds come from other systems. The test checks cross-system replication of direction in a different perturbation (partial loss), not accuracy of the engine's candidate ranking.
**What the result cannot say.** Concordance is not benefit, not mechanism and not a calibrated probability; with n this small a null result is "no call at this power".
**Reopen.** More seed genes with a defined direction, or protein-level seeds.
