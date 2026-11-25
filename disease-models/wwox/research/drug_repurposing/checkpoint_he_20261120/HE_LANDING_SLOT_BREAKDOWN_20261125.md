# HE: where a landing slot goes (ADV-229, RP-029 parked items a and b), measured 2026-11-25

Question (ADV): `safe_push --serialize` spends about six minutes per landing slot under the lock and a push often waits behind
three others. Where does the time go, which component is the biggest, what is the cold-cache cost, how much is unavoidable?
No change was made: no gate edit, no workflow edit, no `safe_push` edit. This is a measurement.

## Method

* Push logs: 15 readable `safe_push` logs from the job folders of this session (file creation to last write = wall time;
  the tool itself prints `landing lock acquired after Ns` and `queue position k of n`). `safe_push` writes no per-phase
  timestamps, so the phases below were timed one by one on the same commit, same machine, same moment.
* Phases timed in isolation, warm cache: `git fetch` (3 runs), `git ls-remote` (3), `git push --dry-run` (2), the three
  `repurposing_view.py` freshness checks that `safe_push` runs before the gate (2 each), `git archive | tar` of the clean clone,
  and the whole public gate twice.
* Cold: the same gate after `posix_fadvise(DONTNEED)` on 23,690 files of the checkout and the git directory (clean pages only,
  no root needed). Not a reboot cold start: the interpreter and the system libraries stay warm, so this is a floor for the cold cost.
* Inside the gate: one `cProfile` run (inflated by the profiler: 262 s against 161 s plain, so only the shares are used).

## Result: one slot, no queue, warm cache

| Phase (all under the landing lock) | Seconds | Share of a slot |
|---|---:|---:|
| fetch + merge of the remote tip (`git fetch` 1.1-1.6 s; the merge is local and writes only changed files) | about 2 to 3 | 1% |
| the three view checks before the gate: `check` 5.2-5.3, `i18n --what check` 5.6-5.8, `package --check` 19.2-25.8 | 30 to 37 | 16% |
| the public gate | 161 to 166 | about 80% |
| `git push` (dry-run 1.4-1.5 s) + `git ls-remote` verify (1.2 s) | about 3 | 1.5% |
| **Sum** | **about 197 to 209** | |
| opt-in `--regenerate-derived` (documented in the tool, not measured again here) | about 80 | when used |

The sum matches the unqueued logs: 196, 218, 242, 251, 253 and 258 s of wall time (the 258 s one included a merge).
With `--regenerate-derived` a slot is about 280 s warm, which is the "about six minutes" once a cold cache is added.

## Queue: the lock wait is the biggest wait, not the biggest component

Nine of the fifteen logs queued. Lock wait: 40, 156, 194, 218, 220, 276, 314, 368, 462 s (median 220 s). By position:
position 2 of 2 waited 40 to 276 s (about 190 s on average, one slot's remainder); position 3 of 3 waited 156 to 462 s
(about 325 s, two slots' remainders). A wait is the sum of the slots ahead, so it grows with the number of publishers, not with
any one phase. Wall time with a queue was 425 to 675 s against 196 to 258 s without.

## Cold against warm

The gate alone: 160.8 s and 165.5 s warm, 263.7 s after eviction: **+100 s (about 60%)**. The other phases are dominated by
process start and a few reads of the git directory; the three view checks were not re-timed cold. A slot after other work has
evicted the checkout (disk at 90% used, several clones per hour) is therefore about 300 s, not 200 s.

## The biggest single component, and what is in it

The public gate, 80% of a warm slot. Inside it (profiled shares of the 262 s profile): `scan_privacy_and_secrets` 203 s, 78%
(134 s of that is its own Python loop, 52 s regular-expression searches over about 806,000 calls); `scan_readme_consistency` 38 s,
14% (it re-walks the tree: 121,000 `walk_publishable` calls); `scan_links` 14 s, 5%; `fill_names` 8 s; `scan_provenance` 7 s. Building
the clean clone is not the cost: `git archive | tar` of 436 MB takes 2.4 s warm. Path handling (`pathlib.relative_to`,
`is_relative_to`, 175,000 calls each) is about 30 s of the profile, which is a hint where the gate's own time is spent, not a finding.

What this answers: the runner's guarded-tree hashing (checkpoint J, 283 s of a 94-minute CI run) is a different cost in a different place
(the CI runner). It is not part of the local landing slot. The slot is the gate's privacy scan plus the view checks.

## Share that is unavoidable

* Unavoidable by construction: the network operations (fetch, push, ls-remote), about 5 to 6 s, 3% of a slot.
* Necessary checks that cost what they cost today: the gate (80%) and the view checks (16%); both exist because of past red CI runs
  (2026-09-09 push with a BLOCK verdict; 2026-11-24 derived views behind their sources). Their time is not waste, but it is not a floor:
  each is a Python tree walk whose hashing or scanning could be made incremental. That is an owner's choice (gate owner and operator).
* Waiting in the queue is not a cost of any phase; it is the serialisation the lock was introduced to give (five sessions gating at once
  were refused at the push). It can be shortened only by shortening the slot.

## Decision this changes (for ADV and the operator, nothing applied)

1. If a shorter slot is wanted, the largest lever is the gate's privacy scan (78% of the gate): a scan limited to files changed since the
   last PASS on the tip would cost seconds, but it changes what the gate certifies, so it is the gate owner's decision, not HE's.
2. The second lever is `package --check` (19 to 26 s, more than the two other view checks together), a candidate for the same
   incremental treatment.
3. Warm the cache or keep slots short by landing from one worktree: each cold start adds about 100 s to the gate.
4. The runner-side stat-based pre-check of the guard (checkpoint J) answers a different cost and stays a separate proposal.

## Limits

Fifteen logs, one machine, one commit; the profile is a single run; cold = page-cache eviction of this repository only; the
`--regenerate-derived` time is the documented figure; the three view checks were timed warm only; no run was made while another
publisher held the lock, so queue figures come from the logs.

Dated line, 2026-11-25: derived-surface regeneration became the default of `safe_push --serialize` (`--no-regenerate-derived` opts out), after a stale ranking was published in CI run #2353; the CI gate is untouched.
