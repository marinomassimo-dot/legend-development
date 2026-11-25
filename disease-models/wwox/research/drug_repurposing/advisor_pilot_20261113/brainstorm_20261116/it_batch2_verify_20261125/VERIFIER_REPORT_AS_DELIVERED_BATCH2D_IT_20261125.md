# Blind verifier report, batch 2 call D (blot and firing statements B1 to B8, PMID 42397075), as delivered (2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high (stated in the dispatch), 8 statements as (statement, source, anchor), no candidate, no prior densitometry and no conclusion given; statements in `statements_batch2d.tsv`. Hand-back text below, unchanged except for this header. The delegate could not write a report file; this file is the saved hand-back. Read-back: see `read_back_batch2.md` in this folder (the delegate says it could not read its own setting back; the transcript is the source).

---

BLIND SOURCE VERIFICATION, PMID 42397075 (Steinberg et al., Brain 2026, human iPSC-derived cerebral organoids), statements B1-B8

Setting read back: I was asked for sonnet at high effort. I did not read it back from a transcript, so treat it as a request.
Sources opened: the five supplement PDFs and their .txt (File008 to File012), the accepted-manuscript PDF and `_fitz.txt`, and the page-renders and figure JPEGs in `PMID42397075_Steinberg2026_assets/figs/`. I also opened the `_assets` figure JPEGs for Figures 1 and 6.
Not opened: READING_NOTE*, FULLTEXT_READ_RECEIPT*, *_derived.txt, anything under disease-models/, ledger/ or other repository folders.
Work folder: /home/desktop/.claude/jobs/6739e4ff/tmp/b2/out3. It holds the scripts densitometry.py, densitometry2.py and densitometry_uncropped_K.py, the output densitometry_output.txt, the extracted images in raw10/ and raw12/, and the crops and overlays in img/. I ran everything with `python3 -I`.

## Where things are (locators used below)
- **Supp Fig 1 images.** File010 PDF page 2 is one embedded JPEG, 1619x2048 px, with an opaque soft mask in the blot areas. Panels K, L and M are at the bottom (`raw10/p2-000.jpg`).
- **Supp Fig 1 legend.** File010 page 3.
- **Uncropped blots.** File012 page 5 is 1K, page 6 is 1L, page 7 is 1M. Each is a pair of small JPEGs (a WWOX strip and an HSP-90 strip) with marker lanes and no printed numbers.
- **Supplementary Methods, immunoblot paragraph.** File009 page 7.
- **Panel letter.** The letter "L" is almost entirely cut off in the embedded image, so panel L is identified by position and by File012 page 6.
- **Panel N.** I checked every file. The supplement has K, L and M only. There is no panel N.
- **Panel-range citations in the AM.** The main text cites "Supplementary Fig. 1K-M" (line 366) and "Supplementary Fig. 1L-N" (line 894). The "-N" citation points to a panel that does not exist.

## Measurement method for B2, B6 and B7
- I used the embedded JPEG as it is: `pdfimages` extraction at the native 1619x2048, converted to 8-bit grey. The R, G and B channels are identical in the blot regions.
- A read-off from a JPEG is not author data. The pixel values are display values after unknown contrast adjustment and JPEG compression, and linearity with protein is unknown.
- **Lane windows and rows (File010 p.2 pixel coordinates).**

| Panel | Lane windows (x) | WWOX band-row window | HSP-90 band-row window |
|---|---|---|---|
| K | WT 88-153, WKO-1C 158-227, WKO-2C 228-296, WKO-1C AAV9 297-360, WKO-2C AAV9 362-437 | rows 1926-1959 | rows 1972-2004 |
| L | seven lanes between x 618 and 1012 | rows 1906-1950 | rows 1961-2002 |
| M | five lanes between x 1190 and 1535 | rows 1902-1948 | rows 1957-1992 |

  I drew the windows as rectangles over the image and checked them by eye.
