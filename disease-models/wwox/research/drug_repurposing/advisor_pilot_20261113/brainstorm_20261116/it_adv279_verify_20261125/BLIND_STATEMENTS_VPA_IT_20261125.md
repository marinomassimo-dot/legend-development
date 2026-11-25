# Statements to check (blind). For each: SUPPORTED / NOT SUPPORTED / PARTLY, and whether the source says MORE or LESS.

Paths: F = /home/desktop/legend-development/files ; D = /home/desktop/.claude/jobs/5fef7cc4/tmp/adv275/data
Repository (read-only) = /home/desktop/legend-development/.claude/worktrees/it_22_20261125
B = <repository>/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116

## Group H — valproate in one carcinoma line
Source: F/fulltext/PMID23464470_Yan2012_APJCP_journal_pdf_2026-11-25.pdf (expected sha256 c2a1066186030672a2a4c4ed0ad6efe82a594cb370073f41a2c4fc610485d778)
H1. A human ovarian carcinoma line, HO8910 (the paper of PMID 23464470), shows WWOX protein UP with sodium valproate 1 to 4 mmol/L over 48 h (pixel estimate 1.6 to 3.2 times control at 2 to 4 mmol/L, one blot, loading control beta-actin) and WWOX protein and mRNA UP in xenograft tumours (protein 0.46 against 0.15; mRNA 0.305 against 0.193; ten mice per arm, tumours taken at death, survival 47 versus 35 days, n per measurement not stated).
H2. It is a cancer line, one blot per panel, no replicate unit stated for the in-vitro blot; no in-vitro WWOX number is printed. The paper states WWOX is wild type in this line (check whether it does: the sentence "it is a cancer line with wild-type WWOX" is to be judged separately).
H3. "A second platform": it comes from a different laboratory and a different cell system than the neural-lineage hESC systems.

## Group I — independence statement
Sources: F/fulltext/PMID15266310_Park2004.xml ; F/fulltext/PMID18460020_Nakayama2008_PMC.txt ; F/fulltext/PMID26272509_Rempel2015_supplement/204_2015_1573_MOESM2_ESM.xlsx (and its _xlsxdump.txt) ; abstracts of PMIDs 16818616, 25720522, 20737170, 17019711 via the PubMed tool.
I1. In the Rempel table, sheet "VPA-sheet 15": the WWOX probe sets have fold changes 1.19, 1.43, 1.09, 1.33, 1.68 with adjusted p 0.321, 0.011, 0.602, 0.027, 0.007; sheet "TSA-sheet 14": 1.15, 1.22, 1.01, 0.79, 0.89 with adjusted p 0.141, 0.032, 0.944, 0.018, 0.155; sheet "SAHA-sheet 12" largest 1.24; "Belinostat-sheet 2" largest 1.23; "Panobinostat-sheet 9" smallest adjusted p 0.138. Find also the entinostat sheet.
I2. "Class heterogeneity in the one table that has all six inhibitors: valproate, entinostat and trichostatin A move at least one of five WWOX probe sets, panobinostat, belinostat and vorinostat none." State which threshold makes this true or false (adjusted p alone? fold change?), and what cell system and exposure the table is.
I3. PMID 15266310: hepatocellular lines, 5-aza plus trichostatin A combined, no change, "not shown".
I4. PMID 18460020: pancreatic line, supplementary Fig S1B legend with 5-aza-dC (5 uM) and/or TSA (1 uM), 5 days; the figure itself is not held.
I5. "Six further reports are abstract or legend level, all with trichostatin A and five with 5-aza-2'-deoxycytidine in the design, in lines selected for WWOX silencing (prostate PMID 16818616; gastric PMID 25720522 and PMID 20737170; lung xenograft PMID 17019711, WWOX re-measurement not stated; pancreatic PMID 18460020, figure not held); they test reactivation, not modulation of expressed WWOX." Note that the list names five PMIDs for "six": say what is missing (see B/it_adv273_20261125/RESULT_ADV273_IT_20261125.md rows only to learn which sixth report is meant, then judge it from its own source).

## Group J — deposited neural tables (GEO), transcript only
Sources: D (series matrices, raw counts, annotation tables); the table B/it_adv275_20261125/adv275_contrasts.tsv is the CLAIM UNDER TEST, not a source; recompute the quoted contrasts from D with your own code.
J1. WWOX mRNA is higher with valproate in: GSE129241 (induced neurons, valproate added day 1, 4 against 4, 1.28-fold); GSE232218 (brain organoids, 400 uM, 4 against 4, 1.41); GSE241903 (spinal-cord organoids, 3 against 3, 1.91); GSE187006 (forebrain organoids of two lines, 3 against 3 each, 1.50 and 1.63). Report what the replicate units are according to the deposits.
J2. GSE166297 agrees but is one experiment with technical replicates.
J3. "No contrast read, 57 in 32 deposits (56 of them in non-transformed or non-tumour neural material), calls WWOX lower." (check the counts in the table and its series_call column; you need not recompute all 57).
J4. GSE305320 spinal-cord organoids 0.88; GSE185453 adult mouse hippocampus and striatum with an HDAC inhibitor, 0.95 and 0.88 (state which compound).
J5. "The pre-registered prediction that more than half of the sentinel-passing contrasts would not distinguish WWOX failed (7 of 22)." (PREREG in the same folder.)
