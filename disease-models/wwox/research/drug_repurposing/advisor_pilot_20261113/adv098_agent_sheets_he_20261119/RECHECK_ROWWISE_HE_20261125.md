# Row-by-row re-check of the ADV-098 compound sheets (HE 9c2cb46c, 2026-11-25)

Asked by ADV after two omissions of one class were found (a ratio computed against the quoted row only). Reference
genotype class only; hypothesis level; no dose; not medical advice.

## Method

Every fold, ratio, range, spread and row count that a sheet takes from the held ChEMBL answers was recomputed against
**all** rows of the held answer (root checkout `files/adv098_agent_sheets_raw_he_20261119/`, digests in
`SHA256SUMS_raw_activities.txt`), matched by target name and by gene symbol without regard to case. Not covered: text
from abstracts, titles, labels and trial registries; SCI-origin dated lines; values of compounds whose rows are not held
(the sibling tetraamines of the 0.95 nM memantine assay). One reader, no blind check of this re-check.

## Counts

| Batch | claims checked | wrong or incomplete | of which false as written | corrected |
|---|---:|---:|---:|---:|
| 1 | 15 | 5 | 1 | 5 |
| 2 | 11 | 2 | 1 | 2 |
| 3 | 13 | 3 | 3 | 3 |
| 5 | 11 | 2 | 2 | 2 |
| 6 | 16 | 6 | 6 | 6 |
| 9 | 22 | 10 | 9 | 10 |
| **total** | **88** | **28** | **22** | **28** |

A claim is one sentence or one count; 6d and 6e are the same fact in two places. Batch 4 was not in the list asked for;
the search for the third cause below found its two count lines (4a, 4b), corrected too and not counted in the table.

## What changes and what does not

No closing conclusion of a sheet is reversed. Five statements move by enough to matter to a reader:

- 9d, 9e: three of the five GSK-3 beta ranges were narrower than the held rows (tideglusib spread: more than 2,000-fold,
  not 400-fold; AR-A014418: 9 of 22 rows outside the quoted 38 to 104 nM).
- 9g: three kinase lower bounds ("above") had been written as measured Ki values.
- 6a: the muscarinic disagreement between two sources reaches 19-fold (the M4 pair had been left out).
- 1e: memantine rows disagree by about two orders, not five, once the probable unit error is set aside.
- 9a, 9j: GSK-3 alpha against beta is 1.0- to 2.5-fold (not 1.4-), with one weak 4.7-fold alpha-preferring pair. The
  IT59 audit of the GSK-3 packet had reported that pair and the sheet was not changed then.

## Causes

1. A fold or range written from the rows in view, not from a query of all rows (6a, 9a, 9d, 9e, 2b, 3b).
2. A table read in part and summarised as a whole (9g, 5b, 3a).
3. `recipe_tabulate_activities.txt` matches expected genes in upper case only, so rat and mouse rows of the same gene
   were counted as "other targets" and left out of "rows on the symbols" (1b, 1c, 2a, 3c, 4a, 4b).
4. "targets" used for "targets with a measured value" (9f, 9h, 9i).

## Checklist before a number leaves a sheet (adopted by HE for this work)

- Compute each fold, ratio or range with a query over every row of the held answer for that target and document; print
  the rows; quote the extremes.
- Say of a `>` row that it is a bound.
- A count says what it counts (rows, targets, targets with a measured value).
- **A blind verification packet carries the whole source table the number was computed from, not the one quoted row.**
  A packet holding only the quoted row cannot see an omission, which is why the earlier checks passed these.

## Cards and views that carry a changed value (for IT; HE edits no card)

| Card | text now | text the rows support | source rows |
|---|---|---|---|
| D02_wnt_tankyrase (`input.p4_card.pharmacology`, packet, join, views) | "alpha about 1.4- to 2.5-fold weaker than beta at most within one document and assay" | "alpha at most about 2.5-fold weaker than beta (1.0- to 2.5-fold) within one document and assay" | batch 9, 9a: CHIR-99021 2 against 2 nM, CHEMBL5728885; AR-A014418 Ki 25.1 against 25.1 nM, CHEMBL1201862 |
| F02_myelination_activity_sign (same field) | "the natural hormone is about equipotent on both receptors in nearly every same-document pair" | "the natural hormone's alpha-to-beta ratio is 0.5 to 1.0 in the seven same-document pairs that carry it; one of the eight has none" | batch 6, 6b and 6c: liothyronine rows of CHEMBL1135520, CHEMBL1145987, CHEMBL1152303, CHEMBL3259553, CHEMBL5723379, CHEMBL5727487; none in CHEMBL2203261 |
| F02, bexarotene sentence | already sent to IT (IT checkpoint 23 queue) | see batch 7 | CHEMBL1130267 |

