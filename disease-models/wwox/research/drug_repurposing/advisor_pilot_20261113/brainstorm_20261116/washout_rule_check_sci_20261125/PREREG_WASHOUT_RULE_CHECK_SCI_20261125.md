# PREREG: does the brief's washout reading rule need a two-sided bound or a different reference? (SCI, window cfe92e9d; ADV direction after ADV-289; hypothesis level; not medical advice; no dose; reference genotype class only)

Frozen before any consumer file was searched for the rule and before the model's washout cases were re-opened. Time and sha256 are in the commit and in the result file.

## 0. The rule under test and what I already know

The rule (brief 13.11 Addendum 14, `EXPERIMENT_BRIEF_V1_1.md`; carried in `SLICE_PACKAGE_V2_CONSOLIDATED.md`): a fall of the burst rate to 0.7 of its pre-exposure value or lower is called a lasting change only if the evoked delayed response is back within 10 percent of its baseline; otherwise it may be block that has not washed out. The 10 percent was derived from the toy model, where every fall that came from a slow unblock had the evoked response at least 22 percent below baseline (window mean) and a residual of about 8 percent gave a rate of 0.8. I know from ADV-289 that in the held experiment the evoked response after washout is ABOVE baseline (1.3 at 100 uA, 1.5 at 40 uA, by graph read) and that the held burst washout bar is about 1.8 (Fig. 3D, held reading). Question: is the rule fine as written?

## 1. The grid (fixed)

Burst-rate class at a post-washout read, against the pre-exposure value: FALL (at most 0.7), BAND (above 0.7 and below 1.3), REBOUND (at least 1.3; the classes of P3 of the hashed priors file). Evoked-response class against its baseline: LOW (below 0.9), NORMAL (0.9 to 1.1), HIGH (above 1.1). Nine cells.

## 2. What counts as covered (fixed)

A cell is COVERED if the brief, the package or the model result states, for that cell, what inference the laboratory may draw (an inference that names the cell's evoked class). A cell is SILENT if no sentence assigns an inference. The held data populate two cells: (REBOUND, HIGH) from the 1.8 burst bar with the 1.3 evoked read, and (BAND, HIGH) from the text's "returned to normal" with the same evoked read; they are populated by different readings of different slices and paradigms, so I treat them as the cells the rule MUST handle, not as a joint observation.

## 3. Uses of the rule (fixed)

Search the repository tree under `disease-models/wwox/research/drug_repurposing/` (and `files/` text of outreach pages if present) for the strings "within 10", "back within", "lasting change", "0.7 of its pre-exposure", "has not washed out" and "residual block"; list every file and sentence that states the rule or relies on it, with its band and its reference. Readouts that share the rule are those whose own sentence uses the evoked response as a gate on a post-washout burst change.

## 4. Rejecting observation (named before looking)

The proposition "the rule is fine as written" is REJECTED if ANY of:
* R1: two uses of the rule state different bands, different references (baseline, time-matched vehicle, d-APV) or different directions;
* R2: either of the two populated cells (REBOUND, HIGH) or (BAND, HIGH) is SILENT in the brief, the package and the model result;
* R3: the model result (Part B) contains a case whose evoked response is HIGH after washout and the rule classifies it in a way the same file contradicts, or the model contains no case with a HIGH evoked response (the high side is NOT REPRESENTED there, which I would then state, and it does not by itself reject).
R3's second clause is reported but does not reject. If none of R1 or R2 holds, the rule is fine as written for the two populated cells and the reference question is answered separately (section 5).

## 5. The reference question (fixed)

The rule's reference for "baseline" is the evoked response before exposure. The held figure has no time-matched control without d-APV (blind reader of ADV-289), so a washout value of 1.3 cannot be separated from drift. The check states whether the package's vehicle arm (time-matched) already gives the evoked response a drift reference, and whether the rule names it. If the rule's wording says "baseline" and the design records the evoked response in the time-matched vehicle slices, the answer is: reference = the vehicle's evoked response at the same time, stated; if the vehicle's evoked response is not recorded, the design needs it.

## 6. Output (fixed)

`RESULT_WASHOUT_RULE_CHECK_SCI_20261125.md`: the list of uses; the nine-cell table with COVERED or SILENT and the sentence that covers it; the verdict against R1 to R3; if rejected, one proposed replacement sentence (two-sided, with the reference) as text only, not an edit of any consumer; DEFAULTS_TAKEN; about 45 minutes, held sources only, no delegate unless a count has to be rechecked blind.
