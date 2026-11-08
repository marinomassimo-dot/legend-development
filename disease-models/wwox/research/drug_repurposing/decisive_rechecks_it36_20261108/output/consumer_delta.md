# Consumer delta (proposals only; nothing here was changed)

Paths are relative to `disease-models/wwox/research/drug_repurposing/` and are written in plain text, not as links. Evidence row ids refer to `hdac5_hif.tsv` (A, B, C, D) and `ephys_claims.tsv` (E).

## HDAC5 and HIF-1alpha (INV-16)

| Consumer file | Proposed change | Reason |
|---|---|---|
| ranking_it8_p9_20261029/investigations_it20.tsv, INV-16, evidence cell | Add: "HDAC5 and HIF-1alpha: knockdown or inhibition lowers hypoxic HIF-1alpha and GLUT1/CA9 mRNA in human cancer cell lines through a cytosolic, catalytic route (PMID 26061431, full text); association with the inhibitory domain raises transactivation without stabilisation (PMID 19071119, abstract); HDAC5 silencing lowers HIF1A in an epilepsy-model neuron (PMID 34021541); opposite-sign reports exist (PMID 42413489, 36124413, 35704695, abstracts)." Replace any "scaffold only" reading of class IIa by "scaffold and catalytic readings both reported; context-dependent". | A01-A07, B01, C01, D01-D03. |
| same row, branch or test cell | Keep HIF1A and EPAS1 beside SLC2A1; add a HIF1A or EPAS1 knockdown arm for the SLC2A1 readout and the catalytic-dead, wild-type, cytosol-locked and nuclear-locked rescue set as the separating measurement. | A06 (HIF-dependence of GLUT1 not shown in the source). |
| hdac5_inv16_20261107/output/README.md, "Which function stays an explorable lever" and Q2 text | Replace "a non-catalytic route through HIF-1alpha is plausible for a class IIa protein, shown for HDAC7 only" by "HIF-1alpha is a candidate mediator for HDAC5 with both catalytic (cytosolic, Hsp70) and scaffold (inhibitory domain) readings and a sign that differs between systems". The post-audit paragraph already carries the three works; add the three counter reports. | D01-D03 were not in that package. |
| hdac5_inv16_20261107/output/three_questions.tsv, Q2 not_established | Same substitution; add "HDAC5 amount, localisation (nuclear or cytosolic) and phosphorylation are part of the function question". | A04, A07, D03. |
| hdac5_inv16_20261107/output/experiment.tsv, Step 1 and Step 2 | Step 1: add the HIF1A knockdown arm; Step 2: list cytosol-locked and nuclear-locked HDAC5 beside the catalytic pair and state "expression and partner binding shown". | A03, A04. |
| view/work_order.json, WO-30 | No change to the order of steps; add the arm above to the premise measurement. | Same. |

## PV electrophysiology (INV-15)

| Consumer file | Proposed change | Reason |
|---|---|---|
| ranking_it8_p9_20261029/investigations_it20.tsv, INV-15 evidence cell ("pooled events, not animals") | "unit of the KS test not declared; the size of the p values is compatible with events and not with one value per cell". | E06, E07. |
| same cell ("more than halved") | Keep for the mean of the declared sIPSC distribution; add "events from 9 to 14 cells, 5 to 7 animals; no animal-level statistic for current amplitudes". | E08, E15. |
| pv_inv15_20261107/output/README.md, DATO third bullet | "Declared counts do not add up as printed in the legends; cause not determinable" and "p values near 1e-100 are compatible with events and incompatible with one value per cell; the unit is not declared; no contradiction of the paper is asserted". | E01, E02, E07. |
| pv_inv15_20261107/output/currents.tsv, K4 (unit_of_test) | Replace "KS test on events; p values near 1e-100 imply events as units" by "KS test; unit not declared". | E06. |
| same file, K6 and K7 | K6 "unpaired t-test on cells" becomes "t-test; unit not declared (N's printed as cells/animals)"; K7 add "no animal-level statistic for current amplitudes (the sag plot is described as 'for all animals tested')". | E05, E08. |
| pv_inv15_20261107/verify/audit_p.md C11 | Left as audit history; do not quote its "all below the floor" for mEPSC and sEPSC: 10 of 18 are below (6 sIPSC, 2 mEPSC amplitude, 2 sEPSC amplitude). | E07. |

## Ih and HCN (INV-18)

| Consumer file | Proposed change | Reason |
|---|---|---|
| ranking_it8_p9_20261029/investigations_it20.tsv, INV-18 why-it-matters cell | "the heterozygote shows the same intrinsic changes" becomes "several of the same intrinsic changes versus wild type (rebound excepted; heterozygote versus knockout untested)". | E14. |
| same row, evidence cell | "rebound is larger only in the knockout" becomes "rebound is marked larger only in the knockout; the printed p cannot be reproduced from the Table 1 means and dispersion"; where the row says "sag" with an Ih implication, write "sag at a fixed -200 pA step". | E09, E10, E13. |
| same row, test cell | Extend "a current-clamp step that matches the resting potential" to "and the peak potential"; list "smaller cell or immature membrane" as its own candidate beside branch D. | E10, E12. |
| hcn_20261107/output/README.md, Answer first | "does not need extra HCN" becomes "need not require extra HCN; the linear deflection accounts for only a share of the sag change and the non-linear share is undetermined". | E10, E11. |
| same file, INFERENZA 1 | "Sag as a fraction of the peak still rises" becomes "the sag fraction is not shown to differ (about 1.5 standard errors on the printed values)". | E11. |
| hcn_20261107/output/physiology.tsv, protocol_conditions (all rows) | "cells analysed as independent units" becomes "N's printed as cells/animals; unit of the test not stated". | E05. |
| same file, Y04, Y05, Y06, Y07 | Label Y05 to Y07 "linear illustration, upper end, no variance"; keep "possibly" in Y04; Y08 keep the bracketed audit note. | E10, E11, E09. |
