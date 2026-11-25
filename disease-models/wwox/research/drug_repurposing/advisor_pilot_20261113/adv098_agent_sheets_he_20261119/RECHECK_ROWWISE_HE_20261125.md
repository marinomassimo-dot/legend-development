# Row-by-row re-check of the ADV-098 compound sheets (HE 9c2cb46c, 2026-11-25)

Asked by ADV after omissions of one class were found (a ratio computed against the quoted row only). Reference genotype
class only; hypothesis level; no dose; not medical advice.

## Result

All twelve sheets. **170 claims checked, 46 wrong or incomplete (27 percent), all corrected.** Four further errors had been
corrected earlier the same day by a sampled pass (bexarotene RAR rows, d-AP5, TMP195 document ratio, the PDK4 row);
they are among the claims checked and not among the 46.

| Batch | claims checked | wrong or incomplete, corrected |
|---|---:|---:|
| 1 | 15 | 5 |
| 2 | 11 | 2 |
| 3 | 13 | 3 |
| 4 | 20 | 5 |
| 5 | 11 | 2 |
| 6 | 16 | 6 |
| 7 | 12 | 3 |
| 8 | 13 | 4 |
| 9 | 22 | 10 |
| 10 | 15 | 4 |
| 11 | 14 | 1 |
| 12 | 8 | 1 |

## Error classes

| Class | count | ids |
|---|---:|---|
| a row or comparator left out of a ratio, range or spread | 19 | 1d 1e 2b 3b 4e 6a 6b 7a 8b 8d 9a 9b 9c 9d 9e 9j 10b 11a 12a |
| a count wrong or wrongly labelled | 20 | 1b 1c 2a 3a 3c 4a 4b 4c 4d 5a 5b 6d 6e 6f 7b 8c 9f 9h 9i 10d |
| a whole document left out, or a quote of selected documents | 4 | 7c 8a 10a 10c |
| a bound written as a measured value | 1 | 9g |
| other (a flag omitted; a comparator said present where absent) | 2 | 1a 6c |
| unit | 0 |  |

The two commonest classes hold 39 of 46.

**By producer:** every sheet was written by an HE window itself (not by a delegate), Claude Sonnet 5.5 at effort high
(commit trailers; session transcripts for the writes found). There is no second model or effort, so no rate comparison.

## What this re-check missed (added after IT's blind check)

