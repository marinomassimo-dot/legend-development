# Locator audit, R2h figure repairs and R2g repairs (blind, 2026-10-22)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Image reads

All figure artefacts rendered on the first read (no "media removed" placeholder), so no triple is UNVERIFIABLE. For 40825030 entry 11 the spike count was also checked by column-clustering the blue trace of the raster (PyMuPDF pixmap plus numpy).

## Counts

| PMID | Entries | SUPPORTED | Adverse | UNVERIFIABLE |
|---|---|---|---|---|
| 37082241 | 18, 19 (figure), 22 (supplement text) | 3 | 0 | 0 |
| 32878331 | 5, 9 (figure) | 2 | 0 | 0 |
| 35184274 | 6, 13 (figure) | 2 | 0 | 0 |
| 32751129 | 13 (figure), 6 (body) | 2 | 0 | 0 |
| 40825030 | 10, 11 (figure) | 2 | 0 | 0 |
| 40834072 | 9 (body) | 1 | 0 | 0 |
| 24953239 | 3 (body) | 1 | 0 | 0 |
| 40068874 | 3 (body) | 1 | 0 | 0 |
| 35243344 | 5 (figure) | 1 | 0 | 0 |
| **All** | **15 (10 figure, 5 text)** | **15** | **0** | **0** |

Adverse rate: 0 of 15 judged triples (0 percent). Mode: every named entry of the scope, no sampling; adverse = OVERSHOOT or UNDERSHOOT; UNVERIFIABLE excluded from the denominator (none). Figure triples alone: 0 of 10.

## Adverse triples

None.

## Notes on triples judged SUPPORTED

- 37082241 entry 18: Figure 8 B, D, F, H read incidence about 230/285/305 (one star)/290, total duration about 2,750/3,400/4,000 (one star)/4,400 s (three stars), average duration about 12/12.5/13.5/15.8 s (one star), frequency about 9 to 10 Hz. The normalised panels carry stars at the middle and highest doses in A and C, at the highest dose only in E and G; the phrase "at the middle and highest doses" is loose for E and G, accepted.
- 37082241 entry 19: Supplementary Figure 2 first-hour values about 64 vs 75/79/78, 945 vs 1,195 s, 15 vs 16 s, no star on any bar, error bars up to about 660 (incidence) and about 1,970 (total duration) percent at the last bin; all match.
- 37082241 entry 22: Table1 text lists analyte, molecular weight, precursor and product ions only; the title line mentions "collision energies" but no such column exists.
- 32878331 entries 5 and 9: panel D peaks about -270 (L909F), -258 (M1508V), -205 (WT), -175 (L208P); peak voltage left for L208P and M1508V only; panel E shifts about 12, 10, 6 mV; panel F L208P and M1508V left by 3 to 5 mV, L909F near WT.
- 35184274 entry 6: Figure 4B at 5 micromolar about 94, 92 and 81 percent; at 300 micromolar about 8, 4 and 6; Cav3.3 curve looser at the low end; caption gives n = 3 cells per concentration.
- 35184274 entry 13: Figure 1B values match at both time bins (about 72/22/0 s and 19.5/19.5/4 s; numbers 36/10/0 and 12/11/3).
- 32751129 entry 13: the Figure 6 schematics match the proposition item for item. Entry 6: quote occurs verbatim in the Results paragraph and "They" refers to the T-type channels.
- 40825030 entry 10: Figure 3 tau values match (A398E about 190 vs WT about 80 ms, M1425V 330 to 410, M1425I 480 to 730, deactivation at -60 mV about 40, 42, 60 vs about 6 ms). Entry 11: WT simulation shows about 10 spikes before the pulse, a burst of about 4 to 5 and 9 after, so about 23 to 24 in all; "about 23" accepted. AV silent at rest with one spike after the pulse; AE, MV, MI fire more at rest.
- 35243344 entry 5: Figure 6B about 2.2 vs 1.0 (star); 6G about 700 vs 155 pA (three stars, dots about 640 to 750 and 40 to 275); Figure 4E ethosuximide about 23 to 1, baclofen about 33 to 63, four mice.
- 40834072 entry 9, 24953239 entry 3, 40068874 entry 3: quotes found verbatim in the named artefacts and propositions restate them without added strength.
