# src_01 — H02 DR-H02-005 note: "three independent centres put the rate among imaged children between 22.1 and 44.7 percent (one at partial full-text depth, the others at abstract level)"

Card: H02_gabaat_inactivator_myelin_exposure, packet /drug_assertions/4/note (DR-H02-005, label row). Species for every row: human children with infantile or epileptic spasms, vigabatrin; NOT WWOX evidence.
Pointer in the sentence: "Batch ORCH-SCIBATCH-DR-20261105 (B1)". Held source table: disease-models/wwox/research/drug_repurposing/batch_sci_20261105/b1_whitematter/evidence_b1.tsv (48 rows, whole file read), README.md, verify/review_B/review_B.md; primaries held under /home/desktop/legend-development/files/fulltext/ (PMID36601084 PMC XML = full text read; PMID39570186 Sathe PMC XML = full text; PMID39641935 Stevering PMC XML = full text; abstracts as Europe PMC core JSON in files/fulltext/adv056_it_20261118/B/ for 20384718, 40527948, 42735667, 19054414, 28230253, 18783433, 19258289, 36601084). Reading depth for this file: table (evidence_b1.tsv) + full-text read of 36601084, 39570186, 39641935 + abstracts of the rest.

## A. Every row of evidence_b1.tsv that carries a human exposed-cohort rate (all 48 rows were read; rows B1-02..03, 05..07, 09..10, 14, 17..34, 37..38, 42..48 carry no rate of this kind)

| B1 row | PMID | centre (from abstract affiliation or review_B) | numerator / denominator as printed | percent (printed or recomputed) | denominator type | depth in B1 |
|---|---|---|---|---|---|---|
| B1-01 | 36601084 | PLA General Hospital, Beijing | 38 / 172 | 22.1 (38/172 = 22.09) | children kept after exclusions (see C) | partial full text |
| B1-13 | 34786694 | same department as B1-01 (review_B correction 1) | 25 / 77 | 32.5 (25/77 = 32.47) | enrolled children | abstract |
| B1-11 | 42735667 | Emory, Atlanta | 18 / 64 | 28.1 (18/64 = 28.125) | children with >=2 MRI before and during | abstract |
| B1-08 | 40527948 | King Fahad Specialist Hospital, Dammam | 34 / 76 | 44.7 (34/76 = 44.74) | children imaged during exposure (76 = 57.6 percent of treated cohort) | abstract |
| B1-41 | 20384718 | Hospital for Sick Children, Toronto | 25 / 81 | 30.9 (25/81 = 30.86) | children imaged during but not before exposure | abstract |
| B1-40 | 18783433 | Children's National Medical Center, Washington DC | 7 / 22 (8 / 23 with the index case) | 31.8 (7/22); 34.8 (8/23) | children with an MRI during therapy | abstract |
| B1-36 | 39570186 | UCLA (same division and senior author as B1-12; review_B) | 17 / 108 treated; 17 / 56 imaged during treatment (from the full text: "56 patients who had at least one MRI conducted during vigabatrin treatment") | 15.7 per treated child; 30.4 per imaged child | both denominators in the full text | full text (held manifest in B1; XML re-read here) |
| B1-12 | 28230253 | UCLA (same division) | 6 / 40 asymptomatic imaged children (abstract); 4 symptomatic among 104 with exposure data; 45 of 104 imaged | 15.0 (6/40, subset); 22.2 (10/45) only if the 4 symptomatic are inside the 45 (not stated in the abstract) | subset | abstract |
| B1-35 | 39641935 | Dutch TSC Registry / EPISTOP | 27 / 76 | 35.5 (27/76 = 35.53) | VGB-treated TSC children with MRI during VGB | full text (XML held) |
| B1-39 | 19054414 | 10 sites, US and Canada | prevalence 22 percent vigabatrin-treated vs 4 percent naive infants; arm sizes not in the abstract | 22 vs 4 | prevalence population | abstract |
| B1-16 | 35180571 | not in table | 44 with the finding among 288 seen with West syndrome | 15.3 (44/288) but denominator is all West syndrome children, not exposed imaged | not comparable | abstract |

Rows with no unexposed or exposed-denominator rate (case series): B1-16 (see above), B1-19, B1-20.

## B. Statement 1, recomputed
* Range of the four rates the sentence rests on (B1-01, B1-11, B1-08, and B1-13 from the same centre as B1-01): 22.1 to 44.7: confirmed (38/172, 18/64, 34/76; 25/77 = 32.5 lies inside).
* Count of independent centres in the table with a rate among children imaged during exposure: Beijing (B1-01 and B1-13, one centre), Emory, Dammam, Toronto (B1-41; review_B calls PMID 20384718 "a fourth independent rate"), Washington DC (B1-40), UCLA (B1-36/B1-12, one centre), Dutch registry (B1-35). That is seven centres, not three. B1's own README Decision 1 cites rows B1-01, B1-08, B1-11, B1-13, B1-35, B1-39 and counts three; row B1-41 (labelled "a fourth independent rate" by the verifier and in RESPONSE.md) is omitted from the count, and so are B1-36 and B1-40.
* Range after adding the omitted imaged-child rates: 22.1 (Beijing) to 44.7 (Dammam) stays the min-max for rows with a clean imaged denominator (30.9, 31.8, 30.4, 35.5, 28.1 all inside). Only UCLA 2017 (B1-12) lies lower: 6/40 = 15.0 percent (asymptomatic subset only) up to 22.2 percent (10/45) if the symptomatic cases are all in the 45.
* "(one at partial full-text depth, the others at abstract level)": Beijing = partial full text; Emory and Dammam abstract: consistent for the three the sentence names. In the whole table, three further imaged-child rates are read at full text (39570186 UCLA, 39641935 Dutch registry, and 36601084 itself), so "the others at abstract level" holds only for the three named.

## C. Denominator check on the 22.1 percent (held full text, PMID 36601084, Results paragraph, XML /home/desktop/legend-development/files/fulltext/PMID36601084_ADV272_PMC9806385_epmc_20261125.xml)
"A total of 533 children with IS who had VGB exposure were screened. Of these, 390 underwent cerebral MRI before VGB exposure and during follow-up. Among these 390 children, 18 with VGB exposure for less than 30 days, 193 with VGB exposure for more than 1 year during cerebral MRI review, and 7 without MRI review before the initiation of rapamycin were excluded ... Ultimately, 172 children were included ... and 38 (22.1%) developed VABAM."
Arithmetic: 533 - 390 = 143 (no MRI: this is the "143" of B1-01); 390 - 18 - 193 - 7 = 172 (checks). So the 172 denominator is NOT "all imaged children": 390 were imaged, and 218 imaged children were removed (193 of them for exposure longer than one year). Per exposed child the same cohort gives 38/533 = 7.1 percent (lower bound: the 193 long-exposure children are not scored); per imaged child 38/390 = 9.7 percent (same caveat). B1-01's breaker lists only the 143.
