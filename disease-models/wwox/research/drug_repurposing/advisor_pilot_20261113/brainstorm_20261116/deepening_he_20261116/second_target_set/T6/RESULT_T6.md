# T6 (Villani 2026, PMID 42818019; NEGATIVE CONTROL: no thread in the corpus): run record and result (HE; 2026-11-17; non-canonical; not medical advice)

Written for: ADV. Frozen: `../FREEZE_SECOND_SET.md` (sha256 7e341642f2429e4e0b964cd4692d6a9094d27e92c0343d0a5b064b2aa0c2e63a). Atoms were frozen from the abstract and importance statement only (no full text served). T4 and T5 results were not read into this one.
## Runs (strictly sequential, `legend-deepdive`, claude-sonnet-5-5; each condition twice with a fresh delegate)
| step | tokens | tool calls | path audit from the transcript |
|---|---|---|---|
| memory probe | 18,282 | none | zero file-tool calls; knows the phage genus and its ligase gene, states "I know of no study" of a ligase conferring tolerance, but offers ligase resealing as a plausible mechanism once its question named the ligase |
| baseline A / B | 24,728 / 24,896 | none | zero file-tool calls |
| v1 A / B | 50,653 / 46,166 | 3 Read, 5 Grep / 3 Read, 4 Grep | all paths under the cut |
| v3 stage 1 A / B | 28,590 / 22,811 | none | zero file-tool calls |
| v3 stage 2 A / B | 81,104 / 96,254 | 7 Read, 1 Glob, 24 Grep / 7 Read, 1 Glob, 29 Grep | only the cut and the one allowed S1 file |
| blind reader (Z01-Z60, seed 20261117; key hashed first) | 38,836 | 1 Read | read only its input |
Total **432,320 tokens** (estimate ~700k; the corpus delegates stopped early because the folder holds no phage text); no usage-limit message. Reports verbatim in this folder; sha256 prefixes: `BASE_A` 2a618d2e, `BASE_B` 427ddd89, `V1_A` ff92aaea, `V1_B` 46955c35, `S1_A` 2b37f2c5, `S2_A` 6e449bce, `S1_B` 7b300e57, `S2_B` 00411c4b, `PROBE` 0931b844, reader answer `READER.txt` d2bccac8, blind input 'blind_input.md' fed02a04, `blind_key.json` 8644a48c0109e3db17bedbc9b072ee31cb1dbe0378ded0ccd900a5c7f313e5cb (hashed before the reader ran; byte-identical to the T4 and T5 keys, same reason as in RESULT_T4), my first pass `MY_FIRST_PASS_T6.md` 848341f4.
Both corpus conditions: the folder holds no phage, restriction-modification or CRISPR-Cas biology (the only "phage" strings are phage display and macrophage); every corpus run said so and used the eukaryotic WWOX-BRCA1 repair-route material (the HDR/NHEJ/SSA readouts and two method cautions) as analogy only. No run called any hypothesis contradicted.
Splitter notes: the builder needed two more tail patterns for this target ("CLASSIFICATION of" and "Basis:"/"Shared readout"); the final input holds 60 statements, 10 per run, with no stage-1 tokens left.
Disclosure on my first pass: before writing it I ran a keyword listing that printed the arm label beside 14 ligase or end-joining statements, so that pass is not blind to the arm for those statements. The reader, who sees no arm, is the scorer; the first pass followed the statement text and the frozen rule.
## Result (blind reader, unblinded through the key; each cell = YES count over 10 hypotheses of that run)
| condition | QS strict | QL loose | QC lever class |
|---|---|---|---|
| baseline A / B | 1 / 1 | 4 / 6 | 7 / 7 |
| v1 A / B | 1 / 1 | 4 / 4 | 7 / 7 |
| v3 A / B | 1 / 1 | 4 / 6 | 7 / 7 |
Totals strict 2 / 2 / 2 of 20 per condition (6 of 60); loose 10 / 8 / 10; lever class 14 / 14 / 14. **All six runs name the phage Ku/ligase end-joining module with small-indel scars and loss of survival without it: the strict atom is reached in every run of every condition, including the memory-free baseline and the two runs that had a corpus with no phage content.** My own first pass found the same six statements (Z05, Z06, Z22, Z37, Z54, Z56) before the reader answered. Ligase religation with a scarless site (three further statements) is loose and lever-class, not strict.
Predictions committed first: baseline reaches A3 in at least one replicate (45%): held, both replicates; v1 (35%) and v3 (40%): held, both replicates; v1 or v3 above baseline (20%): did not occur, the three conditions are equal at 2 of 20. Replicate agreement on the atom: both runs of every condition agree.
## What it says, and what not
This is not a clean negative control in the sense the freeze hoped: the corpus is empty on the topic, yet the memory-free baseline reaches the lever, and the corpus conditions neither added nor removed it. The reading is that the atom was within the model's general knowledge or within what the question itself narrows to (the question already says the phage tolerates nuclease-induced breaks, so a repair lever is the natural answer; the probe, which names the ligase in its own question, confirms the model knows the ligase mechanism at plausibility level but not any study). So on this target the instrument measures what the model can derive without the corpus. It also shows leakage is not what the corpus step does: no corpus condition scored above the baseline.
Limits: abstract-only atoms; one blind reader reading mechanism-level statements; the question wording leaks the repair class; one target.
