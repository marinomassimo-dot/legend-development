# BATCH COMMIT REPORT — BATCH_20261019_003

> Metabolic batch 2026-10-19, waves 2 and 3 (interventions groups H3, H4, H5 and the GOLD pair), together with the repairs of the Mirror review of `BATCH_20261019_001`. Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**
> `BATCH_20261019_002` was reserved for the Mirror repairs alone. The repairs were folded into this batch because the lot's 22 `ORPHAN_COMPLETE_READ` kept `BATCH_COMMIT` blocked; **`_002` is unused** and no batch carries that identifier.

## Summary

- Type: MANUAL (the backlog threshold of 5 was also met). Pre-flight LINT: `BLOCK_BATCH_COMMIT` (22 `ORPHAN_COMPLETE_READ` plus 1 `OUTPUT_STUDY_MISMATCH`), all discharged by this batch. Post-propagation LINT: `WARN`, 0 BLOCK (the only registry-related warning left, `CLAIM 042` against `PAPER 017`, predates the batch).
- WM version: `WM_v7.21` -> `WM_v7.22` (MINOR; one bump per batch; the rule requires it because evidence-boundary text of `CLAIM 001`, `017`, `020`, `031` and `042` changed).
- Commit candidates: 10 on disk for the lot, **9 PROPAGATED**, **1 DEFERRED** (`CC-20261019-SCIENTIST-C-HELD-01`: its ten receipts are staged, not in the ledger; it reached main after the scope was fixed), 0 superseded, 0 merged. Conflicts: 0.
- Snapshot: `backup/20261019_batch003` (not committed); pre-batch commit `7b214f1c4982142b0e161944b46110f6f33987b7`. One restore was used inside the batch to re-do the registry insertions after a separator defect in the first op text (the first attempt put a doubled `---` before `PAPER 311` and no separator before `CORPUS-STUB-181`); the registries were restored byte for byte and re-applied. No other restore.
- No claim was created or reversed; no `Status`, `Type` or `Summary` changed anywhere. `FULL_FALLBACK`: none; every op list was accepted by the record-scoped editor on the first dry run.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_003.md` (this report).
- `backup/20261019_batch003/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation (record-scoped) |
|---|---|
| `registries/paper_registry_current.md` | 45 new `PAPER` records (`PAPER 311`-`355`) after `PAPER 310`; `CORPUS P360` cross-linked "Promoted to" (kept as history); notes on `PAPER 005`, `011`, `015`, `018`, `021`, `031`, `061`, `071`, `093`; Mirror repairs on `PAPER 097` (F2), `PAPER 263` (F3), `PAPER 289` and `291` (F5) |
| `registries/literature_tracking_log_current.md` | 44 new `LIT` records (`LIT-0604`-`0647`); `LIT-0360` promoted to `processed`; `LIT-0561` pointer to the `PAPER 263` identity note (F3) |
| `registries/claim_registry_current.md` | `CLAIM 001` wave note corrected (B1); `CLAIM 042` base rate corrected (F1); evidence-boundary additions on `CLAIM 017`, `020`, `031` (status unchanged in all five) |
| `registries/working_model_current.md` | `Version` and `Last update` lines |
| `registries/working_model_history.md` | `Last update` note and `Changelog` row (written with `record_scoped_edit.py`) |
| `research/discovery_ledger_current.md` | `DL-MECH-133` (B1), `DL-MECH-117` (F4), `DL-MECH-121` (F1) repaired; new section with `DL-MECH-136`-`150` and `DL-METH-125` |
| `research/dismissal_ledger_current.md` | `DIS-037`-`040` (the four negatives of the H5 candidate, each with premises and revival trigger) |
| `research/metabolic_wave_20261019_scientist-d.md` | the Scientist D wave note's "disagree" sentence corrected in place with the correction marked (B1) |
| `framework/state/state_manifest_current.md`, `state_history.md`, `growth_anchors.jsonl` | WM version, last-batch fields, `batch_20261019_003_scope` / `_candidates`, growth delta (+45 papers, +44 literature) with the scale-acknowledgement count correction as a new note (F6) |
| 10 candidates | append-only `## BATCH DISPOSITION` block (9 PROPAGATED, 1 DEFERRED); a CORRECTION line on `CC-20261019-SCIENTISTD-G4-VABAM-01`; the epinephrine-safety disposition names the study identifiers (PMID, receipt, DOI), fixing the `OUTPUT_STUDY_MISMATCH` |
| derived surfaces | regenerated from the committed inputs in a second commit |

## FILES UNCHANGED

`disease_model.md`, `meta_*`, `research_*_current.md`, biomarker, endpoint and therapeutic files, the full-text queue, the receipt ledger (597 chained, untouched by this batch), the DisMech sidecar (no sealed claim touched).

## CHANGE LOG

