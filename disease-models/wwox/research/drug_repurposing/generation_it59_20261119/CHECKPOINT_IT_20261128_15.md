# Checkpoint IT40 (window 8424b293), 2026-11-28, written at 257,298 context (census, 123 turns, effort high)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119. Read this file only (`_14` holds IT39's close). Codex is never contacted. Worktree `it_40_20261128`, branch `task/it40-adv337c`.

## Done
* Bound (marker verified), main merged, effort high. Old window c817e528 released on request.
* **ADV-337 closed and accepted by ADV with the rate as three readings** (folder `advisor_pilot_20261113/brainstorm_20261116/adv337_repudi_it_20261128/`, `RESULT_ADV337_IT_20261128.md`): first reader 20 of 26 = 77 percent; second reader (sonnet, high; Suppl Figs rendered) 7 of 23 = 30.4 percent, 8 of 24 = 33.3 percent if S45 is N; IT40 adjudication of the 13 contested rows 9 of 24 = 37.5 percent; floor agreed by both readers 7 rows (S32, S02, S10, S38, S39, S44, S47). E1 rejected in every reading, E2 undecided (flips on S21 and S41). Never restate one figure. The class boundary W/Q moved 13 of 25 rows, not the facts.
* **S32 confirmed** (CLAIM 003 evidence-boundary line gives quantified myelin endpoints to the S-KO only): N-KO EM axon counts per field (Suppl Fig 5G; legend n = 3 per genotype, plotted points are fields; legend averages 148 ± 45 / 45 ± 26 / 195 ± 35 / 440 ± 210, plotted-point means 145.0 / 37.7 / 192.8 / 407.7) and Wwox-null CC1/PDGFRa (Suppl Fig 7F; WT v null, P17; legend n = 3 "three identical sections", unit ambiguous; bars only, values from geometry 188.8 ± 6.5 v 93.6 ± 8.6, 56.7 ± 6.2 v 87.6 ± 5.4, SEM). HE's blind ADV-338 table agrees cell by cell (no S-KO in either panel). **No CLAIM 003 edit made**: no decision changes, ADV waited for the comparison; proposed wording is in the RESULT section 2.
* **S45**: the second reader's unit lookup was stopped by a safeguard (not retried); IT40 judged W from the sentence text ("the same paper" = the Tc-MEP paper), unit not opened.
* Suppl Fig 6B: legend numbers swapped (S-KO 12 ± 4 v S-Control 7 ± 3 printed under "reduced"; bars control about 13, S-KO about 7). HE did not read this panel; whether it bears on RP-017 is ADV's call.
* **Receipt `FTR-20261128-33914858-41`** (complete_fulltext_read, the two mp4 supplements named unviewed: a temporary decoder fetch was refused by the classifier, not retried, ADV confirmed), manifest `PMID33914858.json` with locators 40 to 50 (from the second reader), **`BATCH_20261128_010`** MINOR (PAPER 004 now carries the complete-read marker; locator count in the record follows the manifest, 51). IT39/IT40 self-evaluation `session_evaluations/self_eval_orchestrator_it39_it40_20261128.md` (scout and takeaways inside).
* **Landed:** `BATCH_20261128_010`, the receipt and the self-evaluation are on `development/main` at `fe1c40bd2` (gate PASS on the exact SHA, verified by ls-remote; third attempt; the first two were refused by landing suites, see Traps). This checkpoint went out in a later push.
* CI: no completed gate run from #2928 to #2961 is red; #2952, #2953, #2955 and #2957 to #2961 were still in progress.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | The gate run of `fe1c40bd2` and of the checkpoint push: read any red from check-run annotations | open |
| 2 | CLAIM 003 evidence-boundary wording (S32) | the comparison is done; a later BATCH_COMMIT after `test_batch_queue`, or a dated pointer if none is queued; ADV decides RP-017 premise wording (S21 compartment-exclusion inference, S41 "no endpoint beyond that") |
| 3 | The two mp4 files | stop for the operator list: a decoder is needed (ADV recorded it) |
| 4 | ADV-286 dates | C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12; one BLOCKED calendar row |
| 5 | ADV's next candidate question after the comparison | neuron-dependence of myelin in a conditional model (S-KO reduced not absent plus N-KO counts): an RP-017 question owned by ADV |
| 6 | Predecessor worktrees | removable from 18:38Z by ADV (branch_hygiene); do not remove anything yourself; `it_39_20261128` holds 61 MB of ignored copies |

## Traps met
* A complete-read receipt on a registry record with no full-text marker is refused by `test_batch_queue` at landing: register the record by a MINOR BATCH_COMMIT first (`record_scoped_edit` ops through `batch_commit.py propagate`; a replace that moves line content across lines is refused as CROSS_LINE_MOVE, keep the edit in one line). Then a count of locators in the record ("N locator") must follow the manifest (`locator_count_crosscheck.py --sweep`; a phrase like "11 locators added" counts as an unparsed assertion).
* `pgrep -f 'safe_push.py development main'` matches every session's push, not only yours: wait on your own log (`PUSH_EXIT=` line in a nohup wrapper) instead.
* Merging main into a branch that already recorded a receipt conflicts on the ledger, the state anchor, ranking, coverage and reading state: restart from main (`git checkout -f -b new development/main`), copy the three own files, record the receipt again.
* The first reader counted every printed qualifier as Q; a second reader with the PREREG O definition and the frozen counterexample moved 11 rows to W. Next PREREG: test the class boundary on one row of each side before the reader runs.
* A one-line fix of my own: ADV-336's 42.9 to 10.9 is a WWOX immunosignal figure (knockout completeness), not a myelin figure.
* Context reached 257k by turn 123: whole-file reads of the first-reading table and sentences, and long tool outputs from `git`/`grep` on large registries; use `cut` and narrow greps.
