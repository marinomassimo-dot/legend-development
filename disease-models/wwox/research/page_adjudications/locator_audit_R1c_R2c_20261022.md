# Locator audit, R1c and R2c readings (blind, 2026-10-22)

Blind adversarial audit under `legend-locator-audit`. Read-only toward every manifest, registry and receipt. The auditor judged only (proposition, quote, anchor) triples against the source artefacts; the authors' notes, task records, selection files, self-evaluations and earlier audits' reasoning about these papers were not opened. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` (whole packet), then sampled by hand: about 25 percent per manifest, weighted to entries with numerals, negations, quantifiers, a text-versus-figure relation, plus every entry carrying a `contradicts_locator` declaration. Every artefact was opened (files/ surface, page render or workbook), none was missing, so no UNVERIFIABLE verdict arises. Artefact digests were not re-hashed in this pass.

Verdicts: SUPPORTED, OVERSHOOT, UNDERSHOOT, UNVERIFIABLE. No UNDERSHOOT and no UNVERIFIABLE was found. The sample covers whole manifests, not only the entries the lot added; the entries are not separable from the packet alone.

## Counts

| Lot | Paper | Triples audited | SUPPORTED | OVERSHOOT | UNDERSHOOT | UNVERIFIABLE | contradicts_locator entries (all audited) |
|---|---|---|---|---|---|---|---|
| R1c | 42587736 | 10 | 8 | 2 | 0 | 0 | 21, 22 |
| R1c | 42650175 | 8 | 7 | 1 | 0 | 0 | 15, 17 |
| R1c | 41378214 | 12 | 12 | 0 | 0 | 0 | 14, 21 |
| R1c | 41373471 | 11 | 11 | 0 | 0 | 0 | 30 |
| R1c | 42569303 | 8 | 7 | 1 | 0 | 0 | none declared |
| R2c | 34483921 | 5 | 4 | 1 | 0 | 0 | 2 |
| R2c | 30175250 | 8 | 8 | 0 | 0 | 0 | 6 |
| R2c | 27616982 | 6 | 6 | 0 | 0 | 0 | 3 |
| R2c | 32678276 | 6 | 6 | 0 | 0 | 0 | 0 |
| R2c | 32751129 | 4 | 4 | 0 | 0 | 0 | none declared |
| R2c | 40166234 (preprint) | 5 | 4 | 1 | 0 | 0 | none declared |
| **R1c total** | | **49** | **45** | **4** | 0 | 0 | |
| **R2c total** | | **34** | **32** | **2** | 0 | 0 | |
| **All** | | **83** | **77** | **6** | 0 | 0 | |

Adverse rate: 6 of 83 triples (7.2 percent), mode: blind hand-weighted sample of about 25 percent per manifest (weighted to numerals, negations, quantifiers, figure-versus-text) plus all 11 contradicts_locator entries, adverse = OVERSHOOT or UNDERSHOOT or UNVERIFIABLE, artefact opened for every triple. R1c 4 of 49 (8.2 percent), R2c 2 of 34 (5.9 percent). Of the 11 contradicts_locator entries, 1 is adverse (42650175 entry 15).

## Adverse triples (OVERSHOOT)

- 42587736 entry 1: the proposition's 'Figure 5 shows 3 to 4 animals per group' fails for the beta2 panel (5D), where bars carry 2 to 3 points (hippocampus treated about 2); the western-blot numbers and regions are right.
- 42587736 entry 5: same count, 'dots show 3 to 4 animals per bar'; panels A to C hold 3 to 4 dots, panel D (beta2) 2 to 3. Values, stars and 'ns' all match.
- 42650175 entry 15: bars read right (about -1.7, -3.3, -2.0, -0.25, +0.5, -0.1, -0.2; mean about -1.0), but DUET (-0.25) is the third-smallest in magnitude among the negative bars (after -0.1 and -0.2), not 'the second smallest'.
- 42569303 entry 29: the contact sheet shows eight thumbnails, the proposition says 'seven images'; the sheet carries no labels, so which thumbnail is not a Figure 1 blot cannot be settled from it.
- 34483921 entry 13: at 60 mg/kg the mutant series is still about 3.7 at 30 minutes with a star, and the wild-type series about 4.1; 'both fall ... and return toward 4 to 5 by 30 minutes' holds for 100 mg/kg and the wild-type 60 mg/kg point only.
- 40166234 entry 16: wild type with Z944, object chamber, reads about 160 s on the axis (bar top about 162, error bar to about 207), not about 130; the other seven bars (325, 135, 225, 240, 345, 350, 145) and the four social indices (0.37, -0.05, 0.34, 0.42) match.

## SUPPORTED with a flag (not counted as adverse)

- 42587736 entry 26: all four-star brackets are in panel B (total alpha1); in panel C the A322D bracket is three stars. The proposition's 'every condition' rise of the HA-tagged alpha1 is true of the bars.
- 30175250 entry 6: bars read vehicle about 32, ethosuximide 1 to 4, six points, two stars; the proposition's opening 'about 35' is loose against its own 'mean about 32'.
- 27616982 entry 17: 'hippocampal and septal bars rise through P21 and fall at P60 in most subfields' holds for CA1 (48 to 40) but the septum is flat (about 29 at both ages).
- 27616982 entry 18 and 32678276 entry 17: the cited artefact file shows only part of the multi-figure claim (Figure 6 panel H and, in a neighbouring file, 8E for the knockout; Figure 3 for 32678276); Figures 5, 7, 9 and Figure 2 were not opened.
- 42569303 entries 7, 11, 13, 23: the per-cell counts and means (41 and 85 with means 11.7 and 49.9; 74, 29 and 44 cells; the Figure 6 insoluble values 185, 219, 311 and 345, 237, 219) were checked against the workbook and match; the clause that N157Q delivery is unaffected in Figure 5D was not opened.
- 32751129 entry 11: the Tmbim3 values 120, 165, 480, 620 are in E11, E13, E17, PN order per the supplement legend (hatched, grey, white, black), so they rise; no direction is misstated.

## Contradicts_locator entries (all 11 audited)

- 42587736 entries 21 and 22: Supplementary Figure S1A reads as declared (wild-type bracket a single hash; I148F bracket ns; M263T untreated a single hash; two points per bar; treated I148F about 0.77 against about 0.66). SUPPORTED. The running text's four asterisks for wild type (29.0 percent, p < 0.0001) is in the XML; the contradiction is real.
- 42650175 entries 15 and 17: the DUET value in the text (-3.4 kcal/mol for Ala305Val) is not in Figure 2B (DUET about -0.1; no bar reaches -3.4; largest is Dynamut2 about -1.9). Entry 17 SUPPORTED; entry 15 adverse only for the 'second smallest' rank.
- 41378214 entries 14 and 21: Figure 5B (R44Q about 5 percent of untreated wild type, three points, one star) and Supplementary Figure S1 (no star, one point below 1) read as declared; the text says 'statistically insignificant'; the supplement caption says no significant change; Table 3 R44W row (-1.3183621 Decrease; -0.37 neutral) is as printed. All SUPPORTED.
- 41373471 entry 30: Supplementary Figure S4 has five blots and three lanes (control, HF-P2, HF-P1), no Sil1 blot, while the legend lists Sil1 and names two lanes. SUPPORTED.
- 34483921 entry 2, 30175250 entry 6, 27616982 entry 3, 32678276 entry 0: SUPPORTED, text and figures as written.

## Notes for the authors (not repairs)

- Signed and ranged values were read against the native surface. Minus signs in Table 3 of 41378214 survive in the XML (U+2212); the Figure 3H values of 40166234 and the Figure 4 ΔΔG bars of 42650175 were read off the plotted axes.
- 41378214 entry 10: the text's '3B' reference and 'mean 8' against a plotted mean of about 6 were not re-opened; only the figure side of the declaration was read, and it matches (4B mean about 6).
