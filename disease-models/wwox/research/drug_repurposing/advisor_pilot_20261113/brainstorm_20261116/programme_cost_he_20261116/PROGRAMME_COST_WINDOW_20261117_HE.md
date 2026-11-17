# Cost of one stated window: 2026-11-17T00:00:00Z to 2026-11-17T21:47:00Z (HE; ADV scoped continuation (b); non-canonical; read from transcripts)

Written for: ADV and the operator. **Measured, not estimated; no model call, no new service.** Same units and tools as `PROGRAMME_COST.md` (this folder): turns, output tokens, cache written, cache read, read from each transcript by `session_model_census.py` and tabulated by `trial_window_table.py`. The account quota is unknown and is not inferred: no figure here is a share of any plan, and an unknown is not zero. Cache read measures context re-read on each turn, not work; do not divide by it.

Commands (repository root, 2026-11-17 21:47Z): `python3 framework/scripts/trial_window_table.py --since 2026-11-17T00:00:00Z --until 2026-11-17T21:47:00Z --ref development/main --root .` (raw output: `window_table_20261117_0000Z_2147Z.txt`); the delegates of HE read independently with `python3 framework/scripts/session_model_census.py --json --since 2026-11-17T00:00:00Z --until 2026-11-17T21:47:00Z --dir <HE subagents folder>`.

## Three kinds of usage, kept apart
| kind | transcripts | turns | output | cache written | cache read |
|---|---|---|---|---|---|
| **Host sessions** (their own turns) | 4: HE 29e50812, IT 4325d70d, SCI 9400b253, ADV host e6526331 | 2,706 | 2,406,311 | 6,398,783 | 1,101,499,559 |
| **Campaign evaluation calls (evaluation-only usage)**: Advisor P20 to P27, each a separate headless run | 8 | 85 | 93,189 | 651,902 | 5,164,386 |
| **Delegates** (subagent transcripts of a host session): HE 66 runs, IT 3 runs, SCI 0, ADV host 0 | 69 | 485 | 968,920 | 3,221,454 | 38,037,555 |
Output tokens of the three kinds together: 3,468,420 (2,406,311 + 93,189 + 968,920).

Per host session (own turns only): HE 792 turns, 657,107 output; IT 518, 396,135; SCI 607, 712,958; ADV host 789, 640,111.
Evaluations: P20 and P21 are labelled incomplete by the tool (11 turns, 16,124 output, kept in the row above, not dropped); P22 to P27 complete (74 turns, 77,065 output). The evaluation rows are the Advisor's analyses only: they are **not** the ADV host session, which is the separate e6526331 row, and they are not the laboratory's total.
Delegates: all 66 of HE's ran on one model throughout (claude-sonnet-5-5, effort high at 324 of 324 turns, read back from the transcripts: 751,264 output, 19,304,003 cache read); IT's 3 runs (161 turns, 217,656 output) are summed by the table and their model was not read separately here.

## Overlap, and what is and is not covered
* **No double count by construction.** A session's own columns and its delegates' columns come from different transcripts (the delegates are subagent files; the table says its subagent columns are summed from the session's own subagent transcripts); an evaluation is a separate transcript from every host. HE's census of its own delegates (66 runs, 324 turns, 751,264 output) equals the table's HE subagent columns, which is the one cross-check made here.
* **A window figure is not a programme figure.** A session row is everything that session did in the window, scientific or not; this window includes harness work (this session's engine trials, the tick fix, the retrieval probe, the derived index) and the research of IT and SCI. No per-task attribution is given.
* **Covered:** the 12 transcripts of the main project folder whose files changed in the window (4 hosts, 8 evaluations); the other three project folders (worktree-specific) have none changed in the window.
* **Not covered:** (1) any session whose transcript is not on this machine or not in these folders, including any session of the Plan role that did not write here in the window; (2) the CI machine's minutes (the 2026-11-16 note counted them from the GitHub API; not repeated); (3) external services (none were authorised for spend; not measured); (4) the account's quota and its remaining allocation: unknown; (5) turns the transcripts do not record (a turn cut by a limit); (6) IT's delegate model and effort, read only as a sum.
* **Boundary effect.** Turns are counted by their own timestamp inside [00:00Z, 21:47Z); a session started the previous day is counted only from midnight (HE's earlier turns are excluded).

## Scale counts for the same window (counts, no interpretation)
335 commits on `development/main` (163 merges); 2 task records created; assignment events DRAFTED 11 and SENT 10 (by latest state: 10 sent, 1 drafted); 0 holds recorded; 9 receipts appended.

## Limit
This is consumption in the units the transcripts record. It does not say what any of it was worth: the value-per-cost method of `PROGRAMME_COST.md` (a numerator and a named denominator per line) was not repeated for this window.
