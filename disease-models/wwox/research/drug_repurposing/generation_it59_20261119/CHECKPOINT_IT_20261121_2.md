# IT checkpoint 5, 2026-11-21 (IT Orchestrator successor window O; ACTOR_ID orchestrator; mandate ORCH-ROADMAP-IT59-20261119; written at ADV's request after the ADV-131 report, context about 330k tokens)

Reply to the operator in Italian, write files in English. This file is read by the next window; nothing here is a result. Model and effort: this window ran on Sonnet 5.5 (census: effort high on every turn); every delegate was dispatched as sonnet at effort high, stated in each dispatch, read back from the transcript.

## 1. Landed in this window (gate PASS, ls-remote verified)
`d2c483dcd` and `2cba88d26` notes on HE's full-edition leads and ADV's ADV-130 decision (section 8 and 9 of `NIGHT_20261120_N1_RECONCILIATION_IT.md`) · `78e79ace3` ADV-131: 50 English-authored shareable passages translated to fr, de, es (`adv131_english_batch_it_20261121/RESULT_ADV131_IT_20261121.md`; renderer: `en_scope.json`, `localize_english_scope`, HE reviews it). The release battery on that tree: 269 of 270 suites green; the red is `test_repurposing_view` with the two known item-17 name reds. ADV read the ADV-131 report and accepted it as measured.

## 2. State of the mandate
Step ADV-131 DONE with evidence; step ADV-132 accepted (IN_PROGRESS); step 6 (operational continuation) stays the standing step. Reserved to the operator: items 17 and 18 (and 9). Nothing here decides them.

## 3. ADV-132 (the work in progress; assignment text: the Advisor's message of 2026-11-21, `assignments/ADV-132.md`)
Done and committed on branch `task/it59-adv132` (not yet pushed when this was written): the parity rule and checker (`adv132_dense_batch_it_20261121/`, rule committed before any run); run 1 on the 150 ADV-131 rows: 27 rows flagged, 29 flags, all FALSE POSITIVE, 0 real drift, no number flag (`PARITY_RUN1_RESULT_IT_20261121.md`); the selection rule v1 (its output `selected_batch3_v1_not_used.json` rejected: 18 of 25 were identifier lists) and v2 (written before it was run), run: `selected_batch3.json` (25 passages numbered 51 to 75, 21,641 characters: 7 `priorities-cur`, 17 `ranking`, 1 `hypotheses`; four are underscore-tag strings, copy the tags and translate only the prose between).
To do, in order: (a) translate the 25 into fr, de, es (`batch3_translations.json`, keys 51 to 75), run `parity_check.py` on every row, classify each flag, repair a real drift before the check; (b) `EN_SCOPE_SECTIONS` gains `hypotheses`, `priorities-cur`, `priorities`, `leads` (one line), `en_scope.json` gains the 25 hashes (`apply_translations.py` and `make_pairs.py` of the ADV-131 folder work on a selection file with `n` and `hash`; use `selected_batch3.json`), `i18n --what collect`, `run --source full --lang all`, `run --source shareable --lang all`, `package`; (c) blind check by one sonnet delegate at effort high on the pairs file (75 rows), third look on any repair that changes more than a word; (d) parity again after repairs; (e) painted before and after for the touched sections (`adv131_english_batch_it_20261121/painted_count.py`, pages copied to a non-hidden directory under the home, `TMPDIR=$HOME/legend_browser_tmp`); (f) tests: `test_repurposing_view_i18n.py`, `check`, `package --check`, then the battery with `TMPDIR=$HOME/legend_browser_tmp` set (without it the snap Chromium hangs: ADV found my first battery hung for 2.5 hours); (g) the report to ADV (parity flags and classification, rates, cost, whether the rejecting observation occurred — a CHANGED row on a long number-bearing evidence sentence — and one updated projection paragraph); tell HE before pushing the renderer line.
STOP RULE (unchanged): CHANGED above 5 percent of the 75 rows, or any CHANGED row that alters a number, a limit, a hedge or a negation, stops the work; repair, report, nothing further. Nothing beyond the 25. The ranking notice stays HE's.

## 4. Open items, owner, named event (as checkpoint 4, with the changes)
| Item | Owner | Event |
|---|---|---|
| Package and `package --check` on the final tip; card-text folds; the Wwox EM label (`needs/needs.json` line 502, then regenerate in one pass); the Italian compound name `4-PBA / acido fenilbutirrico` in the data object if HE asks | IT | operator's item 17 |
| WM103 part 2 and CLAIM 011 Title and BLOCK 2 row | operator | item 18 |
| Seven matching-pilot cases in other languages; the fr/de/es full-edition translation beyond the 50 (and the 25 of ADV-132) | IT, only if the operator or a named reader asks | a request |
| Section-notice wording for a half-translated section (`sec_en_src`), the static guard for the scoped passages | HE | HE's list |
| `--gene-anchor` default; NP4G2 independent reproduction | HE; open question | their own events |
| Portfolio RP-011, RP-013, RP-029 | ADV | their own events |

## 5. Facts and recipes learned (add to memory note `it-successor-o-20261121-pitfalls`)
* A battery run without `TMPDIR` under a non-hidden directory of the home hangs on the snap Chromium (the log stops, the child `test_repurposing_view.py` lives on); stop by exact PID, relaunch with `TMPDIR=$HOME/legend_browser_tmp`.
* The catalogue is hash-keyed: a translation reaches every identical node of every section, so a scoped trial needs a section filter (`localize_english_scope`); an early `return` for `en` made the English page show Italian-authored passages (found by diffing the regenerated pages).
* A verifier's own repair wording can introduce a CHANGED row ('structural' added to 'unrelated', 31-FR): look again at repairs that change more than a word.
* Selection by a score can be dominated by an artefact (hyphenated capital identifiers): look at the list before translating, and when the rule changes keep the first output and write the new rule before running it.
* `safe_push` after the merge of `main`: the gate takes about 5 minutes; do not touch the tree meanwhile. `task_close.py` refuses when `main` is checked out in no worktree: detach at `origin/main` and `git branch -d` after `merge-base --is-ancestor`.
* Delegates: 40k tokens and about 55 seconds for 75 rows (8k output); the main window's cache-read figure (7.5 M for 38 turns) is the long context, not the task.

## 6. First steps for the successor
1. Read the router, the state manifest (`current_state: READY`), sections 21c, 21d, 21e, `roles/orchestrator.md`, this file; verify the digest of this file from the report message that follows it.
2. Bind the mandate (`MANDATE_BOUND: ORCH-ROADMAP-IT59-20261119` as its own text block, then a tool call; `handoff` is the proof).
3. Continue ADV-132 at section 3 (a); nothing on the package before item 17; no frozen candidate is touched.
