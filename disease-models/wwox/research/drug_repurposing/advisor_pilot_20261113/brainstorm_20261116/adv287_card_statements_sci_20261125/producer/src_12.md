# src_12 — F01 DA-W2-004 measured_result_note: "No consistent GRIN2B or GRIN2D shift at 4 versus 2 libraries;"

Card: F01_glutamate_receptor_node, /disease_assertions/3/measured_result_note (DA-W2-004; GSE156243, PMID 34268881 deposit; locator drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv; reading_depth queried_not_full_read; INFERENZA). Species/system: human WWOX-knockout cerebral organoid (engineered KO, culture week 15, bulk RNA, one laboratory), 4 knockout libraries (cko1-4) vs 2 wild-type (cwt1-2). Transcript, not receptor function.
Held: the panel TSV (26 genes, every row read) and the raw Salmon gene count table /home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz (35,337 genes x 6 libraries; recomputed here) and the authors' differential-expression lists GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz and ..._1021_downregulated_genes.txt.gz (searched for each GRIN gene). Reading depth: table (raw counts recomputed to CPM).

## Whole panel table organoid_panel_cpm.tsv (CPM, all 26 rows)
gene | cko1 | cko2 | cko3 | cko4 | cwt1 | cwt2 | raw_min_across_libraries
WWOX 14.12 11.86 16.54 12.28 9.64 10.07 (302); SLC12A2 5.02 5.55 5.49 5.53 5.82 4.65 (139.3); SLC12A5 20.97 19.22 41.33 39.03 19.97 15.64 (469); GRIN1 33.16 37.88 43.71 46.45 40.58 48.83 (1284); GRIN2A 2.56 2.07 5.08 2.40 1.07 0.67 (20); GRIN2B 27.53 45.46 27.43 20.84 26.63 20.25 (607); GRIN2C 2.14 1.41 6.33 2.34 2.25 1.07 (32); GRIN2D 72.54 71.90 114.43 104.51 98.78 88.63 (2657); GRIA1 149.75 162.00 103.28 98.02 90.40 104.81 (3142); GRIA2 12.55 19.73 13.01 12.45 11.46 16.18 (426); GRIA3 18.98 26.44 13.43 17.28 26.84 20.95 (513); GRIA4 0.85 0.75 3.53 1.87 0.78 0.43 (13); GABRB2 2.43 4.01 1.13 3.25 11.33 9.01 (43); GABRB3 16.83 21.95 16.85 18.41 47.99 27.37 (629.7); GAD1 8.93 10.91 37.93 26.98 3.46 0.20 (6); OLIG1 0.10 0.10 0.86 0.73 0.03 0.07 (1); OLIG2 0.65 0.63 1.83 1.64 0.81 1.10 (25); SOX10 0.18 0.05 0.10 0.06 0.11 0.07 (2); PDGFRA 4.70 1.34 2.25 2.16 0.35 0.25 (7.35); MBP 3.05 1.12 3.80 2.25 1.45 1.40 (42); PLP1 68.79 74.50 198.16 87.47 65.47 48.73 (1461); CHRM1 16.86 20.14 8.69 14.30 22.04 24.88 (332); CHRM3 1.41 0.74 2.60 1.49 0.91 0.38 (11.5); HSPA1A 43.88 40.64 62.66 51.35 43.26 64.98 (1612); HSPA8 1455.24 1338.48 1446.28 1353.50 1286.12 1393.56 (41778); SLC12A2_over_SLC12A5 0.24 0.29 0.13 0.14 0.29 0.30.

## Recomputation from the raw count table (counts and CPM, human organoid, KO libraries cko1-4, WT cwt1-2)
library sizes (sum of counts): cko1 38.73M, cko2 41.15M, cko3 38.21M, cko4 34.21M, cwt1 37.26M, cwt2 29.98M

| gene | cko1 | cko2 | cko3 | cko4 | cwt1 | cwt2 | KO mean CPM | WT mean CPM | KO/WT | KO libs above highest WT | KO libs below lowest WT |
|---|---|---|---|---|---|---|---|---|---|---|---|
| GRIN2B (raw counts) | 1066 | 1871 | 1048 | 713 | 992 | 607 | | | | | |
| GRIN2B (CPM) | 27.53 | 45.46 | 27.43 | 20.84 | 26.63 | 20.25 | 30.32 | 23.44 | 1.29 | 3 of 4 | 0 of 4 |
| GRIN2D (raw counts) | 2809 | 2959 | 4372 | 3575 | 3680 | 2657 | | | | | |
| GRIN2D (CPM) | 72.54 | 71.90 | 114.43 | 104.51 | 98.78 | 88.63 | 90.85 | 93.70 | 0.97 | 2 of 4 | 2 of 4 |
| GRIN2A (raw counts) | 98.999 | 85 | 194 | 82 | 40 | 20 | | | | | |
| GRIN2A (CPM) | 2.56 | 2.07 | 5.08 | 2.40 | 1.07 | 0.67 | 3.02 | 0.87 | 3.47 | 4 of 4 | 0 of 4 |
| GRIN3A (raw counts) | 17 | 2 | 71 | 2 | 0 | 2 | | | | | |
| GRIN3A (CPM) | 0.44 | 0.05 | 1.86 | 0.06 | 0.00 | 0.07 | 0.60 | 0.03 | 18.02 | 2 of 4 | 0 of 4 |
| GRIN1 (raw counts) | 1284 | 1559 | 1670 | 1589 | 1512 | 1464 | | | | | |
| GRIN1 (CPM) | 33.16 | 37.88 | 43.71 | 46.45 | 40.58 | 48.83 | 40.30 | 44.71 | 0.90 | 0 of 4 | 2 of 4 |
| GRIA1 (raw counts) | 5799 | 6667 | 3946 | 3353 | 3368 | 3142 | | | | | |
| GRIA1 (CPM) | 149.75 | 162.00 | 103.28 | 98.02 | 90.40 | 104.81 | 128.26 | 97.60 | 1.31 | 2 of 4 | 0 of 4 |

The TSV values reproduce exactly (e.g. GRIN2B cko1 1066 / 38.73 M = 27.53 CPM).
Authors' DE lists (GSE156243, 1,246 up and 1,021 down): GRIN2B, GRIN2D, GRIN1, GRIA1 and GRIN3A do not appear in either list; GRIN2A appears in the up list (log2FC 3.17, padj 0.0159, ENSG00000183454; low count: 20 to 194 counts per library).

## Result
GRIN2D: KO mean 90.85 vs WT 93.70 CPM (ratio 0.97; two KO libraries above the highest WT, two below the lowest): no shift. GRIN2B: KO mean 30.32 vs WT 23.44 (ratio 1.29); 3 of 4 KO libraries are above the higher of the two WT libraries, but cko1 and cko3 exceed it by 0.9 and 0.8 CPM, cko2 (45.46) is an outlier, cko4 (20.84) lies inside the WT pair (20.25 to 26.63); with 2 WT libraries no range test is informative. The authors' lists contain neither gene. "No consistent shift at 4 versus 2 libraries" is a fair description; GRIN2B is the one gene where the group means differ by about a third (stated for the reader; not a printed number in the sentence). No printed arithmetic in the sentence.
