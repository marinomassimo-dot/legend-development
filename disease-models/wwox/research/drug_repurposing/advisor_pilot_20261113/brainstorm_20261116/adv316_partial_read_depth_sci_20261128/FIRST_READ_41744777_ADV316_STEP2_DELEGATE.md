# ADV-316 step 2, first reader, PMID 41744777: delegate report, verbatim (2026-11-28)

Delegate: legend-delegate, sonnet 5.5, effort HIGH stated in the dispatch. Figures: five JPEGs from the PMC open-data bucket (PMC12938943.1), held at files/figures/PMID41744777/. Sentences: SENTENCES_CURATED_STEP2_41744777.txt (C01 to C05). Not edited by SCI; SCI's checks are in the RESULT file.

FIRST READ, Nabakowski 2026, Cells 15(4):334, PMID 41744777. Hypothesis level, not medical advice. I read the whole JATS text and opened all five figures as images, with zoomed crops of Figs 1B, 3B, 4A, 4D, 4E and 5A. The only table in the XML is the abbreviations list, so there is no data table. I read no other repository file and nothing from outside the files named in the dispatch.

**Design (text, Methods 2.1, 2.3-2.6, Fig 3 and 4 legends)**
- Mice: 8-week-old female C57BL/6, single intravenous (tail vein) dose of 1e11 vg/animal, one dose level only.
- Vector: ssAAV-CBA-Fluc in AAV9, AAV9-16, AAV9-HR or AAV9-DM, 9 weeks.
- Imaging n = 5 per group (Fig 3 legend). Tissue vg and RT-qPCR n = 3-5.
- Statistics: Kruskal-Wallis with Dunn, mean ± SEM.
- Readouts: IVIS imaging, vg/µg DNA, Fluc RNA relative to Taf9b (2^-ΔΔCt).
- "AAV9-DM" is defined as five point mutations (501, 505, 527, 533, 706). The paper never expands "DM".

**Verdicts**

| Clause | Verdict | Basis and locator |
|---|---|---|
| C01 "~127-fold" liver de-targeting | SUPPORTED | Text, Results 3.4: "AAV9-DM resulted in a ~127 fold reduction in vector genome copies as compared to AAV9". Also in the Highlights. Fig 4A by eye: AAV9 bar ~1.1e8, DM bar ~9e5, ratio ~125-130. The paper does not say whether 127 is a ratio of means or of medians. |
| C01 "eight-fold worse packaging" | SUPPORTED | Text, 3.2: "3.58 × 10^13 vector genomes" for AAV9 and "AAV9-DM, which yielded 4.5 × 10^12 vgs". Fig 1B printed label is 4.53e12. |
| C01 "fewer brain vector genomes" | SUPPORTED | Fig 4D (figure): bracket "*" for AAV9 vs DM. Discussion: "In the brain, all mutated capsids resulted in significantly lower vector genome copies as compared to AAV9". The Results text (3.4) only says DM was "reduced to a lesser degree" and gives no p value. |
| C02 "WWOX appears zero times" | NOT ADDRESSED | Claim about the paper's text. I counted 0 "WWOX" in the XML. |
| C02 label "double-mutant" | UNSUPPORTED | The paper says only "AAV9-DM" and "five point mutations", never "double mutant". It is the AAV9-16 triple combined with the AAV9-HR pair. |
| C02 hepatic vg ~127-fold | SUPPORTED | As C01. |
| C02 3.58e13 vs 4.5e12, ratio 7.96 | SUPPORTED | Text 3.2. My recompute 7.956. With the Fig 1B label 4.53e12 it is 7.90. |
| C02 "peak whole-animal signal 7.3e7 to 5.8e5, factor 126" | SUPPORTED as printed in the text, with caveats (see below) | Text, 3.3: "AAV9 ... peak AR of 7.3 × 10^7 ... AAV9-DM ... peak AR of 5.8 × 10^5". My recompute 125.9. |
| C02 "by the paper's own Discussion, significantly fewer brain vg" | SUPPORTED | Discussion, para 5, quote under C01. |
| C02 "no toxicity endpoint of any kind" | SUPPORTED by absence in the text and in the figures | Methods list only imaging, qPCR and RT-qPCR. I found 0 hits for body weight, histology, transaminase or any immune assay. "Toxic" appears only as background (Abstract, Intro, Discussion). |
| C02 "dose-ceiling implication is a mechanism hypothesis" | NOT ADDRESSED | The paper has one dose (1e11 vg/animal) and no dose-response. Its own implication is in the Highlights: "AAV9-DM may allow for the use of lower doses ... resulting in reduced immune responses". Nothing was measured on this. |
| C03 "two underlying values exist only in a panel" | SUPPORTED | The text prints no liver vg/µg values. They appear only in Fig 4A, read by eye. |
| C03 packaging, 7.96, 126, brain | As C02 | Same loci. |
| C04 no toxicity endpoint | SUPPORTED | As C02. "Dose-ceiling = mechanism hypothesis" is the repository's gloss, not the paper's. |
| C05 "route reaches primate brain at 1-4 vg/DG, sublinear" | NOT THIS PAPER | Mouse only. No primate, no "DG" or dentate gyrus, no scaling analysis. Primates appear only as citations to other work ("murine and non-human primate models", ref 28; "rats and non-human primates", refs 58-61). |
| C05 "costs ~8-fold packaging" | SUPPORTED | As C01. |
| C05 "and brain exposure" | SUPPORTED in direction; FALSE if read as ~8-fold in brain | Fig 4D by eye: AAV9 ~4.5e7, DM ~7e5, ~60-fold lower (significant, "*"). The clause's grammar ("~8-fold packaging and brain exposure") can be read as an 8-fold brain cost, which would be wrong. |

