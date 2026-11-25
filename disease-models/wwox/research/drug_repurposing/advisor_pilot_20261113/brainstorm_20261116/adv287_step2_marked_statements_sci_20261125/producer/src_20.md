# src_20 (card K01_hif_axis_glycolytic_shift, /p4_fields/functional_evidence_available)

## Verbatim sentence (marked word: "every" in "changes every region")
the other three mutants are within the wild-type range), so that leaving out M6 changes every region.

Immediate context in the same item (verbatim): "and the Adm increase in the three forebrain regions is a two-animal effect (M6 and F8; the other three mutants are within the wild-type range), so that leaving out M6 changes every region. The glycolytic-enzyme shift in cortex is not an M6 artefact (+0.21, p 0.008 to 0.016), but the control set of six hides a split (Pgk1, Aldoa, Pfkp, Pkm, Eno1 up; Ndrg1 down about 0.4 to 0.5 log2)."
Preceding clause in the same item (verbatim): "the six-gene selective set changes by +0.22 (hippocampus; +0.17 under a second normalisation), +0.11 (cortex), -0.07 (PFC) and +0.19 (cerebellum) log2 (exact permutation p 0.32, 0.70, 0.67, 0.057); Bhlhe40 and Ndrg1 fall, Ddit4 and Ankrd37 are flat, and the Adm increase in the three forebrain regions is a two-animal effect".

## Source pointers
- Card packet: disease-models/wwox/research/drug_repurposing/cards/K01_hif_axis_glycolytic_shift.packet.json, /p4_fields/functional_evidence_available.
- Dataset: GEO GSE215425 (mouse brain bulk RNA-seq, Wwox P47T/P47T knock-in versus WT/WT; integer count table), held file files/deepening_downloads/gse215425/GSE215425_processed_data.csv.gz (tab-separated, 55010 genes by 37 libraries; read-only) with files/deepening_downloads/gse215425/GSE215425_series_matrix.txt.gz (sample titles and regions). Animals: WT M1, M2, M3, F4, F5; P47T M6, M7, F8, F9, F10 (cerebellum: WT M2, M3, F4, F5; P47T M6, F8, F10). Regions: HPC hippocampus, CTX parietal cortex (series-matrix region "Parietal cortex"), PFC prefrontal cortex, CB cerebellum. Unit: one animal per library; mouse.
- Repository analysis of the same counts: disease-models/wwox/research/drug_repurposing/p47t_it12_20261031/ (README.md; results/genes_it12.tsv, leave_one_animal_out_it12.tsv, set_scores_per_animal_it12.tsv, sets_it12.tsv; script p47t_reanalysis_it12.py: TMM normalisation per region, logCPM = log2((count + pc) / (effective library + 2 pc) x 1e6) with pc = 2 x effective library / mean effective library). The six-gene selective set HIF_SEL_UP6 = Adm, Bhlhe40, P4ha1, Ankrd37, Ddit4, Egln3 (sets_it12.tsv).
- ADV-233 folder with the same counts and the two-animal discussion: disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv233_p47t_two_animals_sci_20261125/ (RESULT file section 0 states that IT12 identified M6 and F8 as animals with Nptx2 and Bdnf 20 to 30 fold above wild type in the three forebrain regions).

