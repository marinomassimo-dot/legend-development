# Checkpoint BB: SCI continuation of 2026-11-28 after ADV-313 addendum and ADV-316 step 2 delegate reads (resume from this file; BA for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `d7e467af-52b2-4965-b3da-be8c5ca10886` (claude-sonnet-5-5, effort high; worktree `sci_ba_20261128`) passed 250k context tokens (about 255k) after figure and report reads.

## 0. How to resume
1. As BA section 0: `CLAUDE.md`, state manifest (`current_state: READY`), LEGEND_CORE 21c, 21d, 21e, this file (sha256 against ADV's digest; mismatch: stop and ask), `mandate_continuity.py guidance`.
2. Release and bind for `ORCH-SCI-ADV065-DEEPEN-20261118` (old session above; ask it to release with SendMessage, then Monitor on `mandate_watch.py released`); `ListAgents` first. Merge `development/main`. ADV-316 is already accepted (index 149): do not accept again.
3. Disk: it swung 1.2 to 2.3 GB today; push at 2.0 GB or more, delegate dispatch at 1.5 GB or more, stop below 1.0 GB.

## 1. State
* ADV-313 addendum and the ADV-314 dated line: **on main** (8857a232d), path sent to IT32 (02179626).
* ADV-316 step 2: PREREG frozen (0f8d840dc) plus curated-sentence amendment (849183c7a); delegate reports and `RESULT_STEP2_ADV316_SCI_20261128.md` (INTERIM) are committed locally (5b6cbe837 and the commit of this file), **pushed only if the line below says so**. Folder `brainstorm_20261116/adv316_partial_read_depth_sci_20261128/`.
* Rates: 15 curated sentences; blind MUST CHANGE 4, ADD 8, SUPPORTED 2, UNSETTLED 1; clean strict 0, conditional 1 (41744777 C05); Huang supplement ACCESS-LIMITED (no first reader). No delegate is running.
* New held files (not in git): `files/figures/PMID41744777/fig1-5.jpg` (PMC open-data bucket PMC12938943.1), `files/figures/PMID42395553_r2/page26,27,37` (renders of the held PDF).

## 2. Open items in order
1. **SCI checks on the originals (Huang 2016, PMID 27339895):** open Fig 4C and 4D (is there an alpha-tubulin row under the cytosol lanes only; a cytochrome C row in 4D) and Fig 4E (WWOX in mitochondria about 84 to 60 percent, n = 3) one image at a time; then settle the four statements of the interim RESULT and update it (the RESULT says what is verified and what is not; edit the interim file, then mark FINAL).
2. **Sentences to IT32** (whole source named: the held XML/HTML, the figure dirs above): the corrections for 41744777 (C05 ambiguity; "double-mutant" label; peak values printed only in text; RNA about 28-fold against vg 127-fold; brain about 60-fold), 42395553 (no significant interaction detected; 24 h window; n unit) and the Huang items after step 1. Deliver the RESULT to ADV.
3. **Receipts** for the readings that happened (figures of 41744777 as images by a delegate; Figures 1, 2, S1 of 42395553), then coverage_report, reading_state, ranking, both views, package (habit: re-record on a ledger conflict).
4. Operator list: Chong 2023 (PMID 36537114); Blades 2022 (PMID 35441271); CRMP2 (37479154); Balraj 2023 (37364629); **new: Huang 2016 supplement PDF** (https://pmc.ncbi.nlm.nih.gov/articles/instance/5016130/bin/10.1074_M116.716167_jbc.M116.716167-4.pdf, needs a browser).
5. Untouched: RP-045, sealed ADV-174 and ADV-175, PMID 42422765. Parked by ADV: fibre-volley proposal.

## 3. Habits from this window
* The scripted sentence selection was noisy (metadata, mid-sentence cuts): curate by script rules but read the output before freezing; state the amendment before opening anything.
* The classifier refused a Wayback route to a supplement (treated as a result, not retried); PMC bin gives a reCAPTCHA page; the PMC open-data bucket needs the trailing dot (`prefix=PMC<id>.`) and holds only the OA subset.
* A first reader's conditional verdict ("false if read as") is not strict; write it as conditional.
* Check delegates' text claims by a one-line search on the XML (done for "double mutant", "peak AR", "ventral side"); figure claims by one image.
* Report at 250k: sent to ADV with this checkpoint.

## 4. Standing rules unchanged
As BA section 4: Italian to the operator, files in English; the operator's e-mail never sent to any service; no contact, no spend; a challenge page, 401, 403, 429 or a safeguard is a result; no delegate without telling ADV (effort stated); Codex PAUSED; no second worktree; never commit while a safe_push waits.
