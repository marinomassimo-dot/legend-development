# Locator audit, PMID 34268881 targeted reread of 2026-10-25 (blind, 2026-10-25)

Blind audit under `legend-locator-audit`, read-only toward every manifest, registry, receipt and
ledger. The auditor received the eight triples and the source artefacts only: no dossier, no
reader's note, no task record, no reasoning about the reread. Nothing was repaired.

## Scope

The eight entries appended to `disease-models/wwox/research/deepdive_manifests/PMID34268881.json`
on 2026-10-25, taking the manifest from 59 to 67 `verbatim_locators.entries`. They are entries 59
to 66 (zero-based), the tail block, and they are the only entries in the file that speak to the
Figure 4D Wnt qPCR panel, the Figure 4C heatmap, the Figure 4 panel-letter mapping or Figure EV3D.

| Entry | Surface | What it asserts |
|---|---|---|
| 59 | Figure 4D | the panel is a three-genotype (WT / KO / W-AAV) thirteen-gene qPCR at week 15, WT = 1 |
| 60 | Figure 4D | the thirteen WT/KO/W-AAV bar values, and the rescue pattern they describe |
| 61 | Figure 4D | the drawn significance brackets and their comparisons |
| 62 | body | the paper's own sentence about the rescue arm of Figure 4D |
| 63 | Figure 4C | a two-group heatmap, no rescue arm, no statistic |
| 64 | Figure 4 legend | which panels are three-genotype and with what n |
| 65 | Figure EV3D | the three-genotype cortical-layer qPCR values and brackets |
| 66 | Tables EV1/EV2 | which cortical and regional markers are present or absent |

## Image reads

Surfaces were chosen with `framework/scripts/paper_packet.py rank --pmid 34268881`. For Figure 4
the ranked best surface is the embedded raster of page 8 of `PMID34268881_Steinberg2021.pdf`
(xref 33, 1417 x 1157, 200 ppi); the whole-figure JPEG on disk
(`EMMM-13-e13610-g008.jpg`, 712 x 600, ~102 ppi) is the lower-resolution counterpart and was not
used for values. For Figure EV3 the ranked best surface is the embedded raster of page 6 of
`EMMM-13-e13610-s001.pdf` (xref 23, 1312 x 1764, 200 ppi); `EMMM-13-e13610-g004.jpg` is the
659 x 886 counterpart. No placeholder image was encountered and no value was taken from one.

Both panels were calibrated on their own printed ticks, not by eye. Figure 4D: tick centres at
y = 208.5 (6), 401.5 (4), 592 (2), 785 (0) in a zoom-8 render, 96.08 px per unit; bar tops were
taken as the topmost pixel of each bar's own colour in a column run anchored to the baseline, so
the black error-bar caps and the legend swatches (which sit directly above the WNT2B group and
would otherwise be read as bars) do not contaminate the measurement. Figure EV3D: tick centres at
y = 430 (8), 709 (6), 987.5 (4), 1264 (2), 1540.5 (0) in a zoom-12 render, 138.8 px per unit.
Brackets were located by detecting horizontal dark runs of 25 px or more and mapping their
endpoints onto the measured bar centres, then confirmed visually at zoom 18.

## Counts

| Entries judged | SUPPORTED | Adverse (OVERSHOOT or UNDERSHOOT) | UNVERIFIABLE | Wording-level only |
|---|---|---|---|---|
| 8 | 6 | 2 | 0 | 1 |

Adverse rate: 2 of 8 judged entries (25.0 percent). Mode: exhaustive over the declared scope
(every entry added on 2026-10-25, entries 59 to 66); adverse = OVERSHOOT or UNDERSHOOT; no entry
was UNVERIFIABLE, so the denominator is the full eight. Counting the wording-level defect as
well: 3 of 8 (37.5 percent).