- **Signal.** The signal is the summed grey deficit (background minus pixel, negatives clipped to zero) over the whole lane window. I did not use a manual band box.
- **WWOX background.** The primary variant uses one common clean-lane box background per blot: K 243, L 236, M 233, taken as the median of the knockout-lane flank rows. I varied it by -4 and +3 grey levels. Alternatives were a per-lane flank background and an unclipped signed sum.
- **HSP-90 background.** I used a per-lane flank background.
- **Normalisation.** WWOX divided by HSP-90, then divided by the same ratio for the JH WT lane. This is my assumption. No held text says how the authors normalised or what the printed numbers are (see B8).
- "Upper" and "lower" rows in K are the bands above and below row 1941/1942 (WT band centre row 1949, rescue-lane upper band centre about row 1935). The legend says the specific WWOX bands are the lower 46 kDa band and an upper band at about 48 kDa.
- **Uncertainty.** One blot image per panel, no replicate. The spread over background choices is given in the ranges below. JPEG artefacts and unknown linearity are not quantified.

## B1. Printed values in Supp Fig 1M and 1L: SUPPORTED, with qualifications
Locator: File010 p.2, panels M and L, read at full resolution; the legend is on File010 p.3. I read the printed values off the image.

Facts and verdicts:
1. **Fig 1M.** SUPPORTED. The printed values are 1 under JH WT, 0.1 under WPM S1, 0.1 under WPM D1, 0.3 under WPM D3 and 7 under WPM S1 AAV9. There are five lanes and five numbers.
2. **Fig 1L.** SUPPORTED. The printed values are 1 under JH WT, nothing under WSM S2 or WSM S5, then 0.2 (LM-iPS), 0.4 (WSM S2 AAV9), 0.4 (WSM S5 AAV9) and 0.9 (LM-iPS AAV9). There are seven lanes and five numbers, and the blanks are really blank.
3. **Week and species.** SUPPORTED. The legend says "(L) Immunoblot analysis of WWOX levels in WOREE lines and their AAV9 rescue included in the scRNA-seq experiment in week 16 cerebral organoids" and "(M) ... SCAR12 lines ... week 16 cerebral organoids". The lines are human iPSC lines: JH-iPS11 WT and WKO, LM-iPS, the WSM S clones, and the WPM S and D clones. The panel header in File012 reads "Week 16 COs of WT vs WOREE vs AAV9-hSyn-hWWOX rescued WOREE samples", and the 1M header says SCAR12.
4. **Replicate unit.** UNDERSHOOT. The numbers are single printed values per lane with no spread. No held text says how many organoids went into each lane, how many blots were quantified, or what the number is relative to. Each lane is one lysate. Methods say organoids were homogenised, with 30-50 µg protein loaded.

Incidental observation, outside the wording of B1: my read-off (human organoids, week 16, one lane each, single blot image per panel) differs from the printed values, as follows.
- **Fig 1L, WWOX/HSP-90 vs JH WT** (read-off range over the background variants; ratio = read-off / printed):

| Lane | Printed | Read-off | Range | Ratio |
|---|---|---|---|---|
| LM-iPS | 0.2 | 0.146 | 0.111-0.181 | 0.73 |
| WSM S2 AAV9 | 0.4 | 0.377 | 0.341-0.468 | 0.94 |
| WSM S5 AAV9 | 0.4 | 0.317 | 0.270-0.394 | 0.79 |
| LM-iPS AAV9 | 0.9 | 0.839 | 0.768-0.943 | 0.93 |

  WSM S2 and WSM S5 read about 0.02 and 0.007 and have no printed value. HSP-90 loading in L is uneven (relative to WT: 1.11, 0.69, 0.59, 0.51, 0.49, 0.31 for the six non-WT lanes in order), so normalisation matters. The WT WWOX band is clipped (see B2), which would inflate the other lanes' ratios against a linear measure.
- **Fig 1M**

