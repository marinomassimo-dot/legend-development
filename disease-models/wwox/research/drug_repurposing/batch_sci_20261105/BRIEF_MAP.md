# Brief MAP (label `sb-map`): reconstruct the open questions of the Drug Repurposing module and the state of each search

Read `BRIEF_COMMON.md` for the constraints (write only in your directory, no commits, no ledger writes, never `cd` into another worktree). You read papers only if a status cannot be decided otherwise; no receipts are required from you. Your directory: `disease-models/wwox/research/drug_repurposing/batch_sci_20261105/map/`.

## Task

Build the map of every open question of the Drug Repurposing module, and for each one decide, from files and git history, whether its search is concluded, in progress, claimed by this batch, or open, **and where it is published**: on `main` (14c5fc7b), only on the branch `task/it29` (d099a5be), or only on the branch `task/it30` (the IT30 session, still working; its head moves, so read the ref at the time you read and write the commit you saw). Read other branches only with `git -C /home/desktop/legend-development show <ref>:<path>`, `ls-tree` and `diff --name-only`; never enter or write the worktrees of IT29 or IT30.

## Sources of questions (read all; each row cites its source file and anchor)

1. `disease-models/wwox/research/drug_repurposing/view/work_order.json` (`entries`, 15 needs).
2. `ranking_it8_p9_20261029/ranking.json` key `investigations` (INV-01 to INV-10) and `uncarded_items.tsv` (N01 to N18, with `what_would_reopen`).
3. Every `reopen_searches*.tsv` and `triggers.tsv` in the module (for example `recovery_it10_p23_20261031/reopen_searches.tsv` R1 to R9, `function_pharm_it14_p3_20261101/reopen_searches_it14_p3.tsv`, `functional_it13_p3a_20261031`, `target_first_it15_qa_nmdar_20261101`, `target_first_it15_qb_gsk3_20261101`); find them with `git grep -l "reopen"` limited to file names matching `reopen`.
4. The challenges: `ledger/tasks/orchestrator/ORCH-ROADMAP-IT28-20261105.json` (on main: CH-IT28-HDAC5-LEVER, CH-IT28-ISR-ROLE) and, from the branch, `ORCH-FRESH-IT29-P10-20261105.json` (CH-IT29-CLASSIIA-CNS-MYELIN).
5. The IT30 task record on its branch (`git show task/it30:ledger/tasks/orchestrator/ORCH-ROADMAP-IT30-20261105.json`): steps S0 to S14 and their status.
6. The "Next:" and residue lines in `roadmap_current.md` (end of file and Standing method), the IT29 residues (`phenotype_first_it29_20261105/p11_residues_README.md`, `p14_verify`, `p12_scout`, read on the branch `task/it29`), and the two radar items "to examine" (`python3 framework/scripts/scout_daily.py --plan` prints the derived plan with origin; run it once, it only reads).

## Decide, per question

Columns of `open_questions_map.tsv`, in this order: `qid, source_ref, question_text_max300, decision_at_stake_max200, kind, status, published_on, status_evidence, last_touched, blocking_reason, executable_zero_spend, claimed_by`.
* `kind`: wet_lab_measurement | literature_executable | data_access_blocked | engine_or_infrastructure | decision | monitor.
* `status`: CONCLUDED | IN_PROGRESS | CLAIMED_THIS_BATCH | OPEN | SUPERSEDED. `published_on`: main | task/it29 | task/it30 | not_applicable.
* `status_evidence`: file path with an anchor, plus the commit that introduced the concluding record (`git log --diff-filter=A --format=%H -1 -- <path>` on the right ref; write the full 40-character hash). "Concluded" means a record answers the question at the depth the question needs; an abstract-level pass that lists the full-text data as "not found" is **partly** concluded and the row says which part is open.
* `claimed_by`: write `CH-SB-CONCORDANCE` for questions about symptomatic response versus developmental outcome (INV-10, work order `NEED-SEIZURE-CONTROL-SYMPTOMATIC`), `CH-SB-VGB-WHITEMATTER` for the vigabatrin and CPP-115 white-matter question (`NEED-MYELINATION`, card H02), `CH-SB-POSTONSET-RESTORATION` for INV-01 and the `NEED-WWOX-GENE-ADDITION` window states; leave empty otherwise.
* Do not classify by your preference: when two readings are possible, give the one with the stronger file evidence and name the other in `blocking_reason`.

## Also deliver

`README.md`: answer first (counts per `kind` and per `status`; the five open questions that are executable at zero spend and not claimed by this batch, with the evidence that nobody has run them; the questions that look open but are concluded, with the record that concludes them); a short section on what is published on `main` versus only on the IT29 and IT30 branches; and a list of any contradiction you found between records (for example a heading marked CURRENT that is older than later verified work). Plain backticked paths, no markdown links to files. Final message to the Orchestrator: the counts, the five unclaimed executable questions, the contradictions, and anything you could not decide with the reason.
