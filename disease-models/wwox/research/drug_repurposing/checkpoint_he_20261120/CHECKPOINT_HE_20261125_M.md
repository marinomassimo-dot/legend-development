# Checkpoint HE-M (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~03:44Z

Written for: the successor HE session (fresh window, launched by ADV from a detached worktree). Written above 360k context at ADV's request, after ADV-245 and ADV-252 closed. Read after `CHECKPOINT_HE_20261125_L.md`, whose section 3 (traps) still holds. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` for the counts. Kept as before: never write `MANDATE_STATE: COMPLETE`.
- Outgoing session `a930ffce-0106-435b-bf6b-1722dd96fba6` (worktree `he_k_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn.
- Operator rules unchanged from checkpoint K section 0. Reply to the operator in Italian, write files in English.

## 1 Done since L; do not redo
- ADV-235 closed: the two runs after the red night failed one suite each (#2313 `test_batch_queue`, #2317 `test_pathograph`), both repaired.
- ADV-243: `HE_RECORD_PATH_FRICTION_ADV243_20261125.md`. ADV decided the design (section 2, item 1).
- Root checkout refreshed at 02:49Z (133 dirty paths, 131 on main already, 2 were ADV's unlanded ADV-247). Backup `files/coordination/he_root_refresh_20261125/`. Assignments since ADV-189 read from root: executed 43 of 58, before 0. ADV now fast-forwards root itself in its hourly routine.
- `mandate_watch` on stale records: one resume sent since 11-20 (IT59, 11-24 07:39Z); main's record also had open work, so no wrong action was found; the message carried an old step count and the stale record path. Before 11-24 15:39Z only sends can be checked.
- ADV-245: DC-05 counter-evidence text repaired; EN-03 was a display defect in `scout_daily.py --plan` (queries unchanged); the coverage generation, stale since 11-18, was refreshed.
- Disk: 18 integrated, clean, unheld task worktrees removed without --force; free space 15 GB to 23 GB. Kept 19 (roster CURRENT and PREVIOUS windows, held, not integrated, or with ignored files held only there).
- ADV-252: main was red from HE's own ADV-237 test (`test_landing_suites.py`, closed-world guard), runs from #2322. Repaired by one justified ALLOWED entry (guard logic unchanged) and a `landing_suites.py` rule that selects the guard when a `test_*.py` in its three scopes changes. Published in f0daa021 (gate PASS). CI run #2353 was queued behind 23 open runs and has NOT been read: read it first (`ci_runs.py status f0daa021`).

## 2 Open, in order
1. **Campaign home (ADV decision, accepted with HE's caveat).** One registered checkout owns advisor ids: root. `assign` and `deliver` must refuse when a commit in `HEAD..development/main` touches an input. Inputs: `ledger/tasks/*/*.json`, `research_portfolio.tsv`, `roadmap_current.md`, `framework/protocols/cross_session_transport.md`, the shareable view package, the campaign folder, the tool's own code. Reword `roles/advisor.md` (first moves, line 51) and `.claude/skills/legend-strategic-advisor/SKILL.md` (lines about the primary checkout, near 169, 210, 240), add tests in `test_strategic_advisor.py`, ADV reviews. The code seat is `primary_refusal()`. If a write under `.claude/` is refused by the permission control, report it. The recall is re-created from the home by ADV.
2. 03:37Z `mandate_watch` run (first on current code), read: 114 checks, every action NONE, no log line added. Nothing to do.
3. Micro-upgrade proposal (ADV said yes, with consumer and about an hour): a staleness warning when `tick` or the watcher runs from a checkout behind main. Item 1 covers `assign` and `deliver`; the watcher and `scout_daily` from root are covered only by ADV's hourly fast-forward. Measured need: 1,535 commits of drift unseen for four days.
4. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
5. No retirement of old windows without asking ADV. No `--retire-old`.
6. Operator-owned and unapplied: workflow patches (checkpoint J section 3). The push-rule gap in LEGEND_CORE 21d/21e is ADV's to put to the operator: do not edit 21d or 21e.
7. `files/coordination/he_root_refresh_20261125/` (2.5 MB) may go once nobody has asked for it for a week.

## 3 Traps met in this window
- `strategic_advisor.py tick` writes state (it consumes pending events): it is not a read-only look at root. Use `assignment_states` or `status`.
- Root refresh recipe: back up with a sha256 list, move untracked aside (never delete), `git restore` the listed paths only, `git merge --ff-only --no-overwrite-ignore`. Never `reset --hard`, never `git clean`.
- `git worktree remove` takes about a minute per tree here: run the batch under `nohup`.
- A landing can be refused only because another landing regenerated the same views: merge, regenerate on the merged tree, never hand-merge generated files.
- A negative assertion in a test whose body names a registry path is flagged by the closed-world guard even when it reads no registry.
- A "before" figure printed by a plan is not the query sent: read the code before building on printed output (EN-03).

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file, then L and K.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The old window releases and renames; the successor renames nothing of its own.
4. Section 2 item 1; then `guidance`, `debt_report.py`, new ADV assignments. Before every push: `framework/scripts/landing_suites.py`, then `safe_push.py development main --expect-sha <sha> --serialize`.
