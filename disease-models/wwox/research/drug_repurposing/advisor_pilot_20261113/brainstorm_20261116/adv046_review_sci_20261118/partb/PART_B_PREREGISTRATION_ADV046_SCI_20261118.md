# ADV-046 part B, preregistration (SCI, 2026-11-18; written and hashed BEFORE any run of `adv046_b_compare.py`; non-canonical; MODEL: hypothesis generator, not evidence; mechanism level; no dose, no agent; reference genotype class only; not medical advice)

Written for: ADV (host). Corrections go in dated addenda; this file is not edited after hashing.

## Question
Do the held models (the burst oscillator `rebound_oscillator.py`, the hysteresis harness, the homeostat toy `homeostat_toy.py`; sha256 checked by the script: c050b8ff... and a4885508...) allow an informative comparison (a) between single and combined mechanisms and (b) between explanations that give the same observable, here a fall of burst rate at matched block depth and a post-washout burst-rate class? The explanations are the ones already written in lane D (5.2): R-A transient NMDAR suppression, R-D HCN1/Ih, R-E disinhibition, block kinetics, adaptation after removal (R-B). None is renamed.

## Baseline (the simple one)
A single NMDAR-weight scaling without adaptation: J_N x (1 - d) with every other weight at BASE, and a prescribed return of J_N to 1 (the hysteresis harness case: memoryless). Cells C0 (part 1) and K0 (part 2).

## What is represented, and what is NOT REPRESENTED (not refuted)
| Explanation | How it enters the model | Status |
|---|---|---|
| R-A | J_N x (1 - d); d is the fractional reduction of the NMDAR weight; the map from the evoked-response depth to d is ASSUMED linear and one-to-one | represented |
| R-D | the existing `hcn_block` knob (hyperpolarising drive removal and a raised rebound gate); values 0.1, 0.2, 0.4 (held class scan: 0.3 alone gives 0.46 of baseline). The sign (hyperpolarising) is the model's; an opposite-sign action through input resistance is NOT REPRESENTED; there is **no sag variable**, so a sag change cannot be read, and its map to `hcn_block` is unknown | partly represented (drive only) |
| R-E | NOT represented as a mechanism (no interneuron NMDAR term). Represented only as a prescribed rule on the existing `phasic_gain`: phasic_gain = max(0, 1 - e d), e in {2, 4, 8, 16} (e = fractional loss of phasic inhibition per fractional NMDAR loss; an ASSUMED swept value, not a model term) | rule only |
| block kinetics (trapping, off-rate, use dependence, Mg2+ competition) | NOT represented as a state. A slow unblock is a prescribed J_N(t) waveform, J_N x (1 - 0.7 exp(-t/tau_off)) after washout, tau_off in {10, 20, 40, 80} min; use dependence (block deeper during bursts than in the evoked response) is NOT REPRESENTED | waveform only |
| adaptation after removal | the held homeostat toy unchanged (gain w on J_A and J_N, 120 s running mean, bounds 0.5 and 2.0), tau_w in {3600, 1800} s | represented (one functional form) |
Not represented at all: sag as an observable, input resistance, subunit selectivity, trapping state, in vivo.

## Observables fixed in advance
Part 1 (steady state, 600 s after a 60 s burn-in, 40 networks per set, parameter sets vectorised in one call; two seeds 20261201 and 20261202; bootstrap 2000 resamples over networks): burst count per network. For each set: ratio to the control set (d = 0, hcn = 0, e = 0) and, for C1 and C2 cells, the ratio to the C0 cell at the same depth ("the pore-blocker-like cell against d-APV-like at matched depth"). Depth grid 0, 0.05, 0.10, 0.15, 0.20, 0.30, 0.50. **Distinguishable from C0 at depth d** = the point ratio lies outside [0.7, 1.3] and its bootstrap 95% interval excludes 1.0 (direction: below or above); a cell whose control ratio and whose C0 ratio are both at most 0.15 is at the **floor** and is not distinguishable. **Rise** = control ratio at least 1.2 with the interval above 1.0 at some d in {0.05 ... 0.30}.
Part 2 (held toy harness unchanged: 20 networks, seed 20261117, calibration seed 777; J_N multiplier 0.3 for 1800 s as in the held toy cell, so K2_3600 must reproduce the held EARLY 2.50 and MID 1.914; windows from the start of washout: W1 0 to 30 min, W2 30 to 60, W3 60 to 120): rate over PRE, class **below** (< 0.7, the lasting-suppression class of the frozen priors), **within** (0.7 to 1.3), **above** (> 1.3); and E, the mean over the window of the model's own NMDAR weight J_N(t) x w(t) relative to baseline (the model's analogue of the evoked delayed response), class below/within/above at bands of 10% and 5%.
Cells: K0 (instant washout, no gain); K1_10, K1_20, K1_40, K1_80 (slow unblock, no gain); K2_3600, K2_1800 (gain, instant washout); K3_3600_20, K3_3600_40, K3_1800_20 (both).

