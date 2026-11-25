# Disk survey by unique inode (HE, 2026-11-25 15:29Z), report only

ADV's request (15:15Z): free space 24 GB at 12:30Z, 19 GB at 15:15Z. Nothing was deleted except HE's own trial clone (1.2 GB, no unique content), removed after this survey.

"Freed if removed" counts only inodes whose every link lies inside the item; "modified in last 3 h" counts inodes by modification time (a copy that keeps old times is missed). Raw data and scripts, outside git: `files/coordination/he_disk_survey_20261125/`. `root` covers `files/`, `.git` and the rest of the primary checkout without worktrees. The table's `local` and `local_share` rows overlap by about 0.7 GB of the totals.

## Open (not done, the successor's)
- Growth per hour per area measured from two surveys (the 3 h column is an indication only).
- The safe-to-remove list with the rule for each item: closed, integrated, clean worktrees (17 present); job folders of PREVIOUS windows older than 24 h; dead clones in /tmp (`framework/scripts/tmp_clone_report.py`). Never a live or PREVIOUS window of the last 24 h, never `/tmp/claude-1000`, never transcripts.

## Summary

at 2026-11-25T15:29:43Z free GB  20.01 used GB 186.88
| area | items | apparent GB | freed if removed GB | modified in last 3.0 h GB |
|---|---|---|---|---|
| tmp | 35500 | 103.63 |  37.05 |   0.35 |
| home | 90 |  28.06 |  21.96 |   1.38 |
| worktree | 17 |   8.85 |   8.85 |   1.12 |
| claude | 2 |   7.36 |   7.36 |   0.24 |
| root | 3 |  70.93 |   5.53 |   1.11 |
| job | 56 |   4.24 |   4.24 |   0.18 |
| cache | 16 |  12.95 |   2.40 |   0.01 |
| local_share | 8 |   1.56 |   1.56 |   0.00 |
| local | 4 |   0.69 |   0.69 |   0.00 |

| item (freed >= 0.3 GB or recent >= 0.3 GB) | freed GB | recent GB | note |
|---|---|---|---|
| tmp/claude-1000 |  21.08 |   0.00 |  |
| home/.vscode |   9.69 |   0.00 |  |
| claude/projects(transcripts) |   7.09 |   0.24 |  |
| home/.config |   3.96 |   0.00 |  |
| root/files |   3.27 |   0.65 |  |
| home/.vscode-server |   2.25 |   0.00 |  |
| cache/uv |   2.00 |   0.00 |  |
| home/.codex |   1.76 |   0.38 |  |
| root/other |   1.71 |   0.06 |  |
| home/legend_browser_tmp |   1.67 |   0.30 |  |
| local/share |   1.56 |   0.00 |  |
| local_share/claude |   1.56 |   0.00 |  |
| tmp/legend-ethosuximide-inputs |   1.33 |   0.00 |  |
| home/legend_he_trial |   1.23 |   0.70 |  |
| job/5fef7cc4 |   1.18 |   0.00 | IT Orchestrator - PREVIOUS 5fef7cc4 / done |
| tmp/legend-wwox-qr-inputs |   1.06 |   0.00 |  |
| root/.git |   0.55 |   0.41 |  |
| worktree/it_19_20261125 |   0.53 |   0.04 |  |
| worktree/sci_ah_20261125 |   0.53 |   0.04 |  |
| worktree/adv_successor_a_20261120 |   0.53 |   0.04 |  |
| worktree/it_fu_20261124 |   0.53 |   0.00 |  |
| worktree/he_s_20261125 |   0.53 |   0.53 |  |
| worktree/he_q_20261125 |   0.53 |   0.02 |  |
| worktree/it_18_20261125 |   0.53 |   0.00 |  |
| worktree/he_n_20261125 |   0.53 |   0.00 |  |
| worktree/sci_ag_20261125 |   0.53 |   0.00 |  |
| worktree/it_17_20261125 |   0.53 |   0.00 |  |
| worktree/he_p_20261125 |   0.53 |   0.00 |  |
| worktree/he_o_20261125 |   0.53 |   0.00 |  |
| worktree/sci_ah_land |   0.53 |   0.00 |  |
| job/3b826442 |   0.53 |   0.00 | HE - PREVIOUS 3b826442 / done |
| worktree/it_successor_n_20261120 |   0.52 |   0.00 |  |
| worktree/he_g_20261123 |   0.51 |   0.00 |  |
| tmp/tmpr1z1_3h6 |   0.51 |   0.22 |  |
| worktree/p022b |   0.50 |   0.00 |  |
| worktree/it_20_20261125 |   0.46 |   0.46 |  |
| tmp/legend-meeting-cross-runtime-20261123 |   0.45 |   0.00 |  |
| local/lib |   0.45 |   0.00 |  |
| tmp/legend-dashboard-aligned-release.r7dBMYGm |   0.44 |   0.00 |  |
| tmp/legend-dashboard-dossiers-release.ccLOFYHc |   0.44 |   0.00 |  |
| tmp/it55_a |   0.42 |   0.00 |  |
| home/snap |   0.37 |   0.00 |  |
| job/961aabbb |   0.37 |   0.00 | IT Orchestrator - PREVIOUS 961aabbb / done |
| tmp/tmpdg1l7r4n |   0.36 |   0.00 |  |
| home/.npm |   0.35 |   0.00 |  |
| tmp/tmp6dizctew |   0.35 |   0.00 |  |
| tmp/headcopy |   0.34 |   0.00 |  |
| cache/pip |   0.32 |   0.00 |  |
| home/it_tmp_n |   0.31 |   0.00 |  |

| /tmp name pattern | entries | freed GB | recent GB |
|---|---|---|---|
| claude-N | 1 |  21.08 |   0.00 |
| tmp* | 10571 |   8.93 |   0.34 |
| legend-ethosuximide-inputs | 1 |   1.33 |   0.00 |
| legend-wwox-qr-inputs | 1 |   1.06 |   0.00 |
| * | 16 |   0.47 |   0.00 |
| legend-meeting-cross-runtime* | 1 |   0.45 |   0.00 |
| legend-dashboard-aligned-release* | 2 |   0.44 |   0.00 |
| legend-dashboard-dossiers-release* | 2 |   0.44 |   0.00 |
| itN_a | 1 |   0.42 |   0.00 |
| legend-gnx-lp-deps | 1 |   0.22 |   0.00 |
