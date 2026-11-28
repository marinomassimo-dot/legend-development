# Checkpoint IT38 (session 1eb17530), written 2026-11-28 at about 210k context (measured peak 200956 a few turns earlier)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by IT38 (verified BOUND), effort high (sonnet 5.5). Read this file only (`_11` is IT37's, done). Codex is never contacted.

## Done, on main
* IT37's self-evaluation (`self_eval_orchestrator_it37_20261128.md`); IT38's own (`..._it38_...`).
* PMID 31829254 complete read: `FTR-20261128-31829254-02`, `PAPER 571` (was corpus stub 197), `BATCH_20261128_009`, `adv333_cross_it_20261128/RESULT_ADV333B_COMPLETE_READ_IT38_20261128.md`. Published `f54a92508`.
* Report sent to ADV: two edits to the RP-017 line (no "adult"; read now complete) and a proposed next question.

## Open
| # | Item | State |
|---|---|---|
| 1 | ADV's answer on the proposed antibody-and-control question | waiting; if accepted, freeze a PREREG first |
| 2 | CI | 15:56Z: runs >= 2917, 12 success, 12 in progress, 0 failure; red is read from check-run annotations |
| 3 | ADV-286 dates | C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12 |
| 4 | Old IT worktrees | removal is ADV's or by `branch_hygiene.py --removal` with no reason; IT38 removed none |

## Traps (new this window)
* A new worktree has no `files/`: copy the source artefacts into its ignored `files/` before `fulltext_receipts.py record`.
* A complete receipt rejects an optional coverage key set to `not_read`, a string `schema_version`, quotes under 30 characters, and waived `group_assessment` / `field_density`.
* The publisher image host answered 403 today; the PMC open-access bucket served the figures.
* `candidate_tree_freshness.py --regenerate --repo .` regenerated and committed the stale surfaces in the worktree in one step; `repurposing_view.py check` then said current.