## Table 1. Adm (gene symbol Adm, Ensembl ENSMUSG00000030790; the 8028th data row of the count file) in every library, recomputed from the held counts with the IT12 formulas (TMM per region over all libraries of that region; no library omitted)
| region | sample (GEO title suffix) | genotype | sex | Adm raw count | library size (sum of all counts) | TMM factor | Adm CPM (count / (library x TMM) x 1e6) | Adm logCPM (prior 2, IT12 formula) |
|---|---|---|---|---|---|---|---|---|
| HPC | WT/WT_M3 | WT/WT | M | 97 | 46319108 | 0.967 | 2.17 | 1.146 |
| HPC | WT/WT_M2 | WT/WT | M | 67 | 43720754 | 1.006 | 1.52 | 0.651 |
| HPC | WT/WT_M1 | WT/WT | M | 66 | 47615941 | 0.979 | 1.42 | 0.548 |
| HPC | WT/WT_F5 | WT/WT | F | 87 | 44611440 | 1.062 | 1.84 | 0.913 |
| HPC | WT/WT_F4 | WT/WT | F | 63 | 42848548 | 1.000 | 1.47 | 0.601 |
| HPC | P47T/P47T_M7 | P47T/P47T | M | 111 | 49019390 | 1.021 | 2.22 | 1.178 |
| HPC | P47T/P47T_M6 | P47T/P47T | M | 539 | 46287051 | 0.972 | 11.97 | 3.587 |
| HPC | P47T/P47T_F9 | P47T/P47T | F | 45 | 33046111 | 1.028 | 1.32 | 0.455 |
| HPC | P47T/P47T_F8 | P47T/P47T | F | 148 | 38049092 | 0.963 | 4.04 | 2.031 |
| HPC | P47T/P47T_F10 | P47T/P47T | F | 101 | 38914793 | 1.006 | 2.58 | 1.393 |
| CTX | WT/WT_M3 | WT/WT | M | 120 | 38297292 | 0.982 | 3.19 | 1.695 |
| CTX | WT/WT_M2 | WT/WT | M | 70 | 43699804 | 0.987 | 1.62 | 0.740 |
| CTX | WT/WT_M1 | WT/WT | M | 116 | 40729656 | 0.995 | 2.86 | 1.540 |
| CTX | WT/WT_F5 | WT/WT | F | 54 | 45280189 | 1.017 | 1.17 | 0.286 |
| CTX | WT/WT_F4 | WT/WT | F | 123 | 48342820 | 1.035 | 2.46 | 1.325 |
| CTX | P47T/P47T_M7 | P47T/P47T | M | 157 | 46668496 | 1.019 | 3.30 | 1.743 |
| CTX | P47T/P47T_M6 | P47T/P47T | M | 720 | 38376996 | 0.971 | 19.31 | 4.275 |
| CTX | P47T/P47T_F9 | P47T/P47T | F | 111 | 40415302 | 1.016 | 2.70 | 1.459 |
| CTX | P47T/P47T_F8 | P47T/P47T | F | 277 | 43465950 | 0.984 | 6.48 | 2.705 |
| CTX | P47T/P47T_F10 | P47T/P47T | F | 103 | 40688100 | 0.995 | 2.54 | 1.374 |
| PFC | WT/WT_M3 | WT/WT | M | 137 | 39910669 | 1.023 | 3.36 | 1.769 |
| PFC | WT/WT_M2 | WT/WT | M | 79 | 40274726 | 0.988 | 1.99 | 1.026 |
| PFC | WT/WT_M1 | WT/WT | M | 96 | 38187795 | 1.012 | 2.48 | 1.342 |
| PFC | WT/WT_F5 | WT/WT | F | 68 | 34236539 | 1.036 | 1.92 | 0.976 |
| PFC | WT/WT_F4 | WT/WT | F | 85 | 39100362 | 1.015 | 2.14 | 1.133 |
| PFC | P47T/P47T_M7 | P47T/P47T | M | 85 | 39822647 | 1.030 | 2.07 | 1.085 |
| PFC | P47T/P47T_M6 | P47T/P47T | M | 455 | 43343067 | 0.924 | 11.36 | 3.512 |
| PFC | P47T/P47T_F9 | P47T/P47T | F | 84 | 40621528 | 1.013 | 2.04 | 1.065 |
| PFC | P47T/P47T_F8 | P47T/P47T | F | 289 | 38246803 | 0.987 | 7.66 | 2.946 |
| PFC | P47T/P47T_F10 | P47T/P47T | F | 140 | 45324561 | 0.978 | 3.16 | 1.682 |
| CB | WT/WT_M3 | WT/WT | M | 50 | 49068231 | 0.979 | 1.04 | 0.127 |
| CB | WT/WT_M2 | WT/WT | M | 44 | 39248864 | 0.998 | 1.12 | 0.231 |
| CB | WT/WT_F5 | WT/WT | F | 35 | 37696857 | 1.004 | 0.92 | -0.035 |
| CB | WT/WT_F4 | WT/WT | F | 54 | 39637001 | 0.998 | 1.37 | 0.502 |
| CB | P47T/P47T_M6 | P47T/P47T | M | 47 | 32649942 | 1.017 | 1.41 | 0.551 |
| CB | P47T/P47T_F8 | P47T/P47T | F | 62 | 40004894 | 1.007 | 1.54 | 0.669 |
| CB | P47T/P47T_F10 | P47T/P47T | F | 51 | 37813899 | 0.998 | 1.35 | 0.488 |

