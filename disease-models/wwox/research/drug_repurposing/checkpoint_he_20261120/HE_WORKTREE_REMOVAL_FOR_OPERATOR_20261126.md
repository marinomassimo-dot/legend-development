# Released worktrees the operator can remove (HE, 2026-11-26T00:23Z; NOT run)

The auto mode classifier denied the removal to the HE session on 2026-11-26 (about 00:09Z). Nothing was removed. This file is for
the operator: run the command, or allow `git worktree remove` for a session. Rule applied: `branch_hygiene.py --removal` (HEAD on
`development/main`, clean, no process, a released window idle for 6 h; ADV decision record of 2026-11-25 23:46Z, which the operator may change).

## Eligible at the time of writing: 9 worktrees, 4.4 GiB

Run from any shell. `git worktree remove` without `--force` refuses a worktree with changed or untracked files. It does not look for
processes: if much later than the time above, run `python3 -B framework/scripts/branch_hygiene.py --removal` first and drop any name it keeps.

```
cd /home/desktop/legend-development && mkdir -p /home/desktop/legend-keep && mv .claude/worktrees/it_19_20261125/backup /home/desktop/legend-keep/it_19_backup && for n in he_n_20261125 he_o_20261125 he_s_20261125 it_17_20261125 it_18_20261125 it_19_20261125 it_20_20261125 sci_ag_20261125 sci_ah_20261125; do git worktree remove ".claude/worktrees/$n"; done
```

## Every candidate and when it becomes eligible

| Worktree | MiB | Eligible | Note |
|---|---|---|---|
| `he_n_20261125` | 503 | now |  |
| `he_o_20261125` | 503 | now |  |
| `he_s_20261125` | 505 | now |  |
| `it_17_20261125` | 503 | now |  |
| `it_18_20261125` | 503 | now |  |
| `it_19_20261125` | 509 | now | move backup/ first |
| `it_20_20261125` | 506 | now |  |
| `sci_ag_20261125` | 503 | now |  |
| `sci_ah_20261125` | 506 | now |  |
| `it_21_20261125` | 510 | 2026-11-26T00:39Z | move backup/ first |
| `sci_aj_20261125` | 505 | 2026-11-26T00:39Z |  |
| `he_t_20261125` | 505 | 2026-11-26T00:40Z |  |
| `he_u_20261125` | 505 | 2026-11-26T01:39Z |  |
| `sci_ak_20261125` | 506 | 2026-11-26T01:39Z |  |
| `it_22_20261125` | 513 | 2026-11-26T02:39Z | move backup/ first |
| `sci_al_20261125` | 507 | 2026-11-26T02:39Z |  |
| `he_v_20261125` | 506 | 2026-11-26T02:40Z |  |
| `he_q_20261125` | 504 | 2026-11-26T03:19Z |  |
| `it_23_20261125` | 508 | 2026-11-26T03:38Z |  |
| `he_x_20261125` | 510 | 2026-11-26T04:20Z |  |
| `sci_am_20261125` | 509 | 2026-11-26T04:39Z |  |
| `sci_an_20261125` | 509 | 2026-11-26T04:46Z |  |
| `he_p_20261125` | 503 | 2026-11-26T05:43Z |  |

Total of the table: 11.4 GiB. A time moves later if a session launched in that folder writes again.

## Kept for another reason

| Worktree | MiB | Reason |
|---|---|---|
| `adv_successor_a_20261120` | 512 | 1 ignored, deleted silently by remove; 7 process(es) |
| `he_g_20261123` | 489 | 18 process(es) |
| `it_24_20261125` | 510 | 1 process(es) |
| `it_25_20261125` | 447 | 1 process(es) |
| `it_26_20261126` | 446 | 24 changed or untracked; 1 process(es) |
| `it_successor_n_20261120` | 494 | 1 ignored, deleted silently by remove; 6 process(es) |
| `p022b` | 476 | 5 ignored, deleted silently by remove; 6 process(es) |
| `sci_ao_20261125` | 446 | 1 process(es) |
| `sci_ap_20261125` | 446 | 1 process(es) |
| `sci_aq_20261126` | 446 | HEAD not on development/main; 3 process(es) |

## What a landing leaves (measured 2026-11-26 00:21Z; nothing changed)

No landing-suite clone was left over (about 1.25 GB while a push runs, removed by the tool). Loose git objects: 321 MiB in 2,382
files, of which 2,262 (320 MiB) are unreachable, mostly view pages written and never committed; packing the reachable rest saves almost
nothing, and pruning unreachable objects is a deletion, so it was not done. Free space then: 15,461 MiB.
