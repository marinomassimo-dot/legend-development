# SCI45 size check — preregistration (written 2026-11-11 before `size_check.py` was run)

Non-canonical. A **constraint** (what must be true), not an estimate of what is true. Inputs are the producer's pH50 values (`output/ph_sensitivity.tsv`); the verifier's corrected values replace them in a rerun and both runs are kept.

**Model.** Open fraction of a pHo-closed channel: o(pH) = 1 / (1 + 10^(n (pH50 - pH))), n = Hill slope. Fractional closure for a fall from baseline pH0 to pH0 - d: f = 1 - o(pH0 - d) / o(pH0). Loss of resting conductance: L = s * f, where s is the share of the wild-type resting conductance carried by the channel at pH0. Required: L = 0.28 (Wwox Table 1 means, SCI43). Grid: pH0 in {7.2, 7.4}, d in {0.05, 0.1, 0.2, 0.3, 0.5}, n in {1, 2}, s in {0.05, 0.1, 0.23, 0.5}; pH50 per channel: TASK-1 {6.6, 7.3, 7.4}, TASK-3 {6.3, 6.5}, TREK-1 {7.5}. The channel-specific Hill slope is unreported in the sources (except TREK-1 pHi); n is a sensitivity axis, not a datum. Baseline pH0 7.2 reflects the tissue PCO2 offset reported at abstract level, not a Wwox measurement.

**Predictions (fixed now).**
* S1. TASK-3 gives L < 0.01 at d <= 0.2 for every grid cell.
* S2. For d <= 0.2 and s <= 0.23, no TASK-1 or TREK-1 grid cell gives L >= 0.28 (the whole Ba2+-sensitive share measured elsewhere is already below 0.28, so s * f < 0.23 by construction).
* S3. Required share s* = 0.28 / f exceeds 0.5 for every channel at d <= 0.2 and n = 1.
* S4. Only d >= 0.5 with pH50 above pH0 and n = 2 brings f above 0.8.

**Word rule.** "A pH route can carry the published pair" is written only if some cell with s <= 0.5 and d <= 0.3 reaches L >= 0.28 for a sourced pH50; otherwise "the published pair is not reached by a pH change of the size sources report for perfused tissue, for any share below X". A failed prediction is reported as failed. The check says nothing on whether pH differs between genotypes.
