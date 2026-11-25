# ADV-279 increment 1: five held partials read (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Every item below is another disease or another system: **NOT WWOX EVIDENCE**.

Rule, order and predictions: `PREREG_ADV279_RULE_SCI_20261125.md`, `PREREG_ADV279_ORDER_SCI_20261125.md`, `PREREG_ADV279_AMENDMENT1_SCI_20261125.md`. Blind second reading: `BLIND_STATEMENTS_INC1_SCI_20261125.md`, `BLIND_REPORT_INC1_SCI_20261125.md` (legend-delegate, sonnet, effort high stated). The delegate judged eight deliberately worded statements and supported none; this agrees with the reader on all eight and overturns no verdict. It added four limits, carried below.

## 1. Yield

| | strict | loose |
|---|---|---|
| Increment 1 (5 studies) | **2 of 5** | **4 of 5** |
| ADV-279 so far | 2 of 5 | 4 of 5 |
| For comparison, ADV-276 as ADV quotes it | 17 of 43 | 27 of 43 |
| Supplement-class studies (33914734, 39769031, 42875792, 28749468) | 2 of 4 | 3 of 4 |
| Figure-class studies (37781246) | 0 of 1 | 1 of 1 |
| Text-class studies | none in this increment | none in this increment |

Reversals of direction: 0.

## 2. Per study

