# Order in which the distinct measurements are interpretable (ADV-006, producer P)

Non-canonical. Not medical advice; nothing here commissions, authorises or hurries any wet work; measurements are described with the comparison and decision they change. M-ids are this folder's (`measurements.tsv`), not the packages' (SCI42's own M01-M10 are translated in `crosswalk.tsv`). Rule used: B is "after" A only where B's own source says a result of A conditions it; otherwise "unordered".

## Dependencies the sources state (each with its sentence)

| # | B interpretable after A | Source sentence (verbatim) | Where |
|---|---|---|---|
| D1 | M04 (agonist response) and M03 (evoked IPSC) after M01 (sIPSC re-record), in SCI42 only | "no (required if M03 confirms the amplitude loss)" | `chloride_gradient_sci42_20261110/output/new_measurements.tsv`, rows M05 and M06, column required_from_start |
| D2 | M02 (mIPSC) after M04, in SCI42 only | "partly redundant with M05 for the response arm: worth keeping only if M05 is done" | same file, row M04, column separates |
| D3 | M15 (matched non-GABAergic comparator) is a co-requirement of every drug arm | "yes (for any drug arm)" | same file, row M10, column required_from_start |
| D4 | M20 (chloride-transport arm) after M05 (E_GABA) | "E_GABA measured in the same preparation before and after the manipulation (M01)" | `conditional_prediction.tsv`, row 2, column control_that_interprets_a_null |
| D5 | M16 (GABA-supply arm) and M17 (modulation arm) after M02, M04 and M05 | "A GABA-supply arm (L1) or a postsynaptic-modulation arm (L2) is interpretable only after mIPSC, agonist response and E_GABA place the deficit." | `inhibitory_defect_sci47_20261112/README.md`, answer 3 |
| D6 | E_GABA (the L3 measurement) gates L1 and L2 | "(E_GABA) that gates L1 and L2" | same, answer 3 |
| D7 | Phase 1 arms after Phase 0 | "Phase 1 only for the lever Phase 0 selects." | same, answer 4 |
| D8 | M26 (KCC2/NKCC1 protein) after M05/M14 | "direction of evidence runs from `DF_GABA` to the molecules, not back" | `commit_candidates/CC-20260826-EGABA-EXPERIMENT-01.md`, section 2 |
| D9 | inside M14: trajectory arm first, then paired EEG arm, then rescue (M27) | "If Arm B is null with its positive control satisfied, Arms A and C are not run" and "and only if A shows covariation" | `CC-20260826-EGABA-ANALYSIS-PLAN-01.md`, section 9 |

## Dependencies that look stated and are not
* **SCI42 README calls M03, M01, M02 "in order of interpretability", but M01's own row says "Interpretable alone at one age."** The first-then-second order of M01 (sIPSC re-record) and M05 (E_GABA) is a cost and priority order ("cheapest"), not a dependency: neither row conditions the other. Reported as unordered.
* **SCI47 Phase 0 lists seven steps (i)-(vii) with no order** and, unlike SCI42, with no condition on the sIPSC re-record. The two packages therefore order the same recordings differently (D1 versus an unconditional list): conflict CF22 (gap).
* **M11 (driven wild-type slices) and M06 (tonic current):** the SCI42 README sentence lists them after the clause "if M03 confirms the amplitude loss", but the tables' own column says no condition. Reported as unordered.
* **L5 (M19)** is "kept, conditional" in SCI47's status cell; the condition is not named beyond sharing the recorded cells with E_GABA. No order can be drawn.

## Unordered
M05 (E_GABA, alone at one age), M07 (covariates), M08 (age series; contains the methods of M01, M05, M06), M09, M10, M12, M13, M18, M21, M22, M23, M24, M25, M28, and M01 itself (first in SCI42's list; nothing conditions it).

## Are L1 (supply), L2 and L3 arms that can be interpreted in an order?
* **L3 is a measurement that comes first in SCI47, and is not an arm there.** The package keeps "E_GABA kept as the measurement that gates L1 and L2" (levers.tsv L3 status) and drops the drug arm; SCI42 keeps chloride-gradient manipulations as conditional arms with E_GABA read in the same cells (conflict CF15). The order L3-measurement before L1/L2 is stated (D5, D6); an L3 arm before or after them is not.
* **L1 and L2 are not ordered against each other; they are alternatives selected by what Phase 0 shows.** `levers_notes.md` table: "| mIPSC amplitude down, agonist response normal | E2 (supply per event) | L1 GABA availability | L2 starts from normal receptors |" and "| mIPSC amplitude down, agonist response down | E3 (receptor response) | L2, if physiological-chloride deficit is confirmed | L1 raises a signal onto fewer receptors |". A combination of two levers is "only as an exploratory occlusion test" (design_review).
* **L2 wording (ADV-004):** the L2 arm stays gated by the Phase 0 measurements; the subtype wording of `gabaa_subtype_adv004_20261114/README.md` answer 6 and the NP3P3 series (M21) do not change that gating and M21 is not ordered against the slice recordings. Pointer only.
