# ADV-233 result: do two P47T animals carry the carried P47T signatures? (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Pre-registration `PREREG_ADV233_SCI_20261125.md` (digest and time in the companion files, 00:52Z, committed before any per-animal hallmark score or leave-two-out run). Mandate step OBJ_ACCEPTED[103]. Held counts (GSE215425), held primary, MSigDB 2023.2.Mm `mh.gmt` identical to IT12's (sha256 1d4c72ee...). No download, no contact, no spend. Checkpoint AC, RP-045, ADV-174/175 untouched. PMIDs appear in this research file only.

## 0. First, two corrections to my own ADV-231
1. **The two-animal observation was not new.** IT12 (`p47t_it12_20261031`, 2026-10-31) already identified M6 and F8 (Nptx2 and Bdnf 20 to 30 fold above wild type in the three forebrain regions) and called the designation post hoc. My ADV-231 duplicate check searched gene names, not animal identifiers, and ADV-233's duplicate check inherited the gap.
2. **The P47T table is integer counts, not "normalised counts".** The frozen ADV-231 calls median-centre each contrast and are not affected; the post hoc per-animal score there used no library-size normalisation. This run re-does per-animal scores with IT12's TMM normalisation; the two-animal pattern persists.

## 1. Answer first

| Carried inference | All animals (threshold: positive NES, BH q < 0.05) | Without M6 and F8 | M6 and F8 ranks 1 and 2 | Disposition |
|---|---|---|---|---|
| TNF / NF-kB / IL1B / RELA (IT6 row 5; proxy: TNFA_VIA_NFKB set) | met HPC, CTX, PFC | met **nowhere** (CTX even turns negative, NES -1.48) | all three regions | **carried by two animals** |
| IL6-JAK-STAT3 set positive (IT6 row 5) | met HPC, CTX (q 0.0499), PFC | met **nowhere** | CTX, PFC | **carried by two animals** |
| HYPOXIA hallmark (K01 anchor) | met in all three | met HPC only | all three | **carried by two animals** |
| GLYCOLYSIS hallmark (K01) | met in all three | met in all three (NES 1.91, 1.61, 1.54) | CTX, PFC | **robust to leave-two-out** |
| INFLAMMATORY_RESPONSE | met HPC, PFC | met HPC | CTX, PFC | not resolvable (one of two regions lost) |
| mTORC1 (forebrain) | met all three | met HPC | PFC only | not resolvable |
| FATTY_ACID (HPC; only forebrain region met) | met HPC | met HPC (NES 2.22) | no | robust |
| NRF2_5 (L01; IT12 rule, met HPC only) | met HPC | not met (HPC +0.26, p 0.089) | CTX, PFC | not resolvable |
| **RP-036 cerebellum**: cholesterol, fatty acid, mTORC1 | met (NES 1.99, 2.84, 2.02) | not testable (one mutant left) | per animal: all three mutants above every WT | **robust per animal** |

**What this means.** The forebrain inflammatory (TNF, IL6) and HYPOXIA enrichments that the repository carries are **carried by two of five mutants**, the two that also show the activity-gene surge. GLYCOLYSIS is not. The cerebellar lipid readings behind RP-036 are not touched by this (but cannot be leave-two-out tested). **The cause of the two animals' state is unknown** (seizure shortly before euthanasia is one reading; IT12's activity rival; the deposit has no per-animal seizure, age, health or batch record).

## 2. Counter-check: is it library-wide variability?
Share of 1000 random sets (matched on size and expression quintile) in which M6 and F8 are the top two of all 10 animals (chance 1 in 45 = 2.2 percent): HPC 0.9 to 25 percent, CTX 9 to 17 percent, PFC 11 to 39 percent (`random_sets_adv233.tsv`). **In CTX and PFC random sets put these two libraries first about 4 to 18 times more often than chance**, so a large part of their state is a broad shift of the library profile, not a property of one pathway. In HPC the TNFA, IL6 and INFLAMMATORY rankings are specific (random 0.9 to 1.3 percent) while others are not. So the cortical and prefrontal rankings are not pathway-specific evidence, and the leave-two-out result is the stronger test.

## 3. Predictions (frozen)
P1 held (M6 and F8 ranks 1 and 2 for TNFA, IL6 and INFLAMMATORY in at least two regions). P2 held (TNFA and IL6 carried; INFLAMMATORY not). P3 held (GLYCOLYSIS keeps its threshold everywhere; HYPOXIA in HPC). P4 held (cerebellar cholesterol and fatty acid are not M6/F8-carried). P5 held (random sets above 10 percent in CTX and PFC).

