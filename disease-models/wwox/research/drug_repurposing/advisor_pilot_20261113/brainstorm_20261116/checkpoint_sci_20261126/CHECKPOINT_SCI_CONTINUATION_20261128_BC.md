# Checkpoint BC: SCI continuation of 2026-11-28 after BB section 2, the baricitinib check and the Crawford 2010 figure read (resume from this file; BB and BA for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `b09654f8-b07d-4785-af46-7be3b45ef660` (claude-sonnet-5-5, effort high; worktree `sci_bb_20261128`) passed 250k context tokens (about 256k at the report to ADV) after delegate reports and figure reads.

## 0. How to resume
1. As BB section 0: `CLAUDE.md`, state manifest (`current_state: READY`), LEGEND_CORE 21c, 21d, 21e, this file (sha256 against ADV's digest; mismatch: stop and ask), `mandate_continuity.py guidance`.
2. Release and bind for `ORCH-SCI-ADV065-DEEPEN-20261118` (ask the old session to write the plain line `MANDATE_RELEASED: ORCH-SCI-ADV065-DEEPEN-20261118` ALONE in its own text block; a peer saying it did is not the line; check `mandate_watch.py released` by exit code). `ListAgents` first. Merge `development/main`. The record shows only the operator-supply BLOCKED step: accept the next ADV assignment (ADV-317, Crawford) with `mandate_continuity.py accept` before working on it.
3. Disk (17 GB at this report): push at 2.0 GB or more, delegate dispatch at 1.5 GB or more, stop below 1.0 GB. **Never write or commit anything in the worktree while a safe_push runs** (it was REFUSED once for an unclean tree); keep delegate output in `$CLAUDE_JOB_DIR/tmp` until PUBLISHED.

## 1. State
* Landed on main at `bc8a41bde`: ADV-316 step 2 FINAL (Huang Fig 4C/D/E checked on the image; prediction stays UNSETTLED), IT sentence file, receipts `FTR-20261128-41744777-01` and `-42395553-01`, ranking, reading_state, coverage_report.
* In this push (check `git log development/main` for the SHA ADV or the log gives): 42395553 figure-coverage debt closed by a blind figure reader (Figures 3, 5, 6, 7, Supp 1 to 3; verbatim `BLIND_FIGURES_42395553_ADV316_STEP2B_DELEGATE.md`; section D of the IT sentence file; receipt `FTR-20261128-42395553-02`); baricitinib stage-matched check (frozen note sha256 505b17ea9242e797975f105e920c4494f46ae1ffb6d34f162a6379008aea43cc, 11:26:18Z) result NONE with the exact missing observation and all 44 Europe PMC titles; Crawford 2010 recruitment test (frozen note sha256 fcef81d145212bf3bb66f3f9abbbcc11a84c9f94d40c784e12a0570c83faa0d6, 11:34:39Z) with the delegate report and `RESULT_CRAWFORD2010_ADV317_SCI_20261128.md`; ADV-316 and ADV-313 mandate steps DONE.
* Crawford result in one line: Fig 8C/D print full stimulus-response curves; N1 plateau about 0.51 to 0.55 of normal AND the N1 paired-pulse 50 percent interval 2.2 to 3.9 ms (printed): both change, not separable; N2 plateau about 0.4 of normal with the interval 3.1 to 3.5 ms: recruitment-like; my lean is half supported; my guess from a caption that "one stimulus only" was wrong (disclosed).
* Portfolio line for RP-039 (baricitinib missing observation) sent to ADV, who lands it; ADV registers Crawford as ADV-317 with my frozen note as PREREG.
* No delegate is running. Held files not in git: `files/figures/PMID42395553_r3/`, `files/figures/PMID20858739/` (10 figures and `supp_figures.pdf` from the PMC open-data bucket PMC2947430.1).

## 2. Open items in order
1. **ADV-317 closure:** one SCI image check of Fig 9B and its printed table (N1 and N2 50 percent intervals) and of Fig 5C (the delegate's report only so far); then update the RESULT (FINAL) and deliver to ADV with one line. The PMID 31140740 cross-check stays text-level unless ADV asks.
2. **Receipt owed for Crawford 2010** (figures 5, 8, 9 and the supplement opened as images by a delegate, Fig 8 by SCI): record against the prior Crawford receipt (ledger lookup by PMID first), then ranking, reading_state, coverage_report on a committed tree.
3. Sentences for IT only if ADV-317 names a consumer sentence (INV-06 / RP-049 next experiment wording in section 5 of the RESULT).
4. Operator list unchanged from BB (Chong 2023 PMID 36537114; Blades 2022 PMID 35441271; CRMP2 37479154; Balraj 2023 37364629; the Huang supplement PDF).
5. Next held-source question with a named consumer: propose it yourself (standing rule); candidate lines: a second source with stimulus-response curves AND EM from the same animals (none found in ADV-312/313 tables; 31140740 text-level lead), or the Palma 2022 clemastine figures (amplitude by distance, not printed in the text).
6. Untouched: RP-045, sealed ADV-174 and ADV-175, PMID 42422765. Parked by ADV: fibre-volley proposal.

## 3. Habits from this window
* A caption is not a figure: I guessed "one stimulus only" from the Fig 8 caption and the figure printed full curves; write the freeze before reading captions too, or disclose them.
* Blind brief without values or sentences works; whole page renders including legend-continuation pages; recover the report from the user-role transcript record (see memory `sci-bb-pitfalls`).
* Europe PMC `page=2` is ignored; use `pageSize=50` so a negative lists every title.
* `fulltext_receipts.py record` sets the real `event_at`; reading_state and coverage_report refuse a dirty tree (commit the receipt first); on a push conflict take main's side for ledger, manifest, ranking, reading_state, coverage_report, then re-record and regenerate.
* The Agent tool has no effort parameter: state effort in the prompt and tell ADV.

## 4. Standing rules unchanged
As BB section 4: Italian to the operator, files in English; the operator's e-mail never sent to any service; no contact, no spend; a challenge page, 401, 403, 429 or a safeguard is a result; no delegate without telling ADV (effort stated); Codex PAUSED and never contacted; no second worktree; never commit while a safe_push waits; ADV removes the previous worktree and does the rename.
