Under the 1,400-word cap. Quotes were checked as exact substrings of the XML text (whitespace-normalised): all 14 text quotes I tested matched. Figure cells were read from the images.

(a) Table

| # | Verdict | Reason |
|---|---|---|
| 1 | SUPPORTED | Quote gives 135 = 37 NGT + 98 GDM, one named clinic; the Abstract agrees. |
| 2 | SUPPORTED | Table 2 prints age 29.0 (NGT) vs 31.0 (GDM), p = 0.02*. The proposition leaves out the source's "slightly". |
| 3 | SUPPORTED | HIF1A is in the "all p < 0.0001" list and the text gives a 3.8-fold increase. Fig 2B prints ***. The source does not say how fold change is computed. |
| 4 | SUPPORTED | p = 0.0406, 1.4-fold decrease and Mann-Whitney are all stated. Fig 2A prints a single *. The proposition does not claim significance. |
| 5 | SUPPORTED (absence) | See (b). 0 hits for every correction term; Methods give only "A p-value <0.05 was considered as significant." |
| 6 | SUPPORTED | Quote exact; Results use "tendency" for WWOX. |
| 7 | SUPPORTED | The Abstract Results sentence is exact. The Results section itself says "tendency" (see T6). |
| 8 | OVERSHOOT | In the Discussion, "significant" is attached to the HIF1A upregulation, not to WWOX. WWOX is only "downregulated". |
| 9 | SUPPORTED | "approximately 6.5-fold (p <0.0001)" is exact. Fig 2L prints ***. |
| 10 | SUPPORTED (absence) | No sentence apportions the ratio change between the two genes (see (b)). Q1: the quotes show only a joint attribution. |
| 11 | SUPPORTED (arithmetic) | 3.8 > 1.4 is arithmetic on the source's numbers; the source never says one change is larger. |
| 12 | SUPPORTED (figure) | Fig 4 WWOX x HIF1A prints -0.05 with no asterisk. Q1 fails: the quote never mentions HIF1A, so it carries the claim only by omission. |
| 13 | SUPPORTED (figure) | Fig 4 prints HK2 -0.07, PKM2 -0.06 and SLC2A1 0.04, all with no asterisk. Q1 by omission only. |
| 14 | SUPPORTED | Text matches the proposition. Fig 4 prints PFK as -0.22 with *, not -0.23; NFKB1 -0.22*, CTNNB1 0.25*. |
| 15 | SUPPORTED (figure) | Fig 4 ratio x HIF1A prints -0.79***. Q1 fails: the quote is generic and the text never lists this pair. "Strongly" is not the paper's word here. |
| 16 | SUPPORTED | Fig 4 prints SLC2A1 -0.31**, HK2 -0.41***, PFK -0.45***, PKM2 -0.42***, matching the text. |
| 17 | SUPPORTED (figure, absence) | Fig 4 ratio x LDHA prints -0.1 with no asterisk. The ratio correlations in the text never list LDHA. Q1 by omission only. |
| 18 | SUPPORTED | Text matches. Fig 4 prints NFKB1 -0.21* and DVL2 -0.21*; the text says DVL2 p = 0.05, the figure shows a single *. |
| 19 | SUPPORTED | Text and Fig 4 (0.38***) agree on the value. "Weakly" is the proposition's own adjective; the source does not call this correlation weak. |
| 20 | SUPPORTED | See (b): the methods are RT-qPCR in leukocytes taken as a whole, and protein was not measured. |
| 21 | SUPPORTED | R = 0.52 and 0.53, p = 0.001 for both; the claim is in the text. Table S1 was not opened. |
| 22 | SUPPORTED | Fig 5 prints WWOX x PFK 0.3*, LDHA 0.32* and CTNNB1 0.3*, matching the text. |

(b) Non-SUPPORTED, plus the absence searches and figure notes

