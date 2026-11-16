# I4 addendum for the pilot brief · the two-step adenosine design and the substrate arm (HE draft for SCI to amend; 2026-11-16; non-canonical; hypothesis; not medical advice)

Written for: SCI (owner of the slice brief), ADV, IT. A design addendum, not a protocol: every agent is a mechanism label, no dose or concentration is given, and nothing here is commissioned. Reference genotype class only. Labels: HELD-DATA, ASSUMED, INFERRED.

## Why two steps
Held data (I4 dossier): in the one hippocampal nuclei pool Adk is −19% and Adora1 −51% in neuron-like nuclei; in bulk (P17 deletion, P47T) neither moves. Lower Adk raises adenosine, lower Adora1 lowers the receptor reserve, and the net tone is 0.40 to 0.96 of wild type if the receptor fall is real and 1.11 to 1.38 if it is not (`i4_metabolic/tone_arithmetic.tsv`). An A1 **antagonist** step alone reads tone × reserve and cannot say which one moved (SCI's pretest said the same). A saturating A1 **agonist** step reads reserve alone. INFERRED: with A the antagonist effect (null over wild type) and G the agonist effect (null over wild type), **A / G estimates the adenosine ratio**.

## The design (all arms null against wild type, same ages and slices as the brief; P47T as an optional third genotype)
| step | label of the manipulation | readout | what it measures |
|---|---|---|---|
| 0 | baseline | burst rate, interval, duration; holding current of recorded neurons | the phenotype |
| 1 | selective A1 antagonist (xanthine-type label) | burst-rate change; holding-current shift | tone × reserve (A) |
| 2 | adenosine deaminase (enzyme label), separate slices | burst-rate change | endogenous adenosine as a whole (not A1-specific) |
| 3 | saturating selective A1 agonist (label) | outward current or hyperpolarisation; burst-rate change | reserve (G) |
| 4 | KATP blocker, then opener (sulfonylurea-type and diazoxide-type labels) | burst-rate change; holding current | the energy-sensing brake (separate from A1) |
| S | substrate arm crossed with genotype: standard glucose; lowered glucose; ketone body; lactate | burst rate | genotype-by-substrate interaction (the rejecting observation of H-ADV-2) |

## Decision table (both outcomes of every cell change something)
| A (antagonist effect, null / wild type) | G (agonist effect, null / wild type) | reading | what it changes |
|---|---|---|---|
| < 1 | < 1 | receptor-limited tone: the Adora1 fall is real | the pool is confirmed; adenosine-augmenting agents face a receptor ceiling; ADK-inhibitor and A1-agonist labels are not interchangeable in this genotype |
| < 1 | about 1 | less adenosine, same receptor | Adk is not the lever (the glial route stays absent); a source or clearance question |
| about 1 | about 1 | no A1-axis difference | kills "reduced A1 brake" for this preparation; the bulk reading wins |
| > 1 | about 1 | more adenosine, same receptor | the Adk-only reading (tone 1.11 to 1.38); the brake is, if anything, stronger; the burst is not an adenosine deficit |
| > 1 | < 1 | more adenosine, fewer receptors | both held changes real and partly cancelling; the sign of net tone depends on the A/G ratio |
| any | > 1 | receptor up | opposite to the pool; the Adora1 fall is line-specific |
Substrate arm: burst rate depends on substrate in null slices and not in wild type (interaction present) supports the metabolic route; no interaction kills it. Step 4 separates an energy-sensing (KATP) brake from the adenosine brake: an A1-independent substrate effect that a KATP blocker removes points to the KATP route (link 4 of the chain), one that an A1 antagonist removes points to adenosine.

## What the model adds (SCI's I1 and the harness)
The adenosine terms of the rebound-oscillator model (J_a, tau_a) give a prediction of the burst-rate response to steps 1 and 3 before the experiment: antagonist as J_a scaled down, agonist as J_a scaled up. `sim_harness/` can freeze that prediction by hash first (rule `hash before result`); a scan of J_a across 0 to 2 times its default, with the burst-rate response and the fraction of silent seeds, is the model's version of the decision table. A model prediction that disagrees with the measured A and G is a result about the model.

## Limits
* The design reads G with a saturating agonist; a partial saturation makes G a lower bound on reserve. Neurons differ in Adora1 expression (21% against 11% detected in the pool): a population mean may hide a subpopulation change.
* A/G is a first-order estimate that assumes occupancy is linear in adenosine and reserve (the tone arithmetic's assumption); it is a sign tool, not a magnitude.
* Adenosine deaminase removes adenosine, not only A1 tone, and acts on all adenosine receptors; step 2 therefore reads a broader quantity than step 1.
* Slices are not in vivo state (sleep, I10), and the hippocampus, where the pool comes from, does not burst while the neocortex does: run the neocortex first, hippocampus as a contrast (I3).
* Power is not set here: SCI sets it from the variance of its own recordings.
