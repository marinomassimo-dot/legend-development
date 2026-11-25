# ADV-279 increment 1: report of the blind second reading (legend-delegate, model sonnet, effort high stated in the dispatch)

Saved as returned (final message of the delegate, harness indentation removed). Statements: BLIND_STATEMENTS_INC1_SCI_20261125.md.
Hypothesis level; not medical advice.

ADV-279 increment 1, blind second reading. All eight statements judged: **none of S1 to S8 is supported**. None needed "cannot be told". Hypothesis level; not medical advice.

Paths are under `/home/desktop/legend-development/files/`.

## Verdicts

### S1 (PMID 33914734): not supported
**How I looked.** I read the article XML in text form, the response letter (.docx) and the S2 Fig image, and checked the sheet names of the s009 workbook (no activity sheet).

**Locators.**
- Article: "even when we added an N-terminal GST-tag in an attempt to increase solubility, ASPA C152W was not produced in significant amounts (S2B Fig)... Unfortunately, similar to the previous reports, we were unable to detect any enzyme activity."
- Letter: "By assaying yeast cell lysates we found that there was not enough wildtype ASPA activity to obtain a reliable activity estimate"; "it was not possible to purify C152W from cultured mammalian cells, since the protein is largely insoluble"; "it is possible that the C152W variant retains some enzyme activity, but we were unfortunately not able to test this directly".

**What it means.** No attempt is described as using protein accumulated under proteasome blockade. The article's "unable to detect any enzyme activity" is not a measured zero.

**What cuts against, or is easy to miss.**
- In lysates even wild type gave no reliable estimate.
- The NAA growth assay (S2C) tested only vector and wild type, and showed no ASPA-dependent effect.
- Bortezomib "removed the growth defect" in a Ura3-fusion reporter. That reads out abundance, not ASPA activity.
- The article is inconsistent. One passage says previous studies "have failed to show any residual enzyme activity ... [15,17,21]". Another says "very low activity could be detected when expressed in Pichia pastoris [21]".

### S2 (PMID 42875792): not supported
**How I looked.** I extracted the single embedded raster (2352x1716) with `pdfimages` and enlarged panel D (48 h). Lane order was fixed from the GAPDH bands; HIKHOM 100 nM is the 11th of 13 sample lanes.

**By eye.** No HIKESHI band in that lane, or in any HIKHOM lane, even after contrast stretch and background subtraction.

**My measurement.** Grey-level contrast of a 7-row band window against flanking rows. I used two window widths, each with and without a ±3 px vertical search.
- CON: 28 to 30.
- Clear het bands: 12 to 18.
- HIKHOM 100 nM: 2.4 to 3.0.
- Other HIKHOM lanes: -1.0 to 1.5.
- Noise (117 off-band positions): mean -0.7 to 0.2, SD about 2.0, 95th percentile 2.4 to 3.4, maximum about 7.

HIKHOM 100 nM is the highest HIKHOM value but within noise (about 1.4 to 1.8 SD). Its row profile has no local minimum. This is a processed 8-bit figure raster, so it cannot exclude a trace below the noise.

### S3 (PMID 42875792): not supported
**By eye.** Het bands at 1 nM, 10 nM, 1 µM and 10 µM. No band in het vehicle. None, or at most a speckled trace, at het 100 nM.

**My measurement.** Same method and noise as S2.

| Het lane | Contrast |
|---|---|
| vehicle | 1.0 to 1.5 |
| 1 nM | 11.6 to 11.7 |
| 10 nM | 16.9 to 18.4 |
| 100 nM | 2.5 to 2.8 |
| 1 µM | 16.9 to 17.1 |
| 10 µM | 16.4 to 16.8 |

By eye the GAPDH and HSP70 bands in the vehicle and 100 nM lanes are also smaller or fainter, so lower loading may contribute. I did not quantify that.

**What the reader would miss (S2 and S3, same PDF).**
- **24 h, panel C:** three faint bands are visible in HIKHOM at 100 nM, 1 µM and 10 µM, and not in HIKHOM vehicle, 1 nM or 10 nM.
  - My contrasts: 5.3, 3.8 and 5.0, against 0.5 to 1.0 for the other three HIKHOM lanes and 42 to 45 for CON. Noise SD 1.4, maximum off-band 7.7.
  - Numerically they are modest (2.5 to 3.5 SD). The alignment of the three visible bands is the stronger evidence.
- **72 h, panel E:** no HIKHOM band by eye. Het vehicle and 1 nM are very faint.
- **Against the article text:** it says "restoration of HIKESHI protein to around 20% of CON cell amount at 100 nM carfilzomib treatment for 48 h". The 48 h blot on this page does not show it. The quantification may rest on other replicates or on Supplementary Fig. 3, which I did not open, so this does not show the number is wrong.

### S4 (PMID 42875792): not supported
**How I looked.** I viewed both TIFFs whole, enlarged the CON and HIKHet Olig2 panels, and counted red blobs per panel (minimum area 12 px).

**By eye.** CON with marizomib day 60 to 90 shows as many or more Olig2+ cells than CON vehicle. HIKHet and HIKHOM are reduced with both drugs. CON with carfilzomib shows fewer and dimmer cells.

**Blob counts, treated vs vehicle,** at red >40, with red >110 in brackets:

| Genotype | Carfilzomib | Marizomib |
|---|---|---|
| CON | 24 vs 41 (8 vs 26) | **50 vs 41 (28 vs 27)** |
| HIKHet | 3 vs 29 (1 vs 16) | 7 vs 27 (4 vs 16) |
| HIKHOM | 3 vs 15 (0 vs 11) | 3 vs 15 (1 vs 12) |

