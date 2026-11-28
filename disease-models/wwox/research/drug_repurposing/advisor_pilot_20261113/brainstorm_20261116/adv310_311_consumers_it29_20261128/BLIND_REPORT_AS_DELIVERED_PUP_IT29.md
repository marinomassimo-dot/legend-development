# Blind report, 24 candidate sentences (2026-11-28)

Sources used only: cheng_supp_page3.txt, p32000863.txt, ludesmeyers2009.txt, fig7_cheng.jpg.
Arithmetic: arith_blind.py (same folder; run with `python3 -I`). Fig 7 was opened: it shows seizure-group N (pilocarpine -/- N=4; PTZ -/- N=6, +ETS 6, +LiCl 7), none of which any of the 24 sentences quotes. Fig 2 (Tc-MEP) is not in the packet as an image; its values were confirmed from the Results text.

## Verified source facts (all confirmed)
- Cheng supplement p.3: "Neonatal mice at postnatal day 5~12 from Wwox+/- intercrosses were collected for genotyping and the percentages of Wwox-/- mice were 5.1% and 6.5% for WD1 (N=177) and WD234 (N=785)". 0.051*177 = 9.03 (9/177 = 5.08%; 8 and 10 give 4.5 and 5.65, so 9 is unique); 0.065*785 = 51.0 (51/785 = 6.497%; 50 and 52 give 6.37 and 6.62, so 51 is unique). At 7 pups per litter: 0.357 and 0.455 per litter. Cheng's litter size and WT frequency are not reported (confirmed).
- Ludes-Meyers 2009 Table 1: WT 39, HET 85, KO 30, total 154; expected 38.5, 77, 38.5. 30/154 = 19.48%. Chi-square = 2.714, df 2, p = 0.2574 (matches 0.257). Three-day-old pups, F1 x F1 crosses; litter size 3 to 11, mean 7.75; 15 of 35 KO dead by 72 h.
- "brain-wide" occurs nowhere in Cheng 2020. Quote in T04 matches the Discussion verbatim.
- Cheng text: "spontaneous epileptic seizures were commonly observed after postnatal day 12"; no onset age is given.

## Rounding convention found in the brief (the cause of four findings)
Figures at 1.75 per litter are rounded to the NEAREST litter (12/1.75 = 6.86 -> 7; 16/1.75 = 9.14 -> 9; 32/1.75 = 18.29 -> 18; 44/1.75 = 25.14 -> 25; 93/1.75 = 53.14 -> 53; 132/1.75 = 75.43 -> 75). Figures at the Cheng frequency are rounded UP (T08 and T21 say so). Direction at 1.75 is stated nowhere. Rounded up, the 1.75 figures would be 10, 19, 26, 54, 76.

## Per-sentence verdicts

T01_L61_scarce: KEEP. 5.1/6.5 percent, P5 to 12, heterozygote intercross, 0.36/0.46 -> "about 0.4 to 0.5 per litter of 7" (litter size stated), 19.5 percent at day 3, Mendelian-compatible, all confirmed. Rounding to one decimal, direction not needed. Note: "scarce" is true only of the two Cheng lines; the sentence itself shows the third line is Mendelian-compatible.

T02_L105_Q46: OPTIONAL. 0.4 to 0.5 is correct only at 7 pups per litter, and the sentence does not state the 7 (1.75 only implies it); Cheng does not report litter size. Add "at 7 pups per litter (the brief's figure)".

T03_L208_X2_structure_timing: MUST CHANGE. (a) E12.5 (smaller, growth delay, elongated roof plate), E16.5 (Ki-67+ decreased in SVZ; cortical thickness reduced) confirmed. (b) BrdU+ cells are "increased throughout the neocortex" at birth (with many still in VZ/SVZ), not only "in the proliferative zones"; only Ki-67 is stated "in the VZ and SVZ". (c) The paper's phrase is "Gross morphological abnormalities could be observed in Wwox-/- mouse brains from live births" with no age of observation (cerebellar fusion is documented at P19 to 20; Fig 5a legend gives no age). It cannot be placed "at birth", so it cannot be shown to precede seizures. (d) "seizure onset" is not given; the paper says only "commonly observed after postnatal day 12". Suggested: "...birth (more BrdU-positive cells throughout the neocortex, many still in the ventricular and subventricular zones, and more Ki-67-positive cells there) precede the age after which spontaneous seizures were 'commonly observed' (postnatal day 12; no onset age is given); gross brain abnormalities are reported in brains 'from live births' without an age and are not placed in this order."

