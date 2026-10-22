# Locator audit, R1c repairs, R1d first readings and R2 repairs (blind, 2026-10-22)

Blind adversarial audit under `legend-locator-audit`. Read-only toward every manifest, registry, receipt and ledger. The auditor judged only (proposition, quote, anchor) triples against the source artefacts; authors' notes, task records, self-evaluations and earlier audits' reasoning were not opened. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` (whole packet), then selected by hand. Every sampled artefact was opened (files/ surface, page render, image, or workbook parsed from the zip); signed and ranged values were read against the native surface. Figure surfaces were raster pages or native rasters (`paper_packet.py rank` on 42587736 listed rasters with no vector-drawing floor crossed), so values were read from axes and counted by eye. No artefact was missing, so no UNVERIFIABLE verdict arises. Artefact digests were not re-hashed.

Verdicts: SUPPORTED, OVERSHOOT, UNDERSHOOT, UNVERIFIABLE. No UNDERSHOOT and no UNVERIFIABLE was found.

## Counts

| Scope | Paper | Triples audited | SUPPORTED | OVERSHOOT | UNDERSHOOT | UNVERIFIABLE | Entries audited |
|---|---|---|---|---|---|---|---|
| 1 repairs, exhaustive | 42587736 | 5 | 5 | 0 | 0 | 0 | 1, 5, 10, 15, 26 |
| 1 repairs, exhaustive | 42650175 | 4 | 4 | 0 | 0 | 0 | 3, 6, 9, 15 |
| 1 repairs, exhaustive | 42569303 | 1 | 1 | 0 | 0 | 0 | 29 |
| 1 repairs, exhaustive | 41378214 | 1 | 0 | 1 | 0 | 0 | 25 |
| 2 R1d first reading | 40421674 | 8 | 8 | 0 | 0 | 0 | 2, 4, 6, 10, 13, 14, 16, 22 |
| 2 R1d first reading | 39013852 | 13 | 11 | 2 | 0 | 0 | 1, 3, 5, 7, 9, 10, 11, 13, 15, 17, 18, 20, 22 |
| 2 R1d first reading | 40449593 | 11 | 8 | 3 | 0 | 0 | 1, 5, 7, 9, 11, 13, 15, 17, 18, 20, 21 |
| 2 R1d first reading | 42161426 | 7 | 5 | 2 | 0 | 0 | 1, 3, 4, 5, 7, 9, 10 |
| 2 R1d first reading | 41274966 | 7 | 7 | 0 | 0 | 0 | 1, 3, 5, 7, 9, 14, 15 |
| 3 R2 repairs | 34483921 | 1 | 1 | 0 | 0 | 0 | 13 |
| 3 R2 repairs | 40166234 | 1 | 1 | 0 | 0 | 0 | 16 |
| 3 R2 repairs and new figure entries | 27616982 | 6 | 6 | 0 | 0 | 0 | 17 to 22 |
| 3 R2 repairs and new figure entries | 32678276 | 6 | 6 | 0 | 0 | 0 | 14 to 19 |
| **Scope 1** | | **11** | 10 | 1 | 0 | 0 | |
| **Scope 2** | | **46** | 39 | 7 | 0 | 0 | |
| **Scope 3** | | **14** | 14 | 0 | 0 | 0 | |
| **All** | | **71** | 63 | 8 | 0 | 0 | |

Adverse rate: 8 of 71 triples (11.3 percent), mode: scope 1 exhaustive (11 of 11 repaired entries), scope 2 blind hand-weighted sample (35 to 58 percent of each packet, weighted to numerals, counts, recomputations and text-versus-panel relations), scope 3 the named repairs plus every figure entry from index 17 or 14 upward; adverse = OVERSHOOT or UNDERSHOOT or UNVERIFIABLE; artefact opened for every triple. Scope 1 1 of 11 (9.1 percent); scope 2 7 of 46 (15.2 percent); scope 3 0 of 14. The scope 3 selection of "new figure entries" was inferred from index position (the packet does not mark what is new) and may include entries that were not new.

Per-manifest adverse: 41378214 1 of 1; 39013852 2 of 13; 40449593 3 of 11; 42161426 2 of 7; the other nine manifests 0.

## Adverse triples (OVERSHOOT)

- 41378214 entry 25: Figure 6K draws ten points for R44Q (4 + 4 + 2), not 'eleven'; wild type ten and w1118 about seven are right, and the 6J series (24, 32, 30, 43; wild type about 5 to 8) matches.
- 39013852 entry 1: R166H is not cleared 'in about 32 minutes' in Figure 1C; its curve is still about 10 percent at 32 min (wild type about 7, A252T about 18, R274Q about 32, A173T about 50 are right).
- 39013852 entry 17: in Figure 4G the green ellipse is not between the wild-type group and the heterozygous-corrector group; it runs on beyond the light-purple ellipse and does not overlap the grey wild-type points, and the axes carry no ticks, so 'about 25 units on the second axis' cannot be read.
- 40449593 entry 18: Figure 10D has four points at 100 percent on the vertical axis (x about 85, 87, 94, 98), not five of eight; the 60 to 100 range, n = 8 and Figure 10E (two near 55, three at 100) are right.
- 40449593 entry 20: Figure 13A has nine variants with secreted protein 0 (rows 18 to 26), not twelve; the 13 variants at 0 to 4 percent and the other ranges are right.
- 40449593 entry 21: the quote (Discussion sentence on an in vitro platform for pharmacological chaperones) does not carry the proposition (Methods: each variant n = 4 against wild type n = 24, unpaired two-tailed t test); the source states this in the Figure 5 legend (see entry 22), so the anchor and quote are mismatched.
- 42161426 entry 3: the mutant protein in Figure 4C is about 1.8 against about 0.6 for the empty vector, i.e. about three times the empty-vector level, not 'about 1.8 times'; Figure 4F values (0.35, 0.65 ns, 1.15) and the stars are right.
- 42161426 entry 7: 0.39 is about 50 percent of untreated wild type (0.78), not 'about 45 percent'; about 45 percent holds against treated wild type (0.86), and the 8-point gain matches the ratio change 37.4 to 45.7.

## SUPPORTED with a flag (not counted as adverse)

- 42569303 entry 29: eight thumbnails (the first file holds two frames, one an inverted copy) as stated; the sheet carries no labels, so which thumbnail belongs to which blot panel cannot be read from the sheet, but the proposition claims no lane-level reading.
- 42650175 entry 9: the figure side (0.33 to 0.7, 1.1, 1.4; PBA series 0.65 to 1.18 and 0.49 to 1.04) matches; the clause about phenylbutyrate raising wild-type protein in the lot's other papers was not checked here and is an inference.
- 40421674 entry 10: the PC4 outlier in Figure 4D sits at about 550 on the axis, the proposition says 'near 590'; everything else matches.
- 40421674 entry 2: the figure shows PC1 at about 1.85 at the top concentration; the workbook (S1) gives 1.65 for the first compound at 120 micromolar; the proposition quotes the workbook figure correctly and the figure as 'about 1.5 to 2'.
- 42161426 entry 4: the quote and proposition reproduce the text faithfully, but the text's own arithmetic does not close: 45.7 / 37.36 is about 1.22-fold and the difference is 8.34, not 1.36-fold and 8.36.
- 41274966 entry 14: the quote carries only the uncropped-blot sentence; the other clauses (ANOVA, Dunnett for serum phenylalanine, Tukey for blots, 'at least three times') are in the Methods statistics paragraph of the same source.
- 32678276 entry 16: atropine's shading covers nearly all frequencies and states in Figure 7 but in Figure 6 the sleep panel is shaded only below about 5 Hz; levetiracetam, beta-hydroxybutyrate and pyruvate show none in Figure 6 rather than 'little'.
- 41274966 entry 11: no panel exists to read, as the proposition states; the absence was not testable beyond the pages opened.
- 42587736 entries 1, 5, 10: Figure 5 point counts (three to four for alpha1 and gamma2, two to three for beta2), values, stars (one star on gamma2 in the image against four in the text) and the legend-versus-image panel swap all read as written.

## Notes for the authors (not repairs)

- 41274966 entry 3: every recomputation (treated week 4, 8, 12 means; wild-type week 0 and 12 means; sham week 12 1341.01 against the text's 1341.59) was redone and agrees with the proposition.
- 42650175 entry 15: S1B read as declared; DUET is the third smallest negative bar and the seven-bar mean is about -1.0, as the repaired proposition now says.
- 42587736 entry 26: Figure S2B/C values, hashes and the A322D three-star bracket agree with the repaired proposition.
- 34483921 entry 13, 40166234 entry 16, 27616982 entry 17 (septum flat) and entry 18, 32678276 entry 17: all match their repaired text.
