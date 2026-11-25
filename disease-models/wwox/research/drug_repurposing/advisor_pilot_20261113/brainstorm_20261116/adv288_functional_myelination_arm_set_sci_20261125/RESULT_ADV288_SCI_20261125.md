# RESULT ADV-288: minimal arm set for a functional-myelination pharmacology test in a Wwox model (SCI, 2026-11-25; hypothesis level; reference genotype class only; no dose, no compound; not medical advice)

Files: `PREREG_ADV288_SCI_20261125.md` (hash 3715785d8e14e87d, 21:49:30Z), `adv288_power.py` and `adv288_power_output.tsv`, `SENTENCES_ADV288_SCI_20261125.md` (hash cf1b7b201a03b126, frozen before the blind report), `BLIND_REPORT_ADV288_SCI_20261125.md` (blind reader: legend-delegate, claude-sonnet-5-5, effort high, read back from `session_model_census.py`, 22 turns; it received the sentences and the whole sources: Cheng Fig 2 and text, Repudi page 27 and text, Palma Fig 2 and text), `SPEC_ADV288_MIN_ARM_SET_FUNCTIONAL_MYELINATION_SCI_20261125.md` (the one-page spec, with the blind corrections applied).

## 1. Answer

**Step 0: NOT already specified.** Pup brief v2 add-on 5(f) and 5(g), slice package v2 section 3.5 and the current pup text carry the two readouts as candidates ("not yet an endpoint") and no genotype-by-drug arm set, no wild-type drug-only arm, no age or n for a drug test of conduction. The spec was therefore written (Step 1): four cells (WT and KO, vehicle and drug), callosal N1 velocity from the distance slope with N2 as control, one value per animal, same-animal g-ratio, seizure status recorded, recording P17 to P21, 24 animals per arm planned and a vehicle pilot of at least 8 per genotype to replace the held spread, and a stop rule (WT drug-only N1 velocity down at least 10 percent with the interval excluding zero). Optional fifth and sixth cells (Olig2-Cre deletion with and without drug) carry the neuron-dependent versus OPC-intrinsic question of RP-017.

## 2. Predictions against results (PREREG)

| # | Prediction | Observed | Verdict |
|---|---|---|---|
| 1 | SDD at n = 12 per arm, CV 0.12 to 0.21, unadjusted: 0.14 to 0.26 | ratio 1.154 to 1.286 up (0.15 to 0.29), 0.866 to 0.778 down (0.13 to 0.22) | downward inside, upward upper edge 0.29 above 0.26: marginal miss |
| 2 | n for ratio 0.84, unadjusted 9 to 28; adjusted 12 to 38 | 9 to 24; 12 to 32 | inside |
| 3 | interaction 5 to 17 per cell | 6 to 16 (for log contrast 0.305, ratio 1.36, not "30 percent") | inside |
| 4 | the I1 gap detectable at 4 per arm at CV 0.30: yes | equal-n power 0.60; needs 6 per arm (the paper had 10 against 4, harmonic n 5.7) | miss |
| 5 | I3 gap (ratio 1.28) at CV 0.2 needs 8 to 14 | 8 (CV 0.16) to 13 (CV 0.21) | inside |
| RO | "feasible at about 12 per arm" is rejected if n for ratio 0.84 at CV 0.21 exceeds 20 | 24 unadjusted, 32 adjusted | **rejecting observation met** |

## 3. The blind reader (3 of 8 MUST CHANGE, all verified by me)

