# IT16 P3 - catalogue identity and source resilience (2026-11-01)

Scope: only the gaps that change a decision or cut repeated work, each measured. ChEMBL_37 (2026-05-01) through `framework/adapters/chembl.py`; ChEMBL data CC BY-SA 3.0, attribution as in the adapter. Third-party responses are in the gitignored cache `files/drug_repurposing_it16/catalogue_resilience_it16_p3_20261101/cache` (9.8 MB, 69 files); digests in `cache_SHA256SUMS.txt`.

## 1. Offline ChEMBL dump: WATCH confirmed, not downloaded

| Measured today | Value |
|---|---|
| Release | ChEMBL_37 (status.json 2026-11-01: UP), dumps dated 2026-05-29 |
| SQLite tar.gz | 5,764,252,857 bytes (5.4 GiB); PostgreSQL 2,088,889,426 bytes |
| Throughput (32 MiB range request) | 5.4 MB/s, so about 18 min for SQLite |
| Disk free | 85 GB; unpacked size NOT measured (tens of GB expected) |
| Licence | CC BY-SA 3.0 (share-alike on any redistributed derived table; attribution with URL and release) |

Were the IT15 reopen conditions met? Condition "REST 5xx for a task-critical query twice in a day": by the letter yes (Q-A: 35 failed attempts over 8 distinct URLs, 32 HTTP 500 and 3 transport failures; 17 of them on `status.json`, a version label). In substance no: the 8 URLs are the accession and gene searches, 100-870 KB answers; 6 of them failed all three attempts in the run. I replayed all 8 today: all return HTTP 200. The outage was a window, not a missing source. Condition "gene-per-subunit or variant-aware potency table": gene symbols per subunit are already fetched by the adapter from REST (`target_genes`); only `variant_sequences` (mutant protein) is not, and no current question needs it. Verdict: WATCH, no download. Tightened reopen: a task-critical request still failing after retries in two separate sessions on different hours, or a question that needs variant sequences or a cross-compound join the REST pages cannot return within a session.

## 2. Resilience in the adapter (the smallest change)

Compared: (a) cache of successful responses; (b) retrieve only missing parts; (c) targeted acquisition; (d) offline dump. (a) and (b) are one mechanism because every page and every batch is its own cached request; (c) is what the packages already do; (d) is item 1. Shipped:

* `framework/adapters/_http.py: make_fetch(cache_dir, retries, pause)`: bounded retry (5xx or transport failure only, at most `retries`, every failed attempt logged in `fetch.failures`), cache of HTTP 200 responses only, keyed by SHA-256 of URL+params+body, file carries its `retrieved_at`; an error, a 404 or a damaged file is never an answer; nothing is written unless a directory is given. `fetch.stats` counts cache hits, network requests, failed attempts, requests that ended in an error. The key does not contain the release: use one directory per release.
* `chembl.query` accepts that fetch unchanged (`fetch=`) and then states `transport`. Activity answers state `coverage`: COMPLETE, TRUNCATED, PARTIAL_ERROR (rows read are kept with `next_offset`; status stays QUERY_ERROR), NOT_READ, COMPLETE_ASSAY_CONTEXT_MISSING, COMPLETE_TARGET_GENES_MISSING. Four states that were one `error` string or a note.
* `max_rows` ceiling 2000 -> 20000 (default unchanged, 400); a cap that is still hit says TRUNCATED.

Measured: `resume_check.tsv` second identical query: 0 network requests, 4 cache hits, 0.0 s (first run 2 requests, 0.97 s). The three IT15 truncated queries lost 21 + 156 + 943 rows at the 2000 cap; `truncation_check.tsv` re-runs CHEMBL1904 IC50 with max_rows 3000: 2021 of 2021, COMPLETE, 0 failed attempts. Today's whole run: 67 network requests, 0 failed attempts, so the retry path was exercised only by the unit tests (`ResilientTransport`, 7 tests), not by a live outage. Cost: none beyond 9.8 MB of cache. A cache hides a ChEMBL correction until the directory is renewed; that is why the key carries no version and the directory should.

Known cost: a failing `status.json` spends the retry budget on a version label; a rerun with the cache avoids it.

## 3. Identity: the seven false "not found" names

The adapter was not the cause. `identity_retest.tsv`: all 8 queue names (acamprosate, AV-101, AZD8108, delucemine, indantadol, neramexane, ralfinamide, felbamate) return MATCH_FOUND by name through the adapter today. The IT15 miss was a name match on a synonym list truncated to ten, in the package scripts (`names_it15.py`), not the adapter's exact-match rule. What the adapter did lack, and now has:

