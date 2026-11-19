# ADV-070 pre-registration, frozen before any stage-adjusted value or late-set score is computed for these seeds (SCI, 2026-11-19; hypothesis level; held data only; no dose, no recommendation; not medical advice)

Question (ADV-070, SCI prospect accepted at the 2026-11-19 meeting). IT13 P3a scored the channel, receptor, transporter and activity-regulated seeds in the held P17 Wwox-deletion deposits (GSE158681 hippocampus, GSE158682 cortex) without a maturation covariate. ADV-068 showed a late-maturing neuronal set falling with the PV set. Which seeds still carry a shift after the late-set score is taken into account, and which become descriptive?

## What I already know (declared; the retrospective elements)
* **Retrospective:** IT13 P3a's raw per-gene log2 ratios (I read the README summary and the Kv7 rows of `genes_individual.tsv`: for example Pvalb, Kcnj9 down, Npy up, Grin2c and Grm3 down in 4 of 4, Cacna1g and Cacna1h not raised, Slc12a5 mixed, Slc12a2 down, Kcnq2 and Hcn2, Gria1, Grin2b background-confounded), and ADV-068's per-animal late-set scores in the cortex contrast.
* **Prospective:** every stage-adjusted statistic below. I have computed none of them for these seeds.

## Data, unit, contrasts (the same as P3a and ADV-068)
Held files only, sha256 identical to IT13's pins and ADV-068's: the two TPM tables and the Ensembl release-92 cDNA (transcript to gene symbol; TPM summed over transcripts of a symbol, as in ADV-068). **Unit: one GEO sample treated as one animal (assumed, not stated by GEO).** Contrasts (case arm against control arm): H_S (3 v 2), H_N (2 v 2), H_null (2 v 3), C_S (3 v 4); background contrasts, control against control, CC_SW, CC_NW, CC_SN (no deletion). **One laboratory, one cohort family** (not independent of the held single-nucleus data).

## The covariate (the ADV-068 set, unchanged)
Stage score of an animal = mean over the LATE_NONPV genes (Grin2a, Slc12a5, Nrgn, Camk2a, Scn8a) of [log2(TPM+1) minus the control-arm mean of that gene] **minus** the same mean over the REF_STABLE genes (Snap25, Rbfox3, Syt1, Stmn2, Tubb3, Map2). Two stated differences from ADV-068's per-animal arithmetic: the baseline for every animal, control animals included, is the mean over all control animals of its contrast (ADV-068 used leave-one-out for control animals); and **a seed that is a member of LATE_NONPV or REF_STABLE is removed from the score when that seed is analysed (leave-self-out)**, so no seed is adjusted by itself.

## Seeds (fixed now)
* **Channel, receptor and transporter seeds** (the P3a individual list): Slc12a2 Slc12a5 Kcnq2 Kcnq3 Kcnj3 Kcnj6 Kcnj9 Kcnj10 Hcn1 Hcn2 Cacna1g Cacna1h Scn1a Scn2a Scn8a Gabra1 Gabra2 Gabrb2 Gabrb3 Gabrg2 Grin1 Grin2a Grin2b Grin2c Grin2d Gria1 Gria2 Panx1 Atp1a3 Kcna2 Grm3.
* **Reference interneuron genes** (for comparison, not seeds of an arm): Pvalb Sst Npy Vip Gad1 Gad2; **deletion check:** Wwox.
* **Activity seed:** the IEG panel (Fos Fosb Npas4 Arc Egr1 Egr2 Egr4 Junb Nr4a1 Bdnf Btg2 Dusp1), analysed as one set; and the P3a PV panel (Pvalb Kcnc1 Kcnc2 Lhx6) as a positive reference for the method.
Genes absent from the table or below mean TPM 1 in both arms of a contrast are reported as not measurable in that contrast and not imputed.

## Statistic
Per animal and seed: y = log2(TPM + 0.5) (as in P3a); for a set, the mean of its genes' y. Per contrast, over all animals of both arms: ordinary least squares y = a + b x + c KO, with x the stage score and KO the arm indicator (1 for the case arm). Raw shift Delta = mean y in the case arm minus mean y in the control arm. The genotype term c is the shift not carried by the score. **Collinearity is built in** (the score is itself lower in the case arm), so c is unstable at these n; every c is therefore accompanied by its leave-one-animal-out range. The raw Delta is checked against P3a's per-gene log2 ratio only for sign (P3a used a ratio of arm means; this uses per-animal means).

## Labelling rule (before any value)
* **A contrast qualifies for a rule label only with at least three animals per arm: of the four deletion contrasts, only C_S (3 v 4).** All other contrasts are descriptive (the rule ADV-068 used: fewer than three per arm). **Flag to ADV:** the assignment text says "three or fewer animals per arm"; read literally, that makes every contrast descriptive and nothing could stand. I apply the ADV-068 rule (fewer than three) as the primary labelling and report the literal reading as a second column, where every seed is descriptive; ADV may overrule.
* In C_S, for a seed or set with |Delta| at least 0.5 log2: **STANDS** if c has the sign of Delta, |c| is at least 0.3 and at least half of |Delta|, and c keeps its sign in all leave-one-animal-out fits; **EXPLAINED_BY_STAGE** if |c| is below half of |Delta| or below 0.3 or has the opposite sign; **UNSTABLE** if c changes sign under leave-one-animal-out. With |Delta| below 0.5: **NO_SHIFT** (nothing to explain).
* **Background flag (from P3a, read not recomputed):** a seed is BACKGROUND_CONFOUNDED if any control-against-control contrast has |log2 ratio| above 0.25 in P3a's table; it can stand only with the flag shown beside it.
* All other contrasts, and C_S rows that fail the rules above: the same arithmetic as description, and the number of the four deletion contrasts in which Delta and c share a sign.
* **Positive reference:** the PV panel is expected to be at least partly explained by stage (ADV-068); if it stands in full after the adjustment, I will say the covariate adjusts weakly at this n.

## What this step cannot show
Whether a shift is a cause or a consequence; protein, current or cell number; that a seed explained by stage is a "rider" (it only says the shift is not separable from the late-set score at this n); independence from the held single-nucleus data; anything about people; any tier change (IT maps arms; I change none).

## Decision it changes (stated before the run)
Which P3a channel, receptor and activity seeds can still be quoted as carrying a shift beyond stage in the held deposits, and whether any arm cell or the Kv7 opener probe needs an annotation (a seed that is background-confounded, explained by stage or descriptive only). Reasoned stop: seeds that are descriptive or explained by stage are labelled so and not pursued.
