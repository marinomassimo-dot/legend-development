# Questions and alternatives (statements only; assign cells yourself)

## Q1. Why do heterozygous slices burst in a graded way (0 of 11, 4 of 23, 36 of 42) rather than like wild type or like knockout?
Each alternative names which single variable is the rate-limiting graded one that places het between WT and KO.

- **Q1-A1, graded synaptic inhibition.** The loss of synaptic (phasic) inhibition scales with Wwox dose; bursts occur when it falls past a threshold, so het slices sit near the threshold and few cross it.
- **Q1-A2, intrinsic route.** The shared depolarized intrinsic state (O5, O11, het = KO) is permissive but not graded; an additional intrinsic property that is larger in KO (the quoted candidate is rebound) is the graded variable, and synaptic inhibition is not what separates het from KO.
- **Q1-A3, tonic extrasynaptic GABA-A conductance.** A graded loss of tonic (not phasic) GABA-A conductance, not synaptic IPSCs, is the graded variable.
- **Q1-A0, none of the listed explanations** (for example a variable not in the observations, or a non-graded cause such as slice-to-slice variability of an unmeasured property).


## Q2. What sets the interval and the duration of the bursts?
Each alternative names the process whose recovery or time course sets the 26.2 s interval and terminates each burst (O3).

- **Q2-B1, recovery of NMDA-receptor-dependent recurrent excitation.** A burst depletes an excitatory resource that must recover before the next burst; its depletion ends the burst.
- **Q2-B2, recovery of inhibition.** A burst recruits inhibition that ends it and decays over the interval, permitting the next burst.
- **Q2-B3, a slow intrinsic or ionic process.** A cell-intrinsic process (for example a slow after-burst hyperpolarizing or depolarizing state) that cycles over tens of seconds sets the interval and the duration.
- **Q2-B0, none of the listed explanations** (for example no clock at all: timing as a chance threshold crossing; the interquartile range of the interval is not quoted, so a regular or random pattern cannot be told apart from O3).


## Q3. How could the distance of a slice from its burst threshold be measured in all three genotypes so that WT has a defined value?
- **Q3-C1, raised-potassium ladder.** Raise extracellular potassium stepwise; the distance is the step at which the first burst appears. Reads a depolarization-related component of the threshold (O5, O11). Confounds: het and KO already start more depolarized, so equal steps may not be equal distances; het = KO on the passive step (O11) so it may collapse the graded difference; slices that already burst (4 of 23 het) get no value.
- **Q3-C2, lowered-magnesium ladder.** Lower extracellular magnesium stepwise and score the first burst. Reads NMDA-receptor-gated excitation, which bursts need (O7). Confounds: reads the common downstream path and may mask which upstream variable differs; a dependence on the baseline depolarization is not quoted; KO-only evidence for the NMDA dependence.
- **Q3-C3, pharmacological drive by graded antagonism of GABA-A inhibition (excitatory direction, no dose stated).** Reduce GABA-A inhibition stepwise and score the first burst. Reads the inhibitory reserve (O4, O6). Confounds: KO starts with less synaptic inhibition, so the range differs by genotype; ambient GABA depends on uptake (O9); WT tonic contribution is minute at endogenous GABA (O8), so mainly phasic is read.
- **Q3-C4, pharmacological suppression ladder with a tonic GABA-A agonist (THIP).** Add tonic inhibition stepwise and score the step that abolishes bursts. Reads inhibitory capacity (O8 shows the lever works in WT neurons).
- **Q3-C0, none of the listed frames** (for example a non-driven proxy index from patch measures, or an evoked-burst stimulus threshold; neither is entered because no quote supports or opposes them).

