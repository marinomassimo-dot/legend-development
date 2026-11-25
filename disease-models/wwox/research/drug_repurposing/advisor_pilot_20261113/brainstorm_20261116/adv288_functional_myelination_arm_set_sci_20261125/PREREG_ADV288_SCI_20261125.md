# PREREG ADV-288: minimal arm set for a functional-myelination pharmacology test in a Wwox model (SCI, 2026-11-25; hypothesis level; reference genotype class only; not medical advice)

Frozen BEFORE any n, power or detectable-effect number is computed. Held bytes only; no search, no spend, no contact. The Obeid 2026 article is not touched.

## Step 0 (done before this file)

Pup brief v2 add-on 5(f) and (g) (`experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/PUP_BRIEF_V2_CONSOLIDATED.md` lines 71 and 72), slice package v2 section 3.5 (`SLICE_PACKAGE_V2_CONSOLIDATED.md`) and the current text (`current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md`, add-ons (f) and (g)) were read. They carry the two readouts as candidates ("not yet an endpoint") and name no genotype-by-drug arm set, no wild-type drug-only arm, no age or n for a drug test of conduction. A repository search for "drug-only", "WT drug" and "wild-type drug" finds only seizure-arm text (lithium-alone and wild-type ethosuximide arms of the PTZ design). Verdict: NOT already specified; Step 1 proceeds.

## Inputs, labelled by figure, panel, group, unit and species (from the held prints; effects read by eye where marked)

| Id | Source | Readout | Groups and n (unit) | Values | Spread used |
|---|---|---|---|---|---|
| I1 | Cheng 2020 (PMID 32000863), Fig 2c and text; mouse, global Wwox KO, 3 weeks, in vivo, chloral hydrate | Tc-MEP onset latency, ms | +/+ 10, +/- 5, -/- 4 (animals) | 1.39 +- 0.13, 2.13 +- 0.22, 2.44 +- 0.37 (SEM) | SD = SEM x sqrt(n): 0.41, 0.49, 0.74; CV 0.29, 0.23, 0.30 |
| I2 | Cheng 2020, Fig 2b and text | Tc-MEP amplitude, microvolt | same | 59.2 +- 9.0, 59.6 +- 17.2, 11.8 +- 5.4 (SEM) | SD 28.5, 38.5, 10.8; CV 0.48, 0.65, 0.92 |
| I3 | Repudi 2021 (PMID 33914858), Fig 5D(ii); mouse, Synapsin-Cre neuronal deletion, P13 to P17, acute slices | callosal-stimulation N1 latency, ms | S-Control 8 slices from 5 animals, S-KO 8 slices from 6 (slices; tests over slices) | about 2.5 and 3.2 (graph read; Wilcoxon P = 0.0104) | by eye N1 spread small (CV about 0.15 to 0.25); N2 spread large (CV above 0.4) |
| I4 | Palma 2022 (PMID 35372341), Fig 2B; wild-type C57BL/6 mouse, P21 acute slices, clemastine 50 mg/kg/day i.p. from P5 | callosal N1 conduction velocity (distance-latency slope, four distances), axis printed "mm/s" (implausible as a unit; ratios only) | vehicle n = 12, clemastine n = 10 to 12 (mice, each the mean of at least four sections) | about 0.505 and 0.425 (graph read; ratio about 0.84; P < 0.01); N2 about 0.275 in both | SEM by eye about 0.03 and 0.015; SD about 0.10 and 0.05; CV about 0.21 and 0.12 |

## Method (stated before data)

* Primary scale: log of N1 conduction velocity (or log latency), animal as the unit (slices averaged within animal; Palma's own unit), CV taken as the SD on the log scale.
* n per arm from a two-sided two-sample t test, power 0.80, alpha 0.05, computed exactly (noncentral t), labelled **unadjusted**; the same at alpha 0.05/3 (three primary contrasts) labelled **adjusted for three contrasts (Bonferroni)**. The interaction contrast (KO drug effect minus WT drug effect) is a four-cell contrast, variance 4 sigma^2/n, labelled as such.
* Smallest detectable difference (SDD) at a given n, same labels. All inputs and the formula are printed in the output.
* Litters: global-KO fraction 0.25 (Mendelian) and about 1.75 KO pups per litter (pup brief v2 section 3); the neuronal-deletion cross has no held litter data and is not computed.

## Predictions (frozen)

1. SDD for N1 velocity at n = 12 per arm, unadjusted, CV 0.12 to 0.21: **0.14 to 0.26** (relative difference).
2. n per arm to detect a clemastine-sized wild-type slowing (ratio 0.84, i.e. -16 percent) at CV 0.12 to 0.21, unadjusted: **9 to 28**; adjusted for three contrasts: **12 to 38**.
3. n per cell for the interaction contrast of 30 percent (wild type slowed 16 percent by the drug, knockout restored by about 14 percent, which is half of the 28 percent genotype gap of I3), CV 0.12 to 0.21, unadjusted: **5 to 17**.
4. The genotype gap of I1 (latency ratio 1.76) is detectable at 4 animals per arm at I1's own CV (0.3): **yes** (it was detected there, P < 0.01); the amplitude gap (ratio 0.20) likewise.
5. The I3 gap (ratio 1.28 in latency) at CV 0.2 needs **8 to 14** animals per arm unadjusted (the paper used 8 and 8 slices, so its own power at the animal level is not established).

## Rejecting observation

The claim to be rejected is "a four-arm conduction test is feasible at about 12 animals per arm". It is rejected if prediction 2 comes out above 20 animals per arm at CV 0.21 unadjusted (the cost then goes into the spec as the headline) or if CV is not recoverable from the held figure (then the spec states n as unspecified until the pilot).

## Stop condition of the comparison itself (to be written into the spec)

Wild-type drug-only arm: N1 velocity or amplitude slowed or reduced with a 95 percent interval excluding zero and a point estimate at least 10 percent (the Palma pattern) means a knockout drug effect cannot be read as rescue; the comparison stops there for that compound.

## Blind reader

One legend-delegate, model sonnet, effort high (stated here; read back from `framework/scripts/session_model_census.py`), receives the final sentences plus the WHOLE source material (the legend and values of I1 to I4 and the three figure images by path), not the conclusions.

Not medical advice; no dose; no compound chosen; a pro-myelinating comparator is named as a class only.
