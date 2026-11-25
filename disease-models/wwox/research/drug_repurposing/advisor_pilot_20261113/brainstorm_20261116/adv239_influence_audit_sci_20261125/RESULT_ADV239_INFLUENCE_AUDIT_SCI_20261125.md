# ADV-239 result: influence audit of carried small-n transcript inferences (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Held data only: no download, no spend, no external request, no delegate. Checkpoint AD, RP-045 and the sealed ADV-174 / ADV-175 material were not touched. Pre-registration: `PREREG_ADV239_SCI_20261125.md` (committed before any per-unit value). Full table: `out/ranked_inferences_adv239.tsv`.

## 1. Answer

1. **35 carried inferences.** 13 have at least 3 units on both sides of some contrast and could be tested; 6 of those 13 survive every single removal, 7 have at least one part that rests on one unit.
2. **The inferences the repository leans on most cannot be tested.** None of the 12 most consumed rows has a testable contrast: they come from the organoid (4 knockout against **2** wild-type libraries), the CAGE set (1 per arm), one pooled snRNA library per genotype, a qRT-PCR set without per-animal values, or a presence statement.
3. **P47T animal M6 alone** is enough, in cortex, to reverse the TNFA enrichment score (+1.47 to -0.71) and to remove more than half of the cortical set-mean rise for HYPOXIA, GLYCOLYSIS, APOPTOSIS, TNFA and INFLAMMATORY. Post hoc, M6 is also the most influential cortical animal on 41% of random 100-gene sets (chance 10%), 31% in prefrontal cortex: it is an influential library, not a pathway-specific signal.
4. **ADV-233's "carried by two animals" depends on the threshold for IL6/JAK/STAT3 and HYPOXIA.** Without M6 and F8 they lose q < 0.05 in some or all regions (as reported) but keep a positive score in all three forebrain regions (IL6 1.21 to 1.38; HYPOXIA 1.09 to 1.55; 67% to 82% of the full score). IT12 declared that it reads its re-run by direction and size, not q. TNFA is different: its score reverses in cortex and falls to 0.82 elsewhere. **IT should see this before candidate CC-20261125-ORCHESTRATOR-ADV238-P47T-TWO-ANIMALS-01 is propagated.**
5. **Cerebellum holds.** Cholesterol, fatty acid, mTORC1 and reactive-oxygen calls survive all 7 single removals (4 v 3).

## 2. Units behind each deposit

| Deposit | Units (ids in the table) | Leave-out run before this audit |
|---|---|---|
| GSE215425 P47T forebrain | WT M3 M2 M1 F5 F4; P47T M7 M6 F9 F8 F10 | leave-one (own sets, IT12; one dossier fit, ganaxolone P47T); leave-two M6+F8 (ADV-233) |
| GSE215425 cerebellum | WT M3 M2 F5 F4; P47T M6 F8 F10 | per-animal only (ADV-233) |
| GSE158682 P17 cortex | CRTX_S_Ctrl_1-4; CRTX_S_KO_1-3 | one-library omission in the memantine dossiers; ADV-068 control leave-out |
| GSE158681 P17 hippocampus | arms of 2 or 3 per Cre line | NMDA-stress signature (memantine) |
| GSE156243 organoid | cwt1 cwt2; cko1-4 | Wnt (2026-10-25); NMDA-stress signature (memantine) |
| GSE126075 CAGE | one library per arm | none possible |
| GSE158684 snRNA | one pool per genotype | none possible |
| Hussain 2019 (PMID 30290271) | neurospheres 2 KO v 3 WT; hippocampi 4 v 4 | no per-animal values held |

The brief's "Aldaz / Kv7 sets" are the Hussain 2019 set carried by matching triggers T19 and T20. Its RNA-seq is on neurospheres, not hippocampus; Kcna2 is Kv1.2, not Kv7. The August dossier (`fulltext_dossiers/PMID30290271.md`) already states the neurosphere arms of 2 and 3; only the trigger wording lost it. Its two supplement tables were read then; their bytes are absent from this checkout and were not reopened here.

## 3. Top of the ranking (number of consumers)

| Rank | Inference | Consumers | Disposition |
|---|---|---|---|
| 1 | organoid: glycolytic / hypoxia-response transcripts higher | K01, E02, I01, INV-16, CLAIM 002 | not testable |
| 2 | organoid: Wnt output higher | D01, D02, M01, RP-008, CLAIM 002 | not testable |
| 3 | CAGE: ISR, PDK1, HIF, ERBB4, adhesion readings | INV-02, I01, RP-038, RP-033, CLAIM 014 | not testable |
| 4 | organoid: receptor / transporter transcripts present, oligodendrocyte transcripts barely detectable | F01 to F04 | presence, not a contrast |
| 5 | Hussain: Il6 higher | CLAIM 005, L01, J01, INV-14 | not testable |
| 6 | snRNA: PV / ERBB4 / receptor readings | INV-15, RP-019, RP-038, RP-017 | not testable |

"Not testable" is not "wrong": in several organoid rows all four knockout libraries lie on one side of both controls. It means single-library influence on the control side cannot be measured.

## 4. What changes (proposed wording; nothing was edited outside this folder)

For IT (cards, triggers, investigations; claim text only through a candidate):

