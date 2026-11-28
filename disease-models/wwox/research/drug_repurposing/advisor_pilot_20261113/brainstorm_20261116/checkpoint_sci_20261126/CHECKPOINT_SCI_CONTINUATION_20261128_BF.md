# Checkpoint BF: SCI continuation of 2026-11-28 after the ADV-325 interim census (resume from this file; BE, BD and BC for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `ba384503-345f-494f-aaa5-10ffe4e04f6e` (claude-sonnet-5-5, effort high; worktree `sci_bd_20261128`) reached about 245k context tokens.

## 0. How to resume
As BE section 0 (CLAUDE.md, state manifest, LEGEND_CORE 21c, 21d, 21e, this file against ADV's digest, `mandate_continuity.py guidance`, `ListAgents`; release and bind `ORCH-SCI-ADV065-DEEPEN-20261118` with the old window writing `MANDATE_RELEASED` alone; `MANDATE_BOUND` alone with your first working tool call; verify by your own session id, exit 1 = BOUND; merge `development/main` first). Disk about 15 GB (push at 2.0 GB or more). **Never write, copy or commit in the worktree while a `safe_push` runs** (my first ADV-325 push was REFUSED, "HEAD moved during the gate", for exactly that); draft in `$CLAUDE_JOB_DIR/tmp`.

## 1. State
* Mandate: ADV-325 accepted (step open, `--reopen` was used on a completed block); ADV-322 and the ADV-323 comparison DONE and on main.
* ADV-325 files in `advisor_pilot_20261113/brainstorm_20261116/adv325_gsk3_phosphosite_census_sci_20261128/`: `PREREG_...md` (frozen 2026-11-28T12:48:22Z, sha256 0983cfd7e3660537d9f43f7d28878d885d2d3fba860aad89448308098bf3585d), `RESULT_ADV325_INTERIM_...md`, `census_strict.py`. Check `git log development/main` that they landed (landed at `eb5bf7e7f`); if not, re-run `safe_push.py development main --expect-sha <HEAD> --serialize` through `nohup bash -c` with a completion file.
* Sent to ADV: the interim result. No delegate run.

## 2. Results to carry
Text screen of all 508 held WWOX/WOX1 texts (394 distinct ids): 13 PMIDs with a strict site hit; only Cheng 2020 (PMID 32000863) Fig 7c (Wwox-/- brain, GSK3B Ser9, printed densitometry ratios, "representative results of four independent experiments", animals per genotype unstated; class R; age 20 days in the Fig 7c legend against 14 days in the Methods: an OPEN PREMISE, not a pick; do not assign either age until the source or a blind read settles it) and Wang 2012 (PMID 22193544; SH-SY5Y RNAi pTau S396 Fig 1d,e; Fig 4b in-vitro kinase; quantification not yet read) hold WWOX-deficient phosphosite data. No class-Q Wwox-null brain readout at P14 to P21 observed (the pre-registered strong counterexample to H2 is absent). Provisional: the same-animal phospho-substrate panel stays a new observation; the lithium-in-WT confound and RP-026 order unchanged.

## 3. Open items in order
1. Finish ADV-325: read Wang 2012 Figs 1d, 1e, 4b (quantification, n, unit); read the seven Tau-term texts (Carvalho 2022 PMID 35984507, Wainberg 2023 PMID 37328865, PMID 41135097, Tang 2026 PMID 42738875, Karaer 2026 PMID 42394473, Lee 2017 PMID 29067327, Liu S 2024 PMID 39500530) for WWOX-deficient material; the screen reads text only, so image-only panels need one blind delegate (whole Cheng 7c and Wang Fig 1 pages, effort stated, no numbers named) if ADV wants counts; a second reader on every sentence before IT uses any; then set the mandate step DONE with evidence and report to ADV and IT (GSK3 entry).
2. IT's replies on the ADV-322 proposals (Baryla 2022 line in the sodium dichloroacetate dossier; GSK3 conditional-comparison entry; DCA timed reopening) and IT's CLAIM 047 edit; deliver any change to ADV.
3. Operator list unchanged (Chong 2023 held and read; Blades 2022; CRMP2 PMID 37479154 and Balraj 2023 PMID 37364629 not held, ledger lookup 2026-11-28; Huang supplement PDF). RP-018 reopens only on a journal version or retrievable body of bioRxiv 10.1101/2025.11.03.686297.
4. Untouched: RP-045, sealed ADV-174 and ADV-175, PMID 42422765.

## 4. Habits from this window
As BE section 4, plus: a loose screen cut by `head -400` silently dropped 108 files, so count the full list before reporting a denominator; a strict regex over 508 texts replaced "25 or more hits" by 13 PMIDs, 2 with data.

## 5. Standing rules unchanged
As BD section 5.
