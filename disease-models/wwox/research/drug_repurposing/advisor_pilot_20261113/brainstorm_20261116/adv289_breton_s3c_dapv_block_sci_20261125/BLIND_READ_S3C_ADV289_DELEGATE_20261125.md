# BLIND READ of Breton et al. 2021 (Neurobiol Dis 160:105529), Supplementary Fig. S3C versus the d-APV burst experiment

Reader: blind reader (verifier role). Setting: model sonnet (claude-sonnet-5-5), effort high.
Hypothesis level only. Nothing here is medical advice. No dose. Reference genotype class only.

Inputs read in full: `breton2021_main_text.txt` (165 lines, every line read, including Methods and
the reference list), `supplement_captions.txt` (all 40 lines) and
`supplementary_figure_S3_whole.png` (1431 x 801 px, panels A, B, C). No other file was opened and
nothing was searched on the web. Anything not in these three is written NOT STATED.

Quote locators used below: "Results 2.2" is the section "Gap junctional blockade reduces, whereas
glutamatergic blockade abolishes, spontaneous bursting activity". "Fig. 3 caption" is the caption
of main-text Fig. 3. "S3 caption" is the "Supplementary figure S3" paragraph of the supplement
captions. "Methods 5.x" and "6.7" are the numbered Methods sections.

---

## 1. The burst experiment (spontaneous bursts, d-APV applied)

- **d-APV concentration: 50 uM.**
  - Fig. 3 caption: "Examples of the bursts under D-(−)-2-Amino-5-phosphonopentanoic acid (d-APV, 50 μM), carbenoxolone (CBX, 100 μM) and brilliant blue FCF (BB-FCF, 10 μM)."
  - Results 2.2: "Blocking glutamatergic neurotransmission with d-APV (50 μM) eliminated the spontaneous bursting events, as recorded from an LFP placed in the superficial neocortical layer."
  - Methods 5.4: "...for a final concentration of 1 μM TTX, 50 μM d-APV, 100 μM CBX, and 10 μM BB-FCF."
  - This 50 uM is the only d-APV concentration anywhere in the packet.
- **How many bursts, slices, animals.** Fig. 3 caption, last sentence of D: "n = 51 bursts, 5 slices, 3 animals d-APV; n = 36 bursts, 4 slices, 3 animals CBX; n = 73 bursts, 6 slices, 3 animals BB-FCF".
  - Supplementary Table S1 has only Baseline, CBX and BB-FCF columns and no d-APV column. Its N's row ("N's (bursts/slices/animals)") reads "119/18/ 9", "13/6/3", "25/6/3". Table S1 and the Fig. 3 caption disagree for CBX (13/6/3 against 36 bursts, 4 slices, 3 animals) and BB-FCF (25/6/3 against 73 bursts, 6 slices, 3 animals). The text agrees with Table S1 on BB-FCF ("in 10 of 25 bursts evaluated").
  - So the paper's own burst counts are not self-consistent. For d-APV the only count is 51 bursts, 5 slices, 3 animals.
  - How many bursts were scored in the d-APV condition itself is NOT STATED. The text says d-APV "eliminated" the bursts, so the 51 presumably counts the baseline bursts. That reading is mine, not the paper's.
- **Genotype.**
  - Results 2.2, first sentence: "We next sought to investigate how the neocortical bursting activity was generated in the Wwox S-KO mouse brains."
  - The Fig. 3 caption does not name a genotype.
  - Results 2.1 says bursts were found in "0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice". Whether every one of the 5 d-APV slices was S-KO is not stated beyond the Results 2.2 sentence.
- **Age window.**
  - Methods 5.1: "Both male and female mice aged P13 to P17 were humanely sacrificed for these experiments".
  - Results 2.1: "We recorded local field potentials (LFPs) from 13 to 17 day old S-KO, S-HT, and S-WT littermate mouse neocortical and hippocampal slices".
  - Discussion 3.4: "the recordings were obtained at P13-17".
  - No separate age is given for the d-APV slices.
