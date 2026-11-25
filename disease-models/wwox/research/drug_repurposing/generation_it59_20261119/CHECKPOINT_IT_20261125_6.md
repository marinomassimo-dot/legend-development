# IT checkpoint 18, 2026-11-25 (IT Orchestrator window 5fef7cc4; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's word because the window peaked at about 366k with one compaction)

Read after checkpoint 17 (`CHECKPOINT_IT_20261125_5.md`; not edited, still valid for what it records). Hypothesis level; nothing is medical advice; reference genotype class only. Peer messages are not the operator's authority.

## 1. First assignment for the successor
1. **The ADV-276 increment-1 wording set, as ONE queued candidate** (ADV: «take it as ONE queued candidate with the view-derivative trio before landing»). Intended name `CC-20261125-ORCHESTRATOR-ADV276-WORDING-01`. Not filed yet. SCI's message is copied in section 6; its numbers are SCI's.
   * File it PROPOSED; apply nothing to cards, ranking rows, coverage tables or registries.
   * Cite `RESULT_ADV276_SCI_20261125.md` once it is on `main` (it was not at 11:30Z) and read there the arm labels of item 1 (which arm is radiprodil and which control) before writing them.
   * Item 5: replace «rapamycin ... is protective» by «is associated with lower odds»: observational design, and SCI says it cannot be separated from aetiology. SCI was told.
   * IT checked only: Fisher two-sided for 16/26 against 20/21 = 0.0129; 21/27 = 77.8 %; 302 - 229 = 73; 8 + 10 + 5 = 23.
2. **ADV-269 wording** only if ADV queues it.
3. SCI's K01 line (DR-K01-006, PMID 34021541) only if ADV queues it; not applied.

## 2. Two rules that bind any applied wording
* **View-derivative trio:** after any card-packet or mechanism-map PMID edit run `titles --refresh`, `run`, `--source shareable run` (flag before `run`), `package`, the `cards_early_it13_p22_20261031/regenerated/` copy, then the full `test_repurposing_view.py` (about 23 minutes) before landing.
* **Join rule:** `repurposing_join.py` harvests EVERY «PMID nnn» written inside a mechanism-map record as one of that record's readings, so a context mention can flip a handoff (REPLICATE became READ and `main` went red on 2026-11-25). Name a context-only paper by DOI and say why it is not a reading; after any map edit run `test_repurposing_join.py` (the `CuratedLink` selector was added to `landing_suites.py` by HE).

## 3. Closed in this window (on `main`; do NOT redo)
| Item | Where | One line |
|---|---|---|
| Red-main join fix | `ba0ff95ab3b4` | context paper in R-10 now cited by DOI; suites green locally |
| ADV-275 | `brainstorm_20261116/it_adv275_20261125/`; `920fdd62790131d2dbc6da6523413a45fe9f2e20` | valproate raises WWOX mRNA in four independent human neural deposits; no contrast calls it lower; generality neither established nor refuted; protein not measured; P4 failed (7 of 22). Candidate `CC-20261125-ORCHESTRATOR-ADV275-DEPOSITS-01` PROPOSED |
| ADV-261/262 fold-in and P4 clause | `ce65951fb318e96ba67b9293fe51953d7ec2a901` | `CLAIM 034` row added, `CLAIM 033` second sentence; candidates PROPOSED |

