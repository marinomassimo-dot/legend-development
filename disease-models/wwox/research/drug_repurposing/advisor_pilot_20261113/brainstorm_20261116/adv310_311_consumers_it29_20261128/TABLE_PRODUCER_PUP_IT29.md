# Pup brief 1.75-knockouts-per-litter correction: statement table

Brief: `.../current_text_adv143_it_20261121/PUP_BRIEF_CURRENT_IT_20261121.md` (not edited; fragments in `edits.py`, checked exact-once by `verify_edits.py`, output in `verify_output.txt`).
Arithmetic: `arith.py`, output `arith_output.txt`. Litters = knockouts / (7 x frequency). Frequencies: 25 percent (check), 5.1 percent (Cheng WD1, N = 177), 6.5 percent (Cheng WD234, N = 785). Rounding: the new numbers are rounded UP (whole litters); the brief's own old numbers reproduce at 25 percent with round-to-nearest (all 17 checked; the one that differs, 145 knockouts -> 82, reproduces from 2 x 72 = 144), so they are kept as printed and labelled "assumed 1.75". All new numbers are DERIVED from the Cheng frequency, with the litter size of 7 taken from the brief.

## A. Statements resting on the 1.75 assumption (changed)

| tag | line | statement (short) | old | new at 5.1 percent | new at 6.5 percent | status |
|---|---|---|---|---|---|---|
| T01 | 61 | "Knockout pups are scarce (about one in four ...)" | 1 in 4 (25 percent) | 5.1 percent | 6.5 percent (also 19.5 percent day 3, other line) | changed |
| T02 | 105 | Q46 "litter yields about 1.75 knockouts" | 1.75 per litter | 0.36 | 0.46 | changed |
| T06 | 243 | pilot, knockouts 12 to 16 | 7 to 9 litters | 34 to 45 | 27 to 36 | changed (and the wild-type-set-the-size conclusion reverses: knockouts now set it) |
| T06 | 243 | pilot, wild type 24 to 32 | 14 to 18 litters | kept at 1.75 (wild-type frequency not reported) | same | kept, flagged |
| T07 | 322 | "With about 1.75 knockouts per litter the bootstrap ..." | 1.75 | 0.36; 15 percent of knockout litters give 2 or more | 0.46; 19 percent | changed (number clause only; method untouched) |
| T08 | 347 | "a litter yields about 1.75 knockouts" (Y1 + Y3 + X4 clause) | 1.75 | 0.36 | 0.46 | changed |
| T10 | 356 | interaction, floor-bound, 350 to 630 knockouts | 200 to 360 litters | 981 to 1,765 | 770 to 1,385 | changed |
| T11 | 357 | interaction at sigma 0.3, 44 knockouts | 25 litters | 124 | 97 | changed |
| T12 | 358 | three arms, 11 per arm (33 knockouts) | 19 | 93 | 73 | changed |
| T12 | 358 | three arms, 31 per arm (93 knockouts) | 53 | 261 | 205 | changed |
| T12 | 358 | three arms, 36 to 109 per arm (108 to 327) | 62 to 187 | 303 to 916 | 238 to 719 | changed |
| T13 | 359 | planning total, 33 to 150 knockouts | 19 to 86 | 93 to 421 | 73 to 330 | changed |
| T14 | 363a | R3Q37 pilot, 12 to 16 knockouts | 7 to 9 | 34 to 45 | 27 to 36 | changed |
| T15 | 363b | R3Q37 stage 2, 108 to 327 knockouts | 62 to 187 | 303 to 916 | 238 to 719 | changed |
| T15 | 363b | wild-type 231 animals | 132 litters (1.75) | kept; knockout litters exceed it | same | kept, flagged |
| T16 | 373 | "Planning scale" 19 and 53; 25; 62 to 187 | 19, 53, 25, 62 to 187 | 93, 261, 124, 303 to 916 | 73, 205, 97, 238 to 719 | changed (qualified, pointer to T08) |
| T17 | 375 | R3C09 note: 19, 25, 62 to 187 | same | 93, 124, 303 to 916 | 73, 97, 238 to 719 | qualified (overall range written 73 to 93, 97 to 124, 238 to 916) |
| T18 | 387 | C25/Q45 note "33 knockouts need about 19 litters" | 19 | 93 | 73 | changed |
| T19 | 391 | Q45 note "33 knockouts need 19 litters" | 19 | 93 | 73 | changed |
| T20 | 397 | C04 note, 44 knockouts, 25 litters | 25 | 124 | 97 | qualified |
| T21 | 399 | C07 note (a)(b)(c): 19, 25 / 53, 71 / 62 to 187, 82 to 249, 200 to 360 | as printed | (a) 93, 124; (b) 261, 348; (c) 303 to 916, 407 to 1,219, 981 to 1,765 | (a) 73, 97; (b) 205, 273; (c) 238 to 719, 319 to 957, 770 to 1,385 | old body kept (labelled ASSUMED in the note), correction sentence appended |
| T22 | 411 | Q33 note, credible range 62 to 187 and 200 to 360 | as printed | 303 to 916; 981 to 1,765 | 238 to 719; 770 to 1,385 | qualified (the "reproducible at 1.75" part is true and kept) |

