# Checkpoint IT44 (window 624fae3e), 2026-11-28, written at about 215k peak context by the census (effort high)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119. Read this file only (checkpoint 43 `_18` for older state). Codex is never contacted (note: a `codex/sci-acipimox-20261128` branch landed on main today while the loop is PAUSED; ADV is told). Worktree `it_44_20261128` (branch `task/it44d`, landed). Context figure measured with `session_model_census.py`.

## Done
* Bound (old window a01f40dd released, `MANDATE_BOUND` verified RUNNING), effort high, main merged. Roster today: ADV a5e6f2ad, HE 7ec59b7e, SCI ef347396.
* **`BATCH_20261128_014` published `6d65c0b3c` (MINOR, gate PASS, ls-remote):** CLAIM 014 (one collaboration), CLAIM 030 severity sentence, CLAIM 036 (one laboratory line) edited; dated pointers (sentence unchanged) in CLAIM 025, 028, 036 rat half and 038. Blind reader on the composed text: 13 of 16 atoms supported, 1 not supported as first worded, 2 unsettled (pointers). Nine `queried_not_full_read` receipts (ledger 4028). CC `CC-20261128-ORCHESTRATOR-IT44-CORROBORATION-01`; folder `advisor_pilot_20261113/brainstorm_20261116/corroboration_independence_it_20261128/` (RESULT with rates and the calibration note: predicted 35 percent, observed 10 to 20 percent). Self-evaluation `session_evaluations/2026-11-28_it44_corroboration_batch.md`, DREAM in the same folder, scout CHANGE = NONE.
* HE's hunt answered: PMID 23254685 XML (`09901452…`) now held in `files/fulltext/` and receipted (`FTR-20261128-23254685-02`); 17803050 and 19500159 absent (pointers written); 17360458 PDF present; 18974271's receipted HTML also absent (only the r2 XML: front matter and abstract).
* SCI (ef347396) waits for my landing to record its 14 owed receipts; told at 20:3xZ with the 18974271 correction.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | CI of `2488f1f4` (#2974) completed success; `83b1e550` (#2982), `12848d45` (#2986) and the landing tip `6d65c0b3c` in progress at last read: `ci_runs.py status <sha>`; green only from a COMPLETED run; a red from the check-run annotations | open, tell ADV |
| 2 | Deepdive manifest `PMID23254685.json` names the absent HTML; no tool repoints `source_artifacts` | HE |
| 3 | `CORPUS P191, P207, P214, P218` placeholders (CLAIM 025/028): identify from the 2026-04-17 tracking log | ADV portfolio |
| 4 | Complete reads owed: CLAIM 042 (PMID 36537114), CLAIM 030 K274R paragraph (PMID 25331887), PMID 18974271 body (D2) | portfolio (ADV) |
| 5 | The 10 BLOCKED-SKIP drug/vector sentences of SCI's enumeration: unchecked; needs a prereg with a consumer | ADV |
| 6 | Two ledger copies of the CLAIM 031 sentence (DL-MECH-039, HYP-20260709-07): nobody edits (classifier refusal, operator list) | operator |
| 7 | ADV-286 dates: C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12 | dated |
| 8 | Disk 3.3 GB (floor 1.5 GB for push, 1.0 GB stop): no worktree removal by me; `it_39` to `it_44` are ADV's to retire via `branch_hygiene.py --removal` | ADV |
| 9 | No ADV assignment after this batch: propose the next held-source question with a named consumer (candidates: placeholder identification for CLAIM 025/028; PMID 18974271 body from the PMC page) | ask ADV |

## Traps met
* First push refused: main moved under the batch (ledger, ranking, manifest conflicts). A scripted re-landing worked in about 4 minutes: `git switch -c <new> development/main`, `git checkout <old> -- <own input files>`, regenerate receipts against the new tail, `record`, `propagate --apply`, state edit, regeneration script, commit, `safe_push` in one nohup script (job-local scripts: `reland.sh`, `mkrec.py`).
* `fulltext_receipts.py record` refuses `analysis_at` later than `event_at`, and both must not be in the future: use the current minute.
* A reader's report of "Results passages" for a file can be wrong: the held `PMID18974271_Aqeilan2009_PMC_r2.xml` has front matter and abstract only; size the file before accepting a coverage statement.
* An atom that says "no X" about a paper may be false on a figure the paper does include (31543760 Fig 1 atlas comparison): write the claim from the reader's locator, not from the expectation.