* **T1 (MUST CHANGE, verified).** 0.41 / 1.39 = 0.295: CV 0.30, not 0.29 (truncation). SDs 0.41, 0.49, 0.74, CVs 0.23 and 0.30, and both brackets (Fig 2c +/- v -/- n.s.; Fig 2b +/- v -/- *) were confirmed.
* **T6 (MUST CHANGE, verified).** My interaction contrast was ln 1.14 minus ln 0.84 = 0.305 (ratio 1.36), which I had labelled "30 percent". The numbers 6 to 16 per cell are right for 0.305; for a true 30 percent (ln 1.30 = 0.262) the reader finds 8 to 21. Label corrected; the 15 to 42 and 5 to 13 numbers of T6 were confirmed.
* **T7 (MUST CHANGE, verified).** Palma's text says P < 0.01 for N1; Fig 2B marks N1 with one asterisk and the legend defines only * p < 0.05; an unpaired test on the bars as read gives P about 0.03 (reader 0.02 to 0.045). The clemastine slowing is read as P < 0.05. I checked: t = 2.33 from means 0.505 and 0.427, SEM 0.03 and 0.015, n 12 and 10, P about 0.03.
* T2, T3, T4, T5 CORRECT (T3 with a note: one low N1 point in each group; without it the Repudi CV is about 0.09, with it 0.15 to 0.25). T8 is a design rule, not a claim about sources; its power was added to the spec (a true 10 percent fall has power 0.54 and 0.22 at n = 12, 0.85 and 0.40 at n = 24, which I reproduced).
* Extra findings the reader made and I confirmed in the held text: Cheng's Methods name only a one-way ANOVA with no post hoc test while three pairwise brackets are printed, define latency as artefact onset to the major positive peak (the Results say "onset latency") and do not state the knockout line (WD1 or WD234); Palma's Results say dosing P5 to P20 and the Methods P5 to P21, and the unit "mm/s" is probably mm/ms; Repudi's Methods promise an unpaired Student's t test while Fig 5D uses Wilcoxon over slices (nested units), the P = 0.0104 is printed under legend item (i) but belongs to panel (ii), and the N1 latency is a single-distance latency, not a velocity.

## 4. The final sentences (corrected; these replace the frozen ones)

**T1.** In Cheng 2020 (global Wwox knockout mice, 3 weeks, in vivo, chloral hydrate) Tc-MEP onset latency is 1.39 +- 0.13 ms in +/+ (n = 10), 2.13 +- 0.22 in +/- (n = 5) and 2.44 +- 0.37 in -/- (n = 4) (SEM), a standard deviation of 0.41, 0.49 and 0.74 ms and a coefficient of variation of 0.30, 0.23 and 0.30; Fig 2c prints a bracket between +/- and -/- marked n.s. and Fig 2b one on the amplitude marked *, although the Methods name only a one-way ANOVA with no post hoc test.

**T2.** unchanged (Palma 2022: N1 velocity about 0.425 against 0.505 after clemastine from P5, ratio about 0.84, axis printed "mm/s" and probably mm/ms, CV about 0.12 and 0.21, N2 about 0.275 in both).

**T3.** unchanged, with the note that the N1 CV is 0.15 to 0.25 with the one low point in each group and about 0.09 without it.

**T4, T5.** unchanged. **T6.** Restoration of half the 28 percent genotype gap (ratio 1.14 against KO vehicle) needs 15 to 42 animals per arm (unadjusted), restoration of the whole gap (ratio 1.28) 5 to 13, and an interaction contrast of 0.305 on the log scale (ratio 1.36) 6 to 16 per cell; a contrast of exactly 30 percent needs 8 to 21.

**T7.** Palma's Methods name a "paired" Student's t test for two independent groups of mice, the text gives P < 0.01 for the N1 slowing while Fig 2B marks it with one asterisk (legend: * p < 0.05), and an unpaired test on the bars as read gives P of about 0.03; the slowing is read as P < 0.05.

**T8.** unchanged; at 24 per arm and the upper spread a true 10 percent fall has power 0.40, so "no stop" means "a fall of 16 percent or more is excluded".

## 5. Consumers and decision

* **IT (pup brief v2 add-ons (f) and (g), slice package 3.5, current text):** (a) replace "there is no heterozygote-against-null test" by the sentence of T1 (the figure prints the brackets; the test is unnamed); (b) add to add-on (g) the four-cell conduction test of the spec with the WT drug-only arm, distance-slope velocity, N2 control, same-animal g-ratio, seizure status, 24 per arm planned and a pilot CV (ADV-285 S8 listed what was missing; this is the arm set); (c) do not quote Palma's P < 0.01 (use P < 0.05, T7).
* **ADV:** the rejecting observation (about 12 per arm) is met; the cost is 24 per arm at the upper spread, 48 KO animals and about 28 litters in the global-KO arithmetic; RP-017's decision line stays `waiting` for a pilot CV (the held CV is a graph read across three assays). INV-06: the question "does any pro-myelinating comparison become informative" is answered with the arm set and the stop rule; no compound is chosen.

## 6. Limits

All CVs come from graph reads (Palma bars about 0.005, Repudi means about 0.15 ms, Cheng about 0.02 ms); Repudi's spread is per slice and nested; no paper gives an SD. The neuronal cross has no held litter data; the litter arithmetic is global KO only. The class is not chosen and no exposure is held for any agent in pups. Twelve of the 13 adjacent papers of ADV-285 remain abstract level and were not re-read here. Kotler and Obeid were not touched.
