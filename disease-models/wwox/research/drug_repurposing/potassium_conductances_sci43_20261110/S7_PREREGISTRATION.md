# SCI43 S7 — fixed before the run: uncertainty of the implied reversal from printed means

Written and committed **before** `implied_reversal_mc.py` is run. Non-canonical; INFERENZA about published summary statistics; not medical advice.

**What is disclosed first.** The point values of `output/implied_reversal_points.tsv` were computed by the Orchestrator before this file was written, so they were seen. What was **not** seen is any uncertainty: the Monte Carlo below carries the printed dispersions. The predictions below are about that interval, and some were guided by the point values (stated per row).

**Question.** Does the pair (Rin, rest) printed for the Wwox WT, HT and KO neurons constrain the reversal potential of the net conductance change tightly enough to tell a K+-type loss (reversal near E_K on the recorded scale) from a maturation-type change (reversal about -72 to -79 mV on the same kind of scale), and does the same arithmetic work on known cases?

**Method (fixed).** For each case draw Rin_old, Rin_new, V_old, V_new independently from normal distributions with the printed mean and standard error (200,000 draws, seed 43); discard draws with a non-positive resistance; E_x = V_old + (V_new − V_old)·G_new/(G_new − G_old), G = 1000/Rin. Report median, 2.5 and 97.5 percent, P(E_x ≤ −85), P(E_x ≥ −80) and, for each assumed junction offset δ in {0, 8, 13, 16} mV (recorded = true + δ, E_K true −97.5 mV for the Wwox solutions), whether the 95 percent interval contains E_K on the recorded scale. Inputs and their standard errors (the Wwox "±" is read as SEM, which the verifier checks; the Fmr1 Rin "±" is a 95 percent CI, converted by /1.96; the Fmr1 rest change has p = 0.0457, so SE(ΔV) = 3.7/2.0 = 1.85 mV applied to V_new with V_old fixed). Cells are treated as units, as in the sources: the interval is therefore narrower than a per-animal analysis would give, and this is a limit, not a result.

**Predictions (fixed now).**
* P1 (not guided by a computed interval; the point value −91.6 was seen): Fmr1 calibration. The 95 percent interval contains the measured Ba2+ reversal −89.6 mV and the median lies within 10 mV of it. If not, the method has no resolution at this size of change and nothing below is read.
* P2 (the point value −73.7 was seen): Kcnq2 cKO (ΔV +1.6 mV, p 0.2). The 95 percent interval is wider than 40 mV, so the case is uninformative.
* P3 (guided by the point value −93.7): Wwox KO. The median is more negative than −85, the 95 percent interval is wider than 25 mV and **contains the maturation values**; P(E_x ≥ −80) lies between 0.10 and 0.40. Therefore the verdict "K+-type loss rather than maturation" is at most **suggestive**.
* P4 (guided by −88.8): Wwox HT. Wider than KO (smaller ΔV); P(E_x ≥ −80) between 0.20 and 0.50.
* P5: developmental rows (P7→P14 and P14→P28, L3): the median lies between −85 and −65 mV (not K-like).

**Rule for the word to use.** informative: P(E_x ≥ −80 | KO) < 0.05; suggestive: < 0.25; uninformative: otherwise. The word is applied as the run gives it, including if it contradicts the predictions, which are then reported as failed.

**What this cannot do.** It assumes a single changed conductance, a steady state, no shunt, a common junction offset in the compared preparations (the maturation values come from a different area, layer, temperature and internal solution), cells as independent units, and that the printed dispersions are SEM. It cannot say that the change is pathogenic or compensatory, and it does not identify a channel.
