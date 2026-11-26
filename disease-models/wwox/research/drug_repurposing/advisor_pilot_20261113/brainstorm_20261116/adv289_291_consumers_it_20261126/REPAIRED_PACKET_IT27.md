# Blind check of sentences against one 2021 mouse study (hypothesis level; not medical advice)

Source: Breton et al. 2021, neuron-specific Wwox knockout (S-KO) mouse neocortical slices. Files in your folder:
`main_text.txt`, `supplement_text_and_captions.txt`, `supplement_table_S1.tsv`, `fig3.jpg`, `figS1.png`, `figS3.png`,
`figS4.png`. Work only from these files. No network. Do not read any other file on the machine. You may crop with
ImageMagick `convert`; scripts, if any, run with `python3 -I` and live in your folder.

For every sentence: SUPPORTED, ADD (true; a missing condition would help but no reader is misled), MUST CHANGE (some
part false, or true only under an unstated condition that changes the inference; give the exact words and the smallest
correction), or UNSETTLED for what the files cannot settle. Check every number, unit, count, direction and quotation.
Statements about what a repository or laboratory has done or holds are not yours to judge. The unit of replication is
the animal.

## R1
"Deep depth: tied to the block that d-APV gives in the laboratory's own hands, which the laboratory measures first. The
published knockout slice gave a delayed field response lowered to about 0.4 of baseline at 100 uA in the d-APV used for
the burst experiment (graph read of Breton 2021 Supplementary Fig. S3C, 6 slices from 3 animals; 50 uM is the paper's one
stated d-APV concentration and is not restated for S3C; slice identity with the 5 burst slices is not shown), that is
about 0.6 of the measured amplitude, and about 0.7 to 0.8 of the part above an amplitude floor if that floor is additive
and equals the wildtype reading (0.17 to 0.25 of the knockout baseline at 100 uA). 'At least one half' is therefore
close to, but below, the block d-APV reached in that figure at 100 uA (about 0.5 to 0.55 at 10 to 50 uA). The laboratory
defines its measure (peak amplitude at the delayed latency and its floor) before data."

## R2
"A held, field-level analogue exists for d-APV: at 100 uA the delayed evoked response of the knockout slice fell to about
0.4 of baseline at the paper's d-APV concentration (50 uM, not restated for S3C; graph read, 6 slices, 3 animals), about
0.6 blocked. It is not F*: F* is a fraction of the isolated NMDAR current, this is a field amplitude with a floor, d-APV
is competitive and surmountable, and identity with the burst slices is not shown."

## R3
"In the one held case, d-APV in the knockout slice, the evoked response after washout read about 1.3 to 1.5 times
same-strength baseline at 40 to 100 uA (graph read, Breton 2021 Supplementary Fig. S3C, 6 slices, 3 animals, no
time-matched control)."

## R4
"Carbenoxolone lowered the burst frequency by 87% (p = 0.008; Fig. 3D, n = 36 bursts, 4 slices, 3 animals as the legend
counts them) and the burst duration by 18% (p = 0.0274), a figure the paper takes from Supplementary Table S1 medians:
0.54 s under carbenoxolone (13 bursts, 6 slices, 3 animals) against a pooled baseline of 0.66 s (119 bursts, 18 slices,
9 animals); the Fig. 3D duration bar reads about 0.57 of baseline (about 43 percent lower, by eye). Frequency and
duration did not return to baseline after washout. Brilliant blue FCF did not reproduce the frequency fall; for duration
the paper reports no recapitulation, but its Table S1 median (0.53 s) is as low as carbenoxolone's. Legend counts and
Table S1 counts differ (73/6/3 and 25/6/3 for brilliant blue FCF), the Fig. 3D bar statistic is not stated, and the paper
does not reconcile the two."

## R5
Context: the record already says that the source states "there was no significant difference in the slope of the curve"
and that the Abstract and Discussion say increased action-potential frequency, and continues:
"which rests partly on Supplementary Fig. S4: at the same raw injected current knockout pyramidal neurons fire more than
wild type (a1, asterisks at 80, 100, 120 and 140 pA; about 14 against 6 Hz at 100 pA; Table 1 n 40 cells/15 animals
against 13/5; the a1 tests count cells, not animals; heterozygotes about 12 Hz). With current referred to rheobase (a2)
the caption reports p > 0.05 at every step, yet the plotted knockout points lie about 4 Hz above wild type at 60 and 80
pA; which summary statistic and error bar a2 plots is not stated and the figure cannot settle it. The source is
internally mixed on firing."

## R6
"Supplementary Table S1 gives a duration median of 0.54 s under CBX (13 bursts, 6 slices, 3 animals) against a pooled
baseline of 0.66 s (119 bursts, 18 slices, 9 animals), 18 percent lower (BB-FCF 0.53 s); these are raw medians, while the
Fig. 3D bar is normalised and its statistic is not stated, so the two are not reconciled."

## R7
"Per animal (S1G, n = 9) rho is positive in 8 and negative in 1, and p < 0.05 in 2 (animal 1, positive; animal 3,
negative). The paper's Results sentence 'For the delta range, 8/9 subjects showed significant coupling' uses the
authors' own criterion (coupling means a negative or absent correlation between phase-signal power and the coupling
index), so its 8/9 counts animals without a significant positive correlation, not animals with a significant
correlation; the S1G panel and caption name no frequency band, and the body text assigns it to the delta range."