- **Preparation and recording site.**
  - Methods 5.2: "The neocortex and hippocampus were sectioned coronally 400–500 um thick ... using a Leica 1200 vibratome", and "Slices were kept at 35 o for 30 min, after which they were removed to room temperature for at least 60 min prior to experimentation at 35 o." (the degree sign is stripped in the packet text).
  - Results 2.2: the LFP was "placed in the superficial neocortical layer". Results 2.1 says bursts were larger in layer II/III than in layer V, and burst timing was taken in layer II/III.
  - The d-APV experiment had no stimulation.
- **Protocol.**
  - Results 2.2: "Upon observing at least three bursting events, indicating consistent bursting activity in the neocortical slice preparations, the slices were perfused with a glutamatergic blocker, d-APV, ...".
  - Results 2.2: "Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal."
  - Statistics (Fig. 3 caption): "Unpaired t-test with Bonferroni's correction".

---

## 2. What Supplementary Fig. S3 shows

S3 caption, title: "NMDA-receptor blockade suppresses delayed field-evoked activity between neocortical layer V and layer II/III."

**Panel A.**
- Caption: "Examples of field evoked responses in layer II/III in the wildtype controls (S-WT) as compared to the knockouts (S-KO) at various positions in the deep neocortical layer relative to the recording electrode (top – along the same cortical column, bottom – in the adjacent cortical column). The caret '^' symbol shows the peak of the delayed evoked response used to calculate the amplitude."
- Figure: traces labelled "WT" (black) and "KO", with a legend baseline (red), d-APV (dark grey) and washout (light grey). The KO traces carry the three colours overlaid. The WT traces are black only, with no drug trace. Scale bars: 0.5 mV and 100 ms; the inset has 0.5 mV and 5 ms.
- No d-APV concentration appears in panel A or in the caption.
- Stimulation and recording sites (Results 2.2): "an electrical stimulator was placed in layer V, and the local field potential response to 0.1 ms stimuli was recorded in layer II/III".

**Panel B.**
- Caption: "Amplitude of the delayed evoked response for the S-WT as compared to the S-KO mice ('*' indicate significant points as compared to baseline stimulation. from left to right, p = 0.5713, 0.4207, 0.1554, 0.011, 0.0092, 0.0038, unpaired t-test; n = 6 slices, 3 animals S-KO, n = 7 slices, 4 animals S-WT)."
- Genotypes: S-KO and S-WT. No drug.
- The colour key is not printed in B. By A's trace colours, black is WT and red is KO. That mapping is my inference.
- Six p values mean six stimulus strengths. Stars sit at 40, 50 and 100 uA, which are the 4th to 6th values (0.011, 0.0092, 0.0038).
- The star criterion is ambiguous. "As compared to baseline stimulation" could mean KO against WT at each strength (Results 2.2 says "The delayed response in the S-KOs was larger than that of the S-WTs at multiple stimulus strengths"), or each point against the lowest stimulus. Both readings are possible. An unpaired t-test on 6 against 7 slices fits the first.
- Slice and animal numbers: S-KO 6 slices, 3 animals; S-WT 7 slices, 4 animals.
- **Inconsistency with the main text.** Results 2.2: "This peaked at 97 ± 31 ms (mean ± standard deviation, n = 6 animals) after the stimulus onset." The caption gives 6 slices from 3 animals for S-KO. Either the main text's "6 animals" is a slip for 6 slices, or the latency was measured on a different set. The packet does not say which.