## Table 2. IT12 per-gene rows for Adm (results/genes_it12.tsv, verbatim; header then four rows)
```
region	gene	set	ensembl	kept_by_expression_filter	meanCPM_WT	meanCPM_P47T	log2FC_P47T_over_WT	welch_t	welch_p	BH_q_region_wide	exact_perm_p	log2FC_sex_adjusted	p_sex_adjusted	raw_counts_WT / P47T
HPC	Adm	HIF_SEL_UP6	ENSMUSG00000030790.15	1	1.68	4.43	0.957	1.77	0.145	0.5	0.087	1.069	0.0934	97|67|66|87|63 / 111|539|45|148|101
CTX	Adm	HIF_SEL_UP6	ENSMUSG00000030790.15	1	2.26	6.87	1.194	1.97	0.0979	0.435	0.079	1.362	0.0508	120|70|116|54|123 / 157|720|111|277|103
PFC	Adm	HIF_SEL_UP6	ENSMUSG00000030790.15	1	2.38	5.26	0.809	1.56	0.184	0.412	0.214	0.882	0.153	137|79|96|68|85 / 85|455|84|289|140
CB	Adm	HIF_SEL_UP6	ENSMUSG00000030790.15	1	1.11	1.44	0.363	2.91	0.0413	0.19	0.086	0.356	0.0873	50|44|35|54 / 47|62|51
```

## Table 3. IT12 README Table B Adm row and the sentence on the hippocampal signal (README.md, verbatim)
- Row: | Adm | +0.96 / +1.19 / +0.81 / +0.36 | +2.60 | +0.54, +0.71*, -0.45, -0.63* (mixed) |
- Row 1 text: | Is the organoid's selective hypoxia-response pattern present in P47T? | **No.** Of the organoid-up non-IT7 genes only Adm is higher in all four regions (+0.4 to +1.2 log2, 1.7-2.4 CPM, p 0.04-0.18). Bhlhe40 and Ndrg1 fall (-0.2 to -0.8), Ddit4, Ankrd37 flat, Egln3 mixed. Set HIF_SEL_UP6: HPC +0.22, CTX +0.11, PFC -0.07, CB +0.19 (exact p 0.32, 0.70, 0.67, 0.057); selectivity contrast not met anywhere. The one organoid-like hippocampal signal is carried by one animal (drop P47T M6: +0.05). |

## Table 4. IT12 leave-one-animal-out table, whole file (results/leave_one_animal_out_it12.tsv, verbatim)
```
region	set	full_diff	min_diff_after_drop	dropped_for_min	max_diff_after_drop	dropped_for_max
HPC	HIF_SEL_UP6	0.218	0.046	drop M6(P47T)	0.311	drop F9(P47T)
HPC	HIF_FLAT6	0.121	0.091	drop M6(P47T)	0.156	drop F9(P47T)
HPC	NRF2_5	0.326	0.266	drop M6(P47T)	0.396	drop F5(WT)
HPC	ACTIVITY_IEG	0.685	0.114	drop F8(P47T)	1.045	drop F9(P47T)
HPC	ASTRO	0.593	0.429	drop M6(P47T)	0.782	drop F5(WT)
CTX	HIF_SEL_UP6	0.108	-0.068	drop M6(P47T)	0.216	drop F9(P47T)
CTX	HIF_FLAT6	0.248	0.206	drop M6(P47T)	0.272	drop M1(WT)
CTX	NRF2_5	0.190	0.089	drop M6(P47T)	0.246	drop F10(P47T)
CTX	ACTIVITY_IEG	0.224	-0.158	drop F8(P47T)	0.564	drop M7(P47T)
CTX	ASTRO	0.087	-0.023	drop M6(P47T)	0.154	drop F5(WT)
PFC	HIF_SEL_UP6	-0.068	-0.157	drop F8(P47T)	0.016	drop F9(P47T)
PFC	HIF_FLAT6	0.119	0.087	drop F8(P47T)	0.150	drop M7(P47T)
PFC	NRF2_5	0.189	0.153	drop M6(P47T)	0.228	drop F5(WT)
PFC	ACTIVITY_IEG	0.256	-0.170	drop F8(P47T)	0.603	drop F9(P47T)
PFC	ASTRO	0.226	0.156	drop M3(WT)	0.389	drop F5(WT)
CB	HIF_SEL_UP6	0.187	0.157	drop M2(WT)	0.226	drop F4(WT)
CB	HIF_FLAT6	0.043	-0.044	drop M6(P47T)	0.097	drop F10(P47T)
CB	NRF2_5	0.172	0.142	drop M6(P47T)	0.202	drop F10(P47T)
CB	ACTIVITY_IEG	-0.243	-0.484	drop F5(WT)	0.009	drop M2(WT)
CB	ASTRO	0.164	0.126	drop M3(WT)	0.216	drop M2(WT)
```

