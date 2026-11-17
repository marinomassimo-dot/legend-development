# T5 (Song 2026, PMID 42587736; POSITIVE CONTROL): run record and result — RETRODICTION BY ABSENCE FROM THE CORPUS, NOT BY DATE (HE; 2026-11-17; non-canonical; not medical advice)

Written for: ADV. Frozen: `../FREEZE_SECOND_SET.md` (sha256 7e341642f2429e4e0b964cd4692d6a9094d27e92c0343d0a5b064b2aa0c2e63a) and `../AMENDMENT_T5_1.md` (sha256 ed4205cb2dd6d3ceffaa64cb716d572e25cf46cc6748e06a4943e8e6b4ca4f48, on main before any T5 delegate; the unread remainder of the Song text was read first). Later targets' results are not read into this one.
## Runs (strictly sequential, `legend-deepdive`, claude-sonnet-5-5; each condition twice with a fresh delegate)
| step | tokens | tool calls | path audit from the transcript |
|---|---|---|---|
| memory probe | 17,762 | none | zero file-tool calls; states the lever class and the heterologous-cell finding, NO mouse or current finding (positive control: expected, not a void) |
| baseline A / B | 24,384 / 24,332 | none | zero file-tool calls |
| v1 A / B | 83,571 / 110,405 | 8 Read, 8 Grep / 11 Read, 9 Grep | all paths under the cut (443 files) |
| v3 stage 1 A / B | 26,359 / 23,625 | none | zero file-tool calls |
| v3 stage 2 A / B | 136,053 / 130,783 | 10 Read, 1 Glob, 20 Grep / 12 Read, 1 Glob, 41 Grep | only the cut and the one allowed S1 file |
| blind reader (Z01-Z60, seed 20261117; key hashed first) | 43,084 | 2 | read only its input |
Total **620,358 tokens** (estimate ~700k); no usage-limit message. Reports verbatim with sha256 in this folder (`BASE_A.txt` 190ba6d8..., `BASE_B.txt` 59cc0a6f..., `V1_A.txt` a6d3a0d7..., `V1_B.txt` c1e32413..., `S1_A.txt` bb32790e..., `S2_A.txt` 4baa33e5..., `S1_B.txt` 23ba497f..., `S2_B.txt` c96d5db3..., probe 93d6abf2..., reader answer 647d50ec..., blind key `blind_key.json` 8644a48c0109e3db17bedbc9b072ee31cb1dbe0378ded0ccd900a5c7f313e5cb hashed before the reader started). The blind input is the statement and discriminating manipulation of each hypothesis, origin lines, corpus-test fields, file paths and stage-1 references removed (a few 'S1-n' tokens were replaced by 'a rival' by a text substitution before the reader, recorded here).
## Result (blind reader, unblinded through the key; each cell = YES count over 10 hypotheses of that run)
| condition | QS strict | QL loose | QC lever class |
|---|---|---|---|
| baseline A / B | 2 / 3 | 4 / 5 | 2 / 4 |
| v1 A / B | 2 / 2 | 5 / 4 | 2 / 2 |
| v3 A / B | 2 / 2 | 6 / 3 | 3 / 2 |
Totals 13 / 27 / 15 of 60. **Every one of the six runs names the held-type lever class (QS at least 2 of 10 each): replicate agreement 6 of 6 runs, and no condition differs from another** beyond noise (baseline strict 5 of 20 hypotheses, v1 4 of 20, v3 4 of 20). The corpus step neither added nor removed the class relative to the memory-free baseline, as expected for a positive control whose probe already carries the class from general knowledge. QS here is lenient: the reader counted a calcium-channel-blocker class acting on ER chaperone function and ligand-site pharmacological chaperones as chemical-chaperone classes (borderline calls listed in its answer; a stricter reading drops QS to 11); and NO hypothesis states the paper's current outcome (a non-significant trend only): nearly every block predicts current rising with surface, so on the full atom (class AND an at-most-partial current) none is a clean hit and the finding is one-sided on current in all conditions.
Predictions committed first: v1, v3, baseline each reach A3 in at least one replicate (70% each): HELD on the class and expression part for all three; 'a statement that the current is NOT rescued' (15%): did not occur. My own first pass (`MY_FIRST_PASS_T5.md`, written before the reader's answer) counted 2/4/2/2/3/3 hypotheses per run and agrees on the verdict: no difference between conditions; the explicit 4-phenylbutyrate-class lever appears once in v1 (run B) and once in v3 (run A) as a lever, and in baseline and stage 1 only as evidence.
## What it says, and what not
The instrument works on a held-class, positive-control target (it finds the lever class in every run, with or without the corpus) and does not separate the three conditions on it, which is the honest expectation for a positive control; it says nothing yet about v3 against v1 on a target whose axis lies outside the corpus (T4) or about leakage (T6). One target; scoring by one blind reader on a lenient strict rule; the paper's own current result (trend only) is unreached by all conditions.
