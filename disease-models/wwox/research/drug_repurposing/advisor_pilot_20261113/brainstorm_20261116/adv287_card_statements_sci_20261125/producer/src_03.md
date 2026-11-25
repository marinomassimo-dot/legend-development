# src_03 — H02 DR-H02-005 note: "the one cohort reporting its exposed denominator gives about 26 percent per exposed child"

Card: H02, /drug_assertions/4/note. Same source set as src_01 (evidence_b1.tsv whole table, README, review_B; primaries in /home/desktop/legend-development/files/fulltext/). Human infants/children, vigabatrin, NOT WWOX. Reading depth: table + full text (36601084, 39570186, 39641935) + abstracts (40527948, 28230253, 42735667).

## Where "about 26 percent" comes from
B1-08 / PMID 40527948 (Dammam, abstract): "Seventy-six patients (57.6%) underwent MRI during vigabatrin therapy. Thirty-four out of the 76 patients (44.7%) had VABAM."
Recompute: exposed cohort = 76 / 0.576 = 131.9 = about 132 (76/132 = 57.58 percent). 34/132 = 25.76 percent = about 26 percent. Arithmetic is right.

## Every cohort in the held table or its full texts that states how many treated children there were
| cohort | PMID | exposed (treated) denominator stated | imaged | with finding | per exposed child | per imaged child | source place |
|---|---|---|---|---|---|---|---|
| Dammam | 40527948 | about 132 (76 = 57.6 percent of the cohort) | 76 | 34 | 25.8 percent | 44.7 | abstract |
| Beijing | 36601084 | 533 children with VGB exposure screened | 390 MRI before and during; 172 analysed after exclusions | 38 | 7.1 percent (38/533; undercount: 193 imaged children with more than 1 year exposure not scored) | 22.1 (of 172); 9.7 (of 390) | full text, Results (held XML) |
| UCLA 2024 | 39570186 | 108 children with detailed vigabatrin exposure data | 56 with at least one MRI during treatment | 17 (11 symptomatic) | 15.7 percent (17/108) | 30.4 (17/56) | full text, abstract and Methods/Results (held XML) |
| UCLA 2017 | 28230253 | 143 documented VGB-treated; 104 with exposure data | 45 | 6 asymptomatic among 40 imaged asymptomatic; 4 symptomatic among 104 | 10/143 = 7.0 percent or 10/104 = 9.6 percent (derived, assuming the 4 symptomatic are among the 45) | 15.0 (6/40) to 22.2 (10/45) | abstract |
| Dutch registry | 39641935 | 80 VGB-treated TSC | 76 (after exclusions) | 27 | 27/80 = 33.8 percent (derived; the paper states 27/76 = 35.5) | 35.5 | full text (held XML) |
| Emory | 42735667 | not stated in abstract | 64 | 18 | not computable | 28.1 | abstract |
| Beijing sister report | 34786694 | not stated | 77 | 25 | not computable | 32.5 | abstract |
| Toronto | 20384718 | 95 treated of 107 | 81 | 25 | 25/95 = 26.3 percent (derived from the abstract: "95 treated"; 81 scanned during-not-before) | 30.9 | abstract |

## Recomputation
* "The one cohort": the whole table holds four cohorts whose full text or abstract states the treated pool (Dammam, Beijing, UCLA 2024, UCLA 2017) and two more where it can be read off (Dutch registry, Toronto 95 treated). Per-exposed-child values run from 7.0 (UCLA 2017, derived) / 7.1 (Beijing) / 15.7 (UCLA 2024) to 25.8 (Dammam) / 26.3 (Toronto, derived); 26 is the top of the spread, not a single reporting cohort's value among peers.
* The sentence is silent on the Beijing full text, which is the cohort B1 itself read at partial full text (B1-01), and which reports its exposed pool of 533.
* B1's own caveat (B1-01 breaker): "143 exposed children without MRI were excluded"; recompute 533 - 390 = 143 (confirmed); but then 193 + 18 + 7 further imaged children were excluded (src_01 section C).
