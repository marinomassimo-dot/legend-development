# CC-20261004W7-C1-AGE-DOSE-CONFOUND-01 — a fixed-total-vg mouse design cannot separate age from dose per tissue, and its "younger is higher" sentence holds for CSF routes by IHC only

- `context_policy: SOURCE_FIRST` (first pass written before the window and dose candidates were opened).
- Source: PMID 41751597 (`FTR-20261004-41751597-01`), peer-reviewed, open access; manifest `VERDICT: PASS`. WWOX occurrences: zero (an earned null for the gene).
- Change class: **MINOR.** One research-line record. It narrows no `consolidated baseline` claim. It corroborates `CC-20261003W5-A-WINDOW-STATUS-01` (no expression-matched age comparison exists) and adds a worked case to `CC-20261003W5-C-DOSE-SCALAR-01`.
- **Nothing here is medical advice.**

---

## 1 · The finding in one sentence

In a neonatal-to-juvenile mouse study that deliberately used one fixed total dose per animal, body weight rises about tenfold and brain weight about fivefold between injection at postnatal day 1 and day 28, so dose per gram of tissue falls by those factors with age in every arm, the authors' statement that expression is higher after younger injection "regardless of route" is carried by CSF-route immunohistochemistry (n of 2 to 5 per bar, no statistics) and is **not** reproduced in the intravenous arm or in whole-cerebrum vector-genome counts, and the paper therefore **cannot** separate an age effect from a dose-per-tissue effect, which is the same confound the held window record (the wave-3 rejection) identifies.

## 2 · The numbers, each with the command that produced it

All from the persisted JATS of PMID 41751597, tables read cell-wise (`<tr>`/`<td>` iteration), not from flattened text.

| Quantity | Value | Source cell |
|---|---|---|
| Body weight, mean of the two sexes, day 1 / 5 / 10 / 28 | 1.41 / 2.70 / 5.98 / 13.70 g (ratio day 28 to day 1: 9.7) | Table A1 row "Body Weight mean (g)": 1.36 2.76 5.95 13.47 (female), 1.46 2.64 6.02 13.92 (male) |
| Whole brain, mean of the two sexes, day 1 / 5 / 10 / 28 | 0.087 / 0.183 / 0.336 / 0.444 g (ratio 5.1) | Table A1 row "Whole Brain mean (g)" |
| Dose per gram body weight at 2.5 x 10^11 vg, day 1 versus day 28 | 1.8 x 10^11 versus 1.8 x 10^10 vg/g (arithmetic: 2.5e11 divided by the mean weight) | derived |
| Dose per gram brain at 2.5 x 10^11 vg, day 1 / 5 / 10 / 28 | 2.9e12 / 1.4e12 / 7.4e11 / 5.6e11 vg/g (derived); at 5 x 10^11 day 28: 1.1e12 | derived |
| Day-28 arms received the higher total dose (5 x 10^11) except ICV (2.5 x 10^11) | stated in Methods and Results | Table 1 and Results 3.2 |
| Whole-cerebrum GFP vector genomes per diploid genome, ICV 2.5e11, day 1 versus day 28 | 0.294 versus 0.396 (n 10 each) | Table A3 |
| Same, IV, day 1 (2.5e11) versus day 28 (5e11) | 0.00276 versus 0.00464 | Table A3 |
| Same, IT and ICV, day 1 versus day 5 (both 2.5e11) | 0.246 versus 0.957 | Table A3 |
| Caudal-brain GFP-positive area by IHC (panel read by eye, about +/- 3 points; n 2 to 5), CSF routes, day 1 versus day 28 | about 67 to 76 versus about 23 to 38 percent | Figure 2b |
| Same, IV, day 1 / 5 / 28 | about 10 / 16 / 14 percent | Figure 2b |

## 3 · What this adds, bounds or leaves untouched

- **Adds** to `CC-20261003W5-C-DOSE-SCALAR-01`: a fourth worked case of the fixed-total-vg scalar, and the first in the repository with both an age series and the organ weights needed to convert it (Table A1 itself is in the source).
- **Corroborates** `CC-20261003W5-A-WINDOW-STATUS-01`: no source yet matches expression across ages and finds efficacy falling with age; this one is a biodistribution study, has no efficacy endpoint, and is not a window result in either direction. The revival trigger stated there has not fired.
- **Bounds** the authors' advice that "day 1 injection overestimates the transduction a postnatal human would reach and underestimates the minimally effective dose": the sentence rests on a design in which day-1 animals received a larger dose per tissue, so over-estimation of transduction at day 1 may be an effect of dose per gram and not of age.
- **Leaves untouched** every wave-3 to wave-5 statement about neonatal tolerisation: this study has no immune endpoint and no immunosuppression arm.

## 4 · Transfer limits

