# ADV-295 block 1, records 1 and 2: result after the blind step (SCI, window 8fe7aef9, 2026-11-26; hypothesis level; not medical advice)

PREREG `dc88c85b4f3ab51751c123a0a6f775eb00199cfef1b5c5cb918acd443bb41d6c` (unchanged). First reader: `FIRST_READER_REPORT_REC1_2_ADV295_SCI_20261126.md` (sha256 a79538588058b37a2086cf3b00c81d1c2cf195c401e1a1e561560ede366c2f59). Blind reader: legend-delegate, claude-sonnet-5-5, effort high read back on 17 of 17 turns, one hand-back, given only the matching rule and the packet (sha256 5a6542c3584c1cc3c2e5598eb3f6b779a9211f167d50088466931125299c8414); report verbatim in `BLIND_READER_REPORT_REC1_2_ADV295_SCI_20261126.md` (the longest SubagentHandback input of its transcript; sha256 1bfe7f507989aaf85a6874b534da6ae1bf7777c041b1daece7c041de6f447b44). The blind reader read figures itself; none went into SCI's context.

## Match, sentence by sentence (matching rule of the PREREG, applied as written)

| record | sentence | first reader | blind reader | SCI check on the original | class |
|---|---|---|---|---|---|
| 42807679, CLAIM 032 | "Not examined: the remaining WWOX allele (exome was done in six other patients)" | strict candidate (unsupported as written) | ADD; its own grounds say "other" is not supported but not shown false | Table 3 of the held XML (query on the 13 header cells and the 17 rows, 2026-11-26) has no WES column and no "+" or "-" mark in any row (the legend defines them, no cell uses them); the paper names four of the six (P7, P16, P17, P18) and never says whether P8 was one of the other two | **not strict** (blind did not return MUST CHANGE): one of the two conditions only, listed apart; loose (ADD) |
| 42807679, CLAIM 032 | "and inheritance" (the carrier "de novo") | loose (basis not described) | ADD | Table 3 prints "De novo" for all 17 rows | loose (ADD) |
| 41254692, DL-REPO-003 | "names ... as compounds that *«potentially increase»* WWOX expression" | notes the quotation is not exact, calls it trivial | MUST CHANGE (quotation form only; substance correct) | held XML, queries "potentially increas" (1 hit: "potentially increasing WWOX expression"), "potentially upregulat" (1 hit) and "potentially increase" (0 hits), 2026-11-26T03:39Z: a quoted phrase is not in the source | **strict by the rule; form-only, the substance (five compounds named as raising WWOX) is right** |
| 41254692, DL-REPO-003 | "cell type, dose, species and readout (transcript or protein) are unknown" | low-priority candidate: the sheet states Homo sapiens; the ledger may mean the primaries | MUST CHANGE (Table S7 Organism = Homo sapiens in all 11 rows; line 3786 of the same record says "in *Homo sapiens*") | workbook Table S7 column D, rows 3 to 13, all "Homo sapiens"; the sentence names no antecedent, the same record states the species two lines above | **strict by the rule, low weight: the defect is an unreferenced "species unknown" against a stated species** |
| 41254692, DL-REPO-003 | "A curated database says valproate LOWERS WWOX expression in human cells" | not a candidate | ADD (the sheet gives organism only, no cell or tissue type) | Table S7 row 6 | loose (ADD) |

All other statements of both records (19 and 21 judged) were NO CHANGE, UNSETTLED (R1-S14 "dozens of genes", R2-S19 "cancer and toxicology experiments": no held gene annotation, primaries not held) or out of scope; the FDR 0.160, the five WWOX and six THBS2 rows, the valproic-acid PMIDs and the hg18 interval (13,172,590 bp) reproduce.

## Counts after records 1 and 2 (records, not sentences)

* **Strict records: 1 of 2** (41254692, two sentences; both low in substance, listed so ADV can weigh them). 42807679: strict 0; one candidate listed apart (exome sentence: first reader strict, blind ADD).
* **Loose records: 2 of 2** (strict or ADD). ADD sentences: CLAIM 032 "de novo" basis and the exome sentence; DL-REPO-003 "human cells".
* Prediction of the PREREG (strict 2 of the first five, range 0 to 3): not decided; records 3 to 5 follow. Stop rule: 0 strict in block 1 would stop block 2; this block already has 1 strict record.

## Replacement sentences (for IT, after block 1 closes; nothing is sent yet)

* DL-REPO-003: "*«potentially increasing»*" in place of "*«potentially increase»*" (Results; the Discussion adds that vorinostat and valproic acid "can simultaneously upregulate WWOX expression"); "cell type, dose and readout (transcript or protein) are not given in the deposited sheet; the species is Homo sapiens in every row" in place of "cell type, dose, species and readout (transcript or protein) are unknown"; "in Homo sapiens (cell or tissue type not given)" in place of "in human cells".
* CLAIM 032: "Exome sequencing was done in six selected patients, four named (P7, P16, P17, P18) and two not; whether the carrier was one of them is not stated" in place of "(exome was done in six other patients)"; "Table 3 lists the deletion as de novo (the Inheritance column reads De novo in all 17 rows; parental testing for this patient is not described)" for the inheritance clause.

## Limits

Figures 1 and 2 of 42807679 are not held (class not completable); no gene coordinates are held, so the boundary genes of the P8 interval stay unchecked; the primaries behind the CTD rows are not held.
