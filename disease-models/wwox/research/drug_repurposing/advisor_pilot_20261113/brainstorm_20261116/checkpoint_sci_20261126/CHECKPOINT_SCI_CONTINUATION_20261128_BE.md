# Checkpoint BE: SCI continuation of 2026-11-28 after ADV-322, the DisMech block review and the ADV-323 comparison (resume from this file; BD and BC for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `ba384503-345f-494f-aaa5-10ffe4e04f6e` (claude-sonnet-5-5, effort high 9 of 9 turns at bind; worktree `sci_bd_20261128`) reached about 215k context tokens; written early so a successor can take the next question.

## 0. How to resume
As BD section 0 (CLAUDE.md, state manifest `current_state: READY`, LEGEND_CORE 21c, 21d, 21e, this file against ADV's digest, `mandate_continuity.py guidance`, `ListAgents`). Release and bind for `ORCH-SCI-ADV065-DEEPEN-20261118` as in BD section 0 item 2 (ask the old window to write `MANDATE_RELEASED: ...` alone; check `mandate_watch.py released` by exit code; then `MANDATE_BOUND: ...` alone in its block with the first working tool call; verify with your own session id, exit 1 = BOUND). Merge `development/main` first. Disk 15 GB at this report (push at 2.0 GB or more, delegate at 1.5 GB or more, stop below 1.0 GB). Never write in the worktree while a `safe_push` runs; write drafts in `$CLAUDE_JOB_DIR/tmp` meanwhile.

## 1. State
* On main (`3b492f686`, `7533441fd` and later): `COMPARISON_ADV320_ADV323_SCI_20261128.md` and `compare_adv320_adv323.py` in `adv320_chornyy2025_figures_sci_20261128/`; correction of my positional ratio labels in `RESULT_ADV320` (liver gfa1405 81 over brain: BA1 5.1, BA2 1.8, BA3 4.8); `adv322_compound_priority_sci_20261128/RESULT_ADV322_COMPOUND_PRIORITY_NOTE_SCI_20261128.md`; mandate steps ADV-322 and ADV-323 comparison DONE (mandate: 155 DONE, 1 BLOCKED supply-path as before, no TODO).
* Sent: ADV (comparison, then ADV-322 and the one-line DisMech review), IT successor 34 (`IT Orchestrator - CURRENT 4d2da76d`, claim cells for CLAIM 047). No delegate was run in this window.
* Pending: IT answers on the three ADV-322 proposals (Baryla 2022 line into the sodium dichloroacetate dossier; GSK3 conditional-comparison entry; timed reopening of DCA at 2026-12-28 or on a PDHA1-phospho or labelled-flux dataset); IT edits CLAIM 047 bound (2) after its own source check.

## 2. Results to carry (hypothesis level)
* **ADV-320 against ADV-323**: 43 paired Fig 4C percent-area cells (1 beyond tolerance: EFS median 6 against 5.4), 26 RFU cells (0), 28 Fig S1B cells (0). Median area ratio p546/CAG 0.60 in both; whisker maxima 41.9 and 42.3 (text "41", "up to 42"); median RFU ratio 0.22 and 0.21 against text numbers 0.324. Open: tCAG text 5.8 against plot 3.1; text means of EFS, rMBP, MAG against plotted clusters; three wordings of the intensity variable. No counterexample threshold was frozen for ADV-320.
* **ADV-322**: leaders ethosuximide and perampanel; A (GSK3: lithium comparator, tideglusib tool) conditional comparison ranked above B, C, D; B (ganaxolone, etifoxine) unchanged; C (sodium dichloroacetate) lowered with timed reopening because the dossier omits the held Baryla 2022 datum (PMID 35328751 Fig 5b: PDH activity unchanged, lactate up; non-neural; phosphorylation not stated preserved); D (bexarotene, montelukast) rides on INV-06. DisMech block 3 has a false premise for ganaxolone (direct synthetic analogue); blocks 1 and 2 accurate.

## 3. Open items in order
1. IT's replies; deliver to ADV any change in the proposals.
2. **Proposed next held-source question (consumer: IT, for the GSK3 entry; ADV-214 searched tables only and excluded figures and prose)**: which held WWOX-deficient full texts report a GSK3 substrate phosphosite immunoblot (pSer9, beta-catenin S33/S37, CRMP2 T514, glycogen synthase S641, Tau sites) with genotype, tissue, age, n and unit? A loose text screen of 400 held WWOX texts (`files/fulltext`, 2026-11-28) hits 25 or more (Wang 2012, Cheng 2020, Steinberg 2021 and 2025, Repudi 2021, Hussain 2023, Liu 2018, Sengupta 2025, Lima 2026, Kaluzinska 2021 and 2023, Lange 2026 among them); the regex is loose, so each hit needs the figure or sentence read. Freeze the pass rule before opening any (ADV-214 rule: WWOX-deficient against control, protein-level phospho readout, three or more units per arm, species, tissue, age stated). Not held (ledger lookup by PMID 2026-11-28, 0 receipts, 0 files): PMID 37479154 and 37364629 (operator supply).
3. Operator list unchanged (Chong 2023 PMID 36537114 held and read; Blades 2022; CRMP2 37479154; Balraj 2023 37364629; Huang supplement PDF). RP-018 reopens only on a journal version or a retrievable body of bioRxiv 10.1101/2025.11.03.686297.
4. Untouched: RP-045, sealed ADV-174 and ADV-175, PMID 42422765. A blind re-read of Chornyy S1B and 4C is done (ADV-323, HE).

## 4. Habits from this window
* A list of ratios labelled by position hides a swapped order: label each by row (my BA1/BA2/BA3 factors were listed 1.8, 4.9, 4.8 for areas 16, 44, 17).
* Before calling a dossier's premise unmeasured, grep the dossier folder for the PMID of the lab's own held measurement (the DCA dossier missed Baryla 2022 while the PDH/PDK card held it).
* A peer table is compared with a script holding both tables typed from the files; range cells in one reader count as agreement when the other lies inside.
* Wait for a queued push with a loop that exits on the completion file; drafts go to the job tmp folder.

## 5. Standing rules unchanged
As BD section 5.
