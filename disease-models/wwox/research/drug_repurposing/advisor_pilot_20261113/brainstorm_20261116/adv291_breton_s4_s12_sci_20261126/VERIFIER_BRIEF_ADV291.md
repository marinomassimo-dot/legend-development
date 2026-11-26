# Blind figure read (hypothesis level; not medical advice)

Source: one 2021 mouse study (neuron-specific Wwox knockout, S-KO; heterozygote S-HT; wildtype S-WT; neocortical slices). Work ONLY from the files in this folder: figS4.png, figS1.png, figS2.png and this brief. Do not read any other file on the machine, do not use the network. You may crop and enlarge with ImageMagick `convert` and read pixels with `python3 -P -E` (numpy is available; no PIL). Write your scripts and crops in this folder.

Table 1 of the paper, N (cells/animals): pyramidal S-WT 13/5, S-HT 15/6, S-KO 40/15; interneurons S-WT+S-HT (called S-CTL) 5/4, S-KO 6/5.

## Captions, verbatim

Supplementary Figure S1: Time-frequency spectral analysis of neocortical bursting activity of Wwox knockout mice showing elevated coupling between low and high frequency oscillations. A, Local field potential recording of spontaneous bursting activity with a z-score normalized time-frequency spectrogram. Right-hand trace is an expanded view of the left trace with scale bar adjusted to demonstrate the high frequency activity which is coupled to low frequency intervals. B, Power spectral analysis of high (top) and low (bottom) frequency power spectra z-score normalized of a 10s trace surrounding the middle of the burst event. Data presented in mean +/- standard error. C, Phase amplitude cross frequency coupling (PAC) for the trace in A showing peak coupling in the 4-6Hz and 140-200Hz frequency ranges. D, Scatter plot of 102 bursts from 11 slices of 6 S-KO animals showing no significant correlation between the power of the low frequency phase signal where there is maximal coupling and the cross frequency coupling index (Icfc) obtained at the maximal coupling strength (rho = 0.1283, p = 0.1988; Pearson Correlation Coefficient). E, PAC for a second example burst showing coupling between delta and gamma frequencies. The peak coupling range is indicated by the black boxes. For summary of peak coupling ranges for all bursts, see supplementary table S1. F, Scatter plot of 41 bursts from 5 slice of 1 S-KO animal showing no significant correlation between the power of the low frequency phase signal where there is maximal coupling and the Icfc obtained at the maximal coupling strength (rho = -0.1201, p = 0.5674; Pearson Correlation Coefficient). G, Rho and p values for 126 bursts in 18 slices of 9 animals showing no significant correlation or negative correlation in 8/9 of the subjects.

Supplementary Figure S2: Examples of simultaneous local field potential (LFP, top) and whole cell (WC, bottom) recordings at various holding potentials. 

Supplementary figure S4.A, a1, Frequency of action potentials relative to raw injected current strength for increasing stimulus amplitudes for pyramidal neurons (Significance shown for knockout compared to wildtype; * (from left to right) p = 0.012443 unpaired t-test; p = 0.023729 unpaired t-test, p = 0.034794 rank sum test, p = 0.04364; rank sum test). Data presented in mean +/- standard error. a2, Frequency of action potentials where zero injected current represents 20pA below rheobase for each pyramidal neuron (p > 0.05 for all combinations tested, unpaired t-test). B, b1, Frequency of action potentials relative to injected current strength for increasing stimulus amplitudes for interneurons (p > 0.05 for all combinations tested, unpaired t-test). b2, Frequency of action potentials where zero injected current represents 20pA below rheobase for each interneuron (p > 0.05 for all combinations tested, unpaired t-test). For n’s see table 1.

## Task 1: read Supplementary Figure S4, all four panels

For every current step give the value and error-bar half length of every group in a1 and a2 (state your read error), and describe b1, b2. Label every number by panel, group and printed x position. State what kind of statistic each panel appears to plot and anything in the figure that does not fit the caption.

## Task 2: judge these sentences against Supplementary Figure S4

F-a: "(a) *Firing:* the source also states that 'there was no significant difference in the slope of the curve' of the frequency-current relation and writes 'Since these data suggest that the hyperexcitability of the network was not due to action-potential dependent frequency changes'; the Abstract and Discussion do say increased action-potential frequency, which rests partly on Supplementary Fig S4 (not held), so the source is internally mixed on firing."

