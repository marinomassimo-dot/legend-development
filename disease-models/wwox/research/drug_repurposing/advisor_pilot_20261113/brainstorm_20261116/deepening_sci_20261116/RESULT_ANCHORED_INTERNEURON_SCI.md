# Result: the interneuron share of the mixed sodium arm anchored in held numbers (SCI, 2026-11-17; non-canonical; MODEL: hypothesis generator, not evidence; weights, not concentrations; not medical advice)

Written for: ADV (assigned it), HE, IT. Files: `anchored_interneuron/` (predictions file, adapter, scan, frozen run folder `run/` with `summary.tsv`, `results.tsv`, `predictions_scored.tsv`, `e9_anchor.py` and `e9_result.tsv`). Mapping, assumptions and range are in `PREDICTIONS_ANCHORED_INTERNEURON_FROZEN_BEFORE_RUN.md` (sha256 7d3287e67076f16541bea2038c0ca4990b830489fcec5f0c0912f81b2ef9054a); held numbers from Breton 2021 Table 1 and the sIPSC data (HELD).

## Order of record
Digests (freeze.json 64f39549..., predictions 7d3287e6..., adapter 47cc126f..., scan 2b42d209..., e9_anchor 5a09c1b4...) were sent to ADV by cross-session message before the run command; files written 01:10:54Z to 01:11:19Z; run start **01:11:36Z** (`date -u`, `run_start.txt`; load average 2.02 at start, 2.4 to 3.6 later, three workers plus another session's gate; timing only); scan finished 01:36:33Z (run hash f0ff0f8c66be48780f60b3d17e2fdf00b58c58ee6ccc36acc5558b25dcd49da7, 220 rows); E9 check finished 01:52Z. ADV's recorded receipt: 'at 01:11Z or just before'; my own label '01:2xZ' in the digest message was an estimate and wrong. The order rests on the message having been sent before the run command in my own sequence; I cannot prove it to the second. No result had been seen when the predictions were fixed.

## Answer first
1. **Does the P3a miss go away, shrink or stay?** On the central anchored arm (arm 93: the KO's own interneuron-to-pyramidal ratio r = 2.6, proportional coupling k = 1, J_I factor 0.74) the S-HT crossing of rel_bursts above 1.5 is at **s = 0.539**: against my original 0.7 to 1.5 and the earlier arm-9 value of 0.398. By the outcome rule fixed beforehand (in [0.7, 1.5] goes away; 0.5 to 0.7 shrinks; below 0.5 stays) this is **'shrinks'** (it also satisfies Q2, which I wrote with a wider 0.3 to 0.7 band and the words 'the miss stays': the two statements in my file were not consistent with each other; the numeric band passes, the decision rule says 'shrinks', and both say the crossing is below 0.7: the miss is not removed).
2. **It depends on the assumed ratio, and the held numbers do not fix it.** Crossings at S-HT: arm 94 (r 2.6, k 2; J_I factor 0.48) **0.117**; arm 93 **0.539**; arm 92 (r 1, k 2; 0.80) **not within [0, 3]**; arm 91 (r 1, k 1; 0.90) **not within [0, 3]**. With an equal fractional block of interneurons and pyramids (r = 1) there is **no aggravation at S-HT up to s = 3**; with the KO's own class ratio (r = 2.6) there is, at s between 0.12 and 0.54. In terms of the ratio of the log of the J_I factor to the log of the sigma factor: arm 91 1.0 and arm 92 2.1 (no crossing), arm 93 2.9 (0.54), the earlier arm 9 3.4 (0.40), arm 94 7.0 (0.12): the crossing appears between about 2.1 and 2.9 and moves earlier as the ratio grows.
3. **Model-conditional statement with a held anchor (the requested output).** A sodium-class agent whose interneuron effect is as strong, relative to its pyramidal effect, as the KO's own AP-amplitude pattern (interneuron fall 25.9% against pyramidal 10.0%, r = 2.6) raises S-HT bursts above 1.5 times baseline when the interneuron AP amplitude has fallen by **a_I\* = 0.10 x r x s\*: 14.0% (arm 93) or 3.0% (arm 94), that is 54% or 12% of the KO's own 25.9% interneuron deficit**, while the pyramidal side has fallen by about 5% or 1%. An agent that blocks both classes equally shows no such aggravation in the model. So aggravation by a mixed arm near threshold is a statement about class selectivity: the held numbers say how large the interneuron effect has to be (a fraction of the KO's deficit) and not whether any agent has that selectivity.
4. **The S-KO side** (unchanged in direction): arm 91 crosses below 0.7 at 0.82, arm 92 at 1.24, arm 93 at 1.66, arm 94 at 2.84: the larger the interneuron factor the later the suppression at S-KO.

## Scoring of the registered predictions (literal)
| id | statement | observed | verdict |
|---|---|---|---|
| Q1 | S-HT crossing order 94 < 93 < 92 < 91 | 0.117 < 0.539 < not in bracket = not in bracket | FAIL (arms 91 and 92 both not in bracket: a tie, not a strict order; the part 94 < 93 < the other two holds) |
| Q2 | arm 93 at S-HT between 0.3 and 0.7 | 0.539 | PASS |
| Q3 | arm 94 at S-HT below 0.3 | 0.117 | PASS |
| Q4 | arm 92 at S-HT between 0.5 and 1.2 | not in bracket | FAIL |
| Q5 | arm 91 at S-HT above 1.0 or not in bracket | not in bracket | PASS |
| Q6 | arm 94 at S-KO above 1.0 | 2.84 | PASS |
| Q7 | S-KO crossing: arm 91 earlier than arm 94 | 0.82 < 2.84 | PASS |
So 5 of 7 pass; the two failures are the same error: I expected the equal-block variant with coupling 2 (arm 92) to aggravate inside my old range, and it does not aggravate at all.

**E9 re-check at s = 1 (`e9_result.tsv`, 5 seeds, same adapter):**
| arm | S-KO median rel_bursts | S-HT median rel_bursts | S-HT incidence change |
|---|---|---|---|
| 91 | 0.645 | 0.533 | -0.110 |
| 92 | 0.766 | 1.154 | +0.020 |
| 93 | 0.833 | 1.867 | +0.095 |
| 94 | 1.169 | 10.667 | +0.570 |
| 9 (earlier, J_I 0.7) | 0.888 | 2.533 | +0.155 |
| 8 (pyramidal only) | 0.529 | 0.154 | -0.185 |
Registered: S-KO within 0.7 to 1.3 for arms 91 to 93 (arm 92 and 93 yes, **arm 91 no, 0.645**); S-HT incidence change below 0.10 in absolute value for arm 91 (**no: -0.110**, arm 91 is a suppressor at S-HT); at or above 0.10 for arms 93 and 94 (**arm 93 no, +0.095, five thousandths short; arm 94 yes**); arm 92 between 0.05 and 0.20 (**no, +0.020**). 3 of 7 sub-statements pass. At s = 1 the S-HT burst count rises for arms 92, 93, 94 and 9 and falls for 91 and 8; the incidence moves by more than 0.10 only for arm 94 and arm 9 (up) and arms 91 and 8 (down).

## What this does and does not say
* The earlier miss is **not an artefact of one free weight**: with the weight rebuilt from held numbers at the KO's own class ratio, the central arm still aggravates at S-HT at about 0.54 (and earlier with a steeper coupling); only an equal-block agent does not aggravate. The model's S-HT sensitivity to interneuron share is therefore a structural property of the near-threshold setting once the ratio is KO-like, and the ratio is the unmeasured quantity.
* The held numbers anchor **how much interneuron effect is needed** (3 to 14 percent AP-amplitude fall, 12 to 54 percent of the KO's deficit), **not the selectivity of any agent**; r = 2.6 is the KO's pathology, not a drug property, and k = 1 to 2 is bounded above by the held sIPSC-to-spike ratio (the pre/post origin of the deficit, brief section 13.7, would bound k: k about 2 x (1 - rho_m)).
* Weights, not concentrations; one frozen oscillator fitted on held numbers; the phasic position 0.9 of S-HT assumed; S-HT counts are small (about 10 bursts per 40 slices) and five seeds were used, so the crossing values are not sharp; the sigma-to-amplitude equivalence (sigma x0.9 = a 10% fall) is assumed.

## What it changes
* Pilot arm 9 and the sodium arms: the S-HT expectation of the mixed sodium arm is an increase of bursts whenever the agent's interneuron effect exceeds the pyramidal effect by a factor of about 2.5 in log terms; a pyramidal-preferring or equal-block agent is expected to suppress or leave S-HT unchanged. No agent or dose is recommended.
* Engine record: second consecutive miss on the same quantity, now with a held anchor and with the cause located (a free ratio) rather than a miss unexplained.

## Not done
No re-fit; no scan over r between 1 and 2.6 (the transition between about 2.1 and 2.9 in log ratio is bracketed by four variants only); no new bisection with a corrected expectation.
