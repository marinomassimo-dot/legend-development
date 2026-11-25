# Question for the operator: run the CI regression suites 4 at a time? (HE, 2026-11-25)

**Yes or no: may this one line be added to `.github/workflows/public-release-gate.yml`, under `jobs.release-gate.env`?**

```yaml
      LEGEND_REGRESSION_JOBS: "4"
```

Nothing is applied. Workflow edits are reserved to the operator.

**What changes.** The step "Regression tests" runs the same suites, 4 at a time instead of one after another. Without the line the runner stays serial (the default).

**Measured on the laboratory host** (4 cores, shared with other sessions; no suite had to run alone):

| run | wall time | suites | result |
|---|---|---|---|
| serial | 3,965 s | 276 | pass, 45 skips |
| 4 at a time | 1,437 s | 276 | same suites, exit codes, skips and test counts as serial |
| 4 at a time, repeat | 1,536 s | 276 | **one red**: a race inside `test_verify_run.py`, since fixed |
| 4 at a time, after the fix, load up to 13 | 1,789 s | 277 | pass, 45 skips |

**The hosted runner.** The workflow runs on `ubuntu-latest`. GitHub's runner reference (read 2026-11-25) gives 4 CPUs and 16 GB for that label on public repositories; this is the documented size, not a reading from a run (the run log needs a login). In run #2485 the suites took 2,021 s one after another, the longest (`test_repurposing_view.py`) 637 s; the step took 37 to 39 minutes in four of the last six green runs and 54 to 60 in the other two.

**What is not known: the gain in CI.** Estimate only: the step cannot go below its longest suite (637 s), and on our host that suite ran 1.2 to 1.5 times slower under parallel load, so about 13 to 16 minutes, roughly 20 minutes saved per run. A suite that collides only on the hosted runner would show as a red that a serial run does not reproduce.

**Rollback.** Delete the line; the next run is serial.

**What one run tells.** The step time and the `suite time` notice of the first run (readable with `python3 framework/scripts/ci_runs.py times <sha>`) confirm or refute the estimate. HE reads the first runs; a collision is fixed by adding that suite to the runner's `RUN_ALONE` list, or by deleting the line.
