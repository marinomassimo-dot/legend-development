# BATCH COMMIT REPORT — BATCH_20261019_009

> **A correction batch, and the defect it repairs is the integrator's own.** `BATCH_20261019_008` wrote a false locator count into two canonical `PAPER` records and published a correct author declaration as a defect. Integrator: ACTOR_ID `orchestrator` (stated assumption), task `ORCH-METABOLIC-BATCH-20261019`, operator authorisation. **Not medical advice.**

## Summary

- Type: MANUAL. Pre-flight LINT `WARN` (0 BLOCK); post-propagation LINT `WARN`, **0 BLOCK**.
- **WM version: `WM_v7.27` PRESERVED — no bump, and the rule is the reason.** `state_manifest_current.md` § 2 bumps `working_model_version` for *"every `BATCH_COMMIT` that modifies the disease model"*, and `prompt_batch_commit.md` § 4.6 preserves the version, the WM timestamps and the WM changelog rows for a batch with no disease-model change. A count of persisted locators sits in a record's **provenance** sentence: it changes no claim, no block, no `Status`, no `Type`, no `Summary`, no support and no uncertainty, and § 4.6's carve-out ("status changes affecting evidence eligibility, claim meaning, support or uncertainty are not structural corrections") does not reach it. So the version line, its date, the `Last update` note and the `Changelog` row of `working_model_history.md` are all **untouched**.
- Commit candidates: **none.** The scope is this integrator's error, not a candidate.
- Snapshot `backup/20261021_batch009` (not committed); pre-batch commit `8d67f7a49bad324c854f861f1291eac289175894`. No restore used.
- `FULL_FALLBACK`: **none.** Both op lists — paper registry 2 ops, dismissal ledger 1 op — accepted by the record-scoped editor on the first dry run. No `reflow`, no `to_eof`.
- Receipts: 685 chained, untouched.

## FILES TO CREATE

- `disease-models/wwox/research/batch_report_BATCH_20261019_009.md` (this report); `backup/20261021_batch009/` (snapshot; not committed).

## FILES TO UPDATE

