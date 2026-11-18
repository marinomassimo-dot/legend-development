# Expected sign and size per pilot arm, from the frozen model runs (HE with SCI; draft for SCI to amend; 2026-11-16; hypothesis generator, not evidence; not medical advice)

Written for: SCI (owner of the model and the brief), ADV. Source: `sim_harness/runs_20261116/{i19,oat,grid}` (20 seeds each, frozen by digest before the runs; K1-K6, S1-S7, G1-G2 all PASS). **Reading rule:** these are sizes of a model STEP (a parameter scaled by the factor shown), not of a drug at a dose; the class-to-parameter mapping is SCI's labelling and an assumption; a measured size that is much larger or of the other sign says the model lacks a term (for example an interneuron-specific sodium effect), which is itself the informative result. Written beside the brief's arms before any slice exists.

Baseline (no step): S-KO incidence 1.00, 750 bursts per 40 slices x 600 s (median over seeds), median burst duration 0.758 s; S-HT incidence 0.20 (10 bursts); S-WT incidence 0.10 (5 bursts).

## Per arm (I19 run; ratios are step over baseline at the same genotype)

| pilot arm class | model step | S-KO: bursts (ratio) | S-KO: duration (ratio) | S-KO: bursts per bursting slice (ratio) | S-HT: incidence (baseline 0.20) | sign |
|---|---|---|---|---|---|---|
| GABA-A positive modulator, tonic-preferring (neurosteroid-type label) | tonic GABA-A weight x1.2 | 224 (0.30x) | 0.718 s (0.95x) | 5.9 (0.31x) | 0.00 (silent seeds 0.55) | rate lower |
| GABA-A positive modulator, synaptic-preferring (benzodiazepine-type / non-benzodiazepine label) | phasic GABA-A weight x1.2 | 543 (0.72x) | 0.680 s (0.90x) | 13.7 (0.73x) | 0.03 (silent seeds 0.10) | rate lower |
| NMDAR pore blocker or GluN2B NAM at a fractional block (the pore blocker and the NAM differ only in how much NMDAR current is removed) | NMDAR weight x0.9 | 553 (0.74x) | 0.571 s (0.75x) | 13.8 (0.74x) | 0.11 (silent seeds 0.00) | rate lower |
| T-type blocker (one protocol) | T-type trigger weight x0.75 | 616 (0.82x) | 0.772 s (1.02x) | 15.4 (0.82x) | 0.15 (silent seeds 0.00) | rate lower |
| T-type enhancer (the opposite step, as a model check; not a pilot arm) | T-type trigger weight x1.25 | 902 (1.20x) | 0.744 s (0.98x) | 22.5 (1.20x) | 0.25 (silent seeds 0.00) | rate higher |
| sodium-channel blocker, pyramidal component only (AH1 single-component arm) | noise amplitude x0.9 (SCI's label: sigma x0.9) | 403 (0.54x) | 0.820 s (1.08x) | 10.2 (0.54x) | 0.03 (silent seeds 0.05) | rate lower |
| duration-only arm (resource-type; no pilot class named) | resource depletion x0.6 | 888 (1.18x) | 1.248 s (1.65x) | 22.2 (1.18x) | 0.29 (silent seeds 0.00) | rate higher |

## Interval and duration separately (OAT, 40% steps; the I19 run reports no interval)

| step | median interval (s) | median duration (s) | bursts per minute | reading for the brief's 6.2 table |
|---|---|---|---|---|
| baseline | 26.0 | 0.717 | 1.75 |  |
| T-type trigger weight x0.6 | 35.6 | 0.732 | 1.16 | interval UP, duration about equal: the T-type blocker prediction of H-B1 |
| T-type trigger weight x1.4 | 20.6 | 0.707 | 2.42 | the opposite step |
| NMDAR (sustainer) weight x0.6 | 102.1 | 0.144 | 0.21 | duration DOWN a lot and interval UP: the NMDAR arm moves both, mostly duration |
| tonic GABA-A weight x1.4 | 134.3 | 0.551 | 0.09 | the burst rate collapses (silent seeds) |
| phasic GABA-A weight x1.4 | 50.4 | 0.410 | 0.74 | rate down, duration down: a synaptic-selective modulator shortens bursts too |
| adenosine weight x0.6 / x1.4 | 20.2 | 0.752 | 2.33 | x1.4: 1.42 per minute against 1.75 baseline: a weak knob (see the I4 two-step design) |

## GABA-A potentiation at graded steps (GRID; the sign question of the brief's HSCI-2)

| pam (potentiation step) | S-KO bursts | silent seeds |
|---|---|---|
| load_coupling=0, pam=0 | 140 | 0.00 |
| load_coupling=0, pam=0.3 | 6 | 0.30 |
| load_coupling=0, pam=0.6 | 0 | 1.00 |
| load_coupling=1, pam=0.3 | 7 | 0.15 |

Reading: in this model a GABA-A potentiation suppresses bursts and does not raise them, with or without chloride-load coupling (G1 and G2 PASS); an observed RISE of the burst rate under a GABA-A positive modulator (HSCI-2) would be a result the model does not produce, and is the discriminating observation between the rebound-ignition and the restoration-of-inhibition pictures.

## What each outcome would change (for the pilot's decision page)
- A tonic-preferring step that suppresses more than a phasic-preferring step at the same fractional change (S-HT incidence 0.00 against 0.025; S-KO bursts ratio in the table): supports the tonic-brake reading (I13); the opposite order, or no difference, weakens it.
- A T-type step that lengthens the interval without changing the duration, and an NMDAR step that shortens the duration: H-B1 (two-stage) as the model reads it; both moving in proportion: a single gain.
- A sodium-channel step: the single-component noise arm (sigma x0.9) predicts SUPPRESSION; aggravation (AH1) is predicted only by the MIXED arm (pyramidal noise down AND interneuron inhibition down: SCI's arm 9, sigma x0.9 with J_I x0.7: S-KO bursts -12%, S-HT incidence 0.17 -> 0.38, S-WT 0.11 -> 0.25, predictions hashed first; see PILOT_ARM_EXPECTATIONS_SCI.md). Correction 2026-11-16 22:35Z (SCI): an earlier version of this line said the model lacks the term; it does not.

Limits: model steps, not doses; 20 seeds of one frozen model; the labels that map a pilot arm to a parameter are assumptions; the S-HT incidence is the model's reading of the held 0/11, 4/23, 36/42 gradient, not a measurement.