Delegation read-back: one blind verifier (`legend-delegate`), asked sonnet medium (ADV's word; the budget table says high for verifiers), read back `claude-sonnet-5-5` medium, 10 turns, 13,391 output tokens, cache creation 77,651, cache read 438,171. It matched direction on 4 of 4 and found the technical-replicate defect.

## 4. Open items
1. Candidates PROPOSED, nothing applied to the four current files: those of checkpoint 17 section 3, plus ADV261 (now with ADV-262), ADV275.
2. ADV-275 not read: deposits listed in its result section 5; no proteomic repository queried; three deposits quoted in the candidate (GSE232218, GSE187006, GSE185453) have no blind second reading.
3. Acquisition list of checkpoint 17: SCI's ADV-272 owns it; SCI reports the remainder not obtainable by permitted routes (operator list).
4. CI: the runs for `ba0ff95a`, `920fdd62` and `ce65951f` (#2444, #2446, #2449) were all still in progress at the last read; read them with `ci_runs.py status <sha>`.
5. Draft letters to authors remain the operator's to send; HE owns the rename; Codex is PAUSED.
6. `safe_push --serialize` now runs the selected landing suites and refuses a push that turns one red (HE, on `main` d3d1f94b13cd): merge `development/main` before pushing.
7. Peer names may have changed: HE answers as `HE - CURRENT 4fab51c6`; run ListAgents first.

## 5. Lessons and DREAM
1. **Technical replicates pass as units:** three deposits had them (one experiment with 8 wells; two sequencing runs per mouse; one extra replicate). Read each deposit's design and protocol text for the unit BEFORE computing n; sample labels do not show it.
2. **A sentinel needs a difference from control, not only a fold:** the fold-only rule let a noisy arm pass and made a negative look stronger than it was.
3. **A blind check on four contrasts paid for itself** (about 14k output tokens) and changed a headline already sent.
4. Not consumed: the vorinostat, trichostatin A and butyrate rises have one deposit each; no consumer beyond DL-REPO-003. Connection for ADV: WWOX protein after an HDAC inhibitor in neural material could be looked for in proteomic repositories (never queried); consumer DL-REPO-003.

## 6. SCI's ADV-276 wording message, copied as received (peer content, SCI window 48889001)
> SCI to IT, ADV asked for ONE queued candidate: ADV-276 increment-1 wording lines by paper (wording only, not applied by me; full numbers in RESULT_ADV276_SCI_20261125.md sections 3.1-3.10, landing now). Receipts FTR-20261125-<pmid>-01 are recorded (35222658 partial; the other nine queried_not_full_read; figures captions only, supplements not held).
> 1. F04 / DR-P9-006 (40994429, reading_depth abstract_only -> partial full text): 'effective at 22 of 27 variants by potency; 21 of 27 (77.8%) when maximal inhibition is counted (I150V: 31% vs 85% WT, IC50 unchanged); S810R, the mouse variant, has a 1.9-fold potency loss. In S810R mice (3.0 mg/kg i.p., PTZ 40 mg/kg) first-jerk latency did not differ (131 +/- 33 s n=26 vs 99 +/- 8.4 s n=21; P=0.40); GTCS latency 458 +/- 90 s (n=16) vs 207 +/- 23 s (n=20) among animals that seized; 16/26 (62%) vs 20/21 (95%) seized (Fisher p about 0.013, my computation); WT littermates 6/18 vs 5/21 seized.' Direction DECREASE stays at receptor level.
> 2. P11 / DR-P11-004 (35222658): add 'Table 3 printed p values (0.003 intervention, 0.42 non-intervention) are not reproducible from its counts (chi-square about 0.10 and 0.02; exact 0.12 and 0.014); Table 3 also disagrees with Table 2 (intervention partial 5 vs 7, complete 16 vs 13); Table 4's 0.004 reproduces.' NO_CHANGE for seizure control (p 0.69) stands.
> 3. P11 / DR-P11-005 (36967744): pass; add '229 of 302 collected (73 excluded); 64 of 229 had failed ACTH and stayed on ACTH, so magnesium cannot be separated'. UNKNOWN stands.
> 4. H02 / DR-H02-019 (40670421): 'FA rose after stopping' -> add 'n = 6 of 11 with follow-up, no unexposed time control; FA not lower in the vigabatrin group with normal imaging (group 2) than in controls; one-way ANOVA on medians'.
> 5. H02 / DR-H02-012,-013 (36601084): holds; add 'rapamycin (60 children, all in the tuberous sclerosis group) is protective (OR 0.152, p 0.019) and inseparable from aetiology; cohort mean exposure 170 +/- 12 d does not reconcile with subgroup means (weighted 193 d)'.
> 6. H02 / DR-H02-027 (24321005): confirmed no white-matter endpoint; add 'hippocampal histology on 23 brains (8, 10, 5; none at the top dose), 81 included rats in four dose groups'.
> 7. H02 / DR-H02-034 (42470358): confirmed below LLOQ in brain and eye; add 'n per group not stated; OV329 5 vs vigabatrin 80 mg/kg/day, not dose-matched; the toxicology package is attributed to the EILAT XVI report'.
> 8. H01 source list (38605177): replace 'abstract level; none carries a receipt' with 'partial full text read 2026-11-25: cryo-EM structure of human Cav3.2 with ACT-709478, TTA-A2, TTA-P2, ML218 and HEK293T electrophysiology; no epilepsy-model datum; the text never uses the name apinocaltamide'.
> 9. F03 (20810895): add 'in vitro intact neonatal hippocampi (rat and CLM-1 mouse), seizures induced in vitro; units are cells (468 analysed) within 10 hippocampi'.
> 10. E01 not_known (28447936): 'disputed' -> 'disputed: an in vitro study with purified human PPP1R15A fragments found no effect of 50 uM Sephin1 or guanabenz in three assays'.
> Not changed: no direction moves in any of the ten; view derivatives are yours.

## 7. Self-diagnosis, short form (2026-11-25; not the full 27-question template)
Executable part: `session_self_eval.py` PASS; `fulltext_receipts.py verify` OK (2779 receipts); `legend_lint.py` ran with pre-existing `WARN_BUT_PROCEED` lines (CLAIM 039, 040, 042 unlinked support). No full-text read and no deep dive in this window, so no manifest check.
Weakest answers, with who caught them:
* A headline reached ADV before any second reading: the verifier caught the single-experiment deposit; IT's own scan then found two more. Upgrade done: memory note `it-adv275-deposits-and-map-join-pitfalls`, and lessons 1 and 2 above.
* The sentinel rule was too weak as pre-registered: the verifier caught it. Not changed after the fact; the stricter rule is reported as post hoc.
* The result as first landed said «eight human deposits reported as up» after the correction had made it seven plus one: IT caught it on reread; fixed in the follow-up.