## 4. The primary and the deposit metadata (targeted query, receipt `RECEIPT_ADV233_36828035_SCI_20261125.json`)
* No animal identifier (no M6, no F8), no per-animal seizure, health, weight, litter, dissection or batch note; no library batch statement. RNA-seq: "150-280 days of age, n = 5 mice/group (2 males and 3 females)" (deposit sample titles show wild type 3 male 2 female: the Methods sentence and the deposit disagree for wild type, as IT12 noted). GEO series metadata: tissue, region, genotype only.
* The paper's EEG: 3 adult homozygotes with 11 to 22 spontaneous generalised convulsive seizures in 43 to 53 hours: seizures are frequent in this genotype, so a mutant animal euthanised shortly after a seizure is not unusual; whether M6 or F8 were such animals is not recorded.
* Homozygotes die earlier and are euthanised when moribund (survival cohort, not the RNA-seq cohort, as far as the text says).

## 5. Proposed wording (not applied; IT by the ordinary route)
* **IT6 P4 README row 5:** "regulator and pathway inference (TNF, NF-kB, IL1B, RELA; IL6-JAK-STAT3 set) positive in all three regions" -> append: "the TNFA and IL6/JAK/STAT3 hallmark enrichments do not survive removal of the two animals (M6, F8) that also carry the activity-gene surge (leave-two-out, ADV-233); read as a state of two of five mutants, not as a genotype-wide inflammatory signature; the authors' upstream-regulator tool itself was not re-run."
* **RP-036:** append: "per animal all three cerebellar mutants exceed every wild type on cholesterol, fatty acid and mTORC1 set scores (leave-two-out not testable with 3 mutants); forebrain mTORC1 enrichment is lost in CTX and PFC without M6 and F8."
* **K01 (IT12 text):** "GLYCOLYSIS enrichment survives removal of M6 and F8 in all three forebrain regions; HYPOXIA survives only in hippocampus."
* **L01:** "NRF2_5 'up' in HPC falls below the rule without M6 and F8 (+0.26, p 0.089)."
* **IT6 row 6** (cerebellar Il1b, Tnf qPCR, n 6) is a different assay and animals; not tested here.
* **RP-018** (named in the brief): its row text contains no P47T statement that I found, so no wording change is proposed; if ADV had a P47T premise in mind there, please name it.
* The "reactive-pan" list is from the human organoid panel, not P47T; no P47T inference is carried on it (scored descriptively only).

## 6. Deviations and limits
* **Deviation from the PREREG:** the first leave-two-out run removed M6 and F8 from every region and crashed in the cerebellum (one mutant left, no t statistic). The rerun removed them in the forebrain only, leaving CB intact (CB is not testable anyway); the CB lines of the drop run equal the full run up to permutation noise.
* GSEA is IT12's re-implementation (gene-label permutation, anti-conservative with correlated genes): the threshold is the repository's own reading, not a calibrated significance; leaving two of five animals out also lowers power, so a lost threshold is not proof of absence. The leave-two-out set was chosen because the two animals were already flagged (post hoc selection): a different pair would not be expected to give this, but I did not run all pairs.
* The proxy for the authors' TNF/NF-kB/IL1B/RELA inference is a hallmark set, not their tool. Cerebellum: 3 mutants, 4 wild type. mRNA only. The reactive-pan and per-animal scores are not blind-checked.
* My verification of the full run: `gsea_reimpl_it12.tsv` and `sets_it12.tsv` are byte-identical to IT12's committed files.

## 7. What surprised me
The wiring: IT12 had already seen the two animals three weeks earlier and the HIF part of its text says so, yet the inflammatory and hallmark enrichments carried in other places were never re-read with those two removed. Removing them turns the cortical TNFA enrichment from +1.47 into -1.48.

## 8. DREAM line
Changed: the P47T forebrain inflammatory and HYPOXIA inferences rest on two animals; GLYCOLYSIS and the cerebellar lipid readings do not (the latter untestable by leave-two-out). Consumer: IT (wording), ADV (K01/RP-036 direction), and a rule worth carrying: before quoting a bulk-tissue pathway inference, run leave-flagged-animals-out; search a duplicate check by sample identifier, not only by gene.

## 9. Files
`PREREG_ADV233_SCI_20261125.md` (+ digest, time) · `per_animal_scores_adv233.py` · `per_animal_scores_adv233.tsv` · `random_sets_adv233.tsv` · `gsea_drop_M6_F8_forebrain_adv233.tsv` · `sets_drop_M6_F8_forebrain_adv233.tsv` · `disposition_adv233.tsv` · `RECEIPT_ADV233_36828035_SCI_20261125.json`. The full run's tables are IT12's own (`p47t_it12_20261031/results/`).