| Lane | Printed | Read-off | Range |
|---|---|---|---|
| WPM S1 | 0.1 | 0.105 | 0.071-0.143 |
| WPM D1 | 0.1 | 0.103 | 0.069-0.140 |
| WPM D3 | 0.3 | 0.36 | 0.245-0.394 |
| WPM S1 AAV9 | 7 | 1.34 | 0.97-1.40 |

  For WPM S1 AAV9 the ratio is 0.19 (read-off about 1.3 against printed 7). The unnormalised read-off is 2.1, which is not 7 either. The WT HSP-90 band in M is itself clipped (minimum grey 1), which cannot by itself explain a fivefold difference. I cannot explain the 7. The most likely reasons are that the printed value is a mean over other repeats or uses a different normalisation (B8), but that is inference, not a finding.

Corrected wording for B1: "Supplementary Fig 1M (week 16 human SCAR12-line organoids, one blot image) prints 1, 0.1, 0.1, 0.3, 7 under JH WT, WPM S1, WPM D1, WPM D3, WPM S1 AAV9. Supplementary Fig 1L (week 16 human WOREE-line organoids, one blot image) prints 1, blank, blank, 0.2, 0.4, 0.4, 0.9 under JH WT, WSM S2, WSM S5, LM-iPS, WSM S2 AAV9, WSM S5 AAV9, LM-iPS AAV9. No held text defines the numbers (reference lane, normaliser, number of repeats)."

## B2. WT band in the Supp Fig 1L blot is saturated: SUPPORTED for the held images, with a qualification
Fig 1L, JH WT lane (human organoids, week 16, one blot image), 46 kDa band:
- **File010 p.2 panel L embedded image.** In the window x 622-686, rows 1922-1944, the darkest grey is 1 of 255. The per-row minimum sits at 1-6 for about 14 consecutive rows (rows 1925-1938). That is a flat floor, not a peak. Within the 3150-pixel window, 121 pixels are at or below 5 and 528 at or below 10. The darkest 5x5 mean is 5.3.
- **File012 p.6 uncropped image of the same blot.** The 46 kDa WT band has a per-row minimum of 24-27 across about 17 consecutive rows. That is also a flat plateau, though not at the floor. The upper band in that WT lane (just above the 50 kDa marker, so a different band) bottoms out at 0 with 22 pixels at or below 10.
- **Contrast control.** In the same figure, the Fig 1K WT 46 kDa band is peaked, not flat (see B6). The rescue bands in L bottom out at 128-146.

Qualification: this shows display saturation in the held JPEGs. The held rendering cannot show whether the original exposure or detector was saturated, how the figure was contrast-adjusted, or what the unclipped WT intensity would be. A clipped WT band in Fig 1L would inflate the other lanes' ratios against WT.
Corrected wording: "In the held images the Fig 1L JH WT 46 kDa band is clipped at the display floor (flat plateau, minimum grey 1 in the supplement figure, about 25 in the uncropped File012 image); the acquisition-level saturation cannot be assessed."

## B3. Figure 1D legend n values: SUPPORTED, with one qualification
Locator: AM_fitz.txt lines 2093-2094, legend of Figure 1, panel D, on AM PDF page 28. Quote: "(D) Quantification of all the cell-attached recordings obtained from WT, WWOX-KO, WOREE and SCAR12 organoids, including those exemplified in (B). (WT: n= 30 neurons; WWOX-KO: n=30; WPM S: n=21; WPM D: n=21; WSM S: n=24; LM-iPS: n=14), collected from one experiment."
- **Numbers.** WT 30, WWOX-KO 30, WPM S 21, WPM D 21, WSM S 24 and LM-iPS 14 are SUPPORTED.
- **"Collected from one experiment".** SUPPORTED.
- **Unit and qualification.** UNDERSHOOT. The unit "neurons" is stated only after the first number. The legend gives no organoid count for panel D. The figure title says "Week 7 organoids" and the species is human iPSC-derived. The legend then says tests were one-way ANOVA with Tukey, so the replicate unit for the tests is the neuron, not the organoid or the line.
- **Legend defect.** The legend points to "(B)" for the exemplified recordings; the raster plots are panel C.
- **Counts.** I did not count the points on the figure.

