# Strategic Advisor follow-up: reliable inputs, measured cost, lightweight execution

Non-canonical working note. Not medical advice. Task record: `ledger/tasks/plan/PLAN-ADVISOR-RELIABILITY-20261112.json`.
Scope: the problems seen in the first real use of the advisor (the IT48 pilot, four saved assessments). Nothing was rebuilt; no
invocation was made for this work (the two Stage A and two Stage B of the pilot were already spent). Evidence is the pilot's saved
`meta.json` files, the local raw streams and session transcripts (read here, never published), and the repository at the commits named below.

## 1. Built, invoked, consumed, useful

| | Fact | Where it comes from |
|---|---|---|
| Built | Phase 1 build 4633abf7 (agent, procedure, tool, tests); this follow-up adds small corrections to the tool and procedure | `advisor_build_20261112/README.md` |
| Invoked | 2 Stage A and 2 Stage B in the IT48 campaign, all through the tool, all concluded OK; the allowance is spent | `advisor_campaign_it48_20261112/invocations.jsonl` (branch `task/it48`, not yet on main when this note was written) |
| Consumed | Decision 1 adapted the Orchestrator's sealed plan to the advice (a second reading of eight SCI43 rows instead of continuing INV-09); decision 2 accepted the sealed plan with the advisor's refinements; the advisor's own condition-record candidate was withdrawn by Stage A #2 after a check of the records | the IT48 task record, `PILOT_DECISION_1` and `PILOT_DECISION_2` |
| Useful | **Not judged here.** Whether the advice improved the research is the Orchestrator's evaluation in its campaign report; a plumbing check cannot say it | — |

## 2. Input availability (first priority)

**Observed.** Stage A #2 was told in its brief that SCI48 was "delivered to development/main (merge 3f12c196)". The package
`nrf2_comparator_sci48_20261112` did not exist in the snapshot it ran on (`54b985c7`, branch `task/it48`). The advisor searched, found
nothing, tried the sibling checkout (the tool denied it) and wrote that its statements about SCI48 came from memory. It said so honestly under "Not reached".

**Reproduced (on the real SHAs).** `3f12c196` is not an ancestor of `54b985c7`: the task branch had been cut before the merge. In a detached
checkout of `54b985c7` the new snapshot code reports `development/main` 14 commits ahead and the folder `nrf2_comparator_sci48_20261112` among those absent here, and
`3f12c196:disease-models/.../nrf2_comparator_sci48_20261112` as *not in this snapshot* and *not reachable*. A date or a SHA written in a record did not put the material in the checkout.

**A second, independent defect on the same path.** The snapshot parsed `git status --porcelain` after stripping the whole output, which ate the leading
space of the first line: the Stage A #2 brief lists `edger/tasks/orchestrator/ORCH-ROADMAP-IT48-20261112.json` with an empty digest (the real path starts with `l`). A modified tracked
file listed first lost its first character and its hash. Fixed by not stripping; regression below.

**Fix (smallest that works).**
* The brief states four things apart for each delivery the mission announces (`brief --expect SHA[:folder]`, repeatable): *announced*, *in this snapshot*
  (`git merge-base --is-ancestor`), *reachable by the advisor's tools* (the path exists under its working directory), and, after the run, *read* (files opened, searches made; in `meta.json`).
* Without any `--expect`, the brief still lists the commits main holds that the branch lacks and the folders they add, so the gap shows even when nobody announced it.
* `brief` prints a WARNING at build time, before a launch is spent. A missing delivery does not block work: the brief says the advisor must list it under "Not reached" and not describe it from memory.
* Remedy is the existing mechanism: merge `development/main` into the task branch at a safe boundary and rebuild the brief (free). The advisor's tools are not widened and the sibling checkout stays out of reach.
* `check` prints a NOTE for an announced delivery that was unavailable, with the files read and searches made.

