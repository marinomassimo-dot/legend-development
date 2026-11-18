# Hysteresis test of the oscillator: predictions and protocol, frozen before the run (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; mechanism level; no dose, no agent; not medical advice; reference genotype class only)

Requested by ADV after the ketamine note. This file is hashed and the hash is sent to ADV before `hysteresis_sweep.py` is run for results. Script: `hysteresis_sweep.py` (hashed with it). Before hashing I ran only two checks, neither a protocol run: `--smoke` (5 s, no statistic) and a baseline-fidelity run at constant J_N with a non-protocol seed (999; 20 networks, 600 s): 18.2 bursts per 600 s per network, median duration 0.72 s, against the held 18.2 and 0.76 s of the frozen oscillator (`PILOT_ARM_EXPECTATIONS_SCI.md`). The script copies the oscillator loop with J_N made time-dependent; the T-type drive term was re-written inline and matches `simulate` term by term.

## Question
Does the I1 oscillator (S-KO baseline parameters BASE; J_N x1 = the fitted value) keep a memory of a transient or slow reduction of its NMDAR weight J_N, so that its burst rate or burst duration does not return to the pre-reduction baseline after J_N returns?

## Protocol (fixed)
* 40 networks per run, every run uses the same seed within a part (Part A seed 20261117, Part B seed 20261118), so the pre-reduction window is identical across the conditions of a part (paired design). Burn-in 60 s from the rested state. Bursts: onset at u > 0.5, end at u < 0.25, duration > 0.1 s.
* **Part A (transient reduction).** J_N multiplied by a factor f: linear ramp 1 to f over 30 s, hold D, linear ramp back over 30 s. f in {0.5, 0.8}; D in {60, 300, 1800} s; a control run (f = 1) for each D. Windows: PRE = 600 s of baseline after burn-in; HOLD = the held plateau; EARLY = the 120 s after the return ramp; LATE = the next 600 s. Measures per window: pooled burst rate (per min per network), median duration; per network: bursts in PRE and LATE.
* **Part B (slow up-and-down sweep).** J_N multiplier 1 to 0.3 linearly over R, then 0.3 to 1 linearly over R, R in {600, 2400} s, after 120 s of baseline; a control run (multiplier fixed at 1) for the same timeline. Seven bins of the multiplier (0.3 to 0.4, ..., 0.9 to 1.0); rate per bin on the down leg and on the up leg (bursts per min per network in that bin, with the dwell time of the bin).
* Bootstrap: 2000 resamples over networks, seeds fixed in the script (1 for Part A, 2 for Part B); 95% intervals.

## Decision rules (fixed; hysteresis = a memory that outlasts the reduction)
* **Part A, per condition (six):** hysteresis if any of
  (rate) LATE/PRE pooled rate ratio outside [0.75, 1.33] AND outside the control's 95% bootstrap interval of its own LATE/PRE ratio;
  (duration) LATE/PRE median-duration ratio outside [0.75, 1.33] AND differing from the control's same ratio by more than a factor 1.25;
  (silence) more than 10% of networks that had at least 3 bursts in PRE have none in LATE AND that fraction exceeds the control's by more than 0.05.
  EARLY is not used for hysteresis (an early overshoot is a recovery transient, reported apart).
* **Part B, per R:** hysteresis if, among bins with at least 40 bursts on each leg (evaluable bins), at least 2 have an up-leg/down-leg rate ratio outside [0.75, 1.33] AND a 95% bootstrap interval of the ratio that excludes 1.
* **Headline (H):** NO HYSTERESIS = none of the six Part A conditions and neither Part B ramp meets its rule.

## Predictions (written before the run; each scored as a separate binary statement, ln of the probability given to what happened; coin baseline ln 0.5 = -0.693)
| # | Statement | P(true) |
|---|---|---|
| S1 | **H: no hysteresis** (headline, as stated above) | **0.90** |
| S2 | At f = 0.5, D = 1800: the EARLY burst rate exceeds 1.25 times the PRE rate (a recovery overshoot of the resource, the model's analogue of the held washout overshoot) | 0.65 |
| S3 | At f = 0.5, D = 1800: the HOLD burst rate is below 0.25 times the PRE rate | 0.60 |
| S4 | At f = 0.8, D = 1800: the HOLD burst rate is between 0.4 and 0.8 times the PRE rate | 0.60 |
| S5 | In Part A, no condition has a LATE window with more than 5% silent networks | 0.88 |
| S6 | Part B, R = 2400: at least 4 of the 7 bins are evaluable | 0.60 |
Reasoning, for the record, not for scoring: every state variable has a time constant of at most about 18 s, the rested state is the initial state of every held run and returns to baseline bursting, and the held one-at-a-time scans are graded cliffs, so a stable second attractor is unlikely; the residual probability sits in untested bistability, in noise-induced long silent epochs near the cliff and in the criteria's sensitivity at 40 networks.

## What the result will and will not say
A null (no hysteresis) says that this oscillator, with the slow variables it has, has no memory beyond about two minutes after J_N is restored, and that a weeks-long carry-over cannot arise from it without a new slow variable. It says nothing about any person. A positive result (hysteresis) would be a property of the model's bistability and a reason to read its cliff scans again; it would not show a lasting drug effect.
