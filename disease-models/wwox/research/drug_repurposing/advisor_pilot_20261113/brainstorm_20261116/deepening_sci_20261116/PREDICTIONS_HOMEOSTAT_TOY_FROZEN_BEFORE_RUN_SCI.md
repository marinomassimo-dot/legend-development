# LABELLED TOY: a slow homeostatic gain added to the oscillator; predictions and protocol, frozen before the run (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; mechanism level; no dose, no agent; not medical advice; reference genotype class only)

Asked by ADV after the meeting (task 3), to test the gap S1 of `KETAMINE_INDIRECT_EFFECTS_NOTE_SCI_20261117.md`: the oscillator has no slow gain variable and does not reproduce the held washout overshoot (about 1.85 times baseline, image-read, d-APV in the S-KO neocortical slice). **This is a toy. It cannot confirm the structure (it is tuned on one image-read number at most), it says nothing about any person, and its result enters the "what the model says" layer only under that label.**

## Toy definition (fixed)
Script `homeostat_toy.py` (hashed with this file before the run). The I1 oscillator at BASE plus w, a gain on the excitatory recurrent terms (J_A and J_N). A running mean of activity, abar (time constant 120 s), is compared with the baseline mean a0 (measured by the script from a calibration run, seed 777, 600 s, w fixed at 1): dw/dt = w (a0 - abar) / (a0 tau_w), clipped to [0.5, 2.0]. J_N is multiplied by f = 0.3 during a block (linear ramps of 30 s). Before hashing I ran only `--smoke`. No fidelity run was made on a protocol seed.

## Protocol (fixed)
20 networks per cell, seed 20261117 for all cells. Timeline: burn-in 60 s, PRE 600 s, ramp down 30 s, hold D, ramp up 30 s, then windows after the return: EARLY = the first 120 s, MID = 120 to 720 s, LATE = a 600 s window starting at min(3 tau_w, 7200) s after the return. Rate = bursts per min per network (duration > 0.1 s); ratios are to the same cell's PRE rate. Cells: tau_w in {600, 3600} s x D in {1800, 7200} s with f = 0.3 (four blocked cells), plus controls with f = 1 (no block) for tau_w = 600 and 3600 at D = 1800 (two control cells, the same timeline).

## Predictions (each scored as a separate binary statement; log score = ln of the probability given to what happened; coin baseline -0.693)
| # | Statement | P(true) |
|---|---|---|
| T1 | in at least one blocked cell EARLY/PRE exceeds 1.25 (an overshoot of the right sign) | 0.85 |
| T2 | in at least one blocked cell EARLY/PRE lies in [1.5, 2.2] AND the control cell with the same tau_w has EARLY, MID and LATE ratios all within [0.9, 1.1] (size near the held value without destabilising the baseline) | 0.35 |
| T3 | for tau_w = 600 (both D), LATE/PRE lies in [0.85, 1.15] (the overshoot decays; no lasting change) | 0.85 |
| T4 | no blocked cell has a MID or LATE ratio below 0.75 (no lasting suppression, i.e. no benefit) | 0.92 |
| T5 | for tau_w = 600 at D = 7200, the maximum w seen reaches at least 1.9 (the cap region) | 0.90 |
Reasoning, not scored: during a near-silent block, abar falls and w rises toward the cap; on release the network is more excitable and bursts more until abar returns above a0 and w decays at the rate set by tau_w; with tau_w = 3600 the decay is slower than the LATE window of 3 tau_w capped at 7200 s, so LATE may still be elevated for the slow cells (that is allowed by T3, which names only tau_w = 600). The sign of any such toy effect after a block is an excess of bursting, never a benefit.

## What the result will and will not say
It will say whether a slow homeostatic gain of this form can produce an overshoot of the right sign and roughly the right size while keeping the baseline, and how long it lasts. It will not show that the slice's overshoot is homeostatic, will not show any benefit, and says nothing about any person.
