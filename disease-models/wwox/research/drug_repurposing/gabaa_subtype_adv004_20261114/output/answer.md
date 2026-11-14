# ADV-004 answer (producer P, gp-z): GABA-A subtype dispute behind NP3P3

Non-canonical research material. Not medical advice; no dose, no clinical statement, no preference for any drug. Reference genotype class only. Labels DATO / INFERENZA / IPOTESI. Numbers: `numbers.tsv` (row ids N...). Depth: all three papers `partial_fulltext_read` (text, Methods, tables, legends read; figures opened only for Hammer Figs 3-4; the PMC pages of Ralvenius and Jensen returned a bot check and were not retried).

## 1 Head-to-head in one system with diazepam as comparator
DATO. **Ralvenius 2016 only.** One system (rat subunits, HEK293, whole-cell patch, GABA EC10 co-applied, 20-24 C, -60 mV): diazepam, clobazam and N-desmethylclobazam (NDMC), each at alpha1, alpha2, alpha3, alpha5, with EC50 and Emax (mean +- SD) in Table 1 (N001-N033). Binding (IC50, not Ki) only at alpha1 and alpha2. n is printed only as "5-7 cells for all data points" (Fig 1 legend), not per subtype.
**Hammer 2015** has clobazam, NDMC and clonazepam as concentration-response series at four human subtypes (oocytes, GABA EC20), but diazepam only as a single 3 uM point (Fig 4A, N 2-4, bar chart; values read from the image, `inferred_from_figure`) and no diazepam potency; zolpidem at alpha2 only (N = 2). **Jensen 2014** is binding only, no diazepam competitor, no efficacy.

## 2 Do the conditions differ, and can any explain the disagreement?
DATO: they differ in every listed respect (`conditions.tsv`): species (rat vs human vs human); system (HEK293 patch vs oocyte TEVC vs HEK293 homogenate binding); agonist level (EC10 at 1/5/8/1 uM per subtype, no preincubation, vs EC20 at 15-60 uM re-determined daily with 30 s compound preapplication, vs none); temperature (20-24 C vs room temperature vs 4 C); normalisation (Ralvenius Emax percent with undefined 100% reference vs EC20 response = 100%); readout (function vs function vs affinity). Two further differences the question did not list: beta isoform (Ralvenius alpha1/alpha5 with beta2, alpha2/alpha3 with beta3, so the alpha2-vs-alpha1 comparison is also a beta3-vs-beta2 comparison; Hammer and Jensen beta2 throughout) and a Table 1 label/Methods mismatch for alpha5 (beta3 vs beta2).
DATO: the disagreement is smaller in direction than in wording. Hammer's own Imax values give NDMC alpha2/alpha1 = 270/203 = 1.33 and clobazam 261/256 = 1.02 (READER ARITHMETIC; Ralvenius quotes 1.33 +- 0.06 and 1.02 +- 0.05 from Hammer, not printed in Hammer), against Ralvenius 1.77 and 0.78 (printed). Hammer reports significantly lower NDMC Imax at alpha1 than alpha2 and alpha3 (P<0.05) and calls such differences "not pertinent" (S08). Potency: Ralvenius EC50 for clobazam/NDMC is 2.8-5.9-fold higher than Hammer's (READER ARITHMETIC, e.g. 610/132 = 4.6; NDMC alpha5 5.9 rests on n = 2).
INFERENZA: no single condition can be shown to explain the disagreement from the three papers: none varies any condition within its design except Hammer's alpha2 cRNA ratio, and every between-paper difference is confounded with the others. Hammer's own list of reasons for a discrepancy with an earlier rat alpha3 study (species, system, technique, agonist-level precision, desensitisation ceiling; E14-E15) is a hypothesis, not tested. To decide, a paper would need clobazam, NDMC and diazepam concentration-response series at alpha1-alpha5 in one cell system, one beta isoform, both EC10 and EC20 agonist levels with and without preapplication, rat and human subunits, n per subtype and a defined normalisation. "Inconsistent, and no condition explains it" is the supportable result.

