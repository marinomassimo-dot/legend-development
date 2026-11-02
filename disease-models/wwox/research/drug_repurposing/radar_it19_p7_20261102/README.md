# IT19 P7 - how long do reopen questions wait (2026-11-02)

Non-canonical process record. Tool: `wait_model.py` (real plan at HEAD via `resolve_plan`, real `pick_questions`, `questions_per_run` = 2 from CONFIG; simulated days, no network, no state touched). Results: `wait_model_result.json` (before) and `wait_model_result_after.json` (after).

## Measured before any change (plan of 71 questions: 39 reopen, 15 work order, 11 roadmap, 5 diagnosis, 1 task step)
Reopen questions: median first asked on day 24, maximum day 61, 2 not within 60 days, 32 of 39 later than 14 days. Roadmap questions (weight 1-2): **never asked within 90 days** (11 of 11).

## Cause (not the weights)
The existing selector scores weight x days since asked, a repeat capped at 30 and a never-asked question counted as 30. A weight-3 question asked again after 10-30 days therefore ties or beats an unasked weight-1 or weight-2 question forever: the limit is throughput (2 questions a day for 71 questions) plus repeats crowding out first asks, not the weight of reopen questions (weight 2). A quota or a changed weight was not needed; the weights are untouched.

## Change (one constant)
A never-asked question counts as 90 days (`NEVER_ASKED_DAYS`), above the 30-day cap of a repeat times 3. Every question is asked once before a heavy one repeats. After: reopen median day 21, maximum day 30, none unasked; roadmap median day 36, maximum 39; diagnosis and work-order waits unchanged (median 2 and 7). Tests: `NoQuestionStarves` (2), existing 69 unchanged.

## Limits
A 71-question plan at 2 a day takes about 36 days to ask everything once: a month's latency for a reopen condition is acceptable for conditions that wait on literature, not for a condition that wants a fast reaction. Raising `questions_per_run` to 3 (simulated: reopen median 14, maximum 21) costs more requests per day and was not done. The simulation assumes the plan is stable for 90 days; every merge that changes a surface re-derives it.
