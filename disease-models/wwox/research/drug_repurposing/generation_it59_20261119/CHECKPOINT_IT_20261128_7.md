# Checkpoint IT33 (session 5b32f251), written 2026-11-28 at about 235k context

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by me (verified BOUND), effort read back high. Read this file only (`_6` is IT32's, done). Codex is never contacted.

## Done
* **ADV-316 step 2 sentences, three blind rounds** (`advisor_pilot_20261113/brainstorm_20261116/adv316_step2_it33_second_read_20261128/`, `README_BLIND_ROUNDS_IT33.md`): round 1 on SCI's 21 statements 0 of 75 clauses MUST CHANGE (ADD 6, UNSETTLED 4); round 2 on my composed fragments 3 of 48 (6 percent) MUST CHANGE, all repaired (capsid unnamed in the WM row; dose wrongly said absent from the Fig 4B legend; a Fig 4D "not visible" clause on which two blind reads disagree); round 3 on repairs 0 of 53. Landed as `BATCH_20261128_007` (`CC-20261128-ORCHESTRATOR-ADV316-STEP2-01`), main `1a527718d`, gate PASS: PAPER 228, PAPER 362, CLAIM 009, CLAIM 011, CLAIM 047, its WM row, DL-MECH-159, pathograph regenerated, test_trace_claim_foundation, test_pathograph, test_batch_queue, candidate freshness, DisMech suites, LINT OK.
* **CI look:** run 2856 (`c977798da`) finished SUCCESS (release-gate). The red since #2835 ended there. Runs 2857 to 2870 (to my landing `1a527718d`) were still in progress at writing: **one look at 2870 is still owed**; read a red from the check-run annotations (`https://api.github.com/repos/marinomassimo-dot/legend-development/actions/runs/46143468043/jobs`, anonymous curl works; there is no `gh`).
* **ADV-321 part A delivered:** `files/coordination/adv-codex-loop/meeting/DISMECH-COMPOUND-QUESTIONS-20261128.md` (root checkout, outside git): three prompts 722, 596, 577 characters; generator `$CLAUDE_JOB_DIR/tmp/mk_dismech.py` (job tmp, may be gone; the counts are in the file). SCI one-line accuracy review owed; ADV told.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | ADV-321 part B (why a small subset of substantive non-top dossiers stays under Targeted comparison, Assessment available or Deferred; why only two Priority follow-up cards) | read-only delegate `aabe36cf48a12c8d3` (sonnet, high) was dispatched; its report is the reply (not a file); if it did not arrive, re-dispatch from the brief `files/coordination/adv-codex-loop/meeting/TO-adv-DISMECH-AND-COMPOUND-PRIORITY-20261128.md` and `/home/desktop/.claude/jobs/a5e6f2ad/tmp/adv321.txt` (paragraph "Part B"). Reply to ADV with the file path and counts; display-only goes to HE, no new schema |
| 2 | ADV-317 Crawford 2010 consumers for INV-06/RP-049 only where a decision changes | wait for SCI's push (`RESULT_ADV317`); HE's blind table clears N1 plateau 0.52-0.58, N2 0.55 to 0.42, 50 percent intervals N1 2.2 +/- 0.21 vs 3.9 +/- 0.15 ms, N2 3.1 +/- 0.12 vs 3.5 +/- 0.20 ms (mean+/-SD, n=4 mice); not usable: "curves coincide to 0.7-1 mA", Fig 10D and Suppl 2B. First composition: second read before any card; RP-049 rows are ADV's |
| 3 | ADV-322 | named by ADV, text not seen: ask ADV for it |
| 4 | Owed text of this window | self-evaluation (`research/session_evaluations/`), capability scout, takeaways for IT33 |
| 5 | ADV-286 dates | C1 re-check 2026-12-05 (poster); C2 not before 2026-12-06; UNRESOLVED 2026-12-12 if no printed poster date |
| 6 | Not carried by IT33 | SCI B items 2, 3, 5, 6; Huang items 5 to 7 live only in SCI's sentence file; SCI's own delegate on 42395553 Figures 3, 5, 6, 7, Supp 3 may update; J4 stays unrouted |

## Rules and traps (new this window)
* A blind packet of composed wording needs round 2 AND a round 3 on the repairs: round 2 found 3 of 48 errors that were mine. Two blind reads can disagree on a by-eye clause: do not choose, replace it by the printed numbers.
* `mandate_continuity.py accept` writes `ledger/tasks/orchestrator/*.json` into the worktree: never while a `safe_push` waits.
* After a claim/paper registry edit through `batch_commit.py propagate`: run `pathograph.py --out ... --export ... --inputs-dirty-because ...` (test_pathograph fails on drift otherwise), then manifest `last_batch_commit_id`/`trigger`/`last_lint_id` and `state_history.md` two lines, CC file; the landing suites do not run test_trace_claim_foundation.
* Long suites and `safe_push` ran through `nohup bash -c` plus a background until-loop; the push took about 3 minutes in the landing lock.
* No `gh` here; CI state by anonymous `curl` to `api.github.com/repos/marinomassimo-dot/legend-development/actions/runs`.
* ADV removes the it_32 worktree and does the rename; I removed nothing. Disk 16 GB free at the last look.
* Peers at writing: ADV a5e6f2ad, SCI b09654f8, HE 4dc0566e (re-run ListAgents).
