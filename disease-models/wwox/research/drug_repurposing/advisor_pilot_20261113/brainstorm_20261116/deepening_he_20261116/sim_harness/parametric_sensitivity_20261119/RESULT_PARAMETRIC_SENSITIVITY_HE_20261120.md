# ADV-096 result: parametric sensitivity of the simulated bisect crossings (HE, 2026-11-20)

Written for: ADV, SCI, IT. Hypothesis generator, not evidence; not medical advice; reference genotype class only; no dose. **This is a sensitivity analysis of the same equations under other parameter values. It is not a validation on alternative biological structures, and a technical reproduction of the baseline does not show biological validity.** Kv7 is not in the model: the `kv7_offset` variants use an ASSUMED stand-in (a drive offset), not a current. The final bisection brackets are numerical resolutions, not confidence intervals. "No crossing within [0, 3]" means no crossing in the explored range, not that no effect is possible. No class is ranked, no rank correlation is computed, no winner is named; the full per-variant text is in `RESULT_REPORT_STAGE2_raw_20261120.txt`.

## 1. Inputs and versions
- Model: SCI's frozen `rebound_oscillator.py` (sha256 prefix c050b8ff0a1b) and the frozen bisect adapter `pilot_bisect_harness_model.py` (2871a5dbfdf1), both copied unchanged from the published bisect folder (`cmp` identical); wrapper `parametric_sensitivity_model.py` (9c587ab5ae40) multiplies four of the oscillator's own BASE parameters (J_I, tau_c, J_N) or offsets the drive b0 (the Kv7 stand-in), restoring them after each call; at defaults the wrapper is bit-identical to the frozen adapter (three test points, then the baseline run).
- Harness: `sim_harness.py` v1 (sha256 prefix 15c0d27fbf59), **unchanged**; the study uses its own `fixed` block per bisect cell. Python 3.12.3, numpy 2.5.3.
- Freezes: baseline stage `runs/baseline` freeze 6c638de9...f0c8; main stage `runs/rest` freeze **c196229aa99fcd5153d9af97f6fc4f7d7f58de67e4ed3a3f374d77f0849b7493**, scan `scan_rest.json` frozen before the run; seeds 1000 to 1002 (3), base seed 1000, bisection on strength s in [0, 3] with 5 halvings (resolution 0.094 in s), S-KO setting only, observable rel_bursts, threshold 0.5. The published bisect used 5 seeds and 6 halvings.
- Results digests: `runs/rest/results.tsv` e96dde0f83c5...ee5, `summary.tsv` c1f086a8ef2e...49d; `runs/baseline/summary.tsv` 58ce2c116f20...2d1.

## 2. Coverage and limits of the computation
- **Counts reconciled.** 84 cells in total = **7 baseline cells** (runs/baseline: the baseline variant, 7 classes, 111 bisection calls) + **77 continuation cells** (runs/rest: 11 variants x 7 classes, 1,206 calls of a maximum 1,386). The 77 are the continuation, not the total. Variants: the baseline; ji_mult, cl_tau_mult, nmda_mult and kv7_offset each at a low and a high value (8); three joint scenarios chosen for biological meaning: high chloride load with low inhibitory share, a hyperexcitable circuit (high NMDAR gain with a depolarising offset), and an inhibited circuit (low NMDAR gain, hyperpolarising offset, fast chloride extrusion).
- **No missing cell, no error:** the job exit file reads 0; `summary.tsv` has 77 rows; `check` on `joint_inhibited__arm5` re-ran 18 rows byte-identical. 71 of 84 cells crossed; 13 had no crossing in [0, 3].
- **Resources:** job `ps-rest2` ran from 22:43:49Z to before 01:50Z under the 3 GB scope at 2 workers; memory available stayed about 10 GB, swap 2.3 of 4 GB, memory pressure low, load 3 to 4; nothing else was added. One earlier start of the same freeze was stopped by my own mistake (I deleted its output folder) and restarted at 22:43:49Z with the identical freeze digest; the stopped start produced no output.
- **Not run:** the S-HT setting; arms 3 and 9; any variant beyond the 11; structural alternatives (a different circuit element), a Kv7 current, a second interneuron class. The grid was not extended to recover a conclusion.

## 3. Results (per class, as read from `RESULT_REPORT_STAGE2_raw_20261120.txt`)
Crossing multiplier = the fractional change of the targeted parameter at which the median burst count halves; "same class" comparisons use the same arm and coefficient, so they are scale-free; brackets are resolution.

| class | baseline crossing (multiplier) | across the 11 variants: indistinguishable / needs larger / needs smaller change / no crossing in [0,3] | multiplier range where it crossed |
|---|---|---|---|
| d-APV-type (J_N) | x0.844 | 8 / 3 / 0 / 0 | x0.844 to x0.602 |
| NMDAR pore (J_N) | x0.820 | 3 / 5 / 3 / 0 | x0.873 to x0.612 |
| AMPA (J_A) | x0.723 | 1 / 4 / 4 / 2 | x0.837 to x0.517 |
| T-type (J_T) | no crossing | baseline none, so not measurable in 4 variants where it crossed (x0.62 to x0.44); no crossing in 7 | x0.624 to x0.439 |
| synaptic GABA-A (J_I) | x1.372 | 1 / 3 / 4 / 3 | x1.176 to x1.656 |
| neurosteroid-type (J_tonic with J_I, fixed ratio 1.2 to 1.1) | x1.099 and x1.050 | 6 / 5 / 0 / 0 | J_tonic x1.080 to x1.217 |
| sodium (sigma) | x0.893 | 1 / 6 / 4 / 0 | x0.947 to x0.740 |