T04_L208_X3_causal_chain: KEEP. Quote exact; the paper has no network, EEG or tissue-excitability measure and no order-in-time test; "brain-wide" absent. (Results also states the chain as background with refs 25, 49, 54, but nothing tested.)

T05_L208_X2_reversal_clause: OPTIONAL. Logic holds for E12.5 and E16.5. "Early arm" is undefined: an arm starting after birth could in principle reverse the dated birth findings (BrdU/Ki-67). Define "early" as starting before the finding.

T06_L243_pilot_litters: MUST CHANGE (label-level). Cheng numbers verified: KO 12 to 16 -> 34 to 45 at 5.1, 27 to 36 at 6.5 (ceil), union 27 to 45. At 1.75: 12 -> 7; 16 -> 9.14, which is 9 only by nearest rounding (10 if rounded up); WT 24 to 32 -> 14 and 18.29, i.e. 18 nearest (19 rounded up). Direction is stated nowhere in the sentence, and T08 and T21 say "rounded up". Fix: add "(rounded to the nearest litter at 1.75; 7 to 10 and 14 to 19 if rounded up)" or restate as 7 to 10 and 14 to 19. Rest (WT frequency not reported; KO need governs; 14 to 19 < 27 so the same litters supply WT if WT is about 25 percent) confirmed.

T07_L322_interval_method: OPTIONAL. Recomputed with a binomial model, n = 7 pups, independent: P(no KO) = 69.3 percent at 5.1 and 62.5 percent at 6.5 ("most litters give none" true); P(>=2 | >=1) = 15.0 and 19.0 percent ("15 to 19" correct). The model is not stated: Poisson gives 16.8 to 21.0, 6 pups gives 12.6 to 16.0, 8 pups gives 17.3 to 21.9 (Ludes-Meyers mean litter 7.75). Add "binomial, 7 pups per litter".