**The load-bearing reading holds.** The thirteen-gene panel is what entry 59 says it is, the
third bar is the W-AAV rescue arm and nothing else, all thirteen pairs of numerals in entry 60
reproduce to within 0.04, every bracket in entry 61 is where it is claimed with the asterisk count
claimed, and no value is read from the wrong bar or the wrong gene. No transposition was found.
The two adverse findings are a generalisation in entry 60's headline that its own numerals
contradict, and two wild-type values in entry 65 that the panel does not show.

## Verdict per entry

| Entry | Verdict |
|---|---|
| 59 | SUPPORTED |
| 60 | OVERSHOOT (scope) — the thirteen measured values are exact; the headline is not |
| 61 | SUPPORTED |
| 62 | SUPPORTED |
| 63 | SUPPORTED |
| 64 | SUPPORTED, with wording-level looseness (below) |
| 65 | OVERSHOOT (values) — two wild-type bars are not at 1 |
| 66 | SUPPORTED |

## Adverse findings

| Entry | Verdict | What the panel actually shows |
|---|---|---|
| 60 | OVERSHOOT (scope) | The proposition reads "the WWOX rescue lowers Wnt ligands and the ROR2 receptor toward or below wild type". Four of the six plotted ligands behave that way (WNT1 4.09 to 1.36; WNT3 2.66 to 0.97; WNT3A 1.67 to 0.22; WNT5A 3.10 to 1.97), as does ROR2 (2.66 to 1.16). Two do not: **WNT2B rises from 1.27 in the knockout to 1.87 in W-AAV, and WNT8B rises from 2.23 to 2.48** — both further from wild type, not toward it. The entry's own snippet carries these two numbers, so the quote does not support the unqualified headline it is attached to. The paper's own sentence (entry 62) says "some of the Wnt-related genes" and names only WNT3, WNT3A, WNT1 and ROR2; the proposition drops that qualifier. The second half of the proposition — AXIN2 and CCND1 unmoved, LEF1, TCF7, TCF3 and TCF4 above the knockout — is exact. |
| 65 | OVERSHOOT (values) | The attestation gives every gene a wild-type value of 1. Figure EV3D does not normalise to 1: measured against its own 0/2/4/6/8 ticks the wild-type bars are TBR1 0.99, **BCL11B 0.80**, SATB2 0.99, **POU3F2 0.80**, CUX1 0.99, RELN 0.99. The claimed "BCL11B 1 / 0.25 / 0.4" and "POU3F2 1 / 0.4 / 0.45" therefore overstate the wild-type reference by about 0.2 in both genes, which inflates the apparent depth of the knockout deficit in BCL11B (measured 0.80 / 0.21 / 0.37) and removes the W-AAV recovery in POU3F2 (measured 0.80 / 0.40 / 0.43). SATB2's knockout bar measures 0.28 against the claimed 0.35, at the edge of reading error on a 0-to-8 axis. The remaining values reproduce: TBR1 0.99 / 0.75 / 0.99 (claimed 1 / 0.7 / 1.0), CUX1 0.99 / 1.49 / 0.56 (claimed 1 / 1.55 / 0.55), RELN 0.99 / 5.51 / 3.20 (claimed 1 / 5.5 / 3.2). The proposition itself — BCL11B and RELN remain significantly different from wild type in W-AAV — is carried by the drawn brackets and stands. |

## Wording-level only (the proposition is carried by the source; the phrasing is not exact)

| Entry | Reason |
|---|---|
| 64 | "the only three-genotype panels are D … and H" is not exact: **panel G is also three-genotype** (IF staining in week 15 COs, WT n = 3; KO n = 4; W-AAV n = 4), and H is its quantification. Counting G changes nothing about the proposition, since G and H are the same immunofluorescence experiment and neither is the Wnt readout. Separately, "H (immunofluorescence, n=9/16/4, three batches)" compresses the legend: WT n = 9 from 3 batches and KO n = 16 from 3 batches, but **W-AAV is n = 4 organoids from 1 batch**, not three. The panel-letter mapping the entry relies on is correct (see below). |

## Notes on the entries judged SUPPORTED

