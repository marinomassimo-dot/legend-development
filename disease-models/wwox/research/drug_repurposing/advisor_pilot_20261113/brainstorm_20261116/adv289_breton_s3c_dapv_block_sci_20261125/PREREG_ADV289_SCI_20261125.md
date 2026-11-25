# PREREG ADV-289 (SCI, window cfe92e9d): Breton 2021 Supplementary Fig. S3C, d-APV block of the delayed evoked response, and the upper arm of the matched-depth series

Frozen 2026-11-25T23:4xZ (the commit time and the file sha256 are recorded in the commit and in the result file), BEFORE S3C, S3B or the Methods of Breton 2021 were opened in this window. Hypothesis level; mechanism labels only; no dose; nothing here is medical advice; reference genotype class only; not a WWOX therapeutic result.

## 0. What I already know, stated so the reading is not called blind

* The predecessor window read S3B/S3C by eye and wrote the values into checkpoint AP and the ADV-289 brief: S3C d-APV about 0.4 of baseline at 40 to 100 uA, returning on washout; S3B delayed response KO about 0.46 mV, WT about 0.115 mV at 100 uA (6 slices/3 KO animals; 7/4 WT). I have read those sentences, so MY reads are not blind to them. The independent check is the one blind reader (section 6), who receives the figure and caption without any value.
* The brief 13.11 text (original Design bullet) and the package already name a deep depth of at least one half of the evoked response beside the intermediate depths 0.1, 0.2, 0.3. The ADV-289 question speaks of a series "about 0.05 to 0.30"; whether the package already has a deep arm is a premise to be checked in section 4, not assumed.

## 1. Question and rejecting observation (fixed)

Question: at the d-APV concentration that eliminated spontaneous bursts in S-KO slices (50 uM; n = 51 bursts, 5 slices, 3 animals, as the held brief states from the main text), what fraction of the delayed NMDAR-dependent field response was blocked (S3C), and does that held point fix the upper end of the matched fractional-block depth series?

