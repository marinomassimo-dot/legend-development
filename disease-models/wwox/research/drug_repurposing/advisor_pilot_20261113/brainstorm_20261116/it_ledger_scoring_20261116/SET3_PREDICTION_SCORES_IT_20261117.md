# Scoring of the set-3 prediction lines (HE's frozen lines and SCI's independent forecast), by IT (host clock 2026-11-17 ~08:50Z; non-canonical; a model-based register, not evidence; not medical advice)

Written for: ADV (requested it), HE and SCI (the forecasters; SCI may re-score as second reader after this file exists). HE's lines and SCI's lines are scored apart from each other and from the earlier ledger; they are not summed together.
**Rule.** Each line is a probability for one binary statement; log score = ln(probability of what happened) = ln p if the statement occurred, ln(1-p) if not; limits are notes. **Naive comparator: ignorance, 0.5 per statement (ln 0.5 = -0.693).** No naive baseline was declared by either forecaster before the outcomes: I chose this one after reading the outcomes, so it is a convenience comparator, not a pre-registered one (limit).
## What I opened (not taken from the messages)
HE's frozen lines: `deepening_he_20261116/third_set/FREEZE_THIRD_SET_PART_B.md` (sha256 prefix 8920ac510a50, read in HE's worktree; the lines on T7 and T9 are in it). SCI's lines: `deepening_sci_20261116/PREDICTIONS_SET3_T7_T9_SCI_INDEPENDENT.md` (prefix 8be52aefd10c, on main). Outcomes: `RESULT_SET3.md` (prefix 60d45cc42718), `T7/RESULT_T7.md`, `T9/RESULT_T9.md`, and the run files V3/V4_S1/S2 A/B of each target, which I searched myself (zinc, tyrosine hydroxylase, receptor, stimulant, chaperone); reader key digests 7aaa70e4 (T7) and a1d1f654 (T9) are HE's and ADV's, not recomputed by me. HE's files were read in HE's worktree before landing.
## Outcomes (as I found them)
* **T7:** the strict zinc atom: 0 of 40 final-ten statements and 0 in the stage-1 fifteen, v3 and v4. **Zinc occurs once in the v4 output: line 35 of `T7/V4_S1_B.txt`, 'Vitamin A, zinc.' in the enumeration block, as a supply item with no mechanism and no inhibition**; not in any v3 file.
* **T9:** synthesis lowering (tyrosine hydroxylase dosage or precursor supply) named in v3 and v4 in stage 1 and in the final ten (strict atom i: 1+1 in v3, 1+1 in v4). A releaser (amphetamine-type) as a lever: 0 in every run; stimulants appear once in V3_S1_A (H10) and once in V4_S1_B (line 124) only as evidence inside a serotonergic hypothesis, not as the lever. A postsynaptic receptor antagonist class is named in V3_S1_A H8, V3_S1_B H11 and V4_S1_A H9. Chaperone as a rescue lever: 5 of 20 in the final tens, v3 and v4 alike (HE's reader count).
## HE's lines (frozen in Part B before any run)
| line | p | outcome | ln | ignorance |
|---|---|---|---|---|
| T7: v4 reaches the strict atom in >=1 replicate | 0.30 | no | -0.357 | -0.693 |
| T7: v3 reaches it | 0.10 | no | -0.105 | -0.693 |
| T9: v4 reaches (i) or (ii) in >=1 replicate | 0.25 | yes (i, both replicates) | -1.386 | -0.693 |
| T9: v3 reaches (i) or (ii) | 0.10 | yes (i, both replicates) | -2.303 | -0.693 |
| T9: a chaperone ranked as a rescue in v4 | 0.60 | yes (5 of 20) | -0.511 | -0.693 |
Sum -4.662 against ignorance -3.466: **below ignorance by 1.196 nats**, entirely from the two T9 lines where HE put 0.25 and 0.10 on a lever the model reaches from memory. **Not scorable:** the two baseline-condition lines (T7 and T9, 0.10 each): the baseline condition was not run.
## SCI's lines (written and hashed before the launch, before any output was seen)
| line | p | outcome | ln | ignorance |
|---|---|---|---|---|
| T7: zinc named as an inhibitory ion lever (v4, any output) | 0.15 | no | -0.163 | -0.693 |
| T7: zinc named at all, any role (v4, any output; SCI's reading 'any one output of any run') | 0.30 | **yes, once (enumeration supply item)** | -1.204 | -0.693 |
| T7: zinc inhibitor and a discriminating manipulation with a stated prediction | 0.08 | no | -0.083 | -0.693 |
| T9: a chaperone-type lever named in >=1 condition | 0.95 | yes | -0.051 | -0.693 |
| T9: a synthesis-inhibitor class named | 0.35 | yes | -1.050 | -0.693 |
| T9: a releaser class named (strict: as a lever) | 0.20 | no | -0.223 | -0.693 |
| T9: synthesis inhibitor or releaser | 0.45 | yes | -0.799 | -0.693 |
| T9: a postsynaptic receptor antagonist named (calibration line) | 0.90 | yes | -0.105 | -0.693 |
Sum -3.678 against ignorance -5.545: **above ignorance by 1.867 nats**. The eight lines are not independent (the 'or' line depends on the synthesis line; the three T7 lines share one zinc outcome), so the sum overstates the evidence.
**Not scorable from the files:** SCI's two ranking lines (a chaperone in the top 3 as a behavioural rescue, 0.60; a chaperone first in at least one condition, 0.35): the final-ten files list H1..H10 and I did not establish that the order is a ranking (no rank statement in the files); HE's reader counts 'ranked as a rescue' within the final ten, which is a different statement. If SCI or HE says the order is the rank, I score them (H1 is a chaperone-type hypothesis in V3_S2_A, V4_S2_A and V4_S2_B).
## Two readings that move a score (stated, not hidden)
* **Zinc 'named at all' (0.30):** scored YES because SCI's own wording is 'any one output of any run' and the enumeration block is an output. Under the narrower reading (final ten and stage-1 hypotheses only) it is NO, ln 0.70 = -0.357, and SCI's sum would be -2.831.
* **Releaser (0.20):** scored NO (the stimulant remark is evidence inside a serotonergic hypothesis, not the lever). Under the loose reading (a stimulant class paradoxically calming, mentioned anywhere) it is YES, ln 0.20 = -1.609, and SCI's sum would be -5.064.
## Notes (not exclusions)
Two targets; one is TUNED-ON (T7); T9's lever has knock-out precedent that the model knows (HE's own note), so HE's low probability for v3 was an error about memory, not about the engine. Forecaster order: HE's lines were frozen with the design; SCI's after the question texts only. The lines say what each forecaster expected of the engine; they do not show that the engine generates anything outside the model's knowledge (it did not, on either target).
