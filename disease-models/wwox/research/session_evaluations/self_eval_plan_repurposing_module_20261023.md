# Self-evaluation — Harness Engineering (`plan`), Drug Repurposing module, 2026-10-22 → 2026-10-23

Task `PLAN-DRUGREPURPOSING-MODULE-20261022`, deliverables A–E of `harness_mandate_20261022.md`.
A harness session: no paper was read and no receipt was recorded by this actor. Not medical advice.

## Scope and executable verdict

- Batch/session: harness mandate, five stages landed on `main` (A `a24abe41`, B `c17e6e33` + `380e3a64`, C `cfb67740`, D `c34bbf81`, E this landing).
- Studies and complete-read receipt IDs: none by this actor (readings are a Scientist's act; the module consumes receipts, it does not create them).
- `session_self_eval.py --workspace . --disease wwox`: `VERDICT: PASS — every complete read has landed and every declared output resolves` (pre-existing DECLARED GAP lines belong to earlier readings, not to this task).
- Per-study manifest(s): none written; 1,180 manifest rows read by the join.
- Receipt verification: `fulltext_receipts.py verify` → OK, 848 chained receipts, tail anchored (at every landing).
- Structural LINT: 0 BLOCK at every landing.
- Local verdict: PASS.
- Workspace/global verdict and concurrent conditions: gate PASS 0 blocks at every landing; one fresh-clone battery per landed stage (A PASS WITH SKIPS 154/12; B FAIL → the executable bit on two new entrypoints, repaired `380e3a64`; C and E batteries recorded in the task record); no concurrent writer on the worktree.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | not applicable: no reading was performed; the join reports the depth others reached (769 complete reads, 351 partial, 57 without a receipt behind 332 queries) | n/a | — |
| Main message and original contribution | the differentiator is the join: 146 → 59 abstentions once PAPER ids and named claims/leads are resolved through the registries; without it the module sees almost nothing (`module_proof_20261023.md` § 2.4) | strong | — |
| Hidden gold beyond keywords/abstract | two candidates stand on unaudited `contradicts_locator` entries that no one had scheduled for audit (`Q-R-02`, `Q-N-17`) → AUDIT rows | strong | the audits are owed to a blind auditor |
| Source parity: context, type and recency | every external source carries licence, citation and retrieval date; openFDA class-name lookups are `NO_MATCH_FOUND`, written as not-absence | strong | — |
| Team type, field density, observation vs interpretation | not applicable to a harness stage | n/a | — |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | every derived card is `IPOTESI`, `canonical: false`; the lead specs are `INFERENZA`; external hits are `NOT WWOX EVIDENCE` | strong | — |
| Existing claims touched; conflicts/revival triggers | none touched; the four current files were read through `registry_records.py`, never written | strong | — |
| Multi-hop and corpus cross-query | one hop only (record → named record → papers), written per PMID in `pmids_via_records`; a second hop was deliberately not built | partial | a second hop would inflate evidence tables with papers two records away; left out on purpose |

## Persistence diagnosis

- Durable ledger/registry IDs and wikilinks: task record `ledger/tasks/plan/PLAN-DRUGREPURPOSING-MODULE-20261022.json` (A.1c queue, DEFAULTS_TAKEN, DECISIONS_TAKEN, STOP_LOG, LICENCES_READ, NOT_BUILT_BY_DESIGN, STAGE_REPORTS); nothing appended to the discovery ledger by this actor (the lead specs are staged by a Scientist).
- Reading queue/debt: 26 rows for the next batch in `research/repurposing_batch_selection_20261023_module.md` (21 SELECT, 3 REPLICATE, 2 AUDIT).
- Dossier and commit candidate: none (no scientific delta).
- Receipt source fingerprint, coverage and supplement state: consumed, not produced.
- Can a future run distinguish full text from abstract only? How: yes — `reading_depth` per paper row comes from the strongest standing receipt with its `receipt_id`, and the bridge refuses a complete-read declaration without the receipt.

## Process and capability diagnosis

- Skills/gates/patterns used: legend-start bootstrap order, §21c/§21d/§21e, `task_close.py`, `safe_push.py`, fresh-clone battery by PID, `registry_records.py` for every registry read, the bridge for every card.
- Plausible skills deliberately declined, with reasons: ToolUniverse / OptimusKG installs (direct key-less calls measured under a second each; a wrapper framework adds a dependency, not evidence); a freshness gate on the committed join snapshot (would turn red on unrelated batches); a second evidence index (`build_evidence_index.py` already exists); any scoring (hard limit).
- Failures, retries, extraction mismatches or concurrency events: (1) executable bit missing on two entrypoints, caught by the fresh-clone battery, not by the local suites; (2) ChEMBL adapter put a name with spaces into a URL unencoded — the first live join run crashed; (3) the first evidence tables read the wrong receipt-ledger path (`research/` instead of `registries/`) and showed `NO_RECEIPT` beside 25 locators; (4) the bridge refused a complete-read declaration without its receipt id — correct behaviour, which the join had not anticipated; (5) one Edit landed in the root checkout instead of the worktree and was reversed by the inverse edit; (6) a convention test rejected the word "key" inside "optional key not used".
- What caught each failure before an overclaim: (1) `scripts/test_release_surface.py` in the battery; (2) the traceback of the live run, then the adapter guard that turns an exception into `QUERY_ERROR`; (3) the contradiction "NO_RECEIPT with 25 locators" visible in the card table; (4) the bridge's own validator; (5) `git status` on the root; (6) the suite's own failure message.
- Disease-agnostic micro-upgrade shipped: the join turns an adapter exception into a `QUERY_ERROR` for that query and caps cached hits at 100 with the total recorded; the ChEMBL adapter URL-encodes its queries.
- Regression/evidence that makes the upgrade persistent: `test_repurposing_adapter.py` (18) and `test_repurposing_join.py` (18), both in `run_release_regressions.py`.
- Residual risk and next decisive action: the committed `join/` snapshot goes stale as batches land and nothing turns red — by design; the next decisive action is one `repurposing_join.py run` after the next batch, read as a diff. The mechanism map's twenty prose-cited records are the single largest source of abstention; resolving them to `PAPER` ids is a selector's act and is already in the SELECT rows.

## Attribution census — required, fixed, parseable

```
ATTRIBUTION_CENSUS
incidents: 6
machine: 4   blind_auditor: 0   peer: 0   self: 2
severity_high: 1   of which self: 0
undetected_known: 0
```

`severity_high` is the executable-bit regression: it reached `main` and was caught by the battery after landing, before the push. `self` counts the wrong ledger path (seen in the output table) and the misplaced edit (seen in `git status`).

## §21c output

`DEFAULTS_TAKEN` and `STOP_LOG` are in the task record, both non-empty.
