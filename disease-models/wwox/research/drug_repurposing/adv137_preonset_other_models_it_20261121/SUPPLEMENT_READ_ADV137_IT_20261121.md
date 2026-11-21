# ADV-137 increment 2: the supplement of the Scn1a conditional paper (PMC13285258), read in this window (IT, 2026-11-21)

Hypothesis level; a transfer question about another model, never Wwox evidence; no dose, no schedule, no recommendation; nothing here is medical advice. Chosen by IT (ADV's standing instruction to choose a next direction); the reason: `RESULT_ADV137_IT_20261121.md` carried the PN19 IBA1 and cytokine rows of this paper as "supplementary figures not read", and that gap sat under the only stain-level row with a one-day margin. **Not pre-registered as a prediction**: I opened the figures before writing any expectation, so every reading below is post-view and carries no pre-registration weight. The same model family read it; no blind verifier was used (a figure-panel read of plotted points).

## Route and artefact
Europe PMC REST `supplementaryFiles` for PMC13285258 (plain client, one request, no contact address, no challenge page). Archive sha256 `78609c9bef2f2eee37748790421fe851af32935ecc121ddc3b5cb2df9123e542` (about 265 MB, includes a video that was not opened). Items read (published names, digests computed by script):
* `EPI-67-3226-s003.tif` (cortex IBA1): sha256 `85a3e16211c2dcd9db3ca7cc3fd679256fd54f056c889ab1ca46aa6a8e8d0eee`
* `EPI-67-3226-s005.tif` (CA1 IBA1): sha256 `ad5f70697887d4c712cf0bd3e5a9dd190d50622e8433befc4c6b681913ffff86`
* `EPI-67-3226-s007.tif` (cortex GFAP): sha256 `2ad446bd16fdc8590b0278342fc41a58b2777ee78181741c093bac484bbacb96`
* `EPI-67-3226-s004.tif` (GFAP Western, behaviour, field potentials, later ages): sha256 `0f88ce2369ef82a6e4cc9777183fcfbf0eb95f5c0e797154fbceac5b7d9a4bd6`
* `EPI-67-3226-s008.tif` (astrocyte coupling, aggravation and long term only): sha256 `cb6b2cd7f54f25ae40cd54f169d337d1fb7d905be26e157ade957d467e229656`
* `EPI-67-3226-s010.tif` (cytokine mRNA): sha256 `9c341bf8eb6f9fb6e855562919059931f1fdad913b80b752e0745dec640edfd0`
* `EPI-67-3226-s001.docx` (Supplemental Methods): sha256 `a468f61615af1acb79e080b814663f04f1b4eaf9d93d44b685e9e0d059f55706`

Figure legends of the supplement are not in the archive as text; the figures carry printed p values and dots, and **n per arm below is counted from the dots (approximate, not printed)**. The numbered figure each item corresponds to (S2 to S5 of the main text) is not stated in the archive, so items are named by file.

## What the supplement says at the presymptomatic age (PN19; the paper's first age)
| Readout | Region | Arm n (dots) | Printed result at PN19 | Direction |
|---|---|---|---|---|
| GFAP mRNA | cortex (`s007`) | about 12 CTR, about 11 Scn1a+/- | ns | Scn1a mean higher (one dispersed set, several points 3 to 4.5) |
| GFAP MFI | cortex (`s007`) | 5 and 7 | ns | none |
| IBA1 mRNA | cortex (`s003`) | about 13 and 11 | ns | none |
| IBA1 MFI | cortex (`s003`) | 5 and 7 | ns | Scn1a lower |
| **IBA1 microglia Sholl** | **cortex (`s003`)** | cells; unit not stated | **ANOVA p = 0.0131; one post-test 0.0122** | **Scn1a more intersections (more branching)** |
| IBA1 mRNA, MFI | CA1 (`s005`) | about 12 and 10; 5 and 5 | ns | none |
| **IBA1 microglia Sholl** | **CA1 (`s005`)** | cells; unit not stated | **ANOVA p = 0.0359; post-test ns** | mixed: higher near 10 um, equal or lower beyond 15 um |
| Microglia soma size, density | CA1 (`s005`) | 5 and 4 | ns | density lower (Scn1a about 60, CTR about 90 cells per mm2 units as printed; no significance) |
| CCL2, IL1B, IL6, TNF mRNA | whole-tissue region not named in the image (`s010`) | about 12 and 10 per arm | all ns | none; CCL2 and IL1B Scn1a mean higher by eye, IL6 and TNF equal |

Aggravation and long-term readings in the same files (cortex GFAP MFI p = 0.0002 and 0.0231; cortex GFAP mRNA p = 0.0319; cortex IBA1 MFI p = 0.0104 at aggravation; CA1 soma size p = 0.0401; Western GFAP at long term p = 0.0079) agree with the main text, so the figures are the ones the paper cites.

## Supplemental Methods (`s001.docx`): allele origin
"We used the exon 25-floxed mouse line, which was maintained on a C57BL/6J background (Jackson Laboratories ...)"; Meox2-Cre mice "obtained from Jackson Laboratories". So the conditional allele is a **commercially supplied floxed line crossed to a germline Cre, a different construct from the replacement-type allele of PMC9350930** (supplied there by the originating laboratory per its Acknowledgments). Two different Scn1a constructs: the "one gene-model" convention of `RESULT_ADV137_IT_20261121.md` is conservative; counted separately the two Scn1a alleles become two independent models. Not applied here (the pre-registration counts alleles from different laboratories as independent, and the originating laboratory of the floxed line is not stated in the supplement).

## What this changes in `RESULT_ADV137_IT_20261121.md`
1. **The "supplementary panels not read" caveat on the Scn1a conditional PN19 row is closed for GFAP, IBA1 level, microglia soma and density, and four cytokine mRNAs: flat (ns), with n visible (about 5 to 13 per arm).** The stain-level count is unchanged (flat in Scn8a and in Scn1a conditional; rise in the replacement-type allele).
2. **New: a pre-symptomatic microglial morphology difference by Sholl (cortex ANOVA p = 0.0131, CA1 p = 0.0359, post-test significant at one distance in cortex only).** The direction in cortex is more branching in the mutant (not the retracted, amoeboid form that an activation reading would predict), the unit of the ANOVA (cells, not animals) is not stated, and the same ANOVA at aggravation and long term is not significant. It is the only presymptomatic difference in this paper, it is at the cell-morphology level, and it is marginal (p about 0.01 to 0.04 for an ANOVA over distances with cells as units). It does **not** turn the row into a rise at stain level; it is recorded as a morphology exception.
3. **The one-day margin (PN19 against "before PN20") stands; supplement does not date the first seizure** (the Supplemental Methods describe recordings only).
4. **Verdict unchanged: CONFLICT by kind of readout; FUNCTION THIN.** The sign prediction (glial markers not yet different before the first seizure) is again neither confirmed nor refuted as a rule; the supplement adds one exception to a flat row (Sholl) and does not change the count of models.

## Rejecting observation (for the choice of this direction, stated before it was closed)
Had the supplement shown a PN19 rise in IBA1 mRNA, IBA1 MFI or any of the four cytokines with a printed p below 0.05, the stain-level count would have moved to 2 flat and 3 rise and the Scn1a conditional row could no longer have been called flat. It did not (all level and cytokine readings ns); the only printed p below 0.05 at PN19 is the Sholl ANOVA.

## Limits
Dot counts are mine and approximate; no legend text; one blot or one region per readout; ANOVA over distances with cells as the unit is pseudo-replicated by construction; GFAP mRNA in cortex has a high-variance mutant set; the same model family read the panels and no blind transcription was run; the video in the archive was not opened; no spend, no e-mail address sent anywhere.
