# src_02 — A01 p4_card.pharmacology: "the levels applied in cells were about 8 to 78 times the class's HDAC enzyme IC50 (arithmetic, not occupancy);"

Card: A01_pba_class, /p4_card/pharmacology. Pointer in the same string: "Re-examined in IT5 (pharmacology_it5_20261029/proteostasis_pba_a01.tsv)"; the arithmetic itself is in missense_recovery_it5_p8_20261029/applied_over_enzyme_ic50_20261029.tsv and README section 5 ("In the two precedents, PBA was applied at about 8 to 78 times its HDAC IC50 (HDAC1 31 to 78; HDAC6 8 to 21)"). Species: human recombinant HDACs / HeLa nuclear extract (enzyme level); applied levels in human HEK293 cells (and C. elegans plates for Guiberson per proteostasis_pba_a01.tsv). Reading depth: tables (ChEMBL-derived TSVs, all rows read); the primaries behind the applied levels are "primary_text_partial_read" in the TSV and were not re-opened here.
Files read in full: drug_repurposing/pharmacology_it5_20261029/proteostasis_pba_a01.tsv (39 rows); drug_repurposing/missense_recovery_it5_p8_20261029/applied_over_enzyme_ic50_20261029.tsv (15 rows); hdac_enzyme_potency_chembl_20261029.tsv (47 rows).

## Table 1: applied_over_enzyme_ic50_20261029.tsv (all 15 rows)
| compound | study | system | applied (uM) | enzyme | IC50 label | IC50 (uM) | ratio |
|---|---|---|---|---|---|---|---|
| PBA | DeLeeuw 2026 (PMID 42157447) | GAT-1 variants, HEK293T (human) | 2000 | HDAC1 | CHEMBL1469 | 64 | 31.2 |
| PBA | DeLeeuw 2026 | HEK293T | 2000 | HDAC1 | CHEMBL1746 (sodium salt) | 162 | 12.3 |
| PBA | DeLeeuw 2026 | HEK293T | 2000 | HDAC6 | CHEMBL1469 | 240 | 8.3 |
| PBA | Guiberson 2018 (PMID 30266908) | Munc18-1 variants, HEK293T and neurons | 5000 | HDAC1 | CHEMBL1469 | 64 | 78.1 |
| PBA | Guiberson 2018 | same | 5000 | HDAC1 | CHEMBL1746 | 162 | 30.9 |
| PBA | Guiberson 2018 | same | 5000 | HDAC6 | CHEMBL1469 | 240 | 20.8 |
| sodium butyrate | DeLeeuw 2026 | HEK293T | 2000 | HDAC1 | low (CHEMBL62381/14227) | 16 | 125.0 |
| sodium butyrate | DeLeeuw 2026 | HEK293T | 2000 | HDAC1 | high (CHEMBL14227) | 300 | 6.7 |
| sodium butyrate | DeLeeuw 2026 | HEK293T | 2000 | HDAC6 | > 2000 (lower bound) | 2000 | at most 1.0 |
| sodium butyrate | Guiberson 2018 Supp Fig 12a | HEK293T | 5000 | HDAC1 | low | 16 | 312.5 |
| sodium butyrate | Guiberson 2018 Supp Fig 12a | HEK293T | 5000 | HDAC1 | high | 300 | 16.7 |
| sodium butyrate | Guiberson 2018 Supp Fig 12a | HEK293T | 5000 | HDAC6 | > 2000 | 2000 | at most 2.5 |
| SAHA vorinostat | DeLeeuw 2026 | HEK293T | 2.5 | HDAC1 | median 0.076 | 0.076 | 32.9 |
| SAHA vorinostat | DeLeeuw 2026 | HEK293T | 2.5 | HDAC6 | median 0.038 | 0.038 | 65.8 |
Recomputed: 2000/64 = 31.25; 2000/162 = 12.35; 2000/240 = 8.33; 5000/64 = 78.1; 5000/162 = 30.9; 5000/240 = 20.8; 2000/16 = 125; 2000/300 = 6.67; 5000/16 = 312.5; 5000/300 = 16.7; 2.5/0.076 = 32.9; 2.5/0.038 = 65.8 (all the TSV ratios reproduce).

