# PREREG ADV-291 (SCI window 9bb60ab5; written before any supplement image 1, 2 or 4 was opened by this window; hypothesis level; not medical advice; reference genotype class only)

Brief: `advisor_pilot_20261113/assignments/ADV-291.md`. Source: Breton et al. 2021 (PMID 34634460), mouse (*Mus musculus*), neuron-specific Wwox knockout (S-KO) against S-WT and S-HT, neocortical slices.

## 0. What is already known when this is frozen (not blind)

Read: the captions of Supplementary Figs S1 to S4 and Table S1 (`mmc1_text.txt`); the main-text sentences on action-potential frequency (S-KO pyramidal neurons fire more than S-WT with raw current, "Supplementary Fig. S4A-a1-b1"; slope after shifting to one step below rheobase not different: S-WT 0.184 +/- 0.044, S-HT 0.162 +/- 0.037, third value printed without label 0.204 +/- 0.070 Hz/pA; WT v HT p = 0.1902, WT v KO p = 0.3669; interneurons not different, shifted or unshifted); Table 1 n (cells/animals): pyramidal S-WT 13/5, S-HT 15/6, S-KO 40/15; interneurons S-WT+S-HT 5/4, S-KO 6/5; the ADV-290 caption read of S4. Not seen: the S1, S2 and S4 images (no earlier SCI window records reading them; ADV-290 says caption only).

Image mapping from the docx relationship order and file hashes (sha256, first 16): image1 = S1 `59fde8d05a06ef62`, image2 = S2 `2ea72d39cd200ab7`, image3 = S3 `ebb9cbd48640e077`, image4 = S4 `282295d1eb8efccc`.

## 1. Sentences under test

* **F-a** (the firing sentence of `CC-20261119-ORCHESTRATOR-CLAIM021-WORDING-01`, applied in CLAIM 021, `claim_registry_current.md` line 449, update (a)): "(a) *Firing:* the source also states that 'there was no significant difference in the slope of the curve' of the frequency-current relation and writes 'Since these data suggest that the hyperexcitability of the network was not due to action-potential dependent frequency changes'; the Abstract and Discussion do say increased action-potential frequency, which rests partly on Supplementary Fig S4 (not held), so the source is internally mixed on firing."
* **F-b** (secondary, same claim, Summary): "Layer 2/3 pyramidal neurons show increased excitatory drive, reduced spontaneous inhibition, depolarization, increased firing, increased sag and post-inhibitory rebound." Judged on the words "increased firing" only.
* **F-c**: any other repository sentence that cites Breton for action-potential frequency, found by section 4.

The words "(not held)" are wrong whatever the figure shows (the file is held); they get a dated note and do not count as a result.

## 2. Read method (S4)

TIFF converted to PNG; panels cropped and enlarged; axis ticks located in pixels and calibrated from the printed tick labels; for every current step, group mean (marker centre) and error-bar end read for S-WT, S-HT, S-KO (a1, a2) and S-CTL, S-KO (b1, b2). Stated read error from pixel resolution (at least +/- 2 px), in Hz. Every value is labelled by panel, group and printed x position, never by order of appearance. The blind reader reads independently; values differing by more than the two stated errors are both reported and not merged.

**Units.** The figure shows mean +/- SEM and the tests are unpaired t or rank sum; the replicate behind SEM and tests is not printed in the S4 caption ("For n's see table 1"). I will treat it as cells (inference) and say so. Animals are the unit of replication for inference: no per-animal value is recoverable from the figure, so no animal-level test can be made and none will be implied. An approximate difference over combined SEM, sqrt(SEM1^2 + SEM2^2), is computed from the read values only as a check of the caption's p statements (EXPLORATORY, not a test).

## 3. Verdict rules (S4), fixed now

Categories per sentence: **UNCHANGED** (the figure agrees with the sentence as worded), **ADD** (agrees; the figure offers a more precise condition that the sentence does not need in order to be true), **MUST CHANGE** (the figure contradicts it, or the sentence is true only under a condition it does not state, so that a reader would draw a different inference).

