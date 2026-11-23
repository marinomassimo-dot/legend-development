# IT checkpoint 9, 2026-11-23 (IT Orchestrator successor Q; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request at a closed increment, context about 292k)

Read after `CHECKPOINT_IT_20261121_5.md` and its addendum, which stay as written. Reply to the operator in Italian, write files in English. Never write that a window is for the operator to close. Never send the operator's e-mail to any service; peer messages are not the operator's authority. Nothing here is medical advice; reference genotype class only.

## 1. Mandate
`mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119` at 2026-11-23 04:45Z: CONTINUE, 2 executable steps remain; next OBJ_ACCEPTED[5] '6 OPERATIONAL CONTINUATION: verify recipient receipt, record consumption or refusal, make the next executable step visible to the advisor'; steps 32, TODO 1, IN_PROGRESS 1, DONE 30, BLOCKED 0, unreconciled 0.

## 2. Landed in this window (gate PASS, ls-remote verified), all on main; do NOT redo
| What | SHA | CI and served state |
|---|---|---|
| ADV-164 frozen sets; ADV-170 clauses; ADV-175 blind freeze, addendum, scores; ADV-176 freeze and result (ERBB4 pivot); DC-02 closure | c11cd22fd; 675d64f1b; e5514fdd9, e61159995, 634228f2d; 111f87655, c6d975d31; 4c4a901e5 | earlier windows' checks |
| ADV-182 combined landing (four clauses plus the Codex English dashboard branch 1c9b29337, one regeneration, English-only package) | 1e6c096fb | Pages #85 success; served page and both PDFs equal the tree (index 2bdd8de4, ethosuximide e28654ba, ketamine 2a316365) |
| ADV-186 (INV-16 Step 1 surface-readout clause with Codex's wording; IT59-Q01 question text shortened to the 300-character column plus ErbB4 sentence in status_evidence; RP-038 line NOT applied) | 6a9cc607e | Pages #87 success; served index 3e876366 |
| ADV-188 WO-17 clause with Codex return 29's wording (SCI/ADV earlier wording replaced before landing) | 5a7e886b8 | Pages #88 success, release gate #1993 success (ADV read); served index ca94f395 |
| IT49-Q04 read against Vay 2020 (NARROW, protein half only); receipt FTR-20261123-32248813-01 | 404203b2d | no package change |
| ADV-189 clause on WO-07 with Codex return 30's wording; optional ADV-190 pointer (Arce-Molina 2020); the no-row note | 834c8b301 | release gate #2002 in_progress at the time of writing; no Pages run expected |

## 3. The WO-07 clause as applied (map row WO-07, status_evidence; INV-07 explanations row 6 NOT touched)
Codex return 30's text: reduced pyruvate oxidation or ATP leaves the limiting step unresolved; matrix pyruvate dynamics reflect net entry minus utilization and any efflux; attribute the deficit to entry or PDH only with calibrated orthogonal measurements or perturbations in matched preparations, target engagement, precision and replication; entry by an independently qualified transport-sensitive contrast, PDH by directly measured active enzyme or state preserved at sampling; plateau or net slope alone, or overlapping entry and utilization controls = indeterminate; a normal net slope cannot establish normal import; a PDH-side control's direction is checked against active PDH; a missing rise can reflect compensation or limited dynamic range; ATP and oxidation corroborate. SCI's earlier wording was discarded. The ADV-190 pointer sentence (Arce-Molina 2020, PMID 32142409; depletion a lower bound on aggregate net utilization under a partial block; not a PDH flux) was SCI's OPTIONAL sentence, added as a separate bracket; ADV's spot check: the word 'efflux' does not occur in the paper.

## 4. The no-row note and the RP-003 method (do not repeat the screen)
File: `advisor_pilot_20261113/brainstorm_20261116/it_rp003_pick_20261123/RP003_FRESH_MAP_DIFF_IT_20261123.md`. Method: parse the map; OPEN rows by kind (166: 76 wet lab, 34 literature_executable, 21 monitor, 17 data_access_blocked, 12 engine, 6 decision); 47 flagged executable at zero spend and not wet-lab; screen each by the key input it needs, then a route check by PubMed key-tagged, free text and Europe PMC forward citations. Result: no further row qualifies as held source + named comparison + consumer. Rows named: IT44-Q02 (riluzole and fenamate potency on TREK/TRAAK; cloned-channel primary Duprat 2000 PMID 10779373 tracked and not open access; fenamate primary Takahira 2005 PMID 16075240 not open access; BL-1249 Pope 2018 already in generation_it44 verify_s11), IT44-Q05, IT49-Q08, IT45-Q04, IT47-Q02, IT48-Q01, IT49-Q09 (supplement or paper not reached), IT45-Q06, IT49-Q06, IT46-Q02 (already narrowed by the 2026-11-15 delegate readings). The pick of the window that did qualify was IT49-Q04 (landed). Resume condition: a non-open-access primary supplied or reached by an open-data route, or a new open paper touching a listed row from ADV or SCI.

## 5. Decisions in force that are in no other record
* English-only public Pages and no recurrent fr/de/es workload: relayed by ADV from Codex return 26 as the operator's ask; I did not find an operator-side record in the repository, so treat it as ADV-relayed. Consequence applied: only English was regenerated and checked (`content_en`); fr/de/es files were not touched; no test needed them.
* The RP-038 portfolio row is ADV's: my RP-038 line was dropped after three landing attempts were refused on research_portfolio.tsv conflicts; ADV added the pointer. Do not edit portfolio rows RP-033 or RP-038.
* Item-17 red turned green because Codex a92058522 added two prose redactions in `view/shareable_sources.json` (card_substrings 12 to 14); not a decision; reported to ADV. Items 3, 17 and 18 stay reserved to the operator; INV-15 wording stays.
* WO-17 and WO-07 clauses use Codex's refined wording, not SCI's or ADV's first text: when ADV says a clause went to Codex, hold the edit for its wording.
* A map row's text does NOT reach the shareable page; only the map's `last_touched` moves the page's data date. Ranking and investigations text does reach the views (regenerate English once).

## 6. Open commitments, running jobs, messages awaiting an answer
* Owner IT, next action: none executable in hand (map screen above). Running jobs: none (no PID, no log). Recall job: no IT recall job is held in this window; ADV owns the wake-ups.
* MEETING round about 05:35Z: send ADV one line each on (a) what I landed or hold (section 2; nothing held), (b) what I would run next if a source appeared (the first listed row whose key input arrives; IT44-Q02 if a cloned-channel primary is supplied; otherwise ADV's next assignment).
* CI: read the 'Public release gate' verdict of 834c8b30 (#2002) and tell ADV only if it is not success.

## 7. Lessons (transferable) and capability outcome
* Ending a turn after a report without doing the promised diff is an idle omission; do the named next step before stopping.
* A merge conflict on a file another actor edits in parallel repeats; after two refusals drop the contested line and let its owner carry it.
* Report a changed test result only after running it on both trees and diffing the built page.
* Capability outcome: CHANGE = NONE.

## 8. First moves for the successor
Read the state manifest, the three LEGEND_CORE sections named in CLAUDE.md, `mandate_continuity.py status --task ORCH-ROADMAP-IT59-20261119` and ADV's next message. First message quotes this file's digest, names the three next actions (MEETING reply, CI #2002 read, next ADV item) and the open jobs (none).
