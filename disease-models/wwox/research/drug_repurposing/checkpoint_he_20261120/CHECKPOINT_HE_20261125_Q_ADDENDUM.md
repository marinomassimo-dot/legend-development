# Addendum to checkpoint HE-Q (2026-11-25, HE window 9229d112)

Read after `CHECKPOINT_HE_20261125_Q.md`, which stays as written.

## 1 Refusal replay, complete; do not rerun
New `landing_check`, current selector, real suites, scratch clone, previous gate run's commit against the causing run's commit:

| case | suites run | verdict | seconds |
|---|---|---|---|
| #2352 to #2353 | 12 | REFUSES: candidate-tree freshness and ranking, the two causes | 381 |
| #2403 to #2404 | 10 | REFUSES: cards copy and view `Titles`, the two causes | 119 |
| #2420 to #2421 | 8 | REFUSES: join `CuratedLink`, the cause | 150 |
| clean, #2392 to #2393 | 6 | PASSES | 68 |

The host was shared with other timing runs. Under `--serialize` these seconds are lock time.
