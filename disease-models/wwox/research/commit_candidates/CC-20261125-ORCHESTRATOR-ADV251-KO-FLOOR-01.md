# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-ADV251-KO-FLOOR-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (ADV-251) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `advisor_pilot_20261113/brainstorm_20261116/it_adv251_20261125/RESULT_ADV251_IT_20261125.md` (pre-registered; read-off densitometry of Brain 2026 Supp Fig 1K).
**Status:** PROPAGATED (`BATCH_20261125_004`; see the BATCH DISPOSITION block at the foot). No registry file is edited by this act.

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

## 6 · Blind check and the wording that propagates (IT, batch 2, 2026-11-25)
One blind verifier (`legend-delegate`, sonnet, effort high stated; read back high), statements B5 to B8 in `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/statements_batch2d.tsv`, report `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_batch2_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH2D_IT_20261125.md`. The verifier made its own densitometry on the embedded JPEG and the uncropped File012 image without seeing the first reader's numbers. Results against the section 4 and 5 statements: 1 and 2 SUPPORTED (lanes and printed values; the legend names the species as human iPSC organoids at week 16); 3 **corrected**: the wild-type 46 kDa band is not clipped in either image, but the «darkest grey 88» belongs to the uncropped File012 image; the supplement panel gives 63 (both unclipped); 4 and 5 SUPPORTED within the spread: second reader, both band rows summed, knockout lanes 0.055 and 0.113 (range 0.016 to 0.187 over background choices; uncropped image 0.062 and 0.133), rescue lanes 0.22 and 0.45 in the panel (0.33 and 0.58 uncropped), against the first reader's 0.04 and 0.09 and 0.31 and 0.51. Printed values divided into read-offs: second reader 0.27 and 0.32 (panel), 0.41 (uncropped); first reader 0.39 and 0.36. **Statement 6 of the revision in section 5 is corrected:** the Supplementary Methods (File009, page 7) say blots were «repeated and quantified 2 to 3 times per experiment» and representative images are shown; they do not say that the numbers under the lanes are means of those repeats or how they are normalised.
**Proposed sentence, replacing section 2 and the revision of section 5:** «Floor check, 2026-11-25 (ADV-251; two independent readers of the same JPEG, the second blind): on the authors' own week-16 membrane (Brain 2026 Supplementary Fig 1K, human iPSC organoids, one blot image; read-off from a JPEG, not author data) the two engineered-knockout lanes read about 0.04 to 0.13 of the wild-type lane after HSP90 normalisation with both band rows summed (first reader 0.04 and 0.09; second reader 0.055 and 0.113, up to 0.19 by background choice), and the wild-type 46 kDa band is not clipped (darkest grey 63 in the supplement panel, 88 in the uncropped image). Both readers read the printed rescue values (0.8 and 1.4) about 2.5 to 3.7 times higher than their own read-offs, so the scale is uncertain by that factor; no held text defines the printed numbers (the Supplementary Methods say blots were quantified 2 to 3 times per experiment and representative images are shown). The G372R lines printed at 0.1, 0.1 and 0.3 are on another membrane (Fig 1M); by the read-off the two 0.1 lines are not separable from the knockout floor and the 0.3 line is about two to four times it, order of magnitude only; the band-present reading for G372R stays unproven.»
Rule FLOOR_AT_OR_ABOVE_0.1 (larger knockout lane 0.08 or more): met by 0.09 (first reader) and by 0.113 to 0.133 (second reader), not by a wide margin.

## BATCH DISPOSITION — `BATCH_20261125_004` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED (wording corrected by the blind check)

CLAIM 030 floor-check paragraph (same op list). **Change class restated: MINOR.** **Blind check:** call D of batch 2, B5 to B8, with the verifier's own densitometry: knockout floor 0.04 to 0.13 (two readers), rescue values read 2.5 to 3.7 times below the printed ones, «darkest grey 88» belongs to the uncropped image (63 in the panel), the Methods do not say the printed numbers are means.
