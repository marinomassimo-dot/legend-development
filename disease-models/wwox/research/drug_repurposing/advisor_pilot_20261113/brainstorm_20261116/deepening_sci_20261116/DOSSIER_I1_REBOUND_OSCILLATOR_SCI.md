# I1 TWO-STAGE REBOUND OSCILLATOR (dossier v1, SCI, 2026-11-16; hypothesis, not a finding; mechanism-level, no dose, no recommendation; not medical advice; reference genotype class only)

Written for: ADV (cross-reading and the unified model), IT (second reader, attack it), HE (harness freeze), the operator (the first block is the five-minute reading). Labels: KNOWN (source), HELD (table or full text in the repository), ASSUMED, INFERRED, MODEL (an output of the script, which is a hypothesis generator, not evidence).

## Answer first
* **What I built.** A stochastic mean-field network, `rebound_oscillator.py` (numpy only, seeded, 6 slow or fast state variables plus noise), with the parts the idea names: a T-type-like rebound trigger that recovers slowly after a burst, an NMDAR-dependent sustainer, and slow variables for chloride, adenosine and synaptic resource. I fitted 15 parameters by a seeded random search to the held Breton 2021 baseline and checked it with a 32-network, 1,462-burst run: **median interval 26.5 s against 26.2 s held, median duration 0.72 s against 0.66 s held** (HELD: 119 bursts, 18 slices, 9 animals). The spread is only partly reproduced: interval quartiles 15.8 and 41.6 s against 14.3 and 54.5 s read from the printed rate interquartile range (INFERRED), duration quartiles 0.48 and 0.83 s against 0.53 and 1.06 s. The model is too regular: interval gamma shape 1.6 against about 1.3 to 1.4 held, duration shape 5.2 against 2.5 to 4 (the duration quartiles are asymmetric, so no single gamma shape matches them; ADV's 2.45 is one reading of that asymmetry, I did not reproduce it from the quartiles). **A fit shows the model can reproduce the numbers, not that the mechanism is true.**
* **A model error found and fixed on the way (disclosed).** The first version had the sign of the chloride Nernst term wrong, which made chloride look inert. The corrected version was refitted and everything below comes from it; the first outputs are kept in `run1_signbug/` and are not used.
* **Predictions scored against the table frozen before the run (`PREDICTIONS_FROZEN_BEFORE_RUN.md`, sha256 4f9385633ff5a474...): 13 right, 5 wrong, 2 not evaluable (silent network) of 20.** The two clean ones are the idea's own: a T-type-like blockade lengthens the interval and leaves the duration (MODEL: interval +92%, duration +5% at the strongest reduction); an NMDAR-active agent shortens the duration and also lengthens the interval (duration -54%, interval +55%), so **the interval-versus-duration dissociation is clean for the trigger and not for the sustainer**. The wrong ones are the instructive ones (below).
* **Four predictions nobody would make from the standard view (all MODEL; each is a thing an experiment could contradict):**
  1. **A duration-only class exists and it is not an ion-channel class: resource depletion.** Slowing the depletion of the synaptic resource to 0.4 of its value lengthens the burst 2.5-fold (0.70 to 1.78 s) and shortens the interval only 17%. The agents that act here are metabolic or release-related, the I4 family.
  2. **The sign problem of GABA-A potentiation splits the class.** Synaptic-type (phasic) potentiation never raised the burst rate in 65 sampled parameter sets (maximum rate ratio 0.64 to 0.89); a *tonic-selective* potentiation raised it in 2 of 47 sets (up to 2.9-fold), and only where the rebound gate was strong and steep (T-type weight 2 to 3 times the fitted value, steep gate) and the tonic weight raised. In the fitted network every combined potentiation silences the bursts. So "GABA-A positive modulators aggravate" is not a mechanism-class fact in this model; it is a *regime* fact needing a steep rebound gate and a tonic target. The post-hoc coupling of chloride load to the potentiation (the I6 assumption) did not change this in 18 retained sets.
  3. **Tonic inhibition is the most sensitive knob; a 20% change crosses the null/wild-type line.** Raising the tonic GABA-A weight by 20% cuts the burst rate 77%, by 40% silences it; lowering it by 40% quadruples the rate (MODEL, one-at-a-time scan). The same cliff appears for the noise amplitude (-20%: rate 0.17 of baseline), the NMDAR weight (-40%: rate 0.11, bursts shrink to blips) and the resting drive. *The held tables point at the first of these:* the delta subunit of the tonic GABA-A receptor (Gabrd) is the dominant tonic subunit in neocortex (83 TPM against 8.5 in hippocampus) and falls to 0.43 of control in the null neocortex and 0.31 in hippocampus (HELD, `regional_baseline.tsv`, n 2 to 4, bulk). A null neocortex that has lost about half its tonic inhibition is, in this model, a network that bursts; a wild-type one is not. That is the threshold crossing the brief asked for, and it is a *testable single-parameter* statement (measure the tonic conductance, D5b).
  4. **Chloride is asymmetric.** Slower extrusion (KCC2 reduced, extrusion time constant tripled) multiplies the burst rate four-fold (1.8 to 7.0 per minute) and shortens the interval 68%; faster extrusion (0.35) lengthens the interval only 29%. Chloride acts on the *interval* (it accumulates over the slow recovery) and not on the duration (-2%), which corrects my I6 first draft (see that dossier).
* **Hippocampus versus neocortex, from the model plus the tables (I3):** each of the four routes below puts a regional network below threshold with a change of the size the held transcripts show: presynaptic brake of 15 to 25%, NMDAR weight -40%, tonic weight +20 to 40%, noise -20%. The tables support all four candidates, so they cannot choose between them; the unmasking experiment can.
* **Depth reached: model.** It is not experiment-ready until the frozen scan has been run by HE's harness and an IT second reading has attacked the fit; the experiment D5b is already designed.

## D1 Statement and causal chain
1. Wwox-null neocortical neurons are depolarised with more sag and more post-inhibitory rebound (KNOWN/HELD: Breton 2021 abstract, Fig. 2; sag voltage p = 0.048 and p = 0.003 as printed, two cell groups).
2. The slice burst is a repeated event with a median interval of 26.2 s and duration of 0.66 s (HELD) and reverses at about -31 mV in whole-cell voltage clamp (HELD: excitatory and inhibitory conductances both flow; 30 bursts, 5 animals).
3. A T-type-like channel with slow recovery after a burst (time constant ASSUMED 15.7 s in the fit) makes the next ignition possible (ASSUMED; the hypothesis' trigger).
4. A noise-driven escape from a quiet state sets *when* in the permissive window the burst starts; this makes the interval an exponential-like waiting time, gamma shape near 1.5 (MODEL).
5. An NMDAR-dependent recurrent term sustains the burst; synaptic resource depletion ends it (ASSUMED); the duration sits near 0.7 s.
6. Chloride, adenosine and resource are the slow variables; in the fitted network chloride and the trigger act on the interval, resource on the duration (MODEL).

## D2 Why non-obvious
The standard view of a Wwox-null burst treats it as one event with one cause (loss of inhibition, or NMDAR excess). The two-variable reading is that **interval and duration are set by different mechanisms**, so that single drugs can move one and not the other and the same drug class can look inconsistent across experiments that measure only rate. Two further consequences the standard view lacks: duration is moved by resource-type agents (not channel blockers), and GABA-A potentiation is not a single sign.

## D3 Consequences across scales
* Cell: the sag and rebound (HELD) are the trigger's footprint: a T-type blocker or an HCN blocker should reduce the rebound; the model shows an HCN blocker lengthening the interval (full block: +275%) and shortening the duration by about a fifth (a surprise: the frozen table said duration unchanged).
* Slice: the 2x2 readout table (below) predicts which class moves interval, duration or both. Carbenoxolone dissociates frequency from duration in a held table (0.84 to 0.03 bursts per minute, duration 0.66 to 0.54 s, 13 bursts, HELD); in the model that pattern is an interval-type effect with a small duration change.
* Animal: the oscillator predicts bursts that *recur*; in vivo this is sleep- and state-dependent (I10).
* Patient: agents that fail on average may act on one of the two variables only (I2).
* **Surprising predictions:** the four listed under "Answer first".

### The 2x2 readout table (MODEL; changes of median interval and duration at the largest magnitude scanned)
| Class (link acted on) | Interval | Duration | Remark |
|---|---|---|---|
| T-type-like blockade (J_T x0.25) | +92% | +5% | the trigger |
| Persistent-sodium-type, noise-driven ignition (x0.7) | +603% | +21% | steep; near silence |
| HCN blockade (full) | +275% | -21% | |
| Adenosine augmentation (A1 weight x1.4) | +18% | -4% | weak |
| A1 antagonism (x0.4) | -34% | +16% | rate up |
| Chloride loading / slower extrusion (x3) | -68% | +11% | rate x4 |
| KCC2 enhancement (x0.35) | +29% | -2% | weak |
| NMDAR-active (J_N x0.85) | +55% | -54% | both |
| Presynaptic brake, NPY-like (0.10) | +95% | -48% | both; a cliff to blips at 0.15 to 0.25 |
| Resource depletion slowed (x0.4) | -17% | +152% | duration only |
| GABA-A potentiation, combined (0.3 to 1.0) | silent | silent | suppresses |
| Tonic GABA up (x2) | silent | silent | suppresses |

### Frozen predictions: scored list (`scan_out/score.tsv`)
Right: C1 (interval up, duration ~0), C2 (interval up, duration down), C4 interval, C5 interval, C6 (both), C7 interval, C8 (both), C9 interval, C10 interval. Wrong: C3 (predicted aggravation: it suppresses), C4 duration (down predicted: -2%), C5 duration (up predicted: +11%, borderline), C7 duration (~0 predicted: -21%), C9 duration (~0 predicted: +21%). C3 and C10 durations not evaluable (silent). The "cliff within 30%" prediction holds for the tonic weight, the noise amplitude and the NMDAR weight (rate below 0.5 per minute within a 40% change; the AMPA weight reaches 0.51, borderline).

## D4 Model
`rebound_oscillator.py`: u (activity), n (NMDAR variable), r (resource), c (chloride), a (adenosine), h (T-type-like availability), eta (coloured noise); drive x = b0 - J_tonic G(c)(1+pam) - J_a a + J_T h psi + (1-brake)(J_A r u + J_N r n) - J_I(1+pam) G(c) u + sigma eta; u' = (S(x) - u)/tau_u. G(c) is the relative GABA-A driving force from the Nernst potential of chloride (resting potential -65 mV, ASSUMED); psi is the rebound gate, a sigmoid of the hyperpolarisation from tonic GABA-A and adenosine. Fitted: `fit_baseline.py` (seeded, writes `fit_baseline_result.json`, loss 0.28). Predictions: `predict_classes.py`, `pam_sign_scan.py`, `brake_cliff.py`, `score_predictions.py`; all via `run_all.sh` (about 10 minutes). Adapter for HE's harness: `i1_harness_model.py`. A model is a hypothesis generator, not evidence; the held numbers it reproduces are two medians and a rough spread; every other constant is assumed.
Weak points I know: the fit is not unique (15 parameters, 4 targets: many sets may fit equally, and the harness LHS scan is meant to show how many); the model is too regular; chloride and adenosine are both weakly constrained by the held numbers; there is no spatial structure, no thalamus, no layers; the noise is a stand-in for finite-size effects.

## D5 Discriminating experiments
(a) **No new data.** (i) Held tables: tonic-subunit and transporter transcripts across both regions and the P47T line (script `regional_baseline.py`, S-line half done: Gabrd 0.43 of control in cortex; Gabra5 and Gabrd differ by region; the P47T half needs the committed all-genes table). (ii) HE's harness: a frozen 64-point Latin hypercube over four parameters shows whether the "interval from trigger, duration from resource" split survives wide parameter variation (it is a property of the structure or an accident of the fit). (iii) Re-reading Breton 2021's raw burst lists, if supplied, for the interval-duration correlation: in the model the two are independent (INFERRED), a correlation would tell the trigger and the sustainer are coupled. 
(b) **One slice or animal experiment.** In null neocortical layer II/III: (1) measure the tonic GABA-A current (a standard measurement): lower than wild type is predicted; equal kills prediction 3 (the named test); (2) a T-type blocker with the NMDAR component and the resource arm in the same slices: interval-only, duration-only and both classes; outcomes: the three classes behave as the table says (the model stands), or all drugs move both (the two-stage reading is killed); (3) a tonic-selective and a synaptic-selective potentiator applied separately: opposite signs predicted only in a strong-rebound regime; (4) the same applied in null hippocampus, which should not burst (I3).
(c) **Clinical-observational.** Record for each child: whether events are rhythmic and recurrent with a stable interval (EEG epoch structure), the state (sleep or wake) and the exposure history to tonic-selective and synaptic-selective GABA-A agents; the oscillator predicts a *state dependence* and a *drug-class dependence* of worsening.

## D6 Intervention logic (labels only; no dose, no recommendation to use any agent; BLOCK-1 flags from public labels)
| Link in the model | Mechanism class | Agent with a public label | Boxed-warning screen (SCI readiness sheets for the earlier thirteen; `outside_set_label_screen.tsv` for the rest) | Aggravation counterpart |
|---|---|---|---|---|
| trigger (J_T) | T-type-like blockers | ethosuximide (red in the readiness sheet by serious wording; no boxed warning), zonisamide (red) | red | T-type up-regulation or agents that deepen hyperpolarisation before release |
| sustainer (J_N) | NMDAR-active | memantine (yellow), ketamine (yellow), esketamine (red) | per sheets | NMDAR potentiators |
| noise-driven ignition | sodium channel blockers | carbamazepine, phenytoin, lamotrigine (red in sheets); lacosamide (no boxed warning in the screen; unassessed beyond it) | per sheets and screen | sodium-channel openers |
| tonic GABA-A (J_tonic) | tonic-selective potentiation | ganaxolone (no boxed warning in the screen; unassessed beyond it) | screen | tonic antagonists |
| synaptic GABA-A | benzodiazepine-like | diazepam, clobazam, clonazepam, zolpidem, eszopiclone (all red in sheets) | sheets | see I6 |
| tonic GABA availability | GAT-1 inhibition, GABA-transaminase inhibition | tiagabine (no boxed warning), vigabatrin (boxed warning: permanent vision loss, red) | screen | |
| HCN | HCN blockade | ivabradine (no boxed warning in the screen; heart-rate drug) | screen | HCN potentiation |
| adenosine | augmentation by uptake blockade | dipyridamole (no boxed warning in the screen) | screen | A1 antagonism: caffeine citrate (no boxed warning, unassessed) |
| resource and metabolism | ketone- or lactate-linked routes (I4) | not an agent class with a label here | not applicable | glycolytic stress |
| chloride | KCC2 / NKCC1 | bumetanide, furosemide (boxed warning, red) | screen | see I6 |
'No boxed warning in the screen' is not 'safe': that screen reads only the boxed-warning section; it is unassessed beyond it and treated as at least yellow.

## D7 Combination
I3: the model supplies the cliff sizes; I6: chloride acts on the interval here, on within-burst headroom there: the two settle together in a model with both the chloride load and the burst-time membrane potential, which I1 does not have; I4: the duration-only class is the I4 axis; I5/I9: they would enter as a delay in the inhibitory term, which the model lacks; I10: add a slow state variable. Contradictions to settle by experiment: whether PAM suppresses (I1 fitted regime) or aggravates (the strong-rebound regime and the I6 headroom reading); D5b (3) decides.

## D8 Stronger / dead
Stronger: the harness LHS shows the interval/duration split is structural; a measured tonic-current deficit in null neocortex; a duration-only drug effect from a resource-type agent. Killed by (named tests): equal tonic conductance in null and wild-type neocortex *and* a normal NMDAR/tonic pharmacology (prediction 3); all agents moving interval and duration together (the two-stage split). Parked-with-trigger: none.

## D9 Cheapest next step with no literature
SCI: hand HE the frozen scan (`scan.json`); IT: attack the fit (non-uniqueness; target choice: the quartile reading of the rate IQR is mine); HE: LHS result. Needs no outside source.
