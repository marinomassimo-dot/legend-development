# Locator audit, figure attestations rerun (R2d, R2c) and R2e figure triples (blind, 2026-10-22)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` (all entries, no sampling) and judged against the native artefacts under `files/`. The earlier audit was consulted only to learn which triples were UNVERIFIABLE. Nothing was repaired.

## Image-read limitation (applies to the first reads of most figures)

The image reader returned "media removed: request limit" with no pixels for many opens, often with only a dimensions note. A triple is SUPPORTED only where the figure actually rendered and was read. Where every read for a manifest returned the placeholder, the verdict is UNVERIFIABLE and no value was guessed. Where a read failed, a different surface of the same figure (page extraction with PyMuPDF, the journal JPEG, the embedded raster) was tried; this recovered most of the R2c set and all of R2e. It did not recover 40834072, 24953239, 42536722 or 37275776, whose renders (main-figure rasters, page renders, supplement pages) all came back as placeholders in this session.

## Counts

| Lot | PMID | Figure triples | SUPPORTED | Adverse | UNVERIFIABLE |
|---|---|---|---|---|---|
| R2d rerun | 40834072 | 6 (entries 10-15) | 0 | 0 | 6 |
| R2d rerun | 24953239 | 6 (4, 8-12) | 0 | 0 | 6 |
| R2d rerun | 42536722 | 8 (6, 7, 17-22) | 0 | 0 | 8 |
| R2d rerun | 37275776 | 7 (2, 7, 13-17) | 0 | 0 | 7 |
| R2d rerun | 32719346 | 1 (entry 17) | 0 | 0 | 1 (S7 clause; S8 and S9 read and match) |
| R2c rerun | 30175250 | 4 (6, 8, 13, 22) | 4 | 0 | 0 |
| R2c rerun | 27616982 | 5 (18-22) | 5 | 0 | 0 |
| R2c rerun | 32678276 | 7 (5, 14-19) | 7 | 0 | 0 |
| R2c rerun | 32751129 | 5 (10-14) | 4 | 1 (entry 13) | 0 |
| R2c rerun | 40166234 | 4 (14-17) | 4 | 0 | 0 |
| **Rerun subtotal** | | **53** | **24** | **1** | **28** |
| R2e | 37082241 | 9 (6, 7, 14-20) | 8 | 1 (entry 18) | 0 |
| R2e | 32878331 | 6 (5, 9-13) | 5 | 1 (entry 5) | 0 |
| R2e | 33704440 | 5 (11-15) | 5 | 0 | 0 |
| R2e | 35079122 | 3 (7-9) | 3 | 0 | 0 |
| R2e | 35184274 | 6 (5, 6, 10-13) | 4 | 2 (entries 6, 13) | 0 |
| R2e | 40068874 | 5 (5, 10-13) | 5 | 0 | 0 |
| R2e | 40825030 | 3 (9-11) | 2 | 1 (entry 11) | 0 |
| **R2e subtotal** | | **37** | **32** | **5** | **0** |
| **All** | | **90** | **56** | **6** | **28** |

Adverse rate: 6 of 62 judged triples (9.7 percent), counting only triples that rendered (24 + 1 + 32 + 5). Mode: every figure-attestation entry of each named manifest, no sampling; adverse = OVERSHOOT or UNDERSHOOT; UNVERIFIABLE excluded from the denominator. R2e alone: 5 of 37 (13.5 percent). Rerun alone: 1 of 25 judged. 28 of 90 triples (31 percent) remain UNVERIFIABLE because their artefacts would not render; that does not clear them. Of the 53 earlier UNVERIFIABLE triples, 25 are now judged and 28 remain open.

## Adverse triples