## B4. The text on 3-fold WOREE vs SCAR12 and similar hyperactivity earlier: SUPPORTED with qualifications (UNDERSHOOT)
Locator: AM_fitz.txt lines 895-907, AM PDF page 12. Quote: "the firing rate of WOREE organoids was approximately 3-fold higher than that of SCAR12 organoids (Fig. 6A(ii) and Supplementary Fig. 9C), in contrast to what we observed in an earlier time point, where both organoids showed similar neuronal hyperactivity [Fig. 1B(i) and Fig. 1C]. In both cases neuronal firing was significantly higher compared to the WT".

Facts:
1. **"About three times at week 16".** SUPPORTED as a statement of the text. The "approximately 3-fold" is in the passage on week 16 organoids infected at week 10 and grown 6 weeks.
2. **Earlier time point both similarly hyperactive.** SUPPORTED. The text says "an earlier time point" and does not name week 7 there. The Figure 1D panel title says "Week 7 organoids", which gives the week by inference.
3. **Citations.** SUPPORTED as quoted, but with issues:
   - Figure 1 as printed (the figure JPEG) has panels A to F and no sub-panel "B(i)". B is immunostaining, C is raster plots, D is the firing rate.
   - Supp Fig 9C is "Representative calcium transient in selected neurons" (File010 p.3 or 4 legend), not a quantification of firing rate.
4. **Not stated in the sentence.** UNDERSHOOT. The sentence does not say which arm the 3-fold compares or which measure. My read-off from the Fig 6A(ii) events-rate bar chart (week 16 organoids, human, bars with SEM, n = 30 vs 40 ROI per the legend) is about 0.075 Hz for SCAR12 AAV9-EGFP and about 0.26 Hz for WOREE AAV9-EGFP, a ratio of about 3.5. That is a chart read-off, not author data. The "3-fold" therefore applies to the events-rate panel and to the AAV9-EGFP arms. The panel also shows the other two measures are not 3-fold: active-ROI percentage is 100% in both arms, and mean amplitude is about 0.061 vs 0.069 ΔF/F0.
5. **Different assays.** The earlier time point (Fig 1) is cell-attached ephys spikes/neuron; the week 16 comparison is Ca2+ imaging events rate. The two are not directly comparable, and the "3-fold vs similar" contrast crosses assays.

Corrected wording: "The text states that WOREE organoids' firing rate was approximately 3-fold that of SCAR12 organoids at week 16 (Ca2+ imaging events rate, AAV9-EGFP arms by chart read-off about 0.26 vs 0.075 Hz, citing Fig 6A(ii) and Supp Fig 9C, which is a representative trace panel), versus similar hyperactivity at an earlier time point (cell-attached recordings, citing 'Fig 1B(i)' and 1C; Figure 1 has no B(i) panel and the firing-rate quantification is Fig 1D)."

## B5. Supp Fig 1K lanes and printed values: SUPPORTED
Locator: File010 p.2 panel K; legend on File010 p.3; File012 p.5.
- **Lanes.** SUPPORTED. There are five sample lanes labelled JH WT, JH WKO-1C, JH WKO-2C, JH WKO-1C AAV9 and JH WKO-2C AAV9. File012 p.5 shows the same five labels, with marker lanes on both sides.
- **Printed values.** SUPPORTED: 1, blank, blank, 0.8, 1.4. The legend states "(K) Immunoblot analysis of JH-WT, JH-WKO and JH-WKO AAV9-hSyn-hWWOX cerebral organoids from week 16, confirming knockout levels of WWOX and its rescue." The species is human (JH-iPS11-derived).

