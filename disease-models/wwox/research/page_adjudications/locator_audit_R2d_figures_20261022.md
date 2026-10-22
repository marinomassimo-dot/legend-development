# Locator audit, R2d figure attestations and R2c figure controls (blind, 2026-10-22)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Only (proposition, quote, anchor) triples drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` were judged, against the native artefacts under `files/`. No author notes, task records or earlier audit reasoning were read. Nothing was repaired.

## Reason and the main limitation

The audit targets figure attestations (entries whose quote is "[figure attestation - pixels cannot be quote-matched]"), because the author reported earlier "media removed" placeholders on first image reads.

The same failure hit this audit. The image reader returned a "media removed: request limit" placeholder on most first and repeat opens. After the limit reset, only some images rendered. A figure triple is SUPPORTED here only when its native surface rendered and was read. Where it never rendered, the verdict is UNVERIFIABLE, and the reason is the missing render, not the resolution of the figure. No value was guessed. Figures that rendered were read at 0.8 to 2.4 kpx across, enough for bar values to about 5 percent of axis range and for stars. No vector surface was involved, so `paper_packet.py rank` was not needed.

## Counts, figure attestations (all entries of each manifest)

| Lot | PMID | Figure entries | SUPPORTED | OVERSHOOT / UNDERSHOOT | UNVERIFIABLE (surface never rendered) |
|---|---|---|---|---|---|
| R2d | 40834072 | 11 | 5 (3, 5, 16, 17, 18) | 0 | 6 (10-15, main-figure rasters) |
| R2d | 40827489 | 5 | 5 (4, 6, 16, 17, 18) | 0 | 0 |
| R2d | 32719346 | 7 | 6 (5, 13, 14, 15, 16, 18) | 0 | 1 (17: Supp S7 and S9 pages not rendered; S8 part reads as written) |
| R2d | 35243344 | 7 | 7 (5, 10-15) | 0 | 0 |
| R2d | 24953239 | 6 | 0 | 0 | 6 (4, 8-12) |
| R2d | 42536722 | 8 | 0 | 0 | 8 (6, 7, 17-22; see note on 17) |
| R2d | 37275776 | 7 | 0 | 0 | 7 (2, 7, 13-17) |
| **R2d total** | | **51** | **23** | **0** | **28** |
| R2c | 34483921 | 3 | 3 (7, 12, 13) | 0 | 0 |
| R2c | 30175250 | 4 | 0 | 0 | 4 (6, 8, 13, 22) |
| R2c | 27616982 | 10 | 5 (3, 14, 15, 16, 17) | 0 | 5 (18-22, immunogold figures) |
| R2c | 32678276 | 7 | 0 | 0 | 7 (5, 14-19) |
| R2c | 32751129 | 5 | 0 | 0 | 5 (10-14) |
| R2c | 40166234 | 4 | 0 | 0 | 4 (14-17) |
| **R2c total** | | **33** | **8** | **0** | **25** |
| **All** | | **84** | **31** | **0** | **53** |

Adverse rate for figure attestations: 0 of 84 are OVERSHOOT or UNDERSHOOT (0 percent). 53 of 84 (63 percent) are UNVERIFIABLE because the artefact would not render in this session. Mode: every figure-attestation entry in every named manifest, no sampling. Of the 31 triples that rendered, none was adverse. This does not clear the 53 that did not.

## Figure triples read, with notes (none adverse)

- Signs, ranges and stars were checked against the axes. Every bar value, count and star in the 31 rendered triples matched within reading error.
- 34483921 entry 7: the proposition says the sixth mutant trimethadione point is "inferred at 5 from the printed mean 4.00". The panel shows three points at 5, so the value is plotted, not inferred. The data match; the wording is conservative.
- 34483921 entry 13: the earlier flagged "both fall and return" wording is not in this proposition; the plotted series match at all three doses.
- 27616982 entry 17: CA1 stratum radiatum 48 (P21) to 40 (P60), septum about 29 at both ages, no thalamus group, all as written.
- 40827489 entry 18: one ethosuximide animal rises above its saline value (about 63 against 60 events); no star on any bar.
- 42536722 entry 17: the social-novelty values (digenic about 0, P = 0.47; control about 0.3) and the spike-wave frequency (about 20 per hour) match. The "15 of 15 recorded show epilepsy" count could not be separated from 14 of 15 on the percentage bar (page render 1238 x 1575); that clause is UNVERIFIABLE.
- 32719346 entry 17: Supp S8 (PAK3) reads as written (wild type about 83 and 80 percent, ***; transgenic about 50, ns). The S7 and S9 pages did not render.

## Text-quote control (every fifth text entry per manifest, 32 triples)

Only the packet's quote and proposition were compared (first 420 characters of each were read). The text quotes were not re-matched against the XML. This control is a weaker read than the figure one.

| PMID | Text entries | Control triples | Adverse (OVERSHOOT) |
|---|---|---|---|
| 40834072 | 8 | 2 | 0 |
| 40827489 | 14 | 3 | 1 (entry 2) |
| 32719346 | 12 | 2 | 1 (entry 2) |
| 35243344 | 9 | 2 | 1 (entry 2) |
| 24953239 | 7 | 1 | 0 |
| 42536722 | 15 | 3 | 1 (entry 2) |
| 37275776 | 11 | 2 | 1 (entry 9) |
| 34483921 | 11 | 2 | 0 |
| 30175250 | 21 | 4 | 0 |
| 27616982 | 13 | 3 | 0 |
| 32678276 | 13 | 3 | 0 |
| 32751129 | 10 | 2 | 1 (entry 7) |
| 40166234 | 14 | 3 | 0 |
| **Total** | | **32** | **6** |

Adverse rate for the text control: 6 of 32 (18.8 percent). Mode: every fifth text entry per manifest, quote versus proposition only, adverse = OVERSHOOT. All six are the same kind: the proposition adds a clause the quote does not carry.

Adverse text triples:
- 40827489 entry 2: the quote gives only the floor explanation; the interaction p = .044 and the "alternative of distinct mechanisms" are not in it.
- 32719346 entry 2: the quote covers only the wild-type ethosuximide result; the PAK3 and FMR1 non-rescue and the "acts through blocking the discharges" conclusion are not in it.
- 35243344 entry 2: the quote supports the mRNA-does-not-explain point; the proposition's remark on the abstract's wording is an added judgement.
- 42536722 entry 2: the quote says only that ethosuximide did not rescue the social deficit; "controls dosed too" and "group difference before and after" are not in it.
- 37275776 entry 9: the quote has 250 uM no effect and 750 uM restoring near-normal firing; the proposition says the highest concentration over-suppressed and that wild-type networks were not treated.
- 32751129 entry 7: the quote covers the onset-of-corticogenesis uptake routes only; the late-stage list (ASIC1, Orai2, P2X2, GluN1) is not in it.

## Not done

- The R2e manifests (24002024, 26419537, 31781019, 32878331, 33704440, 35079122, 35184274, 37082241) were drawn and counted (1, 1, 1, 6, 5, 3, 6, 9 figure entries) but not read, because of the render failures above.
- The 53 UNVERIFIABLE figure triples need a rerun in a session where image reads succeed. The packet and artefact paths are unchanged.
