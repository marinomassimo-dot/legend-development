# Checkpoint IT31 (session a39fdd2a), written 2026-11-28 at about 230k context

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119, bound by me (verified BOUND), effort read back high. Read `CHECKPOINT_IT_20261128_4.md` (IT30) only if a detail below sends you there; this file adds what happened after it. Operator brief LAB-RESUME-COMPOUND-FOLLOWTHROUGH-20261128 governs; Codex is never contacted.

## 1. Done in this window (all on development/main, gate PASS)
* ADV-286 design note, section 7 addendum: first-composition rates over ten IT28 to IT30 rounds, 43 of 124 MUST CHANGE (35 percent; mixed units; range 2/23 to 4/4; ADV-295 block 1 4/10 and ADV-298 1/8 recounted by me from the verdict tables; the pup-brief repairs 3/8 kept apart). Sidecar `FREEZE_ADV286_DESIGN_NOTE_IT31_20261128.sha256` (note at `9072758fc`).
* ADV decided (2026-11-28): no retrospective hold; RP-005 stays parked with the note as its record; build the C1 freeze. Built in `adv286_prospective_hold_it_20261126/c1_freeze_it31_20261128/`: six questions, input packet (`.txt`), scoring file, ENGINE and B0 answers (delegates, one at a time, sonnet, effort high stated), `FREEZE_C1.sha256` (first hashed 2026-11-28T10:01:32Z, re-hashed after the packet rename). One blind reader overturned 5 of 6 questions; repairs applied, not re-read. Section 8 of the note states the status line: prospective if the poster date is printed, otherwise unresolved. Poster read only after 2026-12-05 and only if retrievable with a printed date; unretrievable by 2026-12-12 closes UNRESOLVED, sealed answers unopened. A plain NIH RePORTER check (WWOX epilepsy) found nothing relevant.
* ADV-312 Z1 to Z4: held; SCI's ADV-313 (336110982) replaces Z1 and Z3 with K1 to K3. Two blind rounds on K1 to K3 (readers held the seven counted sources whole): record `adv313_consumers_it31_20261128/BLIND_ADV313_K_IT31.md` with verdicts, overturned table cells and proposed wording K1', K2', K3'. K lines: 1 of 3 MUST CHANGE, 2 of 3 ADD. NOT yet applied to any consumer file.
* CI, one look per SHA (curl, 2026-11-28 about 10:50Z): 2826 (931a8dc10) failed (stale sealed sidecar, repaired by 8c5fef3f3); 2827, 2828, 2830 success; the rest, up to 2843, still in_progress (queue backed up, each run about 45 minutes).

## 2. Open, in order
| # | Item | State |
|---|---|---|
| 1 | Apply K1' to K3' | consumers listed in the record: INV-06 `next_test` (then regenerate `ranking.json` first, then the view trio and cards copy), `continuous_compounds/clemastine/callosal_propagation.md`, sobetirome note line 14, H02 card (already consistent). ADV asked for a one-line decision before applying anything outside its wording; send ADV the proposed K1' to K3' first. Optional Cheng 2020 clause (Tc-MEP amplitude about 80 percent lower) from SCI. |
| 2 | ADV-286 dates | C1 re-check 2026-12-05 (poster); C2 not before 2026-12-06; entry closes UNRESOLVED 2026-12-12 if the poster is not retrievable with a printed date. Scoring by whoever opens the poster, no answer edited. |
| 3 | CI | look once more per SHA 2827 onward; a red run is read from the check-run annotations (public API, no login). |
| 4 | Self-evaluation (written part), capability scout, takeaways | Part 1 gate `session_self_eval.py` PASS on 2026-11-28 (two declared gaps on PMID 30361190 locators, not mine); the 27-question written part, scout and takeaways are owed for IT30 and IT31. |
| 5 | Later increments (IT30 list) | `meta_gaba_paradox_current.md` line 23 "P14-P18"; DL-MECH-027 migration vs Iacomino; DL-MECH-049 "Conferma e meccanizza DL-MECH-017"; ledger line 566 D-04; generated join files. J4 and ADV-308 stay closed. |

## 3. Rules and traps found this window
* `safe_push` that merges a new `safe_push.py` refuses once and asks for a rerun with the new SHA; the floor is now 1.5 GB.
* A markdown file with an inline `../path` in backticks fails `test_fresh_clone_reader_journey.py` (the gate does not run it); a verbatim extract that keeps a relative path should be `.txt`.
* A delegate's blind-check of a question list overturned 5 of 6 (options not exhaustive; a question that mixed an association with a mediation test; scoring file gaps): give the options an "other" and a stated classification rule, and name what makes a question unresolvable.
* Blind packets for a counterexample claim need the whole paper, its figures and the supplement; the plain-text conversion of PMC XML drops tables if they are image-only (STZ), say so in the dispatch.
* Subagent final reports are only in the hand-back message; the transcript jsonl cannot be mined for them cheaply: write the condensed record yourself and say it is condensed.
* Peers: ADV `a5e6f2ad`, SCI `5c296fab`, HE `a2763bd3` (re-run ListAgents). Operator rules unchanged: no spend, no contact with authors, Codex paused, never send the operator e-mail to a service.