## B6. 46 kDa WT band in panel 1K not clipped, darkest grey about 88: SUPPORTED for "not clipped", but the "88" is from a different image
Fig 1K, JH WT lane (human organoids, week 16, one blot image):
- **File010 p.2 panel K embedded image** (window x 94-143, rows 1940-1959). The darkest grey is 63 of 255. The darkest 5x5 mean is 74.6, the mean of the darkest 200 pixels is 77.6, and the lane-mean row minimum is 74.3. There are no pixels at or below 30. The vertical profile is peaked and rounded (per-row minimum: 127, 105, 81, 68, 64, 63, 65, 74, 92 across rows 1944-1952), not a flat floor. So it is not clipped in the display image. Uncertainty: about ±5 grey levels depending on the pixel-selection rule.
- **File012 p.5 uncropped image of the same blot.** The WT lower-band darkest grey is 88 (per-row minimum 88-92 around the peak). This is the only place I reproduced "about 88". The 88 refers to File012 p.5, not the File010 p.2 embedded panel. Both images are unclipped.
- **Another band in the same blot.** The upper ~50 kDa band in the uncropped K blot is clipped (minimum grey 2 for the WT region; 30 pixels at or below 10). That band is not in the cropped panel K.
- **Corrected wording:** "The JH WT 46 kDa band is not clipped in either held image of Fig 1K (darkest grey 63 in the File010 panel, 88 in the File012 uncropped image, out of 255). The strong ~50 kDa band visible in the uncropped File012 blot, in the WT, KO-1C, KO-2C and 2C AAV9 lanes, is clipped and is outside panel K's crop."

## B7. KO lanes faint signal below 0.2; rescue lanes well below the printed 0.8 and 1.4: SUPPORTED, with an important qualification
Method as above. All values are WWOX/HSP-90 relative to the JH WT lane in the same blot (human organoids, week 16, one blot image, one lane per condition). Format: primary common-background value (range over background variants).

Fig 1K, File010 p.2 embedded panel, sum of both band rows:

| Lane | Read-off (range) | Printed | Ratio read-off/printed |
|---|---|---|---|
| JH WKO-1C | 0.055 (0.016-0.113; per-lane flank 0.061) | blank | n/a |
| JH WKO-2C | 0.113 (0.049-0.187; per-lane flank 0.125) | blank | n/a |
| JH WKO-1C AAV9 | 0.219 (0.174-0.256; per-lane flank 0.242) | 0.8 | 0.27 (0.22-0.32) |
| JH WKO-2C AAV9 | 0.452 (0.368-0.512; per-lane flank 0.467) | 1.4 | 0.32 (0.26-0.37) |

Cross-check on the uncropped File012 p.5 image of the same blot (lower resolution; the lane windows and the signal window of rows 64-108 are my choice; background variants):
- WKO-1C 0.062 (0.029-0.101)
- WKO-2C 0.133 (0.079-0.185)
- WKO-1C AAV9 0.325 (0.283-0.355), 0.41 of the printed 0.8 (0.35-0.44)
- WKO-2C AAV9 0.578 (0.511-0.622), 0.41 of the printed 1.4 (0.37-0.44)

Other supporting numbers:
- **Unnormalised total WWOX (panel), vs WT:** WKO-1C 0.052, WKO-2C 0.081, WKO-1C AAV9 0.245, WKO-2C AAV9 0.348. HSP-90 relative to WT: 0.94, 0.72, 1.12 and 0.77, and the WT HSP-90 is not clipped (minimum grey 38).
- **Lower row only (the 46 kDa position, per-lane flank variant):** KO lanes 0.043 and 0.080, rescue lanes 0.057 and 0.162.
- **Upper row only (the ~48 kDa band):** KO lanes 0.023 and 0.055, rescue lanes 0.204 and 0.341. The upper row therefore carries most of the rescue signal.

Facts:
1. **KO lanes carry a faint signal at the 46 kDa position.** SUPPORTED. A shallow dip (about 8-11 grey levels below background) is visible in both KO lanes at the lower row.
2. **Below 0.2 of WT after HSP-90 normalisation.** SUPPORTED, but near the edge for WKO-2C: all variants give at most 0.187 (panel) and 0.185 (uncropped).
3. **Both rescue lanes read well below 0.8 and 1.4 when both band rows are summed.** SUPPORTED. The read-off is about 0.17-0.26 and 0.37-0.51 in the panel, and 0.28-0.36 and 0.51-0.62 in the uncropped image, against the printed 0.8 and 1.4.

