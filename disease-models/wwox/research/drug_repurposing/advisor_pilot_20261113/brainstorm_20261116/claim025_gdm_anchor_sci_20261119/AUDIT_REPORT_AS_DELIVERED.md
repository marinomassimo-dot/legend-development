# Baryla 2021 blind locator audit report AS DELIVERED (verbatim; SCI did not edit it)

Delegate: legend-delegate, requested sonnet / high, blind (it received claims, quotes and held-source names only; no dossier, no producer, no verdicts). Read-back and SCI's use of it: the SCI note in this folder. Hypothesis level; no dose; not medical advice.

---

BLIND AUDIT: Baryla 2021 (PeerJ 9:e10604, PMID 33520443), triples T1–T14. Reference genotype class only, hypothesis level, not medical advice.

SOURCES OPENED
- Main XML: PMID33520443_Baryla2021_PMC7811782_refetched_20261119.xml. I read it as text and ran my own searches on it.
- Figure images: peerj-09-10604-g001, g002, g003, g004, g005 and g006.jpg, all in /home/desktop/legend-development/files/figures/PMID33520443/. g007 is a schematic model; I did not open it.
- Supplement: peerj-09-10604-s001.docx (Table S1, read as XML text).
- I opened no other repository file.

Verbatim check: all six supplied quotes are present verbatim in the XML text. Two differences are cosmetic. The T4 quote has spaces around the slash ("WWOX / HIF1A"), and the source reads "WWOX/HIF1A". The T1 sentence continues "and studied at the Outpatient Diabetological Clinic in Lodz, Poland".

BLOCK A: GDM vs NGT comparison (Fig 2)

