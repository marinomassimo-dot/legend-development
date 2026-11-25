# Checkpoint HE-O (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~08:13Z

Written for: the successor HE session. Written at ADV's request after the window-handoff tool and one micro-upgrade closed. Read after `CHECKPOINT_HE_20261125_N.md` and its addendum; M section 3 and N section 3 (traps) still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` for the counts. Never write `MANDATE_STATE: COMPLETE`.
- Outgoing session `70b134a9-f886-4004-a66a-61c52a560d8b` (worktree `he_n_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Reply to the operator in Italian, write files in English. Operator rules as in the brief (`HE_BRIEF_TEMPLATE.txt` in this folder).

## 1 Done since N; do not redo
- N addendum condition 2: three real pushes in the `safe_push` row of `framework/scripts/README.md` (step 24, 25, 25 s of 254, 249, 275 s; all nothing stale), ff89f20f7. The step runs in the copy of the tool the publisher started.
- ADV-267: `framework/scripts/held_studies.py` counts held studies by file name and by receipt SHA-256; `debt_report.py` prints the line; 1a26ad91a. On SCI's ledger it equals ADV-264 study for study (670 held, 421 not held; 314 of the 421 carry no digest at all). The index cache is in the host state folder.
- `test_paper_packet`: five cases read one check run; 702 s to 347 s on this host; 576abf926.
- `framework/scripts/window_handoff.py` (`prepare`, `rename`, `verify`); b2393300d. ADV's IT rename was its first live save, both proof lines OK. It never starts, stops or retires a session.
- Receipt-ledger sequence rules indexed by PMID and DOI: `load_ledger` 6.99 s to 0.23 s; equal error lists on the real and 600 altered ledgers; byte-identical `verify` output. `test_phase_handoff` 312 s to 88 s on this host; 49a9dd568.
- CI: #2386 (772fee674, default regeneration) completed SUCCESS.
- Disk: removed `he96` and `it_adv246/248/250/251` worktrees (IT confirmed its four); 21 GB free at 07:07Z.

## 2 Open, in order
1. CI effect of 576abf926 and of the ledger change: ADV asked for the measured number. #2405 (576abf92) was in progress at 08:10Z; the first run holding the ledger change is the one of 49a9dd568; take the suite durations or the run duration from `ci_runs.py status <sha>` and the queue view, compare with neighbouring runs, send ADV. Runs took 70 to 110 minutes this morning with about 20 in parallel, so a single run's wall time is a noisy comparison.
2. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
3. `files/coordination/he_root_refresh_20261125/` may go once nobody has asked for it for a week.
4. Operator-owned and unapplied: workflow patches (checkpoint J section 3). Do not edit LEGEND_CORE 21d or 21e. Pages failures are operator-reserved.
5. No retirement of old windows without asking ADV. No `--retire-old`.

## 3 Traps met in this window
- `cProfile` inflated one ledger load from 7 s to 42 s: report a time only from an unprofiled run (I told the operator 42 s first and had to correct it).
- `du` on `/tmp` counts hard links: a 61 GB folder held 0.47 GB of its own.
- Disk was above the 15 GB trigger when ADV asked for a cleanup; the report found one idle candidate plus four of IT's. Ask the owning live window before removing its task worktrees.
- Slow suites: `python3 <suite> --durations 20` shows repeated work. `test_phase_handoff` spreads its time over many packet builds; see the ledger change before optimising it further.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file, then N and its addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames (`window_handoff.py rename`); the successor renames nothing.
4. Section 2 item 1; then `guidance`, `debt_report.py`, new ADV assignments. With none, tell ADV and propose a measured upgrade. Before every push: `landing_suites.py`, then `safe_push.py development main --expect-sha <sha> --serialize`.
