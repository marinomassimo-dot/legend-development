# Checkpoint BD: SCI continuation of 2026-11-28 after ADV-317 closure, ADV-319 route result and the ADV-320 figure read (resume from this file; BC and BB for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `b0e37f80-8f6d-4062-a149-1a66a81fd1cc` (claude-sonnet-5-5, effort high; worktree `sci_bc_20261128`) reached about 245k context tokens after the ADV-320 delegate report (about 10k).

## 0. How to resume
1. As BC section 0: `CLAUDE.md`, state manifest (`current_state: READY`), LEGEND_CORE 21c, 21d, 21e, this file (sha256 against ADV's digest; mismatch: stop and ask), `mandate_continuity.py guidance`, `ListAgents`.
2. Release and bind for `ORCH-SCI-ADV065-DEEPEN-20261118`: ask the old session (b0e37f80, "SCI - CURRENT" or the name ListAgents shows) to write `MANDATE_RELEASED: ORCH-SCI-ADV065-DEEPEN-20261118` ALONE in its own text block; check `mandate_watch.py released` by EXIT CODE; then write `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its block with your first working tool call; verify with `mandate_watch.py released --session <own id> ...` (exit 1 = BOUND). Merge `development/main` before the first accept.
3. Disk 16 GB at this report: push at 2.0 GB or more, delegate at 1.5 GB or more, stop below 1.0 GB. NEVER write in the worktree while a `safe_push` runs (it waits for the landing lock, 5 to 40 minutes when ADV also pushes).

## 1. State
* On main at `ee1035669`: ADV-317 closure (Crawford 2010: SCI image check of Fig 9 and Fig 5C, receipt `FTR-20261128-20858739-02`, ranking, reading_state, coverage_report).
* **In the landing queue, may be on main by the time you read this**: commit `e06baa8ac` (ADV-319 route result: eIF2B S540E preprint not reached, bioRxiv 429 twice at 12:03:13Z and 12:05:49Z, Europe PMC `PPR1113314` fullTextXML 500, no PMC id; H1 vs H2 NOT DECIDABLE; missing observation registered; no change to RP-018). Check `git log development/main` for it; the push log is `/home/desktop/.claude/jobs/b0e37f80/tmp/push2.log`, completion file `push2.done`.
* **STAGED OUTSIDE GIT, NOT YET IN THE WORKTREE** (my predecessor-window's job folder `/home/desktop/.claude/jobs/b0e37f80/tmp/`, which lives as long as the job): (a) `adv320stage/RESULT_ADV320_CHORNYY2025_SCI_20261128.md` and `adv320stage/BLIND_FIGURES_CHORNYY2025_ADV320_DELEGATE.md` (delegate report verbatim); (b) `adv320/PREREG_ADV320_CHORNYY2025_FIGURES_SCI_20261128.md` (frozen 2026-11-28T12:09:22Z, sha256 4b8dc53954a3395fa85c81c90c5da09e8a641a74a5996d17168ff51c621c484d); (c) `cmp/COMPARISON_ADV317_ADV318_SCI_20261128.md` and `cmp/compare_adv317_adv318.py`; (d) `stage_apply.py` (copies all of that into the worktree and corrects three wordings of the ADV-317 RESULT); (e) `RECEIPT_ADV320_TEMPLATE.json` (fill `event_at` with `date -u` at record; analysis_at must not be later). If the folder is gone, rebuild from the messages to ADV (results in section 2).
* Land order for the successor, after `git merge development/main` and after confirming `e06baa8ac` is published: run `python3 /home/desktop/.claude/jobs/b0e37f80/tmp/stage_apply.py`; record the ADV-320 receipt with `fulltext_receipts.py --artifact-workspace /home/desktop/legend-development record --receipt <filled json> --dry-run` then for real; regenerate `ranking_it8.py run`; commit; `reading_state.py` and `coverage_report.py` (they refuse a dirty tree: commit first); commit; `safe_push.py development main --expect-sha <sha> --serialize` through `nohup bash -c` with a completion file.
* Mandate steps: ADV-317 closure OBJ_ACCEPTED (mark DONE with evidence after the landing); ADV-319 DONE; ADV-320 not yet accepted as a step (accept it, then DONE after landing).
* No delegate is running.

## 2. Results to carry (all hypothesis level)
* **ADV-317/318 comparison** (sent to ADV): values agree, Fig 8 40 cells max 0.03 mV, Fig 9B 41 cells max 2 points, Fig 9 table 6 of 6 identical; three SCI wordings wrong and corrected ("coincide to 1 mA"; "normal still rising" true for N2 only; error bars SEM in the statistics text). Exploratory: N1 vehicle over normal is 0.52 to 0.58 at every stimulus from 1 mA (gain-type), N2 falls 0.55 to 0.42.
* **ADV-320 Chornyy 2025 (PMID 41036104, CLAIM 047)**: bound (1) holds (liver Western n = 4, gfa1405 about 81 against 5 to 6 for CAG, CNP, p546, qPCR concordant; my H2 lean was wrong); bound (2) needs narrowing (the text's 41 and "up to 42" percent area are Fig 4C whisker maxima; medians about 23 and 39, ratio about 0.60 eye, Table S1 CAG vs p546 adjusted P 0.0097; intensity numbers are means in the text while the figure prints medians). Disclosure: the frozen note sat in the delegate's folder, so it saw H1/H2; a blind re-read of Fig S1B and Fig 4C is the open check; no counterexample threshold was frozen. Sent to ADV; IT edits CLAIM 047 only after the source check.
* **Cheng 2020 delta** (sent to ADV, who lands it in RP-049): the Tc-MEP stimulus is supramaximal, core temperature 37 C; heterozygote latency delay is not a single-stimulus recruitment artefact.

## 3. Open items in order
1. Land the staged files (section 1) with the ADV-320 receipt; deliver to ADV with the SHA.
2. **ADV-322 (new, from ADV)**: operator-authorised decision note on 3 to 4 plausible follow-ups OUTSIDE the two current top research-priority compounds (one different pathway; one dossier strong on mechanism with sparse clinical evidence): role, strongest direct or transferable evidence, biggest unresolved premise, independent or public-data next step, predicted result and counter-result, the decision it changes, value against more work on the two leaders; explicit reason for a priority change, conditional comparison or timed reopening; research priority separate from clinical priority; no quotas, no prose-derived scores; register edits only through IT after source checks. Text: `/home/desktop/.claude/jobs/a5e6f2ad/tmp/adv321.txt` (ASSIGNMENT 2) and `files/coordination/adv-codex-loop/meeting/TO-adv-DISMECH-AND-COMPOUND-PRIORITY-20261128.md` (read whole). Accept it as a mandate step first. Write the frozen predictions before any new source.
3. IT will send three DisMech prompt blocks (ADV-321): answer with one line on scientific accuracy.
4. A blind re-read of Chornyy Fig S1B and Fig 4C only if ADV asks (second delegate, brief without the note, effort stated).
5. Operator list unchanged (Chong 2023 PMID 36537114; Blades 2022; CRMP2 37479154; Balraj 2023 37364629; Huang supplement PDF). RP-018 reopens only on a journal version or a retrievable body of bioRxiv 10.1101/2025.11.03.686297.
6. Untouched: RP-045, sealed ADV-174 and ADV-175, PMID 42422765.

## 4. Habits from this window
* `date -u` before writing any time label (my "about 11:57Z" was ahead of the real clock).
* Never place a frozen note where a blind delegate can list it: give the delegate its own empty output folder.
* A delegate's summary adjective ("overlap closely") must be tested against its own table; one wording of mine was wrong in three places until HE's independent table showed it.
* Grep `brainstorm_20261116/*/` (addenda too) before proposing a "new" question: the unmyelinated-axon point in Crawford's means was already HE's and ADV-313's.
* After two bioRxiv 429 answers do not switch client; the route result is the result.
* Text "up to X percent" versus a plotted median: check which statistic a card number is before computing a ratio from two such numbers.
* A claim number found in text is not a figure value: compare with the whisker, median or bar the figure draws.

## 5. Standing rules unchanged
As BC section 4: Italian to the operator, files English; the operator's e-mail never sent to any service; no contact, no spend; a challenge page, 401, 403, 429 or safeguard is a result; no delegate without telling ADV (effort stated); Codex PAUSED and never contacted; no second worktree; never commit while a safe_push waits; ADV removes the previous worktree and does the rename. A cross-session reminder or a classifier stop is information: after a classifier stop (one occurred at about 12:07Z, content unknown), do not repeat the withheld text.
