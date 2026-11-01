# IT15 P5: ToolUniverse v1.5.7 -> v1.5.8 delta and scouting for activity-level resources (2026-11-01)

Scientist package P5, task IT15. Non-canonical research material, not medical advice. Nothing here is WWOX evidence. A resource listed here shows availability, not value; no result was validated.

## (a) ToolUniverse v1.5.8
Primary source: GitHub release bodies via the public API (`raw/rel.json`, SHA-256 in `raw_sha256.txt`), v1.5.8 published 2026-11-01T05:03:22Z, v1.5.7 2026-10-13. Delta in `tooluniverse_delta.tsv`.
- No change names ChEMBL, GtoPdb, IUPHAR, BindingDB, PubChem, UniChem, DrugCentral or Open Targets (string search of both bodies: 0 hits).
- Only indirectly relevant: PR 824 adds completeness metadata (`returned`, `total_results`, `has_more`, `truncated`) to about 300 tools. It addresses the silent truncation seen on 2026-10-26 (100 asked, 50 returned) but maps to none of gaps 1-3.
- Tool code read without executing (tag v1.5.8, copies in `raw/`): ChEMBL tools are a REST wrapper of the same EBI API (so the same 5xx); the activity field projection offers only activity_id, molecule, target, assay, standard type/value/units, pchembl, standard_relation, standard_flag, which is narrower than `framework/adapters/chembl.py` (it already keeps data_validity_comment, potential_duplicate, assay organism/cell/tissue, confidence, parent). GtoPdb tools read the same bulk CSVs the module already uses (affinity high/median/low, units, action, selectivity; no PMIDs or assay context). UniChem tools wrap the UniChem REST API.
- **Decision: no new question, no trial run.** Repeating a query because a release exists was explicitly excluded. Package licence Apache-2.0; wrapped services keep their own terms and tools return no licence text.

## (b) Gap answers
1. **ChEMBL outage.** One probe of `status.json` at 2026-11-01 07:37Z returned HTTP 500 (`raw/chembl_status.json`), so the problem persists. A licence-clean offline route exists: ChEMBL 37 dumps (SQLite 5.4 GB gz, PostgreSQL 1.9 GB, MySQL 2.0 GB, h5 314 MB; dated 2026-05-29; checksums in `raw/chembl_checksums.txt`), CC BY-SA 3.0. Not downloaded: no question demanded it.
2. **Fields for quantitative comparison.** The schema documentation (`raw/chembl_schema.txt`) lists standard_relation, data_validity_comment, potential_duplicate, activity_comment, assays (organism, strain, tissue, cell type, confidence_score, relationship_type, variant_id), target_components, variant_sequences. The adapter already retains the activity- and assay-level ones. What the adapter does not fetch and the dump holds in one join: target components/gene symbols per subunit and mutant-variant sequences. This matches the IT14 proposal (gene symbols per target). GtoPdb, DrugCentral, BindingDB, ToolUniverse add no assay-level fields beyond ChEMBL (IT14 comparison).
3. **Identity joins.** ChEMBL molecule_hierarchy (parent/salt) and `chembl_37_chemreps` (InChIKey) cover parent-metabolite-salt inside ChEMBL; UniChem bulk mappings would extend across resources but no licence sentence was found.

## (c) Decisions
See `decisions.tsv` (6 rows). Summary: ChEMBL offline dump WATCH (strongest, conditional on need); Papyrus DISCARD for now (aggregates per pair, ChEMBL 34, complex handling unverified); UniChem bulk WATCH; ToolUniverse KEEP as optional isolated tool, no re-run; DTA-GNN WATCH (method reference for leakage audits); SIMPATHIC / rd-explainer DISCARD.

## Not verified
VGSC-DB (cadd.zju.edu.cn) unreachable (HTTP 502), not assessed; Chemical Probes Portal licence not found; PR 824 file list read only to the first 100 files; Papyrus handling of heteromeric complexes; unpacked size of the ChEMBL SQLite; UniChem and EMBL-EBI terms; web-search summaries for rare-disease methods were not checked against the papers.

Files: README.md, decisions.tsv, tooluniverse_delta.tsv, licences.tsv, raw/ (copies), raw_sha256.txt. Two scratch files outside the package (release JSON etc.) are duplicated in raw/.
