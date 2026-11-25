# Landing slot after the gate speed-up: the whole lock hold (HE, 2026-11-25). Report only; nothing changed

Asked by ADV. Wait for the lock excluded.

## 1 Method

* `safe_push` logs from the job folders, the last 15 published landings (16:59Z to 18:43Z), 9 with the new
  privacy scan. The log gives the hold, the regeneration step and each landing suite; the rest is untimed.
* The untimed phases, timed twice each in an isolated clone of 9e39bbfcd (load average 3.5 to 4.2 on 4 cores).
* Scripts and raw output: `files/coordination/he_landing_profile2_20261125/` (`slot_stages.py`,
  `time_phases.sh`, `overlap.sh`; `stages_15.tsv`, `phases.log`, `overlap.log`).

## 2 Seconds per stage

| Stage under the lock | Seconds | Source |
|---|---:|---|
| whole hold, median of 15 / of the 9 with the new scan | 336 / 250 | logs |
| public gate | 101 and 124 | timed alone |
| landing suites, median (range 9 to 176; follows what was selected) | 53 | logs |
| three view checks (`check` 6, `i18n --what check` 8 to 14, `package --check` 29) | 43 to 48 | timed alone |
| derived-surface regeneration, median | 24 | logs |
| `git fetch` + push (dry run) + `ls-remote` | about 4 | timed alone |
| gate + views + git together, median of the 9 new-scan landings | 143 | logs (hold minus the timed lines) |

The most selected suites over the last 20 landings: `test_documented_commands.py` (19 of 20, median 29 s),
`test_strategic_advisor.py` (4 of 20, median 74 s), `test_pathograph.py` (5 of 20, median 55 s).

## 3 Largest remaining stage, and one proposed change

The gate, about 110 s of a 250 s slot. **Proposed:** start the three independent checks together (view checks,
gate, landing suites) instead of one after another; refusals and their order of report unchanged.

Measured once on one commit with the nine suites of a code landing: **281 s one after another, 177 s together,
104 s less** (load 5.2 and 5.5 at start). Gate output identical, every part exit 0, tree clean afterwards.
Parts when together: views 52 s (alone 40), gate 162 s (97), suites 177 s (144).

| Risk | What it would cost | Answer before any change |
|---|---|---|
| The gate runs in `staging` mode and reads the live worktree; a suite that writes a transient file there would be seen by it. "Clean afterwards" does not exclude that | a spurious BLOCK, or a finding on a file that is not in the commit | run the suites in a throwaway clone of the merged commit, as the at-base re-run already does; then re-measure (the clone adds a few seconds) |
| 4 cores already loaded: each part gets slower, and a suite timeout counts as red | a false refusal, one lost slot (about 5 min) | keep the serial order as the fallback; record load and suite times for the first ten landings |
| A view check failing no longer saves the gate time | about 2 min on a refused push | none needed |
| One measurement, nine suites, one commit | the saving is smaller for a landing with one or two suites (about the view checks, 40 s) | repeat three times before deciding |

Minutes per risk: about 1.7 min per landing; at the rate of this window (15 landings in 104 min, the lock held
about 70 of them) about 12 minutes of lock time per hour, and the queue behind it shortens by the same.
`safe_push` is the publication path: HE changes nothing without ADV's word.

## 4 Not measured

The cold cache after eviction; the at-base re-run (it runs only on a red; no instance in the 15 landings);
`--no-regenerate-derived`.
