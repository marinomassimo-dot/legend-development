# Blind report on T1-T8 (ADV-288), independent reader, model sonnet, effort high

Inputs read: SENTENCES.md; Cheng 2020 Fig 2 (PNG) and the full text XML (Results, Fig 2 legend, Methods "Recording of Tc-MEPs", "Statistical analysis"); Palma 2022 Fig 2 (JPG, panel B enlarged 4x) and the full text XML (Methods, Statistical Analysis, Results CAP paragraph, Fig 2 legend); Repudi 2021 page 27 (Fig 5 and legend, panel D(ii) enlarged 3x and 8x) and the operator-supplied text (Methods, Fig 5 legend, Fig 2 legend, Results). Power code: `/home/desktop/.claude/jobs/fcd3025a/tmp/code/power.py` and `extra.py` (own noncentral t by numerical integration over the chi distribution; self-checks: n=17/arm, d=1 gives power 0.807; d=0.5 gives n=64; t(0.975,10)=2.2281 all reproduced).

Reading error, stated once. Palma Fig 2B: the original is 699x202 px, so 0.1 velocity unit is about 31 px; bar tops are good to about +-0.005, SEM whiskers to about +-0.004 (so a SEM of 0.015 is 0.011-0.019 and its CV is +-0.03). Repudi Fig 5D(ii): page raster, 11 px per ms, N1 dots overlap, so group means are good to about +-0.15 ms and ratios to about +-0.05. Cheng Fig 2: 140 px per ms, so +-0.02 ms; amplitude +-1 uV.

## T1: MUST CHANGE (minor, one number)

Checked (Cheng Fig 2c, Results paragraph "To understand whether...", Fig 2 legend):
- Values 1.39 +- 0.13 (+/+), 2.13 +- 0.22 (+/-), 2.44 +- 0.37 (-/-) are in the text and match the bars read in Fig 2c (1.39, 2.12, 2.44; whisker tops about 1.52, 2.35, 2.80, i.e. SEM 0.13, 0.23, 0.36). Legend: N = 10, 5, 4; "means +- SEM"; 3 weeks; chloral hydrate 400 mg/kg i.p. in Methods. All correct.
- SD = SEM x sqrt(n): 0.13 x 3.162 = 0.411; 0.22 x 2.236 = 0.492; 0.37 x 2.000 = 0.740. Sentence 0.41, 0.49, 0.74: correct.
- CV = SD/mean: 0.4111/1.39 = **0.2958**; 0.4919/2.13 = 0.2309; 0.74/2.44 = 0.3033. The sentence prints 0.29 for +/+: it should be **0.30** (0.296). With SEM rounding (0.125-0.135) the range is 0.284-0.307, so 0.29 is not impossible but it is not the computed value. Change 0.29 to 0.30 (0.23 and 0.30 stand).
- Brackets, Fig 2c: top bracket +/+ to -/- is **; lower left bracket +/+ to +/- is *; lower right bracket +/- to -/- is n.s. Sentence correct. Fig 2b: top bracket +/+ to -/- *; +/+ to +/- n.s.; +/- to -/- *. Sentence's "+/- and -/- on the amplitude marked *" is correct.
- Not in the sentence, should be: Methods define latency "from the onset of the electrical shock artifact to the major positive peak", i.e. a peak latency, while the Results call it "onset latency". The sentence follows the Results name. Suggest "latency (Methods: shock artefact onset to major positive peak; Results call it onset latency)". Also the test is a one-way ANOVA with no post hoc test named, yet the figure prints three pairwise brackets, and n is 4 to 5 in two groups. Amplitude SEMs from text: 59.2 +- 9.0 (n=10), 59.6 +- 17.2 (n=5), 11.8 +- 5.4 (n=4); bars agree. The knockout line (WD1 or WD234) used for Tc-MEP is not stated.

## T2: CORRECT