- **Entry 59.** The panel is titled "Wnt Target Genes qPCR / Cerebral Oranoids Week 15" — the
  misspelling "Oranoids" is the paper's and is reproduced correctly. The key is three colours,
  WT blue, KO red, W-AAV purple, and each gene group carries exactly three bars in that order;
  the third bar is the rescue arm and is not a second knockout line or a second batch. The
  x-axis labels read, left to right, WNT1, WNT2B, WNT3, WNT3A, WNT5A, WNT8B, ROR2, AXIN2, CCND1,
  LEF1, TCF7, TCF3, TCF4 — the order claimed, thirteen groups, no gene displaced. The y-axis is
  "Relative Expression" with drawn ticks at 0, 2, 4 and 6. Every wild-type bar measures 1.00 to
  1.03 against those ticks.
- **Entry 60, the numerals.** Measured WT / KO / W-AAV against the panel's own ticks, with the
  entry's claim in brackets where it differs by more than 0.03: WNT1 1.03 / 4.09 / 1.36 [4.1 /
  1.35]; WNT2B 1.03 / 1.27 / 1.87 [1.25 / 1.85]; WNT3 1.00 / 2.66 / 0.97 [2.65 / 1.0]; WNT3A
  1.00 / 1.67 / 0.22 [1.65 / 0.2]; WNT5A 1.00 / 3.10 / 1.97 [3.1 / 1.95]; WNT8B 1.00 / 2.23 /
  2.48 [2.2 / 2.45]; ROR2 1.03 / 2.66 / 1.16 [2.65 / 1.15]; AXIN2 1.00 / 1.75 / 1.60 [1.75 /
  1.6]; CCND1 1.00 / 1.03 / 1.24 [1.0 / 1.25]; LEF1 1.00 / 2.29 / 2.59 [2.3 / 2.6]; TCF7 1.03 /
  1.81 / 2.72 [1.85 / 2.7]; TCF3 1.03 / 1.24 / 1.84 [1.2 / 1.8]; TCF4 1.00 / 1.70 / 3.44 [1.7 /
  3.45]. Every one of the thirteen pairs is within 0.04 of the claim. No value belongs to a
  neighbouring bar or a neighbouring gene.
- **Entry 61, the brackets.** Every bracket claimed is drawn, no bracket is claimed that is not
  drawn, and the asterisk counts match. Confirmed group by group: WNT1 one bracket, WT-KO, `*`;
  WNT2B none; WNT3 WT-KO `*` and KO-W-AAV `*`; WNT3A WT-KO `**` and KO-W-AAV `***`; WNT5A WT-KO
  `*` only; WNT8B none; ROR2 WT-KO `***` and KO-W-AAV `**`; AXIN2 WT-KO `*` only, with **no
  knockout-versus-rescue bracket**, as claimed; CCND1 none; LEF1 WT-KO `*` and the long
  WT-W-AAV span `**`; TCF7 WT-KO `*` and the long WT-W-AAV span `**`; TCF3 none; TCF4 three
  brackets — WT-KO `*`, KO-W-AAV `**` and the long WT-W-AAV span `***`. The long spans on LEF1,
  TCF7 and TCF4 measure 45 to 48 px against 24 to 25 px for the single-gap brackets, so they
  cannot be confused with a knockout-versus-rescue comparison.
- **Entry 62.** The sentence "We also observed downregulation of some of the Wnt-related genes in
  W-AAV COs, including WNT3, WNT3A, WNT1, and ROR2" occurs verbatim in the JATS, in the Wnt
  paragraph, immediately after "We next validated some of these genes using qPCR (Fig 4D)". It
  names three ligands and one receptor and says nothing about AXIN2, CCND1, LEF1, TCF7, TCF3 or
  TCF4, exactly as the proposition claims.
