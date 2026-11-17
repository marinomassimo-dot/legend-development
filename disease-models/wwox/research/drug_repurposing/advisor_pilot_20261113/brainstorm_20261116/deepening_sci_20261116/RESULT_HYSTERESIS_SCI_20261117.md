# Result: the oscillator keeps no memory of a reduction of its NMDAR weight (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; mechanism level; no dose, no agent; not a statement about any person; not medical advice)

Written for: ADV (asked it), the meeting. Follows `KETAMINE_INDIRECT_EFFECTS_NOTE_SCI_20261117.md` section 1.

## Order of record
Predictions `PREDICTIONS_HYSTERESIS_FROZEN_BEFORE_RUN_SCI.md` sha256 6a6f01193b0c62b86d8ca05f529f589686cab80eec322b91647aabea02467d83; script `hysteresis_sweep.py` 430258bee3af34ea31281b78dbbcf3913feda7e370aacc275e49eae711d6eefe; `rebound_oscillator.py` c050b8ff0a1ba8fe5ef340f2a57168ecf578f161be12392c42fec98851b89419. All three were sent to ADV at 13:07:38Z, before the protocol run (start 13:07:46Z; the two parts ran in parallel and finished about 13:13Z). Only checks before hashing: `--smoke` and a constant-J_N fidelity run on a non-protocol seed. One run per part; no re-run; the decision was applied by the script's frozen rules (`--decide`), result files `hysteresis_result_A.json`, `hysteresis_result_B.json`, `hysteresis_decision.json`.

## Answer first
**No hysteresis. The oscillator returns to its pre-reduction burst rate, burst duration and fraction of active networks after J_N is restored, for every transient reduction tested (factor 0.5 and 0.8; hold 60 s, 300 s and 1800 s) and for slow up-and-down sweeps of 600 s and 2400 s per leg.** The rule-based headline (S1, prior 0.90) held.

## Part A: transient reduction (40 networks per run; paired seeds; PRE, HOLD, EARLY (120 s), LATE (600 s))
| f | hold D (s) | HOLD/PRE rate | EARLY/PRE | LATE/PRE (control 95% interval) | median duration PRE to LATE (s) | silent networks LATE |
|---|---|---|---|---|---|---|
| 0.5 | 60 | 0.04 | 0.98 | 0.99 (0.91 to 1.08) | 0.73 to 0.74 | 0 |
| 0.5 | 300 | 0.04 | 1.02 | 0.98 (0.90 to 1.06) | 0.73 to 0.72 | 0 |
| 0.5 | 1800 | 0.05 | 0.94 | 0.96 (0.88 to 1.04) | 0.73 to 0.74 | 0 |
| 0.8 | 60 | 0.28 | 0.97 | 0.99 (0.91 to 1.08) | 0.73 to 0.74 | 0 |
| 0.8 | 300 | 0.38 | 1.01 | 0.98 (0.90 to 1.06) | 0.73 to 0.72 | 0 |
| 0.8 | 1800 | 0.40 | 0.94 | 0.96 (0.88 to 1.04) | 0.73 to 0.74 | 0 |
No condition met the rate, duration or silence rule. Every LATE/PRE ratio lies inside the interval of its own f = 1 control. The pre-reduction rate was 1.89 bursts per min per network (18.9 per 600 s), duration 0.73 s.

## Part B: slow ramp, J_N multiplier 1 to 0.3 to 1 (rate on the down leg against the up leg at the same multiplier)
Bins with at least 40 bursts on each leg: 2 of 7 at R = 600 s, 4 of 7 at R = 2400 s. In those bins the up/down ratios were 0.92 and 0.93 (R = 600) and 0.94 to 1.15 (R = 2400), all with intervals containing 1; no bin was flagged and no bin met the two-bin rule. Where the multiplier is below about 0.6 the network is nearly silent on both legs (the cliff), so those bins carry too few bursts to evaluate: at R = 2400 the lowest bin had 6 bursts on the down leg and 15 on the up leg (ratio 2.5, interval 1.0 to 8.0), and the next had 8 and 9. **Under the frozen rule these bins are not evaluable; the 6-against-15 pair is a lead to look at with more networks near the cliff, not a result.** The control sweeps (multiplier fixed at 1) show the false-positive floor of the criterion: one bin of seven (0.8 to 0.9, R = 600) had an interval excluding 1 by chance, which is why the rule asks for two bins.

