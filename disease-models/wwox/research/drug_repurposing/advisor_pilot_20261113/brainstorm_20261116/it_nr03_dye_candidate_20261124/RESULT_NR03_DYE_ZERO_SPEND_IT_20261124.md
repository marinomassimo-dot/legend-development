# CAND-NR03-DYE-01, zero-spend half: Figure 2 of the 2023 glioma paper read (IT, 2026-11-24)

Actor `orchestrator` (IT successor, session 7cf5e85a), task ORCH-ROADMAP-IT59-20261119; ADV asked for this after the receipts. Source: PMID 36979157 (Kaluzinska 2023, Biology; `PAPER 405`), the held article text and **Figure 2 from the PMC open-data bucket** (saved under `files/figures/PMID36979157/`, untracked; Figures 1 and 3 to 6 not opened). Values are READ-OFF from the plotted bars at 789 x 952 pixels, approximate. Hypothesis level; not a claim; no individual-level data; not medical advice.

## What the paper measured, and how
One "Triplex" run on a single 96-well plate (Methods 2.4): TUNEL apoptosis, **BrdU incorporation** (DNA synthesis, time-resolved fluorescence, 24 h in starvation medium) and, in the same wells after the BrdU label, **PrestoBlue read eight times at 10-minute intervals** (the dye, up to 80 min). So the proliferation readout is **independent of the dye** (a DNA-synthesis assay, not a cell count); the dye is not normalised to anything. Assay in duplicate (two lines) or triplicate (two lines).

## The panels (stable WWOX overexpression against control, per line)
| Line | Apoptosis (2A) | BrdU proliferation (2B) | Dye (2C, 10 to 80 min) |
|---|---|---|---|
| T98G | up (*), about 11.8k against 8.7k RFU | **down** (**), about 31k against 93k | **down** about 45 percent at every point from 20 min (n.s. at 10 min) |
| DBTRG-05MG | up (**) | **up** (****), about 87k against 31k (about 2.8-fold) | **down** about 40 percent (significant from 20 min, p about 0.01) |
| U251MG | n.s. | n.s. (about 78k against 60k) | **down** about 33 percent (significant from 10 min) |
| U87MG | up (***) | **down** (*), about 27k against 48k | **down** about 55 percent (p < 0.0001 at every point) |

## Answer to the zero-spend half
* **The dye fell by about a third to a half in all four lines whatever BrdU did**: down with BrdU down (T98G, U87MG), down with BrdU unchanged (U251MG) and **down with BrdU up 2.8-fold (DBTRG-05MG)**. Across these four lines the dye does not follow DNA synthesis, which argues against "the dye is only cell number" as the whole explanation in this dataset (cell number itself is not counted; BrdU is S-phase incorporation, which is not cell number).
* **A same-sign drop with different cell behaviour is what a per-cell reductive-capacity change, a reagent or reductase effect, or an effect common to the construct would give**; it is also what a plain cell-number loss would give if overexpression lowered viable cell number in all four lines irrespective of BrdU (not excluded: no count, and apoptosis rose in only three).
* **T98G here falls with gain; the 2014 T98G statement (gain raises dye conversion, no number, authors point to a diaphorase transcript up more than 3-fold) has the opposite sign.** This paper does not settle which is right: different laboratories, constructs and read times.
* Same laboratory, bladder CAL-29 (2021 paper, ADV-218): loss raised the dye and BrdU; the gain arm lowered BrdU with the dye null at every time point. The 2023 glioma dye fall under gain is therefore the only gain arm in this laboratory's work in which the dye moves.

## What this changes in CAND-NR03-DYE-01
* The held-data half is done at figure level: **dissociation of the dye from BrdU proliferation is confirmed in DBTRG-05MG**, and the dye fall is uniform across the four lines.
* Still open (wet lab): the dye normalised to cell count together with oxygen consumption in a WWOX-deficient neural line; no held figure gives that.
* For `NR-03`: none of these dye readouts is a respiration measurement, and they do not agree in sign across systems or laboratories; they stay out of the complex I question.

## Limits
READ-OFF values from a 789-pixel figure; Figures 1, 3 to 6 and the supplementary archive not opened; duplicates for two lines; the dye run follows the BrdU label in the same wells (the paper does not say whether the BrdU step changes the dye signal); stable overexpression lines, not neural cells.
