# Checkpoint AZ: SCI continuation of 2026-11-28 after ADV-313 (for the successor; resume from this file; AY for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `5c296fab-981d-402e-aef0-73f49e6a1846` (claude-sonnet-5-5, effort high; worktree `sci_ay_20261128`) reached about 298k context tokens, above the 280k restart line, after one increment. The cause was figure images and large text reads in the lead window: **delegate figure reads, or crop first**.

## 0. How to resume
1. As in AY section 0 and 1: read `CLAUDE.md`, the state manifest (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md`, this file (sha256 from `git show development/main:<path> | sha256sum` against ADV's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release and bind for task `ORCH-SCI-ADV065-DEEPEN-20261118` (old session `5c296fab-981d-402e-aef0-73f49e6a1846`). Merge `development/main` before the first `accept`. `ListAgents` first: IT rotated to `a39fdd2a`, HE to `a2763bd3`; ADV is `a5e6f2ad`.

## 1. State
* **ADV-313 DONE and on main** (`336110982b6ad2bd9998dbf4881a011e0100daac`, gate PASS): folder `brainstorm_20261116/adv313_myelin_calibration_sci_20261128/`. Label READABLE: 7 counted sources, 7 laboratories (rank threshold 6 met). Frozen strong counterexample met (PMID 31140740: cuprizone, proportion of myelinated axons about 72 and 89 percent lower, N1 velocity unchanged). No rank agreement under any contrast choice. Replaces ADV-312 lines Z1 and Z3 (K1 to K3 sent to IT; no card held Z1 to Z4 at the time). **Not blind-checked**; IT's blind round with the whole paper is the check.
* Mandate: ADV-302 to ADV-313 DONE, one BLOCKED row (L, supply-path papers). The commit marking ADV-313 DONE travels with this checkpoint.
* Ten receipts `FTR-20261128-*` (none a complete read). Held copies: `files/fulltext/` (`*_efetch_20261128.xml`) and `files/fulltext/adv313_sci_20261128/`.
* Session close done for ADV-313: self-evaluation addendum 4 and dream pass in `research/session_evaluations/2026-11-28_adv302_adv305_sci.md`; capability scout CHANGE = NONE (the routes used are recorded in this window's memory note); takeaways to the operator sent in Italian at close.

## 2. Open items in order
1. **First move: ADV-314** (third and last increment of the calibration strand: what Repudi 2021, PMID 33914858, prints for N1 and N2 amplitude or area, latency, stimulus or input-output curve and recording distance; readings E-A slower N1 in a fixed recruited population and E-B changed recruitment, answered allowed / not allowed / not printed with locators; freeze first; ledger lookup by PMID first; about 75 minutes). Full assignment text: `/home/desktop/.claude/jobs/a5e6f2ad/tmp/adv314.txt`; `assignments/ADV-314.md` lands with an ADV push. Delivered to window `5c296fab` and **not accepted, not started** there (context above the restart line): the successor accepts it once. ADV-313 is already consumed by ADV.
2. IT consumes K1 to K3; answer its questions from the RESULT, table and held copies.
3. Operator list: Blades 2022 (PMID 35441271) needs a person with a browser: https://hdl.handle.net/11343/301987 (repository answers machines with a challenge page; not bypassed). CRMP2 knockout (PMID 37479154) and Balraj 2023 (PMID 37364629) answered 403 on open copies.
4. Untouched: frozen RP-045, sealed ADV-174 and ADV-175 material, PMID 42422765.

## 3. Habits that paid or cost today
* One request to a new host, read the answer, only then the next (an API call left before a challenge page had been read; disclosed to ADV, recorded as not a bypass).
* Write the CAP component (N1, shortest latency, largest peak) beside every velocity.
* Check Europe PMC correction notices before counting a source (one erratum found, acknowledgment only).
* A new `.py` with a shebang needs the executable bit or the landing reds (caught by the early check).
* Push floor is now 1.5 GB (HE, `safe_push.py`); stop writes and dispatch below 1.0 GB. Never commit while a `safe_push` waits.

## 4. Standing rules unchanged
As AY section 6: Italian to the operator, files in English; the operator's e-mail never sent to any service; no contact, no spend; a challenge page, 401, 403, 429 or a safeguard is a result; no delegate without telling ADV; Codex PAUSED; no second worktree; state effort in any delegate dispatch.
