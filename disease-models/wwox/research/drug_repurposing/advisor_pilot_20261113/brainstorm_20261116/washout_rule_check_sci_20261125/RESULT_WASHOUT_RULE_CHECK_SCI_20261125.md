# RESULT: the brief's washout reading rule against the held evoked overshoot (SCI, window cfe92e9d, 2026-11-25; ADV direction after ADV-289; hypothesis level; MODEL statements are labelled; not medical advice; no dose; reference genotype class only)

PREREG: `PREREG_WASHOUT_RULE_CHECK_SCI_20261125.md`, sha256 `8ab53116f635efbaec80db475c1dab8cecf18210ee8ec6614618c1903a0a27f7`, frozen 2026-11-25T23:57:44Z (commit `fc87bba4c`) before the consumer search and before the model's washout table was re-opened. Search run on `development/main` at `c707b5ae4` (2026-11-25), strings "within 10", "back within", "lasting change", "0.7 of its pre-exposure", "has not washed out", "not washed out", under `disease-models/wwox/research/drug_repurposing/`, files of type md and txt; json, jsonl and tsv files excluded.

## 1. Verdict

**"The rule is fine as written" is REJECTED by the rejecting observation R2, not by R1.** The rule covers a fall of the burst rate; the two cells that the held data populate, a rebound with a raised evoked response and a rate inside the band with a raised evoked response, had no sentence in the brief, the packages or the model result that the search of section 2 found (limits in section 6). The reference of "baseline" is also unstated for drift. One replacement sentence is proposed (section 5), as text only.

## 2. Uses of the rule (R1: same band, reference and direction?)

| use | where | wording that matters |
|---|---|---|
| U1 | `EXPERIMENT_BRIEF_V1_1.md` line 180 (Addendum 14, the source) | fall at 30 to 120 min, at most 0.7; lasting only if evoked "back within 10% of its baseline"; reports precision; derivation: "every such fall that came from a slow unblock had the evoked response at least 22% (window mean) below baseline", residual about 8% gave rate 0.8 |
| U2 | `SLICE_PACKAGE_V2_CONSOLIDATED.md` line 23 | "a fall of the burst rate to 0.7 of its pre-exposure value or lower is called a lasting change only if the evoked response is back within 10% of its baseline; otherwise it may be block that has not washed out" |
| U3 | `OPERATOR_OUTREACH_PACKAGE_SCI_20261118.md` line 21 | the same sentence as U2 |
| U4 | `PART_B_RESULT_ADV046_SCI_20261118.md` line 49 (what this changes, 3) | "back within 10% of baseline", precision reported |
| U5 | `KDS_SYNTHESIS_FOR_OPERATOR_ADV_20261117.md` line 55 | "called lasting only if the evoked delayed response is back within 10%" |
| U6 | `ADV050_NMDAR_AGENTS_VS_KETAMINE_SCI_20261118.md` line 33 (INFERENZA) | adds that the rule "must therefore state the probe frequency"; no sentence in the brief or the two packages states a probe frequency for the evoked response (the search for "probe frequency", "probe schedule" and stimulation-interval wording under the brief folder found none) |
| U7 | `TASK_RECORD_SCI_20261116.md` line 52 | a log line of U3's update |