| Where | Proposed wording |
|---|---|
| K01 (forebrain hallmarks) | "Hippocampus and prefrontal cortex keep sign and at least half the set-mean rise without any one animal; the cortical set-mean rise rests more than half on animal M6; in the repository re-run cortical APOPTOSIS does not reach q 0.05. The six-gene glycolytic-enzyme shift in cortex still holds without M6." |
| J01 and CC-ADV238 (TNFA, IL6) | "TNFA/NF-kB rests more than half on animal M6 (cortex reverses without it). IL6/JAK/STAT3 loses the q threshold without M6 and F8 but keeps its sign and about three quarters of its enrichment score." |
| L01 (NRF2 targets) | "Srxn1 is higher in all four regions; the cortical rise of Hmox1 and of the five-gene set rests more than half on M6." |
| F02 | "Oligodendrocyte-lineage markers (SOX10, MOG, OLIG1) are below 1 CPM; PLP1 is 48 to 198 CPM (isoforms not resolved)." |
| F03 | "The cortical NKCC1:KCC2 ratio is not informative: a +0.24 rise falls to 0.085 without one control library." |
| INV-06 | "The cortical sign of CTGF changes when one library is removed." |
| INV-16 | add "forebrain only; cerebellum goes the other way for Slc2a1". |
| INV-15 | "2 control against 3 knockout animals in hippocampus; cortex (4 v 3) shows a smaller fall with overlapping animals." |
| Trigger T19 | "Grin2c and Grm3 transcripts down (qRT-PCR, 4 v 4 whole hippocampus; discovery RNA-seq on neurospheres 2 v 3)": three named genes in all (Kcna2 is T20), not receptor and channel families. |
| CLAIM 005 (GAD2) | "higher on average; libraries overlap." |

For ADV (portfolio):

| Row | Proposed wording |
|---|---|
| RP-036 | "Cholesterol set not enriched in cortex and prefrontal cortex; hippocampus depends on single animals (it reaches q < 0.05 without F5 or without F9). Only the cholesterol set is cerebellum-restricted: mTORC1 meets the threshold in all four regions, fatty acid in hippocampus and cerebellum." |
| RP-038 | "No clear Erbb4 change (absolute log2 up to 0.21; single-animal removals -0.28 to +0.24)", not "no deficit". |

## 5. Predictions

| | Prediction | Outcome |
|---|---|---|
| P1 | at least two thirds of testable inferences are robust | **Not met**: 6 of 13 (T2, T4, M1 cortex, M2, M5, M7). Counted per inference; one weak part is enough to lose "robust". |
| P2 | at least one carried inference outside the P47T hallmarks is one-animal-driven | Met: NKCC1:KCC2 cortex, CTGF cortex sign |
| P3 | no organoid inference testable | Met by design |
| P4 | the top-ranked inference is organoid, "not testable" | Met |
| P5 | the T19 set is not testable | Met |

## 6. Secondary tier (non-WWOX comparators): listed, influence not computed

| Deposit | Used by | Units as the repository states them |
|---|---|---|
| GSE221080 | RP-017 | 3 v 3; a leave-one-sample sensitivity was planned in `ganaxolone_20261123/specificity_prediction.md` (whether run: not checked) |
| GSE292221 | RP-012, RP-039 | 4 per group per age; matrix not downloaded |
| GSE271421 | RP-018 | 4 animals per condition (endogenous cohort) |
| GSE268132 | RP-018 | MEF polysome RNA-seq; units not compiled |
| GSE327470 | RP-043 | units not compiled |
| GSE274921 | RP-033 | units not compiled |
| GSE165371 | RP-036 | reference atlas, not held |
| E-MTAB-14792 | many | not accessible; no value carried from it |

## 7. Limits and deviations

* **Robust means only that no single unit carries the effect.** It is not significance, replication, cell resolution or cause. Several robust sets are small effects (0.1 to 0.2 log2).
* **Two measures disagree in places.** The pre-registered measure is the set mean; the pre-ranked enrichment score (IT12 re-implementation, gene-label permutation, anti-conservative) is less sensitive to M6 for cortical GLYCOLYSIS and HYPOXIA. Both are in `out/`. The q threshold is applied as a criterion only where the carrying text declares it (RP-036); elsewhere q crossings are reported in `out/gsea_loo_adv239.tsv` (several cortex and prefrontal calls sit near 0.05 and are lost under many different removals).
* Only the pair M6+F8 was tried as a pair. No other pair was searched.
* The consumer count is hand-read; consumers were taken from the portfolio, investigations, cards, claims, working-model lines and triggers, not from renderings or earlier result notes. A consumer that uses a deposit without naming it or its genes can be missed.
* Not recomputed: the GSK-3 / Wnt set-versus-random comparison (M3), the stage correlation (O12).
* Secondary tier: the pre-registration promised animals and leave-out history; only the row above was compiled.
* Deviation: the first script run applied the "not testable for absence" rule to every item; it was corrected to the carried "no change" statements before any disposition was written. Numbers did not change.
* Post hoc, not pre-registered: the random-set influence check, and the reading of ADV-233 by direction and size.
* Hits on prior reading: the ADV-233 conclusions were known before the pre-registration, so the M6 findings are not blind.

## 8. Reproduction

`influence_adv239.py` (per-unit values and removals), `gsea_loo_collect_adv239.py` (eleven runs of `p47t_it12_20261031/p47t_reanalysis_it12.py`; the full run is byte-identical to the committed IT12 result), `random_set_influence_adv239.py`, `build_ranked_table_adv239.py`. Each prints its usage when run without arguments. Raw data are under the root checkout `files/`; the hallmark file has sha256 prefix `1d4c72ee`.

## 9. DREAM

Lesson: an influence statement needs its scale. "Carried by two animals" was true under one threshold and not under the repository's other reading of the same run. Association not yet used: M6 and F8 were flagged in 2026-10 for activity-gene outliers; any further P47T cortex reading should be shown with and without M6 at the time it is made, not audited afterwards.