- **Entry 63.** The Figure 4 legend's third list item is "Heatmap of Wnt pathway-related genes in
  15-week COs", so the Wnt heatmap is panel C. Read on page 8 it carries four CKO columns and two
  CWT columns under the printed labels CKO and CWT — no third group, no rescue arm — and no
  asterisk, bracket or P value anywhere on it. Its row labels number **exactly 45**: WNT1, WNT5A,
  WNT2B, WNT8B, WNT5B, WNT3A, WNT9A, WNT10B, WNT7B, WNT4, WNT10A, WNT3, WNT11, AXIN2, TCF7L2,
  LEF1, TCF7L1, TCF7, SOX21, SOX2, SOX9, CD44, BMP4, LGR5, CCND1, CCND2, STK32A, ITGA9, IRX3,
  SIX3, SP5, GBX2, MSX2, GATA2, FRAS1, FAM167A, CD83, CGNL1, ROR2, FZD2, FZD10, FZD1, NKD1, WLS,
  ZIC3. "Roughly forty-five" is right. One detail in the anchor is imprecise rather than wrong:
  the -1.0 to 1.0 colour key is the figure's single shared key, printed beneath panel A at the
  foot of the left column, not a key of panel C's own.
- **Entry 64, the panel-letter mapping.** The Figure 4 legend's alpha-upper list resolves as
  A = heatmap of the top 100 up and 100 down genes, B = GSEA, C = Wnt heatmap, D = Wnt qPCR,
  E = week-16 subfractionation western, F = cortical-layer heatmap, G = week-15 IF staining,
  H = quantification of G. The legend's opening clause, "RNA sequencing (RNA-seq) of week 15 COs
  and transcriptome analysis (WT: n = 2, KO: n = 4)", governs A, B, C and F, so C and F do carry
  no rescue arm. Panel D's own sentence gives WT n = 4 from 1 batch, KO n = 4 from 1 batch,
  W-AAV n = 4 from 1 batch. Panel H's gives WT n = 9 from 3 batches, KO n = 16 from 3 batches,
  W-AAV n = 4 organoids from 1 batch. The proposition's core — that within Figure 4 the Wnt
  readout and the maturation readout are never measured on the same samples in the rescue arm —
  holds, since C and F are the two-group RNA-seq and D and G/H are two different assays.
- **Entry 65, the panel identity and brackets.** Figure EV3's legend list makes D "qPCR for
  markers of the six different layers of the human cortex in week 15 COs … (WT: n = 4 from
  1 batch; KO: n = 4 from 1 batch; and W-AAV: n = 4 from 1 batch)", so EV3D is indeed the
  three-genotype cortical-layer qPCR and the matching design to Figure 4D. The panel is titled
  "Cortical Layers qPCR / Cerebral Oranoids Week 15", carries the same WT/KO/W-AAV key and a
  0-to-8 "Relative Expression" axis, and plots TBR1, BCL11B, SATB2, POU3F2, CUX1, RELN in that
  order. The brackets are as claimed: BCL11B WT-KO `*` and the longer WT-W-AAV span `*`; SATB2
  WT-KO `*` only; RELN WT-KO `***` and the longer WT-W-AAV span `**`; TBR1, POU3F2 and CUX1 carry
  none. The proposition's conclusion is therefore carried by the panel; only two of its numerals
  are not.
- **Entry 66.** Every row reproduces from the flattened workbook text by exact-symbol match:
  SATB2 EV2_down padj 5.2E-2 log2FoldChange -0.93; POU3F2 EV2_down 2.1E-3 -0.76; CUX1 EV1_up
  9.01E-4 +0.56; RELN EV1_up 5.88E-12 +4.01; OTX2 EV1_up 1.82E-7 +2.95; NES EV1_up 4.14E-4
  +1.27; GAD1 EV1_up 1.22E-2 +3.57. The eleven symbols declared absent — TBR1, BCL11B, SOX2,
  PAX6, EOMES, TUBB3, FOXG1, SLC17A7, TCF7, CCND1, WNT3 — are absent from both lists. The
  workbook's own headers, "WWOX-KO COs vs WT COs RNA-seq - 1246 upregulated genes" and the
  matching downregulated block, confirm that the deposited dataset is knockout versus wild type
  only, with no rescue arm.
