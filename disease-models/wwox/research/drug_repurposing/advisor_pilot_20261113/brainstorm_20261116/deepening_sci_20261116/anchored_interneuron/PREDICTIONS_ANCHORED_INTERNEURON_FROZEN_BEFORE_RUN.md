# Anchoring the interneuron share of the mixed sodium arm in held numbers: mapping, assumptions, range, predictions, written and hashed BEFORE the run (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; weights, not concentrations; not medical advice)

Written for: ADV (assigned it), HE (runner of the earlier scan), IT. Context: my pilot-bisection prediction P3a (arm 9 at S-HT crosses rel_bursts 1.5 at s between 0.7 and 1.5) failed (observed 0.398), and E9 failed earlier in the same direction. The interneuron weight in arm 9 (J_I x0.7 per unit strength) was an assumption of mine; this file replaces it by a mapping from held numbers.

## Held numbers used (HELD: Breton 2021 Table 1 and the sIPSC data, `files/fulltext/PMID34634460_Breton2021_EPMC_2026-09-27.xml`)
* Interneuron AP amplitude 60.78 mV (S-WT and S-HT) against 45.03 mV (S-KO): a fall of **25.9%**; 5 and 6 cells; resting potential unchanged (-67.1 against -71.5 mV, ns).
* Pyramidal AP amplitude 76.3 mV (S-WT) against 68.7 mV (S-KO): a fall of **10.0%**.
* sIPSC amplitude 57.3 pA (S-CTL) against 27.5 pA (S-KO): a fall of **52.0%** (aggregated; the held sIPSC data do not reconstruct the heterozygote).
* The ratio of the KO's interneuron to pyramidal AP-amplitude fall: **r = 2.6**. The ratio of the sIPSC fall to the interneuron AP-amplitude fall: **k = 2.0** (an upper value: it attributes the whole sIPSC fall to the presynaptic spike).

## Mapping (ASSUMED steps are marked)
1. A sodium-class agent lowers AP amplitude in both classes. Pyramidal side: arm 8 and arm 9 keep sigma x0.9 per unit strength, read as 'a 10% pyramidal AP-amplitude fall at s = 1' (ASSUMED equivalence; it is the size of the KO's own pyramidal fall, which makes s = 1 interpretable as 'one KO-sized pyramidal deficit').
2. Interneuron side: the agent lowers interneuron AP amplitude by a fraction a_I = r x 0.10 at s = 1, where r is the ratio of interneuron to pyramidal block (r = 1: equal fractional block; r = 2.6: the ratio the KO itself shows).
3. Coupling: phasic output J_I falls by a factor 1 - k x a_I at s = 1 (k = 1: proportional; k = 2: the held sIPSC-to-spike ratio), and the factor is raised to the power s as in the earlier arms (ASSUMED proportionality between presynaptic AP amplitude and the weight; release probability is steeper in general physiology, ASSUMED, so k = 2 is not an extreme).
4. Four variants: arm 91 (r 1, k 1): J_I factor 0.90; arm 92 (r 1, k 2): 0.80; arm 93 (r 2.6, k 1): 0.74; arm 94 (r 2.6, k 2): 0.48. The earlier assumed 0.7 is close to arm 93. **Central anchored arm: arm 93** (the KO's own class ratio, proportional coupling).
5. Non-identifiable: the ratio r for a real agent (the held ratio is the KO's pathology, not a drug's selectivity), the coupling k, the sigma-to-amplitude equivalence. The scan over four variants shows how the result depends on them; the held numbers fix the range, not the value.

## Configuration frozen (harness freeze, sha256 of freeze.json)
64f395491e99cdc69f5647da190c8a766587ee33719ff2a5e42b23c459b68878; adapter `pilot_bisect_anchor_model.py` (arms 1 to 9 unchanged; arms 91 to 94 added); frozen model `rebound_oscillator.py` sha256 c050b8ff0a1ba8fe...; 8 cells (arms 91 to 94 at S-HT crossing 1.5 above, at S-KO crossing 0.7 below), bracket [0, 3], 6 halvings, 5 seeds, base seed 1000. The reference run of arm 9 (J_I x0.7) is HE's earlier scan (S-HT 0.398, S-KO 1.898), not re-run.

## Predictions (mechanical forms are in the frozen scan; E9 is checked by `e9_anchor.py`)
Q1 S-HT crossing order, smallest first: arm 94 < arm 93 < arm 92 < arm 91 (not-in-bracket = +infinity). Q2 arm 93 at S-HT between 0.3 and 0.7 (**the miss stays**). Q3 arm 94 at S-HT below 0.3. Q4 arm 92 at S-HT between 0.5 and 1.2. Q5 arm 91 at S-HT above 1.0 or not within the bracket. Q6 arm 94 at S-KO above 1.0 (rel_bursts stays above 0.7 for s up to 1). Q7 arm 91 at S-KO crosses below 0.7 earlier than arm 94.
E9 re-check at s = 1 (`e9_anchor.py`): S-KO median rel_bursts between 0.7 and 1.3 for arms 91 to 93; S-HT incidence change below 0.10 in absolute value for arm 91 and **at or above 0.10 for arms 93 and 94** (E9 fails again for the central and the strong variants); arm 92 between 0.05 and 0.20.
**How the three outcomes are decided (fixed now), on the central arm 93:** the miss 'goes away' if the S-HT crossing falls in [0.7, 1.5]; 'shrinks' if it lies between 0.5 and 0.7; 'stays' if below 0.5. Across arms: the miss 'depends on the assumption' if arms 91 and 92 land inside [0.7, 1.5] and arms 93 and 94 below.
**Output statement to be written whatever the result (model-conditional, held anchor):** the interneuron AP-amplitude fall at which S-HT bursts first exceed 1.5 times baseline, a_I* = 0.10 x r x s*, reported as a fraction of the KO's own 25.9% deficit, for each variant (the held anchor, not a free weight).
## Limits
Weights, not concentrations; one oscillator, frozen, fitted on held numbers; S-HT counts are small (about 10 bursts per 40 slices), 5 seeds; the phasic position 0.9 of S-HT is ASSUMED; a real agent's class selectivity is unknown. The test is not independent of my first miss in the sense that the central arm is near the old assumption: Q2 predicts exactly that the miss stays, which is a prediction the model could fail.