Cards that cite other batches (E01, E03, H01, I01, L01, M01) were not searched for these values beyond the literal
patterns, which found none. Documents of SCI and IT that say "at most about 2.5-fold" (unit C v2.2, broad one page v3,
ADV158) stay true with the weak pair set apart.

## Sheet lines, before and after

**1a** batch 1, line 8
- before: a row ChEMBL leaves **without a mapped gene** (target "Unchecked"), so it does not count as CACNA1G, H or I.
- after: a row ChEMBL leaves **without a mapped gene** (target "Unchecked"), so it does not count as CACNA1G, H or I; ChEMBL flags this row "outside typical range" too.

**1b** batch 1, line 22
- before: 84 activity rows; 22 on NMDA receptor subunit symbols.
- after: 84 activity rows; 38 on NMDA receptor subunit symbols, 22 of them human.

**1c** batch 1, line 24
- before: 24 other targets in the rows (acetylcholinesterase, cholinesterase, parasite targets), not selectivity.
- after: 24 other (target, species) entries outside the human subunit rows, which include rat NMDA receptor rows as well as acetylcholinesterase, cholinesterase and parasite targets; not selectivity.

**1d** batch 1, line 36
- before: keep the 0.84 to 6.7 microM band for human recombinant GluN1/GluN2A as the working range, with the assay stated.
- after: keep the 0.84 to 6.7 microM band for human recombinant GluN1/GluN2A as the working range, with the assay stated. This band is not the range of all rows: it holds six of the eight human recombinant GluN1/GluN2A rows left, and 28.1 microM (CHEMBL6083260, -40 mV) and 31.6 microM (CHEMBL6115009, calcium flux, 24 hours) lie above it.

**1e** batch 1, line 32
- before: Memantine has many values and they disagree by up to five orders by assay; the assay must be chosen before the number.
- after: Memantine has many values and they disagree by about two orders by assay (IC50 and Ki rows from 0.54 to 55 microM, one rat Ki above 100 microM), setting aside the 0.95 nM row that the dated lines below judge a probable unit error; the assay must be chosen before the number.

**2a** batch 2, line 13
- before: 32 activity rows; 13 on KCNQ symbols by gene; 11 other targets (not selectivity).
- after: 32 activity rows; 13 on human KCNQ2 or KCNQ3; the 11 other (target, species) entries include human KCNQ4 and KCNQ5 and rat and mouse KCNQ2 rows (not selectivity).

**2b** batch 2, line 10
- before: mouse Kv7.2 1.3 microM, human Kv7.2 0.93 to 4.2 microM:
- after: mouse Kv7.2 1.3 microM, human Kv7.2 from below 0.15 to 4.2 microM (below 0.15 microM in 2007 and 0.35 microM twice in 2018, all by Rb+ flux):

**3a** batch 3, line 20
- before: 19 rows, 3 not on GABA-A (SARS-CoV-2 cytotoxicity rows, GABA-B, GABA uptake: IC50 above 100 to 500 microM, no activity).
- after: 19 rows; 5 on neither GABA-A nor GABA-rho (two SARS-CoV-2 cytotoxicity rows, one GABA-B, two GABA uptake: no activity up to limits of 20 to 500 microM) and two on GABA-rho1 (formerly GABA-C), Ki 100 microM.

**3b** batch 3, line 29
- before: sits 50 to 100 times above ganaxolone's modulation EC50
- after: sits about 50 to 140 times above ganaxolone's modulation EC50

**3c** batch 3, line 13
- before: one other target in the rows;
- after: no row outside GABA-A: the one entry counted apart from the human subunit rows is the rat GABA-A binding row;

**4a** batch 4, line 20
- before: 342 rows; 18 on NMDA receptor subunit symbols
- after: 342 rows; 40 on NMDA receptor subunit symbols, 18 of them human

**4b** batch 4, line 21
- before: 135 other targets appear in the rows (DrugMatrix panels, receptors, transporters):
- after: 135 other (target, species) entries appear outside the human subunit rows (rat NMDA receptor rows, DrugMatrix panels, receptors, transporters):

**5a** batch 5, line 11
- before: 15 rows; 6 on ABAT in vitro. Seven other rows are transporter panels (BSEP, MRP2, MRP3, MRP4: IC50 above 133 microM) and a SARS-CoV-2 cytotoxicity screen (above 20 microM): no activity at the concentrations tested.
- after: 15 rows; 9 on ABAT in vitro (3 human, 3 rat, 2 pig, 1 mouse). The six other rows are four transporter panel rows (BSEP, MRP2, MRP3, MRP4: IC50 above 133 microM) and two of a SARS-CoV-2 cytotoxicity screen (above 20 microM): no activity at the concentrations tested.