**Panel C.**
- Caption: "Amplitude of the delayed evoked response at baseline, during d-APV treatment, and after washout. Data was normalized to a stimulus strength of 100μA. (p values relative to baseline for d-APV treatment are (left to right) 0.4798, 0.6458, 0.1692, 0.0229, 0.0103, 0.0006; p-values relative to baseline for washout (left to right) are 0.9425, 0.2524, 0.1975, 0.0492, 0.0372, 0.0499. unpaired t-test n = 6 slices, 3 animals)."
- **Genotype is NOT STATED in the caption of C or in the figure.** It is implied: the legend sits on the KO traces in A, and Results 2.2 says the delayed deflection was "in the Wwox S-KO slices that was not observed in the wildtype controls" and that "This delayed response was NMDA receptor mediated, as addition of d-APV reversibly suppressed the response (Supplementary Fig. S3C)".
- **d-APV concentration is NOT STATED for S3C** (not in the caption, not in the Results sentence). Methods 5.4 gives only the single 50 uM.
- Slices and animals: 6 slices, 3 animals, given once for all three conditions.
- Stars: black stars below the dark grey points at 40, 50 and 100 uA (d-APV against baseline, 0.0229, 0.0103, 0.0006). Black stars above the light grey points at the same three strengths (washout against baseline, 0.0492, 0.0372, 0.0499). The washout stars therefore mark a washout that differs from baseline, not a return to it.

**Error bars.**
- NOT STATED in the S3 caption for B or C.
- Elsewhere the paper states SD or SEM for other figures: Fig. 6B "average ± SEM"; Supp. Fig. S1B "Data presented in mean +/- standard error"; Supp. Fig. S4 "mean +/- standard error". None of these refers to S3.
- Graph reads (see 4) show the bars are asymmetric about the marker at some strengths. In B (KO) at 100 uA: marker 0.458 mV, bar about 0.244 to 0.479 mV. At 50 uA: marker 0.411, bar about 0.214 to 0.450. In C (washout) at 100 uA: marker 1.30, upper cap about 1.93, lower cap hidden below about 1.07. So they cannot be read as symmetric ± SD or ± SEM everywhere.

**Normalisation in C.**
- Caption: "Data was normalized to a stimulus strength of 100μA."
- Possible readings:
  - (a) each slice's amplitudes divided by that slice's own baseline amplitude at 100 uA.
  - (b) all values divided by the group-mean baseline amplitude at 100 uA.
  - (c) each condition divided by its own 100 uA amplitude.
- The figure excludes (c): d-APV at 100 uA is about 0.40 and washout about 1.30, not 1.
- The baseline marker at 100 uA sits at 1.00 with no visible error bar, as expected if every slice is divided by its own baseline at 100 uA (a). Under (b) a spread would remain. This is an inference from the picture, not a statement.

**Test and unit.**
- Test: "unpaired t-test" (S3 caption, B and C). Methods 6.7: "An unpaired t -test was used when there were two groups and a normal distribution", and "A Bonferroni post-hoc correction was applied in each case for tests of multiple comparisons."
- The S3 caption does not say whether the printed p values are corrected. The washout star at p = 0.0499 shows the stars use an uncorrected 0.05 threshold. With six comparisons per condition a Bonferroni threshold would be 0.0083 (my arithmetic).
- The unit of the test is NOT STATED. The n is quoted as "6 slices, 3 animals". If slices were the unit, slices from 3 animals were treated as independent. That is my reading, not a statement.

**Paired or not in C.**
- Wording: "unpaired t-test". Design: one n for baseline, d-APV and washout, and washout presupposes the same tissue. The 100 uA baseline at exactly 1.00 with no bar supports per-slice normalisation, which gives a paired structure. So the data look repeated-measures on the same 6 slices, but they are tested as unpaired.
- It is NOT STATED in so many words that the three conditions are from the same slices.

---

## 3. Tie class of S3C to the burst experiment

**Class: NOT_TIED, by the literal rule you gave. The stated alternative reading gives TIED_SAME_CONDITIONS, labelled "conditions match, identity not shown". TIED_SAME_SLICES is excluded under every reading.**

Checks against the definitions:
- **TIED_SAME_SLICES fails.**
  - No sentence says S3C slices are, or include, the burst slices, or that one recording session had both.
  - The slice counts differ: S3C is "n = 6 slices, 3 animals", the burst d-APV set is "n = 51 bursts, 5 slices, 3 animals". Six is not five, so the sets cannot be identical. Whether they overlap is NOT STATED.
  - The paradigms differ: spontaneous LFP bursts with no stimulation against layer V stimulation (0.1 ms pulses every 30 s) with a layer II/III LFP and amplitude taken at the roughly 97 ms delayed deflection.
