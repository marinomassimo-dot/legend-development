# Checkpoint HE-S (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~13:05Z

Written for: the successor HE session. ADV asked for the handover at this closed increment (this window's context 335k). Read after `CHECKPOINT_HE_20261125_R.md`; the traps of M, N, O section 3, P section 3, Q section 3 and R section 3 still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `4fab51c6-05e4-4bad-b5d1-cdc5d9dfae45` (worktree `he_q_20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status` (145 steps, all DONE, `COMPLETE_PENDING` on purpose). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `48889001`, IT Orchestrator `5fef7cc4` (re-run ListAgents; names roll over).

## 1 Done since R; do not redo
- Radar reader, one page, ADV-agreed: `HE_RADAR_READER_20261125.md`, with the correction of one identifier (41757738 is not the knowledge-graph paper; 42614934 is). ADV routes the four unread leads to SCI.
- View suite per test, and the one change: the A4 print test measures print only (`HE_CI_MINUTES_GATECACHE_20261125.md` section 5): 111 s to 19 s, a widened print page still fails it.
- CI #2444 (join fix, ba0ff95a): success.
- Push cost of the refusal, sent to ADV: last 3 landings, suites median 51 s of a 301 s lock hold (17%); 13 live landings 11:21 to 12:40Z, median 50 s, max 152 s; no live refusal.

## 2 Open, in order
1. **CI #2461** (commit 8302bfbe51b32d96d328a5fa8a77f50f2abb70e3): ADV wants the verdict when it closes (`ci_runs.py status <sha>`).
2. **Read after 2026-11-26 11:21Z** (ADV): the refusal prediction (section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`), and **how many CI reds in that period were on suites the default selection DID run**. ADV: that is the only number that decides whether the rule stays.
3. CI effect of the two test changes: per-suite times in a run holding 094935cd (`test_repository_surface_determinism.py`, against 758 s) and in a run holding the A4 change (`test_repurposing_view.py`, against 996 s). One run each; differences under about 100 s say nothing.
4. **Orphaned headless browsers** (found, not acted on; a candidate micro-upgrade to propose to ADV): at 13:00Z the host held about 290 Chromium processes, 1.7 GB proportional set size, in trees whose parent is gone, some six days old, under several worktrees (`p022b`, `he_g_20261123`, `adv_successor_a_20261120`, removed worktrees) and one from the replay folder of HE `9229d112`. The cause to look at: the view tool's browser class leaves the browser running when its Python process is killed or times out. Only processes shown to be one's own were stopped (two, both of this window).
5. Operator question, unanswered: the one-off backup push of the two `codex/*` branches (HE-R section 2 item 6).
6. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/`. The rest of HE-R section 2 items 7 and 8.

## 3 Traps met since R
- A script that drives the view tool's browser must call `find_chromium()` before it creates its temporary folder: under `/tmp` the snap browser cannot read the page, and each view waits 90 s for nothing.
- A title cut from a radar `Detected` line must be split on `; [` first: an entry without a date joins the next one and pairs a title with another hit's address. Check every identifier against the source before sending it on.
- A shell call that mixes `sed -i`, heredocs, `$(...)` fallbacks and `nohup` can be refused by the built-in safety check as unreadable. Write script files with the Write tool and keep the shell lines plain.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 items 1 and 2; propose item 4 to ADV if it assigns nothing.