R1: NOT met. U1 to U5 carry the same band (10 percent), the same reference (the evoked response "of its baseline", pre-exposure), the same case (a fall). U6 adds a condition and does not conflict. Two readings of "within 10%" exist and no use settles them: the literal reading is two-sided (deviation at most 10 percent either way), and the derivation behind it is one-sided (the model's falls all came with evoked below 0.78). Under the literal reading the held evoked overshoot (1.2 to 1.5) fails the condition and the fall is not called lasting; the sentence "otherwise it may be block that has not washed out" then gives the wrong reason, because a raised evoked response is not residual block. P3 of the priors file and of the three packages classes a rate "at most 0.7" as "lasting suppression" on the rate alone; that is the class name scored literally, the rule is the reading; the two coexist and I flag the double use of the word "lasting" without calling it a conflict of band.

## 3. The grid (R2) and the model's high side (R3)

Rate class against the pre-exposure value: FALL (at most 0.7), BAND, REBOUND (at least 1.3). Evoked class against its baseline: LOW (below 0.9), NORMAL, HIGH (above 1.1).

| rate \ evoked | LOW | NORMAL | HIGH |
|---|---|---|---|
| FALL | COVERED: U1 (residual block, the model's K1 cells with E at most 0.78 or 0.92 at a rate of 0.8) | COVERED: U1 (a lasting change, subject to its precision) | COVERED by the literal reading only (not called lasting; the stated reason, "block that has not washed out", does not fit a raised response) |
| BAND | COVERED in the model: statement 9 (a rate "unchanged" with E 0.69 does not exclude both mechanisms) | no inference needed | **SILENT** (populated: the main text's "returned to normal" with the evoked read of 1.3 in Supplementary Fig. S3C) |
| REBOUND | SILENT in the brief; the model has K3 W1 (rate 1.75, E 0.87) without a statement for the cell | COVERED: model statement 8 (a rebound with a normal evoked response is not evidence for adaptation of the NMDAR weight alone) | **SILENT** (populated: the held burst washout bar of about 1.8, Fig. 3D, with the evoked read of 1.3) |

R2: MET: both populated cells are SILENT. The two populations are different readings of different slices and paradigms; the cells are the ones the rule must handle, not a joint observation (PREREG section 2).

R3 (second clause, reported, does not reject): the model's E reaches at most 1.08 (K2 W1: rate 1.52 to 1.61 with E 1.08); no model cell has E above 1.1. The held evoked read of about 1.3 is above anything the toy produced, and the toy's rate overshoot per unit of E overshoot is about six (ln 1.6 over ln 1.08), against about two in the held reads (ln 1.8 over ln 1.3, graph reads from two paradigms). The high side is NOT REPRESENTED beyond 1.08 in the model, not refuted; the toy's E is the NMDAR weight times a gain, a stand-in for the evoked response, and the held overshoot may include a non-NMDAR component the toy does not carry.

## 4. The reference question (PREREG section 5)

The rule's reference is "its baseline", the pre-exposure evoked response. The Design bullet (brief line 164) reads the burst variables "each against the time-matched vehicle slices (rundown control)" and then, as a separate clause, "the evoked delayed response before, during and after (to confirm that block depth was matched and that washout is complete)". It does not say that the evoked response is recorded in the vehicle slices, or that the vehicle's evoked response at the same time is the reference. Breton's S3C has no time-matched control without d-APV (blind reader of ADV-289), so its 1.3 after washout cannot be told from drift. Answer: the design needs the evoked response in the vehicle slices at the same times, and the rule needs its reference stated as the pre-exposure value AND, for any departure beyond the band, the vehicle's value at the same time. The probe frequency (U6) is not stated either; repeated stimulation can itself change burst rate or the evoked response, and Breton's protocol delivers the stimulus every 30 s with triplicate averages (Methods 5.3 in the blind reader's quotation).

## 5. Proposed replacement sentence (text only; no consumer edited here; IT applies in its own window)

"Post-washout reading rule, fixed before data: the evoked delayed response is read at each post-washout time in the exposed slices and in the time-matched vehicle slices, at a stated probe interval; call its departure from the pre-exposure value a washout deviation when it lies outside plus or minus 10 percent AND outside the vehicle's own value at the same time. A fall of the burst rate to 0.7 or lower is called a lasting change only if the evoked response shows no washout deviation; with a low deviation (below 0.9) the fall may be block that has not washed out; with a high deviation (above 1.1) neither residual block nor a lasting change can be told from a raised response, and the fall or rebound is reported as occurring with a raised evoked response. A rate inside 0.7 to 1.3 or a rebound at 1.3 or more is read together with the evoked class in the same way. In the one held case, d-APV in the knockout slice, the evoked response after washout read about 1.2 to 1.5 times baseline (graph read, Breton 2021 Supplementary Fig. S3C, no time-matched control)."

Not claimed: that the 10 percent band is right (it was derived from the toy's low side, the smallest evoked deficit with a rate below 0.7 was 22 percent, so the set does not locate the threshold between 8 and 22 percent); that the overshoot is physiological and not drift or the stimulus schedule; any dose or use of any agent.

## 6. DEFAULTS_TAKEN and wording check

* DEFAULT: "within 10%" read both ways (literal two-sided; derived one-sided) and not forced to one; why safe: both readings give the same verdict (R2 holds under each); different would have been to pick the reading that fits the model.
* The grid cells the model covers were taken from the Part B table and statements as printed (K1, K2, K3 rows), no rerun; no delegate used, because no count needed a blind recheck beyond quotes that sit in the files cited.
* Wording check: "the two cells ... have no sentence" rests on the search of section 0 and on reading U1 to U5 and the model statements 6 to 9; a sentence outside the strings searched is possible, so the claim is "none found by that search", limited to the folder searched and md or txt files.