Mouse, wild type, one reporter vector (self-complementary AAV9, strong constitutive promoter, GFP), total vg per animal, one analysis time (day 56). Vector genome counts, not protein. Neither dose nor age transfers to a WWOX cassette or to a human infant: the authors' own mouse-to-human dose approximation is a citation and the human-age analogy (day 1 as a preterm infant, days 5 to 10 as full-term to toddler, day 28 as pre-pubescent) is a citation. A constitutive reporter models neither human missense allele.

## 5 · Ops (provisional)

### 5.1 · `disease-models/wwox/research/research_lines_current.md`

| field | value |
|---|---|
| op | `append` (new record, after the current final research-line record) |
| record | `RL-C-20261004w7c2 — Age at dosing is confounded with dose per tissue in a fixed-vg mouse design; the "younger is higher" sentence is CSF-route IHC only` |
| status | `open` |
| tag | `INFERENZA` |
| body | §1 to §4 of this candidate carried verbatim, with the §2 table; cross-references `RL-GT-001`, `CC-20261003W5-A-WINDOW-STATUS-01`, `CC-20261003W5-C-DOSE-SCALAR-01`, `CC-20261003W3-C-RESTORATION-SPEC-01` |
| anchor | none required for an append |
| class | MINOR |

## 6 · What would change this, and what would falsify it

- **Would falsify the confound reading:** a study that injects age cohorts with dose scaled to brain mass (or to body weight) and still finds higher expression after younger injection by whole-tissue qPCR in every route.
- **Would strengthen it:** the same finding that the age fall disappears or reverses once dose per gram is matched.
- **Would be a window result in the sense of the wave-3 revival trigger:** matched expression across ages with efficacy falling with age in a disease model.

### LOCATOR TRIPLES FOR BLIND AUDIT

Format: `(proposition | verbatim quote | anchor)`. Each artefact is on disk and each quote was verified by the manifest validator against the artefact named in the manifest of the PMID in the bracket.

- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Total vector genomes were fixed per injection and not scaled to age or body weight, so dose per body weight was higher in the youngest animals. | Doses were not adjusted to age or body weight | Methods 2.3 Study Design)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Younger animals received the larger dose per body weight; the authors state it. | Younger mice, at P1 and P5 treatment, received a higher vector dose per body weight compared to older mice because the doses were fixed and not adjusted for weight or tissue size. | Results 3.1, Summary)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Brain and spinal cord expression appeared higher after injection at younger ages regardless of route. | regardless of route of administration, GFP expression in younger mice appeared to be higher than in older mice. | Results 3.2, Summary)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (The authors say no significant dose effect was detected and that the study may be underpowered rather than saturated. | No significant dose effects on biodistribution were detected, which might be a reflection of the study being underpowered to see these differences rather than a saturation effect at the lower dose. | Discussion, para 1)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (The authors give a mouse-to-human dose approximation for the lower dose, citing another source. | a 2.5 × 1011 vg mouse dose approximates to a 1.00 × 1015 vg human dose | Discussion, para 1)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Authors' advice: day-1 injection overestimates the transduction a postnatal human would reach and so underestimates a minimally effective dose. | since it overestimates the transduction efficiency that could be expected in a postnatal human, and thus underestimates a minimally effective dose. | Discussion, last para)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Table A3, cerebrum, intracerebroventricular lower dose: day 1 mean 0.293985 versus day 28 mean 0.396319 vector genomes per diploid genome (n 10 each); no fall with age by qPCR in whole cerebrum for this route. | Cerebrum P1 ICV (2.5 × 1011 vg) 10 0.293985 0.069654 | Table A3, Cerebrum, P1)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Table A3, cerebrum, ICV, day 28 (same dose as day 1). | Cerebrum P28 ICV (2.5 × 1011 vg) 10 0.396319 0.295485 | Table A3, Cerebrum, P28)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Table A3, cerebrum, intravenous: day 1 (lower dose) 0.002756 versus day 28 (higher dose) 0.004638; no fall with age. | Cerebrum P28 IV (5 × 1011 vg) 11 0.004638 0.001302 | Table A3, Cerebrum, P28)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Table A3, cerebrum, intravenous, day 1. | Cerebrum P1 IV (2.5 × 1011 vg) 10 0.002756 0.000864 | Table A3, Cerebrum, P1)
- [PMID 41751597, artefact `files/fulltext/PMID41751597_Rioux2026_PMC.derived.txt`] (Table A1 body weight by age (female then male): about 1.4 g at day 1, 2.7 g at day 5, 6.0 g at day 10, 13.5-13.9 g at day 28. | Body Weight mean (g) 1.36 2.76 5.95 13.47 17.07 1.46 2.64 6.02 13.92 22.13 | Table A1, Body Weight row)
