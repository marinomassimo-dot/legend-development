# ADV-243: the friction of the advisor's record path, measured (HE, 2026-11-25 ~02:30Z)

Harness measurement; designs are proposals and ADV decides. Sources: `git log development/main` over the 48 hours before the read, `git status` and file contents of the root checkout (read-only), `framework/scripts/strategic_advisor.py`, `roles/advisor.md`. "Root" is the primary checkout; "main" is `development/main`.

## 1. Why the commands refuse in a worktree

- `primary_refusal()` in `strategic_advisor.py`: a linked worktree holds its own copy of the campaign folder, so its budget and counters would be a second campaign, while the state directory (outside the repository) is keyed by campaign name and would be shared.
- `roles/advisor.md`, first moves: assignment ids come from the root's `assignments.jsonl`, and a stale checkout reuses numbers.
- Refused outside root: `recall`, `tick`, `evaluate`, `assign`, `meeting`, `deliver`, `activate`, `disable`, `authorise-continuous`, `end-continuous`. `portfolio --upsert` is not refused.

The invariant is **one writer location: one budget, one id sequence**. It does not require that the location be the root checkout.

## 2. The copy

- ADV commits on main in 48 h, merges excluded: 95.
- **40 of 95** carried command output that only root can produce (`assignments.jsonl`; 39 of them also a new `ADV-NNN.md`). A further 22 only edited an existing `ADV-NNN.md` (result text, which can be written in a worktree). The meeting record appears in 93 commits; most of that is hand-appended text.

## 3. Root is frozen, so the commands read old data

- Root `HEAD` is `19a86daf5`; its last fast-forward was 2026-11-20 23:00Z; it was **1,535 commits behind** main at the read.
- 129 dirty paths, of which **128 were also changed on main** since that HEAD, so git cannot fast-forward over them.
- `assign`, `tick`, `status` and `meeting` run only from root and read task records, portfolio and roadmap from root's disk. The same walk as `assignment_states`, applied to both trees:

| of the 41 assignments since ADV-189 that main shows executed | main | root |
|---|---|---|
| taken in charge | 41 | 0 |
| executed (a DONE step) | 41 | 0 |

- Over all 244 drafted ids: executed 144 on main, 69 at root.
- Root roadmap: 12 roadmap commits behind, without the 'No idle laboratory' guidance. Root portfolio: no RP-046, RP-047, RP-048; older RP-017, RP-036, RP-038. `strategic_advisor.py` itself: 3 commits old.
- Commit events are read from the main ref and are current. Mandate transitions and openings are read from root records and so cannot fire for work after 2026-11-20.

## 4. Lost or stale

| what | measured |
|---|---|
| Campaign files at root that are identical to main (dirty only against the old HEAD) | 79 |
| Campaign files where root is older than main (copying them back would erase text) | 38 |
| Campaign files where both sides have own lines | 5 (portfolio, `ADV-200`, `201`, `202`, `221`) |
| Not yet on main | `assignments.jsonl` rows and files of ADV-243 and ADV-244 |
| **Missing from main** | the original briefs of **ADV-200, ADV-201, ADV-202** |

- `ADV-200.md` and `ADV-201.md` lost 18 lines for 2 in `ba05e128f`; `ADV-202.md` lost 14 for 3 in `4891bb177`. Each file now holds only the later addendum or result. The briefs survive at root and in history: `git show e248927f3:<path>` (200, 201), `git show 9e2736051:<path>` (202). How the overwrite happened is not established.
- No id was drafted twice. No portfolio row was removed by any commit (the two multi-line deletions removed conflict markers).
- Four framework files and one design record also carry uncommitted edits at root, dated about 2026-11-20 23:10. Compared line by line, main already holds all added lines except one in `framework/scripts/README.md` and one in `mandate_watch.py`.

## 5. Designs that remove the copy

All three keep one writer location, one budget and one id sequence.

| | design | removes the copy | removes stale reads | size and risk |
|---|---|---|---|---|
| **D1 (recommended)** | **Registered campaign home.** The state directory records one checkout path; `primary_refusal` accepts that path and refuses every other, root included. ADV runs the commands and lands from that one worktree, which merges main at each landing. | yes | yes | about an hour: the refusal, a `home` subcommand, tests, two lines of contract text. A removed or moved home must refuse with the way to re-register; disk cleanup must protect it. |
| D2 | **Write where you stand, counters outside the tree.** Id allocation and budget counters move to the state directory under the existing host lock; any worktree may write. | yes | only for the writing worktree | larger: counters migrate, and two worktrees appending to `assignments.jsonl` conflict at merge. |
| D3 | **`land` subcommand.** Root stays home; the command builds a commit on main from root's campaign files through a temporary index and publishes it. | yes | no | duplicates part of the publisher, skips the landing suites, and needs a rule for root files older than main. |

Not a design but a smaller step if none is chosen: an `export --into <worktree>` command that copies only new files and appends only new rows, never overwriting. It replaces the hand copy and leaves section 3 as it is.

**Order for D1:** (1) restore the three briefs on main; (2) land ADV-243 and ADV-244 rows from root; (3) register the new home from a worktree merged with main; (4) leave root's files in place until their content is shown to be on main, then ADV or HE refreshes root with a backup first. Nothing was changed at root in this measurement.

## 6. Until a design is in place

Do not read 'taken' or 'executed' from a root `tick` or `status` for work after 2026-11-20: read the recipient's record on main. Do not `reset` or `checkout` over root: it holds rows that are not on main.

## 7. Limits

- The executed and taken counts come from a re-implementation of the walk in `assignment_states`, run on both trees; the command itself was not run.
- The 40 of 95 count is a lower bound for landings that needed root: a landing that copied only a meeting record is not counted.
- Whether ADV's session compensated by reading main directly is not measured; ADV's commit messages show results verified on main.

## Re-open

If a root fast-forward happens, or the commands gain a way to read records from main, re-measure section 3.
