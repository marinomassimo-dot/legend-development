# BATCH COMMIT REPORT — BATCH_20261019_001

> Metabolic batch 2026-10-19, wave 1 (groups G1 to G4). Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**

## Summary

- Type: MANUAL (the backlog threshold of 5 was also met). Pre-flight LINT: `BLOCK_BATCH_COMMIT` (23 `ORPHAN_COMPLETE_READ` plus 2 `OUTPUT_STUDY_MISMATCH`), all discharged by this batch. Post-propagation LINT: `WARN`, 0 BLOCK.
- WM version: `WM_v7.20` -> `WM_v7.21` (MINOR; one bump per batch).
- Commit candidates: 12 in scope, **12 PROPAGATED**, 0 superseded, 0 deferred, 0 merged. Conflicts encountered: 0.
- Snapshot: `backup/20261019_batch001`; pre-batch commit `d956ded77c509202acf0dd203a1e09ad5f6be60e`. No restore was needed.
- Commits: `99a9f400` (propagation + surfaces), `0284b383` (WM bump, manifest, scope, growth anchors), `32d0fd05` (candidate dispositions), plus the commit carrying this report.
- No claim was created or reversed; no `Status`, `Type` or `Summary` changed anywhere. `FULL_FALLBACK`: none — every op list was accepted by the record-scoped editor on the first dry run.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_001.md` (this report).
- `backup/20261019_batch001/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation (record-scoped) |
|---|---|
| `registries/paper_registry_current.md` | 64 new `PAPER` records (`PAPER 247`-`310`) inserted after `PAPER 246`; 8 corpus placeholders cross-linked "Promoted to" (`CORPUS P288`, `CORPUS P395`, `CORPUS-STUB-015/023/024/049/051/157`); `CORPUS-STUB-157` title corrected in place with the superseded wording quoted; evidence depth of `PAPER 097`, `136`, `147` raised to complete (HELD-partial resumes) with the earlier receipts kept visible |
| `registries/literature_tracking_log_current.md` | 55 new `LIT` records (`LIT-0549`-`0603`); `LIT-0042/0050/0051/0073/0075/0174/0288` promoted to `processed` with a status note; `LIT-0019` evidence depth superseded; `LIT-0395` promoted to `processed` with a receipt note; `LIT-0402` reading debt marked paid |
| `registries/claim_registry_current.md` | `CLAIM 042` evidence boundary: ketogenic-diet base-rate paragraph (status `in observation` unchanged); `CLAIM 001`: wave note on hormonal co-therapy (status `conflicting evidence` unchanged) |
| `registries/working_model_current.md` | `Version` and `Last update` lines |
| `registries/working_model_history.md` | `Last update` note and `Changelog` row (written with `record_scoped_edit.py`) |
| `research/discovery_ledger_current.md` | source note of `DL-MECH-015` corrected; caution on `DL-THER-080`; pointer on `DL-MECH-012` (dry-run by the integrator, no refusal, then applied); new section with `DL-MECH-117`-`135` and `DL-METH-122`-`124` (22 staged leads) |
| `research/full_text_queue_current.md` | `FT-019` closed (old wording kept), `FT-167` annotated, `FT-195`-`200` added |
| `framework/state/state_manifest_current.md`, `state_history.md`, `growth_anchors.jsonl` | WM version, last-batch fields, `batch_20261019_001_scope` / `_candidates`, growth deltas (+64 papers, +55 literature) and a scale acknowledgement |
| derived surfaces | `coverage_report.md`, `batch_queue.md`, `pathograph_inventory.md`, `pathograph_export.jsonl`, `reading_state.md`, `surface_census.md` regenerated |
| 12 candidates | append-only `## BATCH DISPOSITION` block |

## FILES UNCHANGED

`disease_model.md`, `meta_*`, `research_*_current.md`, biomarker, endpoint and therapeutic files, the receipt ledger (542 chained, untouched), the DisMech sidecar (no sealed claim touched: no reseal needed), `dismissal_ledger_current.md`.

## CHANGE LOG