## Table 2: PBA applied levels listed in proteostasis_pba_a01.tsv (rows "applied concentration (not a potency)"; cells human unless stated)
| study | system | level | note |
|---|---|---|---|
| Shah 2025 (PMID 40485335) | GAT-1 G443V, HEK293 | 10 mM, 24 h | fly food arm 1 mM, 48 h |
| DeLeeuw 2026 (PMID 42157447) | SLC6A1 variants, HEK293T | 2 mM, 24 h (butyrate 2 mM, SAHA 2.5 uM, salubrinal 15 uM, TUDCA 100 uM) | |
| Song 2026 (PMID 42587736) | GABRA1 variants, HEK293T; mouse arm 100 mg/kg/day i.p. 7 days | 2 mM | brain exposure not measured |
| Delahanty 2026 (PMID 42650175) | transporter variants, cells | 0.5, 1, 2 mM; 4 mM compromised viability | toxicity ceiling |
| Guiberson 2018 (PMID 30266908) | Munc18-1 variants, C. elegans on plates (this row) | 5 mM | |
| DeLeeuw 2026 | TUDCA | 100 uM | no HDAC potency for TUDCA |

## Table 3: enzyme potency rows for the class (proteostasis_pba_a01.tsv + hdac_enzyme_potency_chembl_20261029.tsv)
PBA (CHEMBL1671826, recombinant human): HDAC1 64, HDAC2 65, HDAC3 260, HDAC6 240, HDAC8 93 uM (IC50). Sodium PBA (CHEMBL5136998): HDAC1 162 uM (IC50). HeLa nuclear extract (CHEMBL1155249, Ki): PBA 2.8 uM; sodium PBA 6.34 uM; butyric acid 136 uM; sodium butyrate 365 uM (IC50 800 uM). Butyrate recombinant: HDAC1 16 / 300, HDAC2 12 / 400, HDAC3 9, HDAC8 15 uM, HDAC6 > 2000 uM. Vorinostat median HDAC1 76 nM, HDAC6 38 nM.

## Recomputation: every PBA applied level over every PBA enzyme value (applied / IC50 or Ki; unitless; computed here)
| applied level | PBA HDAC1 CHEMBL1671826 IC50 64 uM | PBA HDAC2 65 uM | PBA HDAC3 260 uM | PBA HDAC6 240 uM | PBA HDAC8 93 uM | sodium PBA HDAC1 CHEMBL5136998 162 uM | PBA HeLa extract Ki 2.8 uM (acid) | sodium PBA HeLa Ki 6.34 uM |
|---|---|---|---|---|---|---|---|---|
| Delahanty 2026 low of 0.5/1/2 mM series (0.5 mM) | 7.8 | 7.7 | 1.9 | 2.1 | 5.4 | 3.1 | 178.6 | 78.9 |
| Song 2026 / DeLeeuw 2026 (2 mM) (2.0 mM) | 31.2 | 30.8 | 7.7 | 8.3 | 21.5 | 12.3 | 714.3 | 315.5 |
| Guiberson 2018 (5 mM, worm plates per card IT5 table; HEK293T/neurons per applied table) (5.0 mM) | 78.1 | 76.9 | 19.2 | 20.8 | 53.8 | 30.9 | 1785.7 | 788.6 |
| Shah 2025 (10 mM, HEK293) (10.0 mM) | 156.2 | 153.8 | 38.5 | 41.7 | 107.5 | 61.7 | 3571.4 | 1577.3 |

## Result
The sentence's 8 to 78 is exactly the PBA rows of Table 1 (min 8.3 = 2 mM / HDAC6 240 uM; max 78.1 = 5 mM / HDAC1 64 uM): it covers two precedents (2 and 5 mM), PBA only, recombinant IC50 only, and only HDAC1 and HDAC6. Left out of the "class" and "levels applied in cells" spread, all in the same card and files: (a) the 10 mM level (Shah 2025) and the 0.5 mM level (Delahanty 2026), (b) PBA on HDAC2/3/8 (65, 260, 93 uM), (c) the HeLa-extract Ki of 2.8 uM that the same card sentence quotes just before ("one HeLa extract study: low micromolar"), which gives about 180 to 3,600 times at 0.5 to 10 mM, (d) the other class member butyrate (6.7 to 312.5 times in Table 1; at most 1.0 to 2.5 for HDAC6), and vorinostat (32.9 to 65.8; not class but used as comparator). With all PBA applied levels (0.5 to 10 mM) over all recombinant PBA IC50s (64 to 260 uM) the ratios run 1.9 to 156; with the extract Ki up to 3,571.
