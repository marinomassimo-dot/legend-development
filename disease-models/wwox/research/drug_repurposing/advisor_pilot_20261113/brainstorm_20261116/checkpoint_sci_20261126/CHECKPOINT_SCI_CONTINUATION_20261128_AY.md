# Checkpoint AY: SCI continuation of 2026-11-28 after ADV-312 (for the successor; resume from this file; AX only for standing background; hypothesis level; not medical advice; not edited once hashed)

Why: window `64fc909a-6753-4c4e-a196-53496ce8383e` (claude-sonnet-5-5, effort high; branch `task/sci-ax-20261128`) passed ADV's 250k report line and is near the 280k restart line. ADV launches the successor. The session was started from checkpoint AX (old window 919d2041).

## 0. How to resume
1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md` before the first act, this file (sha256 from `git show origin/main:<path> | sha256sum` against ADV's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release and bind as in AX section 0 (task `ORCH-SCI-ADV065-DEEPEN-20261118`; `MANDATE_BOUND: ...` alone in its own text block with the first working tool call; verify next response). Merge `development/main` before the first `accept`.
3. `ListAgents` first (today: ADV `a5e6f2ad`, IT `54ca757b`/`d69eee3d` per ADV, HE `c396c807`/`dc4707bc`).

## 1. Delivered today by this window (all on development/main; each folder under `brainstorm_20261116/`; each with PREREG sha256 frozen before the decisive data)
| Item | Folder | Result in one line | Consumer |
|---|---|---|---|
| ADV-302, ADV-305 | `adv305_divergent_etifoxine_sci_20261128/` and the ADV-302 record | ADV-305: etifoxine/TSPO divergent reading ambiguous; E1/E2 unsupported, E3 compatible only on the blocked-share scale; XBD173 to be added as TSPO-selective comparator | ADV, IT |
| ADV-308 | `adv308_burst_split_sci_20261128/` | NOT TESTABLE FROM HELD SOURCES (burst-vs-spike split); adjacent observation PMID 42589596 slice XBD173 3 uM | ADV |
| ADV-309 | `adv309_age_window_table_sci_20261128/` | 26-row age-window table; four statements superseded by ADV-310 (dated addendum in RESULT) | IT (W1 to W4) |
| ADV-310 | `adv310_cheng_first_hand_sci_20261128/` | Cheng 2020 first-hand: E-B narrowly, 2 of 16 brief statements differ (n lower bound 8 not 12; "only E16.5 precedes onset" wrong); receipt FTR-20261128-32000863-01 | IT (X1 to X6) |
| ADV-311 | `adv311_pup_feasibility_sci_20261128/` | Knockout frequency 5.1 percent (WD1, N 177) and 6.5 percent (WD234, N 785) at P5 to P12 against the brief's 25 percent: 0.36 and 0.46 knockouts per litter at 7 pups; the 33-knockout planning minimum needs 93 and 73 litters (brief: 19); Ludes-Meyers 2009 P3 30/154 = 19.5 percent (misses my frozen 20 percent line by 0.5; both readings reported); E-A vs E-B undetermined; Aqeilan 2008 close-out (no counts); receipts FTR-20261128-19936220-01, -33914858-01, -18487609-01 | IT (Y1 to Y5), ADV |
| ADV-312 | `adv312_myelin_calibration_sci_20261128/` | TOO FEW SOURCES (3 counted of 4 needed): Palma 2022, Crawford 2010 (PMID 20858739), Nr2f1 HET (31318166); direction follows the headline structural variable, size does not (thickness vs g-ratio ratio 10.8 vs 1.04 in one Crawford contrast); candidate counterexample Blades 2022 (35441271, Tyro3 knockout, abstract only, numbers unread); receipts FTR-20261128-20858739-01, -31318166-01, -30703503-01 | IT (Z1 to Z4), ADV (RP-049 resume condition) |
Mandate `ORCH-SCI-ADV065-DEEPEN-20261118`: ADV-302 to ADV-312 DONE, one BLOCKED row (L, supply-path papers).

## 2. State at the checkpoint
* **ADV-312 landed:** push18 published `49f2c6c33632becced38bde0fcdc43ec2d323b8e` on development/main (gate PASS) with the ADV-312 folder, three receipts and the regenerated surfaces. This checkpoint lands in a later push.
* ADV-312 is complete as delivered (nothing left in the current step); the ADV-312 report to ADV is sent with the checkpoint note.
* Session-close: self-evaluation addenda for ADV-308 to 312 are in `research/session_evaluations/2026-11-28_adv302_adv305_sci.md`; the dream pass for ADV-311 is recorded there; legend-capability-scout (CHANGE = NONE valid) and legend-session-takeaways to the operator (Italian) are owed by whoever closes the window.

## 3. Open items in order
1. ADV has the path and sha of this file (sent after it landed); nothing owed there. Check `git log development/main` for later commits by ADV or IT that change the open items.
2. ADV said the next strand comes after IT has consumed Y1 to Y5 and the J-lines. If none arrives, propose a held-source question with a named consumer; strands rotate after three increments (the pup-window strand had three; the etifoxine strand two; the myelin-calibration strand one).
3. ADV-312 leads, none started: (a) a lawful full-text route for Blades 2022 (Springer, no open copy, no PMCID; if it confirms a thickness fall with null callosal and optic-nerve conductivity it is the strong counterexample); (b) Crawford 2009 a (cited by the cuprizone-rapamycin paper; not chased); (c) the peripheral nerve stratum was defined in the PREREG and not searched; (d) abstract-only partial sources (Luo 2018, taiep rats, LES rats, Balraj 2023, md rat) need their full texts for numbers; (e) the search had 12 title-or-abstract queries on Europe PMC only, no PubMed query.
4. IT's lines X1 to X6, Y1 to Y5, Z1 to Z4 are IT's to consume; no card or ranking changes by SCI.
5. Obeid 2026 (PMID 42422765), the frozen RP-045 prediction, ADV-174/175 sealed material: untouched, unopened.

## 4. Habits that paid today (apply from the first act)
* **Ledger before "not held".** Before any brief, assignment or fetch says a paper is not held, run the receipts-ledger lookup by PMID (`grep` of `fulltext_read_receipts.jsonl` by `study_id.pmid`) and put the prior event ids in the first line. "Not held" means "no local copy", never "not read". It failed twice today (Cheng 2020: complete read FTR-20260804-32000863-01; Aqeilan 2008: complete read FTR-20260811-18487609-01, no local copy on this machine).
* Identifiers (DOI, PMID) in a receipt come from the held file's article-id tags, never from memory (two DOIs typed from memory were wrong and were corrected before recording).
* A "seen before freezing" line is written from a quoted line or not at all; a remembered statement goes under "believed seen, not located". Never edit a hashed PREREG (a sed on the copy changed its hash once; restored from the job copy before committing).
* Label numbers by sheet, figure, panel and row; recompute printed ratios (Crawford's n and Nr2f1's degrees of freedom do not match their legends).

## 5. Landing traps met today (recipe)
* After a receipt, regenerate in this order and commit all together before the first push: `ranking_it8.py run`; `reading_state.py --out disease-models/wwox/registries/reading_state.md --inputs-dirty-because "<my own receipts in this worktree>"`; `coverage_report.py --out disease-models/wwox/registries/coverage_report.md` (same flag); the view trio `repurposing_view.py run`, `run --source shareable`, `package`, `i18n --what collect` (about 4 min, run under nohup). The freshness tool exit 2 from the dismech sidecar was fixed by HE (f6de3399c); if it recurs, regenerate those pages by hand.
* The remote moves under a long push (ledger, manifest, ranking, derived pages and view conflict each time). Recipe: `git fetch development && git merge development/main`; for every conflicted generated file `git checkout --theirs <file> && git add <file>`; re-record your receipts only if their event id is missing from the merged ledger (set analysis_at to a past minute and event_at to now); regenerate the surfaces above; commit; push at once. Do not commit while a safe_push waits.
* Disk is shared with other sessions' pushes; df fell to 1.2 GB; the wrapper waits for 2.2 GB (`push_when_room.sh`: loop on df then `safe_push.py development main --expect-sha <SHA> --serialize`).
* Routes met: Europe PMC `fullTextXML` HTTP 500 for a non-open item; NCBI `efetch db=pmc` returns the whole body for open-access items and only front matter for others; the PMC page returns full text; the PMC PDF link returns a reCAPTCHA page (route result, not read).

## 6. Standing rules unchanged
Italian to the operator, files in English; the operator's e-mail never sent to any service; no contact, no spend; a challenge page, 401, 403, 429, 5xx or a safeguard is a result; no delegate without telling ADV (none was used today by this window); Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; PMID 42422765 unopened; df 1.5 GB before a dispatch, 2.0 GB before a push, stop below 1.0 GB and tell ADV; no second worktree.
