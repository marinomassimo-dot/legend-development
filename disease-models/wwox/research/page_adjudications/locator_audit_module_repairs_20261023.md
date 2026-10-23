# Locator audit, repairs and neighbour edits after the 2026-10-23 module-batch audit (blind, 2026-10-23)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Scope

Every entry carrying `contradicts_locator` with no audit block (zero auditors) in the eleven manifests, plus the new 33201535 entry 11 and the 42397075 repointing check.

| PMID | Entries in scope |
|---|---|
| 23611579 | 6 |
| 30497978 | 6 |
| 40139194 | 0 |
| 33201535 | 3 and 11 (new, beside 3) |
| 42397075 | 2, 4, 13; repointing check of 0 to 29 |
| 42422765 | 10, 14, 15, 38, 40, 41, 45 |
| 34268881 | 39, 41, 50 |
| 36779245 | 38 |
| 30362252 | 5 (the Davids statement narrowed to the figure legends) |
| 30361190, 24456803 | none (no entry carries `contradicts_locator`) |

## Image reads

Every image read returned a real image (no "media removed"). 42422765 Figure 2B was read from the 2,906 x 3,769 px raster on mmc2.pdf page 4, cropped with PyMuPDF at 350 dpi, x axis calibrated from its ticks (0 at 369 px, 10 days per 77.5 px). Figure 3 was read from the native 1,744 px render with tick calibration (B: 1.78 px per day; C: 15.4 px per gram). Figure 2F of 42397075 was calibrated at 125 px per unit from its -3 to +1 ticks. 36779245 Figure 4A is a 709 x 226 px native image, so its values are readable only to about +/- 0.03.

## Counts

| PMID | Judged | SUPPORTED | Adverse | UNVERIFIABLE |
|---|---|---|---|---|
| 23611579 | 1 | 1 | 0 | 0 |
| 30497978 | 1 | 1 | 0 | 0 |
| 40139194 | 1 | 1 | 0 | 0 |
| 33201535 | 2 | 2 | 0 | 0 |
| 42397075 (2, 4, 13) | 3 | 3 | 0 | 0 |
| 42397075 (repointing, entries 0 to 29) | 30 | 20 resolve and match | 0 | 10 |
| 42422765 | 7 | 5 | 2 | 0 |
| 34268881 | 3 | 2 | 1 (quote-level) | 0 |
| 36779245 | 1 | 1 | 0 | 0 |
| 30362252 | 1 | 1 | 0 | 0 |
| 30361190, 24456803 | 0 | 0 | 0 | 0 |

Adverse rate: 3 of 20 judged triples (15.0 percent). Mode: exhaustive over the declared scope (every entry with `contradicts_locator` and zero auditors, plus the new 33201535 entry); adverse = OVERSHOOT or UNDERSHOOT; the 10 UNVERIFIABLE repointing entries are excluded from the denominator and the 20 resolving repointed entries are not counted as triples. Substantive adverse only (quote-level excluded): 2 of 20 (10.0 percent).

## Adverse triples

| Manifest | Entry | Verdict | Reason |
|---|---|---|---|
| 42422765 | 10 | OVERSHOOT | Supplementary Figure S8 A and B legends list only KO+WWOX P1, P2, P3 and P5 (P1 n=6, P2 n=6, P3 n=3, P5 n=7); no P4 survival curve exists. P4 appears only as a bar in S8C and S8D. The proposition says survival at any point P1 to P5 reaches at least 40 days and that "P2, P3 and P4 appear solely in the 40-day panel"; for P4 there is no survival reading, and P3 falls to 67 percent from about day 24. The quote itself (P1, P2, P5 at 100 percent, P3 67 percent) is correct; the other S8 numerals (KO+RI 67/33/0 percent at about days 13/14/15, P5 75 percent from about day 35 to 300, P1 100 percent with a marker at about day 300, ns bracket spanning WT to P5 in C and D) were confirmed. |
| 42422765 | 40 | OVERSHOOT (shape) | Figure 3B axes confirm the HD plateau (about 77 percent flat from about day 80), the WT line (about 72 percent) and the KO+RI zero marker at about day 17. But the LD arm is a staircase, not "100 percent to about day 18 then 0 percent": about 90 percent at about day 18, 80 at about 22, 70 at about 40, 50 at about 48, 40 at about 60, 30 at about 62, 20 at about 70, 0 at about day 77 (marker centre; the quote says about 79). The proposition's "a STEP and not a gradient" and the quote's two-point LD description both flatten that progressive decline; entry 41 of the same manifest correctly reads LD at about 79 percent alive at day 30. |
| 34268881 | 39 | OVERSHOOT (quote-level) | The quote supports only the filter rule (1,246 up and 1,021 down at FC beyond 1.2 and P below 0.01, Tables EV1 and EV2). Every other clause of the proposition is true but sits outside the quote: the 15,370-gene set and alpha 0.01 (Methods), the Wald test (Figure EV3 legend), WT n=2 against KO n=4 (Figure 4 legend), and CACNA1E P 0.0097 with adjusted P 0.067 (Table EV1 row, derived text line 864). The "unadjusted P" inference is flagged as the reader's own in the proposition. |