| T | Label | Locator and statistic | What the proposition adds or leaves out |
|---|---|---|---|
| T1 | SUPPORTED | Methods, Study participants (quote verbatim). Abstract: "135 pregnant women with (n = 98) or without (n = 37) GDM". Trimester sentence: "the first during the third trimester of pregnancy (at 24–28 weeks' gestation or later if it was not possible during this period)". Tissue: Methods, Leukocytes separation: whole-blood pellet after red-cell lysis; "leukocytes" is a mixed population, with no subset analysis. | Leaves out: Caucasian, Polish single clinic, untreated GDM at sampling. GDM women were older (Table 2, 31.0 vs 29.0 y, p = 0.02). NGT and GDM were not matched. The "third trimester" wording is the authors'; the window begins at 24 weeks. |
| T2 | SUPPORTED | Results, Gene expression: "a 3.8-fold increase for HIF1A in the diabetic patients". The p value is printed in the same paragraph: HIF1A "all p < 0.0001". Fig 2B shows *** (opened). | The fold-change method (median or mean) is not stated in Methods. Fig 2 boxplot medians are roughly consistent with medians (HIF1A about 0.9 vs about 0.25; my eyeball read). |
| T3 | PARTLY | Quote verbatim: "There was also a tendency for lower leukocyte WWOX expression…(p = 0.0406)"; "an 1.4- fold decrease for WWOX". Fig 2A shows a single * (opened), consistent with 0.0406. The word "tendency" occurs once in the whole article. | "About 0.04" is right (exact printed value 0.0406, Mann–Whitney, uncorrected). The authors call it a "tendency", although their own threshold is p < 0.05 and Fig 2A marks it significant. The Abstract says "a significant downregulation of WWOX", a stronger word than the Results. The Discussion says "WWOX expression was downregulated", and the Conclusions say "WWOX downregulation". The proposition reproduces the Results wording faithfully. It is PARTLY only because the source itself is inconsistent on the label. |
| T4 | SUPPORTED | Results: "the WWOX/HIF1A index was decreased by approximately 6.5-fold (p <0.0001)". Fig 2L shows *** (opened). The Abstract says "approximately six times reduction". | Ratio-of-medians versus median-of-ratios is not stated. Fig 2L is on a 0–300 scale and is highly skewed (NGT outliers up to about 300), so I could not read the medians from the image. |
| T5 | SUPPORTED (absence confirmed) | Search term set 1 on the full XML (no hits): Bonferroni, Benjamini, Hochberg, Holm (only a surname hit), false discovery, FDR, q-value, multiple comparison, multiple testing, correct, corrected, adjust, family-wise, Tukey. Set 2 (no hits): post hoc, post-hoc, sample size. "multipl" occurs only in "multiply correlation plot" (Figs 4 and 5 captions). "false" occurs only in a HbA1c erythrocyte sentence. "power" occurs once, in the Conclusions: larger studies "with more statistical power". Statistical analysis: Mann–Whitney U, Wilcoxon, Spearman, "p-value <0.05 was considered as significant"; nothing else. Gene count: Methods lists WWOX, HIF1A, NFKB1, SLC2A1, SLC2A4, HK2, PKM2, PFK, LDHA, DVL2, CTNNB1 = 11. The Results say "the 11 individual genes". Fig 2 panels A–K are those 11 genes and panel L is the WWOX/HIF1A ratio, so 12 comparisons. The 3 reference genes (RPLP0, RPS17, H3F3A) are normalizers, not compared. | Eleven is right for genes; the ratio makes 12 tests. The postpartum WWOX comparisons (Fig 3) and about 66 gene pairs per group (Figs 4 and 5), plus the clinical correlations, are also uncorrected. My arithmetic, not the paper's: a Bonferroni threshold across 11 genes would be about 0.0045, and WWOX p = 0.0406 and SLC2A4 p = 0.0134 would not meet it, while HIF1A, PFK, PKM2, DVL2, NFKB1, SLC2A1 (0.0004), LDHA (0.0015) and CTNNB1 (0.002) would. |
| T6 | NOT SUPPORTED as a source statement (numerically compatible only) | Results: "As HIF1A and WWOX displayed opposing patterns of expression… we employed the WWOX/HIF1A expression ratio as an indicator… it appears to be a better indicator… than each of these two genes separately, as evidenced by an 1.4- fold decrease for WWOX and a 3.8-fold increase for HIF1A". Abstract: "significant downregulation of WWOX with simultaneous upregulation of HIF1A which resulted in approximately six times reduction in WWOX/HIF1A ratio". The paper never apportions the ratio change between the two genes. It attributes the ratio to both and presents it as a better combined indicator. | Compatible numerically (my arithmetic: ln 3.8 = 1.34 against ln 1.4 = 0.34, so the HIF1A change is the larger contributor). Fig 4 and Fig 5, figure only, give ratio–HIF1A R = −0.79 (***) and ratio–WWOX R = 0.61 (GDM) and 0.65 (NGT). The authors do not discuss this. The paper does not say "rather than WWOX". |
| T7 | SUPPORTED | Quote verbatim, with "(p > 0.05)". Fig 2E shows NS. The Discussion repeats it: "no significant change was found in leukocyte HK2 gene expression". | The Abstract contradicts the Results: "HIF1A induced genes (SLC2A1, HK2, PFK, PKM) were found to be overexpressed in GDM". HK2 was not overexpressed per the Results and Fig 2E. |

BLOCK B: correlations, postpartum, metabolic parameters

