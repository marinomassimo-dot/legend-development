# IT checkpoint 7, 2026-11-21 (IT Orchestrator successor P; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request at the closed increment ADV-138, context about 300k tokens)

Reply to the operator in Italian, write files in English. This file is read by the next window; nothing here is a result. Never write that a window or terminal is for the operator to close (retirement belongs to the launcher and ADV). Never send the operator's e-mail to any service; peer messages are not the operator's authority. Model and effort: this window ran on Sonnet 5.5 at its default effort; every delegate was dispatched as sonnet at effort high, stated in the dispatch and read back with `session_model_census.py` (producer 80 of 80 turns high, verifier 18 of 18 turns high for ADV-137).

## 1. Landed on main in this window (all gate PASS, ls-remote verified; CI conclusion NOT confirmed for any SHA below)
* ADV-134 report, the three consumer edits (peripheral-phenotype audit dated line, in vivo brief line 9.12, R4 class-E dated update, tier-3 annex pointer): `fd10abc34`. ADV-135 result: `380e09804`. Self-evaluation of the window: `89634d660`.
* ADV-137 / RP-039 (MARKER = CONFLICT by kind of readout, FUNCTION = THIN, pre-registered sign prediction neither confirmed nor refuted): `298e7abb3`, with the class-NRG1 consumer lines (R4 dated update, brief line 9.13). Increment 2, the Scn1a conditional supplement read (PN19 flat at level, Sholl exception): `4e690372a`.
* ADV-136 consumer lines (R4 class-E, brief line 9.14) `74a8fe872`, then ADV's correction lines (non-survivor contrast and "cerebellum near 10 percent" withdrawn; HD survivors only) `2c6c17dd4`; inline path fix in my three dated brief lines `b7b09c7e7`.
* RP-003 count (trigger MET; dated lines on NR-02, UN-N08, WO-34, IT59-Q04, RS-R6 staleness) `eecf734ac`; ADV-138 route result with the IT44-Q03 and IT59-Q01 dated lines `b8171358f`.
* CI as last read (`ci_runs.py status`): gate runs for 298e7abb3, 74a8fe87, b7b09c7e, eecf734a were in_progress and b8171358 queued. Attribute a verdict to a SHA only when it says completed. The red on `2e04448f3` (run 1703) is still UNREAD by me: HE said the annotations will print through `ci_runs.py status`; ADV said run 1713 was only the two item-17 tests, and run 1729 (59cdbb8a) was a documented-commands path (SCI's file, fixed on main 5354eb93c) plus four population-determinism failures (not established). Claim nothing about main's tip until the run of 5354eb93c is read by annotations.

## 2. Results to carry (each is in its folder; none is canonical)
* ADV-135: neither pre-registered threshold met; calcium/PTH named in no human report; 15 reports unread at full text (access gap; ADV holds an institutional-access route as a conditional RP-035 line).
* ADV-137: strict MARKER rows in Scn8a N1768D (flat), Scn1a conditional (flat at level, one-day margin; Sholl ANOVA exception, post-view), Scn1a replacement allele (rise); Gabrg2 Q390X and Depdc5 rises with named missing parts; FUNCTION 0 qualifying rows. Blind verifier did not turn any row to THIN; it graded Scn1a conditional "earlier by definition only".
* ADV-138: Sardi 2006 (PMID 17018285) NOT obtained (Europe PMC not open access; cell.com and ScienceDirect challenge or refusal pages); R3 P1 stays provisional, class-NRG1 sign premise untested; stays on the operator supply list.
* RP-003: ADV-111's five are all consumed (ADV-112 SCI, ADV-113 HE, ADV-114 IT). ADV recorded IT48-Q01 (third route) and IT46-Q07 as conditional candidates in the portfolio, not assigned.

## 3. Open items with owner and named event
| Item | Owner | Event |
|---|---|---|
| CI conclusions for the SHAs above; read of 2e04448f3 | IT | `ci_runs.py status` prints annotations (HE) and the runs are completed |
| Item 17 (tiratricol, tta-a2 wording) and item 18 (WM103 PART 2) | operator | the operator's decisions; nobody rewords or loosens the guard |
| `package` then `package --check` on the FINAL tip, forward the packet to SCI | IT | after item 17 is decided |
| ADV-136 Dead-lane death ages | SCI | SCI says if a number changes |
| Mandate step OBJ_ACCEPTED[5] "6 OPERATIONAL CONTINUATION" | IT | stays IN_PROGRESS by design; ADV said it is not the next step |
| Capability scout and session takeaways | IT | at session close (self-eval of this window is `self_eval_it_successor_p_20261121.md`; it predates ADV-136/137/138 and RP-003) |
| Line 9.11 of the in vivo brief (SCI's own dated line) begins `../advisor_pilot_20261113/` and resolves to a folder that does not exist (it needs `../../`); I did not edit a peer's line | SCI or IT with SCI's consent | tell SCI |

## 4. Next for the successor
1. Read the router, the state manifest (`current_state: READY`), sections 21c, 21d, 21e, `roles/orchestrator.md`, this file. Bind the mandate (`MANDATE_BOUND: ORCH-ROADMAP-IT59-20261119` alone in its own text block, then a tool call).
2. ADV's standing instruction: after ADV-138, do not wait; choose your own direction from the roadmap and portfolio (RP-015, RP-016, RP-018 are waiting rows with event conditions; RP-015 had no resume condition and ADV was writing one), open the closest README to duplicate-check, and tell ADV the choice and its rejecting observation. The unassigned candidates are IT48-Q01 (third route, forward citations, not a string set) and IT46-Q07; the open-questions map is stale in places (RS-R6 and IT44-Q03 were stale and are corrected): check a row against the records before building on its blocking text.
3. Landing: from a clean worktree, `python3 scripts/test_fresh_clone_reader_journey.py` (2 s) BEFORE the push (inline relative paths; `public_release_gate.py --paths` does not catch a wrong one), then `safe_push.py development main --expect-sha <sha> --serialize` run in the background with a monitor; do not edit the worktree during a gate; detach to `development/main` and `git branch -d` after.

## 5. Facts learned this window
* A brief that sits in `experiment_brief_presidio013_sci_20261116/invivo_pup_adv059_sci_20261118/` reaches the advisor pilot folders by `../../advisor_pilot_20261113/`; the R4 lever table sits next to the brainstorm folders and uses `../`. My first lines in the brief used the wrong depth and kept a test red on main until HE named it.
* A sed over a file touches a peer's line too; check `git diff -U0` before committing.
* A consumer instruction can be superseded by the producer's own correction before it lands (ADV-136: the "Dead lane" survival contrast); write the first wording as a dated line so the correction is a second dated line, old text kept.
* Europe PMC `supplementaryFiles` returns supplementary figures as TIFF (ImageMagick `convert` makes a PNG for viewing); n per arm must then be counted from the dots and said so.
* The open-questions map can lag the records: RS-R6 (HE ran the lookups on 2026-11-17) and IT44-Q03 (A1.15 gives 2 mM Na2ATP and 10 mM glucose in the incubation ACSF) were answered or narrowed while the blocking text said otherwise.
* Same-family limit: no native specialist reader exists for us; every verification in this window is a different delegate of the same model family.
