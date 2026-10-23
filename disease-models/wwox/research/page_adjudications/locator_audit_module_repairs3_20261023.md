# Locator audit, third repair round of 2026-10-23 (blind, 2026-10-23)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and ledger. Triples were drawn with `framework/scripts/locator_audit.py --pmid <PMID> --triples 0` and judged against the native artefacts under `files/`. Nothing was repaired.

## Scope

The entries rewritten by the three 2026-10-23 repair commits that carry `contradicts_locator` and have no audit of their own text (their only audit blocks refer to the superseded wording). The set was taken from the entries that differ between each commit and its parent.

| PMID | Entries in scope | Why |
|---|---|---|
| 42422765 | 10, 40, 41 | second repair after the previous audit |
| 42397075 | 6; 15, 21 to 29 | Figure 4C re-read; ten entries marked `artifact_status` ABSENT_ON_HOST |
| 34268881 | 39, 45, 48, 49, 52 to 58 | #39 split into quoted entries; DDIT4, RPS6KB2, HK2, SLC2A1, LDHA, DEPTOR rows |
| 24456803 (Abdel-Salam) | 11 | narrowed |
| 25708809 (Hua) | 0, 1, 6, 7, 9, 10 | narrowed |
| 30361190 (Shaukat) | 14, 15, 17, 18, 19, 20 | narrowed (20 is new) |
| 30362252 (Davids) | 5 to 9 | narrowed |
| 36779245 (Oliver) | 39 to 46 | narrowed |

The five resume manifests hold 26 rewritten entries, not 24. Entries 4 and 13 of 42397075, and entries 14, 15, 38 and 45 of 42422765, carry `contradicts_locator` but were not changed in this round and were audited blind on the previous round; they were not re-judged.

## Image reads

All image reads returned real images. 42422765 Figure 3 was read from the 2,906 x 2,832 px raster embedded on mmc2.pdf page 6 (500 ppi): panel B calibrated x 0 to 300 d (about 2.95 px per day) and y 0 to 100 percent (about 5.2 px per percent); panels C and D read against their ticks. Supplementary Figure S8 was rendered from mmc1.pdf page 10 at 300 dpi. 42397075 Figure 4 is the 1,430 x 749 embedded raster (C calibrated on -0.4, 0, 0.4, 0.8 ticks, about 190 px per log2 unit). 25708809 Figures 5 and 6 are the 774 x 532 and 996 x 630 native rasters. 34268881 Table EV1/EV2 was checked against the derived text, whose header (ensg, symbol, EntrezID, pvalue, padj, log2FoldChange) fixes the columns.

## Counts

| PMID | Judged | SUPPORTED | Adverse (OVERSHOOT or UNDERSHOOT) | UNVERIFIABLE | Anchor-level only |
|---|---|---|---|---|---|
| 42422765 | 3 | 2 | 1 | 0 | 0 |
| 42397075 | 11 | 1 | 0 | 10 | 0 |
| 34268881 | 11 | 11 | 0 | 0 | 0 |
| 24456803 | 1 | 1 | 0 | 0 | 0 |
| 25708809 | 6 | 6 | 0 | 0 | 0 |
| 30361190 | 6 | 6 | 0 | 0 | 2 |
| 30362252 | 5 | 5 | 0 | 0 | 0 |
| 36779245 | 8 | 8 | 0 | 0 | 0 |
| Total | 51 | 40 | 1 | 10 | 2 |

Adverse rate: 1 of 41 judged triples (2.4 percent). Mode: exhaustive over the declared scope (every rewritten entry listed above); adverse = OVERSHOOT or UNDERSHOOT; the 10 UNVERIFIABLE entries are excluded from the denominator. Counting the two anchor-level defects as well: 3 of 41 (7.3 percent).

## Adverse triples

| Manifest | Entry | Verdict | Reason |
|---|---|---|---|
| 42422765 | 41 | OVERSHOOT (scope) | The headline "the dose does not grade body weight" is general; the quote carries only P30 (WT 17.5, LD 15.3, HD 15.6 g) and day 180. Figure 3C itself shows the low-dose arm below the high-dose arm from P15 to P25 (about 6.4 vs 7.2, 7.3 vs 8.7, 9.5 vs 12.3 g, the P25 error bars not overlapping), with no significance marker either way. Only the P30 sentence is supported; the all-age headline is not. All numerals in the quote were confirmed (KO+RI last point P15 about 4.7 g in C, about 5.4 in D; LD series ends at day 60 at about 21 g; no marker on C or D; LD about 80 percent alive at day 30 from B). |

Anchor-level only (the proposition is supported by the quote; the printed location is wrong), 30361190, by PyMuPDF search of the PDF:

