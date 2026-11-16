# Contrast sets (blind builder; evidence = OBSERVATIONS.md O1 to O12 only)

All alternatives are labelled hypotheses. None is called proven. Cells were assigned only from the quoted text; the full cell table (156 rows) is in `cells.tsv` (columns: question, alternative_id, observation_id, value, reason). Cell meaning: `supports` = the quote states something this alternative needs or predicts; `opposes` = the quote contradicts it or shows it cannot work; `silent` = otherwise (consistent-but-nondiscriminating also counts as silent). In Q3, confounds are written in the reason with the prefix CONFOUND and do not by themselves count as `opposes`.
Every question carries an abstention alternative (A0 / B0 / C0, "none of the listed explanations"); it makes no claim, so all its cells are `silent`, and it always remains in the residual set.

Two reading cautions from the quotes themselves: (a) O3 gives the burst duration as "0.66 [0.53-1.06]" with no unit; I do not assume one, so duration-to-interval ratios are not computed. (b) O4 pools heterozygotes and wild type as S-CTL, so no heterozygote-alone inhibitory value is available.

---

## Q1. Why do heterozygous slices burst in a graded way (0 of 11, 4 of 23, 36 of 42) rather than like wild type or like knockout?

### (1) Contrast set
Each alternative names which single variable is the rate-limiting graded one that places het between WT and KO.

- **Q1-A1, graded synaptic inhibition.** The loss of synaptic (phasic) inhibition scales with Wwox dose; bursts occur when it falls past a threshold, so het slices sit near the threshold and few cross it. Rejecting observation: a het-alone sIPSC equal to WT, with burst status unrelated to sIPSC size, would oppose it (not available now; O4 pools het and WT).
- **Q1-A2, intrinsic route.** The shared depolarized intrinsic state (O5, O11, het = KO) is permissive but not graded; an additional intrinsic property that is larger in KO (the quoted candidate is rebound) is the graded variable, and synaptic inhibition is not what separates het from KO. Rejecting observation: a het slice with KO-like rebound but no bursts, together with burst status tracking sIPSC size, would oppose it (not available now).
- **Q1-A3, tonic extrasynaptic GABA-A conductance.** A graded loss of tonic (not phasic) GABA-A conductance, not synaptic IPSCs, is the graded variable. Rejecting observation: O8 (only a minute tonic current at endogenous GABA levels in WT).
- **Q1-A0, none of the listed explanations** (for example a variable not in the observations, or a non-graded cause such as slice-to-slice variability of an unmeasured property).

### (2) Cells (full reasons in cells.tsv)

