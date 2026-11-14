# HE52: operational check of the continuous mode on a copy of the real campaign (2026-11-14)

Non-canonical. Run by HE on a **copy** of `advisor_pilot_20261113/` (budget.json, 12 attempt rows, assignments) and of the real Advisor state file (`LEGEND_ADVISOR_STATE` pointed at the copy, `LEGEND_ADVISOR_NOW` forced, the roadmap copied to a temporary file), so that ADV's live state, its evaluation 6 and its recall were not touched. The real campaign was re-read afterwards: budget.json unchanged (2,237 bytes), 12 attempt rows. Fixtures with the real files: they show the code paths on real data, not the runtime of ADV's session.

| Scenario (each starts from the same copied real state) | Forced time | Verdict | Presidio field |
|---|---|---|---|
| bounded pilot, no mode, before expiry | 2026-11-14T12:00Z | EVALUATE | ACTIVE |
| bounded pilot, no mode, after the pilot expiry | 2026-11-14T19:00Z | EXPIRED | PILOT ENDED ... (no continuous authorisation is in force) |
| continuous mode, after the pilot expiry | 2026-11-14T19:00Z | EVALUATE | ACTIVE |
| continuous mode, the next quiet hour | 2026-11-14T20:00Z | NONE | WAITING (legitimate) |
| continuous + `PAUSE: advisor` line in the roadmap section | 2026-11-14T20:30Z | PAUSED | SUSPENDED by the operator |
| continuous + `PAUSE: advisor` then `RESUME: advisor` | 2026-11-14T21:30Z | EVALUATE (the roadmap changed) | ACTIVE |
| continuous + `PAUSE: science` (another perimeter) | 2026-11-14T22:30Z | EVALUATE, the line is listed in `operator_controls` | ACTIVE |

What this shows: the bounded pilot behaves as before; the continuous mode carries on past the pilot expiry without touching the counters; an assignment's end is not a presidio end (the quiet hour reads as a wait); a pause for the Advisor stops evaluations and a resume lifts it; a pause for another perimeter is reported, not applied.

Not shown, with the reason: the launcher refusal under a pause, the weekly-allocation block and the history-preservation of counters are covered by `test_strategic_advisor.py` (class `Continuous`, fixtures); a duplicate recall is prevented by the existing `CronList` + recall-mark rule, which this change did not alter and was verified earlier (2026-11-14, ADV restored one cron without a second copy); **compaction survival of the in-session cron has not been observed** (the process continues through compaction, so it is expected to survive; unverified), and a recall lost with the process, a killed process or a switched-off machine is restored only by the next session that loads the mandate (`CronList`, then `strategic_advisor.py recall`). ADV treats the mode as pending its own confirmation; its recall (job 3382bb86) keeps running the same `tick`.
