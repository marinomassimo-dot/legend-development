# Independent read of package P2b (PDH-activity trace; lactate statistics), scientist-b, 2026-10-27

Class-level, public, de-identified. Not medical advice. Reader differs from the producer (scientist-a). Depth: full text read from
`files/fulltext/` copies (JATS XML for PMID 35328751 and PMID 36271927; PDF text for PMID 42909904, `pdftotext` without `-layout`;
Supplementary_tables_derived.txt), and both figures re-opened as images (Fig 5 of 35328751; page 12 of the PDF). Verdicts are
against the sources, not against the producer's conclusions.

| # | Claim | Verdict |
|---|---|---|
| 1a | "PDH activity unchanged" traces to PMID 35328751 only (Results 2.5, Fig 5b): fibroblast 1BR.3.N, partial depletion, 48 h, colorimetric total PDH activity (Methods 4.10, mU/mL), ANOVA/Tukey, no significant KO-vs-control difference, n not stated | SUPPORTED |
| 1b | The Results sentence naming "pyruvate dehydrogenase kinase (PDK)" is a mislabel of the Fig 5b quantity | SUPPORTED (inference from the caption, which labels panel b "Pyruvate Dehydrogenase", and Methods 4.10; the paper itself does not flag the slip) |
| 1c | PMID 36271927 (review) reports no PDH activity measurement | SUPPORTED (no "PDH" string in the text; it reports PDK mRNA up and HK/LDH activities up only) |
| 2 | Lactate statistics (Wwox main F 7.524 padj 0.0636; Abeta42 main F 27.846 padj 0.0050; interaction F 23.606 padj 0.0174; all under the paper's 10% FDR); Fig 5C rise only in KD+Abeta42; no separate Abeta42-vs-LacZ lactate test | SUPPORTED |
| 3 | Erratum in the 2026-10-26 audit and clause in `biological_needs.md` row C3 say exactly that and no more | SUPPORTED |

## Evidence

1. Results 2.5 names PDH in three conditions (NH "pyruvate dehydrogenase", HN "pyruvate dehydrogenase, lactate dehydrogenase, and citrate
   synthase", NN under the "PDK" slip) and covers HH with "no significant effect on enzymes activity". Methods 4.15 says one-way ANOVA "with repeated
   measures" plus Tukey; no replicate count anywhere in text or Fig 5 caption. Fig 5b image: single bracket (*) joins two control bars
   (NN vs NH); no KO-vs-control bracket; approximate KO vs control NN 3.0/2.3, NH 6.1/6.7, HN 7.2/4.8, HH 5.5/5.6 with wide SEM: matches the producer's
   hand reading. The overexpression arm reports PDH activity lower (p < 0.001) in hypoxia, as the producer says (Fig S3b not reopened by me either).
2. Supplementary Table 4 L-lactate row (exact standard match): 7.524 / padj 0.0636 / log2 +0.679; 27.846 / 0.0050 / +0.970; 23.606 / 0.0174 /
   +1.305 and -0.426. Results text agrees. Fig 5C (page 12): LacZ control about 4.9e5, LacZ+KD about 3.6e5, Abeta42 control about 4.8e5, Abeta42+KD about
   1.2e6; no per-cell significance mark; caption states the FDR applies to panels A-C only. No Abeta42-vs-LacZ lactate test appears in the text.
3. Erratum and row C3 state the three terms, the Fig 5C pattern and the absence of a within-control-background test; neither adds a claim.

## Limits (uncertainty, not error)

- "Wwox main effect passes 10% FDR" is true but marginal (padj 0.0636, F 7.524); both documents say marginal or just give the number.
- Bar heights in Fig 5b/5C are hand readings from a raster; approximate, and the producer labels them so.
- Whether "n unstated" also holds for the supplement or deposited source data was not checked.
- The review being silent on PDH activity shows absence in that text, not that no measurement exists elsewhere.
- No error found in any of the three claims; nothing was edited outside this file.
