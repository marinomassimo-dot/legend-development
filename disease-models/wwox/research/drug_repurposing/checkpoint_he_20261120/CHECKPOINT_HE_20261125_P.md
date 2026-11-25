# Checkpoint HE-P (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~09:35Z

Written for: the successor HE session. Written at ADV's request (context 289k at 09:22Z, real and this window's own; ADV launches the successor). Read after `CHECKPOINT_HE_20261125_O.md`; the traps of M section 3 and N section 3 still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` for the counts. Never write `MANDATE_STATE: COMPLETE`.
- Outgoing session `00c83fd0-b922-4fc1-8c59-c018dc22d605` (worktree `he_o_20261125`, branch `task/he-p-20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Reply to the operator in Italian, write files in English. Operator rules as in the brief (`HE_BRIEF_TEMPLATE.txt` in this folder).
- Peers at writing: ADV `a5e6f2ad`, SCI `48889001`, IT Orchestrator `0d3f20fd` (re-run ListAgents).

## 1 Done since O; do not redo
- `window_handoff.py rename` matched the whole row, so the old window's summary ("successor he_o_20261125 launched") was taken for the successor's row. It now matches the name column only and stops, naming it, if any other row changes name (44a7debda).
- Krug 2013 `.xls`: nothing to install; `python3 -I` hides the user-site `xlrd`, `python3 -P -E` sees it. `xlsx_to_text.py` reads `.xls` (01263a214). 12 of 12 held BIFF files open; the thirteenth held `.xls` (PMID 24932569) is a saved reCAPTCHA page (SCI told).
- CI visibility: the runner publishes the 15 slowest suite times as a `suite time` notice; `ci_runs.py times <sha>` reads it (670251825). No workflow file touched; verdict path gains two print calls.
- `test_paper_packet` speed-up: no gain visible in CI (test/gate step ratio 10.45 before, 10.5 after); recorded in the suite's own note.
- `landing_suites.py`: three rules for the two reds that escaped it, #2353 (needs.json) and #2404 (a card) (555d81c09, e982b57c2). A change to `view/source_titles.json` also selects the `Titles` class (0e767b304); the long view suite stays unselected, and no rule exists for a PMID in a map line (no evidence in #2404).
- Branch hygiene: two `codex/*` commits exist on this host only. A backup push was refused (LEGEND_CORE §21d: no backup branch is pushed); ADV withdrew it.

## 2 Open, in order
1. Per-suite CI times: the first run holding 670251825 is #2428 (f093ab03). `python3 framework/scripts/ci_runs.py times f093ab03b937bea17e959abf8ce0308a61387da1` once it concludes; send ADV the suites that hold the time (ADV asked which ones hold the 50 to 88 minutes). The runner is red until IT's fix 973fa172c lands; the notice is printed on red runs too.
2. Ledger-index CI effect (49a9dd56): first two runs give test/gate ratio 7.7 (#2416) and 8.4 (#2417) against 10.2 to 11.1 on the red runs just before; sent to ADV. More runs would tighten it; the step is closed. Method: job steps through the public API, `Regression tests` divided by `Public release gate` of the same job (the gate does not read the receipt ledger).
3. Red main since #2404: IT's. At 09:33Z 973fa172c was not on main; ADV asks HE to verify its CI run once it lands (`ci_runs.py status <sha>`).
4. Operator question, open, unanswered: authorise a one-off backup push of `codex/wwox-continuous-compounds-20261123` (313a5438a) and `codex/meeting-cross-runtime-20261123` (9807a24e8)? Without an answer they stay local; delete nothing. ADV queues SCI's port of the lamotrigine lines.
5. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/` (sealed, outside git).
6. `files/coordination/he_root_refresh_20261125/` may go once nobody has asked for it for a week.
7. Operator-owned and unapplied: workflow patches (checkpoint J section 3). Do not edit LEGEND_CORE 21d or 21e. No `--retire-old`; no retirement of old windows without asking ADV.

## 3 Traps met in this window
- The unauthenticated API gives 60 requests an hour, shared by every waiter on the host; each job read is one.
- CI step times fall in several runner speed classes (gate step about 280, 340 to 390, or 500 s): compare only after dividing by the same job's gate step.
- Large listings (the agents view, run lists, file dumps) took this window to 289k in under an hour: print counts and the rows you need.

Mandate status at writing: every step DONE.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file, then O.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames (`window_handoff.py rename`); the successor renames nothing.
4. Section 2 items 1 and 3; then `guidance`, `debt_report.py`, new ADV assignments. With none, tell ADV and propose a measured upgrade. Before every push: `landing_suites.py`, then `safe_push.py development main --expect-sha <sha> --serialize`.
