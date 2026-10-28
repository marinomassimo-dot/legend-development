# mandate_watch: live proofs of the P14 states (2026-10-29)

Non-normative record. Run on a probe mandate (WATCH-PROBE-20261028, a throwaway session and record in the scratchpad), session absent from the live listing, `--quiet-minutes 0`, real processes. Restart proof during real work: the in-session cron on 2026-10-28 20:31 UTC (iteration 4).

```
1 idle, silent, resumable (no job):
  STOPPED_RESUMABLE RESUME | session absent from the live listing and silent, authorised work remains (1 executable step(s) remain; next: OBJ_P[0] 
2 long SILENT job alive (sleep 60, writes nothing) while the session is idle and silent:
  RUNNING NONE | job 'silent-long' is alive (pid 323333) even if its output is silent
3 same label again (duplicate execution refused):
  False already running: not started a second time
4 job killed without an exit status (process died):
  STOPPED_RESUMABLE RESUME | session absent from the live listing and silent, authorised work remains (1 executable step(s) remain; next: OBJ_P[0] 
5 waiting for tests = a tagged test job alive:
  RUNNING NONE | job 'tests' is alive (pid 323408) even if its output is silent
6 job finished, to collect:
  STOPPED_RESUMABLE RESUME | session absent from the live listing and silent, authorised work remains (1 executable step(s) remain; next: OBJ_P[0] 
7 explicit pause:
  PAUSED NONE | record verdict RELEASED
8 completed (no push condition applies to this probe root):
  COMPLETE NONE | record verdict RELEASED
9 unreadable record:
  UNKNOWN NONE | record verdict UNREADABLE: <path of the probe record>
10 duplicate request (self-call twice, same queue state):
  first: STOPPED_RESUMABLE RESUME
  second: STOPPED_RESUMABLE NONE | a request is already pending for this queue state
```
