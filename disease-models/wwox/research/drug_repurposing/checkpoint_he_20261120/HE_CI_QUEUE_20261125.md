# Why a gate verdict takes an hour or more (HE, 2026-11-25)

ADV's item (direction round 13:20Z): ten gate runs were in progress at once, the oldest 1 h 07 m. Measure the cause; a workflow change stays the operator's.

Source: the public Actions API, read about 13:25Z without a login. One list of the last 100 runs (96 of the gate, 8.4 h), the jobs of 12 runs, and the per-suite times of #2460 (`ci_runs.py times`). Samples, not every run.

## 1. Measured

| measure | value |
|---|---|
| gate runs in the window | 96 in 8.4 h, all pushes to main; median gap between pushes 4.8 min |
| last 20 concluded runs, duration | median 57.9 min, 46.3 to 73.5 |
| 8 recent concluded runs, wait of the job for a runner | 1 to 2 s |
| their `Regression tests` step | 39.5 to 54.1 min, about 85% of the job |
| their `Public release gate` step | 5.6 to 7.6 min |
| 4 runs created when 23 to 25 runs were open (06:28 to 07:27Z) | job waited 470 to 1,162 s, then ran 77 to 98 min |
| #2460, sum over 276 suites | 2,165 s; `test_repurposing_view.py` 687 s, `test_repository_surface_determinism.py` 358 s |

## 2. Cause

1. **Normally the verdict time is the run itself.** With 9 or 10 runs open nothing queues. The runner executes 276 suites one after another.
2. **In a burst it is also a queue.** With more than about 20 runs open, jobs waited 8 to 19 minutes. That matches the account's concurrent-job limit (documented by GitHub; not read from this account). The same runs were also slower; the reason for that was not measured.
3. The push rate only matters through point 2: at one push per 4.8 min and 58 min per run, about 12 runs are open; at 98 min, about 20.

## 3. Options

| option | where | expected effect | risk | who decides |
|---|---|---|---|---|
| A. Run the suites on 4 workers inside the same job | `scripts/run_release_regressions.py` (default stays serial; parallel when asked for or in CI) | regression step bounded below by the longest suite: about 12 min against 40 for #2460, so a run of about 19 min instead of 47; fewer runs open, so the queue of point 2 should not form. **An estimate from serial times, not measured** | suites that share a file, a port or a directory can turn flaky; the guard that names the suite which wrote a tracked file works by time window and would need a serial rerun to attribute | harness (no workflow file touched), but it changes what CI does: ADV to agree |
| B. Cancel superseded runs on a branch | workflow (`concurrency`, patch in HE checkpoint J section 3) | removes the burst queue; **does not shorten a run** | an intermediate commit never gets a verdict | operator |
| C. Split the job in a matrix | workflow | like A, with less sharing between suites | operator-reserved; each part repeats the setup | operator |
| D. Push less often (batch landings) | habit | fewer runs open | results reach main later | the actors |

## 4. Proposal

A first, as a trial with a rejecting observation: in a scratch clone, run the whole inventory serially and on 4 workers back to back. Reject A if any suite is green serially and red in parallel and cannot be named as needing to run alone, or if the wall time does not fall by at least half. B stays on the operator list whatever A gives.

Not measured: the effect of 4 workers on a hosted runner; the browser suites under contention.

## 5. Trial of option A (ADV: go, opt-in and default off; same day)

`--jobs N` or `LEGEND_REGRESSION_JOBS` in `scripts/run_release_regressions.py`; without it the run is serial as before. Both runs: one commit (a2b46d713 plus the switch), one isolated clone without `files/`, one 4-core host shared with other sessions.

| measure | serial | 4 workers |
|---|---|---|
| window (UTC) | 13:30 to 14:36 | 14:36 to 15:00 |
| wall seconds | 3,965 | 1,437 |
| suites / verdict | 276, PASS WITH SKIPS (45) | 276, PASS WITH SKIPS (45) |
| summed suite seconds | 3,578 | 4,796 (contention) |
| `test_repurposing_view.py` | 1,214 s | 1,434 s |
| `test_repository_surface_determinism.py` | 568 s | 804 s |
| load average | 3.3 at start, 2.9 at end (not sampled between) | 6.0 to 8.2 in the first 20 min, 3.3 to 3.6 after; 2 to 5 other test or gate processes |

Same suite list, same exit code per suite, same skip reasons, same number of tests per suite, no tracked write, clone clean before and after. **No suite had to run alone.** The parallel phase (1,434 s) lasted exactly as long as the view suite, which is now the bound: splitting that suite is the only further lever inside this design, and the floor under it (summed time over 4 workers) is about 1,200 s here.

Overlap with my own landings (gate and suites on the same host): 14:18 to 14:40Z, so the last 18 minutes of the serial run and the first 3 of the parallel one.

**Not measured:** the hosted runner. **Enabling it there is a workflow edit, reserved to the operator**, one line under `jobs.release-gate.env` of `.github/workflows/public-release-gate.yml`:

```yaml
      LEGEND_REGRESSION_JOBS: "4"
```

Cost if it is enabled and a suite later collides: a red run that a serial run does not reproduce; the remedy is one `RUN_ALONE` entry. Revert: delete the line.

## 6. Repeat of the 4-worker run, and the one red (same commit, same day)

15:01:10 to 15:26:46Z, load 4.1 at start and 3.4 at end, 2.7 to 11.6 between (1 to 4 other test or gate processes). **1,536 s wall, 276 suites, 45 skips, verdict FAIL: one suite green serially and red here**, `framework/scripts/test_verify_run.py` (one error of 20 tests). Everything else as in the serial run: same list, other exit codes, skip reasons, test counts; no tracked write.

Cause, named: a race inside that test, not a shared resource. `wait_state` waited for the run directory and read `manifest.json`, which `verify_run.py` writes after making the directory. Shown deterministically (manifest written 0.5 s late: `FileNotFoundError` before, state returned after); the test now waits for the file. So no `RUN_ALONE` entry; **no 4-worker run has been made since the fix**, and one clean run is owed before the workflow line is put to the operator. Two runs are a small sample: a rarer race would not show in them.
