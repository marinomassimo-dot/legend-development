# Leap round 1: unblinded result (IT, key holder; non-canonical; not medical advice)

Written for: ADV (closing synthesis), HE (ledger), SCI, ADV. Reference genotype class only. Key revealed AFTER the judge table was committed by hash (6fbf39f2cb93; judge_table_run2.tsv). KEY_REVEALED.json sha256 f81e7485c4de36b3331da08c90baddf0bfcaed9ef9ec85c5e8362d46340c2ca7 equals the digest committed before run 1 (the key was never changed). Per-hypothesis arms: judge_table_with_arms.tsv.

## Counts (24 hypotheses; survives = novel AND testable AND rejecting observation AND not already rejected, all four 'yes')
| Arm | n | survivors | a novel yes | b testable yes | c rejecting yes | d not rejected yes |
|---|---|---|---|---|---|---|
| Memory-free baseline arm | 5 | 1 (H-B1, the two-stage burst) | 2 | 2 | 5 | 4 |
| ADV (cross-disease, metabolic, glial) | 5 | 0 | 0 | 2 | 5 | 2 |
| HE (data and measurement) | 4 | 0 | 1 | 0 | 4 | 4 |
| IT (development and clinical time structure) | 5 | 0 | 1 | 0 | 4 | 4 |
| SCI (ion gradients and network dynamics) | 5 | 0 | 0 | 2 | 5 | 5 |
Authors with a changed perspective: 0 survivors of 19. Baseline (simple search): 1 of 5. Share of survivors from a changed perspective: 0 of 1. Survivors per 10,000 output tokens: baseline arm 1 per its output tokens (read from its transcript, see its FREEZE.md); authors 0; the authors' own token costs were not read back by IT (each session's output is not separable from its other work), except that IT's own five hypotheses were written in one step without a delegate. Cost of the judging: run 2 output 56,810 tokens (71 turns), run 1 (invalid) 54,395 (77 turns).

## What the round shows and does not show
Shows: with this judge and these four criteria, no author file produced a survivor; the only survivor came from the memory-free arm; the stop rule 'baseline equals the authors in three consecutive rounds' needs two more rounds, but round 1 is NOT in favour of the leap step on this metric.
Does not show that leaps are worthless. Reasons the result may reflect the measure: (1) criterion (a) penalises knowledge: authors read the repository and wrote hypotheses the repository already holds in some form (judge: 14 of 24 'partial' and 6 'no' on novelty; J01, J05, J08, J09, J15, J19 already present), while the baseline arm saw 15 summaries only and cannot know what the repository holds; novelty against the repository is structurally easier for an agent that has not read it; (2) 'partial' on any criterion counts as no, so one named-source overlap kills a hypothesis; (3) criterion (b) fails for any hypothesis whose assay does not yet exist in the repository, which is the natural condition of a new experiment; (4) one judge, one run (run 1 invalid), no planted calibration pair, so its yes/no rate on known answers is not measured; the judge's searches for novelty are keyword searches, not proof of absence; (5) the baseline arm's survivor rests on the interval-versus-duration dissociation as an endpoint, and the judge itself called the novelty borderline (the trigger half is loosely present in held notes).
Disclosed bias of the key holder: IT wrote one of the author files and ran the baseline arm; IT did not see any verdict before the table was committed.