Rejecting observation (ADV's, adopted unchanged): the ADV-289 proposition is rejected if EITHER (a) the d-APV amplitude in S3C is at or above 0.7 of baseline (block at or below 0.3), OR (b) S3C is not tied to the burst experiment (rule in section 2).

## 2. Rule that ties S3C to the burst experiment (fixed before reading Methods and caption)

Read the Methods, the caption of S3 and the main text sentence that cites S3. Classify exactly one of:

* TIED_SAME_SLICES: the text or caption states that the S3C slices are (some of) the slices of the burst experiment, or that the same recording sessions contain both.
* TIED_SAME_CONDITIONS: slice identity is not stated, but ALL of these are stated or printed: genotype S-KO, the same d-APV concentration (50 uM), the same age window (P13 to P17) and the same preparation (coronal neocortical slices). The result is labelled "conditions match, identity not shown" and the limit is carried into every sentence.
* NOT_TIED: the concentration differs or is not stated for S3C, or the genotype or age differs, or the caption does not say d-APV was applied to the delayed response, or S3C is a different preparation (for example whole-cell, a different region, or a different drug).

Only NOT_TIED triggers rejecting observation (b). If a needed fact is absent from the held text it is "NOT STATED", and then the class is NOT_TIED unless the other facts are printed (the two tied classes need all conditions).

## 3. Reads (fixed)

* Medium: the held raster image (`files/supplement/PMID34634460_r2/image3.tiff`, converted to PNG) and the caption in `mmc1.docx`/`mmc1_text.txt`. The reading is a GRAPH READ, not a value from a table; every number carries its read error.
* Primary quantity: the ratio R = (d-APV amplitude) / (baseline amplitude) at the stimulus intensity of 100 uA (the intensity the S3B numbers use), and BLOCK = 1 - R. Secondary: R at each other intensity printed (about 40 to 100 uA). If S3C plots per-slice or per-animal points, read each and record which animal each belongs to when the figure or caption allows it; otherwise report the plotted mean and the plotted error bar and say the points are not recoverable.
* Method: pixel calibration against the two axis ticks nearest the point on each axis, three independent reads of each point (different crops), stated error = half the spread of the three reads plus one pixel converted to axis units. Report R with that error.
* Washout: read the washout value at the same intensity and state whether it returns within 10% of baseline.
* Baseline amplitude also read from S3B (KO at 100 uA) and compared with the S3C baseline, to check that the two panels describe the same quantity (same units, same intensity).

Decision on the primary read: point R at or above 0.7 = rejected (a). Point R below 0.7 but with its upper error bound at or above 0.7 = INDETERMINATE (not rejected, not confirmed, the limit stated). Both point and upper bound below 0.7 = not rejected on (a).

## 4. Placement and the upper-arm rule (fixed)

* Premise check first: open the brief 13.11 original Design bullet, Addendum 14 and `SLICE_PACKAGE_V2_CONSOLIDATED.md` and record in one line each what depths they name ("deep, at least one half", "about 0.1, 0.2, 0.3", "plus one deep depth").
* Place the held BLOCK on the depth axis. The model's own statement (hypothesis generator, assumed linear map from evoked depth to NMDAR weight): about 30% of the burst rate lost at 10% loss of weight, half at 15 to 20%, floor at deep block. The held point can be compared with the model only as follows: it is one point (bursts abolished at BLOCK of about the read value), and the model predicts abolition at any depth well beyond 0.2, so the held point is CONSISTENT with the model's prediction and does not test its steep intermediate range. Say so.
* The depth series needs an UPPER ARM if, and only if: the package/brief has no deep depth defined, OR its deep depth is defined by a lower bound that sits clearly below the held BLOCK (so a laboratory could meet "at least one half" with a block that never reached the value at which d-APV abolished bursts). If the package already defines a deep depth at least one half, the answer is: the held point does not add an arm; it can fix the deep arm's REFERENCE value (the d-APV block at which bursts were abolished in the published preparation), and the sentence of the package may name it with its read error and its limits. Whichever holds, state what each consumer sentence (package, brief, F04 card) should say, as a proposed replacement sentence, not an edit.

## 5. Statistics and units (fixed)

* Unit of analysis: the animal, slices nested. The paper's t-tests use slices as n (the main text and the legend are checked for this); S3C is paired baseline/d-APV data, so an unpaired test on it would discard the pairing: say so. I run no new inferential test on S3B/S3C; I compute descriptive ratios with their read error, and, if per-slice points are recoverable, the animal-level means. Every statistic is labelled (descriptive ratio from a graph read; not a test).
* The S3B KO/WT ratio, if stated, is also a graph read and carries its error.

## 6. Independent reading (fixed)

One blind reader (a `legend-delegate`, model sonnet-5-5 default for the harness, effort high stated in the dispatch) is given: the Methods, the caption of S3 and the sentences of the main text that cite S3, and the whole figure (all panels) as PNG; and the questions: tie class (section 2), R at 100 uA and at the other intensities with error, whether bursts and S3C are the same slices, n of slices and animals, and washout. It is NOT given: the predecessor's values, my reads, this PREREG's thresholds. It is told the repository files to avoid are none beyond the Breton folder, and that "not held" must first be checked by listing `files/supplement/PMID*` and `files/figures/PMID*`. Its report is compared with mine row by row; a disagreement on R larger than the sum of the two stated errors is reported as a disagreement, not averaged.

## 7. Outputs (fixed)

`RESULT_ADV289_SCI_20261125.md` with: the tie class and the exact words that carry it; R and BLOCK with errors at each intensity; the premise check; the placement; the upper-arm decision; proposed replacement sentences for the consumers (package, brief 13.11, F04 card, `nmdar_pharmacology_it6_p9_20261029` E2), each with its limits; the blind-reader comparison; DEFAULTS_TAKEN. Read: wording rule applies to my own sentences (no absolute words without their check: "the only", "largest", "every", "independent", "first", "no").