**Regressions** (`framework/scripts/test_strategic_advisor.py`): a modified tracked file keeps its first character and digest; an announced delivery absent from the snapshot is stated
(announced yes, in snapshot no, reachable no, read 0), and after the merge the same delivery is in the snapshot, reachable and counted as read when opened; an unannounced main-ahead still surfaces without blocking.

**Still procedural.** The warning depends on the caller passing `--expect` or reading the main-ahead lines; nothing refuses a launch. "Read" counts opened files and searches, not understanding.

## 3. Capture, exposure and model read-back

Checked on the four saved assessments with a script that compares, for each, the saved file, the runtime result event in the raw stream and the final text of the session transcript.

| Run | Saved chars | = result event | = transcript | digest in meta | Sealed folder opened | Stage A brief carries an intended action |
|---|---|---|---|---|---|---|
| A1 | 16,244 | yes | yes | yes | no | no |
| A2 | 19,281 | yes | yes | yes | no | no |
| B1 | 6,874 | yes | yes | yes | no | (Stage B: yes, by design) |
| B2 | 7,167 | yes | yes | yes | no | (Stage B: yes, by design) |

Stage B briefs embed the saved Stage A of their own campaign by digest (B1 embeds A1; B2 embeds A2). Exposure is declared by the advisor in its own section: A1 names the partial exposure
to the task record's campaign shape; A2 states that its exposure is larger (it read the Orchestrator's own shortlist and the first campaign's assessments) and says it cannot claim independence from them.
B2's agreement with the sealed plan after seeing it is agreement after exposure, not independent confirmation; the independence label belongs to Stage A only and only as far as its exposure section allows.
The advisor's inherited memory and its earlier-assessment reading are declared exposure, not removed to earn a "blind" label.

**Model: four things kept apart** (request, initial, per turn, final).

| Run | Asked | `init_model` | Per turn (transcript census) | Final turn | Runtime fallback recorded |
|---|---|---|---|---|---|
| A1 | opus / high | claude-opus-5-5 | opus-5-5 ×7, opus-5 ×18 | claude-opus-5 | yes, 1 |
| A2 | opus / high | claude-opus-5-5 | opus-5-5 ×18, opus-5 ×2 | claude-opus-5 | yes, 1 |
| B1 | sonnet / medium | claude-sonnet-5-5 | sonnet-5-5 ×3 | claude-sonnet-5-5 | none |
| B2 | sonnet / medium | claude-sonnet-5-5 | sonnet-5-5 ×1 | claude-sonnet-5-5 | none |

**Cause, from the runtime's own record (not inferred).** Each of the two Stage A transcripts holds a `model_refusal_fallback` row: trigger `refusal`, category `bio`, original `claude-opus-5-5`,
fallback `claude-opus-5`, scope session, "retry"; the runtime also printed that the safeguards stopped a response and that the other model answered instead. The stopped response, and what in it was flagged, is withheld and is not
kept anywhere in the repository; nothing here says what triggered it. So: in A1 the answer and 18 of 25 turns came from the fallback model; in A2, the last two turns, including the final answer. Neither assessment is a single-model product and neither may be
described as produced by the model first asked. The stream also contains the retracted first response (one more opus-5-5 message than the transcript census counts).

**What changed.** `meta.json` now carries `final_turn_model` and `refusal_fallbacks` (models, trigger, category; never the withheld text). `check` prints a NOTE naming the fallback and the final-turn model when the runtime recorded the reason, and keeps
a PROBLEM for a model change with no recorded reason. The procedure says to state who wrote an assessment from `final_turn_model`, never from the alias. Regressions: a recorded fallback is disclosed and carries no withheld text; a silent switch stays a problem.

**Not known.** Whether the fallback can be avoided; whether it will recur on the same inputs; what the flagged response contained. These are the runtime's, not controllable from here, and the request stays visibly different from what ran.

## 4. Cost diagnosis (recomputed from the current metadata)

