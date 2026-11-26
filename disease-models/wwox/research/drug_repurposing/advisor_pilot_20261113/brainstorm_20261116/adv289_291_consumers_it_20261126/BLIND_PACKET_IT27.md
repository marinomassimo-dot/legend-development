# Blind check of proposed sentences against one 2021 mouse study (hypothesis level; not medical advice)

Source: Breton et al. 2021, neuron-specific Wwox knockout (S-KO), heterozygote (S-HT), wildtype (S-WT) mouse
neocortical slices. Files in your folder: `main_text.txt` (article body), `supplement_text_and_captions.txt`
(supplement captions and Table S1/S2 text), `fig3.jpg` (main Figure 3), `figS1.png`, `figS3.png`, `figS4.png`
(supplementary figures). Work only from these files. No network. Do not read any other file on the machine.
You may crop and enlarge with ImageMagick `convert`; scripts, if any, run with `python3 -I` and live in your folder.

For every sentence below give: SUPPORTED (true as worded), ADD (true, a missing condition would help but a reader is not
misled), or MUST CHANGE (some part is false, or true only under an unstated condition that changes the inference), and
for each MUST CHANGE the exact words and the smallest correction. Check every number, unit, count, direction and the
words "the", "only", "every", "no", "at the ceiling". A claim about something the files cannot settle is UNSETTLED.
Statements about what a repository or laboratory has done or holds are not yours to judge: skip them and say so.

## V1
"Deep depth: tied to the block that d-APV gives in the laboratory's own hands, which the laboratory measures first. The
published knockout slice gave a delayed field response lowered to about 0.4 of baseline at 100 uA in the d-APV used for
the burst experiment (graph read of Breton 2021 Supplementary Fig. S3C, 6 slices from 3 animals; 50 uM is the paper's one
stated d-APV concentration and is not restated for S3C; slice identity with the 5 burst slices is not shown), that is
about 0.6 of the measured amplitude and about 0.7 to 0.8 of the part above the amplitude floor if the floor is additive.
'At least one half' is therefore at the ceiling d-APV reached in that figure, not below it. The laboratory defines its
measure (peak amplitude at the delayed latency and its floor) before data."

## V2
"A held, field-level analogue exists for d-APV: the delayed evoked response of the knockout slice fell to about 0.4 of
baseline at the paper's d-APV concentration (graph read, 6 slices, 3 animals), about 0.6 blocked. It is not F*: F* is a
fraction of the isolated NMDAR current, this is a field amplitude with a floor, d-APV is competitive and surmountable,
and identity with the burst slices is not shown."

## V3
"In the one held case, d-APV in the knockout slice, the evoked response after washout read about 1.2 to 1.5 times
baseline (graph read, Breton 2021 Supplementary Fig. S3C, no time-matched control)."

## V4
"Carbenoxolone lowered the burst frequency by 87% (p = 0.008; Fig. 3D, n = 36 bursts, 4 slices, 3 animals as the legend
counts them) and, by the paper's median figure in Supplementary Table S1 (0.66 to 0.54 s; 13 bursts, 6 slices, 3
animals), the duration by 18% (the Fig. 3D duration bar reads about 0.57 of baseline, about 43 percent by eye); it did
not return to baseline after washout. Brilliant blue FCF did not reproduce it (73 bursts, 6 slices, 3 animals in the
legend; 25 bursts, 6 slices, 3 animals in Table S1). The two sources differ in count and statistic and the paper does
not reconcile them."

## V5
Context: the record already says "the source also states that 'there was no significant difference in the slope of the
curve' of the frequency-current relation and writes 'Since these data suggest that the hyperexcitability of the network
was not due to action-potential dependent frequency changes'; the Abstract and Discussion do say increased
action-potential frequency," and continues with the sentence to check:
"which rests partly on Supplementary Fig. S4 (held; read 2026-11-26): at the same raw injected current knockout pyramidal
neurons fire more than wild type (a1, asterisks at 80, 100, 120 and 140 pA; about 14 against 6 Hz at 100 pA; Table 1 n 40
cells/15 animals against 13/5; heterozygotes about 12 Hz). With current referred to rheobase (a2) the caption reports p >
0.05 at every step, yet the plotted knockout points lie about 4 Hz above wild type at 60 and 80 pA; what a2 plots is not
stated and the figure cannot settle it. The source is internally mixed on firing."

## V6
"Supplementary Table S1 (held; noted 2026-11-26) gives CBX duration medians 0.66 to 0.54 s (18 percent), a different
statistic from the Fig. 3D bar."

## V7
"(Supplementary Fig. S3; held, noted 2026-11-26; S3C read: d-APV leaves about 0.4 of baseline at 100 uA.)"

## V8
Replacement inside a note about the supplement: "per animal (S1G, n = 9) rho is positive in 8 and negative in 1, and
p < 0.05 in 2 (animal 1 positive, animal 3 negative), which is what the caption's 'no significant correlation or negative
correlation in 8/9' says; S1G names no frequency band."

## V9
"Breton 2021 Supplementary Fig. S1F contradicts itself: the caption gives rho = -0.1201 while the drawn fit line rises,
and p = 0.5674 does not follow from that rho with n = 41 (two-sided p = 0.4545, recomputed 2026-11-26; S1D's 0.1283 with
n = 102 gives 0.1988 as printed)."
