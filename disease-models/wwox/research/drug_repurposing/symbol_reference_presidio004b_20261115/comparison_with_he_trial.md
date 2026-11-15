# PRESIDIO-004 part B: comparison with HE's trial output (2026-11-15)

Written for: the ADV presidio, the IT Orchestrator (disposition) and HE. Compared after my reference was committed (`cc39da185`, 2026-11-15T07:33:43Z) and after HE's folder reached `development/main` (`e16c42b70`, `it23_symbol_lookup_trial_he_20261115/`). I first opened HE's files after that message; neither side was adapted.

## Answer first

**15 of 15 rows agree on every field compared; there is no disagreement.** Fields: the authors' symbol, the ENSG, the direction (sign of the authors' `log2FoldChange`, and equal to `ko_direction` in `composition_class.tsv`) and the log2FC, row by row in `comparison_rows.tsv` (`agree_all` True for 15). HE's status is `converted_two_routes_agree` for the 15 (previous-symbol route and ENSG route), 0 unresolved, 0 ambiguous; mine is `RESOLVED_UNIQUE` for the 15.

| Item | SCI reference (`mapping_reference.tsv`) | HE trial (`output/symbol_mapping_834.tsv`, `before_after_converted_rows.tsv`) | Agree |
|---|---|---|---|
| Authors' symbol, 15 rows | MRVI1, CTGF, GAS8, SH3D21, FUT11, SOGA1, FAM214B, C16orf87, C9orf16, ADPRHL2, CIR1, HIST1H1C, H1FX, HIST2H4B, SSSCA1 | same 15 | 15/15 |
| ENSG | by HGNC `ensembl_gene_id` | by the authors' row and HGNC record, two routes | 15/15 |
| Direction | 7 up, 8 down, equal to `ko_direction` | the same, `direction_agrees` 1 for 15 | 15/15 |
| log2FC | 2.21, 1.32, 1.03, 1.00, 0.62, 0.60, 0.49, -0.76, -0.47, -0.53, -0.66, -0.56, -0.55, -0.93, -0.55 | the same (`log2fc_after`) | 15/15 |
| Ambiguity | none on the ENSG or previous-symbol route; two alias-only ambiguities noted (CIRSR alias CIR, ZNRD2 alias p27), not used | none among the 15; the only ambiguity HE reports is five other rows (`same_symbol`) whose aliases are rows of the list, outside the 15 | no conflict (different scope) |

## Differences that are not disagreements

* **Different authors' file.** I read the two GEO lists in `files/geo/GSE156243` (`..._1246_upregulated`, `..._1021_downregulated`); HE read `gse156243/derived/list_padj_le_0.05.tsv`. The 15 rows are identical in both, which is a small confirmation that the derived list carries these genes unchanged. It is not independent of the GEO files (the derived list comes from them).
* **Different route logic.** Mine is HGNC `ensembl_gene_id` first, previous-symbol second; HE's is previous-symbol/alias first (as in `validate_symbols.py`), ENSG second. Both end on the same row for all 15, so for these rows the route order does not matter.
* **HE went further than part B and I did not check it.** HE computed rho against log10 day, the composition and broad flags, L1000 membership and the changed query membership (QF_minus_broad_maturation: IRAG1, POFUT4, HDIP1, H1-2, H1-10 leave the set). I computed none of that. Only one of those numbers is independently held: CCN2 rho -0.009, which my ADV-007 analysis also found (flags unchanged), so that single value agrees. The other 14 rho values, the broad-class flips and the query-membership change are HE's, unverified here.
* **HE's 819 `same_symbol` rows and the five alias-hit rows** are outside the 15 and outside what I mapped.

## What this says and does not say

* Says: for the 15 rows, the lookup of the authors' symbol, the ENSG, the direction and the log2FC is reproducible by two separately written routes and one independent hand reading, with no ambiguity on the used routes. The disposition rule (KEEP for a conversion whose classification and provenance can be verified) is IT's.
* Does not say: that the downstream rho, flags or query changes are right (not checked here beyond CCN2); that any ranking changes (HE claims none; none measured); anything about the 819 other rows.
* A caution on independence: both of us used the same HGNC release file (`hgnc_complete_set_20261022.json`) and the same authors' data, so an error in either input would be shared. The two readings compare my route against HE's, not a third source.

Files: `comparison_rows.tsv` (15 rows, 13 columns; HE columns copied from its commit `e16c42b70`).