| Obs | A1 | A2 | A3 | A0 |
|---|---|---|---|---|
| O1 | silent (explanandum) | silent | silent | silent |
| O2 | silent (region restriction unexplained) | silent | silent | silent |
| O3 | silent | silent | silent | silent |
| O4 | supports (KO sIPSC reduced; het-alone not given) | silent | silent (phasic only) | silent |
| O5 | silent | supports (het depolarized) | silent | silent |
| O6 | supports (authors' interpretation) | silent | silent | silent |
| O7 | silent (NMDAR dependence compatible with all) | silent | silent | silent |
| O8 | silent | silent | opposes (minute tonic current in WT; weak, other preparation) | silent |
| O9 | silent | silent | silent | silent |
| O10 | silent | silent (removes only a PPxY route for 16 genes) | silent | silent |
| O11 | silent | supports (het = KO passive step; rebound only in KO) | silent | silent |
| O12 | silent | silent | silent | silent |

### (3) Residual after all observations
Not opposed: **A1, A2, A0**. A3 is opposed by O8 only, a weak opposition (a wild-type value in another preparation); it is not proven dead. O1, O2, O3, O7, O9, O10 and O12 do not discriminate. Two observations support A1 and two support A2, so the quotes do not choose between them; the support for each rests on a different genotype contrast (KO versus pooled controls for A1; het versus WT intrinsic properties for A2).

### (4) First experiment
In the same slices, in age-matched WT, het and KO neocortex, record spontaneous bursts first and then patch layer II/III pyramidal cells in the same slice, measuring (i) sIPSC amplitude and frequency (with the high-chloride pipette used in O4, so the results are comparable) and (ii) the intrinsic profile including rebound. Analyse in het slices: bursting (about 4 of 23) versus non-bursting.
- Favours A1: het sIPSC amplitude intermediate between WT and KO, and bursting het slices have lower sIPSC than non-bursting het slices, while rebound and passive properties do not separate them.
- Favours A2: het sIPSC is indistinguishable from WT (as the pooling in O4 would allow) and rebound (or another intrinsic property) separates bursting from non-bursting het slices.
- Favours A3 only if a tonic current is later measured and shows the same ordering; this experiment does not measure it, and if neither sIPSC nor intrinsic properties separate bursting from non-bursting het slices, A0 gains.
Limit: correlational; a causal follow-up would test whether restoring the favoured variable in KO slices removes bursts.

### (5) Framing-leak and citation lines
- **A1.** Framing leak: wording "synaptic inhibition" comes from O6 (the authors' sentence) and O4; "graded" comes from the question itself; this alternative inherits the authors' own interpretation. Citation: no outside fact named; the link from lower IPSC amplitude to bursting is only the authors' interpretation in O6 (no rescue quoted).
- **A2.** Framing leak: wording shaped by O5 and O11 (the repository note), including the choice of rebound as the candidate graded property because O11 says it is KO-only. Citation: `needs_outside_fact`: that a depolarized state and rebound can promote network burst generation in cortex (no quote states a burst-generating role for any intrinsic property).
- **A3.** Framing leak: shaped by the presence of O8, O9, O12 in the packet (tonic-current papers), not by any Wwox quote; the alternative exists because those quotes were supplied. Citation: `needs_outside_fact`: that tonic GABA-A conductance restrains network excitability and is dose-dependent on Wwox (neither is in the file; no Wwox tonic value is quoted).
- **A0.** No framing leak; no outside fact.

---

## Q2. What sets the interval and the duration of the bursts?

### (1) Contrast set
Each alternative names the process whose recovery or time course sets the 26.2 s interval and terminates each burst (O3).

- **Q2-B1, recovery of NMDA-receptor-dependent recurrent excitation.** A burst depletes an excitatory resource that must recover before the next burst; its depletion ends the burst. Rejecting observation: a time-locked probe showing excitatory efficacy fully recovered well before the next burst would oppose it (not available now).
- **Q2-B2, recovery of inhibition.** A burst recruits inhibition that ends it and decays over the interval, permitting the next burst. Rejecting observation: inhibition probed after a burst found unchanged across the interval would oppose it (not available now).
- **Q2-B3, a slow intrinsic or ionic process.** A cell-intrinsic process (for example a slow after-burst hyperpolarizing or depolarizing state) that cycles over tens of seconds sets the interval and the duration. Rejecting observation: intrinsic properties found flat across the interval would oppose it (not available now).
- **Q2-B0, none of the listed explanations** (for example no clock at all: timing as a chance threshold crossing; the interquartile range of the interval is not quoted, so a regular or random pattern cannot be told apart from O3).

### (2) Cells

| Obs | B1 | B2 | B3 | B0 |
|---|---|---|---|---|
| O1 | silent | silent | silent | silent |
| O2 | silent | silent | silent | silent |
| O3 | silent (explanandum; no time constant quoted) | silent | silent | silent |
| O4 | silent | silent | silent | silent |
| O5 | silent | silent | silent | silent |
| O6 | silent | silent | silent | silent |
| O7 | supports (NMDAR needed for bursts; occurrence, not timing) | silent | silent | silent |
| O8 | silent | silent | silent | silent |
| O9 | silent | silent | silent | silent |
| O10 | silent | silent | silent | silent |
| O11 | silent | silent | supports (rebound only in KO; no kinetics, weak) | silent |
| O12 | silent | silent | silent | silent |

### (3) Residual
**B1, B2, B3 and B0 all remain**; no observation opposes any of them. The honest reading is that the packet holds one timing observation (O3) and nothing that gives a time constant, so Q2 is undetermined by the quotes. The two `supports` cells are weak and concern occurrence (O7) or an intrinsic feature without kinetics (O11).

### (4) First experiment
In KO slices, align everything to the field burst and sample the three candidate variables at fixed lags after a spontaneous burst (from sub-second to beyond the 26.2 s interval), in the same slices: evoked NMDA-receptor-dependent excitatory efficacy (B1), evoked IPSC amplitude (B2), and intrinsic membrane properties including rebound and resting potential (B3). Compare each recovery time course with the interval and with the time of the next burst.
- Favours B1: excitatory efficacy is depressed after a burst and recovers on the scale of the interval, with the next burst following full recovery; inhibition and intrinsic properties are flat.
- Favours B2: IPSC amplitude is enhanced or inhibition is engaged after a burst, with decay matching the interval; the others are flat.
- Favours B3: intrinsic properties shift after a burst and return on the interval scale; synaptic efficacy is flat.
- Favours B0: none of the three shows an interval-scale recovery, or the interval shows no lawful relation to the earlier burst.
The same time-resolved trace also gives a duration test (what changes within the 0.66-long event, unit as quoted).

### (5) Framing-leak and citation lines
- **B1.** Framing leak: shaped by O7 (the NMDA-receptor dependence). Citation: `needs_outside_fact`: that excitatory drive depletes and recovers on a tens-of-seconds scale (no quote gives any recovery time).
- **B2.** Framing leak: shaped by O4 and O6 and by the Q1 answer set (inhibition as protagonist). Citation: `needs_outside_fact`: that a burst recruits inhibition that decays over the interval (no quote gives inhibition's relation to bursts in time).
- **B3.** Framing leak: shaped by O11 (rebound, KO-only) and O5. Citation: `needs_outside_fact`: that an intrinsic process can cycle on a tens-of-seconds scale (no kinetics quoted).
- **B0.** No framing leak; no outside fact.

---

## Q3. How could the distance of a slice from its burst threshold be measured in all three genotypes so that WT has a defined value?

Alternatives here are measurement frames, not mechanisms, so they are not mutually exclusive in practice; they are contrasted by what each reads and what it confounds. Four frames are entered (one above the usual two or three, at the question's invitation to propose others).

### (1) Contrast set
- **Q3-C1, raised-potassium ladder.** Raise extracellular potassium stepwise; the distance is the step at which the first burst appears. Reads a depolarization-related component of the threshold (O5, O11). Confounds: het and KO already start more depolarized, so equal steps may not be equal distances; het = KO on the passive step (O11) so it may collapse the graded difference; slices that already burst (4 of 23 het) get no value. Rejecting observation: none (not opposed).
- **Q3-C2, lowered-magnesium ladder.** Lower extracellular magnesium stepwise and score the first burst. Reads NMDA-receptor-gated excitation, which bursts need (O7). Confounds: reads the common downstream path and may mask which upstream variable differs; a dependence on the baseline depolarization is not quoted; KO-only evidence for the NMDA dependence. Rejecting observation: none.
- **Q3-C3, pharmacological drive by graded antagonism of GABA-A inhibition (excitatory direction, no dose stated).** Reduce GABA-A inhibition stepwise and score the first burst. Reads the inhibitory reserve (O4, O6). Confounds: KO starts with less synaptic inhibition, so the range differs by genotype; ambient GABA depends on uptake (O9); WT tonic contribution is minute at endogenous GABA (O8), so mainly phasic is read. Rejecting observation: none.
- **Q3-C4, pharmacological suppression ladder with a tonic GABA-A agonist (THIP).** Add tonic inhibition stepwise and score the step that abolishes bursts. Reads inhibitory capacity (O8 shows the lever works in WT neurons). Rejecting observation: O1, since WT has 0 of 11 bursting slices, there is nothing to suppress and WT has no defined value.
- **Q3-C0, none of the listed frames** (for example a non-driven proxy index from patch measures, or an evoked-burst stimulus threshold; neither is entered because no quote supports or opposes them).

### (2) Cells

| Obs | C1 | C2 | C3 | C4 | C0 |
|---|---|---|---|---|---|
| O1 | silent (WT burst under drive not shown; 4/23 het already past threshold) | silent | silent | opposes (nothing to suppress in WT) | silent |
| O2 | silent | silent | silent | silent | silent |
| O3 | silent (CONFOUND: window must span several 26.2 s intervals) | silent (same) | silent (same) | silent (same) | silent |
| O4 | silent | silent | supports | supports | silent |
| O5 | supports (CONFOUND: shifted start) | silent (CONFOUND not quoted) | silent | silent | silent |
| O6 | silent | silent | supports | supports | silent |
| O7 | silent | supports (NMDAR needed; KO only) | silent | silent | silent |
| O8 | silent | silent | silent (mainly phasic read) | supports (lever works in WT; gives current, not distance) | silent |
| O9 | silent | silent | silent (CONFOUND: uptake) | silent (CONFOUND: uptake) | silent |
| O10 | silent | silent | silent | silent | silent |
| O11 | supports (CONFOUND: het = KO may collapse grading) | silent | silent | silent | silent |
| O12 | silent | silent | silent | silent | silent |

### (3) Residual
Not opposed: **C1, C2, C3, C0**. **C4 is opposed by O1** (no defined WT value); it remains useful only as a suppression read within bursting het and KO slices. None of C1 to C3 has quoted evidence that it brings WT to a burst, so whether each returns a defined WT value is untested; this is the main thing the first experiment must show.

### (4) First experiment
Sibling slices from the same animals and ages for WT, het and KO, genotype-blind. In each slice run one ladder (C1, C2 or C3) with a washout and a balanced order across slices, scoring the first burst with an observation window that spans several 26.2 s intervals at every step. Then analyse (a) whether every WT slice reaches a defined threshold; (b) whether thresholds are ordered WT > het > KO; (c) in het, whether the threshold predicts the baseline burst status (4 of 23 burst); (d) within-genotype spread and reversibility; (e) whether thresholds from two ladders in the same slice agree.
- Favours C1: WT thresholds are defined and het slices that burst at baseline have the lowest values, but het and KO thresholds are similar (the passive step, O11); C1 then reads the shared intrinsic component.
- Favours C2: thresholds are defined in WT and graded across WT, het, KO, and predict het baseline status better than C1.
- Favours C3: thresholds are graded and track the sIPSC deficit, with KO thresholds off-range because of the reduced starting inhibition.
- If two ladders disagree on the het position in the same slice, they read different axes; if no ladder gives WT thresholds, C0 gains.

### (5) Framing-leak and citation lines
- **C1.** Framing leak: the frame was named in the question itself ("raised-potassium ladder"); O5 and O11 then shaped how it is read. Citation: `needs_outside_fact`: that raising extracellular potassium depolarizes neurons and can bring a slice to burst (no quote).
- **C2.** Framing leak: named in the question; O7 shaped the reading. Citation: `needs_outside_fact`: that lowering magnesium relieves the NMDA-receptor block (voltage-dependent) so it acts on the path O7 shows bursts need (O7 states only the d-APV effect).
- **C3.** Framing leak: "pharmacological drive" came from the question; O4, O6 shaped the target. Citation: `needs_outside_fact`: that antagonizing GABA-A receptors lowers synaptic inhibition and can provoke bursts (no quote; no antagonist or dose is named here).
- **C4.** Framing leak: shaped by the presence of O8 and O12 in the packet (THIP papers). Citation: no outside fact named for the lever (O8 gives the THIP-induced tonic current in WT neurons); that THIP suppresses KO/het bursts is a prediction, not quoted. It is opposed by O1 irrespective.
- **C0.** No framing leak; no outside fact.

---

## Summary of outside-fact needs (alternatives, excluding abstentions)
Q1: 2 of 3 (A2, A3). Q2: 3 of 3 (B1, B2, B3). Q3: 3 of 4 (C1, C2, C3). Total 8 of 10. The needed facts are general physiology links (a mechanism's ability to cause bursts or a drug's action), none specific to Wwox; none of the 8 was supplied by the packet.
