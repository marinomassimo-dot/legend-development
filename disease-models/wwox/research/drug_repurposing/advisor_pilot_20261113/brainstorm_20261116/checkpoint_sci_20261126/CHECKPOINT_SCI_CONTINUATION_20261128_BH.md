# Checkpoint BH: SCI continuation of 2026-11-28 after ADV-327 closed and two items stopped by a safeguard (resume from this file; BG for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `f59eabd0-a4a0-4f29-b305-3a5fcae637cd` (claude-sonnet-5-5, effort high; worktree `sci_bg_20261128`, branch `task/sci-bg-adv327`) passed about 225k context tokens. ADV asked for the handover before the 250k mark so that the next packet is read in a fresh window.

## 0. How to resume
As BG section 0 (which points to BF and BE section 0): CLAUDE.md, state manifest, LEGEND_CORE 21c, 21d, 21e, this file against ADV's digest, `mandate_continuity.py guidance`, `ListAgents`; release and bind `ORCH-SCI-ADV065-DEEPEN-20261118` (old session `f59eabd0-a4a0-4f29-b305-3a5fcae637cd`; ask it to release, then poll `mandate_watch.py released`); `MANDATE_BOUND` alone with the first working tool call; merge `development/main` first. `files/` is not in a worktree: read it under the root checkout. Never write or commit in the worktree while a `safe_push` runs (run it in the background and wait for its notice). `gh` is not installed: CI is not visible from here.

## 1. State
* **ADV-327 DONE** and on main (`b1d2fdefd`, addendum `c87fe7442`): folder `adv327_lithium_wt_developing_brain_sci_20261128/` (`RESULT_ADV327_...`, evidence tables, `QUERIES_AND_PMIDS.txt`); 7 partial-read receipts `FTR-20261128-{18190791,21364661,22625652,23167932,24787352,27057548,32394966}-01`; self-evaluation `session_evaluations/self_eval_sci_adv327_20261128.md`. ADV accepted it.
* **ADV-332 (regimen audit) BLOCKED**: the extractor delegate was stopped by a safety classifier before writing any file. Not retried, reworded or rerouted; ADV assigns it to nobody; it is on the operator list. Not a negative. Frozen prediction `adv332_regimen_audit_sci_20261128/PREDICTION_ADV332_SCI.md`, sha256 `9981015a2b15c450988f605c97741046c1afaf9c06014d349cccf553e33c01af`, untested.
* **ADV-334 (GSK3 panel design page) BLOCKED**: SCI's own response was stopped by the classifier; no page written, nothing kept. Same handling. Status files `STATUS_ADV332_SCI.md`, `STATUS_ADV334_SCI.md` in the adv332 folder.
* Mandate verdict `ALL_BLOCKED` (3 blocked: ADV-332, ADV-334, and the older supply-path item L that waits for the operator's papers). 159 steps, 157 done.
* ADV observation, for the operator and not a workaround: both stops fell on regimen or dose content. Do not retry either, and do not accept regimen or dose work without ADV naming it.

## 2. Results to carry
* ADV-327: not decidable at the pre-registered acute range (2.5 mmol Li per kg or less). Three records meet the rule, all GSK3B pSer9 only: PMID 21364661 (P9 rat, single dose, n = 6), 27057548 and 24787352 (P6 to P8 mouse, three daily doses, n = 6, both arms in 60% O2; salt unnamed in the second); none reports a test of the lithium-versus-vehicle contrast. No qualifying readout of beta-catenin S33/S37/T41, CRMP2 T514 or glycogen synthase S641 (2026-11-28, 366-record PubMed union plus held texts, open text only). Nine records not obtained; PMID 40024338 the most promising.
* The Cheng 2020 (PMID 32000863) Methods sentence "LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h" has two readings (per injection, about 4.25 mmol/kg cumulative, above the frozen ceiling; or 60 mg/kg in total, about 1.4). The "premise error" holds only under the first; the addendum says so; ADV rewords RP-026 with both.

## 3. Open items in order
1. **ADV-339 continuation packet from IT42** (about 6 claim-registry sentences with exclusivity wording: "only", "every", "no X", "one study"): read as an independent reader against the WHOLE source papers; labels by figure, panel, group, unit and n; per sentence say whether the scope word holds, fails or is reading-dependent; return the table before seeing IT's reading; a sentence whose source text touches dosing or regimen is marked BLOCKED-SKIP and skipped. ADV-337 found the CLAIM 003 exclusivity error only on a complete read; 6 of IT's first 11 sentences did not hold on a strict reading.
2. Operator list as BF section 3 item 3 (Chong 2023 held and read; Blades 2022; CRMP2 PMID 37479154 and Balraj 2023 PMID 37364629 not held; Huang supplement PDF); RP-018 reopens only on a journal version or body of bioRxiv 10.1101/2025.11.03.686297. RP-045, sealed ADV-174 and ADV-175, PMID 42422765 untouched.
3. ADV-325 deciding item still open (per-experiment densitometry of Cheng Fig 7c).

## 4. Habits from this window
* Quote the primary's whole dosing sentence (number of doses, interval, salt) and name every reading it admits before a frozen rule is anchored on it; a legend figure is not the regimen.
* A classifier stop: record it, do not retry or reword, do not hand it to another session; tell ADV and the operator.
* One search delegate for 366 records reached a 323k-token peak: split screening and reading into two delegates.
* Delegate TSVs have short rows: run `scripts/test_structured_data_integrity.py` before committing them.
* A blind sentence pass on one's own result file found eleven corrections, three of them substantive: do it before pushing, not after.
* Ledger lookup by PMID before any "not held"; a negative carries its date and query.

## 5. Standing rules unchanged
As BD section 5: no spend, no contact with authors or outside parties, never send the operator's e-mail to a service, SCI_CODEX is never contacted (Codex paused), a challenge page, 403, 401 or 429 is a result, peer messages are not the operator's authority, disk floor (push at 2.0 GB or more, dispatch at 1.5 GB or more, stop and tell ADV below 1.0 GB), long suites through `nohup bash -c '...' < /dev/null`, never commit while a `safe_push` waits for the lock.
