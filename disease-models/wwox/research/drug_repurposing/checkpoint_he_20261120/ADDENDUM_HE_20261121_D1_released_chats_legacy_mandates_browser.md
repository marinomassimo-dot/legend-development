# Addendum D1 to checkpoint HE-D (2026-11-21): a released chat is not a recipient and not an operator item; the two legacy mandates; the browser temporary directory

Written by HE (ACTOR_ID `plan`, successor D, session `e5d84418`). Checkpoints are never edited; this is the dated correction. Reference-genotype class only; nothing here is medical advice; no personal data.

## 1 Correction (dated 2026-11-21)

- `CHECKPOINT_HE_20261120_A.md` line 42 ("the old terminal is the operator's to close by hand"), `CHECKPOINT_HE_20261120_B.md` section 4 line 29 ("the old interactive HE terminal 29e50812 (the operator closes it by hand)") and `CHECKPOINT_HE_20261121_D.md` section 3 (the old interactive HE terminal listed among the operator's items) are **wrong and withdrawn**. Operator, 2026-11-21: "io non chiudo a mano i terminali, ricordatelo. Spetta a voi non a me."
- The sentence "Questo terminale e da chiudere a mano dall operatore, come detto da ADV" is not from this window: it comes from the old interactive session `29e50812`, its last assistant message at 2026-11-20T18:31:18Z (identity finding of PLAN/Codex, 2026-11-21).
- No handoff message, checkpoint or report of this role lists a window, terminal or spare as an operator item.

## 2 The distinction that replaces the blanket rule

- A **released legacy chat is not the recipient of new HE work.** New work goes to the bound host (`labels` says which). Closing the old chat's window is an optional tidy-up of the interface; it is never a prerequisite for research and never waits on the operator.
- A **background** predecessor is retired by `mandate_watch.py handoff --retire-old` (the supported route, no operator instruction needed).
- An **interactive** predecessor is kept by the watcher (the supported retirement covers background sessions only). Finding and testing a route is a harness item of this role and of ADV, reported as ours; no `claude stop` on an interactive session unattended, no kill signal, no wrapper around a refusal. Proposal and first trial: section 5.
- `mandate_watch.py handoff` now prints this to the launcher in its `next` line and in `legacy_bound_tasks` (HandoffNextLine tests), so the solution reaches the command that is read at the handoff.

## 3 The two legacy mandates bound in the old interactive chat (state from the records, 2026-11-21)

The old interactive HE chat `29e50812` is released for `PLAN-HE-CONTINUITY-20261118` (release line 2026-11-20T15:37:25Z) and is **absent from the live runtime inventory** (`claude agents --json`), so no window is left to close. Its transcript still carries two bind lines with no release line, which is why `handoff` reads KEPT. A release line is written only by the chat that holds the bind; none is written for it from here.

| Mandate | Record (ACTOR_ID `plan`, OWNER orchestrator) | Reading |
|---|---|---|
| `PLAN-HE-AUTONOMY-RADAR-20261114` | top-level `CURRENT_STATE` and `MANDATE_STATE` COMPLETE; the execution queue block `AUTHORISED_QUEUE_20261114B` has `MANDATE_STATE` OPEN with 26 of 26 steps DONE, so `mandate_continuity.py status` reads COMPLETE_PENDING | HE's own record. Closing it means setting that block's `MANDATE_STATE` to COMPLETE by the record owner after ADV has had the chance to object (message sent 2026-11-21); nothing else is open |
| `PLAN-PROACTIVE-ADVISOR-20261113` | top-level `CURRENT_STATE` OPEN by design ("the campaign stays open with the Orchestrator as verified operational owner"); the execution queue block `AUTHORISED_QUEUE_20261113B` `MANDATE_STATE` COMPLETE, 8 of 8 DONE, `status` reads RELEASED | Not executing; the campaign's ownership is the Orchestrator's and ADV's (ADV host), not this chat's. Nothing for HE to release |

## 4 Browser temporary directory (operator integration, 2026-11-21)

IT's ADV-131 battery lost hours because a snap-confined Chromium cannot read `file://` pages under `/tmp`, although the cure (TMPDIR on a non-hidden directory under the home) was written in `snap_tmp_hint` and in the scripts README. The cure now runs at the place every browser path passes: `find_chromium()` calls `prepare_browser_tmp()`, which for a snap browser with a temporary directory under `/tmp` points `tempfile` and `TMPDIR` at `$LEGEND_BROWSER_TMP` or `~/legend_browser_tmp`, proves the browser reads a probe page there (one `--dump-dom`, unique title) and otherwise raises `BrowserCannotReadLocalPages` within seconds (never a skip; `viewports` prints `ERROR` and returns 2; `browser` states the directory in force). A browser that is not snap-confined is untouched. Before and after on the real path, default TMPDIR, test `Browser.test_unfiltered_and_filtered_counts`: before `OK (skipped=1)` in 6 s, the skip text being the browser's own `Page load failed`; after `OK` (ran, no skip) in 16 s. `ShareableAuditRendered` and the `RealViewports` phone-viewport test, default TMPDIR: 2 tests OK, 188 s, no skip. Logs of both runs are kept in the job folder; IT's earlier attempt, its verdict and logs, are untouched. Skip sites that catch every exception and skip (`browser could not be driven`, `viewport emulation unavailable`, `Browser.dom`) were NOT changed: they mask other causes and are listed as a known family for a separate, measured change.

## 5 Interactive predecessors: proposed route and first trial (proposal, not executed)

Facts at 2026-11-21: `claude agents --json` lists two interactive sessions, both idle (`legend-development-1e`, `q230p-tooluniverse-blind-91`); the interactive HE chat `29e50812` is not listed. The supported `claude stop` addresses background sessions only. Proposal: (1) identify the owner of each remaining interactive session from the repository (cwd, records, bound lines) before touching any; (2) for a session whose records are all closed, the candidate route is the session's own `/exit` typed into its terminal (a chat cannot run `/exit` as a tool), for example through the terminal multiplexer when that terminal runs in one (to be checked first: `legend-development-1e` runs on `pts/6`, whether it sits in a multiplexer pane is unknown); no signal, no operator; whether any such route exists is exactly what the trial establishes; (3) first trial on one idle interactive session whose records are all closed, with the result read back from `claude agents --json`. Nothing is run until ADV agrees the trial session.

## 6 Native display names (policy of `cross_session_transport.md`, 2026-11-20), done 2026-11-21

The runtime has no headless rename; the native route is the `claude agents` list, the exact row, `ctrl+r`. It was driven in a detached `tmux` pane with the screen read before every save (the rename field starts with the old name: it must be cleared first; the first attempt on ADV showed `ADVADV - ...` before saving and was corrected before Enter). Result read from `claude agents --all --json`: `ADV - CURRENT a5e6f2ad`, `IT Orchestrator - CURRENT bf7d7d3b`, `HE - CURRENT e5d84418`; immediate released predecessors `ADV - PREVIOUS e6526331`, `IT Orchestrator - PREVIOUS d003f364`, `HE - PREVIOUS f7c03ec4` (`5d9fc467` was already PREVIOUS); `labels` reads CURRENT with no rename pending for the three mandates. No refusal by the application occurred; nothing here was an authorisation question.