Palma Fig 2B (enlarged), Results "Conduction Velocity of the Interhemispheric Fibers", Fig 2 legend, Methods.
- My reading, by group: N1 vehicle (control) bar 0.505, whisker 0.479-0.536 (SEM about 0.029); N1 clemastine 0.427, whisker top 0.443 (SEM about 0.016). Sentence 0.425/0.505 is within reading error. Ratio 0.425/0.505 = 0.842 (my reading 0.845). N2: control 0.276, clemastine 0.278, whiskers almost invisible: "about 0.275 in both" correct.
- n: legend "vehicle (n = 12) and clemastine-treated mice (n = 10-12)", Results "n = 10-12". Sentence "10 to 12 and 12" (clemastine first, then vehicle) is correct.
- CV: clemastine 0.015 x sqrt(10 to 12) = 0.047-0.052, /0.425 = 0.112-0.122; vehicle 0.03 x sqrt(12) = 0.104, /0.505 = 0.206 (with my SEM 0.029: 0.199). Sentence "about 0.12 and 0.21" correct within reading error (about +-0.03).
- "One mean per mouse": legend "For each mice, the average measure come from at least four different sections recorded three times". Supported. Species/age: C57BL/6 wild-type, P21 slices ("400 um coronal slices from P21 mice"), clemastine 50 mg/kg i.p. daily from P5. Correct.
- Unit: Methods give distances in um (500-2000) and latency; velocity is the slope. If latency is in ms, the unit is mm/ms (= m/s), so 0.5 is plausible and "mm/s" is almost certainly a typo. Using only the ratio is safe. Note: the y-axis starts at 0.2, so bar heights are visually exaggerated.

## T3: CORRECT (with two reading notes)

Repudi page 27, Fig 5D(ii), Fig 5 legend, Methods.
- N1 latency, by group: S-Control mean line about 2.4 ms (sentence 2.5; within error), S-KO mean line about 3.1-3.2 ms. Ratio 1.28 in the sentence; my reading 3.13/2.38 = 1.31 (range 1.24-1.33 across plausible reads). Unit ms on the axis. Fine within error.
- Legend: "N1 *P = 0.0104; N2 = 0.5737 Wilcoxon rank sum test" (printed under item (i) but it belongs to (ii): the N1 bracket carries one * and the N2 bracket "n.s."); "n = 8 slices, five subjects S-Control; n = 8 slices, six subjects S-KO". The sentence's 8/5 and 8/6 match. I counted the N2 dots: 8 blue, 8 red. N1 dots overlap and cannot be counted by eye, so 8 each is consistent but not verifiable.
- Age/model: Synapsin-Cre, P13-P17 (Methods), acute slices. Correct.
- CV by eye: N1 dots sit in a tight band (S-Ctrl about 2.1-2.8 ms, S-KO about 2.8-3.9 ms), but **each group has one low point** (about 1.3 ms in S-Ctrl, about 1.5 ms in S-KO, the latter below the S-Ctrl mean). Estimated CV including that point: S-Ctrl about 0.20, S-KO about 0.24; excluding it about 0.09. So "0.15 to 0.25" is fair only when that point is included; "tightly grouped" holds for 7 of 8. N2: S-Ctrl 3.7-13 ms (mean about 6.7), S-KO 3.5-16 ms (mean about 8.3): widely spread, CV about 0.5. Correct.
- Sentence misses: (a) the Methods say "two-tailed unpaired Student's t-test" for all statistics, but Fig 5D uses Wilcoxon rank sum; (b) the slice is the unit (8 slices from 5 or 6 animals), so the P is not an animal-level test; (c) the legend says "250 mm" from the stimulator; the same legend lacks mu glyphs elsewhere ("100 lA" for 100 uA in Fig 2), so this is um by glyph loss; (d) latency is "from the onset of the stimulus", a single distance, so it is a latency, not a velocity; the text says callosal stimulation with recording in neocortical layer V.

## T4: CORRECT

