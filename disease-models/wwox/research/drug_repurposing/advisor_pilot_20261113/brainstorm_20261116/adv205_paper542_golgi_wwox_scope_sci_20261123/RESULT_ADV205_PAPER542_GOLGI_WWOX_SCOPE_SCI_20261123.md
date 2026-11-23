# ADV-205 result: PAPER 542 (Aragon-Ramirez et al.) WWOX perturbation under its actual controls

SCI window AB, 2026-11-23. Pre-registration `PREREG_ADV205_SCI_20261123.md` (first commit 3815dceef at 23:37:56Z under the id ADV-204, id corrected to ADV-205 in e3da9d358, content unchanged), frozen before any text of the paper was read by me. Hypothesis level; reference genotype class; no WWOX causal claim; nothing is medical advice. No delegate, model call or spend; no ranking row, no pharmacological direction, no neural ITGB1 restart, no duplicate of ADV-178.

Source: Aragon-Ramirez et al., "Golgi CATCHR complexes function as organizing hubs for vesicle tethering and fusion", bioRxiv preprint (PMID 42523332, PMC13405132, DOI 10.64898/2026.06.16.732723). **Preprint only: no journal version seen.** The Europe PMC XML matches version 3 (open-data bucket holds v2 and v3); WWOX statements, n and the single siRNA are the same in v2 and v3 text (differences are reference numbering and the placement of the supplement legends; the Fig 5C legend wording changed slightly).

## Answer first
**Disposition (b): a WWOX perturbation is present, but controls the pre-registration required are missing; keep the ambiguity visible. No re-grade to "WWOX evidence".** The catalog label "NOT WWOX EVIDENCE" is also not accurate in the other direction: this is not an incidental mention (disposition c is rejected), it is a single-siRNA knockdown with a quantified lectin readout.

**Narrowest statement the controls allow:** *in hTERT-RPE1 cells, one WWOX siRNA (verified at mRNA by RT-PCR, two repeats) was followed by higher plasma-membrane HPA and GNL binding, a lower COPB2 and GALNT2 colocalisation and a slightly smaller Golgi area, with n = 30 cells per panel; no second siRNA or knockout, no rescue, unit = cells.* That is an association after one siRNA, not a demonstrated WWOX-dependent mechanism. The abstract's "establishes WWOX as a previously unrecognized regulator of Golgi homeostasis and glycosylation" is stronger than these controls.

## Control checklist (the pre-registered five), with locators
| # | Condition | Finding | Locator |
|---|---|---|---|
| 1 | WWOX depletion verified | **Met at mRNA only**: RT-PCR, "Two biological repeats", endpoint gel plus bar (about 10,000 AU control against about 200 knockdown, read from the figure); no protein-level verification shown; commercial anti-WWOX antibodies "did not show any specific signal for IF" | Supplementary Fig 4C legend; Results, Fig 5 section; supplement page 4 image |
| 2 | Two or more independent siRNAs, or a knockout | **Missing**: one siRNA "used in previous studies" (cited to a breast-cancer paper, ref 58); no sequence, vendor, dose, time or transfection method anywhere in the Methods (the string siRNA occurs 3 times in the whole XML: Results and two supplement legend copies; checked in the Europe PMC XML and the bucket text of v2 and v3) | Results, Fig 5 section; Methods (absence) |
| 3 | Non-targeting or parental control in the same experiment | **Unclear**: the control is labelled "CTRL" and, in one supplement panel, "control (CTRL)"; the identity (non-targeting siRNA, mock, untransfected) is not stated; no scrambled or non-targeting term occurs in the text | Fig 5 images; Supp Fig 4D legend |
| 4 | Biological unit stated, with n | **Missing for the lectin readout**: "n = 30 cells" (Fig 5C legend, Supp Fig 4E, G); independent experiments not stated; Golgi area: Wilcoxon rank sum "W = 25487, p = 0.00159" (Fig 5B legend), and W cannot exceed n1 x n2, so at least about 160 objects per group if balanced, unit = Golgi objects or cells; no test named for Fig 5D, 5E or Supp Fig 4E | Fig 5 legend; Supp Fig 4 legend |
| 5 | Readout quantified | **Met**: HPA intensity about 9 against about 17.5 AU (asterisk), GNL about 6,700 against about 7,600 AU (about +13%, asterisk), COPB2 and GALNT2 Pearson about 0.47 against about 0.34 (asterisk); error bars not defined as SD or SEM (values read from the images, approximate) | Fig 5D, 5E; Supp Fig 4E |
| rescue | Not required for (a) but raises the category | **None**: no siRNA-resistant WWOX re-expression; myc-WWOX was used only for localisation | Results; Methods (absence) |

**Specificity points in favour:** SLC30A6 localisation unchanged after knockdown (Supp Fig 4G, ns), so the Golgi is not globally disrupted in the one marker tested; the phenotype resembles that of COG depletion in this paper's own lines.
**Specificity points against:** one reagent, mRNA-only verification, unit = cells, GNL effect small (about 13%), no second assay of glycosylation (no glycoprotein blot, no mass spectrometry); a broad cell-surface change is not excluded (prereg rule 1 not met).

## What else the source says (data against inference)
* **Localisation is overexpression-based:** WWOX localises to the medial Golgi by myc-WWOX (LQ 0.27, "n = 20 Golgi regions from 3 cells", Fig 5A); the endogenous protein could not be imaged. The proximity result is real in RPE1 cells (WWOX enriched in COG-TurboID), "and HEK293T cells (data not shown)".
* **Panel lettering disagrees:** the text and legend cite HPA as 5C and 5D, but the figure shows the HPA images as C, the HPA bars as D and the COPB2 and GALNT2 bars as E, while the legend places the quantification in C and the images in D (version 3).
* **Mechanism sentences are hypotheses:** the Discussion names a WW-domain scaffold and a redox role of the SDR domain as possibilities ("may"), with "the molecular mechanism of WWOX remains unknown".

## Surprise (one line)
The same HPA assay is rescue-validated for the VPS53, VPS54, COG4 and COG6 knockouts in this paper (Fig 1C legend: "Reduced HPA binding following rescue indicates restoration of normal glycosylation"), so the lab already has the knockout-plus-rescue design in hand for its own genes, but the WWOX arm has neither a knockout nor a rescue.

## Consumers and what changes
* **Depth queue (PAPER 542, LIT-0814):** keep "no re-grade"; suggest the entry note "WWOX perturbation present (one siRNA, RPE1, unit = cells, no rescue)" instead of "NOT WWOX EVIDENCE", the catalog owner decides. Nothing for a ranking row, a compound, RP-017, the neural ITGB1 branch or the WWOX causal model.
* **Revival condition (what would change disposition to a):** a second independent siRNA or a knockout with the HPA or GNL readout in independent experiments, or a rescue; or the final published version adding them.

## Receipt
FTR-20261123-42523332-01 (supersedes the partial FTR-20260921-42523332-01 in the sense of reread): preprint v3 only; coverage in the receipt.

## Limits
Preprint v3 only; Supplementary Fig 4 (supplement PDF page 4) and Fig 5 opened as images, other figures and the two supplement spreadsheets not opened; values read from images are approximate; the proteomics and the CCDC186 parts were not read beyond the passages that mention WWOX; no author contact; nothing about WWOX in a neural cell type.
