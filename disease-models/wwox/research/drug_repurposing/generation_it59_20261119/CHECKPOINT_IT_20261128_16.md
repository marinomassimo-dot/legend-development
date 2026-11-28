# Checkpoint IT41 (window 98a18a59), 2026-11-28, written at about 246k context (census, effort high)

Hypothesis level; nothing here is medical advice. Mandate ORCH-ROADMAP-IT59-20261119. Read this file and the two ADV-339 results; `_15` only for IT40's close. Codex is never contacted. Worktree `it_41_20261128`, branch `task/it41b`.

## Done
* Bound (marker verified), main merged, effort high; IT40 (8424b293) released on request.
* **CLAIM 003 repaired and landed** (`BATCH_20261128_011`, MINOR, `f0d03ecce`, gate PASS verified by ls-remote): headline (no quantified myelin endpoint for the O-KO) holds; EM and CC1/PDGFRa counts were given to the S-KO alone, RNA readouts to null + N-KO alone: wrong. Second reader: first composition 1 of 3 sentences incomplete; final text 0 of 27 atoms, **same reader (delta), not independent**. Receipt `FTR-20261128-33914858-42` (`queried_not_full_read`). Landing refusal taught: the view trio needs `package` too (run, run --source shareable, package).
* **ADV-339 accepted from ADV** (exclusivity sentences in the claim registry). PREREG frozen before any source (`4c8533c10`); enumeration net `enumerate_adv339.py` (233 candidates, 42 claims, lexical); delegate counted about 49; **11 checked, two readers each**. Result: **6 of 11 not holding on the second readers' strict reading, 3 of 11 firm** (S1 age atom, CLAIM 011 title, CLAIM 011 "no untreated arm / bytes absent"); undecided-to-E2; stopping observation not met. Files: `advisor_pilot_20261113/brainstorm_20261116/adv339_exclusivity_it_20261128/` (`RESULT_ADV339_part1_*`, `_part2_*`). Arm assignments held; **scope words** failed.
* CI: no red through #2959 (success); #2960 to #2968 still in progress at 18:12Z (queue ~1 h per run); a monitor script `/home/desktop/.claude/jobs/98a18a59/tmp/ciwatch.sh` was armed; re-arm or read `ci_runs.py queue` and the API. Codex commits (`codex/sci-trimetazidine-20261128`) are on main today despite PAUSED; ADV told the operator, no contact.

## Open, in order
| # | Item | State |
|---|---|---|
| 1 | CI of runs after 2959: read any red from check-run annotations | open |
| 2 | **ADV decides the CLAIM 011 title** (survival is graded by Fig 3B, expression mostly ns) and which of RP-016/017/019 cite it; then one BATCH_COMMIT (CC, ops, `test_batch_queue`, view trio incl. package) for the part 1 and part 2 wording repairs that ADV approves; the CLAIM text is partly Italian | waiting for ADV |
| 3 | ADV-339 continuation: about 25 counted sentences unchecked (CLAIM 013, 016, 017, 019, 025, 030-047) plus the enumerator's borderline list; ADV chooses whether to continue or close the pattern | ADV |
| 4 | ADV-286 dates: C1 re-check 2026-12-05, C2 not before 2026-12-06, UNRESOLVED 2026-12-12 | dated |
| 5 | Two mp4 supplements of 33914858 still unviewed (decoder; refused fetch, not retried) | operator list |
| 6 | Predecessor worktrees `it_39`, `it_40`: ADV removes via branch_hygiene from 18:38Z; never remove yourself | ADV |

## Traps met
* A reader packet built from the text file alone turns held figures into "not held": search `files/figures`, `files/supplement` and `figure_renders` by PMID, and name the PDF with embedded figures (Fig 5 of 34747138 is only in `PMC8649866.1.pdf`).
* A ledger move on main (SCI_CODEX receipts) after my receipt: restart from main (`checkout -b new development/main`), copy own files, record again, regenerate coverage, reading_state, pathograph, ranking and the view trio.
* `git rev-parse --short A B` fails ("Needed a single revision"); one SHA per call.
* The sentence splitter cuts blockquotes at line ends: join before dispatch (#68/#69).
* Context: 246k by turn 108; whole claim records and four delegate hand-backs of 4 to 8k each.