- **TIED_SAME_CONDITIONS needs four facts.**
  - Genotype S-KO for S3C: not in the C caption. It is printed only as the "KO" label on the A traces that carry the drug legend, and implied by the Results 2.2 sentences quoted above.
  - Same d-APV concentration: NOT STATED for S3C. Only Methods 5.4 (50 uM, generic for the paper) and the Fig. 3 caption (50 uM, bursts) give one.
  - Same age window: P13 to P17 for all animals (Methods 5.1).
  - Same preparation: coronal neocortical slices 400–500 um, 35 degrees (Methods 5.2). The recording site differs by paradigm.
- **Which rule applies.** Your NOT_TIED clause says "the d-APV concentration differs or is not stated for S3C". It is not stated for S3C (caption and Results sentence), so the literal rule gives NOT_TIED. If Methods 5.4 is read as covering every d-APV application in the paper, concentration and age match, and the genotype can be accepted from the printed "KO" in A, the class becomes TIED_SAME_CONDITIONS. These are two readings of one body of text; I do not merge them.

**Confidence.** I am sure (high) that TIED_SAME_SLICES is not supported. I am only moderately sure between NOT_TIED and TIED_SAME_CONDITIONS, because it turns on whether a generic Methods concentration counts as stated for S3C.

**What would change the class.**
- To TIED_SAME_CONDITIONS: a sentence in the S3 caption or Results such as "S-KO slices were treated with 50 μM d-APV".
- To TIED_SAME_SLICES: a sentence such as "the slices of Fig. 3 were also stimulated" or "d-APV (50 μM) was applied to the slices of Fig. 3 and S3C", with the slice counts reconciled (6 against 5).

---

## 4. Graph reads from the figure

**These are graph reads from the raster image, not table values.** The paper gives no table of the plotted means. The PNG is 1431 x 801 px.

**Calibration.**
- Y ticks are short marks inside the plot at the right of the y axis. I located them from pixels.
- Panel B: 0.5, 0.4, 0.3, 0.2, 0.1 mV at rows 45, 98.5, 152, 205.3, 259. That is about 534.8 px per mV, with a maximum linear-fit residual of 0.00026 mV.
- Panel C: 2, 1.5, 1, 0.5 at rows 410, 470.5, 531, 591. That is about 120.7 px per unit, with a maximum residual of 0.0017.
- X ticks: 0 at column 960.5, 50 at 1152.5, 100 at 1344.5, so 3.84 px per uA. Only 0, 50 and 100 are labelled. The other strengths below are placed by this scale.
- The x axis does not sit at zero. It crosses the y axis at about 0.070 mV in B and about 0.095 normalised units in C.

**Three reads per value.** These are three pixel methods on the same image, run independently:
- (1) template fit of a disk of radius 8 px to the marker colour mask;
- (2) the row of maximum horizontal chord width;
- (3) the vertical extent on a flank column about 6 px from the marker centre, away from the error bar.

Central value = median of the three. Error = largest deviation of any read from the central value + calibration residual + half a pixel.
- Read (3) is biased low for the dark marker at 100 uA by the darker marker outline, which falls outside the grey colour mask. Pixel dump and cap midpoints (caps at rows 593 and 611, midpoint 602) support about 0.405. I kept the biased read in the error rather than drop it.
- Read (2) is pulled off the true centre by the dashed line for the washout marker at 40 uA, which is why that row has a large error. Reads (1) and (3) agree there.

**Panel B, amplitude (mV), at each strength.**

| Stimulus (uA) | KO (red) | WT (black) |
|---|---|---|
| 100 | 0.458 ± 0.002 (reads 0.459, 0.457, 0.458) | 0.116 ± 0.003 (0.116, 0.114, 0.116) |
| 50 | 0.411 ± 0.004 | 0.115 ± 0.002 |
| 40 | 0.340 ± 0.003 | 0.112 ± 0.002 |
| 10 | 0.166 ± 0.001 | 0.095 ± 0.003 |
| about 5 | about 0.072 (hidden by overlap) | about 0.08–0.09 (partly hidden) |

