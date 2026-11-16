# EXPERIMENT BRIEF (PRESIDIO-013, SCI, 2026-11-16): the head-to-head slice experiment that breaks the five-way tie

Written for: IT and ADV (BLOCK-1 triage is IT's, after this brief), and then a laboratory that holds a Wwox-deficient slice preparation. Non-canonical working note. Not medical advice: mechanism matching only, no dose, no schedule, no recommendation to use any agent; concentrations below are PUBLISHED TOOL CONCENTRATIONS cited with their source, never recommendations. Reference genotype class only. Nothing here edits the frozen matrix (freeze f5b71a3f4). DATO = stated in a held source (named); INFERENZA = my reading; background pharmacology = general knowledge, flagged. Predictive capacity of this brief: none until the experiment is run.

## On one page

**Decision.** The informed arm of the AED matrix ranks five mechanism classes level at seizure P13-P15 (NMDAR pore blockers, GABA-A positive modulators, benzodiazepines, sodium-channel blockers, valproate-type; 5 of 15, `tie_set_weak`), and literature cannot break the tie because the three scoring threads come from one network (origin hunt, PRESIDIO-012). Only a measurement can. **The experiment**: in Wwox neuron-knockout slices at matched age, one mechanism representative per class is tested head to head on the same spontaneous-burst readout, against a time-matched vehicle and d-APV (the published positive control), in neocortex (where Breton 2021 saw bursts: 36 of 42 knockout slices against 0 of 11 wild type) and hippocampus (where it saw none), with a wild-type trigger or evoked-current control so that "knockout-specific" can be told from "generic".

**Why this one.** The VOI pass shows that lowering the pore-blocker link or the GABA-A link by one step each hands the top to the other, so a pore blocker against a GABA-A positive modulator is the pair whose outcome changes the ranking in both directions; the sodium-channel arm tests the aggravation hypothesis AH1 in the same slices; the GluN2B NAM arm tests the age-composition split (LEAP-2).

**What it changes** (table 4): a specific pore blocker alone leaves 1 of 15 on top; a specific GABA-A positive modulator leaves 2 (with benzodiazepines); if everything suppresses and nothing is specific the tie stays at 4; if nothing suppresses, no tested class leads.

**How many animals** (table 5): about 8 to 17 animals per genotype per arm for one primary comparison under assumptions I cannot check from the repository (the between-animal variance of burst suppression is not held); 6 to 34 for WO-10; a four-animal-per-genotype pilot fixes the variance before any arm is sized.

**First step, no animals:** fix the conditions that decide interpretation (bath Mg2+, temperature, trigger, burst definition, window length), then WO-10 with a genotype contrast and the baseline burst incidence in both regions. **Stop** if the knockout neocortical slices do not burst under the laboratory's conditions or d-APV does not abolish them.

**The Aldaz question** (a measurement that would decide whether it counts as a match): the only independent signal on the inhibition axis, PV+ and NPY+ interneuron loss, is HIPPOCAMPAL (Aldaz 2019, full knockout, 2 weeks), while the bursts are NEOCORTICAL. Count PV+ and NPY+ interneurons in neocortical layer 2/3 and in hippocampus of the same animals at the slice age, and record spontaneous inhibitory current rate and amplitude with an unpooled wild-type control in both regions. If neocortex shows the loss and the inhibitory deficit, the region confound dissolves and the PV loss counts as a match for GABA-A classes (top set 5 to 2 in the scratch run of PRESIDIO-012); if only hippocampus does, it stays `unknown`.

## 1. Preparation and conditions (what is already in the repository)
* **Model and ages.** Synapsin-I-Cre Wwox knockout and wild-type littermates, both sexes, P13-P17 (Breton 2021, PMID 34634460, PMC8609180; INV-05 `experiment.tsv` X1 to X4). DATO: neocortical bursts 36/42 KO v 0/11 WT, absent in hippocampus; pyramidal resting potential -73.62 (KO) v -79.25 mV (WT), no liquid-junction correction; glucose 10 mM; incubation solution 1.3 mM MgSO4; recording-bath Mg2+ not stated; baseline burst rate printed as 2.29 per minute in the text and 0.84 per minute in Table S1; d-APV 50 µM abolished bursts in 5 slices from 3 animals, reversible on washout, no test (registry wave notes of CLAIM 021, receipts FTR-20261029-34634460-01/-04/-05).
* **What must be fixed first (INV-05 X0, unresolved):** bath Mg2+ and temperature (they set how much NMDAR current is available); the burst definition and window; the 2.29 against 0.84 per minute discrepancy (measure, do not assume); whether the mouse line is obtainable (it appears to come from the Aqeilan laboratory, as in Repudi 2021; no contact is made from here).
* **WO-10** (IT15 definition): the NAM-sensitive fraction of the isolated NMDAR current in burst-age slices; the only published number is WO-11 (Mierau 2004, wild-type barrel cortex, evoked EPSC, 3 µM ifenprodil, 14% with an interval of 0-34% at P13-P15 against 53% at P6-P8; room temperature, 2 mM Mg2+, Cs-based internal with QX-314, bicuculline; pre-incubation at least 40 min and ifenprodil in the bath; holding potential of the comparison not stated). A knockout fraction of at least 40% against the wild-type interval is LEAP-2's prediction; inside 0-34% rejects it.

## 2. Arms (class; examples with their selectivity source; no recommendation)
| arm | named examples and selectivity source (held) | published tool concentration (cited, not a recommendation) | what it tests | rejecting result |
|---|---|---|---|---|
| d-APV, positive control | competitive NMDAR antagonist, mildly GluN2A-preferring (`nmda_inv05_20261107/output/probes.tsv`) | 50 µM abolished KO bursts (Breton 2021) | the preparation reproduces | no abolition: stop |
| vehicle | time-matched | n/a | drift and washout | burst rate drifts by more than the effect sought |
| NMDAR pore blocker | memantine, MK-801, ketamine (probes.tsv; PMID 20720132 autaptic rat neurons: memantine 1 µM blocked 27.1% synaptic and 50.4% extrasynaptic; MK-801 1 µM about 94% and 96%) | as cited | total NMDAR current limits the bursts | no suppression at a verified fractional block |
| GluN2B NAM | ifenprodil (155 nM GluN2B v 28 µM GluN2A, oocytes), Ro 25-6981 (9 nM v 52 µM, compiled, primary unread), radiprodil (GluN2B only, 4-70 nM); all three share the ifenprodil site, so they are one mechanism, not three | as cited | GluN2B-containing current carries the bursts (LEAP-2) | suppression-per-current-removed curve coincides with the pore blocker's |
| AMPA antagonist | GYKI 53655 (noncompetitive; mouse slices IC50 2.5 µM, 10 µM removed 80.5% in entorhinal cortex and 89% in barrel cortex layer V; PMID 27838344), NBQX (competitive; Ki 0.077 µM GluA2 v 2.6-5.4 µM GluK1-3, binding; PMID 35955932); perampanel is the same pocket as GYKI (`ampa_comparison_it41_20261109`) | as cited | excitatory drive, any glutamate class | suppresses KO bursts at the same potency as the pore blocker AND in provoked WT slices: NMDA dependence gives no class specificity |
| T-type blocker | Z944 (Cav3.2 IC50 about 265 nM, Cav1.4 about 31 µM; PMID 41489546), flunarizine (Kd 530 / 3552 / 837 nM at Cav3.1/3.2/3.3; PMID 11784784); ML218 and TTA-P2 share Z944's scaffold, so not independent; ethosuximide is millimolar and nonselective (`ttype_20261107/output/README.md`) | as cited | rebound-driven bursting (T13) | no suppression |
| GABA-A positive modulator, non-benzodiazepine | **no held selectivity source**; IT to source one before BLOCK-1 (class examples exist; I do not name one without a source) | not applicable | inhibition deficit as the lever (T2) | suppresses KO bursts but equally provoked WT bursts: generic (PTZ-like), not WWOX-specific |
| benzodiazepine | diazepam, clobazam, N-desmethylclobazam; rat subunits in HEK cells, alpha1/2/3/5; NDMC alpha2/alpha1 efficacy ratio 1.77 as printed (Ralvenius 2016; `gabaa_subtype_adv004_20261114/README.md`) | as cited | same lever, with the subtype dispute noted | as above |
| sodium-channel blocker (AH1) | **no held selectivity source** (carbamazepine, lamotrigine and phenytoin appear in held files only as clinical entries); IT to source | not applicable | direction: does it RAISE burst rate (aggravation) | no change is also a result: AH1 stays `unknown`, not rejected |

## 3. Design, both regions, both genotypes
* **Each slice is its own control:** baseline then drug (paired), with a time-matched vehicle group and washout (d-APV is reversible per Breton 2021; the others' reversibility is not held); arm order randomised across slices; recordings blind to genotype and arm; analysis fixed before unblinding.
* **Neocortex (L2/3 to L5 network):** KO spontaneous bursts are the readout (rate, duration, amplitude). **Hippocampus:** KO does not burst spontaneously per Breton 2021, so the readout is a provoked burst threshold or rate, in both genotypes, chosen BEFORE the experiment and justified. **Trigger caveat:** low Mg2+ unblocks NMDAR and would bias the NMDAR arms; a GABA-A block as trigger confounds the GABA-A arms; a trigger that does neither (for example raised extracellular K+) is preferable, and whichever is used must be matched to the KO burst rate. The trigger is a declared choice, not a result.
* **Genotype-independent control:** the evoked NMDAR and AMPA components in both genotypes, so each class's burst suppression is expressed per unit of NMDAR current removed (INV-05's conditional hypothesis); drug exposure and achieved block verified (INV-05 correction), not assumed.
* **Readouts:** burst incidence, rate, duration, amplitude; evoked non-burst responses (X3, sparing of physiology); resting potential; viability. **Units:** animals, with slices nested (mixed model).

## 4. Outcome to top set (official generator, rule pinned; the mapping is mine and declared)
Outcome codes per arm: S specific suppression (new tier-3 drug-by-genotype cell, directness 3), G generic suppression (tier 1, directness 3), N no suppression (the class's seizure links are rejected), A aggravation (aggravation cell, never netted). Untested classes (valproate-type, carbonic-anhydrase/multi-target, SV2A, Kv7, cannabidiol, steroid, diet) keep their frozen scores. Generated by `scenarios.py`; `output/scenarios.tsv`.
| scenario | outcomes | top set at seizure P13-P15 | size of 15 |
|---|---|---|---|
| S1 | pore S; GluN2B NAM, AMPA G; the rest N | NMDAR pore blockers | 1, `discriminating` |
| S2 | GABA-A PAM and benzodiazepine S; pore G; the rest N | GABA-A PAM, benzodiazepines | 2, `tie_set_weak` |
| S3 | pore S and GABA-A PAM S; the rest N | pore blockers, GABA-A PAM | 2, `tie_set_weak` |
| S4 | GluN2B NAM S; pore G; the rest N | GluN2B NAMs | 1, `discriminating` |
| S5 | every arm G (generic) | pore, GABA-A PAM, benzodiazepines, sodium-channel | 4, `tie_set_weak` |
| S6 | sodium-channel S; the rest G | sodium-channel blockers | 1, `discriminating` |
| S7 | no arm suppresses | valproate-type (untested, by breadth only) | 1: no TESTED class leads; the top is an artefact of an untested class |
| S8 | pore S; GABA-A PAM, benzodiazepine, sodium-channel A | pore blockers; aggravation reported apart for the other three | 1 |
The head-to-head pair is S1 against S2: the two scenarios hand the top set to opposite classes, which is why the pair is first.

## 5. Number of animals (a range, with its assumptions; `size_l7.py`, `output/sizing.tsv`)
Unit the animal; two-sided alpha 0.05 (0.0083 for six arms each against vehicle), power 0.8, normal approximation with the Guenther correction. **Not held in the repository: the between-animal variance of burst suppression**; the d-APV arm gives 51 bursts in 5 slices from 3 animals and no window length. So the range is conditional.
| test | assumption range | animals per group |
|---|---|---|
| WO-10, NAM-sensitive fraction, KO v WT | SD 20-35 points, difference 20-26 points, 3 cells per animal, ICC 0.2-0.5 | 6 to 34 (central 9 to 14) |
| one primary burst-suppression comparison (arm v vehicle, or arm v arm) | SD of animal-level proportional change 0.2-0.4, difference 0.3-0.4 | 5 to 29 (central 10 to 17) |
| six arms each against vehicle | SD 0.2-0.4, difference 0.4, alpha 0.0083 | 8 to 26 |
| drug-by-genotype (KO v provoked WT) | SD 0.2-0.4, difference 0.3 | 8 to 29 |
Pilot: four animals per genotype with vehicle and d-APV fix the variance; every n above is then recomputed.

## 6. Sequence, and what stops it
1. **Desk, no animals (X0):** fix bath Mg2+, temperature, burst definition and window, the trigger, the slice region, blinding and randomisation; resolve the 2.29 v 0.84 per minute discrepancy by plan, not by assumption. 2. **Pilot and WO-10:** baseline burst incidence in both regions and both genotypes; the NAM-sensitive fraction; d-APV. **Stop** if the KO neocortical slices do not burst, or d-APV does not abolish. 3. **Decisive pair:** pore blocker against GABA-A positive modulator (with benzodiazepine) against vehicle, KO and provoked WT, neocortex. 4. **Then, in this order if resources are short:** the sodium-channel arm (AH1, because an aggravation result is the most information per animal), the GluN2B NAM arm, the AMPA arm, the T-type arm. 5. **The Aldaz measurement** alongside step 2 (counts and sIPSC in the same animals), because it decides whether the GABA-A rows may rely on the hippocampal PV loss.
BLOCK-1 triage of each representative is IT's, after this brief; nothing here clears any agent.

## 7. What already exists, and what does not
Exists: the burst preparation and its numbers (Breton 2021 and the INV-05 files), the experiment ladder X0-X4 (`nmda_inv05_20261107/output/experiment.tsv`), the probe table, the AMPA, Cav3 and GABA-A tool reviews (IT41, ADV-009, ADV-004), WO-11, the sizing and scenario scripts and the frozen matrix with the official generator. **Does not exist in the repository:** a variance for burst suppression, a held selectivity source for a non-benzodiazepine GABA-A modulator and for a sodium-channel tool, the bath Mg2+ of the source recordings, a second laboratory's replication (PRESIDIO-012), and any agent tested in any Wwox slice except d-APV.

## 8. Limits
Mechanism matching only; not an experiment result. Scenarios are my declared mapping from outcomes to cells, not rule v1; the sizing is conditional on assumptions I list; the trigger and the region of the neocortical recordings are not fixed by the sources; hippocampus has no spontaneous-burst precedent. Tool concentrations are literature values for other preparations; achieved block in the slice must be measured.