Own computation, noncentral t, two-sided, two-sample, df = 2(n-1), effect ln(1/0.84) = 0.1744, alpha 0.05, power 0.80.
- CV 0.12: n = **9** (normal approximation 7.44, then +1 to 2 for the t correction); CV 0.21: n = **24** (normal 22.77).
- alpha = 0.05/3: CV 0.12 gives **12** (normal 9.92); CV 0.21 gives **32** (normal 30.38). Sentence "9 to 24 (12 to 32)" is reproduced exactly.
- Using sd_log = sqrt(ln(1+CV^2)) (0.1196, 0.2077) gives the same 9 and 24.
- Sensitivity to my reading error: ratio 0.845 gives 10 to 26; CV 0.11-0.13 gives 8-10 at the low end; CV 0.20 gives 22. So say "about 9 to 24 (reading error +-2)". The effect is the observed Palma effect, which is a single-study point estimate and may be inflated; the sentence is correct as stated.

## T5: CORRECT

n = 12 per arm, df = 22, power 0.80, alpha 0.05, two-sided: smallest detectable ln ratio = 0.1436 (CV 0.12) and 0.2513 (CV 0.21), i.e. ratios **1.154 and 1.286** (normal approximation 1.147 and 1.272); downward **0.866 and 0.778**. Sentence 1.15 to 1.29 (0.87 to 0.78) is correct. Power to detect a ratio of 0.84 at n = 12: 0.925 at CV 0.12 and **0.494** at CV 0.21, so "not reliably detected at the upper spread" is correct and "detected at the lower spread" also holds (implicit). At alpha = 0.05/3 the detectable ratio would be 1.185 and 1.346 (not stated, not required). Cross-check with Palma itself: from its read SEMs an unpaired test gives P about 0.03 (see T7), as expected for a power of about 0.5 to 0.9 effect. Caveat: the CV of 0.21 is the vehicle arm's; the clemastine arm's is about 0.12, so a pooled CV is about 0.17; the "upper spread" is a conservative bound, not a pooled value.

## T6: MUST CHANGE (the interaction figure)

Same method (two-sample, log scale, per arm).
- Ratio 1.14 (linear half of 28 percent): CV 0.12 gives **15** (normal 13.17); CV 0.21 gives **42** (normal 40.32). Sentence "15 to 42": correct. (If "half the gap" is taken as half on the log scale, ratio 1.131, the numbers are 16 and 47; say which half is meant.)
- Ratio 1.28: CV 0.12 gives **5** (normal 3.71), CV 0.21 gives **13** (normal 11.36). Sentence "5 to 13": correct.
- **Interaction contrast, four-cell, variance 4 sigma^2/n, df = 4(n-1)**: with the stated rule (effect = ln(r)), a 30 percent contrast is ln(1.30) = 0.2624 and needs **8 per cell at CV 0.12 and 21 per cell at CV 0.21** (normal approximation 6.57 and 20.11). The sentence says 6 to 16. I reproduce 6 and 16 only by using 0.30 as the log-scale effect (ratio 1.35). So either change the sentence to "8 to 21 per cell" (ratio 1.30) or state that the contrast is 0.30 log units (ratio 1.35). If a 30 percent contrast is instead read as ln(1/0.7) = 0.357, it needs 5 and 12. The sentence as written does not follow the stated method. At alpha 0.05/3 the ln(1.30) contrast needs 10 and 28.
- The 28 percent gap is a by-eye ratio of two means, 3.2/2.5 (my reading 1.31, plausible 1.24-1.33). Sensitivity: gap 1.31 gives half-gap 12-35 and whole-gap 5-11; gap 1.25 gives half-gap 18-51 and whole-gap 6-15. The sentence's numbers are exact for 1.28 only.

## T7: MUST CHANGE (the last clause)