- Points that are hidden or overlapped in B: the lowest-strength KO and WT points overlap near 4 to 5 uA (the red marker sits on top of the black one), so those two values are rough. Six strengths are implied by the six p values, but only five red and four or five black markers can be told apart.
- KO error bar at 100 uA runs from about 0.244 to 0.479 mV (caps at rows 182 and 56). The WT cap at 100 uA is at about 0.132 mV.

**Panel C, normalised amplitude.** Baseline = red, d-APV = dark grey, washout = light grey.

| Stimulus (uA) | Baseline | d-APV | Washout |
|---|---|---|---|
| 100 | 0.996 ± 0.008 | 0.405 ± 0.034 (reads 0.405, 0.406, 0.377) | 1.297 ± 0.015 (1.297, 1.288, 1.297) |
| 50 | 0.907 ± 0.014 | 0.405 ± 0.009 | 1.226 ± 0.010 |
| 40 | 0.911 ± 0.007 | 0.414 ± 0.014 | 1.363 ± 0.048 |
| 10 | 0.493 ± 0.010 | 0.237 ± 0.030 | 0.841 ± 0.024 |
| about 4–5 (two lowest) | about 0.11 (only a red crescent shows, rows 633 to 644) | hidden behind the light grey circles | two light circles: about 0.26 (at about 5.3 uA) and about 0.16 to 0.20 (at about 4.3 uA, partly covered) |

- **Points seen.** Four strengths (10, 40, 50, 100 uA) have all three series clearly visible: 12 points. The two lowest strengths (about 4 and 5 uA) overlap and are only partly readable. Six strengths are implied by the six p values in the caption, so two cannot be read cleanly. The exact stimulus strengths of the two lowest points are NOT STATED (my scale puts them at about 4.3 and 5.3 uA).
- **Error bars in C (graph reads).** d-APV at 100 uA has caps near 0.485 and 0.335. Washout at 100 uA has its upper cap near 1.93 and its lower cap hidden below about 1.07. Baseline at 100 uA has no bar.

---

## 5. Ratios from the reads

The ratio errors below use only the read errors in the table, by quadrature of the relative errors. They do not include the error-bar spread, which is much larger.

| Stimulus (uA) | d-APV / baseline | 1 − ratio | Washout / baseline |
|---|---|---|---|
| 100 | 0.407 ± 0.034 | 0.593 | 1.30 ± 0.02 |
| 50 | 0.447 ± 0.012 | 0.553 | 1.35 ± 0.02 |
| 40 | 0.454 ± 0.016 | 0.546 | 1.50 ± 0.05 |
| 10 | 0.48 ± 0.06 | 0.52 | 1.71 ± 0.06 |

- At 100 uA the baseline is 1.00 by construction, so the ratio is the d-APV read, 0.405. If the biased flank read (0.377) is excluded, the error shrinks to about ±0.01. I report both.
- The two lowest strengths cannot be given a ratio because their baseline and d-APV markers are hidden.
- The ratio is not constant across strength. d-APV is a plateau of about 0.40 to 0.41 at 40, 50 and 100 uA while baseline rises from 0.91 to 1.00.
- Washout is above baseline everywhere I can read (about 1.2 to 1.7 times baseline), and the washout stars mark exactly that. This sits uneasily with the text's "reversibly suppressed" (Results 2.2).
- For B, WT / KO is 0.25 at 100 uA (0.253 ± 0.007), 0.28 at 50 uA, 0.33 at 40 uA and 0.57 at 10 uA.

