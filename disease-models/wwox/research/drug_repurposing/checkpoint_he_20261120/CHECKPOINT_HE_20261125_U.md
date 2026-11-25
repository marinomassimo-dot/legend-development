# Checkpoint HE-U (Harness Engineering, ACTOR_ID plan), 2026-11-25 ~17:45Z (context past the restart line; ADV asked for it at 17:02Z)

Written for: the successor HE session. Read after `CHECKPOINT_HE_20261125_T.md`; the traps listed there and in M to S still hold. Hashed once committed; never edited, an addendum is a new file.

## 0 Identity and state
- Outgoing session `02915fa6-d5e1-4a78-98ee-72de16e18472` (worktree `he_t_20261125`, branch `task/he-t-disk-20261125`), model `claude-sonnet-5-5`, effort `high`.
- Mandate record `ledger/tasks/plan/PLAN-HE-CONTINUITY-20261118.json`: run `mandate_continuity.py status`. Never write `MANDATE_STATE: COMPLETE`.
- Reply to the operator in Italian, write files in English.
- Peers at writing: ADV `a5e6f2ad`, SCI `0d0c6dc3`, IT Orchestrator `6739e4ff` (re-run ListAgents; names roll over).

## 1 Done since T; do not redo
- **Leaked test folders** (850cbc14c): `test_regenerate_adjudications_fails_closed.py` left 37 MB per run in `/tmp`; fixed. ADV approved a bounded removal: 793 folders removed, free space 18.8 to 23.9 GB.
- **Disk survey 2** (`HE_DISK_SURVEY_2_20261125.md`): about 15.5 GB of surviving new bytes in 24 h, half of it worktrees of about 0.5 GB each.
- **Clean 4-worker run** (`HE_CI_QUEUE_20261125.md` section 7): PASS WITH SKIPS, 277 targets, 45 skipped, 1,789 s on ea12cde65.
- **Removal reasons** (`branch_hygiene.py --removal`, report only) and **the cleanup report in each window handoff** (`window_handoff.py verify`, 1a0e45c77): what keeps the old worktree, "eligible after <UTC>", processes with their folder, and the worktrees with no reason to keep. Nothing is removed by either.
- **CI workflow question** for the operator: `HE_CI_WORKFLOW_LINE_QUESTION_20261125.md` (one line, `LEGEND_REGRESSION_JOBS: "4"`). Not applied.
- **Orphaned browsers, source fix landed** earlier (a2b46d713, checkpoint T). The existing orphans are untouched (operator).
- **Memory fold:** HE's 20 index lines are now `he-window-pitfalls.md`; MEMORY.md 124 to 105 lines; no note deleted.
- **Privacy-scan speed-up**, landed alone: commit `bb3c81129` (published in `547a0a41f`, gate PASS, `ls-remote`). Section 2.

## 2 Gate privacy scan: state and what is open
**Rule (ADV, from this item).** A differential over today's tree cannot see a pattern added tomorrow, so any cache or short-cut in a privacy gate keys on a digest of its own source and patterns and falls back to the full search on any change.

- Guards inside `scan_privacy_and_secrets` run only while `scan_source_digest() == GUARDS_WRITTEN_FOR`. **Anyone who edits the scan, `record_blocks`, `semantic_blocks` or the parental patterns** sees `test_search_guards_are_in_force` fail: re-read every guard, add a planted case, then set the constant to the digest the failure prints.
- Seeded positives: `planted_cases()` in `scripts/test_public_release_gate.py`, 121 of them, one per guarded alternative: identifier and bibliographic author, machine path roots, e-mail, report identifier, private key, provenance, the three key shapes, password, both variants in each written form, cross-paragraph pairing, parental pairing (attributed and not, `.jsonl`, long extra-suffix block), parent-and-variant, reference genotype, each person noun with each clinical term and country, and the non-ASCII letters that `(?i)` reads as ASCII.
- Proof on base 6af888dc5: findings identical and in the same order on the whole tree (31/31), 50 first-parent commits (34/34), 121 planted trees (127/127); whole-gate output and exit code identical, clean and planted; 53 of 53 broken guard literals detected; **new alternative with the cache present**: 5 of 5 found with 0 cache hits, and 5 of 5 missed with the fall-back forced off. Whole gate 217 to 118 s; scan 201 to 68 s. Scripts and logs: `files/coordination/he_gate_speedup_20261125/`. Not run: `GATE_CACHE_FULL_TREE=1`.
- **Open (ADV condition 5):** for the first three real landings after `547a0a41f`, read the findings count with the old and the new script on the landed commit and report to ADV. Old script: `git show 6af888dc5:scripts/public_release_gate.py`. Run each in a clone at that SHA (`python3 -B scripts/public_release_gate.py`) and compare the whole output.
- Any difference: report to ADV first; one revert of `bb3c81129` undoes the change.

## 3 Open, in order
1. Section 2, condition 5 (the next three landings).
2. **Read after 2026-11-26 11:21Z** (mandate step; method in section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`): CI reds after d3d1f94b on suites the landing selection did name; selector gaps counted apart. ADV: that number decides whether the rule stays.
3. **From SCI ADV-279, report only until ADV says** (minutes per risk):
   a. 39 of about 6,100 held files under `files/` do not match their name; 27 are HTML pages or empty files saved as figure or PDF. List path, size, first line, and which receipt or card cites them; propose a save-time check (content type or magic bytes) in the acquisition script.
   b. Two false consumer joins in the consumer-count scan: `33958783 paper 204` matched `P204`; `DL-MECH-056` appears in a skip list. Find the matching rule and count the other joins made by it.
4. **Disk, ADV removes, HE does not:** `he_o`, `it_17`, `it_18`, `sci_ag`, `it_fu` after 2026-11-26 about 10:40Z; `it_19` after about 15:40Z; `it_successor_n` waits for the orphan-browser decision. Open in the survey: 18.96 GB in the scratchpad of session `4325d70d` (do not touch), browser profile leftovers older than the producer fix, 16 folders still in `/tmp`.
5. 2026-11-29: recheck and delete `files/adv174_negraes_custodian_he/`.
6. If the operator enables the parallel runner: read `ci_runs.py times <sha>` and the step time of the first runs.
7. **Operator list** (ADV carries): the gate privacy cache (decision item 9), the CI workflow line, the 18.96 GB scratchpad, the orphan browsers, the `codex/*` backup push, the patches of checkpoint J section 3.

## 4 Traps met since T
- A built-in safety check refuses `rm -rf` of a path that is a command substitution, and the **whole** command does not run. Print the path, then remove the literal path.
- `find` in the tool shell is a function (bfs); use `/usr/bin/find`, and `/usr/bin/stat -c %W` for birth time.
- A mutation test of a guard must force `guarding = True` in the mutated copy, or the fall-back hides every mutation.
- The cache suite pins the size of the base gate suite (now 76) and wraps the scan function: bind a source digest to the original functions, not to their names at call time.

## 5 First moves for the successor
1. `framework/state/state_manifest_current.md` (`current_state: READY`), LEGEND_CORE §§21c-21e, this file and any addendum.
2. Bind: `mandate_continuity.py status --task PLAN-HE-CONTINUITY-20261118`, MANDATE_BOUND alone in its own block, verify in the next response. Merge `development/main` before the first `accept`.
3. The launcher renames; the successor renames nothing.
4. Section 3 item 1, then item 2 when its time comes.