1. **Registry debt first.** All 64 PMIDs of the wave now have a `PAPER` and a `LIT` record. Numbers were assigned from `registry_records.py catalog` (`PAPER` max 246, `LIT` max 0548); the candidates' provisional ids (`P01`-`P13`) were replaced. Record text was authored from the artefacts' own front matter (JATS or HTML metadata, with full sha256 of the artefact) plus the candidates' and wave notes' per-paper content; no 8-digit PMID literal appears outside `Identifier` lines.
2. **Earned negatives carried in every record** (none is WWOX loss-of-function evidence): common-variant lipid and diabetes association papers are nominal, uncorrected or unreplicated; the oleate paper is a tumour-cell-line knockdown in conditioned medium; ceramide-synthase, ELOVL1 and peroxisome papers are myelin comparators whose cell of origin differs from the WWOX defect; recessive human ELOVL1 disease is recorded without seizures; a review's conclusion on ELOVL1 epilepsy is unsupported by its own body.
3. **Identity.** The PubMed record of PMID 31145772 joins one article's title and abstract with another article's authors, DOI and pages. `PAPER 263` carries an `identity_correction` and the DOI printed on the article; the PubMed fact is not rewritten. The article is by Jamaspishvili et al. (Acta Biochim Pol 2019;66(2):159-165); the selection file's "Permana 2019" was wrong.
4. **Research layer.** Leads staged by B, C and D became `DL-MECH-117`-`135` and `DL-METH-122`-`124` (the discovery ledger has no separate validated writer; they landed as record-scoped ops in this batch). A's two method notes are `DL-METH-123` and `124`.

## Parked (not propagated), with the reason

- C proposals 1 and 2 (support mentions on `CLAIM 034` and `CLAIM 010`): no op text, and they edit claim support sets; they stay in the candidate's section 3. No claim status or baseline is involved.
- A's optional sentence for `PAPER 084` (non-replication of its lead SNP): optional, not written.
- D's correction of the selection file's description of `PAPER 003`: the selection file is a research file, not a registry; the fact is carried in the `CLAIM 001` wave note and `DL-MECH-133`'s reading-debt lead.
- Blocked retrievals (Yuan 2025, Aqeilan 2007, Martin 2025, Kunkle 2021) were queued (`FT-197`-`200`), not obtained.

## DEFAULTS_TAKEN

1. **Scale trigger.** The 64 `PAPER` records took the paper registry to about 1190 KB, past the 1024 KB sharding trigger. Default taken: `growth_anchors.py acknowledge-scale` with the stated decision "stay on the canonical Markdown family for now"; the sharding or event-store question is **not** decided here and is reserved to the operator. The tool re-raises it at about 1479 KB.
2. **No blind locator audit.** The trigger (a baseline-claim narrowing or a MAJOR candidate) is not met; locator triples travel with the candidates.
3. **`current_state` was not set to `IN_BATCH_COMMIT`** during the batch: other actors land on `main` concurrently and the gate reads `READY`; the snapshot and `drift FRESH` check carried the protection instead.
4. **Queue ledger edited in place** (`FT-019`, `FT-167`) through the record-scoped editor, with the superseded wording kept in the row.
5. A candidate (C) was missing its receipts' PMIDs and DOIs, which tripped `OUTPUT_STUDY_MISMATCH`; the identifiers were added to its disposition block rather than editing the candidate body.

## DECISIONS_TAKEN

- Stub promotions keep the placeholder as history and cross-link it; the stub vocabulary was not changed.
- `CORPUS P395` / `LIT-0395` (Sze 2015, a commentary re-read) was first left unpromoted, then promoted to `PAPER 310` after `test_batch_queue` showed a complete read with no `PAPER` record carrying its PMID (the registry coverage-not-overstated invariant).

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 542 chained. `growth_anchors.py check`: PASS. `public_release_gate.py`: **BLOCK_PUBLICATION, 1 block, not caused by this batch** — `README_PRIVACY_CONTRADICTION` fires on a figure file name (`NG2015000992FF1.jpg`) inside `deepdive_manifests/PMID27066568.json`, written by Scientist C before this batch: the gate's `NG` accession pattern matches the publisher's figure id. Left untouched (renaming a path would break its sha256 link; loosening the gate is not an integrator's call): it needs either a manifest path alias or a gate pattern fix by whoever owns the manifest or the gate.