**What limits "fraction of the response blocked".**
1. **Noise floor.** The amplitude is read at the roughly 97 ms point even where there is no delayed response. In B the WT slices read 0.07 to 0.116 mV, and the axis itself crosses at about 0.070 mV. A fully blocked response would not read zero.
   - Because the floor is at least zero, (1 − ratio) = 0.59 is a lower bound on the blocked fraction of the above-floor response, if the floor is the same in all conditions.
   - Conditional case only, assuming S3C slices have a raw baseline at 100 uA like B's KO mean (0.458 mV, which the paper does not state): the WT value corresponds to about 0.25 in C's units. The floor-corrected remaining fraction would be (0.405 − 0.253) / (1 − 0.253) = 0.20, a blocked fraction of about 0.80. This is a what-if, not a read.
2. **Normalisation.** The denominator is the baseline at 100 uA, and the ratio is a ratio of mean normalised values. Per-slice raw baselines are not shown. The baseline at 100 uA has no bar, so the plotted spread comes only from the d-APV and washout slices.
3. **Error bar type.** NOT STATED, and the bars are asymmetric in several places (see 2). They cannot be treated as confidence intervals of the ratio. The d-APV bar at 100 uA spans about 0.335 to 0.485, which as a bare spread of the plotted values would give a ratio range of about 0.33 to 0.49.
4. **Test and design.** Unpaired t-tests on what looks like repeated-measures data, unit not stated, uncorrected stars.
5. **Washout above baseline.** No time-matched control without d-APV is described in the packet, so drift or rebound cannot be separated from drug effect.
6. **Hidden points.** The lowest strengths cannot be read.

---

## 6. Same preparation, time course or duration of exposure as in the burst experiment?

Quotes that bear on it:
- Results 2.2 (bursts): "Upon observing at least three bursting events, indicating consistent bursting activity in the neocortical slice preparations, the slices were perfused with a glutamatergic blocker, d-APV, ..."
- Results 2.2 (bursts): "Upon washout, the frequency, duration and peak-to-trough amplitude returned to normal."
- Methods 5.3: "Current pulses of 0.1 ms duration with varying strengths were applied every 30s using a GRASS S88 stimulator ... Evoked stimuli were first repeated at a constant strength for at least 5 min to achieve inter-response stability. Then, evoked responses were done in triplicate to ensure reproducibility of results, then an average of the evoked response was reported."
- Methods 5.4: "...a final concentration of 1 μM TTX, 50 μM d-APV, 100 μM CBX, and 10 μM BB-FCF."
- Methods 5.1 and 5.2: P13 to P17; coronal 400 to 500 um slices; 35 degrees.
- Results 2.2 (S3): "This delayed response was NMDA receptor mediated, as addition of d-APV reversibly suppressed the response (Supplementary Fig. S3C)."

What the paper does NOT say that a reader would need (all NOT STATED):
- Duration of d-APV perfusion, time to a steady effect, and washout duration, in either experiment.
- Perfusion rate.
- Whether the d-APV in S3C was applied in the same recording session or slice as the bursts, or in separate slices.
- Which stimulus strengths were run in each of the three conditions, and in what order. A 6-point input-output curve in triplicate at 30 s spacing, per condition, is a long protocol compared with the burst one.
- The genotype and the d-APV concentration in S3C itself.
- Error bar type, whether p values are corrected, the unit of the test, and whether the three conditions are the same slices.
- Whether a vehicle or time-matched control without d-APV was run.
- The raw baseline amplitude at 100 uA used as the denominator.
- Which of the n = 6 slices came from which of the 3 animals, and how the "6 animals" of Results 2.2 relates to "6 slices, 3 animals" in the S3 caption.
- The exact stimulus strengths of the two lowest points.

---

## Scope note

All numbers in 4 and 5 are graph reads from the S3 PNG. Helper crops and scripts are in this folder (`crop_B.png`, `crop_C.png`, `zoom_C_low.png`, `zoom_B_low.png`, `zoom_B_low2.png`, `reads.py`, `ticks.py`, `ticks2.py`, `blobs.py`, `full.raw`). No other file was opened. I did not open `delegation_budget.md` or any other repository file, because the dispatch forbade it for blindness.