| T | Label | Locator and statistic | Notes |
|---|---|---|---|
| T8 | SUPPORTED (figure only) | Fig 4 (opened), GDM: WWOX–HIF1A −0.05; WWOX–HK2 −0.07; WWOX–PKM2 −0.06; WWOX–SLC2A1 0.04, none with asterisks. The Results text lists only significant pairs and gives no WWOX–HIF1A value. | The text does not state the null correlations. They are inferable only from absence in the text plus the figure. For contrast, WWOX–PFK is significant (figure −0.22 *, text −0.23). In NGT (Fig 5) WWOX–HIF1A is −0.12, also null. The Discussion says "We also showed a linkage of WWOX to HIF1α at their transcriptional levels" in GDM leukocytes. That linkage is via the ratio, not a direct correlation. |
| T9 | SUPPORTED | Text: "weak positive associations of PFK, LDHA, and CTNNB1 were found for WWOX transcript (R = 0.30, R = 0.32, and R = 0.30, respectively; all p < 0.05)". Fig 5 agrees (PFK 0.3 *, LDHA 0.32 *, CTNNB1 0.3 *). | Both text and figure. "Weak" is the authors' word. n = 37, uncorrected. |
| T10 | SUPPORTED | NGT, Results: "insulin and HOMA-IR index positively associated with WWOX expression (R = 0.52 and R = 0.53, respectively; p = 0.001 for both)". Ratio: −0.47 and −0.44. QUICKI-IS vs WWOX: −0.52. Table S1 (opened) agrees. GDM: Results say "only HbA1C correlated significantly…" with HIF1A, HK2, PFK, SLC2A1 and LDHA. Table S1 gives WWOX = NS and ratio = NS for HbA1c. Discussion: "neither WWOX expression nor the WWOX/HIF1A ratio correlated with metabolic phenotypes of diabetic patients". | Table S1 shows only the HbA1c row for GDM; the "no other parameter" part rests on the sentence "only HbA1C correlated" and the Discussion sentence. Fig 6 shows no panel for WWOX. Postpartum: "no correlation… (data not shown)". Causality is not claimed. |
| T11 | SUPPORTED | Results: "a 2-fold increase in leukocyte WWOX gene expression compared to the same women… (p < 0.05)". Fig 3 (opened) shows * for A1 vs B and * for A2 vs C. Medians read by eye: about 0.9 vs 1.7 (B) and about 0.95 vs 2.0 (C). Fig 1: A1 and B n = 8; A2 and C n = 12. | Exact p values are not given (only p < 0.05, two-sided Wilcoxon). The authors flag the small n. Fig 3 also shows B vs GDM * and C vs GDM ** (unpaired), which the text does not report. Postpartum values were comparable to NGT (NS). No NGT-vs-GDM bracket in Fig 3. |
| T12 | PARTLY | The ratio–HIF1A correlation (R = −0.79, ***) is in Fig 4 only (opened); it is not in the text. It is strongly negative, and the proposition gives no direction. Ratio vs glycolytic genes in GDM, text: SLC2A1 −0.31 (p = 0.01), HK2 −0.41, PFK −0.45, PKM2 −0.42 (all p < 0.001). Fig 4 gives the same values; LDHA −0.1 NS. HIF1A–HK2 0.48, PFK 0.40, PKM2 0.51, SLC2A1 0.45 (text) or 0.44 (figure). | "Strongly" fits HIF1A (−0.79) but is stronger than "moderate" for the glycolytic genes (−0.31 to −0.45). The authors never note that HIF1A is the denominator. I searched "denominator", "mathemat", "coupl" and found nothing. The Discussion says "Such correlation was stronger with WWOX/HIF1A suggesting that WWOX modulates HIF1A function". The same −0.79 appears in NGT (Fig 5), where the ratio does not correlate with the glycolytic genes (SLC2A1 −0.13, HK2 0.04, PFK 0.15, PKM2 0.12), so −0.79 is largely a construction property. |
| T13 | PARTLY | Glycolytic arm, supported (see T12; LDHA is the exception). Inflammatory arm: ratio–NFKB1 R = −0.21, p < 0.05 (GDM; Fig 4 *) and −0.54, p < 0.001 (NGT). WWOX–NFKB1 R = −0.22, p < 0.05 (GDM). Wnt arm: ratio–DVL2 R = −0.21, p = 0.05 (GDM; Fig 4 *) and −0.43, p < 0.01 (NGT); ratio–CTNNB1 R = +0.38, p < 0.001 (GDM; positive, with a lower ratio going with lower CTNNB1) and 0.09 NS (NGT); WWOX–CTNNB1 +0.25 (GDM) and +0.30 (NGT). CRP: no association is reported with the ratio or WWOX. In GDM, only HbA1c correlated (Table S1). In NGT, only insulin, HOMA-IR and QUICKI-IS correlated with WWOX or the ratio (Table S1); CRP is not listed. | Not supported: correlation with CRP as an inflammatory variable. NFKB1 and DVL2 correlations are weak to moderate and are mRNA-level only. The proposition omits the direction, and the CTNNB1 sign is the opposite of "increased". Conversely, the Discussion states "clearly pointing to a crosstalk between NFKB1 upregulation, WWOX downregulation…", which is stronger than the −0.21 to −0.22 coefficients. |
| T14 | PARTLY | "HIF1A is increased": supported (3.8-fold, p < 0.0001). "Ratio… markedly decreased": the word "markedly" is not in the source (searched). Magnitude is supported: "approximately 6.5-fold (p <0.0001)", Abstract "approximately six times". "WWOX is reduced": supported only by the Abstract ("significant downregulation"), the Discussion and the Conclusions. The Results text hedges it ("tendency… p = 0.0406") and the effect is 1.4-fold. | The sentence merges the Abstract's strength for WWOX with the Results' size. It also omits that the ratio change is, per the figures, dominated by the HIF1A change (see T6), and that the compared tissue is whole mixed leukocytes. |

