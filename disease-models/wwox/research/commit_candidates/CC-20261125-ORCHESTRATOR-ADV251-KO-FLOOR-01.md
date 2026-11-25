# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV251-KO-FLOOR-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-251) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `advisor_pilot_20261113/brainstorm_20261116/it_adv251_20261125/RESULT_ADV251_IT_20261125.md` (pre-registered; read-off densitometry of Brain 2026 Supp Fig 1K).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One sentence added to the evidence boundary of the G372R limb of `CLAIM 030`. No conclusion, grade, status or number changes.

## 2 · Proposed sentence (English)
"Floor check, 2026-11-25 (ADV-251): on the authors' own week-16 membrane (Brain 2026 Supplementary Fig 1K) the two engineered-knockout lanes read 0.07 and 0.15 of the wild-type lane at 46 kDa (HSP90-normalised; read-off from a JPEG, wild-type lane not saturated; my read-off did not reproduce the authors' printed rescue values by a factor of about 6, so the scale is uncertain by that factor). The G372R lines printed at 0.1, 0.1 and 0.3 are on another membrane (Fig 1M); by this read-off the two 0.1 lines are not separable from the knockout floor and the 0.3 line is about two to four times it, order of magnitude only; the band-present reading for G372R stays unproven."

## 3 · What this does NOT do
No status or grade change, no ranking row, no card; the knockout floor is my read-off from pixels, not author data; no same-membrane comparison exists.

## 4 · Statements for the blind check at propagation time
1. Supp Fig 1K (File012 page 5) has five lanes: JH WT, JH WKO-1C, JH WKO-2C, JH WKO-1C AAV9, JH WKO-2C AAV9; File010 prints 1, no value, no value, 0.8, 1.4 under them.
2. File010 prints 1, 0.1, 0.1, 0.3 and 7 under JH WT, WPM S1, WPM D1, WPM D3 and WPM S1 AAV9 for panel M.
3. The 46 kDa band of the 1K wild-type lane has darkest grey 88 of 255 in the embedded JPEG (not clipped).
4. The knockout lanes carry a faint band at the 46 kDa position, read at 0.07 and 0.15 of wild type by my read-off.

## 5 · Revision, 2026-11-25 (IT, after the 1L/1M re-read; `it_panels1lm_20261125/`)
The sentence in § 2 says the read-off missed the authors' printed rescue values "by a factor of about 6". That holds for the 46 kDa rows alone. The rescue bands sit about 16 rows above the wild-type band; with both rows inside the window (exploratory on 1K, already seen) the rescue lanes read 0.31 and 0.51 against the printed 0.8 and 1.4 (a common factor of about 2.6), and the knockout lanes 0.04 (below noise) and 0.09 (0.05 and 0.11 on the 46 kDa rows). If this candidate is propagated, replace "by a factor of about 6, so the scale is uncertain by that factor" with "by a factor of about 6 on the 46 kDa rows and about 2.6 with the higher rescue band included, so the scale is uncertain by that factor; the authors' Methods say values come from 2 to 3 quantified repeats with representative images shown". Rule FLOOR_AT_OR_ABOVE_0.1 (larger knockout lane 0.08 or more) is met by 0.09, not by a margin. Statement 5 for the blind check: the 1K strip reads rescue lanes at 0.31 and 0.51 when both band rows are summed (read-off, not author data).
