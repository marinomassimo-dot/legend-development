# RESULT ADV-333 completion (IT38): PMID 31829254 read complete

Hypothesis level; nothing here is medical advice. Assigned by ADV after `RESULT_ADV333_IT_20261128.md` (partial read). The frozen rejecting observation of `PREREG_ADV333_IT_20261128.md` is unchanged and is applied here to the whole paper. Species mouse throughout.

## What was read
Producer: legend-delegate (sonnet 5.5, effort high), 2026-11-28: the Europe PMC XML whole (sha256 `785a10ea6b5998f1777e8fdf14c3b68301e8ae541f3e4b11cd8e49c176a29543`), reference titles (33), and all six figures opened as images from the PMC open-access bucket (the publisher image host answered 403 to this window; not retried). IT38 re-ran string checks on eight quoted passages and viewed Fig 6. Supplement: none found on 2026-11-28 in the XML, the PMC bucket listing, the Europe PMC supplementary archive, the publisher article page and the PMC article page. Data are available from the author on request, as printed; no contact is made.

## Answers to the frozen question
- **(a) Specificity control for the anti-WWOX staining: none found.** Text, legends and all six figures show no deficient-tissue, blocking-peptide, second anti-WWOX antibody, secondary-only or omission control, and no Western blot. One reagent: rabbit anti-WWOX 1:500, `sc-366,157`, Santa Cruz, as printed. The vendor datasheet answered 403: the catalogue entry's host species and validation are **not verified**.
- **(b) Per-animal proportions or values: none found.** Fig 6c is percentages with no cell count and no error; Fig 6e is mean ± SEM with no points and no stated unit of n; Fig 6b is per cell (n = 10 cells, mice not stated).
- **Verdict:** X1 (a citable specificity premise) stays rejected, now on the complete paper. This is a statement about what the paper holds, not about what its authors ran.

## What the complete read adds to the partial one
| Item | Source place | Reading |
|---|---|---|
| Direction of the proportion | Fig 6c, charts Medial and Lateral | The percentages are of WWOX-positive cells (73.88 medial, 70.24 lateral triple-labelled). The reverse fraction, TH+VGLUT2+ cells that are WWOX-positive, which a marker statement needs, is not reported |
| Figs 1 to 4 | all panels | No Wwox image or Wwox control in them; Fig 4c and 4d show other candidates. Fig 5c marks Wwox as the choice among five and prints no coefficient or P for it |
| Densities between experiments | Fig 4e legend against Fig 6e legend | VGLUT2+ cells 77.71 cells/mm2 (Slc17a6-like experiment, 3 mice) against 224.48 medial and 112.07 lateral (Fig 6e); TH+ 484.62 against 359.17 and 407.78. Different image sets; the paper gives no explanation. IT38 draws no conclusion from the difference |
| A repeated error term | Fig 4 legend | The two co-labelled densities (67.21 and 474.48) both carry ± 14.22; a copy error cannot be tested: the drawn error bars of Fig 4e look shorter than most legend ± values (second reader's approximate pixel reading), so the figure does not settle it |

Unchanged from ADV-333: WWOX triple-label IHC in male C57BL/6J mice, N = 6, 22 slices, 22 medial and 14 lateral images, **age not stated** ("adult" appears in the paper only for the Allen Brain Atlas mice and a reference title); no neuronal marker in the WWOX triple label; Wwox selected computationally (correlation screen, then top five, then in situ inspection), not for prior WWOX biology.

One further limit, an inference and not a statement of the paper: the Methods list goat anti-VGLUT2 and "rabbit or sheep" anti-TH, so a rabbit anti-WWOX triple label would use sheep anti-TH with goat and sheep primaries detected by separate anti-species secondaries; cross-reaction between those is possible and no control for it is shown.

## Second reader
A different delegate (sonnet 5.5, effort high), reading the XML and all six figures before the two texts (this result and the PAPER 571 draft): **2 of 77 clause parts MUST CHANGE (3 percent)**, 3 ADD, 72 OK; 30 statements about this session's own acts were not checkable from the sources. All five repairs are applied and were not re-read; the sentence on goat and sheep reagents was added afterwards and has no second reader.

## Decision (RP-017, owner ADV)
No change of direction. The row's premise line stands: immunoreactivity reported, not a demonstrated neuronal WWOX premise; missing observation: a deficient-tissue or peptide-block control and per-animal proportions. Two wording points for the row: the read is now complete (all figures; no supplement found), and the paper does not state the animals' age, so it does not support calling them adult.

## Negatives, dated
"None found" means: not in the sources and routes named above, 2026-11-28. Correction or retraction: `retraction_check.py` flagged 0 for PMID 31829254; reference screen SCREENED_CLEAN (33 declared, 30 screened, 3 without DOI in the deposited list the tool read; snapshot of 2026-10-21).