- Palma Methods, Statistical Analysis: "Comparisons between two groups were analysed using paired Student's two-tailed t-test." Quote confirmed. Vehicle and clemastine are separate mice treated from P5 (legend n = 12 versus 10-12, unequal), so a paired test cannot be applied as described. First two clauses correct.
- "The P value is read as reported" is not safe. The Results say "p < 0.01, n = 10-12", but Fig 2B marks N1 with a **single asterisk**, and the Fig 2 legend defines only "* p < 0.05" (no ** appears in Fig 2). So text (P < 0.01) and figure (*) disagree. From my read bars an unpaired test gives: SEM 0.03/0.015, n 12/10, Welch t = 2.39, df 16, P = 0.030 (pooled P = 0.037); my own SEM read 0.029/0.016, n 12/12: Welch P = 0.031, pooled P = 0.028; across plausible reads P = 0.02-0.045. A P below 0.01 would need t above about 2.8. So the figure (P < 0.05) agrees with the recomputation and the text P < 0.01 does not. Required change: "the text reports P < 0.01, the figure marks one asterisk (legend: * p < 0.05), and an unpaired test from the read bars gives P of about 0.03; the P value cannot be read as reported at P < 0.01". Estimated 95 percent CI of the velocity difference from the read bars: 0.010 to 0.150 (the lower end is nearly zero).

## T8: NOT ASSESSABLE as a statement about the sources (design rule)

It is a decision rule of the arm set, not a finding. What the sources allow: Palma's clemastine in wild-type mice would trip it on the point estimate (about -16 percent) and, marginally, on the interval (difference CI 0.010 to 0.150 on a 0.505 base, i.e. about 2 to 30 percent; lower end depends on the read error). Two properties of the rule from my computations: (a) at 12 animals per arm the CI condition binds, not the 10 percent: the observed fall must exceed about 10 percent at CV 0.12 and about 16 percent at CV 0.21 for the interval to exclude zero; (b) a true 10 percent fall has power only 0.54 (CV 0.12) and 0.22 (CV 0.21) at n = 12 (n of 22 and 64 would be needed), so a real 10 percent slowing will often not stop the comparison. The second clause (a knockout drug effect cannot then be read as rescue) is a logical choice I cannot test against these papers.

## Extra findings

1. Cheng Methods call latency "to the major positive peak"; Results call it "onset latency" (T1).
2. Palma: text P < 0.01 versus single asterisk (legend * p < 0.05) versus recomputed P about 0.03; Methods "paired" t test on independent groups; Results say treatment P5-20, Methods P5 to P21; axis unit "mm/s" probably mm/ms; Fig 2B axis starts at 0.2.
3. Repudi: Methods promise unpaired Student's t-test, Fig 5D uses Wilcoxon rank sum on slices (8 slices, 5 versus 6 animals); P = 0.0104 is printed under item (i) of the legend but belongs to panel (ii); "250 mm" is um with the glyph lost; one low outlier per group in N1 latency; N1 dots cannot be counted (overlap), N2 counts 8 and 8.
4. Neither Cheng nor Repudi nor Palma give SD directly; every CV in T1-T3 is derived (Cheng exact from printed SEM, Palma by eye from SEM whiskers, Repudi by eye from points).
5. T4-T6 treat the CV as the log-scale SD and the Palma spread as animal-level; Repudi latency spread is slice-level (nested), so applying it as an animal-level CV is an assumption.

## Verdict counts and required changes

CORRECT: T2, T3, T4, T5 (4). MUST CHANGE: T1, T6, T7 (3). NOT ASSESSABLE: T8 (1).

Changes required:
- T1: CV of +/+ = 0.30, not 0.29 (0.2958); optional: note that Methods define a peak latency.
- T6: interaction contrast of 30 percent (ln 1.30) needs **8 to 21 per cell**, not 6 to 16 (6 to 16 corresponds to a log effect of 0.30, ratio 1.35).
- T7: replace "the P value is read as reported" by: text says P < 0.01, figure shows one asterisk (legend * p < 0.05), recomputed unpaired P about 0.03.
