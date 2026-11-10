# SCI42 S3 — minimum discriminating design for the GluN2B-directed comparison, with onfasprodil and NP10679 placed where the data allow

Non-canonical working note, a **proposal to discuss with the laboratory**. Not medical advice; no dose, schedule or route; no experiment is commissioned. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI. Builds on `ampa_nmda_discrim_20261108/` (M01–M18), `nmda_composition_discrim_20261109/` (INV-05 narrow comparison) and `generation_it41_20261109/comparisons_it41.md`; nothing there is changed here. The producer's tables (`output/`) give the compound facts; every compound statement below cites a `D`/`M` row.

## 1 · The preparation actually studied, and what is missing from it

DATO (PMID 34634460, as carried in `ampa_nmda_discrim_20261108/output/observations.tsv`): neuron-specific (Synapsin-Cre) Wwox deletion, acute neocortical slices, layer II/III pyramidal cells, P13–P17, 35 C; spontaneous bursts abolished by d-APV 50 µM at one concentration, without a vehicle or time-matched control group; incubation ACSF 1.3 mM Mg2+ and 3.5 mM K+ (the recording ACSF is not stated); sIPSC amplitude about halved. DATO (absence, perimeter in the earlier packages): no isolated NMDAR current, no subunit, glycine, bath pH or measured Mg2+ datum exists for it. Nothing from other preparations (oocytes, culture, adult or other-region slices, humans) is merged into this system: the compound facts of the producer (`D02`, `D09`, `D13`) are recombinant or declared and enter only as constraints on what an arm can mean.

## 2 · The four explanations

| Id | Explanation (IPOTESI) | Reading in this design |
|---|---|---|
| E1 | Total NMDAR gain: the burst needs NMDAR-mediated drive beyond a threshold x (percent of isolated NMDAR current that must be removed to stop it) | The d-APV series defines x; any NAM is read against it |
| E2 | Weight of GluN2B-containing receptors beyond their share of the current | A GluN2B NAM stops the burst at a smaller percent of isolated NMDAR current removed than d-APV needs |
| E3 | State of the preparation: bath pH, Mg2+, K+, Zn2+, temperature, run-down | Burst incidence and drug effect move with the measured state and wild-type tissue can be made to burst |
| E4 | Alternative action or general loss of network function: any large cut in excitatory drive, off-target action of a tool (for NP10679 a declared H1 antagonism, `D14`), sedation-like or release-reducing effects | A receptor-agnostic cut matched to the same percent reproduces the effect |

## 3 · What each arm predicts (qualitative; no cell is a measured result)

"x" = the abolition threshold measured with d-APV. "r" = the removable share of isolated NMDAR current for the NAM used, measured, not assumed.

| Arm | E1 | E2 | E3 | E4 | Compatible with several (not discriminating) | Weakens | Control that interprets a null |
|---|---|---|---|---|---|---|---|
| A0 conditions + vehicle (time-matched, same order) | no change | no change | drift or a change of bursts without drug | no change | stable bursts | any drift here is the E3 signal and confounds every later arm | none: it is the control |
| A1 d-APV series against percent isolated NMDAR current removed (separate slices or cells for the isolated current, GABA-A not blocked in the burst slices) | burst falls along one curve; threshold x | same curve (the reference) | curve shifts with measured Mg2+, K+, pH | same curve if drive is general | all explanations expect abolition at full block | no abolition at near-complete removal | measured percent removed (a nominal concentration is not a percent); d-APV is surmountable, so the glutamate level matters |
| A2 one ifenprodil-site NAM (ifenprodil or Ro 25-6981 as the tool; r measured, with and without a Zn2+ chelator in the isolated-current recordings) | burst falls only as far as r, curve coincident with A1 over [0, r] | curve left of A1 over [0, r] | effect only at some Mg2+/K+/pH | coincident with A1 and with A6 | a plateau below x is unresolved: GluN2A pool, triheteromers, or x above r | curve coincident with A1 | r measured in the same preparation and age; a plateau below x is not support for E1 and not a refutation of E2 |
| A3 Zn2+ chelator, isolated-current arm | r larger in a Zn2+-rich preparation (the ceiling moves, not the share logic) | same | tonic Zn2+ is a state variable (E3) | none | NAM removable share depends on Zn2+ (INFERENZA from ifenprodil values, D-rows of the earlier package, not read for the newer compounds) | no Zn2+ dependence of r | chelator arm without NAM to see its own effect |
| A4 NP10679, only after M03 and M01 (see section 5) | follows A1 at the measured r | left of A1 as A2; plus a potency shift between two controlled pH values | the burst effect follows pH itself even at fixed vehicle | an off-target effect would not follow the recombinant pH-potency shift | a shift in potency alone cannot separate E2 from E3 | no pH-dependent potency shift in the isolated current | vehicle and d-APV at each pH (protons change NMDAR current themselves); maximum and potency kept separate |
| A5 onfasprodil, chemotype control for A2, only if A2 shows a removable fraction | as A2 | as A2 if the percent removed matches | as A2 | as A2 | same percent removed by a second chemotype: target-level reading, not site independence (site unknown, `D01`) | a different percent removed at the same measured exposure: the NAM class cannot be assumed to share a ceiling (`D03`) | none beyond A2's; its maximum on triheteromers is not known (`D03`) |
| A6 receptor-agnostic cut matched to the same measured percent (for example a release-reducing manipulation; no mechanism paper read here) | coincident | the NAM is more effective per percent removed | the cut shifts with state | coincident with A1 and A2 | coincidence supports E4 and E1, says nothing on WWOX | NAM or d-APV acts at a smaller percent than A6 | A6 must itself be quantified on two metrics (charge; peak or slope), because the burst depends on both |
| A7 wild-type tissue under a matched trigger, same arms | same sensitivity | same | wild-type bursts under the same state | identical sensitivity in all genotypes | a response in wild-type tissue is not a Wwox-specific finding | knockout-specific sensitivity | triggered wild-type bursts need their own timing and vehicle |

