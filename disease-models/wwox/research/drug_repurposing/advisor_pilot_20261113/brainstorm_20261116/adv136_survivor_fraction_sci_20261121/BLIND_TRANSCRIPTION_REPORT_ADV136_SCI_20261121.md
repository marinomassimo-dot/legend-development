# ADV-136 blind transcription report, verbatim (producer: legend-delegate, dispatched with model sonnet and effort "medium" stated in the brief; read back by `framework/scripts/session_model_census.py` from the subagent transcript: model claude-sonnet-5-5, effort high, 2 turns, peak context 31,920 tokens; the Agent tool has no effort parameter, so the stated "medium" was not applied and the run was at high)

The delegate received only eight cropped panel images (no legend, no values, no thresholds, no question) and the instruction to transcribe, count and flag, not to interpret. Persisted from the session transcript, not from the agent output file. The crops themselves are third-party material: not in git; digests in `CROP_DIGESTS_ADV136_SCI_20261121.txt`, a copy in the root `files/` tree.

Blind transcription of 8 crops (printed numbers only, no interpretation). Panel titles are partly clipped in the crops, so I give only what is visible.

## crop_1 (title visible: "Cortex"; WWOX / HSP90)
Counts: 11 top-strip lanes, 11 printed numbers, 11 lane labels. No mismatch.
The Dead bar spans lanes 8-11. It starts under the lane-8 label and ends under lane 11.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no |
| 2 | WT | 1 | no |
| 3 | KO | 0.02 | no |
| 4 | LD | 2.2 | no |
| 5 | LD | 2.1 | no |
| 6 | HD | 2.6 | no |
| 7 | HD | 2 | no |
| 8 | HD | 0.5 | yes |
| 9 | LD | 0.9 | yes |
| 10 | LD | 1 | yes |
| 11 | LD | 1.5 | yes |

Less-than-certain readings: none. The only dependence on position is that lane 8's HD label sits at the left end of the bar, and I read it as under the bar.

## crop_2 (title partly clipped, likely "Mid-brain"; WWOX / HSP90)
Counts: 11 top-strip lanes, 11 printed numbers, 11 lane labels. No mismatch.
The Dead bar spans lanes 8-11.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no |
| 2 | WT | 2.2 | no |
| 3 | KO | 0.1 | no |
| 4 | LD | 0.9 | no |
| 5 | LD | 0.9 | no |
| 6 | HD | 5.2 | no |
| 7 | HD | 4 | no |
| 8 | HD | 0.1 | yes |
| 9 | LD | 0.6 | yes |
| 10 | LD | 0.4 | yes |
| 11 | LD | 0.2 | yes |

Less-than-certain readings: none.

## crop_3 (title clipped, likely "Hippocampus"; WWOX / HSP90)
Counts: 11 top-strip lanes, 11 printed numbers, 11 lane labels. No mismatch.
The Dead bar spans lanes 8-11.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no |
| 2 | WT | 2.3 | no |
| 3 | KO | 0.1 | no |
| 4 | LD | 1.4 | no |
| 5 | LD | 8.5 | no |
| 6 | HD | 28.2 | no |
| 7 | HD | 11.8 | no |
| 8 | HD | 12.9 | yes |
| 9 | LD | 5 | yes |
| 10 | LD | 3.8 | yes |
| 11 | LD | 2.5 | yes |

Less-than-certain readings: none.

## crop_4 (title clipped, likely "Cerebellum"; WWOX / HSP90)
Counts: 11 top-strip lanes, 11 printed numbers, 11 lane labels. No mismatch.
The Dead bar spans lanes 8-11. It starts under the HD label of lane 8 and ends under the last LD.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no |
| 2 | WT | 0.8 | no |
| 3 | KO | 0.02 | no |
| 4 | LD | 0.1 | no |
| 5 | LD | 0.09 | no |
| 6 | HD | 0.6 | no |
| 7 | HD | 0.6 | no |
| 8 | HD | 0.2 | yes |
| 9 | LD | 0.1 | yes |
| 10 | LD | 0.06 | yes |
| 11 | LD | 0.1 | yes |

Less-than-certain readings: none. Lane 5 (0.09) is small print but I read it clearly. Alternative reading: 0.08.

## crop_5 (title "Cortex", panel letter E; WWOX / HSP90)
Counts: 10 top-strip lanes, 10 printed numbers, 10 lane labels. No mismatch.
There is no Dead bar in this panel. The black lines at the bottom edge belong to other panels.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1.2 | no bar in this panel |
| 2 | WT | 1 (printed in bold) | no bar in this panel |
| 3 | WT | 1.7 | no bar in this panel |
| 4 | WT | 0.7 | no bar in this panel |
| 5 | KO | 0 | no bar in this panel |
| 6 | HD | 4.7 | no bar in this panel |
| 7 | HD | 6.3 | no bar in this panel |
| 8 | HD | 10.6 | no bar in this panel |
| 9 | HD | 8.2 | no bar in this panel |
| 10 | HD | 6.7 | no bar in this panel |

Less-than-certain readings: none.

## crop_6 (title "Mid-brain", panel letter F; WWOX / HSP90)
Counts: 10 top-strip lanes, 10 printed numbers, 10 lane labels. No mismatch.
There is no Dead bar in this panel. The lines at the bottom belong to other panels. The text "P90, P300" is a separate heading.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no bar in this panel |
| 2 | WT | 1 | no bar in this panel |
| 3 | WT | 1.5 | no bar in this panel |
| 4 | WT | 0.8 | no bar in this panel |
| 5 | KO | 0 | no bar in this panel |
| 6 | HD | 1.3 | no bar in this panel |
| 7 | HD | 1.5 | no bar in this panel |
| 8 | HD | 2.9 | no bar in this panel |
| 9 | HD | 1.6 | no bar in this panel |
| 10 | HD | 1.3 | no bar in this panel |

Less-than-certain readings: none.

## crop_7 (title "Cerebellum", panel letter G; WWOX / HSP90)
Counts: 10 top-strip lanes, 10 printed numbers, 10 lane labels. No mismatch.
There is no Dead bar in this panel. The lines at the bottom belong to other panels.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1.2 | no bar in this panel |
| 2 | WT | 1 | no bar in this panel |
| 3 | WT | 1 | no bar in this panel |
| 4 | WT | 1.1 | no bar in this panel |
| 5 | KO | 0.1 | no bar in this panel |
| 6 | HD | 0.1 | no bar in this panel |
| 7 | HD | 0.3 | no bar in this panel |
| 8 | HD | 0.4 | no bar in this panel |
| 9 | HD | 0.5 | no bar in this panel |
| 10 | HD | 0.2 | no bar in this panel |

Less-than-certain readings: none.

## crop_8 (heading "HD-p300"; WWOX / HSP90; tissue-name labels)
Counts: 6 top-strip lanes, 6 printed numbers, 6 lane labels. No mismatch.
There is no Dead bar in this panel.

| Lane | Label | Printed number | Under Dead bar |
|---|---|---|---|
| 1 | WT | 1 | no bar in this panel |
| 2 | KO | 0.2 | no bar in this panel |
| 3 | Cortex | 8.2 | no bar in this panel |
| 4 | Hippo | 10.7 | no bar in this panel |
| 5 | mid | 5.6 | no bar in this panel |
| 6 | Cere | 1.4 | no bar in this panel |

Less-than-certain readings: none.

Overall: all 8 crops were read without UNREADABLE entries. Lane, number and label counts matched in every crop. I did no computation and drew no conclusions. I read only the 8 named files.