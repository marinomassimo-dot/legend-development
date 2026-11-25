# ADV-288 spec: minimal arm set for a functional-myelination pharmacology test in a Wwox model (SCI, 2026-11-25; hypothesis level; reference genotype class only; no dose, no compound, no treatment recommendation; not medical advice)

Held material only (no search, no spend, no contact). PREREG `PREREG_ADV288_SCI_20261125.md` (hash 3715785d8e14e87d, 21:49:30Z); numbers from `adv288_power.py` (output `adv288_power_output.tsv`); sentences `SENTENCES_ADV288_SCI_20261125.md` (hash cf1b7b201a03b126, frozen before the blind report). Form follows ADV-278. Consumers: ADV, IT (pup brief v2 add-ons (f) and (g), slice package 3.5, INV-06, RP-017). Step 0: add-on 5(f), 5(g) and slice package 3.5 carry the readouts and "not yet an endpoint" and no arm set, so this page is not a duplicate.

## One-page head

* **Question.** If a pro-myelinating drug class is ever put into a Wwox model, which four cells and which readout make the result readable, and what stops the comparison?
* **Arms (core, four cells, same litters, drug assigned within litter):** WT vehicle, KO vehicle, WT drug, KO drug. The class is named only as "an OPC-differentiation-promoting class with a published developmental conduction precedent"; the precedent in held full text is clemastine in developing wild-type mice (Palma 2022, below). No compound, dose or schedule is chosen here.
* **Optional fifth and sixth cells** (they carry the neuron-dependent versus OPC-intrinsic question, section 4): Olig2-Cre oligodendrocyte-lineage deletion vehicle and drug (Repudi 2021 already has the Olig2-Cre line, no conduction data).
* **Primary readout (route A):** callosal N1 conduction **velocity** from the distance-latency slope over at least three electrode distances (Palma used four: 500, 1000, 1500, 2000 micrometre), N2 velocity as the within-slice control, slices averaged to **one value per animal** (Palma's unit), seizure status recorded per animal; the same animals give the EM g-ratio and myelinated-axon count. Model: Synapsin-Cre neuronal deletion (the line with the held slow N1, Repudi 2021 Fig 5D). **Route B (secondary):** in vivo Tc-MEP latency and amplitude in the global knockout at 3 weeks (Cheng 2020), a gross readout (below).
* **Age window:** recording P17 to P21, inside both held ages (Repudi slices P13 to P17; Cheng 3 weeks; Palma P21). Dosing start and length are the laboratory's. Palma started at P5, before the first behavioural seizures (after P12, Cheng 2020) and slices of the neuronal knockout burst from P13 (Repudi Fig 2): seizures are a confound for any N1 reading and are recorded per animal.
* **n:** the held spread gives a coefficient of variation (CV) of about 0.12 to 0.21 for N1 velocity in wild-type mice (Palma, by eye) and 0.29 to 0.30 for Tc-MEP latency (Cheng, from SEM and n). Planning **24 animals per arm** (KO arms 24 each, about 28 litters, global-KO litter arithmetic only); **a pilot of at least 8 vehicle animals per genotype replaces the held CV before the drug arms run**, and `adv288_power.py` is rerun on it.
* **Stop condition:** WT drug-only N1 velocity down by at least 10 percent with a 95 percent interval excluding zero (Palma pattern). Then a KO drug effect is not read as rescue for that compound. Power to see a true 10 percent fall (unadjusted): 0.54 and 0.22 at 12 per arm (CV 0.12 and 0.21), 0.85 and 0.40 at 24 per arm; so at 24 per arm the interval condition, not the threshold, decides at the upper spread, and "no stop" is read as "a fall of 16 percent or more is excluded", not "no fall".
* **Rejecting observation of "feasible at about 12 animals per arm" (PREREG): MET.** At CV 0.21 the clemastine-sized WT slowing needs 24 animals per arm unadjusted (32 adjusted for three contrasts); at 12 per arm the smallest detectable ratio is 1.29 upward or 0.78 downward, so a slowing of about 16 percent is missed at the upper spread.

## 1. Held inputs (labelled by figure, panel, group, unit, species)

| Id | Source | Readout, unit | Groups, n (unit) | Value | SD, CV (derived) |
|---|---|---|---|---|---|
| I1 | Cheng 2020, Fig 2c; mouse, global KO, 3 weeks, in vivo | Tc-MEP onset latency, ms | +/+ 10, +/- 5, -/- 4 animals | 1.39 +- 0.13, 2.13 +- 0.22, 2.44 +- 0.37 (SEM) | SD 0.41, 0.49, 0.74; CV 0.30, 0.23, 0.30 |
| I2 | Cheng 2020, Fig 2b | Tc-MEP amplitude, microvolt | same | 59.2 +- 9.0, 59.6 +- 17.2, 11.8 +- 5.4 | SD 28.5, 38.5, 10.8; CV 0.48, 0.65, 0.92 |
| I3 | Repudi 2021, Fig 5D(ii); mouse, Synapsin-Cre, P13 to P17, slices | N1 latency, ms | 8 slices from 5 (control), 8 from 6 (KO) | about 2.5 and 3.2 (graph read; P = 0.0104 Wilcoxon over slices) | N1 CV by eye 0.15 to 0.25 with the one low point in each group, about 0.09 without it (blind reader); N2 widely spread |
| I4 | Palma 2022, Fig 2B; wild-type mouse, P21 slices, clemastine from P5 | N1 velocity (axis printed "mm/s", probably mm/ms, i.e. m/s; ratio only) | vehicle 12, clemastine 10 to 12 mice (each the mean of at least four sections) | about 0.505 and 0.425, ratio about 0.84; N2 about 0.275 in both | CV about 0.21 and 0.12 |

Limits of the inputs: values are read from graphs by eye; I1 and I2 carry SEM bars of unequal-n groups; I3 counts slices from 5 and 6 animals (the control n may be a copy of another experiment's n, slice package v2 3.5); I4's Methods name a "paired" t test for two independent groups, the text says P < 0.01 for N1 but Fig 2B marks N1 with one asterisk (the legend defines only * p < 0.05) and an unpaired test on the bars as read gives P about 0.03 (blind reader: 0.02 to 0.045 across reads), so the clemastine slowing is read as P < 0.05, not P < 0.01; Palma's Results also say dosing P5 to P20 and the Methods P5 to P21. **A correction for the pup brief:** Fig 2b and 2c of Cheng 2020 print brackets between +/- and -/-: amplitude marked *, latency marked n.s. Pup brief v2 add-on 5(f) says "there is no heterozygote-against-null test"; the figure carries both (amplitude *, latency n.s.); the Methods name only a one-way ANOVA with no post hoc test, so the test behind the brackets is unnamed. Cheng's Methods also define latency as shock-artefact onset to the major positive peak while the Results call it "onset latency", and the knockout line (WD1 or WD234) used for the recordings is not stated.

## 2. Design (cells, readout, units)

* **Cells:** the four core cells, every litter contributing to all four where possible (litter as block, drug assigned within litter and genotype), so litter is a cluster, not a confound. Global-KO litter arithmetic only (0.25 KO, about 1.75 KO pups per litter, pup brief v2 section 3): the neuronal cross has no held litter data.
* **Readout details:** distance-slope velocity (not first-peak latency at one distance: ADV-285 S8 shows the held readout is a single 250-micrometre latency); N2 as the control of the same slice; amplitude ratio N1/N2 secondary; slices to one value per animal before any test; seizure status, sex and litter recorded; EM g-ratio and myelinated axons counted per animal (Repudi's counts are per field from 3 animals: fields are not replicates, ADV-247).
* **Route B (Tc-MEP):** a clemastine-sized WT effect at CV 0.30 needs 48 animals per arm unadjusted: not resolvable. Route B can read a gross change only (the 1.76 latency ratio of I1 needs 6 per arm at CV 0.30); the global knockout dies by about 4 weeks and is fragile. It is a secondary, in vivo, ratio readout, never the primary.
* **Exposure:** the compound's brain exposure is measured in the age used (no pup exposure is held for any agent); a null at an unchecked exposure is a dose null.

## 3. n from the held spread (exact noncentral t; unadjusted two-sided 0.05, power 0.80; adjusted = alpha 0.05/3)

| Contrast (log scale) | CV 0.12 | CV 0.16 | CV 0.21 | CV 0.30 |
|---|---|---|---|---|
| WT drug-only slowing, ratio 0.84, per arm: unadjusted / adjusted | 9 / 12 | 15 / 20 | 24 / 32 | 48 / 64 |
| KO restored by half the gap (ratio 1.14 against KO vehicle), per arm | 15 / 20 | 25 / 33 | 42 / 56 | 84 / 112 |
| KO restored by the whole gap (ratio 1.28, the I3 gap), per arm | 5 / 7 | 8 / 11 | 13 / 17 | 25 / 33 |
| Interaction contrast, log scale 0.305 (ratio 1.36: KO restored 1.14 minus WT slowed 0.84; four-cell), per cell | 6 / 8 | 10 / 13 | 16 / 21 | 31 / 42 |

Smallest detectable ratio at n per arm (unadjusted; downward in brackets): n = 12: 1.15 (0.87) at CV 0.12, 1.29 (0.78) at CV 0.21; n = 24: 1.10 (0.91) and 1.19 (0.84). **At 24 per arm and CV 0.21 the test sees a WT slowing of about 16 percent and a KO restoration of about 19 percent or more (about two thirds of the I3 gap); it cannot see a restoration of half the gap at CV 0.21 (needs 42).** Held checks: the I1 contrast (n 10 against 4, CV 0.30) is at the harmonic equal-n of 5.7; the equal-n power at 4 per arm is 0.60, so the PREREG prediction that 4 per arm suffices is a miss. All inputs are by-eye graph reads: the CV is the weakest number and the pilot replaces it.

## 4. What each outcome favours (hypothesis; the neuron-dependent versus OPC-intrinsic question is RP-017)

Panel valid first: KO vehicle N1 slower than WT vehicle in this colony (else stop, outcome 0).

| # | WT drug | KO drug (against KO vehicle) | Same-animal g-ratio | Favours | Does not show |
|---|---|---|---|---|---|
| 0 | n/a | KO vehicle not slow | n/a | the held slice readout does not reproduce here | any statement about the drug |
| 1 | no change (interval inside minus 10 percent) | N1 restored by about a third of the gap or more, g-ratio lower | lower | the oligodendrocyte-lineage machinery can still be pushed in a neuronal knockout: the block is upstream or non-cell-autonomous | that it is neuron-dependent; needs the O-KO cells |
| 2 | no change | N1 unchanged, oligodendrocyte count may rise | unchanged | maturation is not the limiting step, or the drug acts on a cell count that does not translate into myelin (the Palma dissociation) | which |
| 3 | slowed by 10 percent or more | any | any | stop for this compound: the class costs conduction in normal myelination | rescue |
| 4 | no change | N1 slower | higher | harm in the knockout at this exposure | mechanism |
| 5 (needs optional cells) | no change | restored in neuronal-deletion cells, not restored in Olig2-Cre deletion cells | lower, not lower | a differentiation-promoting drug rescues what neuronal loss removes and cannot rescue what the oligodendrocyte-lineage deletion removes: neuron-dependent defect | any clinical use |
| 6 (needs optional cells) | no change | restored in both | lower in both | the drug bypasses either defect: the pharmacology does not separate the two explanations | which |

N1 alone cannot separate a neuron-dependent myelin defect from a non-myelin cause (axon calibre, excitability, seizures): the same-animal g-ratio does (ADV-285 S7).

## 5. When the experiment is uninformative (so it is not run)

1. A wild-type drug-only arm is missing (Palma: the drug slowed conduction in normal pups while oligodendrocytes rose).
2. N1 is read at one distance, or slices are the unit, or fields count as animals.
3. Fewer than about 12 animals per arm at the held spread, unadjusted (a 16 percent change is then missed), or no pilot CV.
4. Seizure status not recorded (burst age overlaps the recording age).
5. Tc-MEP used as the primary readout of a modest effect (48 per arm at CV 0.30).
6. No brain exposure at the age used.

## 6. Premise check, and what this changes

ADV's brief premise stands as written: the pup brief and slice package carry the readouts but no arm set. The check found one correction (the heterozygote-against-null brackets in Cheng Fig 2b and 2c) and one by-eye unit problem (Palma's axis). Decision: the pup brief gets **a conduction line that is a four-cell test with a WT drug-only arm**, replacing "candidate needing re-measurement"; RP-017's decision line stays `waiting` until a pilot CV exists, because the held CV is a graph read from three different assays.