## 3 Per-subtype potency and efficacy (separate conditions; no pooled column; full detail in numbers.tsv)
| Paper and system | Compound | alpha1 | alpha2 | alpha3 | alpha5 |
|---|---|---|---|---|---|
| Ralvenius: rat, HEK293 patch, GABA EC10; EC50 uM / Emax percent (SD); n 5-7 cells | diazepam | 0.033 / 141 | 0.048 / 123 | 0.071 / 227 (text 237) | 0.029 / 100 |
| | clobazam | 0.61 / 171 | 0.39 / 134 | 1.10 / 317 | 0.50 / 157 |
| | NDMC | 0.57 / 143 | 0.49 / 253 | 0.81 / 245 | 0.58 / 148 |
| | printed alpha2/alpha1 (Emax) | DZP 0.88; clobazam 0.78; NDMC 1.77 | | | |
| Hammer: human, oocyte TEVC, GABA EC20, preapplied; EC50 nM / Imax percent of EC20 response; N experiments | clobazam | 132 / 256 (5) | 138 / 261 (6) | 240 / 269 (4) | 174 / 216 (6) |
| | NDMC | 151 / 203 (6) | 138 / 270 (6) | 282 / 270 (5) | 98 / 233 (2; 123 and 79; 248 and 217) |
| | clonazepam | 15 / 209 (4) | 7.4 / 253 (5) | 16 / 316 (2) | 21 / 255 (5) |
| | diazepam, 3 uM single point (figure, inferred) | about 254 | about 241 | about 335 | about 225 (N 2-4) |
| Jensen: human, HEK293 binding, [3H]flumazenil, 4 C; Ki nM (n) | clobazam | 519 (7) | 205 (6) | 753 (5) | 331 (5) |
| | NDMC | 634 (5) | 147 (6) | 668 (5) | 292 (6) |
Dispersions (SD, SEM, pEC50) are in numbers.tsv. Emax in Ralvenius and Imax in Hammer are not the same quantity (the Ralvenius 100% reference is undefined). Efficacy is not affinity: Jensen's alpha2 preference (Ki ratios alpha1/alpha2 2.5 clobazam, 4.3 NDMC) is a binding result; Ralvenius's rat alpha1 vs alpha2 binding IC50 differ little (clobazam 0.43 vs 0.39 uM; NDMC 0.78 vs 0.59 uM; Ralvenius: "generally low").

## 4 NP3P3 trigger
DATO: as worded in S0 (one paper, clobazam and/or NDMC and diazepam at the four alpha subtypes in one system, potency and efficacy and n) the trigger is **met by Ralvenius 2016 alone**, with two qualifications: n is given only as a range for all points, and the Emax reference is undefined in the text. INFERENZA: the trigger is not met in an independent second system (Hammer lacks a diazepam series; Jensen lacks function), so the dispute is not resolved by it; the paper that reports alpha2 preference is also the paper that supplies the only complete head-to-head.

## 5 Conditional design position for the L2 arm (SCI47; no clinical statement)
IPOTESI/INFERENZA. May be stated: in one rat-subunit HEK293 series with diazepam as comparator, NDMC showed higher Emax at alpha2 and alpha3 than at alpha1 and alpha5 (Ralvenius, EC10 agonist level); clobazam did not; in a human-subunit oocyte series (EC20) the same compounds were described by the authors as non-selective in potency and efficacy, although their Imax values lean in the same direction for NDMC; in human binding the alpha2 affinity was higher for both. May not be stated: that clobazam or NDMC is "alpha2-selective" or "alpha2-preferring" without naming the quantity, system and species; that any one of the three papers refutes another; that a rat efficacy ratio transfers to human receptors or to the reference genotype's neurons; that affinity order implies functional order; any ranking of compounds against diazepam. Wording consistent with the sources: "alpha2-preferring in efficacy in one rat recombinant series; non-selective in one human oocyte series; modestly alpha2-preferring in human binding; not separable on public data".

## 6 Discriminating wet measurement (described, not commissioned)
Measurement: clobazam, NDMC and diazepam full concentration-response series at alpha1b2g2, alpha2b2g2, alpha3b2g2, alpha5b2g2 in one expression system, human and rat subunits arms, at GABA EC10 and EC20, with and without 30 s preapplication, one beta isoform (and a beta3 arm), normalisation to maximal GABA, n and dispersion per subtype. Comparison: within-system alpha2/alpha1 Emax ratio per compound per condition against diazepam. Decision it changes: whether alpha2-preferring wording may enter the L2 arm at all (ratio above 1 and robust to agonist level and species) or must be dropped (ratio near 1 in the human arm).

## 7 Priors G1-G6 (S0)
| Prior | Score | Row |
|---|---|---|
| G1 | partly | Ralvenius has diazepam with both compounds at all four subtypes (N001-N033) so held; but "the other two papers do not include all four subtypes for all three compounds" fails in part: Hammer has diazepam at four subtypes as a single 3 uM point (N072-N075), not a series |
| G2 | held, refined | potencies 2.8-5.9-fold apart (not discordant by orders of magnitude); the disagreement is mainly in which quantity is called selectivity; Hammer's own Imax arithmetic leans alpha2 > alpha1 for NDMC (1.33), same direction, smaller magnitude |
| G3 | held (INFERENZA) | conditions not varied within any design; new confounds found: beta isoform and per-subtype GABA concentrations in Ralvenius |
| G4 | partly | Hammer n = 2 for NDMC applies to alpha5 only (alpha1-3 n 5-6) and to clonazepam alpha3; Ralvenius n only as a range; IT14 numbers all match but omit SD, SEM, n and the diazepam values |
| G5 | held | Jensen is binding only (Ki; no diazepam competitor; no efficacy) |
| G6 | failed | trigger is met as worded by Ralvenius for clobazam and NDMC with diazepam |

## Not done / not reached
Ralvenius and Jensen figures (bot check); Ralvenius supplement; Fisher (cited by Hammer) not read; no verification by a second reader; a competing-interest statement for Ralvenius not found in the extracted text.
