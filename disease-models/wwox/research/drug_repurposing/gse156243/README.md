# GSE156243 qualification and exploratory reversal query (scientist-b, 2026-10-22)

Exploratory, class level, not medical advice. LINCS output is NOT WWOX EVIDENCE. The dataset is a WWOX
knockout versus wild-type organoid contrast; it is not a Q230P, child or rescue signature.

Order of work (the order matters): `qualify.py` -> `validate_symbols.py` -> `marker_sets_declared.tsv` and
`thresholds_and_query_declaration.md` (committed first, b2daa702) -> `build_sets.py` -> `sigcom_map_entities.py`
-> `sigcom_query.py` (S1, S2, S3, S0) -> `sigcom_summarise.py` -> `kg_lookup/` (kg_thin_slice.py).

- `derived/` : qualification.json, the padj<=0.01, padj<=0.05 and p-value-only lists, symbol validation with ENSG,
  marker annotation, the four declared query sets, the entity map, the reverser summary.
- `tool_responses/` : the ORIGINAL service responses and request/metadata records. `FORMAT_ATTEMPT1_*` is a
  response to a first request that used gene symbols where the service needs entity identifiers; it returned zero
  results and is kept, not hidden.
- `kg_lookup/` : kg_thin_slice.py output for WWOX, GRIN2A, HTR2C (INCOMPLETE states preserved), raw pages beside it.
- The three original files, the soft file and the vocabulary snapshot are in the shared `files/geo/GSE156243/` (gitignored); digests in the note.