**T8, OVERSHOOT.** Source words:
- "In contrast to the significant upregulation of HIF1A leukocyte WWOX expression was downregulated in diabetic pregnancy versus normal controls"
- "leukocyte WWOX downregulation seen in our GDM patients may be a unique feature of diabetic pregnancy"
- Elsewhere in the Discussion: "support an important contribution of WWOX downregulation toward enhanced glycolysis"; "reduced WWOX expression in the leukocytes of GDM patients".

Across the Discussion and Conclusions I found no "significant ... WWOX" phrase for the GDM vs NGT decrease. The only "significant downregulation of WWOX" is in the Abstract. Within Results, the paper's own wording differs: "There was also a tendency for lower leukocyte WWOX expression ... (p = 0.0406)". Fig 2A prints a single *.

**T5, absence.** Terms searched in the whole XML text, hits in brackets:
- Bonferroni [0], multiple [0], correct [0], adjust [0], FDR [0], false discovery [0], Benjamini [0], multiplicity [0], Sidak [0], family-wise [0].
- Holm [1], a surname in a reference.

Statistics section: "A p-value <0.05 was considered as significant." "11 individual genes" is in Results. The Fig 4 and Fig 5 captions use unadjusted asterisk thresholds only. I did not search "Hochberg" or "q-value".

**T10, absence.** Terms searched: attribut [3, all licence text], driven [2], responsible [1], mainly [0], predominantly [1].
- Neither "driven" hit is about the ratio. They are "WWOX/HIF1A-driven transcriptional regulation" and "glycolytic genes driven by HIF-1α".
- The "responsible" hit concerns T2D network genes, and the "predominantly" hit concerns placental hormones.

The closest wording is "significant downregulation of WWOX with simultaneous upregulation of HIF1A which resulted in approximately six times reduction in WWOX/HIF1A ratio". That is a joint attribution with no split. The Results give both fold changes, so a split could be computed, but the paper does not do it.

**T11, arithmetic.** The source says only "as evidenced by an 1.4- fold decrease for WWOX and a 3.8-fold increase for HIF1A in the diabetic patients". The comparison of sizes is the proposition's arithmetic. The paper also does not reconcile 1.4 and 3.8 with the 6.5 for the ratio.

**T12, qualification elsewhere.** The Discussion says "We also showed a linkage of WWOX to HIF1α at their transcriptional levels in leukocytes of the patients with GDM." This is a different sense (opposing group means and the ratio), but it sits against a within-GDM WWOX x HIF1A cell of -0.05. The text never states the -0.05.

**T14, T18 and T19, wording and figure notes.**
- T14: PFK is -0.23 in the text and -0.22 in Fig 4.
- T18: the figure DVL2 cell has a single *, while the text writes p = 0.05.
- T19: the paper uses "weak" for the WWOX correlations of 0.25, 0.17, 0.30, 0.32 and 0.30, and does not apply it to the 0.38.

**T15 and T17.** The paper uses "strongly" for HIF1A x NFKB1 and DVL2 in the NGT group (R = 0.66 and 0.60). It does not use it for ratio x HIF1A. In Fig 5 (NGT) the same ratio x HIF1A cell also prints -0.79***. The ratio contains HIF1A, so this is a mathematical coupling, which is my inference and not something the paper says.

**T20.** The strongest passage for "not separated by cell type" is in the Discussion: "leukocytes are examined as a whole population of different cells". Quote 1 alone does not state it. Protein: Western [0], ELISA [0], immunoblot [0], flow cytometry [0]. The Conclusions' call for "analysis of protein expression" implies none was done.

**Figure-label discrepancies (not affecting any verdict).**
- The Fig 2 panel letters I and K are swapped against the caption: the image has I = NFKB1 and K = DVL2, while the caption says DVL2 (I), NFKB1 (K).
- The Fig 5 caption says "GDM group" in its second sentence, but its title and the correlation values mark it as NGT.

(c) Not judged: nothing was left unjudged. All figure cells were legible and I declare no attestation. Table S1 (the supplementary docx) was not opened. T21 rests on the main text, which states the values.