Direction of the shifts follows what the parameters mean in the equations: variants that raise excitability (depolarising offset, high NMDAR gain, low inhibitory share, the hyperexcitable and high-chloride joint scenarios) need a larger parameter change for the suppressive classes, and variants that lower it need a smaller one. That is the model's own sensitivity, not a claim about biology. In the two excitable joint scenarios AMPA, T-type and synaptic GABA-A do not cross within [0, 3].

## 4. Identifiable and not identifiable comparisons
- **Identifiable:** (a) the same class across variants (above); (b) **d-APV and the NMDAR pore blocker, which the model represents as the same perturbation of J_N, are indistinguishable on the multiplier scale in all 12 variants** (baseline and the 11 others; the brackets overlap every time: for example 0.798 to 0.893 against 0.811 to 0.828 at baseline, 0.569 to 0.637 against 0.605 to 0.618 in the hyperexcitable scenario). The published "d-APV before pore blocker" order is not a finding under any variant.
- **Not identifiable here:** any order or superiority between classes that act on different parameters (J_N, J_A, J_T, J_I, sigma); the multipliers describe the model's sensitivity to each parameter, not pharmacological potency. The model does not represent what the data sheets show to matter for real agents: the voltage dependence of pore block (30 to 100 times between -60 and -40 mV in one document), competitive against uncompetitive action, and kinetics. A composite arm (neurosteroid-type) depends on its fixed ratio of actions.

## 5. Variability, resolution and sensitivity to the assumptions, kept apart
- **Numerical resolution:** 0.094 in s per cell (the last bracket), identical for all cells; a difference between two cells smaller than this is not read.
- **Seed variability:** with 3 seeds the crossing decision rests on the median; in **49 of the 71 crossing cells at least one bracket end had fewer than 3 of 3 seeds on the same side of 0.5**. Seed variability is therefore not small compared with the resolution; 3 seeds cannot support a finer reading than the bracket and the seed counts printed beside each cell.
- **Sensitivity to the assumptions:** the class-by-variant shifts beyond both the bracket (numbers in section 3). They are not read as the shift's size with an interval.
- **The variants are not re-fitted to the held baseline.** The baseline burst count of each variant, as a multiple of the baseline variant: 2.10x, 0.70x (chloride extrusion slower, faster); 0.36x, 1.68x (inhibitory share higher, lower); 1.59x, 0.47x (NMDAR gain higher, lower); 2.58x, 0.23x (the Kv7 stand-in depolarising, hyperpolarising); 2.91x (high chloride, low inhibition); 3.05x (hyperexcitable); **0.06x (inhibited: 47 bursts per 40 slices, nearly silent)**. Where a multiple is far from 1 the variant is a different circuit state, not a perturbation of the fitted one, and its rows are read with that in mind.

## 6. Which conclusions change, and what the model cannot resolve
- **Changes:** (1) a statement of the form "class X needs a change of size m" is conditional on the circuit state: the NMDAR-pore crossing multiplier ranges from x0.87 to x0.61, AMPA from x0.84 to x0.52 (and fails to cross in two states), sodium from x0.95 to x0.74, within the explored parameter changes; (2) "T-type needs more than a 58 percent reduction of J_T" is an explored-range statement: in four lower-excitability states it crosses at x0.62 to x0.44; (3) the neurosteroid-type composite crossing stays within J_tonic x1.08 to x1.22 across all 11 variants, the narrowest range of the seven, which describes this model's sensitivity and is not evidence for the class.
- **Does not change:** the J_N pair equivalence; that the baseline reproduces the published bisect within resolution (7 of 7 classes, technical only).
- **Cannot be resolved by this model:** a ranking of classes across parameters; the effect of a real agent at any exposure (no mapping was built: the public potency data are assay- and potential-dependent, and the model has no representation of the dependence that decides them); any alternative biological structure; the seed-level variability below the bracket.

## 7. Interpretations to correct in consumers
1. "8 of 9 predictions pass" and prediction P1 (class order in s): read only with the normalisation caveat; the order between d-APV and the pore blocker is two labels of one parameter (note beside the frozen bisect; confirmed here under 12 variants).
2. Any text that calls the simulated class order "robust" or "stable across structures": this study did not test structures and did not rank; it shows within-class sensitivity to parameters.
3. Any ordering of classes by percent change of different parameters: not supported.
4. A class "last" or "inactive" because it did not cross: an explored-range result.
5. Any use of the neurosteroid-type crossing as a preference: composite arm, fixed ratio, model sensitivity.

## 8. Useful follow-up (one, proportionate)
None for the class choice: the simulator should not absorb the search, and extending the grid would not make a cross-parameter comparison identifiable. If a mapping from a class to an exposure is ever attempted, it needs SCI's per-agent potency under a stated holding potential and agonist condition first; the sheets show that these do not exist for most agents.

## 9. SHAs and scope of the checks (separate from the final SHA)
- Scan freeze `c196229aa99f...` (the computation); baseline freeze `6c638de9...`.
- Checks on the computation: freeze digest verified at run start by the harness (`--expect-freeze-sha256`); `check` byte-identical on `joint_inhibited__arm5` (18 rows); the report tests 10 OK on the code that wrote the text (the code was edited only to add the baseline-burst line and its test after the run; the data files were untouched); the previous landing of the stage-1 files passed the publication gate at c8180d6fb.
- The commit and landing SHA of this report is reported in the message that delivers it; the report text itself carries no later SHA.
