# Result of the LABELLED TOY: a slow homeostatic gain added to the oscillator (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; a toy tuned on nothing; cannot confirm the structure S1; says nothing about any person; no dose, no agent; not medical advice)

Written for: ADV (asked it), IT (the "what the model says" layer of the statement, as a dated labelled-toy line). Follows `RESULT_HYSTERESIS_SCI_20261117.md` and `KETAMINE_INDIRECT_EFFECTS_NOTE_SCI_20261117.md` (gap S1).

## Order of record
Predictions `PREDICTIONS_HOMEOSTAT_TOY_FROZEN_BEFORE_RUN_SCI.md` sha256 a5909676e3a6bd207559d9949f392122280ef1f077f1308c0fc8bcefe9c633f5; script `homeostat_toy.py` a48855081414110fb02b5c58550844b54225f3bf548dcf40da676df36e0ac420 (hashes re-checked equal immediately before the run). Hashed at 13:21:16Z and sent to ADV (who verified the digests) before the run; run start 13:21:41Z; six cells in parallel, one run each, no re-run; only check before hashing: `--smoke`. Results `homeostat_toy_cells.json` (all six cells).

## Answer first
**A slow homeostatic gain of this form produces a post-release excess of bursting of the right sign, larger than the held one, that decays over about its own time constant; it never produces a lasting suppression (a benefit) in any cell.** In the model, then, S1 can supply the missing ingredient for the held washout overshoot (about 1.85 times baseline, image-read) qualitatively, with the sign that makes it a rebound, not a benefit. Size and baseline stability are not matched.

## Cells (20 networks; PRE rate 1.63 bursts per min per network; ratios to the same cell's PRE)
| tau_w (s) | hold D (s) | HOLD/PRE | EARLY (first 120 s after return) | MID (120 to 720 s) | LATE (window at min(3 tau, 7200) s) | max w seen |
|---|---|---|---|---|---|---|
| 3600 | 1800 | **0.04** (block holds) | **2.50** | **1.91** | 1.07 | 1.27 |
| 3600 | 7200 | 0.86 (block escaped) | 3.54 | 2.80 | 1.03 | 1.82 |
| 600 | 1800 | 1.24 (block escaped) | 3.21 | 0.81 | 1.07 | 1.84 |
| 600 | 7200 | 1.77 (block escaped) | 3.28 | 0.83 | 1.05 | 1.84 |
| 3600 | control, f = 1 | 1.13 | EARLY 1.13 | 1.01 | 1.07 | 1.00 |
| 600 | control, f = 1 | 1.10 | EARLY 1.10 | 1.01 | 1.07 | 1.00 |
(HOLD/PRE is the plateau rate divided by the same cell's PRE rate; raw rates are in `homeostat_toy_cells.json`.)

## What the cells show
1. **Overshoot of the right sign in every blocked cell (EARLY 2.5 to 3.5 times PRE, held about 1.85, image-read), decaying with tau_w:** for tau_w = 3600 s the excess lasts well beyond the 12-minute MID window (1.9 to 2.8) and is gone by LATE; for tau_w = 600 s it is over within MID.
2. **For the fast gain the block escapes during the hold** (HOLD/PRE 1.2 to 1.8 at tau 600; at tau 3600 and a 2-hour hold, 0.86): the toy compensates for a sustained block, because w also scales the AMPA recurrent term, which the NMDAR block does not touch. The held d-APV result (bursting abolished) is reproduced only by the cell with tau_w = 3600 s and the shorter hold (0.04, with an overshoot of 2.5 after).
3. **A transient undershoot after the overshoot at the fast gain** (MID 0.81 and 0.83 at tau 600): about 17 to 19 percent fewer bursts for minutes 2 to 12 after release, gone by LATE. It is the toy's damped return, not a lasting effect, and sits just inside the pre-set limit (0.75). A slower or stronger variant could be deeper; I did not test one.
4. **No cell has a lasting suppression** (LATE 1.03 to 1.07). The toy cannot produce a weeks-long benefit; it can only produce a rebound whose length is its time constant.
5. **The no-block controls are not perfectly flat:** EARLY 1.10 and 1.13, LATE 1.07 (a calibration of a0 on a different seed leaves the baseline about 7 to 13 percent off); all blocked-cell ratios of 2.5 or more are far above that, but the stability criterion of statement T2 was not met.

## Prediction against result (separate binary statements; log score = ln of the probability given to what happened; coin baseline -0.693)
| # | Statement | P | Result | Score |
|---|---|---|---|---|
| T1 | EARLY/PRE above 1.25 in at least one blocked cell | 0.85 | **true** (2.5 to 3.5) | -0.163 |
| T2 | EARLY/PRE in [1.5, 2.2] with the same-tau control within [0.9, 1.1] | 0.35 | **false** (size 2.5 to 3.5; control EARLY 1.10 and 1.13) | -0.431 |
| T3 | tau_w = 600: LATE/PRE in [0.85, 1.15] | 0.85 | **true** (1.07, 1.05) | -0.163 |
| T4 | no MID or LATE ratio below 0.75 | 0.92 | **true** (lowest 0.81) | -0.083 |
| T5 | tau_w = 600, D = 7200: max w at least 1.9 | 0.90 | **false** (1.84; w stops short of the cap because the returning bursts feed back on abar) | -2.303 |
**Total -3.142 against -3.466 for five coin flips (+0.32 nats).** The real miss is T5: I expected w to climb to the cap during a long block; the escape from the block (the bursts returning) stops it near 1.84, which also is why hold rates of 1.2 to 1.8 appear. I had not foreseen that the toy compensates for the block during the hold; this is a property of scaling both excitatory terms and should be read as a design choice, not as biology.

## What this says for the statement (layer "what the model says", labelled toy)
In a toy with a slow homeostatic gain, lowering NMDAR weight leads to a rebound of excess bursting after release, whose length is set by the gain's time constant and which returns to baseline; no lasting suppression appears, so nothing in the toy resembles a lasting benefit. The held slice overshoot is the one observation such a gain would explain (qualitatively), and it points the opposite way from a benefit. The toy is not tuned and is not evidence that the slice overshoot is homeostatic.

## Limits
Twenty networks, one seed per cell, one functional form (a multiplicative gain on J_A and J_N, a 120 s running mean, bounds 0.5 and 2.0), two time constants and two holds, a calibration of a0 on a different seed; tuned on nothing; no weeks-scale run (the longest window is 7200 s plus 600 s); it does not test S2 to S4. Not medical advice; nothing about any person.
