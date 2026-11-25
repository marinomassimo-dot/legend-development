# ADV-237: why main was red, and what a diff-selected local run would have caught (HE, 2026-11-25)

Harness measurement. Sources: the public Actions API for the workflow `public-release-gate.yml` on `main` (run list and check-run annotations, no login) and a replay of the suites in a scratch clone of this repository. Times are UTC.

## 1. The size of the problem

- Completed gate runs from #1910 (2026-11-22 04:23) to #2297 (2026-11-24 23:43): **227 failed of 383 (59%)**, in **16 red episodes** (an episode runs from a first red run to the next green one).
- Main was red for about **38.8 of those 67.3 hours (58%)**, measured between the creation times of those two runs. The first episode (#1910, 63 failed runs, 18.3 h) may have started earlier, and the last one was still open at the read.
- A gate run takes more than an hour (17 were open at once at 01:00 on 2026-11-25), so an author learns of a red long after landing, with other landings stacked on top.
- The publisher (`safe_push.py`) runs the publication gate and the committed-view checks. It runs none of the regression suites.

## 2. Replay

For each episode: the paths changed between the last green run and the first red run selected suites by the rules of `framework/scripts/landing_suites.py`; each selected suite ran at the red commit, and each failing one ran again at the green commit as the control. The two later causes of the open episode were replayed as their own commits (`57c2f2453`, `fd5442f77`). The two quick suites added to the rules after the replay (release surface, reader journey) played no part in any verdict below.

| episode (first red run) | failed runs | hours | failing suite in CI | what the change touched | selector |
|---|---|---|---|---|---|
| #1910 | 63 | 18.3 | not read (HTTP 403 rate limit) | not read | not replayed |
| #1978 | 2 | 0.3 | not read (same) | not read | not replayed |
| #1981 | 6 | 0.7 | batch queue; view | registries, research | **caught** (the queue part) |
| #1990 | 3 | 0.4 | view (stale committed views) | registries, research | not selected |
| #1994 | 1 | 0.1 | coverage report, reading state | receipts ledger | **caught** |
| #2023 | 23 | 2.6 | a research folder's `test_wwox.py` | new research files | **caught** |
| #2067 | 8 | 0.9 | structured data integrity | new `.tsv` | **caught** |
| #2084 | 21 | 2.5 | view | registries, research | not selected |
| #2109 | 2 | 0.3 | coverage report, reading state | receipts ledger | **caught** |
| #2129 | 29 | 3.3 | view | registries, research | not selected |
| #2165 | 4 | 0.6 | view | registries, research | not selected |
| #2187 | 36 | 5.1 | view | registries, research | not selected |
| #2237 | 16 | 2.6 | documented commands | new research `.py`, `.md` | **caught** |
| #2257 | 1 | 0.1 | none: dependency install failed before any test | one new `.md` | not catchable |
| #2277 | 2 | 0.2 | documented commands | new research `.md` | **caught** |
| #2285 | 10 or more | 1.0 or more | documented commands | new research `.md` | **caught** |
| later in #2285: `57c2f2453` | | | Advisor isolation test | new `framework/scripts/debt_report.py` (HE) | **caught** |
| later in #2285: `fd5442f77` | | | pathograph drift, batch queue drift | registries | **caught** |

Every suite counted as caught was red at the red commit and green at the control, except the batch queue on `fd5442f77`, whose registry-coverage assertion was already red there; its queue-currency assertion and the pathograph were new.

## 3. Totals

- **Causes replayed: 16** (14 episodes plus 2 later causes). Flagged: **10**. Not flagged: 5 stale-view episodes and 1 dependency install.
- **The window ADV named** (31 failed runs read on 2026-11-24): flagged episodes hold **25 of 31** failed runs (16 + 2 + 7); the other 6 are the tail of a view episode (5) and the install failure (1).
- **By red hours, the read episodes give the opposite weight**: flagged about 8.3 h, stale views about 11.9 h. The view cause is already covered: `safe_push.py` began refusing stale views at 01:41 and stale packages at 06:47 on 2026-11-24, and no view episode started after #2187 (04:57 that day).
- **Since those view checks: 5 of 5 code causes flagged** (three documented-commands episodes, the Advisor test, the registry drift).

ADV's condition (build only on a clear majority) was met on the window it named and on the causes still uncovered; it would **not** be met on red hours alone if the view episodes counted as open.

## 4. What was built

`framework/scripts/landing_suites.py`: print-only and advisory. It prints the suites that the committed diff since the merge base with `development/main` selects, and one command that runs them. No hook, no gate or workflow edit, no change to `safe_push.py`. Routed once in `framework/scripts/README.md`; tests in `framework/scripts/test_landing_suites.py`.

Cost of running what it prints, from the replay: 42 to 50 s for a change in research files or scripts, about 130 to 150 s when registries or the receipts ledger change.

## 5. Limits

- The replay is an upper bound on the benefit: it assumes the author runs what is printed, and the episode diffs span every landing between the last green and the first red run, so a selection from one author's own diff can be narrower.
- Nothing enforces it. The README already carried this advice as prose ("run the quick suites") and mains still went red. Whether a printed command is followed more than a paragraph is not known; the next red episodes after 2026-11-25 are the measure.
- A defect that appears only in the merge of two sound branches is not seen.
- A name-based lookup of the tests that read a changed file was judged on 2026-11-18 and not built; these rules select by path class instead and do not replace that judgement.
- Not selected on purpose: the view suite (about 20 minutes) and the other long suites.

## 6. Re-open

If, after a week of use, a red episode starts from a path no rule matches, add the rule with its run number. If the printed command is not being run (episodes of the flagged classes keep starting), wiring it into the publisher before the lock is the next option; it adds a refusal and is a decision for ADV, with the already-red-on-main case to solve first.
