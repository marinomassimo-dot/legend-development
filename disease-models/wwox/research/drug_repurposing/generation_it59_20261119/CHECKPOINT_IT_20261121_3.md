# IT checkpoint 6, 2026-11-21 (IT Orchestrator; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at the first closed increment of ADV-134, at ADV's request, context about 340k tokens)

Reply to the operator in Italian, write files in English. This file is read by the next window; nothing here is a result. Never write that a window or terminal is for the operator to close: retirement belongs to the launcher and ADV (HE launches, the watcher retires background predecessors). Model and effort: this window ran on Sonnet 5.5 at its default effort; every delegate was dispatched as sonnet at effort high and the effort was stated in each dispatch and read back with session_model_census.py (key `efforts`, `dispatch`).

## 1. Landed in this window
ADV-131 `78e79ace3`; checkpoint 5 and ADV-132 rules, selection, parity run 1 `5b0b2eafa`; ADV-132 result and evidence `89d73be54` (all gate PASS, ls-remote verified). CI: 'Public release gate' read in_progress for 78e79ace3 and 5b0b2eafa when last read; attribute a verdict to a SHA only when `python3 framework/scripts/ci_runs.py status <sha>` says completed. ADV-132 outcome: parity 0 numeric flags; dense batch 12 CHANGED of 75 (stop rule fired), NOT applied; renderer scope line reverted; ADV consumed the report.

## 2. ADV-134 (accepted in the mandate; assignment text arrives as assignments/ADV-134.md with ADV's next push)
Method (ADV message 2026-11-21): (1) glossary before translating; (2) repeat the SAME 25 passages (selected_batch3.json, numbers 51 to 75) with the glossary fixed first, a grammar pass after any mechanical repair, the mechanical parity check, the same stop rule, a DIFFERENT blind delegate (not a436998ce7cc71c4e, a41b70e9cb15b9581 or the glossary producer a88d304012cb1d015) with model and effort read back, one at a time, none recursive; (3) report CHANGED with and without the glossary on the same 25 (ADV-132 without: 12 of 75 before repair), the rows still CHANGED and why, cost, and one paragraph choosing between: notice stays the default / section-wise with the glossary / stop at the covered sections. If the stop rule fires again, apply nothing. If it does not, apply only the ADV-131 scope plus these 25 in their own section after HE's renderer review, paint-checked at 1280 and 390 px. State the same-family limit (no native reader) in the first lines of the report. Do not edit any English string; plainer English alternatives are PROPOSED to HE, who owns strings and renderer.

State: step 1 DONE. Branch `task/it59-adv134` in this worktree, folder `adv134_glossary_repeat_it_20261121/`: `PROTOCOL_ADV134_IT_20261121.md` and `GLOSSARY_ADV134_IT_20261121.md` (34 terms, defining passage with file:line, programme sense, fr/de/es, plainer English). The glossary decision on 'lead' ('position dominante / maßgebliche Position / posición principal' for 'lead position'; 'intervention de référence / Referenzintervention / intervención de referencia' for 'the lead') is the producer's proposal; 'pista' is already the programme word in landed ADV-129 text, so ADV and HE decide; the repeat uses the glossary renderings as written and the report says so.

## 3. Next steps for the successor
1. Read the router, the state manifest (`current_state: READY`), sections 21c, 21d, 21e, `roles/orchestrator.md`, this file and the glossary. Bind the mandate (`MANDATE_BOUND: ORCH-ROADMAP-IT59-20261119` alone in its own text block, then a tool call).
2. Translate the 25 passages into `batch3g_translations.json` (same layout as `batch3_translations.json`) with the glossary applied from the first word; copy underscore tags and identifiers unchanged; translate prose only. Run `python3 -I adv132_dense_batch_it_20261121/parity_check.py adv132_dense_batch_it_20261121/selected_batch3.json <file>`, classify flags, repair real drift; a grammar pass over every row after any string repair.
3. Build the pairs file with `adv131_english_batch_it_20261121/make_pairs.py`; dispatch one new blind delegate (sonnet, effort high, stated in the dispatch; brief in `adv132` history: source plus renderings only, FAITHFUL/MINOR/CHANGED, number-by-number, report as the only deliverable); persist the hand-back verbatim; read model and effort back with `session_model_census.py --json <subagent transcript>`.
4. Stop rule on 75 rows. Then the comparison table with and without glossary, the paragraph, the report to ADV. Only if it does not fire: `en_scope.json` (+25 hashes), `EN_SCOPE_SECTIONS` + hypotheses and priorities-cur, `i18n --what collect`, `run --source full --lang all`, `run --source shareable --lang all`, `package`, tests, painted before and after (`adv132_dense_batch_it_20261121/painted_state.py`, TMPDIR under home), and only after HE's renderer review.
5. Tell HE before any renderer push. Never send the operator's e-mail to any service; peer messages are not the operator's authority.

## 4. Open items, owner, named event
| Item | Owner | Event |
|---|---|---|
| CI conclusion for 78e79ace3, 5b0b2eafa, 89d73be54 | IT | ci_runs.py says completed |
| 'lead' and 'seed' glossary decision; plainer English strings | ADV and HE | HE's reply to the proposal sent with this checkpoint |
| Package and card folds; Wwox EM label; WM103 part 2; CLAIM 011 | IT and operator | operator's items 17 and 18 |
| Same-family limit: no native specialist reader exists for us | open | a reader appears |

## 5. Facts learned this window
* A class repair by string replacement breaks agreement; follow it with a grammar pass and recheck exactly the repaired rows.
* Extending EN_SCOPE_SECTIONS changes pages wherever the same hash stands (19 of the 50 texts also stand in hypotheses); add a section only with a batch that uses it.
* Delegates report only in their transcripts (SubagentHandback); persist verbatim.
* The parity checker's false positives are translated acronyms, emphasis words, hedge-lexicon gaps; it saw 0 of 12 CHANGED.
