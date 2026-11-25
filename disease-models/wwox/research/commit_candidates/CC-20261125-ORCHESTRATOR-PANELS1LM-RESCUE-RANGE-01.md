# COMMIT CANDIDATE — CC-20261125-ORCHESTRATOR-PANELS1LM-RESCUE-RANGE-01

**Actor:** `orchestrator` (IT) · **Task:** ORCH-ROADMAP-IT59-20261119 (re-read of Supp Fig 1L and 1M) · **Date:** 2026-11-25 · **target_wm_version:** `WM_v7.29` (unchanged)
**Origin of the finding:** `drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_panels1lm_20261125/RESULT_PANELS1LM_IT_20261125.md` (pre-registered; read-off from the embedded JPEGs of the held supplement File012; IT's own reading plus a blind verifier's, both partial: figures only, no author data).
**Status:** PROPOSED, for the next `BATCH_COMMIT` that the queue triggers. No registry file is edited by this act.

> Public, disease-level, de-identified. Hypothesis level; nothing here is medical advice. Reference genotype class only.

## 1 · CHANGE CLASS
**MINOR.** One qualification added to the evidence boundary of `CLAIM 002`, beside the list of qualifications that the deferred repointing of its Source would carry (the line «la proteina consegnata fra 0.4× e 7× il WT»). No conclusion, grade, status or number changes.

## 2 · Proposed sentence (English)
"Delivered-protein range, check 2026-11-25: the printed values under the AAV9 lanes of Supp Fig 1L and 1M (0.4 to 7 times wild type) are author densitometry; the Methods say blots were quantified 2 to 3 times and representative images are shown, so a printed value may summarise repeats. Read off the shown originals (File012 pages 6 and 7; two readers, one of them blind), the four printed 1L values and the printed 0.1, 0.1 and 0.3 of the three untreated SCAR12 lines in 1M reproduce within a factor 1.5 when each lane's band is captured where it sits and normalised to HSP90, and the printed 7 for WPM S1 AAV9 does not (it reads about 1 to 2 times wild type, no variant above about 2.2). The 1M HSP90 strips are clipped. The original 1M membrane has seven lanes; WPM D1 AAV9 and WPM D3 AAV9 are not in the published panel, and WPM D1 AAV9 reads about 0.1 to 0.3 of wild type, near its untreated line (D3 AAV9 and S1 AAV9 read near wild-type level). Which WPM D clone fed the functional arm is not stated. The printed values are carried as printed."

## 3 · What this does NOT do
No printed value is changed; no claim about conduct (the legend says the panels show the lines included in the single-cell experiment, so an omission by design is possible); no grade or ranking change; read-off from JPEG display exports, one blot per panel.

## 4 · Statements for the blind check at propagation time
1. File010 page 2 prints 1, 0.2, 0.4, 0.4, 0.9 under JH WT, LM-iPS and the three AAV9 lanes of panel L, and 1, 0.1, 0.1, 0.3, 7 under JH WT, WPM S1, WPM D1, WPM D3 and WPM S1 AAV9 of panel M.
2. File012 page 7 holds seven sample lanes (JH WT, WPM S1, WPM D1, WPM D3, WPM S1 AAV9, WPM D1 AAV9, WPM D3 AAV9); the File010 panel shows five.
3. File009, Immunoblot analysis: "Blots were repeated and quantified 2–3 times per experiment in Bio-Rad's Image Lab software. Representative images of those repeated experiments are shown."
4. The HSP90 strip of panel M has 34 to 72 percent of the pixels in each lane's band window at grey 5 or below.

## 5 · Blind check of the text statements, 2026-11-25 (IT dispatch; one verifier, sonnet, effort high)

Report as delivered: `it_batch1_verify_20261125/VERIFIER_REPORT_AS_DELIVERED_BATCH1_IT_20261125.md`. Statements 1 to 3 of section 4 and the legend sentence (panels L and M show the lines included in the single-cell experiment) were SUPPORTED, from page images at 300 dpi. The densitometry itself was blind-read earlier (`it_panels1lm_20261125/VERIFIER_REPORT_AS_DELIVERED_PANELS1LM_IT_20261125.md`). Detail: panel L prints no value under WSM S2 or WSM S5 in the text layer. Status: PROPOSED, blind-checked.

## BATCH DISPOSITION — `BATCH_20261125_002` (2026-11-25, ACTOR_ID `orchestrator`, MANUAL, mandate IT59), append-only

**Status:** PROPAGATED

1 record-scoped `replace-within` op on `claim_registry_current.md` CLAIM 002: the delivered-protein-range sentence added as its own line after the provenance note that lists the qualifications the deferred repointing would carry. **Change class restated: MINOR** (additive; `WM_v7.29` preserved). The densitometry was blind-read earlier; the text statements were checked in this batch's blind check (4 statements, SUPPORTED).
