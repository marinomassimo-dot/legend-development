# ADV-274: red streaks on main and what the landing selection would have named (HE, 2026-11-25)

Plan frozen first: `HE_RED_STREAKS_ADV274_PREREG_20261125.md` (commit c3fae0d3b). Sources: the public run list (one read, cached) and check-run annotations of 10 red runs; local bisection in a scratch clone for the introducing landing of each failing suite. Times are UTC. No workflow file touched.

## 1. The set
Gate runs #2340 to #2432 on `main`: 41 success, 40 failure, **12 excluded as not concluded at the read**. Excluded as red for a reason outside the commit: 0 among the runs read (each failed in `Regression tests` with a failing suite). The other red runs sit inside the three streaks and were not read one by one.

| streak | first red | red runs | push of first red to push of first green |
|---|---|---|---|
| 1 | #2322 (starts before the set) | 34 | 2.24 h |
| 2 | #2370 | 7 | 0.43 h |
| 3 | #2404 | 17 at the read, still open | over 3 h at 10:18 (censored) |

Median over the six closed streaks from #2246: **0.99 h**. Median run duration in the set: **96 min**, so a verdict arrives after most streaks have already gathered further landings.

## 2. Causes
A cause is one failing suite at the landing that turned it red (red there, green at the previous run, both run locally).

| cause | landing | failing suite | rules in force | rules at 071ad65e4 | rules now |
|---|---|---|---|---|---|
| C1 | #2322 `25c2114a` | closed-world guard | no selector yet | named | named |
| C2 | #2353 `f0daa021` | `test_ranking_it8.py` | escaped | named | named |
| C3 | #2353 `f0daa021` | `test_candidate_tree_freshness.py` | escaped | named | named |
| C4 | #2370 `47a57e75` | `test_batch_queue.py` | escaped | **escaped** | named |
| C5 | #2372 `e8423539` | `test_documented_commands.py` | **named, landed anyway** | named | named |
| C6 | #2404 `40a78e0b` | cards copy suite | escaped | named | named |
| C7 | #2404 `40a78e0b` | view `Titles` class | escaped | named | named |
| C8 | #2421 `ab80dc73` | `test_repurposing_join.py` | escaped | **escaped** | named |

- **8 suite causes over 6 landings** (expected 4 to 6: wrong, there were more).
- Named by the rules in force: **1 of 7** (expected at most 2).
- Named at `071ad65e4`: **6 of 8**; after the two rules below: **8 of 8**. Both figures are in-sample: the rules were written from these reds. The next streaks are the test.

## 3. Rules added (each a single observed case with a cheap trigger)
- `test_batch_queue.py` also on any `*_current.md` under `disease-models/`: the queue scans them all; the case was a retracted PMID cited in the discovery ledger.
- `test_repurposing_join.py CuratedLink` (about 10 s) on a change of the mechanism map: the case was a dated addition whose PMID became the first evidence row of its query.

## 4. What the counts do not show
- **C8 was still red** at `670d60bf3` (10:07): the title and card fix did not cover it. Reported to IT and ADV at about 10:15.
- The title-cache fix (IT) also needed the view pages and the shareable package regenerated. No selector rule names those; `safe_push.py` checks the committed views itself before the gate. No red run of this set came from them.
- C5 shows that a printed selection is not a run one: the rule existed and the landing went out.
- A suite that failed and was repaired between two of the runs read would be missed.
- Derived-surface regeneration became the default of `safe_push --serialize` during this set, after C2 to C4; it would now repair that kind before the push.

## 5. Decision left to ADV
The selector stays advisory. `safe_push.py --landing-suites` already runs the selection under the lock and refuses nothing. Making the run the default is the open option of `HE_RED_MAIN_ADV237_20261125.md` section 6; it would have shown C5 and C8 (now that it is named) to the publisher before the push, at the cost of lock time.
