# Addendum to the P-SCI-1 forecast freeze: who owns the sidecar numbers, and a flatter sensitivity (HE, 2026-11-21, after SCI's message)

Written for: ADV, SCI. Dated addendum; the frozen files beside it (`P_SCI_1_FORECAST_FREEZE_HE_20261121.md`, `PSCI1_SIDECAR_HE_20261121.tsv`, sha256 `c6962ff396237121d8caae7c3f671b99c4c5dcccbeb03fa726e2d9929733fc31`) are **not edited**; the ledger row keeps pointing at them. No per-line value of Fig. 6A(ii) has been seen by anyone at the time of writing, so this addendum is still before any outcome.

## 1. Correction of a label (SCI's request)
- **What is SCI's:** the direction (each WOREE line above each SCAR12 line, four pairings) and the range (a pairwise ratio of about 1.5 to 8, SCI's own INFERENCE). SCI deliberately gives no distribution and has no defensible source for one.
- **What is mine:** every probability in the frozen sidecar. In particular `genotype_effect` = 0.05, 0.15, 0.70, 0.10 on the bins (below 1; 1 to 1.5; 1.5 to 8; 8 and above) is **an HE assumption, not SCI's forecast**, and so are the probabilities of `line_or_batch_effect` and `pooled_rule`. The sentence in the freeze file that calls `genotype_effect` "P-SCI-1 as SCI wrote it" is to be read as "SCI's direction and range with HE's numbers".
- **Why the 0.70 is too high:** SCI's prior is lower than when the forecast was written: week 7 shows the four lines within about 10 percent, and the pooled week-16 gap is confounded with AAV9-EGFP exposure from week 10.

## 2. A flatter sensitivity (labelled a sensitivity, not SCI's forecast)
`PSCI1_SIDECAR_SENSITIVITY_HE_20261121.tsv` (sha256 `cbf6469cb51b10d74627a9a153118ea515c1f3431228b120784e3dce90b18c12`) holds the three frozen forecasters unchanged plus `genotype_effect_flat_sensitivity` = 0.15, 0.25, 0.50, 0.10 on the same bins, for each of the four ids (`prospective_ledger_score.py check`: 4 ids, 4 forecasters, 64 bins). Use: score both sidecars when the table exists and report the two secondary log scores side by side; **neither changes the binding reading rule** (a reversed pairing refutes; all four in order is a tie; improvement unreachable; floor 1 in 6; unscorable when labels or denominators are missing).

## 3. Removal
Delete this addendum and the sensitivity sidecar; the freeze is untouched.
