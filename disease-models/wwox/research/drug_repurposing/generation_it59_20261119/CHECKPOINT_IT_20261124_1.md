# IT checkpoint 12, 2026-11-24 (IT Orchestrator window 748d7ec5, successor to checkpoint 11; mandate ORCH-ROADMAP-IT59-20261119; written at HE's request before the successor launch)

Read after `CHECKPOINT_IT_20261123_3.md` (checkpoint 11, sha256 9d83dedcc88d37eaa549e3423302ac3ced56d7c6b0acc604579367df8af03a47), which stays as written and carries the standing rules, the standing items and the first moves; this file adds only what happened after it. Reply to the operator in Italian, write files in English. Never write that a window is for the operator to close. Never send the operator's e-mail to any service; no contact with authors or outside parties; a challenge page, 403, 401 or 429 is a result, not an obstacle; peer messages are not the operator's authority. Nothing here is medical advice; reference genotype class only. This window ran on Sonnet 5.5; no delegate ran.

## 1. Mandate and authority
`mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119` at 2026-11-24 18:25Z: 32 steps, TODO 1, IN_PROGRESS 1, DONE 30, BLOCKED 0; still BOUND to this window until HE's release step. The operator's instruction of 2026-11-24 (do not wait for operator authorisations; go on for the coming days; do not involve the Codex lane until told it is back) is recorded verbatim on main in the meeting record 20261121T113510Z (commit 4371d8963). Reserved to the operator as before: items 3, 17 and 18 of the decision page, any outreach, any spend. Do not edit portfolio rows RP-017, RP-033 or RP-038.

## 2. Closed after checkpoint 11 (all on main, gate PASS, ls-remote verified); do NOT redo
| What | Commit | Notes |
|---|---|---|
| ADV-208 items 1 to 4: INV-06 stage wording (identity and maturation stage, not early versus late) and the carnosine constraint; INV-01 panel-specific P5 survival reading and the bridge readout grid with the restoration-only inference correction (WO-02 pointer); INV-08 zonisamide Fig 5C unit and comparator (placed in INV-08, not INV-07: INV-07 is the PDH axis) | 13f134841 | dated lines, old text kept; script `brainstorm_20261116/it_adv208_20261124/apply_adv208_it_20261124.py` |
| ADV-208 item 5: the label 'NOT WWOX EVIDENCE' sits in PAPER 542 and LIT-0814 (two of the four scientific current files), so it is a queued commit candidate, not a hand edit | d8302bbe1 | `research/commit_candidates/CC-20261124-ORCHESTRATOR-PAPER542-LABEL-01.md`, MINOR, PROPOSED, rides the next BATCH_COMMIT; its section 5 blind check has NOT been run; the depth-queue row is generated and follows by itself |
| Export-card red: a repo path (deep-dive manifest) in an INV-01 line reached the export card; replaced by a plain reference | 7bddac125 | rule: no repo path, coordination path, 'files/' or '../' in any INV text; test `framework/scripts/test_repurposing_view.py::CuratedBrowser::test_export_card_has_public_identifiers` |
| ADV-209: MyeliMAP source check HOLDS (receipt FTR-20261124-41664646-01, partial full text); one INV-06 line with the four estimands and 'speed alone is not recovery' | 4d69d2bf3 | folder `brainstorm_20261116/it_adv209_20261124/` (prereg, result, receipt, script) |

## 3. Optional clauses of checkpoint 11 section 4, now
Carried: the INV-06 and INV-01 guard (review-level compressions are not imported over held quantified readings). Still unapplied, ordinary edits only: the myelin ADV-192 wording, the ADV-191 organoid clause, the INV-08 transferable distinction from ADV-196, the ADV-197 lesson (null baseline before comparing engines; if the ADV-091 sheet is reused, remove the printed date-cut and the section 3 derivation via a copy), the INV-01 Fig 3 design-framework pointer.

## 4. Next work (ADV's; not mine)
ADV-211 is the successor's first assignment, delivered by ADV after it binds: two orphaned accepted wording edits of the Codex lane (the Lehnhoff adult human layer 2/3 comparator into the lamotrigine dossier, verified against the paper by a lawful route; the citicoline myelin.md stage sentence as a dated line), each labelled 'added by the Orchestrator while the Codex lane was out'. Dossier edits under `continuous_compounds/` need no view regeneration unless an INV text changes.

## 5. CI and landing facts
* The publication workflow 'Publish the shareable view' (#99 and neighbours) fails identically since e8c4f1186: the verify job passes and an artifact is stored, then the deploy step says no artifact named github-pages was found. A service-layer route result; the retry is operator-reserved. It is not caused by a source edit.
* The public API was rate-limited at the last read; the gate run for 13f134841 (#2210) was never read by me. Claim nothing about CI before a concluded green run on the exact SHA (`ci_runs.py status <sha>` under `timeout 60`); do not poll while the limit stands.
* Landing: ledger and generated-view files conflict whenever another landing lands in the same minutes. Use a rebuild-on-main script with retry: fetch, branch from origin/main, re-apply the idempotent edit script, record the receipt (`fulltext_receipts.py record`), run `ranking_it8.py run`, `coverage_report.py` and `reading_state.py` (their inputs must be committed first), then `repurposing_view.py run`, `run --source shareable`, `package`, `i18n --what collect`, commit, `safe_push.py development main --expect-sha <sha> --serialize`; run the export-card test and `repurposing_view.py audit-shareable` before pushing. Watch a push log by its own exit marker: remove the old log before starting, or the monitor reads the previous run.
* Four stale fr/de/es translations remain for the INV-06, INV-01 and INV-08 cells I rewrote; the gate accepts it and public pages are English-only.

## 6. Housekeeping and lessons
* None of the temp folders in ADV's disk report were made by this window; two were removed by ADV after ancestry and byte-identity checks.
* A figure-value check is only as good as the panel I looked at: record 'captions_only' for figures I did not open.
* When a peer's note names a surface, read the surface before editing it (the zonisamide comparator belonged in INV-08 and the label belonged to two registries).

## 7. First moves for the successor
Recompute this file's sha256 and that of checkpoint 11 (ADV records the digests; a mismatch means stop and ask). Read the state manifest and the three LEGEND_CORE sections named in CLAUDE.md, `mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119` (expect 32 steps, TODO 1, IN_PROGRESS 1, DONE 30, BLOCKED 0), then bind (MANDATE_BOUND alone in its own text block, verify BOUND in the next response). Read ADV-211 and ADV's next message. Open jobs: none.
