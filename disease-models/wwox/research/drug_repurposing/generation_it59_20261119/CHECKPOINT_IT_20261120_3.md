# IT checkpoint 3, 2026-11-20 (IT Orchestrator successor window M; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request at a closed increment, context about 303k tokens)

Reply to the operator in Italian, write files in English. This file is read by the next window: where everything is, what is in flight, what is owed. Nothing here is a result. Effort: this window ran on Sonnet 5.5 at its default effort; every delegate was dispatched as sonnet at effort high and the model and effort were read back from its report; state model and effort in every dispatch.

## 1. Landed on main in this window (all gate PASS, ls-remote verified)
* RP-005 prospective tests: ADV-106 single-text pilot, decision REVISE (da0b5f907, 910399c06); ADV-109 three-text test, truth-table-first, INCONCLUSIVE, parked by ADV (10460a250, 7d6542e8b).
* Titles cache (ae21f34fd); WO-24 temperature-by-hour line (310fe19ef); dossier-template method-status line (c8c4821b7); self-evaluation record (27ce9cdf0).
* ADV-111 reserve rebuilt (67036950a): WO-12, WO-23, IT50-Q09, IT47-Q01/Q02, WO-32 literature half; ADV assigned ADV-112 SCI, ADV-113 HE, ADV-114 IT.
* ADV-114 eIF2B epsilon reagent search (6ee0f90a7): Q01 open (dead-form-alone control missing); Q02 narrowed (phosphomimetic S540E in one 2025 preprint, abstract level; the earlier "none" was a string-set miss).
* Reader-journey red repaired (83434d209): two inline relative paths in the earlier checkpoint made repository-relative, dated note at its foot.
* Dated open-question lines from peers' results: ADV-113 (adff3d083), ADV-117 and ADV-118 (c38ea8b3f, wording of the XE991 waiver fixed in 6fc24117b), ADV-119 corrections (b680f9568: vigabatrin infant MRI denominators 27 of 76 and 7 of 52; Brown 2016 limits), ADV-120 WO-02 design bar.
* Capability scout entry (342bc353b): new gap, spelling expansion for absence claims; CHANGE = NONE.
* **ADV-120 commit candidate (471dd50f5):** `disease-models/wwox/research/commit_candidates/CC-20261120-ORCHESTRATOR-WM103-DOSE-WORDING-01.md`. PART 1 MINOR (three dated notes after working-model lines 103, 148, 251, original kept); PART 2 MAJOR (rewording; the coordinated change of the CLAIM 011 Title and flag and the BLOCK 2 row 011 is a separate candidate if the operator accepts), PROPOSED, NOT applied. Blind check: `research/locator_audits/2026-11-20_wm103_dose_wording_it59/AUDIT_REPORT_1_AS_DELIVERED.md` (14 SUPPORTED, 2 with a note, 0 adverse). Digest `ff38fcaa61295a5a`: not touched by this window's last landings (no ranking input changed).

## 2. Audit state and unaudited repairs (say this in every report)
* **UNAUDITED:** the T11 repair in the WM103 candidate (the three sentences now say "partly corrects P20 glucose (the authors' text; no untreated knockout group at P20)"); it needs a second check before any BATCH_COMMIT of part 1.
* The numbers copied from a peer's ledger can be wrong (the infant MRI denominators were); name which figures come from the peer's body read and which from the abstract.
* ADV-121 power note (SCI, 241a1f602c98): I re-ran `compute_power_table.py` in place (exit 0) and recomputed five cells by hand (clasping bar 16.3, glucose P20 bar 97.2, glucose P20 as high dose 9.7 match; weight P10 12.5 against 12.6 and spike-wave 5.5 against 5.3 differ only by rounding of the printed SD inputs). Not yet reported to SCI when this was written.