T08_L347_yield_Y1_Y3_X4: OPTIONAL. All numbers verified (about 9 and 51 KO; 0.36 and 0.46; 30/154 = 19.5 percent, 38.5 expected, p = 0.257; day 3; exon 1 Cre; "Mendelian-compatible"; embryonic death stated without a count). "Rounded up" is stated for the Cheng figures only; add the 1.75 convention (nearest) here, the natural home of the rule (see T06). The clause "only the authors could add one" has no referent in this extract; cannot be checked. The remark that pre-genotyping losses "would lower the yield further" holds only if the litter of 7 counts pups at birth (survivors' KO frequency already contains the losses); state the baseline. Note also that Cheng does not state the collection criteria for the 177 and 785 pups. The Ludes-Meyers line is also an exon 1 deletion, as is Cheng WD1; "a different line" is still right (different construct, Cre-lox).

T09_L347_supplement_N_clarify: MUST CHANGE (scope). Only page 3 of the supplement is held. Page 3 contains genotyping and brain-water methods, with N = 177 and 785 as its only N; that part is confirmed. "The supplement contains no seizure methods and no seizure-group N" is a whole-document negative that page 3 cannot support (seizure methods and group N are in the main text, Fig 7 legend). Say "page 3 of the supplement (the only page held) contains..." or cite verification of the full file. "No second source" has no referent here.

T10_L356_interaction_floorbound: KEEP. 350/1.75 = 200 and 630/1.75 = 360 exact; Cheng 350/(7*0.065) = 769.2 -> 770 and 630/(7*0.051) = 1764.7 -> 1765 (ceil). Animals 4 x 175 = 700 and 4 x 315 = 1260 ("about 1,300", stated as about).

T11_L357_interaction_optimistic: MUST CHANGE (label-level). 22 x 4 = 88 animals, 44 KO. 44/1.75 = 25.14 -> 25 only by nearest rounding (26 rounded up). Cheng 44/(7*0.065) = 96.7 -> 97; 44/(7*0.051) = 123.25 -> 124 (ceil) correct. Direction not stated. Fix: "25 litters (26 if rounded up)" or state the convention.

T12_L358_three_arms: KEEP. All verified: 33/1.75 = 18.86 (about 19); 93/1.75 = 53.14 (about 53; "about" covers the nearest/up difference); 108 to 327 KO, 61.7 -> 62 and 186.9 -> 187; Cheng 33: 72.5 -> 73 and 92.4 -> 93; 93: 204.4 -> 205 and 260.5 -> 261; 108: 237.4 -> 238; 327: 915.97 -> 916. Lower = 6.5, higher = 5.1 correct. Mixed rounding is mitigated by "about".

T13_L359_planning_total: KEEP. 33/1.75 = 18.86 -> 19; 150/1.75 = 85.71 -> 86 (nearest and up agree). Cheng: 33 -> 73 (6.5) and 93 (5.1); 150 -> 330 (6.5) and 421 (5.1, 420.17 -> 421). Overall 73 to 421 correct.

T14_L363a_pilot_application_figure: MUST CHANGE (label-level), same as T06: 16 KO -> 9.14 litters (9 nearest, 10 up); 27 to 45 and the WT remark verified; 14 to 18 should read 14 to 19 if rounded up. State the direction.

T15_L363b_stage2_application_figure: KEEP. 62 to 187 (1.75) and 238 to 916 (6.5 to 5.1) verified. 21 x 11 = 231; 231/1.75 = 132.0 exact; 231/7 = 33.0 exact. 238 and above exceed 132, so the "already exceed" and "would supply WT" clauses hold; WT frequency indeed unreported.

T16_L373_planning_scale: KEEP. 62 to 187 at 1.75 and 238 to 916 at the Cheng frequency verified; 1.75 = Mendelian by construction.

T17_L375_R3C09_note: OPTIONAL. 62 to 187 (36 to 109 per arm), 73 to 93 (11 per arm), 97 to 124 (22 per cell interaction), 238 to 916 all verified. The three Cheng figures belong to three different scales; listing them unlabelled "against" the credible 62 to 187 invites comparing 62 to 187 with 73 to 93. Label each by scale. "75 litters (3 x 44)": 132/1.75 = 75.4, consistent with nearest rounding (76 rounded up).

T18_L387_C25_Q45_note: KEEP. 231/7 = 33; 33/1.75 = 18.86 -> about 19; Cheng 73 to 93; WT frequency not reported (true), so 1.75 for WT is an assumption.

T19_L391_Q45_note: KEEP. Same arithmetic: 33 and 19 and 73 to 93 confirmed.

T20_L397_C04_note: MUST CHANGE (label-level), same as T11: 88 animals, 44 KO, 25.14 -> 25 nearest (26 up); 97 to 124 correct.

T21_L399_C07_note: OPTIONAL. Verified: (a) 73 to 93 and 97 to 124; (b) three arms 93 KO -> 205 to 261, interaction K = 124 (4 x 31) -> 272.5 -> 273 and 347.3 -> 348; (c) three arms 238 to 916, floor-bound 770 to 1765, equal-variability 319 to 1219. The last pair reproduces only with K = 145 and 435 (unrounded per-arm 36.25 and 108.75); with the stated per-arm 36 and 109 (K = 144 and 436) the figures would be 317 and 1222, and three arms use K = 108 and 327. Tiny, but say which per-arm basis. "Rounded up" stated for Cheng figures.

T22_L411_Q33_note: MUST CHANGE. "200 to 360 ... at 180 to 320 per cell": the interaction has two KO cells, so 180 and 320 per cell mean 360 and 640 KO -> 206 and 366 litters at 1.75, and 792 and 1793 at the Cheng frequency. The stated 200 to 360 and 770 to 1765 correspond to 175 to 315 per cell (350 and 630 KO, as in T10). Fix: "175 to 315 per cell" (or "about 180 to 320" and "about 200 to 360"). 238 to 916 verified for 36 to 109 per arm.

T23_L508_X5_Tc_MEP: KEEP. 3 weeks; n = 10, 5, 4 (WT, HET, KO); latency 1.39 against 2.44 ms; amplitude 59.2 against 11.8 microvolts; all in text. Sciatic nerve EM at P20, N = 3 (Fig 3 legend) confirmed. The paper has no Tc-MEP treatment arm and does not say the animals are shared with the histology (confirmed). "Add-on (f)" cannot be checked. The text does not say which line (WD1 or WD234) was used for Tc-MEP.

OPT_Y5_L365_S14_missing_observation: OPTIONAL. 5.1 and 6.5 percent at P5 to 12 confirmed. "Cannot be assumed" is fair for the Cheng lines, but a third null line (Ludes-Meyers, day 3) was Mendelian-compatible; consider "in two lines". Question-form, no recomputation needed.

## Counts
KEEP 10 (T01, T04, T10, T12, T13, T15, T16, T18, T19, T23). MUST CHANGE 7 (T03, T06, T09, T11, T14, T20, T22). OPTIONAL 7 (T02, T05, T07, T08, T17, T21, OPT_Y5).
