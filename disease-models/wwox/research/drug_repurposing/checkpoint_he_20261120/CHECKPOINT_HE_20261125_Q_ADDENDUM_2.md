# Second addendum to checkpoint HE-Q (2026-11-25, HE window 9229d112)

Read after `CHECKPOINT_HE_20261125_Q.md` and its first addendum.

## 1 Gate timing, for Q section 2 item 3
One shared host, `public_release_gate.py --cache` with `LEGEND_GATE_CACHE_FILE` in the job folder: **cold 265 s (15,396 misses), warm 32 s (15,396 hits)**, both VERDICT PASS. Applied to both gate calls of `test_a_stray_git_file_cannot_suppress_a_real_block` it would save about 230 s per local run; the link scan that the test asserts runs in full either way. The CI effect is not measured. Sent to ADV as the one change proposed; not implemented.

## 2 View suite per-test times
Not read at writing. Rerun `python3 -B framework/scripts/test_repurposing_view.py --durations 25` through `nohup` if wanted (about 20 minutes).