## Assumptions whose dependence is tested
Ih knob strength (0.1, 0.2, 0.4); coupling e (2 to 16); tau_off (10 to 80 min); tau_w (3600, 1800 s); the noise seed (part 1, two seeds: a statement counts as true only if true on both); the E band (10% and 5%). **Not tested** (stated limits): the depth map (only the ordering of results transfers, not the depth numbers), the gain's target (J_A and J_N only), the sign of the Ih action, one baseline parameter set.

## Predictions (subjective weights fixed now; not validated probabilities; each a separate binary statement; log score = ln of the probability given to what happens, against coin ln 0.5 = -0.693; scored literally by `--decide`)
| # | Statement | P |
|---|---|---|
| B1 | at d = 0.5 every C0, C1 and C2 cell has control ratio <= 0.15 (floor: burst rate cannot tell them apart at deep block) | 0.75 |
| B2a | the C1 cell with hcn = 0.1 is distinguishable (below) from C0 at 2 or more of the depths 0.05, 0.10, 0.15, 0.20, 0.30 | 0.30 |
| B2b | the same for hcn = 0.2 | 0.80 |
| B3 | at some depth <= 0.20 some C2 cell is distinguishable above C0 and some C1 cell is distinguishable below C0 (opposite signs available) | 0.50 |
| B4a | no rise at e = 2 or 4 | 0.90 |
| B4b | a rise at e = 8 | 0.45 |
| B4c | a rise at e = 16 | 0.75 |
| B5 | C1 combined with depth is log-additive: for hcn 0.2 and 0.4 at d = 0.10 and 0.15, abs(ln R_comb - ln R_C0 - ln R_hcn alone) <= 0.25 | 0.50 |
| B6 | K0 in W2: rate over PRE in [0.9, 1.1] | 0.85 |
| B7 | K1_20 is within and K1_40 is below in W2 | 0.70 |
| B8 | K2_3600 and K2_1800 are both above in W2 | 0.35 |
| B9 | in W2 some K1 cell is below and some K2 cell is above (sign opposition between residual block and adaptation) | 0.60 |
| B10 | in some K3 cell and window the rate is in [0.9, 1.1] while the matching K1 cell (same tau_off) and the matching K2 cell (same tau_w) are both outside [0.9, 1.1] (cancellation of the two mechanisms) | 0.30 |
Harness checks, not scored: K2_3600 reproduces the held EARLY and MID within 2% (if not, part 2 is void and reported so); the depth at which C0 falls to 0.5 and the residual J_N deficit at which C0 falls to 0.7 are read from the held class and one-at-a-time scans (J_N x0.9 gives 0.73 of baseline, x0.8 0.39) and from the run.

## Verdict rule (frozen)
INF1: some depth in {0.05 ... 0.30} where C0 control ratio is at least 0.15 and some C1 cell is distinguishable (below), on both seeds. INF2: B9. **INFORMATIVE** if both, **PARTLY** if one, **NOT INFORMATIVE** if neither (then a targeted reading of held data replaces the simulation, as the assignment allows).

## What each outcome changes (stated now)
* B1 true and INF1 true: the depth at which pore blocker and d-APV can be told apart by burst rate is intermediate, not the deep depth of P1 or the shallow depth of P2. The arm changes by an order and a readout: a matched depth **series** (about 0.1, 0.2, 0.3 of the evoked response) for **both** agents instead of one deep point, and the burst-rate-against-evoked-depth curve as the readout.
* B9 true: the post-washout sign of the burst-rate deviation, read together with the evoked response (E), separates residual block (below, E below) from adaptation (above, E above); the evoked response must then be reported at 30, 60 and 120 min with its precision, since the model amplifies a small residual into the "lasting" class.
* B10 true: a post-washout "no change" does not exclude the two mechanisms acting together; the evoked response is needed to say which.
* B4b and B4c false: within e <= 16 the oscillator cannot produce a bell shape; R-E is then NOT REPRESENTED in the sense that the model needs a loss of inhibition more than 16 times the NMDAR loss to show it, and the burst-rate series cannot test it at the depths where the oscillator is steep; the P2 sub-arm would test the model's cliff, not R-E.
A null or an unexpected result is reported as it is; nothing is added to the model afterwards.

## Limits
One parameter set (the S-KO neocortical fit), 40 or 20 networks per cell, one seed in part 2, a toy with one functional form, an assumed depth map, no sag; the results describe the model, and any mapping to a slice is an INFERENZA. The held oscillator is fitted to one slice baseline.
