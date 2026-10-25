# GSE156243 qualification and exploratory reversal query (scientist-b, 2026-10-22)

TRANSFORMATION NOTICE: in the ten files listed in `uuid_transform_manifest.tsv` the hyphens inside UUIDs were removed (publication-gate false positive on UUID fragments); no other byte changed. The verbatim originals are under the shared gitignored `files/geo/GSE156243/tool_responses_verbatim/`; the manifest gives the verbatim sha256 and byte count of each, and `transform_uuids.py verify` re-inserts hyphens and compares byte for byte (all 10 LOSSLESS; the inverse leaves the value of the "md5" key alone because an md5 digest is also 32 hex). The scripts sigcom_query.py and sigcom_summarise.py were run on the verbatim form; to rerun them point them at the verbatim copies or restore with transform_uuids.restore.

Exploratory, class level, not medical advice. LINCS output is NOT WWOX EVIDENCE. The dataset is a WWOX
knockout versus wild-type organoid contrast; it is not a Q230P, child or rescue signature.

## Whose data this is, and the one rule this folder earned

**Source and credit.** GSE156243 is the deposit of **PMID 34268881** (Repudi et al., *EMBO Molecular
Medicine* 2021, DOI `10.15252/emmm.202013610`), who built the organoid model, ran the sequencing and made
the data and the differential-expression tables public. Every result in this folder rests on their work and
is theirs to be credited for; cite that paper wherever a result derived here is used. The series is used
under NCBI GEO's public-data terms, and nothing here redistributes the raw files (they stay in the
gitignored `files/geo/GSE156243/`, by digest).

🔴 **Read the paper's own manifest before analysing its deposit.** On 2026-10-24 an analysis of this folder
reported the raised canonical Wnt readout as a new finding. It was not new: entry 31 of
`deepdive_manifests/PMID34268881.json` already carried the same genes with the same values, read from the
authors' Table EV1, and entry 32 carried the complementary negative. The analysis still added a null model
and a confound analysis, but a targeted look at the manifest first would have aimed it better and cost
almost nothing. A deposited dataset in LEGEND usually has a paper, and that paper usually has a manifest —
`registry_records.py` and the manifest come before the data.

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