## Table 5. Six-gene set HIF_SEL_UP6, per-animal set scores (results/set_scores_per_animal_it12.tsv, all rows for this set; score = mean over set genes of logCPM minus the region mean) and set statistics (results/sets_it12.tsv rows for this set)
```
region	set	animal	genotype	score_log2_centered
HPC	HIF_SEL_UP6	M3	WT	0.0889
HPC	HIF_SEL_UP6	M2	WT	-0.1481
HPC	HIF_SEL_UP6	M1	WT	-0.0394
HPC	HIF_SEL_UP6	F5	WT	-0.2536
HPC	HIF_SEL_UP6	F4	WT	-0.1916
HPC	HIF_SEL_UP6	M7	P47T	-0.0552
HPC	HIF_SEL_UP6	M6	P47T	0.7929
HPC	HIF_SEL_UP6	F9	P47T	-0.2652
HPC	HIF_SEL_UP6	F8	P47T	0.1153
HPC	HIF_SEL_UP6	F10	P47T	-0.0440
CTX	HIF_SEL_UP6	M3	WT	0.1009
CTX	HIF_SEL_UP6	M2	WT	-0.0839
CTX	HIF_SEL_UP6	M1	WT	0.1069
CTX	HIF_SEL_UP6	F5	WT	-0.3816
CTX	HIF_SEL_UP6	F4	WT	-0.0123
CTX	HIF_SEL_UP6	M7	P47T	-0.1934
CTX	HIF_SEL_UP6	M6	P47T	0.7591
CTX	HIF_SEL_UP6	F9	P47T	-0.3776
CTX	HIF_SEL_UP6	F8	P47T	0.2507
CTX	HIF_SEL_UP6	F10	P47T	-0.1687
PFC	HIF_SEL_UP6	M3	WT	0.2183
PFC	HIF_SEL_UP6	M2	WT	0.0007
PFC	HIF_SEL_UP6	M1	WT	0.0809
PFC	HIF_SEL_UP6	F5	WT	-0.1899
PFC	HIF_SEL_UP6	F4	WT	0.0592
PFC	HIF_SEL_UP6	M7	P47T	-0.2474
PFC	HIF_SEL_UP6	M6	P47T	0.2465
PFC	HIF_SEL_UP6	F9	P47T	-0.3686
PFC	HIF_SEL_UP6	F8	P47T	0.3239
PFC	HIF_SEL_UP6	F10	P47T	-0.1234
CB	HIF_SEL_UP6	M3	WT	-0.0219
CB	HIF_SEL_UP6	M2	WT	-0.1721
CB	HIF_SEL_UP6	F5	WT	-0.1635
CB	HIF_SEL_UP6	F4	WT	0.0365
CB	HIF_SEL_UP6	M6	P47T	0.1331
CB	HIF_SEL_UP6	F8	P47T	0.0607
CB	HIF_SEL_UP6	F10	P47T	0.1273
```
```
region	set	n_declared	n_used	genes_used	mean_log2FC_P47T_minus_WT	welch_t	welch_p	exact_perm_p	n_splits	sex_adj_diff	sex_adj_p	genes_up	genes_down
HPC	HIF_SEL_UP6	6	6	Adm,Bhlhe40,P4ha1,Ankrd37,Ddit4,Egln3	0.218	1.14	0.308	0.317	252	0.280	0.148	4	2
CTX	HIF_SEL_UP6	6	6	Adm,Bhlhe40,P4ha1,Ankrd37,Ddit4,Egln3	0.108	0.48	0.647	0.698	252	0.170	0.451	2	4
PFC	HIF_SEL_UP6	6	6	Adm,Bhlhe40,P4ha1,Ankrd37,Ddit4,Egln3	-0.068	-0.45	0.672	0.667	252	-0.046	0.784	2	4
CB	HIF_SEL_UP6	6	6	Adm,Bhlhe40,P4ha1,Ankrd37,Ddit4,Egln3	0.187	3.29	0.0294	0.057	35	0.187	0.0631	6	0
```
