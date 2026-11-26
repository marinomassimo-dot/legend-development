# COMMIT CANDIDATE — CC-20261126-ORCHESTRATOR-ADV292-LEDGER-PAPER-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-292 consumers) · **Date:** 2026-11-26 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin:** SCI's ADV-292 (`drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv292_next_held_partials_sci_20261126/`, proposed sentences A3, B5, B6). **Checks:** two blind rounds by `legend-delegate` (sonnet, effort high stated in each dispatch), records in `adv292_consumers_it_20261126/`.
**Status:** PROPOSED, for the next `BATCH_COMMIT`.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** Two dated wording corrections in `DL-MECH-170` (discovery ledger) and one in `PAPER 219` (paper registry). No status, grade or flag changes.

## 2 · Proposed wording (old = verbatim record text)

**DL-MECH-170 / 1** *Old:* «an APP/PS1 line (PMID 31781019) shows same-direction effects in both genotypes for the spike classes present in both;»

*New:* «an APP/PS1 line (PMID 31781019; 8 male APP/PS1 and 6 wild-type littermate mice, 5 to 6 months, ethosuximide 200 mg/kg intraperitoneal, within-animal crossover, three-hour recordings; per-mouse Supplemental Table 1 recomputed 2026-11-26) changed cortico-hippocampal spikes (down), fast-spindle spikes (down) and spindle-associated spikes (up) in the same direction in both genotypes by group means; simple cortical spikes had opposite signs by group means once the one wild-type outlier the authors remove from the cortical analysis is excluded (wild type up, APP/PS1 down; neither significant; with the outlier kept the wild-type sign is down); muscle-twitch spikes and spike-wave discharges showed no significant effect in either genotype; significance differs by genotype (wild type: spindle-associated and fast-spindle; APP/PS1: cortico-hippocampal and fast-spindle; these are omnibus tests across saline, ethosuximide and levetiracetam, and ethosuximide-specific post hoc tests are shown only for both genotypes pooled); and no genotype-by-drug test exists (the authors write that the wild-type response 'seemed to follow' the APP/PS1 pattern and that they could not apply a two-way ANOVA);»

**DL-MECH-170 / 2** *Old:* «which carries a wild-type arm with no effect and a direct test that loss of the worm T-type channel does not remove the benefit)»

*New:* «in which ethosuximide extended the lifespan of the dnj-14 mutant by 26.29 percent on control RNAi and by 5.60 percent, not significant, on daf-16 RNAi (separate log-rank comparisons against their own controls, no interaction test, and daf-16 RNAi shortened baseline lifespan); wild-type N2 lifespan was unchanged at 1, 2 and 4 mg/ml without RNAi (Table S1, n 52 to 54; N2 on hsp-1 RNAi did extend, +17.72 percent) and wild-type thrashing was tested at 1 mg/ml only (Fig S1C); in the separate Tau V337M model loss of the worm T-type channel cca-1 did not remove the thrashing or lifespan benefit (+29.26 percent against +26.62 percent, Table S1; the main text prints 25 and 16 percent for a cohort whose control lifespans differ from Table S1); Table S1 also shows +18.85 percent (P = 0.0038) for dnj-14 at 4 mg/ml where the text says no significant increase)»

**PAPER 219 / 1** *Old:* «Both consequences are **predicted by rule** (`PVS1, PM2, PM3, PP3`) with **no RNA and no protein assay**.»

*New:* «Both consequences are **predicted by rule** (`c.517-1G>A`: `PVS1, PM2, PM3, PP3`; exon-5 deletion: `PVS1, PM2, PM3`, PP3 is on the SNV only) with **no RNA and no protein assay** (the Supplementary Data column headed 'RNA' holds the coding-DNA change `c.517-1G>A`, not an RNA result; checked 2026-11-26).»

## 3 · Checks and what was changed by them
Kam 2019 sentence: SUPPORTED with ADD; the blind reader recomputed the group means from the per-mouse table and found that sex is stated only for the APP/PS1 group ('6 wild-type male mice' removed) and that the per-genotype p values are omnibus tests that include a levetiracetam arm (added). Chen 2015: ADD (separate log-rank comparisons, no RNAi in the wild-type arm, thrashing at one dose, Table S1 against text); the added clauses are the reader's, not re-checked. PAPER 219: SUPPORTED. SCI's item (ii) (carry the CLAIM 033 'exonic or near-exon' wording into the Transferability line) was not blind-checked and is not proposed here.

## BATCH DISPOSITION — `BATCH_20261126_002` (2026-11-26, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED as section 2 states (one ledger record with two replacements; one paper-registry record with one). MINOR.
