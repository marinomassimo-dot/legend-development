# IT28 P10 pilot: do human-derived seed directions replicate in the P47T partial-loss mouse?

Non-canonical research material, not medical advice. Declared in `PRE_DECLARATION.md` before computing; code `pilot_it28.py`, result `pilot_result.json`, per-seed table `pilot_seeds.tsv`.

| Item | Value |
|---|---|
| Seed genes with a defined direction (Q2, Q3, Q8), found in the mouse contrast | 7 |
| Concordant in PFC, parietal cortex and hippocampus (same sign, |log2FC| >= 0.15 in all three) | 3 (HK2, LDHA, SLC2A1; all Q2, all "up") |
| Not concordant | 4 (BNIP3, LDHB, PSAT1, NFE2L2): mixed or flat, none discordant in all three regions |
| Expression-matched decoys with a random direction: expected concordant of 7 | 0.60 |
| One-sided probability of 3 or more among decoys (100,000 draws) | 0.016 |

**Reading.** The three concordant genes belong to one glycolysis module chosen in IT7 for being the readout (the IT7_READOUT6 guard), and they are co-regulated, so the effective number of independent units is nearer 1 than 3: the 0.016 overstates the evidence. Regions are repeated measures of the same ten animals. The result says the glycolysis-direction seen in human systems is not contradicted in a different perturbation (partial loss, protein present); it says nothing about the engine's ranking of candidates, nothing about benefit and is not a calibrated probability. The four non-concordant seeds are flat or mixed, which is "no call at this power", not a contradiction. Comparison cannot be made for the 22 seeds with uncertain or unchanged direction (no sign to score).
**Dependence.** The mouse contrast was used in IT27 to annotate these seeds (informational, no order effect); no seed was built from it. Seeds come from human neural systems and fibroblast/MEF data.
**Not possible now.** A prospective test of candidate ranking needs held-out intervention data in a WWOX-deficient neural system (none exists in the sources read); a protein-level replication needs protein-level seeds (none). Measure that would reopen it: ATF4/eIF2-alpha-P or HIF1A protein in a WWOX-deficient neural system, which is also the INV-02 next test.

**Scope (IT29 rewording, no number changed).** This is an exploratory concordance analysis between two systems (human neural deposits and the P47T partial-loss mouse): it asks whether the *direction of expression seeds* repeats. It is not a validation of responses to any compound, not a test of the ranking, and not evidence of benefit. A protein-level measurement of ATF4 or eIF2-alpha-P can settle a biological premise (the sign of the integrated stress response in a WWOX-deficient cell); by itself it would not validate the pharmacological ranking, which also depends on the compound's action, exposure and attribution.