- 37082241 entry 18 (OVERSHOOT, mislabelled source). Figure 8 (page 11 raster) reads raw incidence about 230 (vehicle) against about 305 (30 mg/kg, one star) and about 290 (100 mg/kg); total duration about 2,750 s against about 4,400 s (three stars at 100 mg/kg); average duration about 12 s against about 15.8 s (one star). The proposition's "about 65 against 78 to 79", "about 940 s against about 1,200 s" and "about 15 against about 16 s" are the first-hour values of Supplementary Figure 2 (Image2.png), where no bar carries a star. Values come from one figure and stars from the other.
- 32878331 entry 5 (OVERSHOOT). Panel D is described as "peak current density similar between variants, voltage of peak current shifted left for all three". Panel D shows L909F and M1508V peaks of about -270 and -255 pA/pF against about -205 for wild type and about -175 for L208P (entry 9 of the same manifest says larger for two variants), and the L909F peak sits at -25 to -20 mV, the same as wild type, so a left shift for all three is not read.
- 35184274 entry 13 (OVERSHOOT). At 40 to 60 minutes the three groups are not all about 19 to 20 s: vehicle and the 150 dose are about 19 to 20 s, the 300 dose is about 4 s (Figure 1B, cumulated duration). The discharge-number values (about 12, 11, 3) match.
- 35184274 entry 6 (OVERSHOOT, minor). Residual current "from near 100 percent at 5 micromolar": Cav3.1 about 93 and Cav3.2 about 92, but Cav3.3 is about 81. Values at 300 micromolar (below 10 percent) and the looser Cav3.3 low-end fit match.
- 32751129 entry 13 (OVERSHOOT, minor). Figure 6 E17-PN1 schematic is said to list ASIC1, Cav3.2, Orai2, P2X2, GluN1, CX36 and LETM1 "in addition". It drops TMEM165, Cav3.1, Orai3, TRPM7 and CX43, CX45, CX37 from the E11-E13 schematic, so it is not cumulative.
- 40825030 entry 11 (UNDERSHOOT). The wild-type simulation is said to fire about 14 spikes in the first 3,000 ms. Figure 6A shows about 10 tonic spikes before the hyperpolarising pulse, a burst of about four and about 9 afterwards, roughly 23 in all (19 excluding the burst); no reading gives 14. The other clauses (A398V silent at rest, one spike after the pulse; other variants fire more at rest with denser bursts) match.

## Notes on triples judged SUPPORTED

- 32751129 entry 11: the Tmbim3 values (about 120, 165, 480, 620) match, but the bars in that panel run PN, E17, E13, E11 left to right, so the highest value (620) is E11. The proposition states no ages for them; any age order read into it must be reversed.
- 37082241 entry 15: second compound brain value at 60 minutes reads about 0.08, the proposition says about 0.15; 5 percent of axis range, accepted.
- 35079122 entry 8: the "two stars" on resting-potential current sits on the antioxidant group; the comparator is not printed on the panel.
- 40068874 entry 13: panel D (third supplier) shows diffuse signal; "in the hilus" is not separable on the panel.
- 32719346 entry 17: Supp S8 (PAK3, wild type about 84 and 80 percent, three stars; transgenic about 54 and 47, ns) and S9 (FMR1, wild type about 80 and 78, three and two stars; knockout about 52 and 56, ns) match; S7 did not render.
- 32678276 entries 16 and 15: the packet's image order for Figures 6 and 7 was resolved by caption position on the PDF page; the ethosuximide bands (7 to 22 Hz absolute, narrow relative) match.

## Not rendered (UNVERIFIABLE, 28)

40834072 entries 10-15 (Figure 1, 2, 4, 5, 7 rasters), 24953239 entries 4, 8-12 (Figures 1-6 JPEGs), 42536722 entries 6, 7, 17-22 (page renders, supplement pages), 37275776 entries 2, 7, 13-17 (page rasters, Data Sheet pages), 32719346 entry 17 (S7 only). Each was opened through the packet's best surface and through at least one alternative; every open returned the "media removed" placeholder. They need a session whose image reads succeed. The packet and artefact paths are unchanged.
