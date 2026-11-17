# Second target set (T4, T5, T6): the frozen decision rule applied (HE; 2026-11-17; non-canonical)

Written for: ADV. Frozen set: `FREEZE_SECOND_SET.md` (sha256 7e341642f2429e4e0b964cd4692d6a9094d27e92c0343d0a5b064b2aa0c2e63a). Per-target records: `T4/RESULT_T4.md`, `T5/RESULT_T5.md`, `T6/RESULT_T6.md`.
| target | role | strict hits per condition (2 runs of 10 hypotheses each): baseline / v1 / v3 | tokens |
|---|---|---|---|
| T4 Thiel (GNAO1, metal-ion cofactor) | axis outside corpus and memory | 0+0 / 0+0 / 0+0 | 623,008 |
| T5 Song (GABRA1 chaperone class) | positive control, held class | 2+3 / 2+2 / 2+2 | 620,358 |
| T6 Villani (phage ligase) | negative control, empty corpus | 1+1 / 1+1 / 1+1 | 432,320 |
Total 1,675,686 tokens (estimate 2.1 million); no usage-limit message in any of the 36 delegate runs.
## The frozen rule, applied exactly
"v3 is called better than v1 only if, on at least 2 of the 3 targets, v3 reaches STRICT or LEVER-CLASS hits in both replicates where v1 does not AND v3 is not below the baseline; AND the negative control shows no v1 or v3 hit above the baseline's."
- T4: v3 reaches nothing in either replicate: condition not met.
- T5: v3 reaches the atom in both replicates, but so does v1 (and the baseline): "where v1 does not" not met.
- T6: same: v1 and v3 and the baseline reach it in both replicates: not met.
- Negative control: v1 and v3 are not above the baseline (strict 2 / 2 / 2; loose 10 / 8 / 10): that clause holds.
Targets where v3 beats v1: **0 of 3**. **No improvement is claimed**: on this set the two-stage v3 generator did not do better than the plain corpus brief (v1), and neither did better than the memory-free baseline. This is the valid outcome the freeze named in advance. One set of three is small; it licenses a statement about this set only.
## What the set shows beyond the rule
1. Where the lever class is in the model's general knowledge or is narrowed by the question (T5, T6), every condition finds it, with or without the corpus; the corpus step adds nothing and costs about 2 to 5 times (v1) and 4 to 8 times (v3) the baseline tokens per run.
2. Where the lever is outside both corpus and memory (T4), no condition finds it; keeping outside hypotheses and testing support/contradict/not stated (the v3 stage 2 step) did not generate a class that no stage proposed.
3. The negative control is not clean: the baseline reaches the atom from general knowledge, so a corpus-empty target does not by itself measure leakage; its useful content is that no corpus condition exceeded the baseline.
4. ADV's note (T4 acceptance): a generator step that enumerates the physical-chemical levers of a named defect (catalytic cycle: cofactors and ions; folding; trafficking; substrate supply), independent of the corpus, is the candidate engine change this set points at. It is not tested here; it needs a NEW one-outcome target after the operator-budget decision.
