# Checkpoint HE-V (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~18:50Z (context past the restart line; ADV asked for it at 18:40Z)

Written for: the successor HE session. Read after `CHECKPOINT_HE_20261125_U.md`; the traps listed there and in M to T still hold.
Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `2140fbda-f284-4405-9299-c41ff651bdc9` (worktree `he_u_20261125`, branch
  `task/he-u-held-files-joins-20261125`), model `claude-sonnet-5-5`, effort `high` on every turn read.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. At writing:
  159 steps, 157 DONE, 2 TODO (section 2 items 1 and 2). Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English. Operator rules as in `HE_BRIEF_TEMPLATE.txt`.
- Peers at writing: ADV `a5e6f2ad`, SCI `a25686e1`, IT Orchestrator `9945c156` (re-run ListAgents; names roll over).
- ADV's line for HE (2026-11-25 18:40Z): one measured step per window is the right size.

## 1 Done since U; do not redo
- **Privacy-scan reads, 3 of 3 identical** (old script against landed, whole output, 31 finding lines, PASS):
  b11fa45ca 193/85 s, 0f0e64ddc 200/131 s, f9f550d75 245/174 s. Step closed.
- **ADV-279 defect 1:** `framework/scripts/held_content_check.py` plus one line in the save step of `find-fulltext`
  (the edit under `.claude/` was accepted). 61 of 11,322 held files unusable; no receipt names any. The first report
  said 34 of 6,270: the extra 27 are text formats that pass did not scan (26 `.html` bot pages, 1 empty `.xml`).
- **ADV-279 defect 2:** `framework/scripts/consumer_count.py` (the corrected rule; the frozen ADV-265/279 scripts are
  untouched). 1,272 joins to 1,237; note `HE_CONSUMER_JOINS_20261125.md`. SCI and ADV have the result; the corrected
  order is `files/coordination/he_adv279_defects_20261125/new_order_eligible.tsv`.
- Published: 9e39bbfcdb5594b4233779b111da291262d0f603 (gate PASS, `ls-remote`), then this checkpoint.
- **Landing-slot profile**, report only: `HE_LANDING_SLOT_PROFILE2_20261125.md`.

## 2 Open, in order
1. **Read after 2026-11-26 11:21Z** (the one TODO step): the refusal prediction of section 6 of
   `HE_CI_MINUTES_GATECACHE_20261125.md`, and how many CI reds in the period were on suites the default selection did
   run; selector gaps counted apart. ADV: that number decides whether the rule stays.
2. **Concurrent lock stages: ADV GO (about 18:52Z), the successor builds and trials it.** Measured once: view
   checks, gate and landing suites together 177 s against 281 s. Median hold 250 s, gate 101 to 124 s. ADV's
   conditions, all five:
   1. the suites move to a throwaway clone made with the battery-clone recipe (`git clone --no-hardlinks`,
      hard-link only `files/`; not `cp -al`), removed by the script itself on exit and on failure; state its disk
      cost in GiB (about 21 GB free);
   2. three repeat trials before it becomes the default, each with gate verdict and finding lines byte-identical
      to serial, and the suites' result set identical (same failing names, none only in parallel). Any red that
      appears only in parallel stops the change (the `test_verify_run.py` race precedent);
   3. a flag to run serial (the opt-out leaves the trailer, as the landing-suite flag does) and a NOTICE until the
      first ten landings are read;
   4. land it ALONE, no other change in the same push;
   5. the ten-landing read counts minutes of lock held before and after, from the log. ADV counts the expected
      saving (about 1.7 min per landing) only after that read.
   The gate reads the live worktree in `staging` mode: that is why condition 1 comes first. Scripts of the
   measurement: `files/coordination/he_landing_profile2_20261125/`.
3. **Open limit:** the consumer count misses author-year mentions (the working model cites PMID 42137291 as
   "Thomsen 2026"); portfolio rows are single long lines and an agenda-style mention inside one still counts.
4. Seen, not touched: `files/files` is a symlink to `files/` itself (2026-11-13 20:42Z); recursive globs follow it and
   list files two or three times. One tracked record mentions the path
   (`session_evaluations/2026-10-22_repurp_10h_r2b_b.md`). Removing a symlink loses nothing, but check who writes
   through it first.
5. From U section 3, unchanged: disk removals are ADV's (`he_o`, `it_17`, `it_18`, `sci_ag`, `it_fu` after 2026-11-26
   about 10:40Z; `it_19` after about 15:40Z); 2026-11-29 recheck and delete `files/adv174_negraes_custodian_he/`;
   operator list carried by ADV; patches of checkpoint J section 3 stay operator-reserved. Free space at writing 22 GB.

## 3 Traps met in this window
- `safe_push` refuses if the worktree changes while it waits: also hold `mandate_continuity.py accept` and `step`
  (they write a tracked file) until the push ends.
- In a timing script, make every loop variable `local`: a helper's `for a` / `for s` overwrote the caller's arm name
  and start time, and one whole round was lost.
- A count reported twice with different scopes reads as a contradiction: state the scope in the same line.
- A pre-registered script is not "the source" to fix: put the corrected rule in `framework/scripts/` and keep an
  `--old-rule` switch.

## 4 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify
   in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 2 item 2 first (one measured step per window); item 1 when its time comes.
