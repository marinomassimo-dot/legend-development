# ADV-231 result: is there a STAT3-axis transcript echo in the held Wwox-deficient brain tables? (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Pre-registration `PREREG_ADV231_SCI_20261125.md` (digest and time in the companion files, 00:31Z; committed before any analysis; frozen after the one Socs3 row ADV named had been read). Mandate step OBJ_ACCEPTED[102]. Held tables only, no download, no contact, no spend. No receipt (no source was read, only held tables). Checkpoint AC, RP-045 and ADV-174/175 untouched. Answers ADV228-Q01.

## 1. Answer first

**Frozen disposition: 4, NOT RESOLVABLE.** Only 3 of the 6 target genes are measurable in the P17 tables (Socs1, Il6 and Bcl3 are below 1 TPM in both), no target has a verdict of HIGHER or LOWER, and the noise floor is not empty. **No rising echo of STAT3 targets in the held P17 hippocampus or cortex, and none in the P47T adult tables by the frozen rule.** Two things the frozen rule does not capture are reported below and labelled as such.

| Gene (reason on the list) | P17 verdict | Calls (H_S, H_N, H_null, C_S) | P47T verdict (4 regions) |
|---|---|---|---|
| Socs3 (direct target, feedback) | NOT RESOLVED | not measurable x3 (hippocampus below 1 TPM), **LOWER** in cortex | NOT RESOLVED |
| Socs1, Il6, Bcl3 | NOT MEASURABLE | below 1 TPM in P17 (Il6 in P47T too); Socs1 and Bcl3 measurable in P47T | NOT RESOLVED |
| Osmr, Pim1 | NOT RESOLVED | not separated | NOT RESOLVED |
| Stat3 (axis member, self-induced target; not in the disposition rule) | **HIGHER** (hippocampus S and N, not null, not cortex) | HIGHER, HIGHER, not resolved, not resolved | NOT RESOLVED |
| Jak2, Il6st (axis members) | NOT RESOLVED | none called in a knockout contrast | NOT RESOLVED |

## 2. What the repository already answered (duplicate check, first step)
* The cortex row ADV named (IT24 P4, contrast C_S, Socs3 1.08 against 5.68 TPM, centred log2 -1.77) **reproduces here as LOWER** with the same loader and rule (KO animals 1.06, 0.86, 1.31; controls 12.29, 2.26, 1.74, 6.45). Read per animal: the "separation" is real but the controls spread 7-fold (1.74 to 12.29) and every value is near the 1 TPM floor; Socs3 is **not measurable in any hippocampal contrast** (group means 0.4 to 2.3 TPM; one S_KO animal is at 5.97 against 0.55 and 0.47 for the other two). So the row is a low-expression, small-n descriptive fall, not an echo and not a test of the axis.
* The IT6 README line 104 SOCS3 value (5.7 against 14.2 CPM, lowered) is **the human organoid panel (GSE156243)**, not brain; line 54 (P47T "IL6-JAK-STAT3 set positive in PFC, CTX, HPC") is an enrichment inference with no gene value carried. This run tests it at the gene and animal level (section 4).
* No per-animal, fixed-list, control-versus-control analysis existed; that is what is added.

## 3. Predictions (frozen)
* **P1 held:** Socs3 LOWER in C_S, never HIGHER.
* **P2 MISSED:** I predicted disposition 2 or 3; the rule gave 4 (too few measurable targets). The expected weak sign was there for Socs3 (cortex), but the rule's own requirement of a hippocampal call plus a cortex call cannot be met when Socs3 is unmeasurable in the hippocampus.
* **P3 held:** Il6 not measurable (below 1 TPM in P17; below 10 counts in P47T too).
* **P4 held:** no target HIGHER in two or more P47T regions; Stat3 not resolved (PFC: separated at Rc 0.27, below the 0.3 threshold).
* **P5 held:** the noise floor is not empty: Jak2 is LOWER in both S_Ctrl against WT and N_Ctrl against WT (4.28 and 3.93 against 5.93 TPM, separated), Il6st HIGHER in S_Ctrl against WT, Wwox LOWER in S_Ctrl against WT. Controls from the two deletion lines differ from WT in genes of this axis without any knockout.

