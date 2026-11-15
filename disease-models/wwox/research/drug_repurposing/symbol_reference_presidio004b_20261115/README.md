# PRESIDIO-004 part B: independent reference mapping of the 15 blank-log2fc rows (2026-11-15)

Written for: the ADV presidio, the IT Orchestrator and HE, who compare it with HE's offline trial of the IT23 symbol lookup.

**Status of this folder: built and committed BEFORE HE's trial output was seen.** At the time of building, `main` held no HE trial folder for this assignment (checked by listing `disease-models/wwox/research/drug_repurposing/` only; no HE file was opened). The commit that adds this folder carries the time. Nothing here was adapted afterwards; the comparison is in `comparison_with_he_trial.md`, written after, if HE's output exists on `main`.

## Answer first

All 15 rows resolve, each to exactly one authors' row, with no unresolved and no ambiguous conversion on the route used (`mapping_reference.tsv`, status `RESOLVED_UNIQUE` for 15 of 15).

* **Route used (primary):** current symbol in `composition_class.tsv` -> HGNC approved record (`hgnc_complete_set_20261022.json`, one record per symbol) -> `ensembl_gene_id` -> the `ensg` column of the authors' two lists (GSE156243 `1246_upregulated`, `1021_downregulated`). Each ENSG occurs in exactly one authors' row (2267 rows, 2267 distinct ENSG, no ENSG in both lists) and in exactly one HGNC record.
* **Route checked (second, independent):** the authors' symbol is in the HGNC `prev_symbol` of the same record for all 15, each such previous symbol belongs to one HGNC gene only, and the HGNC `entrez_id` equals the authors' `EntrezID` for all 15.
* **Direction:** the sign of the authors' `log2FoldChange` equals the `ko_direction` already in `composition_class.tsv` for all 15 (7 up, 8 down), and equals the list the row sits in.
* **log2FC where present:** present for all 15 in the authors' lists (values in the table; for example IRAG1 = MRVI1 +2.21, CCN2 = CTGF +1.32, H4C15 = HIST2H4B -0.93). The blank `log2fc` in `composition_class.tsv` is therefore a failed lookup, not an absent value.
* **Ambiguity:** none on the symbol or ENSG route. Two rows have an HGNC **alias** shared by several genes (CIRSR: alias `CIR`, 3 genes; ZNRD2: alias `p27`, 4 genes). The alias route is not used and would be ambiguous; a lookup that fell back on aliases for these two would need to refuse them. The previous-symbol route is not ambiguous for any of the 15.

| query symbol | authors' symbol | ENSG | list | log2FC |
|---|---|---|---|---|
| IRAG1 | MRVI1 | ENSG00000072952 | up | 2.21 |
| CCN2 | CTGF | ENSG00000118523 | up | 1.32 |
| DRC4 | GAS8 | ENSG00000141013 | up | 1.03 |
| MNMIP1 | SH3D21 | ENSG00000214193 | up | 1.00 |
| POFUT4 | FUT11 | ENSG00000196968 | up | 0.62 |
| MTCL2 | SOGA1 | ENSG00000149639 | up | 0.60 |
| ATOSB | FAM214B | ENSG00000005238 | up | 0.49 |
| HDIP1 | C16orf87 | ENSG00000155330 | down | -0.76 |
| BBLN | C9orf16 | ENSG00000171159 | down | -0.47 |
| ADPRS | ADPRHL2 | ENSG00000116863 | down | -0.53 |
| CIRSR | CIR1 | ENSG00000138433 | down | -0.66 |
| H1-2 | HIST1H1C | ENSG00000187837 | down | -0.56 |
| H1-10 | H1FX | ENSG00000184897 | down | -0.55 |
| H4C15 | HIST2H4B | ENSG00000270276 | down | -0.93 |
| ZNRD2 | SSSCA1 | ENSG00000173465 | down | -0.55 |

## What this does not say

* It does not say what a regeneration would change in rho, flags or QD/QF membership: those columns need the time-course data and the rho computation, which are outside this part. For CCN2 ADV-007 found the flags unchanged (rho -0.009); the other 14 are not computed here.
* The padj values are in `mapping_reference.tsv`; all are below 0.01 in the authors' lists (they were already selected as differential). No claim on effect size or biology.
* It was built with a small script (`build_reference_mapping.py`) after I had looked the 15 rows up one by one in the two source files; the script re-expresses that reading and adds the cross-checks. It is not the IT23 lookup and shares no code with `gse156243/validate_symbols.py`.
* Not a verifier of HE's output; a comparator. A disagreement is reported as a disagreement, not resolved by choosing a side.

## Files

`mapping_reference.tsv` (15 rows, 18 columns), `input_digests.tsv` (SHA-256 of the HGNC file, both authors' lists and `composition_class.tsv`), `build_reference_mapping.py` (`python3 -I build_reference_mapping.py <files/geo/GSE156243> <composition_class.tsv> <out_dir>`; offline, read-only).

Zero spend; no external request; no committed file edited.