**Numbers I carry**

All are mouse data. Replicate unit is one animal unless stated.

- **Fig 1B packaging yield:** one bar per capsid, no error bar and no replicate shown, so effectively one production, per 1.6e9 HEK293 cells (text 3.2).
  - AAV9 3.58e13, AAV9-16 2.06e13, AAV9-HR 2.32e13, AAV9-DM 4.53e12.
  - Ratios to AAV9: 1.74, 1.54 and 7.90 (printed labels), or 7.96 using the text's 4.5e12.
- **Fig 4A liver vg/µg DNA, n = 4-5 dots per arm, read by eye from bars:**
  - AAV9 ~1.1e8, 16 ~1.1e7, HR ~3.8e6, DM ~9e5.
  - AAV9/DM ~125-130, which matches the printed 127.
- **Fig 4D brain vg/µg DNA, by eye, n = 5 AAV9, 4 AAV9-16, 5 HR, ~5 DM:**
  - AAV9 ~4.5e7, 16 ~1.3e6, HR ~2.7e5, DM ~7e5.
  - AAV9/DM ~62.
  - The brain-to-liver ratio rises from ~0.4 (AAV9) to ~0.8 (DM), so the brain falls less than the liver does.
- **Fig 4B heart, by eye:**
  - AAV9 ~1.3e8 vs DM ~7e5, ~180-fold lower, "**".
  - So the heart is de-targeted at least as much as the liver. The authors say "reduced heart tropism".
- **Fig 4C gastrocnemius, n = 3, no bracket:**
  - AAV9 ~7e6, DM ~3e5 (~20-fold lower by eye).
  - AAV9-16 and AAV9-HR were below detection.
  - The text calls the DM level "consistent with" AAV9.
- **Fig 4E spinal cord, by eye:**
  - AAV9 ~1.6e7, DM ~6e5, ~27-fold lower.
  - Only the HR comparison is flagged significant, so the text says "equivalent".
- **Fig 3 imaging (IVIS), liver, n = 5 per group:**
  - Fig 3A weeks 3, 4, 5, 6, 7, 9, all pairs AAV9 vs DM marked "**".
  - Fig 3B group means, by eye: AAV9 week 3 ~1.6e7 (highest single point ~2.5e7), DM week 3 ~1.0e5 (highest single point ~2.2e5).
  - Mean ratio at week 3 ~155, and ~150-200 at other weeks.