## 4. Two findings outside the frozen rule (labelled post hoc)
**(a) Stat3 itself is higher in the S and N hippocampal knockouts (frozen table, not in the disposition rule).** H_S: KO 48.6, 75.9, 114.1 against controls 34.5, 38.7 TPM (Rc +1.49, 2.2-fold); H_N: 68.3, 54.2 against 41.3, 35.9 (Rc +0.91, 1.6-fold). Not in the full null (27.3, 25.1 against 31.9, 35.3, 32.2; Rc -0.12) and not in the S-deletion cortex (Rc -0.06). Stat3 is also an abundant transcript expressed in several cell classes, no control-contrast call exists for it, and neither contrast has more than three animals per arm. The S and N lines agree with each other and disagree with the full null; I read this as unresolved, not as an echo.
**(b) The P47T "positive" pathway inference rests on two animals, post hoc and reported beside the frozen result (`p47t_animal_scores_posthoc_adv231.tsv`, script `p47t_animal_posthoc_adv231.py`).** Per animal, the mean log2 of eight axis genes (Stat3, Jak2, Il6st, Socs3, Socs1, Osmr, Bcl3, Pim1) against the region's WT mean: P47T animals M6 and F8 score high in every forebrain region (PFC +1.14 and +0.89, HPC +2.13 and +0.56, CTX +1.37 and +0.97), while the other three P47T animals (M7, F9, F10) lie between -0.39 and +0.34, inside or near the WT range (-0.79 to +0.49). In the cerebellum the same animals do not stand out (M6 -0.39, F8 +0.07). The signal is **a per-animal state shared across three regions of two animals** (one male, one female), not a genotype-wide shift of five. The deposit lists age as "150 to 280 days" with no per-animal age, litter or seizure observation, so the cause (an inflammatory or seizure state, age, handling) cannot be settled from the table. I did not re-run the IT6 enrichment, so I can only say its "positive in three regions" is what two high animals would produce, not that it was produced that way.

## 5. Disposition against the frozen options
Disposition 4. The measured part of the question has an answer: **no target of the axis is raised in P17 Wwox-deficient hippocampus or cortex (where measurable), and the only target with a called direction (Socs3, cortex) goes down**. The unmeasured part (Socs1, Il6, Bcl3 and Socs3 in the hippocampus are below the table's floor) cannot be settled from bulk TPM at 2 to 3 animals per arm.

## 6. DL-MECH-014 (JAK2/STAT3 axis, cancer-line origin) in neural tissue
Neither gains nor loses much. **No gain:** no neural transcript target rises, the one called target falls, and the P47T pathway positivity is an animal-state pattern of two of five. **No loss either:** the axis is a phosphorylation mechanism (WWOX restrains JAK2 and STAT3 phosphorylation in the 2018 cancer-line work), and a bulk mRNA of low-abundance targets at P17 in 2 to 3 animals per arm would not show a loss of restraint if it existed. The echo question is closed as "not seen where measurable"; the lead stays in the ledger at its cancer-line origin.

## 7. What would still be needed (Q02, no held source)
Phospho-STAT3 (Y705), total STAT3, phospho-JAK2 and the same loading control per animal in Wwox-null, hypomorph and P47T brain, with the animal's seizure observation, age and litter, at P17 (and in the adult P47T animals if the two high animals are to be explained). Cell-resolved measurement is the second need: the one held cell-resolved deposit (GSE158684) is one pool per arm. **A cheap held-data step exists:** reading the P47T paper's text and supplement for seizure or health notes on animals M6 and F8 (the P47T deposit's paper is PMID 36828035, already in the repository; I did not open it in this run).

## 8. Limits
Bulk RNA; 2 to 3 animals per arm in P17 (4 in the S-deletion cortex control); one GEO sample = one animal assumed, not verified; the P47T table carries normalised counts on an unstated scale (I used a threshold of 10 counts and the same ratio rule, not the TPM floor); the P17 lines differ (deletion lines S and N, a full null; the controls are not interchangeable, as the noise floor shows); cell composition not separated; the post hoc per-animal score is mine, not blind-checked, and its eight-gene list is the frozen nine minus Il6 (unmeasurable) plus none.

## 9. What surprised me
That the strongest per-animal structure in these tables is not a genotype effect at all: two of five P47T animals carry the whole forebrain signal, in two sexes and in three regions at once, so a genotype-level "pathway positive" inference that had been carried for weeks may be a two-animal state.

## 10. DREAM line
Changed: the IT6 P47T pathway-positive entry should carry "two of five animals" (proposed note for IT, not applied); the Socs3 cortex fall is low-expression and control-spread. Consumer: IT (batch route for the carried entry; the ADV228-Q01 row can close as CONCLUDED with this folder), ADV (Q02 stays the open measurement; a possible next step is reading PMID 36828035 for the two animals).

## 11. Files
`PREREG_ADV231_SCI_20261125.md` (+ digest, time) · `stat3_echo_adv231.py` · `stat3_echo_animals_adv231.tsv` (per animal, every contrast and gene) · `stat3_echo_verdicts_adv231.tsv` · `p47t_animal_posthoc_adv231.py` · `p47t_animal_scores_posthoc_adv231.tsv`.