### 33914734 (Gersing 2021, ASPA C152W; yeast and U2OS): STRICT
**Class of correction:** an absent or failed assay carried as a negative result.
**Consumer wording now:** "Insoluble stabilised variant with no measurable activity (ASPA C152W)" (card A02 and the IT6 P6 A02 card and packet); "accumulated insoluble pellet protein with no measurable activity (yeast and U2OS; earlier reports also found no residual activity)" (`HYP-20260709-08`; mechanism-intervention map line 702; `LIT-0706`; `PAPER 434` says "no enzyme activity could be measured").
**What the held files say:**
* Results: "even when we added an N-terminal GST-tag in an attempt to increase solubility, ASPA C152W was not produced in significant amounts (S2B Fig)... Unfortunately, similar to the previous reports, we were unable to detect any enzyme activity."
* S2C: the yeast growth assay tested vector and wild type only and showed no ASPA-dependent effect.
* Response to reviewers: "By assaying yeast cell lysates we found that there was not enough wildtype ASPA activity to obtain a reliable activity estimate"; "it was not possible to purify C152W from cultured mammalian cells, since the protein is largely insoluble"; "it is possible that the C152W variant retains some enzyme activity, but we were unfortunately not able to test this directly".
* Discussion: "very low activity could be detected when expressed in Pichia pastoris [21]", against another passage that says earlier studies "failed to show any residual enzyme activity".
* No activity measurement on the protein accumulated under route blockade, and none in U2OS, is described.
**Proposed wording:** "route blockade accumulated insoluble C152W protein; its enzyme activity was not measured (the authors' attempts with recombinant protein and yeast lysates could not test it, wild type included in lysates); earlier reports: none detected in COS-7, very low in Pichia." Replace "yeast and U2OS" after "no measurable activity" everywhere. (The earlier-report species are as the paper's Discussion gives them; those two primaries were not opened.)
**Bearing:** the card's negative precedent for route blockade rests on solubility, not on a measured lack of activity.

### 42875792 (Rathan-Kumar 2026, HIKESHI V54L; patient iPSC cells): STRICT
**Class of correction:** a single-lane signal that is not visible on the unedited blot, carried as a measured protein recovery.
**Consumer wording now:** `repurposing_10h_scientist-a_20261021.md` lines 262 to 264: "Proteasome inhibition restores it to about 20 percent of control at 100 nM for 48 h in one dose-time series (Supplementary Figure 3A, opened; no replicates drawn)", "protein return from an undetectable baseline", "closest measured precedent for the Q230P premise"; card A02 "HIKESHI: partial protein return with function-adjacent readouts".
**What the held files say:**
* Supplementary Figure 3A (densitometry, one point per condition, no error bars; read from the plot): HOM 48 h, percent of control, vehicle about 1, 1 nM about 6, 10 nM about 10, 100 nM about 23, 1 µM about 17, 10 µM about 18.
* Unedited blots (MOESM7, one page; PDF sha256 prefix 5960195c56acf6d0): at 48 h **no homozygous HIKESHI band is visible by eye** in any lane, reader and delegate. Screening contrast on the published 8-bit raster: control 28 to 31; clear heterozygous bands 12 to 18; HOM 100 nM 2.4 to 3.9, the highest HOM value but within the off-band noise (SD about 2; maximum about 7). A trace below the noise cannot be excluded.
* Same blot, heterozygous lanes: vehicle and 100 nM carry no band while 1 nM, 10 nM, 1 µM and 10 µM do. The delegate notes smaller GAPDH and HSP70 bands in those two lanes, so loading may contribute (not quantified).
* 24 h: three faint HOM bands at 100 nM, 1 µM and 10 µM (contrast 3.8 to 5.3 against 42 to 45 for control).
* Late window (Supplementary Figures 4 and 5): the comparator is labelled "D30 to D90 Vehicle"; no day-60-to-90 vehicle is shown. The text's marizomib sentence, "Day 60–90 treatment displayed a reduced amount of Olig2+ cells and MBP+ protein across all HIKESHI genotypes", is not seen for Olig2 in control cells (delegate blob counts, treated 50 against vehicle 41; single fields). In HOM, DAPI-positive nuclei also fall strongly.
**Proposed wording:** "the authors' densitometry gives about 20 percent of control at 100 nM for 48 h, one value per condition; on the published unedited blot no band at that lane can be told from noise, and faint HOM bands are seen at 24 h. Protein return in this precedent is weakly shown; the function read-outs stand on their own limits." Drop "protein return from an undetectable baseline" as an established step for PB.
**Not shown:** that the 20 percent is wrong. Their quantification may use the original scan and loading normalisation.

### 28749468 (Janczar 2017; ovarian cancer clones): loose
**Class of correction:** a supplementary panel that disagrees with its sentence.
**Consumer:** `DL-MECH-023` (and the working statement that PERK activation does not change with WWOX status).
* Supplementary Figure 6, panel labelled "p PERK" (legend: "PERK (ab65152)"; text uses ab65142): the band is **stronger in untreated than in paclitaxel lanes** (delegate: vector clone 54 against 22; WWOX clone 24 against 16, background-dependent; actin equal). Text: "Both IRE-1 and PERK showed induction or increase of phosphorylation...in all cell lines".
* Supplementary Figure 3: plot titles "48 hrs", legend "72 hours". Supplementary Figure 8 legend "alone or together" with no combined arm; Supplementary Figure 2 has no vector arm.
**Proposed addition to DL-MECH-023:** "the paper's own supplementary PERK panel does not show induction by paclitaxel (image reading), and whether its antibody is phospho-specific cannot be told from the files; do not use this paper for a PERK-branch direction in either sense." `DL-METH-114` and `DL-THER-115` unchanged.

### 37781246 (Kałuzińska-Kołat 2023; glioblastoma lines with WWOX over-expression): loose
**Class of correction:** a legend's "all cell lines" that its own table contradicts.
**Consumer:** `DL-MECH-054`, `CLAIM 011`.
* Figure 2E/4A, module membership / gene significance, U87MG, T98G, U251MG, DBTRG-05MG: HSF2BP .85/−.79, .72/−.58, .65 or .66/−.53, .75/+.74; POLE4 .91/−.82, .75/−.66, .80/−.58, .76/+.73. Figure 4 legend places both in the top-right corner "for all cell lines": on absolute gene significance at 0.65 HSF2BP passes in 2 of 4 lines and POLE4 in 3 of 4.
* At the paper's 0.7 driver threshold (Table_4) both genes are drivers only in U87MG and DBTRG-05MG. The sign is opposite in DBTRG-05MG against the other three.
**Proposed addition to DL-MECH-054:** "HSF2BP and POLE4 are drivers (0.7) in two of four lines, with opposite sign between them; the figure legend's 'all cell lines' is not borne out." The record's "five main figures read integrally" was written while the receipts held figures at captions only; the images were opened in this increment.

### 39769031 (Rico-Molina 2024; LDHA enzyme assay): no change
Supplement (47 pages): dose-response curves S65 to S74 cover analogues 3, 4 and 5 only; none for stiripentol (compound 1). Table 2 as card E02 records it (STP 9.9 ± 2.3; (S) 34.0; (R) 38.4; IC50 above 500). Unconsumed note from the delegate: the chromatogram of compound 2 (Figure S43) carries a second peak of nearly equal height that is stiripentol; no repository sentence uses compound 2.

## 3. Predictions after five (final scoring after ten)
P4 (a figure, supplement image or spreadsheet disagrees with text or legend): **already met** (28749468, 42875792, 37781246). P5 holds so far. P2 (loose 4 of 10, range 2 to 7) will very likely be exceeded: the point estimate was low.

## 4. The count behind the ten
Old rule (ADV-265): **3** studies readable from held bytes. Wider rule (counts figures and supplements held as separate files): **51**. Two routes agree on 43; only route A: 37248434, 41948127, 41664646 (no held XML), 41210171; only route B: 28045433, 28749468, 10.1101/2025.05.01.651195, 40301740 (route totals 47 and 47).

## 5. Method defects found
* **Error pages saved under figure and PDF names.** 30362252's "figures" are HTML "HTTP 404" pages; a magic-bytes check of 6,100 held files found 39 mismatches, 27 of them HTML or empty. A held-file count without a content check over-reports readability (for HE and for the acquisition step).
* **False consumer joins.** 33958783 was counted because CLAIM 024 cites corpus placeholder "P204", not PAPER 204.

## 6. Receipts and limits
Receipts `FTR-20261125-<pmid>-01`, depth `queried_not_full_read`; only the class named in each is marked read. Single laboratory per study; blot and image statements are screening measures or eye readings on published rasters, not densitometry of originals. The delegate read the 42875792 full text, which its statements did not name (it had already viewed and measured the blot). Primaries cited by these papers were not opened.
