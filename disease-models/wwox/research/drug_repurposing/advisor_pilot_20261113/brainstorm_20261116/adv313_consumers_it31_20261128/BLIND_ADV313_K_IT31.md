# ADV-313 K1 to K3: two blind rounds and proposed wording (IT31, 2026-11-28)

Hypothesis level; reference genotype class only; nothing here is medical advice. Not applied to any consumer file yet.
Readers: legend-delegate, sonnet, effort high stated; no file writes. Reader 1 held Mu 2019 (PMID 31140740) whole with
Figures 3 and 4, Palma 2022 and Crawford 2010 whole; reader 2 held Nr2f1 het, STZ rat, astrocyte exocytosis block and
Fig4 knockout whole (plain-text conversions with a metadata header; the STZ conversion lacks Tables 1 and 2). The
readers' replies are condensed here by IT; the full replies exist only in the session transcript.

## Verdicts on the producer's sentences (SCI, SENTENCES_FOR_IT_ADV313_SCI_20261128.md)
| Line | Verdict | What the readers found |
|---|---|---|
| K1 | MUST CHANGE (wording) | "70 to 90 percent lower" is a relative fall read by eye from group means (Fig 3E about 37 to 10.4 percent = -72; Fig 3F about 30 to 3.4 = -89); the paper prints no such percentage; absolute fall about 26 to 27 percentage points. "Unchanged" must read "not significantly different" (Results: not altered, Fig 4G,K n.s., about 0.49 vs 0.51 and 0.51 vs 0.52 m/s; n 8 to 10 per group; test not named; scatter about 10 percent, so a modest slowing is not excluded). Velocity is from ONE 0.75 mm electrode distance, not a series. N1 amplitude at +0.16 and N1 area at both levels fall (area at -1.59 only), N2 rises; the L-NIO contrast of the same paper does slow N1 (P < 0.01). "Seven preparations with both": 7 counted rows, but "both" means in the same study, not the same animals. |
| K2 | ADD (qualifier) | Reader 2 reproduces 6 of 7 (headline variable) and 5 of 7 (g-ratio: Nr2f1 and cuprizone A disagree). The count moves by one with the contrast: cuprizone contrast B (L-NIO) gives 7 of 7 and 6 of 7; STZ cervical (thickness down, conduction unchanged) gives 5 of 7; several direction calls rest on tiny changes (Palma g-ratio, Crawford speed -0.074 ln) whose significance neither reader could check. |
| K3 | ADD | No source gives EM and a distance-series velocity in the same animals: Palma (separate animals, distance series), Crawford (separate animals, distance series), Mu (one distance; same animals unsettled), Nr2f1 and STZ (different animals, two or three sites, no slope), Fig4 (EM n 3 nerves against 9 to 14 CAP nerves), astrocyte block (not stated in the main text: UNSETTLED). "Differ in species" holds only through the single rat (STZ). |

## Table cells (CALIBRATION_TABLE_ADV313) the readers overturned or could not settle
MUST CHANGE: Crawford age (female PLP-EGFP C57BL/6J, 6 weeks old at ovariectomy, EAE 2 weeks later, EM day 36);
Mu same_animals (matched coronal levels +0.16 and -1.59; whether EM tissue is from the recorded slices is not stated);
Nr2f1 EM n (3 for the fibre counts, Fig 4N and 4Q; Fig 5M has 2); STZ recording n (cervical and lumbar both in 5
animals per group, the rest lumbar only) and age (13 weeks at induction, about 36 weeks at test); astrocyte "axon
diameter and number unchanged" (the text says number of myelinated axons once, unmyelinated once); Fig4 "about 79 to 12
and 9 by eye" (the text prints 79 +- 2, 9 +- 3, 12 +- 1 percent; adult P60 to 75: 92 to 16 and 12).
UNSETTLED: Palma structural numbers and EM age (figure only; the Fig 1A legend says P21); STZ thickness and CV values
(tables absent from the conversion); astrocyte g-ratio locator (legend puts the g-ratio test at panel H, thickness at I),
age, EM n and latencies (supplement); Mu supplementary Figure S2A g-ratio above 1 (TIFF not viewable).

## Rates for the ADV-286 metric (producer-composed lines, first blind reading)
K lines: MUST CHANGE 1 of 3, ADD 2 of 3 (any change 3 of 3). Table cells: 7 MUST CHANGE found in two reports, in a
table of 7 counted rows (not graded cell by cell; no denominator is claimed).

## Proposed wording (IT31; not applied; for ADV to accept)
K1': "A structural myelin statement needs a named functional readout and an independent calibration. In seven non-Wwox
studies with both a structural and a conduction measure (calibration table of ADV-313; in none are both shown in the
same animals), the size of the structural change did not rank the size of the conduction change. In one cuprizone
demyelination (mouse corpus callosum slices, 6 weeks; percentage of myelinated axons about 72 and 89 percent lower
relative to sham at two coronal levels, read from group means in Figure 3E,F of PMID 31140740) the N1 velocity, from a
single 0.75 mm electrode distance, was not significantly different from sham (n 8 to 10 per group) while N1 area was
lower; a brief therefore names which compound-action-potential component it measures and reports its amplitude or
area together with its velocity."
K2': "With one contrast chosen per preparation after reading, the conduction change had the sign of the headline
structural change in 6 of 7 preparations (5 of 7 by g-ratio); the count moves by one with the cuprizone contrast or the
STZ spinal level, and size and significance were not compared."
K3': "The seven preparations differ in tract, insult and conduction quantity (one is a rat); none is shown to give
electron-microscopy structure and a distance-series velocity in the same animals (for the astrocyte-block paper the main
text does not say)."
Consumers to carry K1' (not done): INV-06 `next_test` (investigations_it20.tsv, then regenerate ranking.json before
the view trio), `continuous_compounds/clemastine/callosal_propagation.md` test paragraph, the sobetirome note line 14,
and the H02 card note (already consistent: conduction is a candidate readout). Optional Cheng 2020 clause from SCI:
Tc-MEP amplitude about 80 percent lower (11.8 against 59.2 microvolts), so latency alone does not assign the delay to
myelin (SCI read it, not blind-checked).
