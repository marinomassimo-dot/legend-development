# Cold-start repeat after the "First moves" bullet (2026-11-19)

Non-normative. Author: Harness Engineering (`plan`), at the ADV host's request; companion of [`adv_cold_start_20261119.md`](adv_cold_start_20261119.md). Same two prompts, same method and isolation (read-only `claude -p`, Sonnet, medium effort, no memory, one run each), on a clean checkout of `development/main` at `3ff07ad50`, which holds the charter bullet "First moves of any recall". Evidence: [`adv_cold_start_20261119_evidence/repeat/`](adv_cold_start_20261119_evidence/repeat/). No verdict is drawn beyond what follows.

| | first run (before the bullet) | repeat (after) |
|---|---|---|
| Prompt N (facts only) | assign now | assign now; names the guidance and the tick as pre-send steps |
| Prompt W (with the old "motivated wait") | assign now, rejects the wait | **assigns nothing yet**: says the given facts contradict the repository and its first move is to measure |
| Operator's standing guidance | not read | read in both, at its source (the OPERATOR_GUIDANCE block of the roadmap), reported as read "in place of" the command |
| `guidance` and tick | not named as first moves | named by both as the first live steps; neither could run them (no shell) |
| Next assignment number | proposed numbers that already existed | both took it from the log (ADV-088 stated by W; N read the log tail) |
| §21c-§21e | not read | still not read by either |
| Calls / reported cost | 11 and 13 / 0.13 and 0.28 USD | 20 and 12 / 0.64 and 0.47 USD (notional) |

**What changed in what the cold session reads or runs:** the bullet was found and followed in the sense that matters here: both runs read the operator guidance and put `guidance` and the tick first in the live sequence, and the numbering gap did not recur. **A confound, stated plainly:** the tree is now much later than the scenario clock (assignments up to ADV-087 sent at 16:16Z, a later MEETING), so run W treated the scenario as stale and deferred the decision to a measurement; that is a correct reading of an inconsistent scenario, not necessarily a change caused by the bullet, and it differs from the first run's outcome for that reason as well. The higher cost follows from the larger tree and the extra reads, not from a measured effect of the bullet. Limits unchanged: one model, one run per prompt, no commands, cold not warm.
