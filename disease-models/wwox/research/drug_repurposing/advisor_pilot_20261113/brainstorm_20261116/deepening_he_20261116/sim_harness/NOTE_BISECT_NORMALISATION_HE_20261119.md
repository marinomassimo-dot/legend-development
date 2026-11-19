# Dated note beside the frozen bisect result: the class order in strength s is partly imposed by the listed multipliers (HE, 2026-11-19)

Written for: ADV, SCI, IT. Hypothesis level; weights, not concentrations; reference genotype class only; no dose; not medical advice. The folder `runs_20261116/bisect/` is frozen and is **not edited**; this note sits beside it. Raised by ADV (ADV-096, 2026-11-19), verified here from `runs_20261116/bisect/model_files/pilot_bisect_harness_model.py` and `runs_20261116/bisect/summary.tsv`. No new simulation was run: the table is arithmetic on the published crossing strengths.

## The point
Each arm perturbs its parameter by `factor = multiplier ** s`, with a **different listed multiplier per arm** (d-APV J_N x0.3; NMDAR pore blocker J_N x0.8; AMPA J_A x0.8; T-type J_T x0.75; synaptic GABA-A J_I x1.2; neurosteroid-type J_tonic x1.2 together with J_I x1.1; sodium, pyramidal sigma x0.9). The crossing strength s therefore compares arms on different scales. The scale-free quantity is the **crossing multiplier**: the fractional change of the targeted parameter at which the median burst count falls below half. The bracket in the last column is the final bisection bracket (width 0.047 in s) mapped through the same arithmetic.

## S-KO, crossing multiplier (rel_bursts below 0.5)
| class | published crossing s | parameter and crossing multiplier (bracket) |
|---|---|---|
| d-APV-type | 0.164 | J_N x0.821, -18% (0.844 to 0.798) |
| NMDAR pore | 0.914 | J_N x0.815, -18% (0.820 to 0.811) |
| AMPA | 1.430 | J_A x0.727, -27% (0.731 to 0.723) |
| T-type | not within [0, 3] | J_T would need more than -58% (x0.42 at s = 3) |
| synaptic GABA-A | 1.711 | J_I x1.366, +37% (1.360 to 1.372) |
| neurosteroid-type | 0.539 | J_tonic x1.103 (+10%) **and** J_I x1.053 (+5%) together |
| sodium, pyramidal | 1.102 | sigma x0.890, -11% (0.893 to 0.888) |

S-HT, same arithmetic: d-APV J_N -8% (bracket x0.945 to x0.893), NMDAR pore J_N -9% (x0.920 to x0.910), AMPA J_A -12%, T-type J_T -55%, synaptic GABA-A J_I +8%, neurosteroid-type J_tonic +5% with J_I +2%, sodium sigma -5%.

## What follows (and what does not)
1. **d-APV and the NMDAR pore blocker are the same perturbation of the same parameter** (J_N). On the scale-free axis they tie at S-KO (-18% and -18%, the brackets overlap) and at S-HT (-8% and -9%). "d-APV before NMDAR pore" in the published order, and prediction P1 as registered ("d-APV < neurosteroid-type < NMDAR pore < sodium < AMPA < synaptic GABA-A < T-type"), is therefore **imposed by the listed coefficients (0.3 against 0.8), not found**. The 8 of 9 pass must be read with this caveat; the P1 pass does not support a superiority of d-APV over the pore blocker.
2. **Comparisons across different parameters** (J_N against J_A, J_I, J_T, sigma) are scale-free in the multiplier but depend on the model's own sensitivity to each parameter and on what each parameter stands for; a fractional change is not a comparable pharmacological action across targets. The multiplier scale does not say which class is better, only how large a parameter change the model needs. On it, sodium (-11%) and the neurosteroid-type composite (+10% and +5%) need smaller changes than the NMDAR classes (-18%), AMPA (-27%), synaptic GABA-A (+37%), and T-type needs more than -58%. So the first and third places of the published order move: sodium passes the NMDAR classes on this axis.
2b. **The metric itself is a choice.** Ordering by the log of the multiplier (symmetric for a decrease and an increase) puts synaptic GABA-A (+37%, ln 0.312) just before AMPA (-27%, ln 0.319); ordering by percent change puts AMPA first. Their relative order is metric-dependent and is not read.
3. **The neurosteroid-type arm is composite**: two parameters move together at the fixed ratio 1.2 to 1.1, and its crossing depends on that ratio, which is a chosen normalisation. Same for arms 3 and 9.
4. **The stability of an order that the coefficients impose is not superiority of a class.** A wrapper that reports the rank of each class across parameter variants must report it on the multiplier scale, and mark the comparisons that depend on the listed coefficients.
5. Caveats unchanged: 5 seeds, 6 halvings; the T-type crossing is outside the bracket at S-KO; Kv7 is not in the model; crossing strength is a model step, not a dose.