* Salt versus parent. The queue ID CHEMBL2106165 is delucemine HYDROCHLORIDE; the parent is CHEMBL2110814 (DELUCEMINE, phase 2), which carries the mechanism "Glutamate [NMDA] receptor antagonist" (CHEMBL2094124). The IT15 verifier's "delucemine: no NMDAR record in ChEMBL" (and the 'no mechanism' of the salt row) is therefore a salt-level finding: at parent level a mechanism record EXISTS. Neramexane (parent CHEMBL2110954) has, besides the NMDA antagonist mechanism, a second one: "Neuronal acetylcholine receptor; alpha9/alpha10 antagonist" (CHEMBL2109238), not in the IT15 verification. Neither has activity rows (0 on parent, as before), so no subunit comparison and no case changes. Mechanism rows are marked `mechanism_found_via` and `queried_is_salt_or_child`; activity rows of salt, parent, stereoisomer and metabolite are never merged (test).
* Names ChEMBL does not store. `AP5`, `d-AP5`, `dizocilpine`, `TCN-201` and `Ro 25-6981` give NO_MATCH_FOUND by design (no molecule carries that name or synonym; ChEMBL stores MK-801 as the maleate CHEMBL344151 with parent CHEMBL284237, and Ro 25-6981 as CHEMBL305195 with no name at all). The answer now lists the nearest hits with synonyms and parent so the reader sees them, and `{"drug": name, "molecule_id": "CHEMBL..."}` reads a declared identity (`identity_basis: declared_chembl_id`, name kept; 404 is NO_MATCH). A search-ranked guess is never promoted to a match.
* Short names. No queue entry has a name shorter than 6 characters (column in `queue_reconciliation_reports_searched.tsv`), so the 6-character floor of `_name_tokens` loses nothing today; not changed.

## 4. Assay context for Ro 25-6981 and ethosuximide

ChEMBL answers now (HTTP 200, no retry needed). Pulled the activity rows of CHEMBL305195 (27 of 27) and CHEMBL696 (292 of 292), coverage COMPLETE; 186 of 186 assays that `scout_it14_p6_20261101/relations.tsv` references and `assay_context.tsv` lacked are recovered (`assay_context_recovered.tsv`, same 11 columns, not merged into the other package). Regrade with `scout_it14_p6_20261101/regrade_table.py` (unchanged grader on this branch) into `regraded_with_recovered_context.tsv`: 40 rows, INTERPRETABLE 3 -> 4, LIMITED 19 -> 18; exactly two rows change, both Ro 25-6981:

* CHEMBL1132364 (rat, 9 vs 52,000 nM): LIMITED "assay context not retained" -> LIMITED "assay techniques differ (no shared technique among the descriptions)". The descriptions are "Antagonistic activity against N-methyl-D-aspartate glutamate receptor 1/2A/1/2B" with no technique, cell system or conditions. The new reason text is misleading: the technique is not stated, not different. This is the condition-missing case the orchestrator's grader change addresses; I did not touch `selectivity_p6.py`.
* CHEMBL4308825 (the Burnell 2018 review, human oocyte TEVC for both arms): LIMITED -> INTERPRETABLE under the current grader. The earlier verification stands: it is a compilation of two papers and the grader still has no provenance guard; do not read this INTERPRETABLE as one experiment.

Ethosuximide: no row changes (all its document groups are NOT_DETERMINABLE: fewer than two attributable targets); the context was missing for it but decided nothing.

## 5. Queue reconciliation over the research reports

`q5_reconcile_docs.py` applies the tokens and whole-word pattern of `ranking_it8.prior_assessments` to the 1,393 markdown files under `research/` that do not themselves read the queue (11 excluded: they contain "deepening_queue"; without that exclusion the IT15 packages count the queue as a mention of itself). Result (`queue_reconciliation_reports_searched.tsv`): 6 of 34 values change, all NO_CARD_OR_RECORD_FOUND -> MENTIONED_ONLY: esketamine (2 documents), abt 639 (1), ulixacaltamide (4), bepridil (2), mibefradil (3), trimethadione (9). Totals 4 ASSESSED_ELSEWHERE / 5 MENTIONED_ONLY / 25 NO_CARD -> 4 / 11 / 19. Nothing becomes ASSESSED_ELSEWHERE (a text mention cannot establish an assessment). The other 19 have no mention outside the queue's own readers. Decision: NOT wired into `ranking_it8.py`: it would regenerate the queue, the ranking snapshots and their tests that the orchestrator is concurrently touching, for a pointer ("read these documents before new work") that the table already provides. If wanted, it is a 10-line loop over the same corpus.

## Not done / limits

No live outage was available to exercise the retry; the 3 transport-failure and 32 HTTP 500 cases of IT15 were replayed only as successes. Dump unpacked size unmeasured. Open Targets, GtoPdb, DGIdb adapters not touched (no observed failure there). `status.json` still spends retries when down.

Files: `p3_measure.py` (stages identity, context, truncation, resume), `q5_reconcile_docs.py`, `test_p3.py`, the TSV outputs above, `failures_log.json` (empty list), `cache_SHA256SUMS.txt`. Adapter tests: `framework/scripts/test_repurposing_adapter.py` (class `ResilientTransport`).