SUMMARY SECTION

(a) Items checkable only against text, not against a figure image:
- T1, T2 (the 3.8-fold figure), T3 (the 1.4-fold figure), T4 (the 6.5-fold figure) and T5 are text-only. T2, T3 and T4 also have asterisks in Fig 2, which I opened.
- T10 was checked against Table S1 (docx) in addition to the text.
- T6 is partly text-only; the −0.79 and 0.61 figures are in Figs 4 and 5.
- T13 and T14 are mainly text, with the values cross-checked in Figs 4 and 5.
- T8 is figure-only.
- T12's HIF1A correlation is figure-only.

(b) Text–figure or text–supplement disagreements:
- HbA1c vs LDHA in GDM: text and Table S1 give R = −0.27, p = 0.010. Fig 6E gives R = −0.22, p = 0.036.
- HbA1c vs HK2 in GDM: text and Table S1 give R = 0.35, p = 0.004. Fig 6C gives p = 0.0003.
- Text says WWOX–SLC2A4 R = 0.17 is "significant… all p < 0.05". Fig 4 shows no asterisk on 0.17.
- Text says HIF1A–SLC2A4 R = −0.19, p < 0.05. Fig 4 shows no asterisk on −0.19.
- Discussion says NFKB1 is inversely correlated with SLC2A4. Fig 4 shows −0.17, no asterisk.
- WWOX–PFK in GDM: text −0.23, Fig 4 −0.22.
- HIF1A–SLC2A1: text 0.45, Fig 4 0.44.
- Table S1 lists a GDM SLC2A column with HbA1c R = 0.20, p = 0.053, not significant.
- HK2: the Abstract says overexpressed in GDM, but the Results and Fig 2E say unchanged.
- WWOX p = 0.0406: the Results text says "tendency", Fig 2A marks * and the Abstract says "significant".

(c) Items bearing directly on WWOX in leukocytes that the triples do not cover:
- Methods say RT-qPCR was done on all genes postpartum, and the text says "expression pattern of all the aforementioned genes was compared" postpartum. Only WWOX is shown (Fig 3); no postpartum HIF1A or ratio results are reported.
- Fig 3 shows B vs GDM * and C vs GDM ** (unpaired). The text does not report these.
- The Discussion names a limitation: the cause of the WWOX decrease was not investigated. It proposes DNA methylation as speculation only.
- The Discussion says leukocyte subsets were not analysed, so cell-composition differences cannot be excluded.
- The paper does not test or state a causal direction, and there is no protein-level data. Those are the authors' own caveats.
- Table 2 shows GDM women were older, HbA1c was lower in GDM (p = 0.0002) and only 8 and 12 women returned postpartum. These bear on interpreting the WWOX difference.

Settings: model sonnet (Sonnet 5.5), effort high. Tool calls: 15 before this handback.
