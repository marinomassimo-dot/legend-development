# PRODUCER_NOTE — ADV-287 step 1 (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. No web fetch, no PubMed, no acquisition, no contact, no spend; Obeid 2026 (PMID 42422765), RP-045, ADV-174 and ADV-175 not touched. No classifier refusal occurred. Held data only.

## Addendum (coordinator message): replacement for n=7
n=21 (route1 reserve, draw_order 15, P11 DR-P11-004, DQ/SQ p 0.09) assessed from the held Yadav 2022 full-text XML: CORRECT (0.055 and 0.114 reproduce for 26 and 22; the printed 0.09 is reproduced by no size read from the paper). Total with n=21: CORRECT 10, INCOMPLETE 7, WRONG 0, NOT ASSESSABLE 4 (n=7 stays in the table as the Obeid stop). Upper bounds of the stated ranges (0.075, 0.128) name no sizes and need sizes not in the paper, so are not checkable size by size.

## Class counts (20 sampled statements)
CORRECT 9 (n=4, 5, 6, 8, 9, 10, 12, 13, 17); INCOMPLETE 7 (n=1, 2, 3, 14, 15, 16, 20); WRONG 0; NOT ASSESSABLE 4 (n=7, 11, 18, 19). Of the 16 assessable, 7 (44 percent) are INCOMPLETE; none is WRONG. The error class that recurs is the one HE found in the sheets: a comparator row or cohort left out of a range or count (n=1 centres, n=2 applied levels and class members, n=3 exposed denominators, n=15 the 75-case cohort, n=16 the below-clinical-exposure comparator).

## Could not access
* n=7: only source is Obeid 2026; classifier stop, nothing opened.
* n=11 (omaveloxolone): label JSON of 2026-04-06 and Reisman 2019 (PMC6475100) not held; only the 97 percent binding is quoted in a held table.
* n=19 (anakinra): abstracts of Hanin 2024 (38430119) and Giussani 2025 (40614647) not held; only the repository's secondary table. Likely INCOMPLETE on the denominator of "73 percent" (52 on anakinra vs 75 total; tocilizumab 70 percent omitted), but unconfirmed.
* n=18: a proposed design, no quantity; not a source statement.
* Not held but assessed at lower depth: n=8 (Tollner 2015 abstract bytes), n=10 (PMC4027860 bytes absent after a SHA-256 search; verbatim abstract IC50s only), n=5/6/20 (abstracts only), n=15 (2025 Neurology article via manifest only).

## Surprises
* n=1: the "three centres" claim sits beside seven centres in the same batch's own table and held full texts; the endpoints 22.1 and 44.7 survive.
* n=3: "the one cohort reporting its exposed denominator" is not true: Beijing (533), UCLA 2024 (108), Toronto (95) also give one.
* n=15: the repository's own repair record (M9) already says the 75-case Oliver 2023 pool exceeds the 50-person Neurology cohort; the card insertion kept the superlative.
* n=17: the audit sentence matches all 12 recomputed minima; the check passed because it was done as a minimum over every row, not on the quoted row.

## Borderline calls for the verifier
n=14 and n=16 (INCOMPLETE; a reader could keep CORRECT, n=16 is the most contestable); n=3 (could be read as WRONG, a count); n=12 (CORRECT, GRIN2B mean ratio 1.29 with two WT libraries); n=10 (3.25 rounded to "about threefold"); n=8 (abstract bytes not held); n=20 (INCOMPLETE rests on identifying the label's N=205 study with PMID 19054414).

## Files
STEP1_TABLE_ADV287.tsv (20 rows, 13 columns, no tab or newline in a cell) and src_01.md to src_20.md (src_07 is the stop note only). Helper scripts were kept outside the folder in /tmp.