## 4 · Order of the experiments, and what may not wait

**Present from the first slice (a result is uninterpretable without them):**
1. Measured values, not recipes: bath pH, Mg2+, K+, temperature at the recording site; the isolated NMDAR current (AMPA and GABA-A blocked, holding potential stated) in separate cells or slices from those scored for bursts.
2. A time-matched vehicle (A0) at the same position in the sequence.
3. The percent of isolated NMDAR current removed for every drug at the concentration used (the x-axis), with the d-APV series defining x (A1).
4. One conventional ifenprodil-site NAM with its removable share r, with and without a Zn2+ chelator in the isolated-current recordings (A2, A3): a plateau without r cannot be read.
5. The matched receptor-agnostic cut (A6) in the same slices as the NAM burst arm: a favourable NAM result cannot be read without it, so it is not deferred until a favourable result appears.
6. Animals as the unit of replication; blinded scoring of bursts; order of arms randomised within animal.

**Conditional (only if step 4 shows a removable fraction, or the cited premise is measured):**
* A4 NP10679, only after (a) the preparation's tissue pH is measured (M01 of the producer's list), (b) NP10679's recombinant potency and maximum at two pH values are measured with the stated conditions (M03; the discovery paper was not readable, `D08`), and (c) its H1 and other off-target actions are considered for the readout in use (`D14`). Its unique contribution is a within-preparation specificity signature: if the burst effect follows the recombinant pH-potency shift while d-APV and a conventional NAM do not, it supports a GluN2B-NAM action over an off-target one (IPOTESI). Neither a pathological pH nor a pH shift in the Wwox tissue is assumed.
* A5 onfasprodil as a second chemotype after A2.
* A7 genotype comparators.

**May wait:** the GluN2A-preferring arm (TCN-201: needs a measured slice co-agonist level first), the AMPA/kainate arm (separate question, `ampa_comparison_it41_20261109/`), heterozygous tissue as an intermediate (the earlier package shows it is not a clean one), a second NAM of the same site.

**Redundant or to avoid:** a second ifenprodil-site NAM before the first has shown r (it controls chemotype only, same ceiling); NP10679 at several pH values before the preparation's pH is measured; any clinical-exposure matching.

## 5 · Limits that this proposal keeps

* Design thresholds are assumptions to agree with the laboratory, not findings: the number of pH values (two controlled, within the slice's viability), the concentration steps, the definition of "abolition" (percent of baseline burst rate), what counts as a plateau. None is given a number here.
* Statistical unit: the animal (litter where applicable); slices and cells are nested and enter a mixed model or are summarised per animal; cells or nuclei are not independent animals. Bursting is binary per slice and counts per minute per slice; analysis choices are for the laboratory.
* A reduction of bursts by any arm is a reduction of an electrophysiological phenotype in P13–P17 slices. It is not a developmental recovery, not a rescue of the defect, and a drug response does not show that the drug's target is altered in Wwox.
* Onfasprodil and NP10679 have no data in this preparation; their roles (producer's `roles.tsv`, verified separately) concern the comparison, not benefit.
* Human exposure (onfasprodil in depression and healthy adults; NP10679 in healthy adults) is exposure in other populations: no dose, no pediatric statement, nothing about WOREE (`D05`–`D07`, `D16`).
