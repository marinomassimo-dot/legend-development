# CI-red read after the landing-suite refusal (HE, 2026-11-28, history only, no suite run)

Method: section 6 of `HE_CI_MINUTES_GATECACHE_20261125.md`; prediction fixed there before the read: no red caused by a suite the
selection named for that landing, from a publisher whose worktree held the new script; rejected by one such red. Source: the
public GitHub Actions API (no token), runs created from 2026-11-26T11:21Z to 2026-11-28 about 04:40Z (282 runs; the list is a
scratch file, 80 KB).

| Workflow | success | failure | in progress |
|---|---:|---:|---:|
| Public release gate | 152 | **0** | 3 |
| Publish the shareable view (Pages) | 108 | 18 | 1 |

- **Prediction held: zero gate failures in 152 concluded runs** (baseline before the refusal: 44 of 85 concluded runs failed,
  52 percent, over 7 h 33 min). No red from a named or an unnamed suite.
- The 18 failures are all in the Pages publication workflow, on `push main`, from 2026-11-26T15:44Z to 2026-11-28T03:29Z, 16 of
  them on 2026-11-27 between 14:09Z and 23:27Z. Failing steps (job `deploy`): 9 at "Build the audited Pages publication from this
  commit" and 9 at the `actions/deploy-pages` step. The gate was green on every one of those commits, so no landing suite caused them;
  whether a landing changed what the Pages build audits is not readable without the job logs (not fetched: authenticated).
  The Pages workflow is operator-reserved: reported, not touched.
- Not read: the three gate runs still in progress.
