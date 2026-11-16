# Report of the 24-hour continuous-autonomy trial (ADV presidio, 2026-11-15)

Non-canonical working report. Written for the operator (compact; the chat version is in Italian). Window [2026-11-14T15:29:29Z, 2026-11-15T15:29:29Z) on `main`; units from `framework/scripts/trial_window_table.py` (cross-checked by hand against `session_model_census.py`, identical); the remaining subscription quota is unknown and no percentage is inferred; a unit is not a quota. Record: `ledger/tasks/orchestrator/ORCH-ADV-FOLLOWTHROUGH-20261114.json` (`TRIAL_24H`, `OBJ_8` to `OBJ_19`). Nothing was spent externally; no contact parameter was sent to any service; no bot or proof-of-work check was bypassed (IT stopped on two reCAPTCHA pages, a 403 and one proof-of-work page).

## Decisions and reasons
- Seven strategic evaluations (P8-P14), each at a decision point (after a consumed result, a changed roadmap or an empty pipeline); six produced a draft, one (P11) was degraded (3 turns, a classifier stop) and its stale premise was corrected, not followed. About a dozen mechanical EVALUATE ticks were held with a written reason (the trigger was the presidio's own update).
- Every Advisor draft's decisive premises were checked in the originals before sending: wrong or stale in five of six (ADV-007: blank composition flags, a grep that missed CCN2, a consumption not pending; ADV-008: both premises false, declined; ADV-010: unknown tier distribution, narrowed; ADV-011: the seed already adjudicated in September; ADV-012: part (a) already decided by IT).
- Not done on purpose, with reasons: a second lens case, the Contrastive replay (option kept), RP-002 (wet-gated), WO-12's Hess half, the two live LINCS queries (S8/S9), a regeneration of committed IT23 files, any card or ranking edit, any send to Mirror (no live session: RP-022 queued).

## Assignments: given, completed, consumed
- Advisor drafts ADV-007 to ADV-012: 6 drafted, 5 sent, 1 declined; 5 delivered; 5 consumed (INV-06 wording, compare_it28 and WO-25 with the IT15 pointer, RP-008 parked and one receipt, the case README update, one WO-11 number).
- Operator-directed: PRESIDIO-004 (HE trial, SCI reference, IT disposition) and PRESIDIO-005 (X1 table): delivered and consumed; the INV-06, INV-03 and WO-25 wordings applied.
- Presidio-decided: PRESIDIO-003 (Ro 25-6981 sources) and PRESIDIO-006 (staleness pass: 2 answered, 8 narrowed, 24 open of 34): delivered and consumed.
- Self-started by IT, SCI, HE: IT49-Q11, WO-32 and IT49-Q06 remainders, three IT delegates (IT44, IT45 and the first), SCI's 32000863 quantification (landing pending), HE60, the window table, HE's CI diagnosis.

## What improved, what did not
Improved (changed a comparison, hypothesis, experiment formulation or open question, and reached a consumer): the INV-03 efonidipine/flunarizine pair is a qualified proposal with sourced values and one corrected frozen statement; INV-06's CTGF wording replaced by the held-data reading, the X1 first question answered (O0-O4); the IT23 symbol lookup: 15 conversions KEEP with provenance, QF membership 365/260 to 363/257, benefit INCONCLUSIVE; the JNK x WWOX contrast has a fifth rival and a third control; WO-11 concluded with a number (14%, 0-34%) and IT15 pointer; K2P tool rows carry premise corrections as dated updates; the open-question map is 2 answered, 8 narrowed, 24 open with the stale rows marked; harness: durable monitor-and-help rule, activity block, window table, recall text, section 13 row, incomplete-run rule, meeting.
Unchanged: every ranking, sign, need and candidate state; no card text edited. Predictive capacity: not shown (frozen predictions about paper contents: F1-F7 5 held, 2 not determinable, 0 missed; WO-32 predictions 2 of 5 held; IT49-Q11 3 of 5; IT's H1-H5 and the case bets P-a/P-b not yet scored or not determinable). Most narrowings are premise corrections and hygiene, not decisions moved.

## Waits, interruptions, restarts, human interventions
- Human: five operator inputs in the window (activation; the NOW/NEXT list with links; a scout report for PLAN; the permanent no-idleness instruction; the permanent monitor-and-help clarification). Work in between, six Advisor drafts and the staleness pass, came without a new prompt.
- Waits: landing batteries of 70-98 minutes (SCI, three times); a 47-minute all-idle gap (12:40Z-13:27Z, ended by the presidio's prompts, acknowledged by IT); a stale P11 wait invalidated; repeated hourly EVALUATE triggers from unchanged digests (held; HE declined a rule).
- Interruptions: 3 or 4 refused pushes (main moved), a first CI-gate refusal for an e-mail literal in a test fixture, classifier stops (P11 and the start of P10 and P13), CI red since 12:39Z on a receipt-freshness defect (ranking surface not regenerated when receipts land; HE regenerating, then a freshness check), two reCAPTCHA stops and one proof-of-work stop respected.
- Restarts: no session restarted; the recall job recreated twice to follow the canonical text.
- Presidio errors corrected on the record: a mis-read cross-check (PRESIDIO-002), an incomplete grep, a nudge based on a mis-read lag (IT was working, two pushes were refused), "last commit by actor" (git has one author), and one hold "until the report".

## Cost, in explicit units (window; main-session transcripts; subagents apart)
| session | turns | output | cache written | cache read |
|---|---|---|---|---|
| HE | 287 | 218,665 | 867,726 | 39,654,371 |
| IT | 354 | 249,624 | 973,136 | 70,289,291 |
| SCI | 397 | 396,628 | 1,521,019 | 68,094,416 |
| ADV presidio | 286 | 303,094 | 518,071 | 194,910,600 |
| IT delegates (2 runs) | 126 | 147,210 | 383,418 | 14,121,307 |
| SCI verifier (1 run) | 44 | 51,210 | 125,260 | 3,111,079 |
| Advisor evaluations P8-P14 (7) | 85 | 82,535 | 534,901 | 4,677,178 |
Output tokens: about 1.45 million in all (main sessions 1.17 M, subagents 0.20 M, evaluations 0.08 M). 254 commits (102 merges), 21 task records created, 12 receipts appended, 7 evaluation runs. ADV's cache read is 3 to 5 times the others only because its context grew all session. Not measured: batteries and CI wall time, delegates a record states without a transcript, the humans' time.

## Recommendation on 48-72 hours
Extend to 72 hours, with five conditions: (1) evaluate on events (a consumed result, a new instruction, an empty queue with no written wait), not on digest changes, and stop evaluating after two consecutive "wait" or no-change outcomes while keeping the hourly check and the meeting; (2) report decisions moved and consumed, not notes or rows narrowed; (3) restart the presidio session from its records at a quiet boundary and recreate the one recall job (CronList first); (4) bring a live Mirror session for the ex-post review queued as RP-022, and a blind verifier for any claim that changes a card or a row (several consumed results had one reader); (5) the operator states a weekly limit so that resource discipline has a number. Risk named: diminishing returns (the last delegate batches were mostly narrowings) and unproved predictive capacity: keep frozen predictions and score them.

**Reconciliation (ADV, 2026-11-16, after the operator's INTEGRATION 'Strategic continuity and scientific initiative').** The recommendation to 'extend to 72 hours' asks for nothing: the continuous mode is the operator's standing authorisation (`CONTINUOUS.json`, written 2026-11-14T09:50:42Z, and the roadmap entries of 2026-11-14 that say no new prompt is needed after any number of assignments or hours and that the end of the observation window revokes nothing). The extension is therefore closed, not pending, and is not a decision item for the operator. Of the five conditions, (2), (3) and (4) stand as working conditions; (5) is a request for a number, not a precondition; **condition (1)'s clause 'stop evaluating after two consecutive wait or no-change outcomes' is superseded**: a wait is revisited at the ordinary cadence with the closing comparison of cross-session transport section 12 ('A local wait is not exhaustion'), because stopping after two waits is how local waits came to be read as exhaustion on 2026-11-16. Finding a laboratory is likewise not a prerequisite for continuing authorised research; it suspends only the experiment that needs it.
