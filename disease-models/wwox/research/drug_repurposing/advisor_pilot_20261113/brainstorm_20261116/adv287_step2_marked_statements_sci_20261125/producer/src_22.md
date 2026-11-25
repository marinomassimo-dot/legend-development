# src_22 (card L01_nrf2_axis, /p4_fields/functional_evidence_available)

## Verbatim sentence (marked words: "at least" and "every")
IT12 P2-P47T datum (no change of selection or priority): in the deposited P47T brain the NRF2 target transcripts Hmox1 and Srxn1 are modestly higher in all four regions (+0.3 to +0.7 log2), Nqo1 is mixed, Gclm and Txnrd1 flat [IT 2026-11-25, ADV-239: Srxn1 keeps at least 70 percent of its rise without any one animal in every region;

## Source pointers
- Card packet: disease-models/wwox/research/drug_repurposing/cards/L01_nrf2_axis.packet.json, /p4_fields/functional_evidence_available.
- Dataset: GEO GSE215425 (mouse brain bulk RNA-seq; Wwox P47T/P47T versus WT/WT; one animal per library; regions HPC hippocampus, CTX parietal cortex, PFC prefrontal cortex, CB cerebellum; HPC, CTX, PFC 5 WT versus 5 P47T, CB 4 WT versus 3 P47T). Held counts files/deepening_downloads/gse215425/GSE215425_processed_data.csv.gz (not reopened for this statement; the rows below are the repository's own tables computed from it).
- Repository tables: disease-models/wwox/research/drug_repurposing/p47t_it12_20261031/results/genes_it12.tsv and sets_it12.tsv (IT12; normalisation TMM per region, logCPM with prior 2; log2FC = mean P47T minus mean WT of per-animal logCPM); disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv239_influence_audit_sci_20261125/out/influence_adv239.tsv and unit_values_adv239.tsv (ADV-239 influence audit; unit values are per-animal values on the scale named in the scale column).
- The set NRF2_5 of IT12 (sets_it12.tsv) is Hmox1, Nqo1, Srxn1, Gclm, Txnrd1.

## Table 1. IT12 per-gene rows (results/genes_it12.tsv, verbatim, all four regions for each of the five genes; the last column is raw counts WT (5 or 4 values) / P47T (5 or 3 values))
```
region	gene	set	ensembl	kept_by_expression_filter	meanCPM_WT	meanCPM_P47T	log2FC_P47T_over_WT	welch_t	welch_p	BH_q_region_wide	exact_perm_p	log2FC_sex_adjusted	p_sex_adjusted	raw_counts_WT / P47T
HPC	Hmox1	NRF2_5	ENSMUSG00000005413.8	1	7.20	12.55	0.710	2.39	0.0555	0.447	0.024	0.781	0.0333	297|300|322|469|246 / 588|1055|350|333|320
CTX	Hmox1	NRF2_5	ENSMUSG00000005413.8	1	5.58	8.74	0.512	1.73	0.152	0.516	0.024	0.601	0.067	226|268|226|249|235 / 293|657|287|287|251
PFC	Hmox1	NRF2_5	ENSMUSG00000005413.8	1	6.07	7.79	0.343	2.22	0.062	0.247	0.040	0.371	0.0545	215|250|248|254|207 / 289|432|273|290|301
CB	Hmox1	NRF2_5	ENSMUSG00000005413.8	1	4.15	5.10	0.297	2.31	0.0732	0.231	0.029	0.301	0.111	165|176|165|170 / 191|185|187
HPC	Srxn1	NRF2_5	ENSMUSG00000032802.8	1	98.71	134.74	0.417	2.17	0.0741	0.461	0.063	0.402	0.0945	4701|4193|3706|5365|4306 / 4875|8251|4004|5974|4388
CTX	Srxn1	NRF2_5	ENSMUSG00000032802.8	1	113.42	168.98	0.543	2.84	0.0295	0.28	0.016	0.567	0.0271	4472|4463|4268|6421|5004 / 6856|9350|5348|7600|5750
PFC	Srxn1	NRF2_5	ENSMUSG00000032802.8	1	111.26	157.24	0.476	3.19	0.0233	0.156	0.016	0.471	0.0231	4573|4183|4012|4526|4272 / 5067|8293|5431|6754|6415
CB	Srxn1	NRF2_5	ENSMUSG00000032802.8	1	117.49	145.52	0.307	4.92	0.0156	0.161	0.029	0.309	0.0088	5430|4742|4311|4822 / 4935|6170|5086
HPC	Nqo1	NRF2_5	ENSMUSG00000003849.8	1	6.32	7.86	0.349	1.57	0.163	0.512	0.135	0.303	0.223	234|259|243|484|217 / 471|274|259|259|356
CTX	Nqo1	NRF2_5	ENSMUSG00000003849.8	1	6.43	5.77	-0.156	-0.98	0.358	0.717	0.349	-0.091	0.486	284|270|306|264|254 / 283|254|228|269|172
PFC	Nqo1	NRF2_5	ENSMUSG00000003849.8	1	5.14	5.09	-0.014	-0.09	0.933	0.968	0.960	-0.005	0.98	240|166|184|225|180 / 269|186|199|197|185
CB	Nqo1	NRF2_5	ENSMUSG00000003849.8	1	11.53	15.64	0.425	2.07	0.127	0.295	0.086	0.473	0.0418	497|544|428|418 / 651|585|483
HPC	Gclm	NRF2_5	ENSMUSG00000028124.15	1	40.84	41.98	0.039	0.65	0.536	0.771	0.571	0.038	0.586	1671|1908|2015|1843|1773 / 2116|1789|1409|1452|1831
CTX	Gclm	NRF2_5	ENSMUSG00000028124.15	1	46.34	44.65	-0.051	-0.77	0.465	0.79	0.437	-0.052	0.498	1887|1905|1793|2352|2105 / 2123|1666|1759|2088|1712
PFC	Gclm	NRF2_5	ENSMUSG00000028124.15	1	43.42	45.73	0.070	0.94	0.385	0.607	0.349	0.102	0.0908	1725|1813|1760|1491|1653 / 2078|1999|1633|1595|2046
CB	Gclm	NRF2_5	ENSMUSG00000028124.15	1	85.31	81.06	-0.074	-0.80	0.471	0.626	0.543	-0.083	0.455	4566|3126|3124|3315 / 2422|3473|3171
HPC	Txnrd1	NRF2_5	ENSMUSG00000020250.10	1	73.23	79.44	0.116	2.38	0.0494	0.439	0.056	0.124	0.0456	3181|3122|3628|3552|3056 / 3864|3914|2528|3012|2992
CTX	Txnrd1	NRF2_5	ENSMUSG00000020250.10	1	67.43	72.37	0.103	2.46	0.0444	0.32	0.032	0.115	0.0235	2452|3008|2944|3049|3170 / 3478|2722|3117|2990|2829
PFC	Txnrd1	NRF2_5	ENSMUSG00000020250.10	1	64.89	68.32	0.071	1.20	0.277	0.512	0.246	0.061	0.359	2720|2654|2376|2378|2481 / 2939|2364|2967|2651|3040
CB	Txnrd1	NRF2_5	ENSMUSG00000020250.10	1	82.05	76.81	-0.096	-1.51	0.223	0.396	0.171	-0.099	0.212	4172|3210|2964|3206 / 2359|3235|2984
```

## Table 2. IT12 set row NRF2_5 (results/sets_it12.tsv, verbatim)
```
region	set	n_declared	n_used	genes_used	mean_log2FC_P47T_minus_WT	welch_t	welch_p	exact_perm_p	n_splits	sex_adj_diff	sex_adj_p	genes_up	genes_down
HPC	NRF2_5	5	5	Nqo1,Hmox1,Gclm,Srxn1,Txnrd1	0.326	3.46	0.00887	0.024	252	0.329	0.0149	5	0
CTX	NRF2_5	5	5	Nqo1,Hmox1,Gclm,Srxn1,Txnrd1	0.190	1.59	0.166	0.135	252	0.228	0.0748	3	2
PFC	NRF2_5	5	5	Nqo1,Hmox1,Gclm,Srxn1,Txnrd1	0.189	2.91	0.0201	0.032	252	0.200	0.0218	4	1
CB	NRF2_5	5	5	Nqo1,Hmox1,Gclm,Srxn1,Txnrd1	0.172	4.03	0.0173	0.029	35	0.180	0.0096	3	2
```

## Table 3. ADV-239 influence table rows for the five genes (out/influence_adv239.tsv, verbatim; leave-one-animal-out over all units of the contrast, controls and mutants; ratio = leave-one-out effect divided by the effect with all animals; columns as stored)
```
deposit	contrast	item	n_control	n_mutant	scale	effect_all	min_effect_leave_one_out	max_effect_leave_one_out	min_ratio_leave_one_out	unit_at_min	sign_flips	threshold_crossings	separation	first_read
GSE215425	HPC	gene:Hmox1	5	5	log2CPM difference	0.710	0.458	0.836	0.644	M6			overlap	robust
GSE215425	HPC	gene:Srxn1	5	5	log2CPM difference	0.417	0.296	0.524	0.709	M6			overlap	robust
GSE215425	HPC	gene:Nqo1	5	5	log2CPM difference	0.349	0.280	0.535	0.802	M7			overlap	robust
GSE215425	CTX	gene:Hmox1	5	5	log2CPM difference	0.512	0.226	0.604	0.441	M6			overlap	one-animal-driven
GSE215425	CTX	gene:Srxn1	5	5	log2CPM difference	0.543	0.390	0.627	0.718	M6			overlap	robust
GSE215425	CTX	gene:Nqo1	5	5	log2CPM difference	-0.156	-0.237	-0.051	0.329	F10			overlap	one-animal-driven
GSE215425	PFC	gene:Hmox1	5	5	log2CPM difference	0.343	0.220	0.405	0.642	M6			overlap	robust
GSE215425	PFC	gene:Srxn1	5	5	log2CPM difference	0.476	0.369	0.556	0.777	M6			overlap	robust
GSE215425	PFC	gene:Nqo1	5	5	log2CPM difference	-0.014	-0.109	0.066	-4.906	F5	M3;F5;M6;F9;F10		overlap	one-animal-driven
GSE215425	CB	gene:Hmox1	4	3	log2CPM difference	0.297	0.208	0.368	0.701	M6			all mutant above all control	robust
GSE215425	CB	gene:Srxn1	4	3	log2CPM difference	0.307	0.269	0.361	0.876	F8			all mutant above all control	robust
GSE215425	CB	gene:Nqo1	4	3	log2CPM difference	0.425	0.251	0.557	0.591	M6			overlap	robust
```

## Table 4. ADV-239 per-animal unit values for Srxn1 (out/unit_values_adv239.tsv, verbatim, all rows for gene:Srxn1; scale log2CPM, one animal per row, mouse)
```
deposit	contrast	item	unit	arm	value
GSE215425	HPC	gene:Srxn1	M3	control	6.7144
GSE215425	HPC	gene:Srxn1	M2	control	6.5756
GSE215425	HPC	gene:Srxn1	M1	control	6.3136
GSE215425	HPC	gene:Srxn1	F5	control	6.8243
GSE215425	HPC	gene:Srxn1	F4	control	6.6519
GSE215425	HPC	gene:Srxn1	M7	mutant	6.6060
GSE215425	HPC	gene:Srxn1	M6	mutant	7.5185
GSE215425	HPC	gene:Srxn1	F9	mutant	6.8812
GSE215425	HPC	gene:Srxn1	F8	mutant	7.3501
GSE215425	HPC	gene:Srxn1	F10	mutant	6.8089
GSE215425	CTX	gene:Srxn1	M3	control	6.8943
GSE215425	CTX	gene:Srxn1	M2	control	6.6940
GSE215425	CTX	gene:Srxn1	M1	control	6.7187
GSE215425	CTX	gene:Srxn1	F5	control	7.1237
GSE215425	CTX	gene:Srxn1	F4	control	6.6448
GSE215425	CTX	gene:Srxn1	M7	mutant	7.1719
GSE215425	CTX	gene:Srxn1	M6	mutant	7.9706
GSE215425	CTX	gene:Srxn1	F9	mutant	7.0253
GSE215425	CTX	gene:Srxn1	F8	mutant	7.4735
GSE215425	CTX	gene:Srxn1	F10	mutant	7.1509
GSE215425	PFC	gene:Srxn1	M3	control	6.8087
GSE215425	PFC	gene:Srxn1	M2	control	6.7172
GSE215425	PFC	gene:Srxn1	M1	control	6.6987
GSE215425	PFC	gene:Srxn1	F5	control	6.9959
GSE215425	PFC	gene:Srxn1	F4	control	6.7511
GSE215425	PFC	gene:Srxn1	M7	mutant	6.9490
GSE215425	PFC	gene:Srxn1	M6	mutant	7.6941
GSE215425	PFC	gene:Srxn1	F9	mutant	7.0452
GSE215425	PFC	gene:Srxn1	F8	mutant	7.4837
GSE215425	PFC	gene:Srxn1	F10	mutant	7.1773
GSE215425	CB	gene:Srxn1	M3	control	6.8220
GSE215425	CB	gene:Srxn1	M2	control	6.9198
GSE215425	CB	gene:Srxn1	F5	control	6.8327
GSE215425	CB	gene:Srxn1	F4	control	6.9303
GSE215425	CB	gene:Srxn1	M6	mutant	7.2153
GSE215425	CB	gene:Srxn1	F8	mutant	7.2599
GSE215425	CB	gene:Srxn1	F10	mutant	7.0752
```

## ADV-239 PREREG (verbatim; defines the first-read labels and the thresholds used in Table 3)
# ADV-239 pre-registration: influence audit of carried small-n bulk-RNA inferences (SCI; hypothesis level; not medical advice)

Frozen at 2026-11-25T01:24:57Z, before any per-unit score or leave-out value was computed in this window. Effort high, no delegate, no spend, no external request except reading held files.

## What I had read before writing this (not blind)
* The brief, checkpoint AD sections 2, 3 and 7, and therefore the ADV-233 conclusions (P47T animals M6 and F8 carry the forebrain TNFA, IL6/JAK/STAT3 and HYPOXIA enrichments; GLYCOLYSIS survives; cerebellar cholesterol, fatty acid and mTORC1 are above every wild type).
* The opening of the IT12 README (its tables A and B, including group means and exact permutation p), the head of HELD_RESULTS_BY_GENE_derived.md, and statement snippets in investigations.tsv, the candidate cards and the claim registry.
* PMID 30290271 Results 3.5 and the Figure 6 legend (RNA-seq on neurospheres 2 KO v 3 WT; qRT-PCR on whole hippocampus 4 v 4). The "Aldaz/Kv7 sets" of the brief are this set: the matching trigger T19 carries it; Kcna2 is Kv1.2, not Kv7.

## Definitions
* **Inference**: a statement of direction, magnitude or enrichment about a gene, gene set or pathway, from a bulk transcript measurement (count or TPM table, or qRT-PCR reported with a bulk set) with **1 to 5 units in at least one arm** (unit = animal, organoid library or pool), that at least one consumer carries.
* **Consumer**: one research_portfolio row, one investigations.tsv row, one candidate card, one claim, one working-model or disease_model line, or one matching trigger. A consumer counts once per inference. Generated renderings, translations, shareable copies and result notes of the analysis itself are not consumers.
* **Counted** only after the hit is opened and read: a consumer that names the deposit without using the inference does not count.
* **Primary tier**: WWOX-deficient systems. **Secondary tier**: non-WWOX comparator deposits that a portfolio or investigation row uses with a direction; listed with animals and leave-out history, influence not computed in this task (cost cap, stated as a gap).

## Influence rule (applied to held per-unit tables only)
* Comparator and normalisation: those of the carried analysis where it states them (IT12 for GSE215425 sets; the folder's own script elsewhere); where only per-gene values are carried, log2 CPM or log2(TPM+1) as stated per row in the result table. Raw integer counts are normalised before scoring.
* Unit score: for a set, the mean over set genes of log2 expression centred per gene within the contrast; for a gene, its log2 value. Effect E = mean(mutant) minus mean(control).
* **Leave-one-out**: every unit of both arms is removed in turn (this includes the most extreme animal). Reported: smallest E_without / E, and whether any sign flips.
* **one-animal-driven**: some single removal flips the sign of E, or leaves less than 0.50 of E, or moves the statement across the threshold its source declared.
* **two-animal-driven**: P47T only, where ADV-233 already tested the flagged pair M6 and F8: the same rule with both removed. No other pair is searched (stated limit).
* **robust**: an arm of at least 3 on both sides and neither rule met. "Robust" means only that no single unit (and, for P47T, not the flagged pair) carries the effect; it does not mean the effect is significant, replicated, cell-resolved or causal.
* **not testable**: an arm with fewer than 3 units, a pooled library, or no per-unit value held. Where per-unit values exist with an arm of 2, report whether the two arms separate completely (descriptive, no disposition from it).
* A carried statement of "no change" or "flat" is not rescued by this rule: leave-one-out is reported, disposition "not testable for absence" if |E| < 0.20 log2.

## Ranking
Inferences ordered by the number of distinct consumers that lean on them (counted as above); ties by how many of those consumers are decisions about a compound or experiment.

## Predictions (recorded now)
* P1: among testable inferences from arms of 3 to 5, at least two thirds are robust to leave-one-out.
* P2: at least one carried inference outside the P47T hallmark sets is one-animal-driven.
* P3: no GSE156243 organoid inference is testable, because its control arm has 2 libraries.
* P4: the top-ranked inference (most consumers) comes from GSE156243, so the head of the ranking is "not testable" rather than "one-animal-driven".
* P5: the T19 set (PMID 30290271) is not testable (no per-animal value held).

## Rejecting observations
If every testable inference is robust and no consumer wording overstates its units, the audit's disposition is "no correction needed", stated as such. Stop at 120 minutes in two increments; anything not computed is listed as not computed.
