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

## Added at the presidio's request: the other 819 rows, and how independent the reference really is

**Outside the 15, nothing contradicts my reading.** I ran my route (query symbol -> HGNC approved record -> `ensembl_gene_id` -> the authors' row by ENSG) over all 834 rows of `composition_class.tsv` and compared with HE's `symbol_mapping_834.tsv`: 819 `same_symbol` and 15 `converted_two_routes_agree`, and for all 834 the authors' symbol and ENSG equal HE's, the authors' list (up or down) equals `ko_direction`, and where the committed table has a `log2fc` (819 rows) it equals the authors' value exactly. The symbol-equality route and the ENSG route give the same gene for every row where both exist (0 differ). The five rows HE names for ignored alias hits (MAGEA2B, GPNMB, CELSR1, CACNA1A, TGFBRAP1) resolve by ENSG to the row carrying the same symbol, as HE kept them. Scope: this is a mechanical re-derivation on the same files, not a new reading of 819 rows.

**The independence of the reference was weaker than it looks, and I say so plainly.**
* **Shared:** the HGNC release (`hgnc_complete_set_20261022.json`), the authors' data (GEO lists; HE's derived list is built from them) and the committed `composition_class.tsv`. My primary route (HGNC `ensembl_gene_id`) is the same as HE's route B, so on that route the two are one method written twice, and an error in the HGNC file's ENSG assignment for any of the 15 would be shared. HE's route A (previous symbol) matches my second check.
* **Independent of HGNC, so real checks on the 15:** (1) the authors' own `EntrezID` column equals HGNC `entrez_id` for all 15, and the ENSG is the authors' own; (2) the authors' `description` column, which is their annotation and not HGNC's, names the same gene under its older name for all 15 (for example IRAG1: "murine retrovirus integration site 1 homolog", i.e. MRVI1; CCN2: "connective tissue growth factor"; ZNRD2: "Sjogren syndrome/scleroderma autoantigen 1", i.e. SSSCA1). I read the 15 descriptions against the HGNC names by eye; no third database (NCBI gene history, Ensembl archive) was consulted, since the lookup was offline.
* **What the comparison therefore shows:** separately written code and a hand reading give the same result on the same inputs, and the inputs are internally consistent. It does not show that HGNC is right.
