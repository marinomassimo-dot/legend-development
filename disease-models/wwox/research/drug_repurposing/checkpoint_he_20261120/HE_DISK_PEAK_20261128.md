# Disk use of a push after the shared suite clone: two measured pushes (HE, 2026-11-28)

Asked by ADV. Measurement and proposal. **Decided by ADV the same day:** both proposed values, landed with this note; the
1.0 GB stop line and the operator's 15 GB report-first rule are unchanged; the release battery keeps 1.4.

## Method

A passive sampler read the size of every push temporary folder in `/tmp` every 3 s (unique inodes, hard-linked `files/`
skipped) with the free space of `/`. It ran from about 09:41Z to 09:47Z. It did not start, stop or touch a push.

## Measured

| Push (publisher) | Candidate tree | Suite clone | Both at once |
|---|---:|---:|---|
| `f51067bf0` (ADV; sampled from 09:41Z, it had started at 09:35Z) | 462 MiB | 462 MiB, `.git` 3 MiB | no |
| `d0bc8e409` (IT Orchestrator; whole push) | 462 MiB | 462 MiB, `.git` 3 MiB | no |

Free space fell by about 0.49 GB during a push and came back at its end. 462 MiB is 0.48 GB (`safe_push` counts
GB of 1e9 bytes). Every worktree with a commit in the previous 12 hours, and the root checkout, carried the `--shared` code.

## Not measured

- A push with a red suite builds a base clone beside the suite clone (`_red_at_base`): about 0.97 GB, computed.
- The release battery (`run_release_regressions.py`).
- The first six minutes of the first push, which it spent before the sampler started.
- A push published by SCI or by HE (the two measured are ADV's and the Orchestrator's; the code is the same).

## Proposal (accepted by ADV)

| Constant in `framework/scripts/safe_push.py` | Before | Now |
|---|---:|---:|
| `MIN_FREE_GB` | 2 | 1.5 |
| `PEAK_GB["safe_push.py"]` | 1.4 | 1.0 |

- 1.5 GB is the laboratory's 1.0 GB stop line plus one green push (0.5 GB). It also holds the computed red case with
  about 0.5 GB to spare. Twice the green peak (1.0 GB) would let a push start that ends under the stop line.
- 1.0 GB is the red case, reserved for each other live push.
- The laboratory's standing 2.0 GB disk rule states the same number as `MIN_FREE_GB`; both would move together.

## What it would change

The job logs of 2026-11-28, 08:18Z to 09:41Z, hold 10 `waiting for disk space` lines, 20 to 71 s each, at 2.3 to 2.9 GB
free. With the proposed constants 9 of the 10 would not have waited (computed from the free space and the live runs each
line names). A push would also be possible between 1.5 and 2.0 GB free, where today it is refused.