IT gave a blind reader the card sentences and the whole held answers
(`../../brainstorm_20261116/it24_checkpoint23_queue_20261125/VERIFIER_REPORT_AS_DELIVERED_A_IT24.txt`). It found nine
points that also belong in the sheets, applied here with ids 6g, 7d to 7g, 8e, 8f, 9k, 9l: a second panel that moves a
selectivity reading, two same-document values that change a comparison, two statements too strong ("that document's
only", "not found in these rows"), a tissue named that the row does not name, and validity flags left out. So "46
wrong or incomplete of 170" is what one reader found, not the number there was: the rate is higher by at least these
nine, on the sheets IT's cards touch (6, 7, 8, 9). The other eight sheets have had no blind check.

## Method and limits

Every fold, ratio, range, spread and row count that a sheet takes from the held ChEMBL answers was recomputed against
all rows of the held answers (root checkout `files/adv098_agent_sheets_raw_he_20261119/` and
`files/adv113_m1_comparators_raw_he_20261120/`), matched by target name and by gene symbol without regard to case. Not
covered: text from abstracts, titles, labels and trial registries; SCI-origin lines; counts from queries that are not
held (the 334 EBP rows of batch 12); rows of compounds not held (the sibling tetraamines of the memantine 0.95 nM
assay). One reader, the author of the sheets' own role, and **no blind check of this re-check**. Claim counts depend on
how a sentence is cut; the list of corrections does not.

## What changes for a reader

- 10a: tazemetostat antiproliferation was shown only in lines above 3 microM; held rows reach 2.3 nM in EZH2-mutant
  lymphoma lines. This was the most misleading sentence found.
- 8a: dichloroacetate PDK values and their isozyme order are one document's; two other documents disagree.
- 9d, 9e, 9g: GSK-3 ranges narrower than the rows; kinase lower bounds written as measured Ki.
- 7c: bexarotene RXR-alpha quoted as two or three values; rows run 2.7 to 149 nM (EC50).
- 6a: muscarinic disagreement between sources reaches 19-fold. 1e: memantine spread about two orders, not five.
- ADV-283: SCI's judgement that PDK3 is not shown relevant rests on transcript data and reads the same; 'PDK3 least
  inhibited' holds inside CHEMBL4007440 only.

## Causes

1. A fold or range written from the rows in view, not from a query of all rows.
2. A large answer read by its main groups and summarised as a whole.
3. `recipe_tabulate_activities.txt` matches expected genes in upper case only, so rat and mouse rows of the same gene
   were counted as "other targets".
4. "targets" or "rows" used without saying which (for example targets with a measured value).

## Checklist before a number leaves a sheet (adopted by HE for this work)

- Compute each fold, ratio or range with a query over every row of the held answer for that target; print the rows;
  quote the extremes, and group by document before saying "one document".
- Say of a `>` row that it is a bound. A count says what it counts.
- **A blind verification packet carries the whole source table the number was computed from, not the one quoted row.**

## Cards that carry a changed value (sent to IT; HE edits no card)

| Card | change | batch |
|---|---|---|
| D02_wnt_tankyrase | GSK-3 alpha/beta "1.4- to 2.5-fold" becomes "1.0- to 2.5-fold" | 9 |
| F02_myelination_activity_sign | natural hormone ratio 0.5 to 1.0; RXR-alpha EC50 2.7 to 149 nM; bexarotene RXR preference | 6, 7 |
| E03_pdk_inhibition_dca, I01 | four isozymes within one document; other documents disagree | 8 |
| H01_apinocaltamide_ttype | its parenthesis "the sheet says about 2.5-fold" is now out of date: the sheet says about 3-fold | 11 |

E01, L01 and M01: read, no change required. No card cites batches 1 to 5 or 12.

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

**4c** batch 4
- before: (21 rows, 18 on the NMDA receptor or its binding site)
- after: (21 rows, 19 on the NMDA receptor or its binding site; two of the 19, 170 and 2,260 nM, equal the ratios 280/1640 and 3710/1640 and look like subunit ratios stored as Ki)

**4d** batch 4
- before: appears on about 25 rows with
- after: appears on 22 rows with

**4e** batch 4
- before: The values span 0.5 to 53 microM across assays:
- after: The IC50 values span 0.5 to 53 microM across assays (Ki rows go down to 0.18 microM):

**7a** batch 7
- before: against 0.66 nM Ki (DrugMatrix, human): different species and sources.
- after: against 0.66 nM Ki (DrugMatrix, human; the same panel gives IC50 1.46 nM): different species and sources.

**7b** batch 7
- before: cytochrome P450 3A5 and 3A4 rows and bile salt export pump rows (3 each) are the other groups.
- after: cytochrome P450 3A5 (7 rows), 3A4 (4 rows) and bile salt export pump (3 rows) are the other groups.

**7c** batch 7
- before: other documents give RXR-alpha EC50 28 and 42 nM and Kd 36 nM (1995 and 2002).
- after: other documents give human RXR-alpha EC50 from 2.7 to 149 nM and Kd from 14 to 1,890 nM (measured rows).

**8a** batch 8
- before: Another 1999 row gives IC50 above 2 mM for PDK in vitro
- after: **The order and the size of these values are that document's only:** CHEMBL4177695 (2017, GST-tagged PDK from Sf9 cells) reads PDK1 5.1 mM and PDK2 9.0 mM, PDK1 and PDK2 in the reverse order; CHEMBL6121009 (2025, radiometric) reads PDK1 3.66 mM, PDK2 and PDK3 above 5 mM and PDK4 0.108 mM; two 2023 rows give PDK1 only as bounds (above 0.1 mM; EC50 above 0.05 mM). "PDK3 is the least inhibited" is therefore a statement about CHEMBL4007440. Another 1999 row gives IC50 above 2 mM for PDK in vitro

**8b** batch 8
- before: (DrugMatrix, [3H]ketanserin) against IC50 243 nM in an HTRF cAMP assay (2020): a 12-fold spread by assay type.
- after: (DrugMatrix, [3H]ketanserin) against IC50 243 nM in an HTRF cAMP assay (2020): a 12-fold spread by assay type (14-fold when the rat receptor row, IC50 17 nM, 1999, is counted).

**8c** batch 8
- before: - **Potency (43 rows):** PDK isozymes as above (millimolar); 5 cytotoxicity rows in leukemia cell lines at 8 to 14 mM (MTT, 48 hours, 2016); five "non-protein target" rows. The compound acts at millimolar concentrations in these assays.
- after: - **Potency (43 rows):** PDK isozymes as above (0.108 to 9.0 mM, plus bounds); five 2016 cytotoxicity rows at 8 to 14 mM (MTT, 48 hours), filed by ChEMBL as "non-protein target"; further cell-viability rows from other documents (measured values 11 to 40 mM, the rest bounds). The compound acts at about 0.1 mM and above in these assays.

**8d** batch 8
- before: Dichloroacetate acts at millimolar concentrations in the rows read:
- after: Dichloroacetate acts at about 0.1 mM and above, mostly millimolar, in the rows read:

**10a** batch 10
- before: Antiproliferative IC50 is above 3 microM in six wild-type EZH2 lymphoma lines (2025) and 17.8 microM in one EZH2-overexpressing line (2020); one 2024 row gives 1.07 microM in MINO cells. The exposure time of those growth assays was not read for every row.
- after: Antiproliferative values are not one number either: in EZH2-mutant lymphoma lines 2.3 to 299 nM in six documents (Pfeiffer, KARPAS-422, WSU-DLCL2), but 14 to 22 microM for lines of that kind in two others (an EZH2-overexpressing description of WSU-DLCL2 and SUDHL4, 2020; SU-DHL-6, 2024); above 3 microM in six wild-type lines (2025); 1.1 to 1.2 microM in MINO and OCI-Ly7 (2024); micromolar values or bounds in other cancer lines. The exposure time of those growth assays differs and was not read for every row.

**10b** batch 10
- before: about 6- to 370-fold (two places)
- after: about 6- to 420-fold

**10c** batch 10
- before: (about 7-fold). The three documents disagree by more than tenfold on the ratio
- after: (about 7-fold); CHEMBL5729508: 2.45 against 140 nM (about 57-fold). The four documents disagree by more than tenfold on the ratio

**10d** batch 10
- before: appears in five documents (2020 to 2023) as a quotation of the 2015 value (document CHEMBL3414551)
- after: appears in five documents, the 2015 original (CHEMBL3414551) and four of 2020 to 2023 that quote it

**11a** batch 11
- before: species values within about 2.5-fold of the human ones, rat Cav3.3 (4-fold lower than human) the largest difference.
- after: species values within about 3-fold of the human ones (dog Cav3.1 3.1-fold) except rat Cav3.3 (IC50 4-fold lower than human), the largest difference.

**12a** batch 12
- before: run from about 5-fold to about 180-fold depending on the document, subtype and species.
- after: run from about 1.7-fold (M5 against M1, CHEMBL1137537, 2007) to about 180-fold depending on the document, subtype and species.
