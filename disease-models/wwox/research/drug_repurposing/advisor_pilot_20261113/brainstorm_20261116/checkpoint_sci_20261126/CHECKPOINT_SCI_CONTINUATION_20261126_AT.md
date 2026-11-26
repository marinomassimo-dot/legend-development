# Checkpoint AT: SCI continuation of 2026-11-26 after ADV-282 ranks 25 to 48, for the successor (resume from this file; AS only for background; hypothesis level; not medical advice; not edited once hashed)

Why: window `7f7fcdaa` (claude-sonnet-5-5, effort high read back) closed ADV-282 ranks 25 to 48 and reached ADV's checkpoint line. ADV's instruction: record the increment 4 blind report, dispatch increments 5 and 6 one at a time, then checkpoint AT with path, sha256 and what is owed. This file is its answer. It supersedes AS for the next steps; AS (sha256 62b07db4...3e3332) and its ADDENDUM1 (sha256 9e887a2e...7806, three corrections to the predecessor's sentences) stay in force.

## 0. How to resume

1. Read `CLAUDE.md`, `framework/state/state_manifest_current.md` (`current_state: READY`), sections 21c, 21d, 21e of `framework/instruction/LEGEND_CORE.md`, then this file (compute its sha256 and compare with the launcher's digest; mismatch: stop and ask), then `python3 framework/scripts/mandate_continuity.py guidance`.
2. Release first, then bind: `python3 framework/scripts/mandate_watch.py released --session 7f7fcdaa-efe9-492e-92e6-50382d5295c1 --task ORCH-SCI-ADV065-DEEPEN-20261118` (exit 0 = RELEASED; wait in a QUIET Monitor until-loop); then `MANDATE_BOUND: ORCH-SCI-ADV065-DEEPEN-20261118` alone in its own text block in the same response as the first working tool call; verify in the next response. Own worktree on a task branch; merge `development/main` before the first `accept`.
3. Read your effort back with `session_model_census.py --json --dir <own project folder>` (must be high). Run `ListAgents` (at 2026-11-26 about 02:10Z: ADV - CURRENT a5e6f2ad, IT Orchestrator - CURRENT 6f4e0008, HE - CURRENT 888b4b03).
4. Landing: `task_close.py` refused earlier ("main must be checked out in exactly one worktree"; no worktree holds `main`). Do not repair the root checkout; publish with `safe_push.py development main --expect-sha <sha> --serialize` through `nohup bash -c '...' < /dev/null`, and tell HE.

## 1. Done in this window

* **ADV-282 ranks 25 to 48 closed** in `advisor_pilot_20261113/brainstorm_20261116/adv282_null_note_control_audit_sci_20261125/`: `PREREG_ADV282_INC4/5/6_SCI_20261126.md` (frozen before any source), `FIRST_READ_ADV282_INC4/5/6_SCI_20261126.tsv`, `BLIND_SENTENCES_ADV282_INC4/5/6_SCI_20261126.md`, `BLIND_REPORT_ADV282_INC4/5/6_SCI_20261126.md` (verbatim), `FILES_VIEWED_ADV282_INC4_6_SCI_20261126.tsv`, `recompute_k01_007_adv282.py`, and **`RESULT_ADV282_INC4_6_SCI_20261126.md`** (the result; its sha256 is in the commit that landed it).
* **Numbers (22 rows read of 24; DR-L01-003 NOT ASSESSABLE after a Europe PMC HTTP 503, DR-H02-005 set aside):** strict 2 of 17 assessable, loose 10 of 17, blind MUST CHANGE 7 of 22, **verified MUST CHANGE 5 of 22** (DR-A01-007, DR-B01-002, DR-W2-004, DR-H02-036 one clause, DR-I01-014), ADD 15. The rejecting observation (3 or fewer) was not met. Held apart, not counted: DR-A02-010, DR-H02-008, DR-H02-023 (blind MUST CHANGE or first-reading MUST CHANGE that I grade ADD, reasons in RESULT 3.2). UNSETTLED: the DR-H02-036 coculture clause, 'only' in DR-I01-004, 'the full text is closed'.
* **Dispatch deviation to carry:** reader 6 got one added phrase on the rule (the study's own endpoint is not an engagement check); readers 4 and 5 got the PREREG wording. Stated in the RESULT and in report 6.
* **Memory:** `sci-as-adv282-pitfalls.md` (not in git; in the project memory folder).

## 2. Next work, in order

1. **Report to ADV** (if not yet answered): the RESULT path and sha256, with strict, loose and ADD labelled separately and only the verified MUST CHANGE as the yield.
2. **Sentence files owed to IT** (card owner): RESULT sections 3.1 (five verified MUST CHANGE, with consumers) and 4 (ADD) are the sentence set for ranks 25 to 48. First check IT's queue and apply report; do not resend what IT has applied. DR-L01-003 stays open (one later retry of the Europe PMC route, then close as NOT ASSESSABLE).
3. **H02/A01 second random 20 of ADV-287** (IT's apply landed): draw with the ADV-287 seed rule recorded in its PREREG, frozen PREREG first, one matching rule, first reader on held files, blind sentence-level reader given the sentence alone.
4. **Proposal (ADV: the debt is not exhausted at one consumer):** the remaining readable held partials at one consumer, after item 3; use the ADV-292 recipe. Run `rank_held_partials_adv265.py`, `containment_adv265.py`, `content_check_adv280.py`, `count_adv280.py` and `consumer_count.py` first, with the standing exclusions 28151481, 28045433, 41948127, 33958783 and the ten ADV-292 records (reserve 36282524 and 42807679 unused).
5. One mandate item stays BLOCKED (the operator's papers); ADV-282 closes with this window.
6. **Session close** (the predecessor and this window skipped them): `legend-session-self-eval`, `legend-capability-scout`, `legend-dream`, `legend-session-takeaways`.

## 3. Standing rules (unchanged from AS)

Italian to the operator, files in English. No e-mail address to any service; challenge pages and 401/403/429/5xx are results; no spend; no contact with authors or outside parties; Codex PAUSED; frozen RP-045 and sealed ADV-174/175 untouched; the HE window does renames; the Obeid 2026 article (PMID 42422765) stays stopped and unopened, including its manifest and receipts. State model and effort in every delegate dispatch and read them back (the Agent tool has no effort parameter). Delegates cannot write files in the repo: ask for the text as the reply and extract it from the transcript's SubagentHandback call. Long suites and `safe_push` through `nohup`; never commit or create a repo file while a `safe_push` runs. Before a first push of a new .md: `test_fresh_clone_reader_journey.py`, `test_documented_commands.py`, `test_link_targets.py`, `test_structured_data_integrity.py`.

## 4. Lessons of this window (memory `sci-as-adv282-pitfalls.md`)

* A figure can contradict the paper's own text at one dose: when a note generalises over doses, read the per-dose marks (DR-W2-004, Fig 3A).
* A lower-bound potency ('> 2 mM') cannot support 'does not engage' at a higher applied level (DR-A01-007).
* An attribution must name its object ('the effect that was seen'; DR-B01-002).
* Abstract-level null notes fail mostly by omission (15 ADD) and by inference ('opposite signs', 'depended on').
* Put every clarifying phrase into the PREREG before the first dispatch; adding one for a later reader makes the increments differ.
* Pseudocount choice moves a log2 ratio at the edge of a stated bound (K01-007 cortex Hif1a, 0.01 gives -0.21, 0.1 gives -0.20): state it beside the number.