**5b** batch 5, line 18
- before: BSEP IC50 above 133 to 526 microM (vesicle assays, 2010 to 2013); 15 antiparasitic rows
- after: BSEP IC50 526 microM in one assay and above 133 and 135 microM in two others (vesicle assays, 2010 to 2013); 16 antiparasitic rows

**6a** batch 6, line 11
- before: differ by 3 to 7 times for the same muscarinic receptor (M3 8.3 nM against 56 nM; M5 6.0 against 27.5 nM)
- after: differ by about 5 to 19 times for the same muscarinic receptor (M3 8.3 against 56 nM; M4 2.8 against 54 nM; M5 6.0 against 27.5 nM)

**6b** batch 6, line 8
- before: about 1-fold in nearly every pair (for example
- after: 0.5- to 1.0-fold in the seven pairs that carry it (for example

**6c** batch 6, line 8
- before: in each document the comparator is measured in the same assay.
- after: in seven of the eight sobetirome pairs the comparator is measured in the same document and assay type; the 2012 document (12.5-fold) holds no T3 row.

**6d** batch 6, line 23
- before: (17 rows, all on thyroid hormone receptors)
- after: (17 rows: 16 on thyroid hormone receptors and one unrelated screen, IC50 above 100 microM; corrected 2026-11-25, HE; see the dated line at the end)

**6e** batch 6, line 24
- before: (rows are TR only)
- after: (apart from that one screen row, rows are TR only)

**6f** batch 6, line 15
- before: also appear (3 rows each, values not tabulated here)
- after: also appear (3 rows each for hERG, sigma-1 and alpha-2A; 2 rows without a value for beta-1; values not tabulated here)

**9a** batch 9, line 6
- before: Ki 10 against 3.98 nM (the "Navigating the Kinome" panel): alpha about 1.4- to 2.5-fold weaker than beta.
- after: Ki 10 against 3.98 nM (the "Navigating the Kinome" panel), 2 against 2 nM (2021, a Caliper panel): alpha 1.0- to 2.5-fold weaker than beta.

**9b** batch 9, line 6
- before: and 1.5 against 0.9 nM (2019): 1.7-fold.
- after: and 1.5 against 0.9 nM (2019): 1.7-fold; the same 2019 document's mutant constructs read 1.02 (alpha S449A) against 1.29 nM (beta H350L), 0.8-fold.

**9c** batch 9, line 6
- before: So the five agents are, at most, about 1.4- to 2.5-fold beta-preferring or not distinguished;
- after: So, setting aside the weak 2011 FRET pair of AR-A014418 (4.7-fold, alpha-preferring), the agents with a pair are not distinguished or at most about 2.5-fold beta-preferring;

**9d** batch 9, line 7
- before: 3 to 30 nM (CHIR-99021)
- after: 2 to 30 nM (CHIR-99021; six further rows of 10 microM are myeloma cell-growth assays, not enzyme inhibition)

**9e** batch 9, line 7
- before: 38 to 104 nM Ki and IC50 (AR-A014418; two outliers from other assays: Ki 770 nM in 2012 and IC50 330 microM in the 2011 FRET assay) and 5 nM to 2 microM (tideglusib, a spread of 400-fold across documents)
- after: 2.1 nM to 330 microM (AR-A014418: 22 IC50 and Ki rows, 13 of them between 38 and 104 nM) and 5 nM to above 10 microM (tideglusib, a spread of more than 2,000-fold across documents)

**9f** batch 9, line 12
- before: 124 Ki rows on 9 targets named by gene symbol;
- after: 124 Ki rows on 124 targets, 9 of them with a measured value and 115 reported only as above a limit (lowest limit 398 nM);

**9g** batch 9, line 12
- before: The kinases outside GSK-3 in that set carry Ki values of 6 to 10 microM in the rows I read (for example MRCK alpha 10 microM, CAMK2G 6.3 microM, CSNK1G2 7.9 microM).
- after: Outside GSK-3 the seven measured Ki values are 1.6 to 6.3 microM (lowest: CDK2 and CLK4, 1.6 microM); the figures first quoted for MRCK alpha, CAMK2G and CSNK1G2 (10, 6.3, 7.9 microM) are lower bounds ("above"), not measured values.

**9h** batch 9, line 13
- before: 79 rows on 6 targets in the same set;
- after: 79 rows on 79 targets in the same set, 6 of them with a measured value (outside GSK-3: 5 to 10 microM);

**9i** batch 9, line 14
- before: 80 rows on 24 targets in the same set,
- after: 80 rows on 80 targets in the same set, 24 of them with a measured value (0.25 to 7.9 microM; lowest CDK2, 251 nM),

**9j** batch 9, line 42
- before: Alpha against beta: at most 2.5-fold in the same-document pairs;
- after: Alpha against beta: at most 2.5-fold beta-preferring in the same-document pairs, the one weak FRET pair of AR-A014418 (4.7-fold, alpha-preferring) set apart;