Statements found that rest on the assumption: 20 (T12 and T21 each count once although they carry several numbers). Changed or qualified by a fragment: 18 (fragments T01, T02, T06, T07, T08, T10 to T22). Kept with the number retained and flagged: 2 (wild-type litters at 1.75, L243 and L363b; the wild-type frequency is not in the held supplement). Further fragments not about the yield: T03, T04, T05 (X2, X3), T09 (supplement-N clarification), T23 (X5), OPT_Y5 (optional); 24 fragments in all.

## B. Not resting on the assumption, left unchanged

| line | statement | reason |
|---|---|---|
| 11 | "the litter counts for wild-type supply" | describes status labels, no number |
| 74, 322 (second clause) | "fewer than 10 litters in a cell" | analysis threshold, independent of yield |
| 81 | "heterozygote crosses (expected 1:2:1)" | an expectation, true as stated; T08 gives the observed frequency |
| 82, 84 | "a litter yields only about 7 pups" | litter size, not knockout yield (7 is the brief's own; Cheng gives no litter size; Ludes-Meyers 2009 reports 3 to 11, mean 7.75, in the other line) |
| 162, 164, 255, 365 | knockout supply questions (S14 gets optional Y5) | no number |
| 385 | "Wild-type and heterozygous animals are not limiting" | stays true; the yield correction only makes knockouts scarcer |
| 375, 397, 411 | "75 litters" (3 x 44) | already declared a superseded figure |
| 556 to 805 (History, markers) | quoted old wording incl. 75 litters (586 to 589, 674, 752 to 753), 19, 25, 53 (709, 753), "12 to 20" (740), Marker Q46/C25 text (690) | History keeps old text verbatim by design |

## C. Check of the previous reader's proposals

| item | verdict | what I did |
|---|---|---|
| Y1 | right (5.1 of 177, 6.5 of 785, P5 to P12; 0.36 and 0.46; LM 30/154 = 19.5 percent, expected 38.5, p = 0.257, day 3, Wwox+/DeltaCre; supplement p. 3 and LM Table 1 re-read) | used, plus about 9 and 51 knockouts (percent times N) and that the 25 percent figure stays as the labelled ASSUMED case |
| Y2 | right (93 / 73, 421 / 330, 770 to 1,765 reproduced) | spread across T10 to T22 by statement |
| Y3 | one error | "The held text does not state whether knockouts were lost before genotyping" is contradicted by Cheng Results ("some very severely affected embryos died embryonically", no count, no cross). Replaced: losses before genotyping are not quantified and would lower the yield |
| Y4 | accurate with nuance (not drafted) | Repudi: "Wwox-null mice are born at a Mendelian ratio" is a cited literature statement (refs 19, 20), not their count; N-KO = Nestin-Cre (progenitor), S-KO = Synapsin-Cre (neuron); no counts. The brief has no passage on the neuron-specific preparation, so no fragment |
| Y5 | usable | OPT_Y5 appended to OPEN-GAP S14 |
| X1 | mismatch, no fragment | the live brief already says "8 to 20" (L347, per-panel N confirmed on the Fig 7b and 7d images: 20, 16, 18, 12 / 12, 8, 12, 12; knockouts 6, 6, 7; saline controls 4 or 5 not listed). "12 to 20" survives only as quoted old text in History L740 |
| X2 | right, drafted (T03, T05) | E12.5, E16.5, birth findings precede "commonly after P12"; DCX P14 and P19 to 20 (vermis fusion "19~20", checked) stay concurrent or later; the closing clause of L208 also needed the change |
| X3 | right, drafted (T04) | quote "may cause reorganization of neuronal networks ..." is in the Discussion; reworded to "tests neither its order in time nor the link" |
| X4 vs Y1 | Y1 chosen | keeping 1.75 as the plan and adding a clause would leave the litter figures 4 to 5 times low in the live text; the 25 percent is kept only as the labelled Mendelian case. X4's "about 0.4 per litter" is right (0.36 to 0.46) |
| X5 | right on numbers, drafted (T23) | Tc-MEP 3 weeks, n 10 / 5 / 4, 1.39 vs 2.44 ms, 59.2 vs 11.8 microvolts match; the live (f) already carries them, (g) lacked the pointer. "animals not paired with the histology" softened to "the paper does not state that its animals were those of the histology" (not stated either way); "conduction measured once" applies only to the callosal slice latency |
| X6 | out of scope | not touched |

## D. For the integrator
- Same 1.75 sentence still lives in `v2_consolidated_sci_20261119/PUP_BRIEF_V2_CONSOLIDATED.md`, `invivo_pup_adv059_sci_20261118/INVIVO_PUP_EXPERIMENT_BRIEF_V1_SCI_20261118.md` (X4's A46 and B34) and in rp041/adv144/adv148 TSVs; not examined here.
- The wild-type frequency among Cheng's genotyped pups is not reported on supplement p. 3; every wild-type litter statement stays a Mendelian assumption.
- Pilot size in litters is now set by the knockout need (27 to 45 litters) rather than the wild-type need; the Q45 reading ("not limiting only if wild-type breeders") should be re-read after landing.
- WD1's 5.1 percent rests on about 9 knockouts; its interval is wide, so the 5.1 to 6.5 range is not a precise bracket.
