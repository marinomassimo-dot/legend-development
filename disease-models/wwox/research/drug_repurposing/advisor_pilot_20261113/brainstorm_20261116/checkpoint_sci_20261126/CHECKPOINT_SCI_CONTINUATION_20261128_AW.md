# Checkpoint AW: SCI continuation of 2026-11-28 after ADV-295 block 2 and ADV-297 (for the successor; resume from this file; AV only for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `fc428159-b22b-41a9-8e5f-3aa6ff67b24f` (claude-sonnet-5-5, effort high) is over the restart line ADV set (context about 346k at ADV's tick); ADV launches the successor. AU, AS (+ ADDENDUM1) and AT stay in force.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md`, this file (compute its sha256 from `git show origin/main:<path> | sha256sum` and compare with the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release first, then bind: `python3 framework/scripts/mandate_watch.py released --session fc428159-b22b-41a9-8e5f-3aa6ff67b24f --task ORCH-SCI-ADV065-DEEPEN-20261118` in a quiet Monitor until-loop (exit 0 = RELEASED), then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; verify in the next response (exit 1 = BOUND is normal).
3. Effort: `session_model_census.py --json --dir <own project folder>` must read high. `ListAgents` first.
4. Merge `development/main` before the first `mandate_continuity.py accept`. Disk: `df -h /` at least 1.5 GB before a dispatch, 2.0 GB before a push; below 1.0 GB stop and tell ADV. Push with `safe_push.py development main --expect-sha <sha> --serialize` from a `nohup bash -c` loop that waits for `df` (copy of my loop: `/home/desktop/.claude/jobs/fc428159/tmp/scripts/push_when_room.sh`); do not run the suites yourself first.

## 1. First move: ADV-297b (ADV's decision of 2026-11-28; check that an assignment file or message from ADV names you, then `accept` it once)

A second frozen increment of the abstract-triage test: a new seeded draw of ten from the remaining 184 catalogued-only records without a receipt, **restricted before the draw** to records with an open full-text route checked by script (state the route test in the PREREG, for example Europe PMC isOpenAccess or a held file); the PREREG says the answer is about the openly readable part of the tail. Same step A rule family (freeze again with time and hash, before any abstract), same prediction form (1 miss of 10, range 0 to 3; reject at 2 or more; park at 0 misses with 7 or more DISCARD). Starting material in `brainstorm_20261116/adv297_catalogued_triage_sci_20261128/`: `PREREG_ADV297_SCI_20261128.md` (rule text, matching rule, score), `draw_adv297.py`, `RESULT_ADV297_SCI_20261128.md`. Packet builder: `/home/desktop/.claude/jobs/fc428159/tmp/scripts/mk_packet_adv297.py` (NCBI efetch by script; abstracts stay out of git). SCI's suggestion: keep the step A rule unchanged and report reviews apart. Exclude the ten already drawn.

## 2. State of what this window did

* ADV-295 block 2 closed: strict 1 of 3 (33704440); both blocks strict 4/8, decision-bearing 2/8. Sentences sent to IT. Session-close notes landed (`research/session_evaluations/2026-11-28_adv295_block2_sci.md`).
* ADV-297 closed as **not decidable from this draw**: 3 of 10 checked (needs 7), 1 miss (25662954, a review), 2 calls confirmed; 4 access failures; 3 not checked because the step B batch 1 reader was stopped by a safety classifier. **Those three (26120275, 31829254, 32931356) stay unchecked: no retry, no re-dispatch, no other route** (ADV, 2026-11-28; recorded for the operator). Three receipts `FTR-20261128-{25662954,26910372,17690733}-01`.
* Files for others: `SENTENCES_FOR_IT_ADV297_SCI_20261128.md` (I1 to I5; I3 needs BATCH_COMMIT), `DEFECTS_FOR_IT_AND_HE_ADV297_SCI_20261128.md` (CORPUS P214 unreadable entry; consumer_count false join through the word "Identifier"; PMCID citations invisible to joins; discovery ledger line 29 cites a never-read record).
* Mandate: ADV-297 step DONE; ADV-297b is not registered; one older step stays BLOCKED (the operator's papers).

## 3. Session-close skills OWED (ADV: here, not before the restart)

For ADV-297: `legend-session-self-eval` (gate scripts first), `legend-dream`, `legend-capability-scout`, `legend-session-takeaways` (the last one is also the report to the operator, in Italian, covering ADV-295 block 2 and ADV-297). Material for them: three classifier stops in one day on delegates (one command refused, one hand-back cut, one reader stopped before any check); a frozen threshold made unreachable by access and stops (check reachability of a draw before freezing a minimum); the step A reader named what the full text would hold and the rule still sent it to READ-LATER; verifying a peer-facing claim in two files was not enough (first retraction missed the PMCID citation in a third).

## 4. Standing rules (unchanged)

Italian to the operator, files in English. No e-mail address to any service; a challenge page, 401, 403, 429, 5xx is a result; no spend; no contact with authors or outside parties; Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; HE renames; the Obeid 2026 article (PMID 42422765) stays unopened in every form. One delegate at a time, model and effort in the dispatch and read back; a 20-minute stall and disk watch. Save each delegate report from the longest `SubagentHandback` of its transcript and run `public_release_gate.py --mode staging --paths` on it before committing. Never commit while a safe_push waits.

## 5. Noticed, not acted on

`development/main` received a montelukast session evaluation named `..._scicodex.md` on 2026-11-28 (commit dae3363cb, 05:24Z) although Codex is recorded as PAUSED. Told ADV; not examined.
