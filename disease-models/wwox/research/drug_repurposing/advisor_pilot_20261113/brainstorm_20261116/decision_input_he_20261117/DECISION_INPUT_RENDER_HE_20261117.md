# Decision input of the proactive evaluation: measurement and what was simplified (ADV scoped continuation (a), HE, 2026-11-17)

Characters, not tokens or money. No model call: the brief is rendered by `build_brief_p` in `framework/scripts/strategic_advisor.py` from the repository state. Method: `render_ab.py` (this folder) renders the brief twice in one process on ONE observation (same commit, same state), once with the previous renderers and once with the new ones, so that no input differs between before and after.

## Sizes on the same inputs
| Section of the brief | Before | After |
|---|---|---|
| Whole brief | 83,224 | 81,367 (-1,857, -2.2 %) |
| Operator roadmap | 35,992 | 35,992 (unchanged) |
| Assignments already drafted | 10,378 | 8,700 |
| Living Research Portfolio | 8,981 | 8,981 (unchanged) |
| Neutral entry points | 6,702 | 6,702 (unchanged) |
| Observed state | 2,354 | 2,201 |
| Laboratory activity | 324 | 303 |
| Incomplete attempts | 355 | 350 |
Plan's saved rendering before the continuation was 80,983 (roadmap 35,457; assignment history 9,725; portfolio 8,159; entry points 6,702); the live inputs have grown since, so the first column is the same code on today's inputs, not Plan's number.

## What was changed (lossless)
The JSON blocks were printed with one line per key and one indent per level, and the same four mandates (task, verdict, path) were repeated under most of the 27 assignments. Now: one line per assignment; each mandate named once, with its verdict and path, and referenced by task id. Every assignment keeps recipient, key, origin, highest evidence level and mandates; every mandate keeps verdict and path. `render_ab.py` checks that no id, key, recipient, level, task, verdict or path of the old render is missing from the new one (27 assignments, 0 missing), and `test_the_assignment_render_names_each_mandate_once_and_loses_no_field` pins it. The advisor suite passes (174 tests). The one-space separators of the old form are kept because the readers and tests of the brief match `"key": "value"`.

## Duplication measured, and why it is not the lever
Verbatim repeated runs of ten words or more, second and later occurrences, across the whole brief: 2,472 characters (3.0 %), of which 1,758 were in the assignment block (removed above) and 69 in the roadmap. The brief is not long because text is repeated; it is long because the roadmap carries 96 lines of dated operator instructions (36 % of the characters in 22 entries), the assignment and portfolio records accumulate history, and the entry points table prints per-file sizes.

## Candidates NOT applied (kept until the owner reconciles them)
They are operator or ADV text; I did not move them and ask ADV to decide. Sizes are the entry's characters in the roadmap block.
| Roadmap line | Entry | Chars | Why it is a candidate | Why it was kept |
|---|---|---|---|---|
| 93 | 2026-11-13 night mission, "ends 2026-11-14T09:33Z" | 1,584 | window ended; the entry on line 92 says the night mission and its report "stay as historical" | the reconciliation (which of its clauses still bind, for example "a wet-lab experiment is described, never commissioned") is the owner's |
| 88 | 2026-11-14 24-hour trial, "observation window ends 2026-11-15T15:29:29Z" | 1,746 | window ended; the entry says the end of the window "does not revoke the continuous mode" | its standing clauses may be carried by the 2026-11-15 standing entry on line 22; I did not verify that |
| 74 | pilot campaign limits | 1,021 | the sentence "the 3/3 and the 5/6 are historical, not the current limit" (about 330 characters) | the current limits are in the same paragraph and `budget.json` |
Together 4,351 characters (5 % of the brief). If ADV confirms, the form is a stub in the hot text (date, first sentence, "full text: roadmap_current.md line N") with the entry unchanged in the roadmap file, so nothing is deleted; a renderer rule or a roadmap edit are both possible, the first leaves the operator's file untouched.
Not examined as candidates: the portfolio rows (16 rows, 7,779 characters; the five longest are 3,599 of them, mostly dated "next:" chronicle written by ADV), the entry-points table (6,702; the "largest file" column serves the 20,000-byte rule in the contract), laboratory ownership (4,289; sourced from the protocol, not forked).

## Reversal
Revert the renderer change in `strategic_advisor.py` (functions `_compact` and `render_assignment_states` and their four call sites); nothing is stored, so there is no data to restore.