HIKHet with carfilzomib has many tiny dim specks below the area cut-off, so 3 understates what the eye sees. These are single representative fields, not quantification.

**What the reader would miss.**
- The comparator is labelled "D30 to D90 Vehicle". There is no day-60-to-90 matched vehicle in these figures.
- Both figures reuse the same vehicle micrographs (correlation 0.95 to 0.997 for Olig2 and DAPI after a shift of a few pixels, 0.80 to 0.99 for MBP).
- The article says day 60 to 90 marizomib reduced Olig2+ cells "across all HIKESHI genotypes". The CON images contradict that.
- It also says "there were abundant DAPI+ cells". In HIKHOM, DAPI blobs fall from 390 to 81 (marizomib) and from 392 to 88 (carfilzomib), which suggests general cell loss.
- The article has a sentence saying marizomib did not affect Olig2+ percentage "in both CON and HIKHOM genotypes", right after reporting a HIKHOM increase. It is probably a slip for HIKHet.

### S5 (PMID 37781246): not supported
**How I looked.** Figure 4A scatter, the enlarged Figure 2E table, and `Table_4.XLSX`.

Values are MM / GS from Figure 2E:

| Gene | U87MG | T98G | U251MG | DBTRG-05MG |
|---|---|---|---|---|
| HSF2BP | 0.85 / -0.79 | 0.72 / **-0.58** | 0.66 / **-0.53** | 0.75 / 0.74 |
| POLE4 | 0.91 / -0.82 | 0.75 / -0.66 | 0.80 / **-0.58** | 0.76 / 0.73 |

- On absolute GS, HSF2BP passes in 2 of 4 lines and POLE4 in 3 of 4. MM passes everywhere.
- `Table_4.XLSX` agrees: sheet `U87MG green+pink GSEA` rows 99 and 129, and sheet `DBTRG-05MG green+pink GSEA` rows 81 and 112. Neither gene is in the T98G or U251MG driver sheets.

**What the reader would miss.**
- GS is negative in three lines, so a signed threshold would leave only DBTRG-05MG.
- Table 4 defines drivers at 0.7, while Figure 2 says the threshold was "set at ≥0.65 to facilitate the overlap".
- Figure 2D's red-labelled genes in lists of three or more lines include POLE4 but not HSF2BP. Figure 4 still pairs the two as a signature.

### S6 (PMID 28749468): not supported
**How I looked.** I extracted the page 6 raster, enlarged the "p PERK" strip and measured it.

**By eye.** The untreated lanes are darker than the paclitaxel lanes, clearly so in Vector-9.

**My measurement** (background just above the band):
- Vector-9: untreated 54, paclitaxel 22.
- WWOX-8: untreated 24, paclitaxel 16.
- Actin is essentially equal (about 213 to 215).

WWOX-8 depends on the background choice, because there is a smear over the upper left (one choice gives 10 vs 10). In no choice is paclitaxel stronger.

**What the reader would miss.** The legend names the antibody "PERK (ab65152)" while the panel says "p PERK". These files do not settle whether it is phospho-specific. The legend also gives thapsigargin 6 h and 24 h; the paclitaxel lanes are 24 h only.

### S7 (PMID 28749468): not supported
**How I looked.** Rendered page 3 and read the .docx legend.

Both plot titles say "(48 hrs)". The legend says "72 hours" for both the SP600125 exposure and the tunicamycin treatment. Supplementary Figure 2's plots say 72 hrs and match their legend.

**What the reader would miss.** The tunicamycin axis labels read "200 ng/µl" (one "200 ng/ul"), which is a high dose if literal. SP600125 alone lowers survival to about 0.6.

### S8 (PMID 39769031): not supported
**How I looked.** Text search of the 47-page PDF, a contact sheet of all pages, and rendered pages 37 and 44 to 47.

Section 6, "Dose response curves against hLDHA", holds Figures S65 to S74. These cover only compounds 3, 4 (isomers) and 5. Figure S43 identifies stiripentol as compound **1** ("corresponds to stiripentol (1)"), and there is no curve for 1 or 2.

**What the reader would miss.**
- Figure S43, the chromatogram of compound **2**, shows a second peak of nearly equal height that is stiripentol. The sample as shown is roughly a mixture.
- The fitted curves look fixed near 100% at the top and heading to 0 at the bottom, although some points at 1000 µM sit around 5 to 17%. That is my reading of the picture, not a stated constraint.

## Scope and deviations
- **One blindness deviation.** I read the PMID 42875792 full-text XML, which S2 to S4 do not name. It is the paper itself, not a project record. I used it for the "against the article text" points. I had already viewed and measured panel D before opening it.
- **Skipped on purpose.** I did not read `framework/protocols/delegation_budget.md` §2 and §7, because your blindness limit excludes other repository files.
- **Not opened.**
  - PMID 42875792: `MOESM1` to `MOESM3`, `MOESM6`, `SuppFig3_render.png` and the .webp main figures.
  - PMID 39769031: the .zip and `PMC11675970.1.pdf` in `supplement/PMID39769031_r2/`, so S8 is judged only for the named PDF.
  - PMID 37781246 and PMID 28749468: the article XMLs.
- No network, no commits, no repository edits.

Scripts are in `/home/desktop/.claude/jobs/8ee4045d/tmp/verify_inc1/tools/`. Images, plus text and PPM/PGM extracts, are in `/home/desktop/.claude/jobs/8ee4045d/tmp/verify_inc1/img/`. The most useful are `d_hik.png`, `d_hp.png` (inverted), `c_hik.png`, `con_olig2.png`, `het_olig2.png` and `perk.png`.