- **Fig 5A liver Fluc RNA relative to Taf9b, 2^-ΔΔCt, AAV9 n = 3 and others 5:**
  - DM bar ~2^-4.8, about 1/28 of AAV9 (by eye, log2 axis).
  - The liver RNA drop is therefore ~28-fold, not 127.
- **Fig 5D brain Fluc RNA:** all arms are "equivalent" (text). By eye DM is ~0.5x AAV9, with no significance bracket at n = 5.
- **Fig 5B heart:** DM is "*" (reduced).
- **Fig 5C gastrocnemius:** HR is "**" (increased).
- **Fig 5E spinal cord:** no significant bracket.

**Caveat on the 7.3e7 and 5.8e5 "peak AR" values (C02, C03)**

The ratio 125.9 is correct arithmetic, but the values do not match anything plotted.
- Fig 3A and 3B (liver ROI, n = 5) show means and individual points of at most ~2.5e7 for AAV9 and ~2.2e5 for DM.
- The text values 7.3e7 and 5.8e5 are 3-4x and ~2.6x above the highest single plotted points.
- The paper does not say whether "peak" is a mean or a maximum, which ROI it uses, or which week.
- The Fig 2 colour-bar maxima (6.0e7 for AAV9, 4.5e5 for DM) are display ranges, not data.
- The text says AR was taken "from the ventral side of the animal" (3.3). Fig 3 plots "liver". "Whole-animal" in C02 is therefore not clearly the plotted quantity.
- The AAV9-16 and AAV9-HR text peaks (6.6e6, 3.5e6) are ~6-11x above their plotted means (~6e5, by eye).
- My recompute from Fig 3 means is ~155, not 126. Treat 126 as text-stated, not figure-verified.

**What the figures show that no sentence mentions but that bears on them**
- **Brain:** the paper's own conclusion is "minimally affecting CNS tropism" and "AAV9-DM may be more appropriate for targeting the CNS with minimal off-target transduction" (Discussion). "Fewer brain vg" is true but is not the authors' framing. Brain vg falls ~60-fold vs ~127-fold in liver, a ~2-fold gain in brain-to-liver ratio by eye. Brain RNA is not significantly different (Fig 5D). Brain vg and brain RNA disagree, which the authors attribute to a possible capsid effect on transcription.
- **Expression over time (Fig 3B):** AAV9-DM expression falls significantly at weeks 6 and 9 vs week 3. By eye it drops from ~1.0e5 to ~2e4, about 5-fold. AAV9 also falls (week 9 vs 3, "*"). This bears on "durable".
- **Packaging:** Fig 1B has one bar per capsid. There is no replicate or batch variability, so "~8-fold" is a single-production figure.
- **Toxicity, immune and body-weight readouts:** none anywhere. The liver and immune benefits are asserted in the Highlights and Discussion but not measured. Only one dose, one sex, one strain and one transgene (Fluc) were tested.
- **Statistics:** Kruskal-Wallis with Dunn on n = 3-5 has very low power. "Equivalent" in the text means "not significant", not shown to be equal. Examples are the gastrocnemius (~20-fold lower) and spinal cord (~27-fold lower) DM vs AAV9 differences by eye.
- **Strain naming:** the text says "C57BL6/J" in 3.3 and "C57BL/6" in Methods.

**What I could not read or do**
- No values are printed for any panel, so every figure value above is read by eye from bars, using axis ticks on 729-755 px wide JPEGs.
- Individual dots overlap in places, so n per arm is approximate where I wrote "~".
- I could not find the source of the 7.3e7 and 5.8e5 peak values in any panel.
- The 3.3 text says AR was evaluated "from the ventral side", but Fig 3 is labelled liver. I did not resolve this.
- I did not open the framework files (delegation_budget.md §2 and §7), because the dispatch limited me to the listed files. Nothing was written to the repository. Scratch crops are in /tmp/f316, outside the repository.
