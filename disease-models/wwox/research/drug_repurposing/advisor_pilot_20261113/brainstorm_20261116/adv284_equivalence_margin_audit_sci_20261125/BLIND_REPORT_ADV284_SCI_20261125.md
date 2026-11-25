# Blind report ADV-284 (sonnet, effort high), 2026-11-25
Hypothesis-level reading of held files; not medical advice.

## 1. VERDICT: ADD
Every factual clause I could check is reproducible from the held source; nothing is false. But the sentence says "not significant against wild type" without the one thing a reader needs to weigh it: the held source gives no margin, the n are few and mismatched with the plotted points, and the smallest detectable difference is about as large as the disease effect. Read as sameness/restoration it says more than the data can bear.

Clause checks (file, page, panel):
- "SOX2+MYC+ about 72 (KO) to about 50 with A51": measured from pixels in Supp Fig 7F (File010.pdf p.12, SOX2+MYC+ panel, rendered 600 dpi): KO bar 73.5 (bar top), mean of plotted points 73.0; KO+A51 bar ~52, point mean 51.2. WT NT bar 48.7, WT DMSO 46 (point mean 45.5). "About 72/50" is within ~1-2 points; fine (73 and 51 would be closer).
- "SOX2+ about 60 to about 33, same pattern": SOX2+ panel: KO bar ~60 (point mean 59.9), KO+A51 ~33.5 (point mean 33.1); WT NT ~27, WT DMSO ~28.5. Brackets: ** KO vs KO+A51; ns KO+A51 vs WT NT and vs WT DMSO. Same pattern, yes.
- "significant against the untreated KO and not significant against WT": SOX2+MYC+ panel brackets: ** KO vs KO+A51; ns WT NT vs KO+A51 (outer bracket); ns WT DMSO vs KO+A51. True. (Same bracket reading in SOX2+.)
- The paper text quote: AM_fitz.txt lines 770-771 "We observed a marked reduction in both progenitor populations, confirming successful MYC inhibition". True.
- "No treated-wild-type arm": panels show WT NT, WT DMSO (vehicle), KO, KO+A51 only. True. Also true and not stated: there is no KO vehicle (DMSO) arm; the Methods say "A51 drug or DMSO" (File009.txt "MYC inhibition") but no KO+DMSO arm is plotted or listed in the legend n.
- "no dose-response": one dose, 125 nM, week 8 to 15 (AM_fitz.txt lines 764-765; File009.txt MYC inhibition). True.
- "no randomisation or blinding": AM_fitz.txt Statistical analysis, "No randomization or blinding was applied in this study." True.
- "one of three experiments the paper excludes from independent differentiations": AM_fitz.txt lines 298-300: "Experiments were performed in independent differentiations, except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq"; Supp Fig 7 legend: "biological and technical replicates from one experiment". True.
- "suppresses two pathways": AM_fitz.txt lines 758-760 "multi-kinase inhibitor (A51) established to suppress Wnt and MYC expression". True.
- Not stated in the sentence and needed: n per arm; the unit; the denominator of the percentage (y axis "Percentage of cells(%)", panel title "count"; denominator not defined in the held methods, only "QuPath v0.5.1" quantification); that the KO-versus-WT disease contrast in this panel is itself only P<=0.05 (one star, WT NT vs KO), so the assay has little room to show treated = WT.

## 2. EQUIVALENCE CLASS: DERIVABLE (bounded, not a point value)
- No margin: searched (2026-11-25) the words power, sample size, equivalen*, non-inferior*, confidence interval, TOST, margin, SEM, SD in File008/009/010/011/012 .txt and AM_fitz.txt. Only hits that matter: "mean +/- SEM" (Supp Fig 7 legend, File010.txt; AM_fitz.txt line 316). No pre-specified smallest difference, no equivalence test, no CI of a difference, no power calculation. Searched "random|blind|mask" in File009.txt (only "blind patch-clamp", unrelated) and AM_fitz.txt (line 322 "No randomization or blinding...").
- n and unit: Supp Fig 7 legend (File010.pdf p.13) gives n = organoids: "WT NT: n=4 organoids, WT DMSO: n=4, WiBR3 WKO-1B: n=6; WiBR3 WKO-1B: n=7" (the last two carry the same label; I read them as KO = 6 and KO+A51 = 7 in plotted order). Spread: SEM bars plus every point legible in the image. So an SDD can be computed, but the plotted unit is not the organoid (section 4), so I give a bracket: point-level SD with plotted points as n (anti-conservative, pseudoreplicated) and with legend organoid n (conservative, because point SD includes within-organoid variance).

## 3. SDD (two-sided alpha 0.05, power 0.80, equal variance)
Formula: SDD = (t(0.975,df) + t(0.80,df)) x sp x sqrt(1/n1 + 1/n2), df = n1+n2-2, sp = pooled SD of the two arms.
Spread: measured from pixels, not by eye. Page 12 rendered with pdftoppm at 600 dpi (embedded image 1887x2048 px, jpeg, 213 ppi), black dots found by thresholding plus morphological opening and connected components, y axis calibrated from tick marks (0 at row 973, 100 at 564.5, 150 at 362 in the crop). Touching dot pairs split into two (checked at 8x zoom). Reconstructed point means agree with the plotted bar heights within ~1.5, which supports the reading. Scripts: /home/desktop/.claude/jobs/ae0002e7/tmp/adv284/blind/ (count_pts.py, panel.py, sdd.py, sddcalc.py). t values computed numerically (df 19: 2.093, df 9: 2.262, checked).

