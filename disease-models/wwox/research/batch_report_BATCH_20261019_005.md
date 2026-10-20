# BATCH COMMIT REPORT — BATCH_20261019_005

> Metabolic batch 2026-10-19, interventions lot H1/H2 of Scientist A (transfusion, iron, plasma, complement, albumin, immunoglobulin). Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation, operator away. **Not medical advice.**

## Summary

- Type: MANUAL. Pre-flight LINT: `BLOCK_BATCH_COMMIT` (the lot's complete readings had no registry record: `ORPHAN_COMPLETE_READ`), discharged by this batch. Post-propagation LINT: `WARN`, 0 BLOCK, 0 `ORPHAN_COMPLETE_READ` (the remaining warnings are the standing `UNLINKED_SUPPORT` and `POSSIBLE_CONTRAST` set; none names a record of this batch).
- WM version: `WM_v7.23` -> `WM_v7.24` (MINOR; one bump per batch; the rule requires it because the registries gained 58 records and `CLAIM 028` gained a source).
- Commit candidates: 2 on scope (`CC-20261019-SCIENTIST-A-PLASMA-01`, `CC-20261019-SCIENTIST-A-PLASMA-02`), **2 PROPAGATED**, 0 deferred, 0 superseded, 0 merged. The six lipid candidates of the same Scientist were already `PROPAGATED` by `BATCH_20261019_001`; no other `CC-20261019-SCIENTIST-A-*` on main was undispositioned. Receipts: 30 of this lot are in the ledger (654 chained at `38de821c`).
- Snapshot: `backup/20261020_batch005` (not committed); pre-batch commit `38de821c5577b0dd4ffd933f9dd534e4ecc6edd5`. No restore was used.
- No claim was created or reversed; no `Status`, `Type` or `Summary` changed anywhere. `FULL_FALLBACK`: none; every op list was accepted by the record-scoped editor on the first dry run.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_005.md` (this report).
- `backup/20261020_batch005/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `registries/paper_registry_current.md` | 30 new `PAPER` records (`PAPER 370`-`399`) after `PAPER 369`, in the candidate's table order; "Promoted to" line on `CORPUS-STUB-068` (-> `PAPER 383`) and `CORPUS P330` (-> `PAPER 387`), both kept as history |
| `registries/literature_tracking_log_current.md` | 28 new `LIT` records (`LIT-0652`-`0679`); `LIT-0091` and `LIT-0330` promoted to `processed` with a Status note |
| `registries/claim_registry_current.md` | `CLAIM 028`: one further source in the `Source` line and the `Wikilinks` line (status, type and summary unchanged) |
| `registries/working_model_current.md` | `Version` and `Last update` lines |
| `registries/working_model_history.md` | `Last update` note and `Changelog` row (written with `record_scoped_edit.py`) |
| `research/interventions_batch_selection_20261019.md` | the "nothing on complement" wording in the Karayanni row corrected in place, old wording quoted |
| `research/full_text_queue_current.md` | `FT-108` follow-up line (the text-only reading was resumed at complete depth; the earlier verdict is not rewritten) |
| `framework/state/state_manifest_current.md`, `state_history.md`, `growth_anchors.jsonl` | WM version, last-batch fields, `batch_20261019_005_scope` / `_candidates`, growth delta (+30 papers, +28 literature) |
| 2 candidates | append-only `## BATCH DISPOSITION` block (2 PROPAGATED) |
| derived surfaces | `coverage_report`, `batch_queue` and `pathograph` (inventory and export) regenerated from the committed inputs; `reading_state` regenerated and unchanged (it reads only the ledger, untouched by this batch) |

## FILES UNCHANGED

`disease_model.md`, `meta_*`, `research_*_current.md`, biomarker, endpoint and therapeutic files, the discovery and dismissal ledgers, the receipt ledger (654 chained, untouched), the DisMech sidecar (no sealed claim touched: `CLAIM 028` is not one of `016`/`024`/`035`), `surface_census.md` (a dated photograph of a gitignored directory; not regenerated, as in `BATCH_20261019_003` and `_004`).

## CHANGE LOG

1. **Registry debt.** Every PMID of the lot now has a `PAPER` record and a `LIT` record. 28 are new class-level records; two upgrade existing placeholders (Shin 2023 from `CORPUS-STUB-068`, Hong 2009 from the stale `CORPUS P330`). Numbers continue after the last (`PAPER` max was 369, `LIT` max 0651). Identity was authored from the PubMed record (E-utilities summary, 2026-10-20) and checked against each receipt's study identifiers; the evidence depth, receipt, artefact path and full sha256 come from the ledger event; partial depths and absent sections state what the receipt's `coverage` map leaves unread. Role text is derived from the Scientist's per-paper readings; every class-level record is labelled **NOT WWOX EVIDENCE**.
2. **`CLAIM 028` source.** Shin 2023 (`PAPER 383`) is added as a further source: a non-neural partial-knockdown instance in which WWOX loss lowers poly(I:C)-induced NF-kB signalling, with the system gap stated (one immortalised human keratinocyte line, partial knockdown, one stimulus). The opposite-sign comparison is carried in the paper record with `PAPER 102`, `113`, `114` and `115` named there; the claim text does not name them (a claim must not name a paper whose `Claim links` do not name it). Status stays `flagged for review`, Type stays INFERENZA, Summary is unchanged.
3. **Complement correction.** Hong 2009 (`PAPER 387`) is the only WWOX-direct complement paper: gain of WWOX in prostate cancer cells, killing that needs overexpression, no loss-of-function datum, a serum-free arm shown as "data not shown", and a text-versus-figure contradiction on C7 depletion. The record states that the selection file's "nothing on complement" was too strong, and the selection file row is corrected in place with the old wording quoted. The earlier 2026-09-21 verdict on the endogenous activation arm is carried unchanged and the figure-level limits are added; `FT-108` carries a follow-up line.
4. **Methods and chains of inference recorded as read.** Figure-versus-text and table-versus-text discrepancies of individual papers (for example the plasma-and-IVH target-trial emulation, the plasma-exchange series, the home-made ketogenic-diet rat study) are in the records; none changes a claim.

## Parked (not propagated), with the reason

- Section 3 of `PLASMA-02` (seven proposed method notes: non-significance read as prevention, omnibus test read as pairwise, subgroup claim on a stratum with no comparison arm, sensitivity statistic read in the wrong direction, pooled correlations and ordinal scales analysed by ANOVA, reference-title mismatch, table arithmetic that does not reproduce): patterns, not claims; no registry target and no op text.
- **Full-text queue entries for gene-direct reference debts.** Not written. The two manifests that record them (Shin: 8 references; Hong: 12) list entries with "no PMID in the screened entry" and state "not queued by this actor"; neither candidate carries an entry, an identifier or op text, and the instruction was to add them only where the candidates carry them. They stay recorded in the manifests; a later reference-resolution pass would have to identify the papers first. The four blocked WWOX-direct items named in the wave note stay blocked (no lawful body).
- Informational: the Scientist's outcome statements that touch an existing strand (a transfusion-and-glucose observation, a ketogenic-diet rat study) were kept as record text only; no claim support mention was added.

## DEFAULTS_TAKEN

1. **Numbering and order.** `PAPER 370`-`399` follow the candidate's table order (Shin at 383, Hong at 387); `LIT-0652`-`0679` follow the same order skipping those two.
2. **Transferability grade** T3 for mechanistic or biological substitutes, T4 for clinical-practice papers in other populations, reviews of such practice and case reports; T4 for Shin (non-neural, per the candidate); T3 for Hong (WWOX-direct, not a loss-of-function neural system). Clinical relevance LOW for the two WWOX-direct papers and BACKGROUND (non-WWOX) for the rest. The grades are the integrator's, stated in each record.
3. **Primary pathway** "none — comparator / adjacent source" for the 28 class-level records; "inflammatory signalling (NF-kB), non-neural" for Shin; "oncology / tumor suppressor biology" for Hong.
4. **Claim links.** Only `PAPER 383` carries a claim link (`CLAIM 028`); no other record in the lot names a claim.
5. **Scale.** The paper registry grew by about 90 KB; no new scale acknowledgement was recorded (the tool re-raises the sharding question at +25 percent over the acknowledged anchor).
6. **`surface_census.md` not regenerated** (see FILES UNCHANGED).

## DECISIONS_TAKEN

- A study identifier appears only in `Identifier` lines of registry records and in the candidates; the claim note and this report name papers by `PAPER` number, so that no claim names a paper whose `Claim links` does not name it.
- No parent-side term is paired with a variant in the registry records of the batch (a record that would have carried one — the COL4A2 missense series — states the variant only as "of uncertain significance" with no inheritance wording); `public_release_gate.py` was run. *Narrowed at `BATCH_20261019_006` (Mirror M8): the original sentence said "anywhere in the new text", which is false of the files the batch rests on. A dossier and the Scientist A wave file still record transmission wording about a published COL4A2 family, and a WWOX dossier records the carrier status of the relatives of a published child. These are third-party published facts, none is the reference genotype's, and they are retained on purpose; the gate's pairing rule is about the reference genotype.*
- Hong 2009 was upgraded as a promotion of a stale placeholder rather than as a new record, so that the registry holds one record per paper; its `LIT-0330` was promoted in place.
- The two disposition blocks were written by the integrator; the candidates' locator triples are carried for a later blind audit and the audit was not run here (no baseline claim is narrowed, reversed or removed).

## Verification

`legend_lint.py`: `WARN`, 0 BLOCK. `fulltext_receipts.py verify`: OK, 654 chained (untouched by this batch). `growth_anchors.py check`: PASS (papers 389, corpus 376, literature 660, unread premises 0). `public_release_gate.py`: PASS, 0 BLOCKS. The full release battery was not run (the Orchestrator runs it).