Totals over the four saved runs, summed from each `meta.json` census: output **55,779** tokens; cache written **463,657**; cache read **3,224,722**; they equal the figures in the assignment.
Reported by the runtime as separate lines and kept apart: the main model per run (opus-5 and opus-5-5 for Stage A, sonnet-5-5 for Stage B), and a small secondary haiku service in every run
(input 39,277 / 3,804 / 10,694 / 11,483 tokens, output under 2,000 in each); the advisor's cost is not mixed with the scientific work that followed it, with mechanical operations (this note, the tests) or with those secondary calls, and none of it is converted into a share of a plan or an invoice.

| Run | Turns | First-turn context | Peak context | Cache read | First-turn share of cache read |
|---|---|---|---|---|---|
| A1 | 25 | 16,904 | 201,140 | 2,315,013 | 18% |
| A2 | 20 | 16,842 | 79,056 | 857,096 | 39% |
| B1 | 3 | 23,657 | 28,071 | 47,903 | — |
| B2 | 1 | 24,521 | 24,521 | 4,710 | — |

**What loaded the context (tool results, by file).** A1 read 418,998 characters in 40 calls. Largest: the investigations table of the ranking module, four reads for 114,696 characters (27%; its rows are wide, about 6,000 characters each,
and one read hit the tool's 25,000-token limit, so rows were taken in passes; these passes do not overlap, so this is volume, not duplication); the dismissal ledger 50,464 (the first 220 lines then a heading search; 342 lines not reached); the drug-repurposing roadmap 44,383; the dashboard
notes 35,417; the project mission 24,395. A2 read 136,120 characters: the SCI43 verdicts file 28,354, the two earlier assessments 16,526 and 7,093, and **its own brief, 6,580 characters, which was already its prompt** — the only plain duplicate found.
A1's wide table and long ledgers are originals the question needed; none was replaced by a summary, and none is to be.

**Two observations that need no new control.**
1. After the model change, the *second* turn on the fallback model rebuilt almost the whole context in the cache in both Stage A runs: A1 wrote 68,647 tokens with 0 read; A2 wrote 74,249 with 4,710 read. Together 142,896 of the 415,779 cache-write tokens of Stage A (34%). Correlation in two of two runs; the cause is not established here and the runs without a fallback show no such turn.
2. The fixed first-turn context (instructions, memory index, tools) is 17k tokens and is re-read on every turn: 18% of A1's cache read and 39% of A2's. Not changed: lowering it would change what the advisor inherits, which needs a real call to judge, and none was made.

**One change, from observed causes.** The entry-point table now marks, in the brief, any group whose largest file is over 20,000 bytes, with its path and size; and the brief's contract tells the advisor that its own prompt is the brief (do not open the saved copy), that a marked file is paid again on every later turn,
that it should search for the heading or id and read that range, and that it opens a whole file when the question needs all of it. Originals stay fully reachable. **The saving is expected, not measured**: no extra invocation was made to prove it, and the model may read whole files anyway.

## 5. Browser preflight in the real runtime

Selection was already corrected by the integrated work (4ff3ced5: installed launchers first, the Snap-internal executable last) together with the existing skip of a candidate whose `--version` fails and the older-revision fallback; reused unchanged.

**Facts in this shell, 2026-11-12 22:00 UTC** (host GLIBC 2.39; Snap channel latest/stable at revision 3593): `/usr/bin/chromium-browser`, `chromium`, `chromium-browser` exist and fail `--version` (the Snap shim: "cannot track application process" in this desktop cgroup);
`/snap/chromium/current` and revision 3593 exist and fail (`libm.so.6: version GLIBC_2.43 not found`); revision 3583 is still installed, reports Chromium 157.0.8103.38, starts headless with a DevTools endpoint in one to three seconds (0.6 and 2.9 s in two probes), and is what the selector chooses. `CHROME_BIN=/usr/bin/chromium-browser`
(requested by a peer) is honoured and fails explicitly at `--version`. The earlier notes that said GLIBC 2.42 are corrected here: this shell reports 2.43. Nothing assumes revision 3583 stays installed.

**Residual limit that was reproducible.** "Present" and "`--version` works" were all that the selector proved, the headless start was first exercised inside a 27-minute suite, and a skip (no browser at all) reads as success. No short command stated which fact failed.

**Change.** `framework/scripts/repurposing_view.py browser` (about 2 s): prints `CHROME_BIN`, whether an executable is present (and the other candidates with their `--version` outcome), `--version`, headless start with a DevTools endpoint, and that dashboard tests were not run. It stops at the first failure and exits 1; a missing browser says tests would skip and measure nothing.
It uses the existing `find_chromium` and `Cdp`; the protections (no sandbox-bypass flag) are untouched; it installs and starts nothing. Regressions: the five states stay apart (absent, `--version` fails, `--version` passes but start fails, success, and that a success proves the browser and not a view). CI keeps its own startup step.

## 6. Generated outputs and release efficiency

**Ranking.** `ranking.json` embeds the receipt ledger's line count (`receipt_ledger_lines`); every recording from any session stales it, by design. The check exists (`ranking_it8.py check`, about 15 s) and the suite runs it, but nothing in the path that records receipts or in the freeze steps named it,
so it was found in a battery (two cycles on 2026-11-12). The landing-time mechanism (`candidate_tree_freshness.py`, called by `task_close.py` and `legend_commit.sh`) does not declare the ranking. **Considered and not done:** declaring it there. It would run a 15-second check on commits touching a wide input set, couple the surface to
BATCH_COMMIT Phase 4.7 through the shared discovery tests, and put a shared landing tool, used by every peer, at risk for a defect seen twice. Revival trigger: a third stale-ranking cycle after this change.
**Done:** the freeze checklist in `framework/scripts/README.md` now names it once, after the *last* recording or data edit and not after each append; and `record_staged_receipts.py`, which is where receipts are recorded, prints the check command when the module is present.

**Translation inventory.** `repurposing_view.py i18n --what check` verified the translations but not that the committed inventory (`view/i18n/ui_source.json`, `content_source.json`) equals a fresh collection; only `test_repurposing_view_i18n.py` asserted that, hours later. The same
assertion now runs in that command (the collection is already done there, so no added cost) and prints the fix. Regressions: a passage missing from the committed inventory fails with the command to run, and a current inventory adds nothing.

**Code change versus report update.** The new checks are tied to their inputs: the ranking check to a receipt recording or a data edit, the inventory to an edited passage, the browser probe to the start of a browser-dependent suite. A report-only edit needs none of them.

## 7. What stays procedural

* Ceilings, the `--expect` warning and the fallback NOTE are read by people; nothing refuses a launch.
* A launcher that works in one shell can fail in the desktop service's: the probe must be run where the suite runs, and an installed Snap revision can change at any time.
* Whether the advisor's advice helps is not tested here; one-time savings and the fallback's cost are observations or expectations, not trends.
* No claim of three-day autonomy or better research strategy follows from technical checks.

## 8. Turning it off

* The corrections to the advisor tool: revert `framework/scripts/strategic_advisor.py`, its test and the paragraphs added to `.claude/skills/legend-strategic-advisor/SKILL.md`; `--expect` is optional, so not passing it is the old behaviour.
* The browser probe: delete `browser_preflight` and the `browser` choice in `repurposing_view.py` and its two tests; nothing calls it.
* The inventory check: delete the four-line block at the top of `i18n_check` and its test class.
* The checklist text and the one printed line: delete the added sentences in `framework/scripts/README.md` and in `record_staged_receipts.py`.
* This folder: delete it; nothing reads it.

## 9. From the technical problem to what can now be formulated

Chain per improvement: available knowledge → obstacle observed → minimal correction → consumption actually seen → hypothesis, comparison or experiment now formulable. The level reached is stated for each; none is a pharmacological benefit, and counts of tools, lines or links are not offered as evidence of better generation.

| Improvement | Knowledge | Obstacle observed | Consumption seen | Now formulable | Level reached |
|---|---|---|---|---|---|
| Delivery states, main-ahead lines | the SCI48 comparator package, delivered on main | absent from the advisor's snapshot; Stage A #2 argued a branch-switch dependency ("would SCI48 cover the K-branch shares?") from a short memory paraphrase of it, and said so | none yet: no advisor run was made after the correction | the same dependency can be answered from the package's records, and a missing package is stated instead of replaced by memory | technical; the next real Stage A is the only test, and it is the Orchestrator's to run |
| Model and fallback read-back | two Stage A assessments | a runtime safeguard stopped the first-choice model's response (category bio) and another model answered; what was withheld is not kept | the Orchestrator already carries the change in its decision record and will cite the cause | a reader can weigh an assessment knowing which model wrote it; a proposal lost in the withheld response cannot be recovered or even sized | disclosure only |
| Large-file marker, prompt note | wide investigation rows, long ledgers | volume, not meaning, was the problem; originals were needed whole | not observed | none new; the risk is the opposite one, that a range read drops a relation or an alternative the rest of the file held, so the contract keeps whole reads allowed | expected cost only; judge it by the advisor's "Inspected" and "Not reached" lists, never by a smaller token count |
| Browser probe, inventory check, ranking check | the dashboard and its translations | a stale order, a missing passage or an unmeasured view would show the readers a different map than the records | not applicable | none: they protect what is shown, they do not add a hypothesis | technical |

**What the readers, memory and DREAM did with meaning, in the four saved assessments.** Stage A #1 opened the dismissal ledger and recorded a rejection together with its premise and its revival trigger (so a negative is a claim with a condition, not a closed door), and opened the IT47 DREAM note
(opened; the assessment shows no use of it beyond listing it, which is not proof it was not used). Stage A #2 used memory notes as sources nine times, each time labelled as memory rather than as the record it described, and corrected Stage A #1 by reading the record: the single condition record was already applied in a prediction matrix.
Memory carried lessons here (a negative finding can be false; no contact address to a service), not facts about the disease.

**Wrong proposals and useful ones that access or representation may have lost.**
* Wrong, and caught: Stage A #1 called the condition record unapplied (Stage A #2 read the matrix and withdrew it); Stage A #1 said a juvenile resting-K share had never been searched (the Orchestrator found a package that had already searched it, and that the question had narrowed). Both were caught by reading originals, not by the advisor's own limits.
* Possibly lost, not measurable: Stage A #1 did not reach 342 lines of the dismissal ledger, the discovery ledger, the radar entry point or over a hundred session evaluations, and it made no claim about public tools or datasets for that reason; Stage A #2 did not reach the SCI48 package. What a fuller reading would have proposed is unknown, and no extra run was made to find out.
* A representation limit seen by a peer, not mine and not patched here: the comparison engine derives the role "probe" for two compounds the SCI48 package states as comparators, because its tier rule reads depth and class, not meaning; the label is disclosed beside the display and the engine has no comparator role. It is the same shape as the problems above: the knowledge existed, a tool flattened it.

## 10. Verification

* Release battery on commit 5deeb1ad (clone, own evidence directory): REGRESSION VERDICT PASS WITH SKIPS, 247 targets, 12 skipped, none of the skips concerning this work. The view suite ran in full (1,433 s) with no browser skip: the selector chose the older installed Snap revision on its own in the battery's shell, which is evidence for that shell on that day, not a promise about the next one.
* Targeted: 24 advisor tests (7 new); 8 `CdpStartup` tests (2 new); the inventory regression (2 new); the browser probe run for real in two configurations (default: passes at revision 3583; `CHROME_BIN` set to the Snap shim: fails at `--version` with the shim's own message).
* Not run: a new advisor invocation (the allowance was spent and none was needed); a battery on the final merge commit that includes later landings of other sessions, only the landing gate and CI.
