# src_15 — B01 not_known[2]: "About 57 percent of classifiable individuals in the largest genotype-classified cohort are null/null (56.8 percent in the abstract of the 2025 Neurology cohort of 50 individuals from 45 families, PMID 40875931, confirmed by PubMed abstract on 2026-10-21;"

Card: B01_amlexanox, /not_known[2]. Species: human, biallelic WWOX variants, WWOX-DEE. Pointer: PMID 40875931 (Neurology 2025, DOI 10.1212/WNL.0000000000213883); registry route: disease-models/wwox/research/deepdive_manifests/PMID40875931.json (receipt FTR-20260804-40875931-02; 20 verbatim locators, all read) and disease-models/wwox/analysis/woree_therapeutic_class_census_20260921.md (where the sentence "In the largest genotype-classified cohort ... 25 of 44 classifiable individuals (56.8 %) are null/null" originates).
Held: the manifest of 40875931 (locators quote its abstract, Results and Table 2); the article itself and its abstract file are NOT held (files/fulltext has no 40875931; census text says its artefact is gone with the container); for the comparator, the full text of Oliver 2023 (PMID 36779245) IS held: /home/desktop/legend-development/files/fulltext/PMID36779245_Oliver2023_PMC_r2.xml (and ..._2026-09-27.xml), plus registries/paper_registry_current.md PAPER 018 and registries/claim_registry_current.md CLAIM 033. Reading depth: manifest verbatim locators (abstract and body snippets) + full text of the comparator paper.

## The 2025 cohort (PMID 40875931), from manifest locators 5, 9, 19, 1
| quantity | value | unit | where |
|---|---|---|---|
| individuals with biallelic WWOX variants | 50 | people | abstract: "50 individuals with biallelic WWOX variants across 45 families, identifying 25 variants that have not been previously reported" |
| families | 45 | families | abstract |
| included in the genotype-phenotype analysis | 44 | people | Methods: "Forty-four of the 50 cases were included ... Six cases were excluded where we could not confidently predict the effect of the variant as null." |
| null/null (N/N) | 25 | people | Results: "Over half (n = 25, 56.8%) displayed the N/N variant genotype" |
| null/missense (N/M) | 13 (29.5%) | people | same |
| missense/missense (M/M) | 6 (13.6%) | people | same |
| abstract percent | "Individuals classified with a null/null genotype (56.8%) ... null/missense (29.5%) ... missense/missense (13.6%)" | | abstract |
Recompute: 25/44 = 56.8 percent (25 + 13 + 6 = 44). The sentence's "about 57 percent" and "56.8 percent" agree; "classifiable individuals" = 44 of 50; matches.

## Comparator genotype-classified set held in the same registry (Oliver 2023, PMID 36779245, Epilepsia)
Verbatim (held full text, Results): "We stratified all 75 cases into one of three genetic groups: (1) null/null (n = 45), (2) null/missense (n = 15), (3) missense/missense (n = 15)." Recompute: 45 + 15 + 15 = 75; null/null = 45/75 = 60.0 percent. These 75 are 13 new patients (12 families, 5 centres) plus 62 literature cases (CLAIM 033: "I 75 casi sono 45 null/null, 15 null/missense, 15 missense/missense"; "non sommare mai queste coorti fra loro").
The repository's own repair record (commit candidate CC-20260928-MIRROR003-REPAIRS-01, item M9): "PAPER 018 (PMID 36779245) pools 75 (13 + 62, per CLAIM 033); PMID 40875931 has 50"; and the PAPER 117 Role field: "as cohorts both PMID 40875931 (50 individuals / 45 families) and PAPER 018 (75 pooled ...) are larger"; the earlier unqualified "largest WOREE cohort" was repaired as "false against two records this registry already holds".
The same sentence, with the same superlative, sits in disease-models/wwox/analysis/woree_therapeutic_class_census_20260921.md line 33 ("In the largest genotype-classified cohort, 63 of 88 classified alleles (71.6 %) are predicted null and 25 of 44 classifiable individuals (56.8 %) are null/null"); 63/88 = 71.6 percent (recomputed).

## Recomputation
56.8 percent (25 of 44) is right for the 2025 cohort. "Largest genotype-classified cohort": the 75 individuals genotype-classified in Oliver 2023 (held) are more than the 44 classified in the 2025 cohort; their null/null share is 45/75 = 60.0 percent (not 56.8). The two sets overlap in an unknown way (the 2025 paper's overlap with literature sets is "unexcludable" in analysis/ft116_cohort_triage_20260921.md), so they are not to be summed; but the superlative and the single figure leave out the second classified set that the registry already holds. The sentence's own scoping ("classifiable individuals", "abstract of the 2025 Neurology cohort") is accurate; the word "largest" is the affected span.