1. **Registry debt.** All 45 PMIDs of the interventions lots H3, H4 and H5 now have a `PAPER` and a `LIT` record (13 + 15 + 16 new in addition to the promotion of `CORPUS P360`). Numbers were assigned from `registry_records.py catalog` (`PAPER` max 310, `LIT` max 0603). Identity (title, authors, journal, DOI) was authored from each artefact's own JATS front matter; the evidence depth, receipt, artefact path and sha256 come from the ledger event, and partial depths state what the receipt's `coverage` map leaves unread.
2. **Substitutes labelled.** Every new record is labelled NOT WWOX EVIDENCE, except the WWOX-direct gene-level blood-pressure association (`PAPER 324`): exploratory, one ancestry group, no SNP at the stated threshold, no autonomic content.
3. **Gold notes.** The re-read WWOX-direct papers carry their evidence-boundary additions: `CLAIM 020` (the 40-year course is a retrospective narrative with one video-EEG day), `CLAIM 017` (n = 1 does not overturn the cohort rule), and the opposite-sign metabolic phenotype notes on `PAPER 005`, `011`, `061`, `071`, `021`, `031`.
4. **Definition note.** `CLAIM 031` states that SUDEP excludes status epilepticus, so a death in status epilepticus is not SUDEP and the two must be counted separately.

## Mirror repairs of `BATCH_20261019_001` (each checked against the source, not the review)

| # | Verdict on the Mirror claim | What was done |
|---|---|---|
| B1 | **Confirmed**, with one addition the review missed: the wave note also said both cohorts were "read in full", but both receipts are `partial_fulltext_read` (figure images, references and supplement not examined). Sathe: hormonal therapy in 11 of 11 symptomatic cases and no difference in the asymptomatic comparison (4 of 6 against 17 of 39); Stevering: RR 0.94 for the MRI finding and RR 9.00 for symptoms (eight exposed). They agree. | `CLAIM 001` wave note, `DL-MECH-133` and the Scientist D wave note restated ("both associate hormonal therapy with symptomatic VABAM, neither with the MRI finding alone; both underpowered; neither isolates a mechanism"), and the depth corrected to partial. The candidate body is left as written with a CORRECTION line. Status `conflicting evidence` unchanged. |
| F1 | **Confirmed.** The dossier of the review records CDKL5 0 of 10 in the same gene-level study; `PAPER 269` is `partial_fulltext_read` (receipt coverage: figures `captions_only`). | `CLAIM 042` paragraph and `DL-MECH-121` carry CDKL5 0 of 10 (the 47 to 100 range is a range among responding groups), and the `PREMISE_TAG` names the partial depth. Status unchanged. |
| F2 | **Confirmed.** `PAPER 097` still read "`figures: captions_only` in entrambe: nessun pannello ispezionato" next to `complete_fulltext_read`. | Marked "as of the earlier receipts only; superseded by `FTR-20261019-35984507-03`", with the body negatives' currency stated as unknown. |
| F3 | **Confirmed.** A fresh PubMed query returns the East Asian type-2-diabetes title and abstract with Permana et al. as authors, DOI `10.18388/abp.2020_5563`, pages 679-686 and a 2019 date; no 2021 appears. | `PAPER 263` wording ("another 2021 article") replaced by what PubMed returns; `LIT-0561` Note now points to the `PAPER 263` identity note. |
| F4 | **Confirmed.** | `DL-MECH-117` and its title recast as a conditional on uncorrelated transcripts. |
| F5 | **Confirmed.** `PAPER 291` asserted a CLAIM 034 support and `PAPER 289` named CLAIM 010, both with `Claim links: none`. The candidate has no op text, so the support was not landed. | Both sentences marked "proposed, parked at `BATCH_20261019_001` and again at `BATCH_20261019_003`". |
| F6 | **Confirmed** (64 landed, 1,214,458 bytes). | Corrected in a new growth-anchor note on this batch's record; the `scale_ack` anchor (1,211,399 bytes) is untouched. |

## Parked (not propagated), with the reason

- Oxygen candidate: the `CLAIM 009` scope note and the `CLAIM 025` support mention (no op text); its reading debts (closed-body WWOX-direct papers and primaries behind the reviews) were not queued as full-text queue rows.
- Adrenergic candidate: the optional working-model note on catecholamines (no op text).
- GOLD-METAB item 1 asks for an RL-003 evidence boundary; research lines are not among the four current files and were not edited.
- `CC-20261019-SCIENTIST-C-HELD-01` (DEFERRED, see above).

## DEFAULTS_TAKEN

1. **Folded repairs.** The repairs ran inside the batch that clears the orphans instead of as a separate `_002` (reserved, unused), on the coordinator's decision.
2. **Transferability grades** for the H3 and H4 records were assigned by the integrator (T4, class-level) because those candidates grade none per paper; H5 grades come from its candidate.
3. **Primary pathway** "none — comparator / adjacent source" for every substitute; `P5` only for the WWOX-direct blood-pressure record.
4. **Scale.** The registry is 1,321,413 bytes, 9 percent above the acknowledged anchor; the tool re-raises the sharding question at +25 percent. No new acknowledgement was recorded.
5. **No blind locator audit** (no baseline claim narrowed, no MAJOR candidate); triples travel with the candidates.
6. **`current_state` stayed `READY`** during the batch (concurrent landings); the snapshot and the clean base carried the protection.

## DECISIONS_TAKEN

- Published-case details already carried by the GOLD candidate (a variant name in a third-party case report) were kept; no individual linkage to the reference genotype was introduced.
- Where the review and the dossier differed from the wave note on depth (B1), the receipt governs.
- The four negatives of the H5 candidate became `DIS-037`-`040`; their revival triggers point at `DL-MECH-148` and `149`.

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 597 chained. `growth_anchors.py check`: PASS.