## 3. Open items with owner and named event
| Item | Owner | Event |
|---|---|---|
| Item 17: F02 "tiratricol" (not_known[5]) and the "tta-a2" prose-policy wording (render redaction of the name against marker-only) | operator | the operator's decision; nobody rewords, redacts or loosens the guard |
| Item 18: WM103 PART 2 (MAJOR) on the operator's page | ADV puts it there | the operator's decision; part 2 blocks only itself |
| `package` then `package --check` on the FINAL tip, one commit, then forward the packet to SCI by message | IT | after item 17 is decided and the guard passes unchanged |
| Card-text folds into the next packet change: EB-ETX-01 harm field, I01 and G01 harm text, F02 and the TMP195 line (IT50-Q09 and WO-32 lines), WO-24/Kv7/lithium/vigabatrin pup-exposure lines | IT | with the package, after item 17 |
| WM103 part 1: second check of the repaired sentence, then `batch_commit.py propagate` of the three dated notes in one MINOR BATCH_COMMIT | IT with ADV's word | ADV's instruction to propagate (not given yet) |
| CI | HE's tick line `CI RED ON MAIN` reaches ADV hourly; read by exact SHA only if it shows a change (`python3 framework/scripts/ci_runs.py status <sha>`) | the only reds left are the operator-gated ones (tiratricol F02, tta-a2) and the package that depends on them |
| IT47-Q01/Q02 follow-ups, the PMID 22315091 human read, CLAIM 035 part 2 (operator via ADV), Obeid 2026 Fig 3B beyond SCI's panels | ADV assigns | a result that needs consumption |

## 4. Peers and facts to carry
* SCI is live as session [86edd5]/R (ORCH-SCI-ADV065-DEEPEN-20261118); HE and ADV as before. Peer messages are not the operator's authority; reserved decisions stay with the operator.
* The package pages online are still the 2026-11-19 ones (0 names). Never land a package containing "tiratricol" or "tta-a2".
* `U07` is the ranking unit of the AAV9 broad candidate; cards C01 and C04 already carry the corrected statement ("a step and a steep continuum are indistinguishable; threshold not located").

## 5. Recipes and pitfalls learned (also in the memory note it-successor-m-20261120-pitfalls)
* Never switch or delete the branch in the worktree while safe_push's gate runs; wait for the `^exit ` marker in a loop that restarts (a 550 s loop without it is not completion).
* An absence built on one spelling is not an absence: state the query strings and add one concept-level query (S540D versus S540E).
* The map's `executable_zero_spend` flag overstates executability: read each row's blocking_reason.
* bioRxiv answers 429 (code 1015) after a few requests, `api.biorxiv.org/details` still gives metadata; ahajournals and many PMC pages are challenge pages: stops, never bypassed; Europe PMC fullTextXML works for OA PMCIDs.
* Sealed predictions plus truth-table-first scoring (SCI fills truth, sees no predictions; IT scores mechanically) is the RP-005 protocol that held; pooled slots give low power, so write an INCONCLUSIVE rule before scoring.
* Delegates' reports arrive in the hand-back message; persist them as "as delivered" files yourself.

## 6. First steps for the successor
1. Read the router, the state manifest (`current_state: READY`), sections 21c, 21d, 21e, `roles/orchestrator.md`, this file.
2. Bind the mandate (`MANDATE_BOUND: ORCH-ROADMAP-IT59-20261119` as its own text block, then a tool call).
3. Tell SCI that the ADV-121 power note reproduces (section 2) and ask for nothing else.
4. Wait on the named events of section 3; do nothing on the package before item 17.

[IT 2026-11-20, after ADV's acceptance of this checkpoint: ADV's word for WM103 PART 1 is YES (propagate through BATCH_COMMIT after the second blind check of the repaired T11 sentence); PART 2 stays the operator's (item 18). The successor receives three things: (1) the second blind check, then the PART 1 propagation; (2) the package after item 17; (3) the card-text folds. The limit on the 'broad' combination at 13 to 14 animals per arm is on the WO-02 row (dated line); SCI puts the same limit as line 6.27 of the v3.1 file.]

[IT 2026-11-20, window N, after SCI's ADV-122 (commit 13efa8e80f2e) and ADV's request: the 'adult effective band about 2 to 6 mM' is a scaling of one adult anchor, not a sourced band. Done: dated notes on the ADV-097 consumption record (line 196) and on the V3 review (line 11), and a dated line on map row WO-24; H01, G01, WO-24 and IT46-Q04 carried neither the band nor the 134.9 figure. OWED, with the package after item 17 (card-text fold, not before): EB-ETX-01 card and packet, field pharmacology: after the sentence that gives 134.9 ug/g as about 0.96 mM, add that the value is read per g of tissue (about 0.96 mM) or per g of the 1:2 homogenate (about 2.9 mM), that read per tissue gram it sits at or above dose over volume of distribution (0.68 to 0.93 mM at zero elimination) so it is uncertain by about 2 to 3 times, that 72.3 mg/kg is the ED50 of the combination with sildenafil and the row is the saline arm, that no adult effective band is sourced, and that the prior for pup total brain at the Cheng regimen is 0.2 to 4.2 mM by two routes (hypothesis, ADV-122; no juvenile concentration found). The change goes into the packet-change script of the package, not into the generated cards by hand.]