Qualifications and limits:
- The printed values are not defined anywhere I could find (see B8). They may be means over other repeats, may use a different reference or normaliser, or may be computed on the original unprocessed image. I cannot tell which. The discrepancy is a difference between a JPEG read-off and a printed number, not evidence that the printed number is wrong.
- "Summing both band rows" counts the upper ~48 kDa band as WWOX signal. The legend says both the lower 46 kDa band and the upper ~48 kDa band are specific WWOX bands, but the AAV9 construct is the human transgene and its mobility is not stated for K.
Corrected wording: "From the embedded JPEG of Fig 1K (week 16 human organoids, one blot image), my read-off of WWOX/HSP-90 against the JH WT lane, summing both band rows, is about 0.05-0.11 for the two KO lanes (up to 0.19 depending on background), and about 0.22 (0.17-0.26) and 0.45 (0.37-0.51) for WKO-1C AAV9 and WKO-2C AAV9, against printed 0.8 and 1.4. A uncropped-image cross-check gives about 0.33 and 0.58. These are JPEG read-offs, not author data."

## B8. Methods on immunoblot quantification: UNDERSHOOT as to source, and read carefully
- **Wrong source file in the brief.** The sentence is not in the AM main text. The AM says only "A detailed Materials and methods section is provided in the Supplementary material" (AM line 266, PDF page 4). The text is in the Supplementary Methods, File009 page 7, "Immunoblot analysis" paragraph (File009.txt lines 212-213). Quote: "Blots were repeated and quantified 2–3 times per experiment in Bio-Rad's Image Lab software. Representative images of those repeated experiments are shown."
- **2-3 repeats quantified.** SUPPORTED as quoted, but the phrase is "2–3 times per experiment". The text does not say that the number printed under each lane is the mean of those repeats. That is not stated anywhere I could find.
- **Representative images shown.** SUPPORTED.
- **What the printed values are.** I found no sentence or legend in any held file (File009, File010, File011, File012, AM) that defines the numbers under the lanes: no mention of normalisation, reference lane, spread or n. File010's Supp Fig 1 legend does not mention them. "HSP-90 normalisation" in B7 and in my numbers is my own assumption.
- **Corrected wording:** "Supplementary Methods (File009 p.7) say blots were repeated and quantified 2–3 times per experiment in Bio-Rad Image Lab and representative images are shown. They do not say that the numbers printed under the lanes of Supp Fig 1K-M are means of those repeats, nor how they are normalised."

## Counts
- B1 SUPPORTED (3 facts) + UNDERSHOOT (1 fact)
- B2 SUPPORTED (1 fact, with a qualification on acquisition-level saturation)
- B3 SUPPORTED (2 facts) + UNDERSHOOT (1 fact)
- B4 SUPPORTED (3 facts) + UNDERSHOOT (2 facts)
- B5 SUPPORTED (2 facts)
- B6 SUPPORTED for "not clipped"; the "88" is reproduced only in File012 p.5, and the File010 p.2 image gives 63
- B7 SUPPORTED (3 facts), with the qualification above
- B8 SUPPORTED for the wording, wrong source file in the brief, and the point that the printed numbers are undefined (UNDERSHOOT as stated)
- OVERSHOOT 0, WRONG 0, UNVERIFIABLE 0 as such. The one thing I could not determine is the origin of the printed values (see B7 and B8).

## Not opened
- READING_NOTE*, FULLTEXT_READ_RECEIPT*, any *_derived.txt, and every path under disease-models/, ledger/ and other repository folders were not opened.
- `PMID42397075_Aqeilan2026_assets/` was listed but its contents were not read.
- File008 was read only for its first lines (author contributions); File011 (tools and reagents list) was read only for one grep hit.

Files written (all in /home/desktop/.claude/jobs/6739e4ff/tmp/b2/out3): densitometry.py, densitometry2.py, densitometry_uncropped_K.py, loadimg.py, densitometry_output.txt, the raw10/ and raw12/ extracted images, and the img/ crops and overlays.