F-b (judge only the words "increased firing"; F-a belongs to the same record): "Layer 2/3 pyramidal neurons show increased excitatory drive, reduced spontaneous inhibition, depolarization, increased firing, increased sag and post-inhibitory rebound."

The words "(not held)" are already known to be wrong (the file is held) and do not count.

Apply these rules, fixed before the read. Where a rule's premise is not established by the figure, say so and give the verdict under each reading.

## 3. Verdict rules (S4), fixed now

Categories per sentence: **UNCHANGED** (the figure agrees with the sentence as worded), **ADD** (agrees; the figure offers a more precise condition that the sentence does not need in order to be true), **MUST CHANGE** (the figure contradicts it, or the sentence is true only under a condition it does not state, so that a reader would draw a different inference).

* Figure pattern **P1** (raw current, a1): at every starred step, S-KO mean above S-WT mean.
* **P2** (aligned to rheobase, a2): no step where S-KO exceeds S-WT by more than 2 combined SEM.
* **P3** (range): list the steps where S-KO mean is not above S-WT in a1.
* **P4** (genotype specificity): at the starred steps of a1, is S-HT within 1 combined SEM of S-KO (then the excess is not shown to be specific to homozygous loss in this figure).
* **P5** (interneurons, b1/b2): no step with a difference over 2 combined SEM.
* F-a: UNCHANGED if P1 holds and the figure carries both a raw-current excess and an aligned null (so "rests partly on S4" and "internally mixed" stand). MUST CHANGE if P1 fails, or the stars mark a comparison other than S-KO against S-WT, or P2 fails at two or more consecutive steps (the figure would then show an excess after alignment, against "no significant difference"). Otherwise ADD.
* F-b: UNCHANGED if S-KO exceeds S-WT in both a1 and a2. MUST CHANGE if the excess is present only with raw current (P1 holds and P2 holds) AND no sentence in the same claim record already says that the excess is absent once current is referred to rheobase, or if P1 fails. If P1 and P2 hold and the claim record already says it (update (a) is part of the record), ADD, with the words that would carry the condition.


## Task 3: judge these record sentences against S1, S2 and S4

C1: "S1 (phase-amplitude coupling controls: low-frequency power versus coupling index uncorrelated, animal-level significance in 8 of 9 for delta)"

C2: "S2: -70 mV burst shows inward transients with a high-frequency component; 0 mV shows large high-frequency events of the order of 380 pA scale; S4 a1: KO and HT f-I curves lie above WT from about 60 pA (stars at four stimulus steps), a2 (aligned to rheobase) the three curves overlap; b: interneuron curves overlap with wide error"

C3: "bursting recorded in slices, whole-cell recordings separate" (context: a row about burst counts in slices of knockout, heterozygote and wildtype mice and about intrinsic properties measured in patched neurons)

C4: "the burst is a network event recorded as an LFP; whole-cell data come from separate cells (Results 2.2; Supp S2 shows burst currents of several hundred pA at -70 mV in the patched cell)"

C5: "Neuron-specific Wwox loss is associated with spontaneous neocortical bursting activity, altered oscillatory organization and increased phase-amplitude coupling." (judge only against what S1 can bear on)

Judge each sentence part by part with the categories UNCHANGED / ADD / MUST CHANGE, using:

**Matching rule.** A repository sentence "uses" a figure if (i) it cites Breton for the statement and (ii) it states a number, band, count, unit, correlation, or a qualitative fact about coupling and its relation to power or across animals (S1), or about what a cell does during a burst or at a holding potential (S2), that the figure is the source of or bears on. **Change** = the figure contradicts it, or narrows it so that MUST CHANGE applies in the sense of section 3. A fact the figure only adds is ADD and is not a change. A sentence about another paper that shares a word is not a hit.


Animals are the unit of replication for inference. If a sentence can only be settled by something these files do not contain, mark it UNSETTLED and say what is missing; do not turn "not shown here" into "does not exist".

## Output

Write `REPORT.md` in this folder: the S4 table, the verdicts with one or two sentences of reason each, and limits. Final reply: the verdict list only (under 200 words).