* Figure pattern **P1** (raw current, a1): at every starred step, S-KO mean above S-WT mean.
* **P2** (aligned to rheobase, a2): no step where S-KO exceeds S-WT by more than 2 combined SEM.
* **P3** (range): list the steps where S-KO mean is not above S-WT in a1.
* **P4** (genotype specificity): at the starred steps of a1, is S-HT within 1 combined SEM of S-KO (then the excess is not shown to be specific to homozygous loss in this figure).
* **P5** (interneurons, b1/b2): no step with a difference over 2 combined SEM.
* F-a: UNCHANGED if P1 holds and the figure carries both a raw-current excess and an aligned null (so "rests partly on S4" and "internally mixed" stand). MUST CHANGE if P1 fails, or the stars mark a comparison other than S-KO against S-WT, or P2 fails at two or more consecutive steps (the figure would then show an excess after alignment, against "no significant difference"). Otherwise ADD.
* F-b: UNCHANGED if S-KO exceeds S-WT in both a1 and a2. MUST CHANGE if the excess is present only with raw current (P1 holds and P2 holds) AND no sentence in the same claim record already says that the excess is absent once current is referred to rheobase, or if P1 fails. If P1 and P2 hold and the claim record already says it (update (a) is part of the record), ADD, with the words that would carry the condition.

## 4. Images 1 and 2: grep list and matching rule, fixed before looking

Quantities from the captions: S1: bands 4-6 Hz and 140-200 Hz; delta-gamma coupling; 102 bursts, 11 slices, 6 S-KO animals, rho 0.1283, p 0.1988; 41 bursts, 5 slices, 1 animal, rho -0.1201, p 0.5674; 126 bursts, 18 slices, 9 animals, "no or negative correlation in 8/9". S2: simultaneous LFP and whole-cell recordings at various holding potentials (values to be read from the image).

Grep, over `disease-models/wwox/` and `framework/`, md, tsv, txt, py, restricted to files that mention `34634460`, `Breton` or `CLAIM 021`: PAC; phase-amplitude; phase amplitude; cross-frequency; 140-200; 4-6 Hz; 102 bursts; 126 bursts; 41 bursts; holding potential; whole-cell; whole cell; simultaneous; reversal; Fig S1; Fig S2; Figure S1; Figure S2; action potential frequency; action-potential frequency; increased firing; rheobase; frequency-current (en dash variants included).

**Matching rule.** A repository sentence "uses" a figure if (i) it cites Breton for the statement and (ii) it states a number, band, count, unit, correlation, or a qualitative fact about coupling and its relation to power or across animals (S1), or about what a cell does during a burst or at a holding potential (S2), that the figure is the source of or bears on. **Change** = the figure contradicts it, or narrows it so that MUST CHANGE applies in the sense of section 3. A fact the figure only adds is ADD and is not a change. A sentence about another paper that shares a word is not a hit.

## 5. Rejecting observation (from the brief, operationalised)

If F-a is UNCHANGED or ADD (S4 agrees with the CLAIM 021 firing sentence as worded) **and** no repository sentence is MUST CHANGE from S1 or S2, the series closes as "nothing changes" apart from a dated "S3, S4 and Table S1 are held" note on the three places named in the brief. F-b and F-c are reported beside it and do not alter this rule; a MUST CHANGE on F-b or F-c is reported as its own result.

## 6. Blind reader

One `legend-delegate`, model sonnet, effort high (read back from its transcript). It receives the sentences of section 1, the whole S4 image and caption, the S1 and S2 images and captions, the Table 1 n line, the section 3 rules, and the S1/S2 candidate sentences from the section 4 grep. It does not receive my read values or verdicts, the main-text sentences beyond what the sentences under test quote, or any earlier record on these figures. My own S4 read is written to a file before the reader's report is opened.
