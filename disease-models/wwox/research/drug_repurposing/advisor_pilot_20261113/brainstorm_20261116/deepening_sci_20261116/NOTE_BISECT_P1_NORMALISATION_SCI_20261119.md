# Dated note beside the frozen bisect scoring: which registered comparisons depend on the per-arm multipliers (SCI, 2026-11-19; MODEL: a hypothesis generator, not evidence; weights, not concentrations; no dose; reference genotype class only; not medical advice)

Written for: ADV, HE, IT. Raised by ADV (ADV-096, operator direction 22:19Z, point 1); the arithmetic is HE's `NOTE_BISECT_NORMALISATION_HE_20261119.md` in `deepening_he_20261116/sim_harness/`, which I verified against the frozen `SCORE_PILOT_BISECTION_SCI.md` (this folder). **The frozen files are not edited:** `SCORE_PILOT_BISECTION_SCI.md` (scored 8 of 9, written 2026-11-17) and `TRANSFER_QUALIFICATION_SCI_20261117.tsv` (rows R17a at lines 51, 52 and 65 carry "predictions P1-P4: 8 of 9 pass") stand as the registered scoring. This note is the dated line that belongs beside each of them, and the three sentences below are the form to use wherever those rows are quoted in short.

## Three sentences for any short form
1. The registered P1 order passes by construction of the listed multipliers (d-APV x0.3 against the NMDAR pore blocker x0.8 on the same parameter, which tie on the scale-free axis at about -18%), so cross-arm order is not evidence of class superiority.
2. Crossing strength is a model step, not a dose, and the multiplier scale says how large a parameter change the model needs, not which class is better.
3. HE's wrapper is parametric sensitivity of one structure plus a few joint scenarios, not a structural alternative (Kv7 is not in the model: an assumption).

## Which of my registered comparisons depend on the normalisation
| Registered statement | Depends on the listed multipliers? | Reading now |
|---|---|---|
| P1 (cross-arm order of crossing strength) | **Yes, entirely** | the PASS stands as a literal score and is not a result about classes; on the multiplier axis d-APV and the pore blocker tie and sodium (-11%) passes both NMDAR classes, so the registered order is not reproduced as an order of classes |
| P1b (T-type last, only above s = 2 or not within the bracket) | the numeric threshold yes, the ordering no | T-type needs more than -58% on J_T against at most +37% for any other class: last on the multiplier axis too; read as "largest parameter change needed", not "weakest class" |
| P2a, P2b (GluN2B modulator duration threshold at s of 1 and 1.5) | the numeric s thresholds yes (one arm, its own multiplier) | within-arm direction only (duration falls late); the threshold values are in coefficient units |
| P3a, P3b (sodium with an interneuron share: aggravation at S-HT, none at S-KO) | the numeric ranges yes, the direction no | the direction (aggravation at the near-threshold setting, not at S-KO) is a within-arm sign and survives; the 0.7 to 1.5 range was in coefficient units |
| P4a, P4b, P4c (S-HT crossing smaller than S-KO, same arm) | **No** | a ratio within one arm and one multiplier: unaffected; these three are the registered statements that survive the normalisation unchanged |
So I do not restate "8 of 9". What carries forward is: P4a to P4c, the direction of P3a and P3b, the within-arm direction of P2, and "T-type needs the largest change". Cells that use R17a only for a within-arm sign (IT verified C013, C015, C055) are unchanged.

## Consequences for how the model is used in the selection
* Comparisons between classes are made on the crossing multiplier, and only between biologically comparable perturbations or pharmacological profiles supported by data. A class mapped to a parameter is not a compound prediction.
* The simulated order may not replace the pharmacological comparison: for the broad objective the model has no role (no myelination, no development in it); for the bridge objective it supplies within-arm directions and the S-HT sensitivity, nothing about which real agent to prefer. The comparison of real agents is the target and exposure table (ADV-095 unit B) and the held pharmacology (ADV-050 kinetics, ADV-067 lithium regimen).
* The composite arms (neurosteroid-type with J_tonic and J_I at a fixed ratio 1.2 to 1.1) carry a chosen normalisation that is not a measured profile.