| File | Propagation |
|---|---|
| `registries/paper_registry_current.md` | **2 ops, one per record.** `PAPER 427`'s Evidence depth sentence now reads **11 persisted verbatim locators, all 11 on the body surface**; `PAPER 428`'s reads **9 persisted verbatim locators, 8 on the body surface and 1 on a figure**. Each carries the correcting batch, the date and the superseded wording verbatim, per `prompt_batch_commit.md` § 7.2 |
| `research/dismissal_ledger_current.md` | **`D-40`** appended to `DEFAULTS THAT BIT US` — minted because no existing row covers it (`D-05`, `D-06` and `D-16` are the nearest and are about implementation winning silently, a tool sharing its subject's defect, and shell quoting; none is about sizing a container) |
| `research/commit_candidates/CC-20261020-SCIENTIST-A-AMLEXANOX-01.md` | the disposition block's discrepancy bullet withdrawn in place, with its old wording quoted and the true counts stated |
| `research/batch_report_BATCH_20261019_008.md` | the `DECISIONS_TAKEN` bullet that carried the false finding withdrawn in place, with its old wording quoted |
| `framework/state/state_manifest_current.md`, `state_history.md` | last-batch and last-LINT fields; `batch_20261019_009_scope` / `_candidates`. **`working_model_version` deliberately unchanged** |
| derived surfaces | `coverage_report`, `batch_queue`, `pathograph` (inventory and export), `reading_state`, `surface_census` regenerated from the committed inputs |

## FILES UNCHANGED

All four scientific current files except the paper registry — `working_model_current.md`, `working_model_history.md`, `claim_registry_current.md` and `literature_tracking_log_current.md` are untouched, and so are `disease_model.md`, the `meta_*` files, the research lines, the biomarker, endpoint and therapeutic files, the discovery ledger, the full-text queue, the receipt ledger (685), the DisMech sidecar, `growth_anchors.jsonl` (no structural count changed, so no `record`), the two `deepdive_manifests/` files at issue (**they were correct and nothing in them was edited**), and the other two candidates' records and disposition blocks.

## CHANGE LOG

1. **The count, re-measured.** `len(d['verbatim_locators']['entries'])` is **11** for `PMID22938201` and **9** for `PMID40544182`. Surfaces: 11 body for the first; 8 body and 1 figure for the second. Every entry in both files carries an identical key set, so there is no partial-entry class that six could be counting. **Candidate 1 § 2's declaration of 11 and 9 was correct in every respect.**
2. **The two records are repaired at source**, in place, each with the three things § 7.2 requires inside the row it corrects: the correcting batch and date, the superseded wording quoted verbatim, and nothing else — the surrounding provenance prose was not improved while the hand was in there.
3. **The false finding is withdrawn where it was published**, in the candidate's disposition block and in the `BATCH_20261019_008` report, both in place and both quoting the wording they replace. A conclusion is not overwritten silently: the old sentence travels in the row that corrects it.
4. **`D-40` minted** (`max(D-nn) + 1`; `D-39` was the maximum present, allocated by this integrator the same day).

## DEFAULTS_TAKEN

1. **No WM bump**, for the reason stated in the Summary and derived from the two normative texts rather than from precedent.
2. **No `growth_anchors.py record`:** no structural count changed (claims 47, papers 418, corpus 376, literature 681 — identical to the post-008 anchors). **The registry scale acknowledgement was not renewed**; every cost axis is far inside its budget and nothing was asked for.
3. **The manifests were not edited.** They were right. The defect was entirely in the reading of them.
4. **Op form:** `replace-within` on the exact defective substring, one op per record, so no byte outside those two sentences moved and no `reflow` had to be asserted.

## DECISIONS_TAKEN — how the wrong count arose

🔴 **The reconstruction, because it is the useful part.** At the metadata-gathering step of `BATCH_20261019_008` I ran a loop over each receipt's and manifest's interesting keys that printed `len(v)` for `verbatim_locators`. In both manifests that key holds an **object**, not an array: `waived`, `source_fulltext_indexed`, `source_fulltext_indexed_evidence`, `entries`, `note`, `artifact_locality_note`. `len()` on a mapping returns its **key count**, so the loop printed **6**, and it printed 6 for *both* files because 6 is a property of the shared schema, not of either reading. I then wrote that number into `PAPER 427` and `PAPER 428` and reported the candidate's correct declaration as a discrepancy.

**Two tells were in front of me and both were misread as corroboration rather than as alarms:**
- **Two unrelated readings returned the identical number.** Two independent partial reads of two different articles landing on exactly the same locator count is the signature of measuring something they share. I read the agreement as a confirmation that the instrument was sound.
- **The disagreement with the author ran in the same direction for both** (6 against 11, 6 against 9). A systematic, same-signed gap across two artefacts points at the measuring instrument; a real authoring error would not be expected to be systematic.

**And a third, procedural:** I had the correct expression available. Candidate 1 § 2 declared 11 and 9 and the manifests were on disk; I treated my own one-liner as the arbiter of an author's declaration without once asserting what shape the node I was sizing had. That is `D-05` and `D-06` from the other side — **implementation wins silently**, including my own.

**Detection rule, recorded as `D-40`:** never size a JSON node without asserting its type — `assert isinstance(x, list)` before `len(x)`, or name the leaf (`['entries']`) explicitly. And when a re-measurement contradicts an author's declaration, **the first hypothesis is that the instrument is wrong, not the author** — a count that lands identically on two different artefacts is measuring something they share.

🔵 **One honest note about how this was caught.** It was not caught by any gate. LINT, the receipt chain, `growth_anchors`, the publication gate and `candidate_tree_freshness` all passed over the false count, because none of them reads a prose count in a provenance sentence against the artefact it describes. It was caught because the coordinator re-measured a number I had reported as a finding. **A number a batch asserts about another artefact is derived, not copied** — the repository already carries that rule (the registry-scale note of 2026-10-20 records the same class of failure), and this is a second instance of it in two days. No new gate is proposed here: the cheap half is `D-40`'s detection rule, and the expensive half — a checker that re-derives every count a registry record asserts about a manifest — is a real capability gap and is named as one rather than improvised at the end of a correction batch.

## Verification

`legend_lint.py`: `WARN`, **0 BLOCK**. `fulltext_receipts.py verify`: OK, **685 chained**, tail anchored. `growth_anchors.py check`: **PASS** (claims 47, papers 418, corpus 376, literature 681, registry-only 4, unread premises 0). `public_release_gate.py`: **PASS, 0 BLOCKS**. The two corrected sentences re-read against the manifests after the edit. No e-mail string, no truncated digest and no study-identifier literal outside the `Identifier` lines already present. **The full release battery was not run — the Orchestrator runs it.**

## Recommended next actions

- **Capability gap, named not improvised:** nothing re-derives a count that a registry record asserts about a manifest, a ledger or a figure. `D-40` makes the author's mistake detectable; a checker would make it unmissable. Worth scoping as a harness item, with `test_manifest_receipt_provenance.py` as the nearest precedent for the shape.
- The four recommended actions of `BATCH_20261019_008` stand unchanged; none of them depended on the corrected number.