## Notes on triples judged SUPPORTED

- 23611579 entry 6, 30497978 entry 6, 40139194 entry 0, 33201535 entries 3 and 11: each quote occurs verbatim in the cited JATS, and the narrowed propositions claim no more than the quote carries (the Discussion sentence on bumetanide is now its own entry 11).
- 30362252 entry 5: "lactate" and "spectroscopy" each occur once in the article (the neuroimaging sentence); neither of the two figure legends mentions MRS; the WWOX exon-6 deletion within maternal UPD and the two HSPG2 variants are in the text.
- 34268881 entry 41: CACNA1G, CACNA1H and CACNA1I occur in neither list; the only CACNA1 genes listed are CACNA1A (line 861) and CACNA1E (line 864), both EV1_up; CACNA2D2 and CACNA2D3 up, CACNB3 down. The quoted CACNA1A row is at line 861. Entry 50: mTOR, autophagy and EIF4EBP each occur once, in the top-100 downregulated sentence; rapamycin and 4E-BP occur zero times; Appendix Fig S3A is cited but not held. The rewritten proposition is accurate.
- 42397075 entry 2 (Figure 2F re-read): KO RGs +0.99 and Neu -2.38, SCAR12 RGs -0.28 and Neu +0.18, WOREE RGs +0.07 and Neu -0.07; panel E neuronal fractions about 0.45, 0.08, 0.58, 0.45; panel D counts 5649, 3020, 3422, 5916. Entry 4 (Figure 5F and G): WT about 33 percent early, WOREE about 66, SCAR12 about 68; G log2FC about +1 early and -1 late for both; n=9094. Entry 13: the quoted line and the "potentially pointing to the safety profile" sentence are in the Results; Supplementary Figure 10C to F is the cited support and is not held.
- 42422765 entry 14 (Figure 2B): KO 75, 50, 0 percent at about days 17, 18, 19; 4E10 arm 67 percent at about 18, 33 percent at about 19, black dot at 33 percent at about day 25; 8E10 marker at about day 27; WPRE 4E10 marker at about day 31; WT to about day 40; arm identity as stated. Entry 15 (Figure 2E): lane values 0.8/0.9/0.3/0.1 and 4.7/5.9/1.5/0.4 without WPRE against 11.6/11.9/4/2.4 and 25.6/22.3/11.6/6.2 with it, as read; the earlier "did not lower" clause is gone. Entry 38 (Figure 1 A, C, D, F, G, I, J, L): EF1a glucose about 102 with all dead by about day 20, CMV about 131 ns with 40 percent of 5 alive at about day 32, MBP about 50, SynI about 131 ns with full survival. Entry 41 (Figure 3C and D): P30 weights about 17.5, 15.3, 15.6 g, KO+RI last at about day 15, LD series ends at about day 60 at about 21 g, no significance marker on either panel. Entry 45 (Figure 1 G, H, I, M): MBP+W 100 percent to about day 14, 0 by about day 16 to 17; weights, glucose brackets and panel M as stated; all four promoter vectors are WPRE-bearing at 4e10 vg per the legend.
- 36779245 entry 38 (Figure 4A, 709 x 226): blue about 0.91 flat, green about 0.75 then about 0.62 from about 8 to 9 years to about 24 years, red about 0.45 by about 3 years and about 0.26 from about 9 years, p = 0.0085; the bands overlap at late ages. Readable only to about +/- 0.03.

## 42397075 repointing (entries 0 to 29)

- Resolves: entries 0 to 14 and 16 to 20 now cite `PMID42397075_Steinberg2026_*` paths that exist (body quotes found in `..._OUP-AM_fitz.txt`; `locator_audit.py` reports 28 of 28 text quotes matched, 0 not found); figure entries 2, 4, 6, 9, 11 cite Steinberg figure files that exist, and the three figure files checked (fig_p35_1430x749.png, fig_p35_1430x795.jpeg, fig_p36_1430x1754.jpeg) have the same SHA-256 as the legacy Aqeilan copies still on disk.
- Not repointed, UNVERIFIABLE: entries 15 and 21 to 29 (10 entries, supplementary figures) still cite `PMID42397075_Aqeilan2026_assets/S10_caption_p19_200dpi.png` and `S_fig_p*_170dpi.png`; none exists on disk (the Aqeilan assets folder holds only six main-figure files) and no copy exists elsewhere on the machine. The supplementary volume is the same absent artefact as in the earlier audit; no guess was made.
- The manifest's `source_artifacts` list and its `files/fulltext/PMID42397075_Aqeilan2026.pdf` / `_fitz.txt` entries still carry the Aqeilan names (48 occurrences of "Aqeilan2026" remain in the manifest).
- Observation outside scope (entry 6, not carrying `contradicts_locator`): Figure 4C G1/G0 bar ends at about -0.30 on the printed axis; the quote reads about -0.2.
