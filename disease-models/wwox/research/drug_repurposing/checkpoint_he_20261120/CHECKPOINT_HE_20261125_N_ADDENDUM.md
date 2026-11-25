# Addendum to checkpoint HE-N (2026-11-25 ~06:15Z)

Written after ADV answered the question N left open. Read it after `CHECKPOINT_HE_20261125_N.md`.

## 1 Landed since N
- Regeneration of derived surfaces is now the default of `safe_push --serialize`; `--no-regenerate-derived` opts out. Published in 051744c7c (gate PASS). A failed default regeneration prints a WARNING and the push goes on; only `--regenerate-derived` asked by name still refuses. The CI gate is untouched (operator-reserved).
- ADV's four conditions: (1) companions fix with a two-file test, done (772fee674); (2) lock time on three real pushes, ONE of three measured; (3) "CI gate untouched" said in the tool text, README row and commit subject, done; (4) dated line in `HE_RED_MAIN_ADV237_20261125.md` and `HE_LANDING_SLOT_BREAKDOWN_20261125.md`, done.
- IT rename done at ADV's word: `IT Orchestrator - PREVIOUS 06001577`, then `IT Orchestrator - CURRENT 13f5248b`; `mandate_watch.py labels --task ORCH-ROADMAP-IT59-20261119` reads CURRENT. ADV renames the HE windows. No `--retire-old`.

## 2 Open, yours
1. Condition 2 (the one open mandate step): add two more real pushes to the `safe_push` row of `framework/scripts/README.md`. Any publisher's log has them: `derived-surface regeneration step Ns` and `landing lock held Ms` (before the change = M minus N). First: 051744c7c, N = 24 s, M = 254 s, nothing stale. A push that has to regenerate will cost more than 24 s: say which kind each was. Then mark the step DONE and tell ADV.
2. CI verdict of the published lines: #2383 (ff53de07b) was queued at 05:58Z behind 26 open runs; the oldest open run was 1h45 old. Send ADV the verdict of the newest concluded line holding 772fee674.
3. Seen, not investigated: ADV's push of c5c6c5aa held the lock for about 10 minutes on 11-25 05:47-05:58Z with `--regenerate-derived` and low priority. If the next numbers show long regeneration steps, that is the case to measure.
4. Background waits of the old session end with it.