## Prediction against result (each a separate binary statement; log score = ln of the probability given to what happened; coin baseline ln 0.5 = -0.693)
| # | Statement | P | Result | Score (nats) |
|---|---|---|---|---|
| S1 | no hysteresis (headline) | 0.90 | **true** | -0.105 |
| S2 | EARLY rate above 1.25 times PRE at f 0.5, D 1800 | 0.65 | **false** (0.94) | -1.050 |
| S3 | HOLD rate below 0.25 times PRE at f 0.5, D 1800 | 0.60 | **true** (0.054) | -0.511 |
| S4 | HOLD rate between 0.4 and 0.8 times PRE at f 0.8, D 1800 | 0.60 | **false** (0.396, 0.004 below the edge) | -0.916 |
| S5 | no condition has more than 5% silent networks in LATE | 0.88 | **true** (0) | -0.128 |
| S6 | at least 4 evaluable bins at R = 2400 | 0.60 | **true** (4, exactly) | -0.511 |
**Total -3.221 against -4.159 for six coin flips (+0.94 nats better than the coin).** S4 is scored literally as a miss by 0.004; in substance the hold reduction (-60%) is deeper than the -46% of the pilot-arm table at J_N x0.8 (different windows, ramps and seeds; I did not reconcile the two and the model's burst-count sensitivity to J_N should be read as roughly -50 to -60%).
**Calibration note (owned):** S2 was the real miss. I expected the resource variable, fully recovered during a block, to give an overshoot of bursts on release (the model's analogue of the held washout overshoot). There is none (EARLY/PRE 0.94 to 1.02): bursts are paced by chloride, adenosine and T-type availability, which relax in the same 10 to 18 s, so the extra resource shows up as nothing at the population-rate level. **Consequence: the model does not reproduce the held 1.85-fold washout overshoot of the slice.** That overshoot (an observation) therefore needs a variable the oscillator lacks, which is evidence for S1 (a homeostatic gain) as a missing structure, not for a lasting benefit.

## What would have to change in the oscillator for a weeks-scale carry-over (model statements; none is a claim about a person)
* **S1, homeostatic gain.** Add a slow variable w (time constant of hours to days) driven by the time-averaged activity and scaling J_A, J_N or J_I. Sign: a block lowers the average, so w would raise the gain after the drug, an excess of bursting, not a benefit; a lasting benefit would need feedback of the opposite sign to scaling, for which nothing is held. The unexplained held overshoot (1.85-fold) is the one observation such a variable would explain.
* **S2, a ratchet.** Add a state m that moves during the block or the plasticity window and does not relax (time constant of weeks or no decay) and shifts a weight across the cliff. The held sensitivities give the size: a persistent 20% lowering of J_N gives roughly -50 to -60% of bursts; a persistent 20% rise of the tonic weight -77% (R17c); a persistent 20% rise of the synaptic GABA-A weight -20%. So a persistent change of order 20% in one or two weights is enough in the model; whether one exposure can produce it is unmeasured (ASSUMED).
* **S3, bistability.** The time constants and feedbacks of the fitted oscillator give one attractor: the result above says there is no memory beyond the relaxation time, tested up to a 30-minute hold and 40-minute ramps. A second attractor would need positive feedback in a slow variable (for example a chloride or resource loop with a sign this parameter set lacks) and a region of the cliff where it exists; the weak 6-against-15 hint at the lowest multiplier is the one place to look, with more networks.
* **S4, a non-neuronal slow variable.** Add q (inflammation, glial or metabolic state; weeks) as a slow drift of J_tonic, J_a or J_I. The model would then show a weeks-long effect that follows q's own time course, driven by whatever moves q (illness resolution, for example), not carried over from the drug; this is the rival explanation table's rows 3 to 4 written as a model term.

## Limits
40 networks, one seed per part (paired across conditions inside a part), hold up to 1800 s and ramps up to 2400 s per leg: the test covers minutes to about an hour, not days or weeks, and says nothing outside that range; hysteresis near the cliff (multiplier below about 0.6) was not evaluable with the frozen minimum count; a single parameter set (BASE, the S-KO neocortical fit); the model is a hypothesis generator fitted to one slice baseline and does not describe any person or condition other than the reference genotype class; the criteria (25% change, bootstrap over 40 networks) have a detection floor of about that size. Not medical advice.

## One line
The oscillator is memoryless on this protocol (score -3.22 against -4.16 for coin flips; the one real miss was an expected rebound overshoot that the model does not produce); a weeks-long carry-over would need a new slow variable (S1 to S4), none of which is held.