SOX2+MYC+ panel, point values (percent), measured:
- WT NT: 6 points, mean 48.7, SD 8.4 (38,46,46,48,52,63)
- WT DMSO: 11 points, mean 45.5, SD 18.9
- KO: 24 points, mean 73.0, SD 18.3
- KO+A51: 15 points, mean 51.2, SD 18.8
Disease effect (KO minus WT): vs WT NT 24.3; vs WT DMSO 27.5; vs pooled WT (17 points, mean 46.6) 26.4.

| Reference WT | n1 / n2 (unit) | df | t.975 + t.80 | sp | SDD | SDD / disease effect |
|---|---|---|---|---|---|---|
| pooled WT | 17 / 15 (plotted points) | 30 | 2.042+0.854 | 17.2 | 17.7 | 67% of 26.4 |
| WT NT | 6 / 15 (points) | 19 | 2.093+0.861 | 16.7 | 23.8 | 98% of 24.3 |
| WT DMSO | 11 / 15 (points) | 24 | 2.064+0.857 | 18.8 | 21.8 | 79% of 27.5 |
| WT NT | 4 / 7 (legend organoids) | 9 | 2.262+0.883 | 16.1 | 31.7 | 130% of 24.3 |
| pooled WT | 8 / 7 (legend organoids) | 13 | (df 13) | 17.2 | 27.0 | 102% of 26.4 |

Observed treated minus WT: +2.5 (WT NT), +5.7 (WT DMSO), +4.6 (pooled).
SOX2+ panel (same method): disease effect 32-33; SDD 18.4 (pooled WT, points) to 40.6 (legend n); 57% to 123% of the effect.
Even the most favourable row (pooled WT, plotted points as n, which inflates n) has an SDD at 67% of the disease effect; the others are 79% to 135%. All are above the half-of-effect threshold, so the sentence read as sameness or restoration claims more than the data can bear. For calibration, the KO versus WT contrast with the same machinery has SDD 22.5 (vs WT NT) against an effect of 24.3: the panel barely resolves the disease effect itself (one star).

## 4. Plotted points versus n
SOX2+MYC+ panel plotted points: WT NT 6, WT DMSO 11, KO 24, KO+A51 15 (total 56). SOX2+ panel: 7, 9-10, 10, 15. Legend n (organoids): 4, 4, 6, 7 (total 21). Every arm has more points than organoids (ratios 1.5, 2.8, 4.0, 2.1), and the point counts for KO differ between the two panels of the same sections (24 vs 10), unexplained. The plotted unit is therefore probably an image field or section (or other technical replicate; the legend says "biological and technical replicates"), several per organoid. If the one-way ANOVA with Tukey ran on the plotted points, its unit (n ~56) is not the independent unit (organoid, and all from one experiment, one differentiation); if on organoid means, n is 4/4/6/7. The source does not say which. Missing for a reader: which unit entered the ANOVA; points per organoid; the denominator of "percentage of cells"; a KO vehicle arm; the label of the duplicated "WiBR3 WKO-1B" n; any margin or power.

## 5. Corrected sentence
> Treated knockout organoids: SOX2+MYC+ about 73 percent (knockout) to about 51 with A51, significant against the untreated knockout (**) and not significant against wild type (WT NT about 49, WT DMSO about 46; Supplementary Fig. 7F, Tukey), but this is a non-significant P, not equivalence: the paper gives no margin, power calculation or interval; legend n is 4, 4, 6, 7 organoids from one experiment while 6, 11, 24, 15 points are plotted (unit and ANOVA unit unstated); from the plotted spread the smallest detectable difference from wild type is about 18 to 32 percentage points against a knockout-minus-wild-type effect of about 24 to 27, so sameness or restoration is not supported. SOX2+ about 60 to about 33, same pattern. No treated wild-type arm, no knockout vehicle arm, one dose (125 nM), no randomisation or blinding, one of the three experiments the paper excludes from independent differentiations. The compound suppresses two pathways (Wnt and MYC): causal attribution to MYC inherits the ambiguity. (The paper's text: 'a marked reduction in both progenitor populations'.)

## Files opened
- /home/desktop/.claude/jobs/ae0002e7/tmp/adv284/BLIND_SENTENCES_ADV284_SCI_20261125.md (read)
- .../PMID42397075_Steinberg2026_OUP-Supplement/brain-2025-03809-File010.pdf (pages 12-13: pdftotext, pdfimages -list, pdftoppm renders at 300 and 600 dpi)
- .../brain-2025-03809-File009.txt (read relevant parts: MYC inhibition, immunofluorescence; grepped)
- .../brain-2025-03809-File008.txt, File010.txt, File011.txt, File012.txt (word search only)
- .../PMID42397075_Steinberg2026_OUP-AM_fitz.txt (read the Statistical analysis and MYC inhibition Results paragraphs; grepped)
- Directory listing of the Supplement folder (names only; I did not open READING_NOTE, receipt, zip or the figures-page PNGs). AM.pdf and File*.pdf other than File010 not opened.