| Manifest | Entry | Reason |
|---|---|---|
| 30361190 | 17 | "and urine sulfocystine. Cranial MRI at two months of" is on printed page 405, left column, not page 404. |
| 30361190 | 19 | "on four antiepileptic medications including vigaba-" is in the right column of page 404, not the left. (Entry 18's "page 403 left column to page 404" is loose: its quote is page 404 left column.) |

## Notes on triples judged SUPPORTED

- 42422765 entry 10: S8A legend lists only P1 (n=6), P2 (n=6), P3 (n=3), P5 (n=7), no P4; S8A P1, P2, P5 at 100 percent to day 40, P3 67 percent from about day 24, KO+RI 67/33/0 percent at about days 13/14/15; S8B shows only P1 (100 percent to about day 300) and P5 (75 percent from about day 33 to 300); S8C and S8D show seven bars (WT, KO, P1 to P5) with one ns bracket spanning WT to P5.
- 42422765 entry 40: Figure 3B confirms the staircase. Low dose: 100 percent to about day 16, 90 at about 18, 80 at about 22, 70 at about 40, 60 at about 44, 50 at about 47 to 59, 40 at about 59, 30 at about 64, 20 at about 68, 0 at about 77. High dose: red hidden under the navy WT line, first step to about 92 percent at about day 50, about 85 at about 67, 76 to 77 flat from about day 80. KO+RI zero marker centred at about day 17. WT 90 percent from about day 48, 72 percent from about day 125. Red censoring tick at about day 23. The caption sentence with p = 0.78 is quoted in entry 46 and matches.
- 42397075 entry 6: Figure 4C G1/G0 about -0.30, M about -0.40, G2M about +0.54, S about +0.80 (quote -0.29, -0.39, +0.52, +0.77, within reading error of about 0.03); Figure 4D S-KO positive, M-KO negative, WT near zero; 4A curves close.
- 42397075 ABSENT_ON_HOST marking: truthful. The Aqeilan assets folder holds only `figs/`; none of the nine cited supplement paths exists; no file on the host (files/, worktrees, Downloads) matches any of the 14 declared SHA-256 values; no other entry cites a missing path. Entries 15 and 21 to 29 are UNVERIFIABLE: the supplementary-figures volume is not held.
- 34268881: every row matches the derived Table EV1/EV2 (DDIT4 +0.71, padj 1.03E-5; RPS6KB2 -0.39, 0.0195; HK2 +2.46, 8.75E-34; SLC2A1 +1.44, 9.99E-10; LDHA +0.91, 4.92E-6; DEPTOR +1.16, 3.09E-3). The tool-run statements hold: RPTOR, RICTOR, RPS6KB1, RPS6, ULK1, ATG5, ATG7, BECN1, MAP1LC3B, SQSTM1, TSC1, AKT1-3, PTEN, PDK1, PKM and HIF1A are in neither list; EIF4EBP2 is up, SESN2 down, PDK3 up with padj 0.0565. The body quotes (1,246 up and 1,021 down; alpha 0.01; 15,370 genes; Wald test; WT n=2, KO n=4) occur in the JATS.
- 24456803 entry 11: the metabolic-screen sentence is verbatim in the Results paragraph on II:4.
- 25708809: all quotes occur in the JATS; "42 parried of HCC tissues" and the nude-mouse xenografts are in the Methods; no brain, neur or cerebr string occurs; the antagomir sentence gives no dose or vehicle (the only mg/kg is the diethylnitrosamine dose). Figure 5C: two lanes per group, WWOX stronger in the antagomir lanes, no densitometry. Figure 6C: the higher-expression curve falls to 0 by about 20 months and the lower-expression curve stays at 100 percent to about 14 months, so the panel matches the section title and not the quoted sentence, as the entry says.
- 30361190 entries 14, 15, 17, 18, 19, 20: each quote is a verbatim fragment of the PDF text; the propositions claim no more than the fragments (anchor defects above).
- 30362252 entries 5 to 9: quotes verbatim; "lactate" and "spectroscop" occur once each; no sodium or vigabatrin string; gestational diabetes occurs once; the HSPG2 attribution follows the quoted sentence in the same Results paragraph.
- 36779245 entries 39 to 46: Table 2 row cells parsed from the JATS match the quoted row (13 cells; Patient 5 is VPA, LEV). The broad and strict sets in entry 44 are not defined in the proposition; under the usual sodium-channel-blocker reading the counts (8 and 7) reproduce. Entry 45: vigabatrin appears in the cells of 8 patients (1, 3, 6, 7, 8, 10, 11, 13); 7 of the 10 patients with spasms at onset have it (Patient 6 has none at onset), so "7 of 10" and the table agree.
