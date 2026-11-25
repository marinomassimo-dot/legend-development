# Blind report, ADV-282 increment 1 (checker: sonnet, effort high, 2026-11-25)

Hypothesis-level reading of public data. Not medical advice.

## Common method (applies to every section)

Sources used: the GSE156243 Salmon count table (35,337 gene rows x 6 libraries), the two deposited gene lists, the family SOFT file, the 2021 article XML and its figures, and for culture-time claims only GSE150123 (series matrix and the 62 per-sample count CSVs).

- Replicate unit and species for GSE156243: one library per GEO sample, human (Homo sapiens) WiBR3-hESC-derived cerebral organoids, age 15 weeks, bulk polyA RNA-seq, Salmon gene counts. 4 knockout libraries (GSM4727527-30, columns cko1-cko4) and 2 wild-type libraries (GSM4727525-26, columns cwt1-cwt2). KO clone and batch are not given per library in the SOFT file. The article says 8 organoid samples were sequenced and 2 WT were excluded (Methods, "Library preparation and RNA sequencing").
- Normalisations I used, all computed from the count table with total-count library sizes of 38.73M, 41.15M, 38.21M, 34.21M, 37.26M, 29.98M (cko1-4, cwt1-2):
  - CPM = count / library total x 1e6 (total over all 35,337 rows). "ratio CPM" = mean CPM of the 4 KO libraries divided by mean CPM of the 2 WT libraries.
  - NM = counts divided by median-of-ratios size factors (cko1-4, cwt1-2 = 1.057, 1.113, 1.100, 0.953, 1.006, 0.809, computed on genes with all six counts > 0). "ratio NM" and "log2 NM" are defined the same way.
  - "meanlog2" = mean over KO of log2(x+1) minus mean over WT of log2(x+1).
- Deposited lists: 1,246 up and 1,021 down genes. Every gene in them has raw P <= 0.00999 and |log2FC| >= 0.26, but padj runs up to 0.0684 (825+1,067 genes have padj < 0.05, 518+317 have padj < 0.01). So "in the authors' list" means nominal P < 0.01 plus FC > 1.2 (article Results, RNA-seq paragraph), not padj < 0.01. The two lists do not overlap.
- Knockout check (same for all six blocks, given once here and referred to below):
  CHECK CLASS = CHECK PRESENT. In-study check: yes.
  - Another effect of the same knockout in the same week-15 preparation, inside the deposit itself: 2,267 differentially expressed genes; PCA separates KO from WT libraries (article Fig EV3A, file EMMM-13-e13610-g004.jpg, panel A). Recomputed from the count table: GAD1 ratio CPM 11.57 (KO 8.9-37.9 CPM vs WT 3.5 and 0.2; deposited UP list padj 1.22E-02, log2FC 3.57); RELN ratio CPM 14.1 (padj 5.88E-12, log2FC 4.01); WNT3 ratio CPM 3.71; AXIN2 and LEF1 in the UP list. The article reports the same direction by qPCR on week-15 organoids (Fig 1D, g006 panel D, GAD1 and GAD2 up; Fig 4D, g008 panel D, Wnt genes up).
  - Loss of the target protein is shown only at other times: Fig 1A and 1B (g006 panels A, B, week 10 immunofluorescence, WWOX absent in KO); Fig EV1B (g011 panel B, western blot, week 6 organoids, WWOX absent in KO organoids); Fig EV2A and B (g009 panels A, B, week-24 western blot, WWOX fold change KO 0.03 +/- 0.002; the figure legend says week 24, the Results text says week 20). No WWOX protein measurement at week 15 and none on the sequenced libraries is in the held bytes.
  - WWOX transcript is not lowered in the deposit: WWOX raw counts KO 547, 488, 632, 420 vs WT 359, 302; CPM 9.64-16.54, ratio CPM 1.39, all four KO above both WT; WWOX is in neither list. This is expected for an exon-1 frameshift (Fig EV1C, g011 panel C) and means the deposit cannot show the loss by transcript.
  - Caveat: this is a time-bracketed check (protein at weeks 6, 10, 24) plus an effect check at week 15, not a protein check at the sampling time.

---

## DA-GSE-PDK-003

VERDICT: MUST CHANGE (one statement not reproducible as worded; two clauses need adding).

Recomputed (human organoids, 4 KO v 2 WT libraries; PDK1 is in neither list):
- PDK1: raw counts KO 533.0, 672.8, 477.5, 520.6; WT 659.0, 579.2. CPM KO 13.76, 16.35, 12.50, 15.22; WT 17.69, 19.32.
  - meanlog2(CPM+1) = -0.341, so "-0.34" is right as worded and it is a total-count (CPM) number.
  - log2 of ratio NM = -0.392 (meanlog2 of NM+1 = -0.401), so "-0.39" is right and it is a median-of-ratios number. This is the whole difference between -0.34 and -0.39 (see DA-I01-001).
  - All four KO libraries are below both WT libraries (KO max 16.35 CPM < WT min 17.69; same under NM).
- "inside the single-gene null, p about 0.30": the null is not defined in the held files. My version, the fraction of genes with |shift| >= |PDK1 shift|: 0.266 (CPM, -0.341, all 19,694 genes with total count >= 10), 0.317 (CPM, mean CPM >= 5, n = 11,449), 0.389 (NM, -0.401, all), 0.267 (NM, mean CPM >= 5). So "about 0.30" falls inside my 0.27-0.39 range; the exact figure is NOT CHECKED. Side note: with 4 v 2 libraries the smallest possible exact rank-test P is 1/15 one-sided, 2/15 = 0.133 two-sided, so no rank test could reach 0.05 here.
- "the PDK/PDH set +0.17 (P 0.22)": set membership is not given. Mean shift (mean over genes of meanlog2(NM+1)): PDK1-4 + PDHA1, PDHB, DLAT, DLD, PDHX, PDP1, PDP2, PDPR = +0.160; PDHA1, PDHB, DLAT, DLD, PDHX = +0.171; PDK1-4 alone = +0.102; PDK1-4 + PDP1/2 = +0.064. So a +0.16/+0.17 mean is reproducible for plausible sets. The P of 0.22 is NOT reproduced: random gene sets of the same size (20,000 draws from the 19,694 filtered genes, two-sided) give P = 0.48 and 0.55 for the two sets that match +0.17, 0.33-0.81 for the others. P 0.22 is NOT CHECKED (test unnamed).
- "LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries)": the definition is not given; the claim is not robust. Per-library ratios of CPM, KO cko1-4 and WT cwt1-2:
  - LDHA/PDHA1: KO 0.717, 0.580, 0.826, 0.750; WT 0.910, 0.807. KO mean 0.718, WT mean 0.858 (ratio 0.84). KO inside the WT range: 1/4; below WT minimum: 3/4.
  - (LDHA+LDHB)/(PDHA1+PDHB): KO 3.22, 3.16, 3.12, 3.06; WT 3.54, 4.60. KO inside WT range 0/4, all four below.
  - LDHA/(PDHA1+PDHB): KO 0.532, 0.441, 0.608, 0.574; WT 0.563, 0.550. KO mean 0.539 vs WT 0.556 (about -3%): "not shifted" holds for this pairing only.
  - LDHA/PDHB: KO 2.07, 1.84, 2.31, 2.45; WT 1.47, 1.73. KO mean 2.17 vs WT 1.60 (+35%).
  So the shift ranges from about -36% to +35% by pairing; "inside the spread of two WT libraries" is true for at most one pairing.
- What a reader needs and the sentence omits: PDHA1 (the PDH E1-alpha gene) is in the authors' UP list (padj 5.75E-10, log2FC 0.96; ratio CPM 2.02; all four KO above both WT: KO 115.5-133.3 CPM vs WT 57.4, 68.0); PDPR in the UP list (padj 1.26E-04, log2FC 0.64; ratio CPM 1.66); LDHA in the UP list (padj 4.92E-06, log2FC 0.91; ratio CPM 1.70); PDK3 in the UP list (P 7.39E-03, padj 5.65E-02, log2FC 0.55; ratio CPM 1.55). A set-level mean of +0.17 averages these away from PDK1 (-0.39), PDK2 (-0.17), PDHX (-0.23).

Replacement / added clauses:
- Replace "LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries)" with: "the LDH-to-PDH transcript ratio depends on the pairing (LDHA/PDHA1 0.72 KO v 0.86 WT, 3 of 4 KO below both WT; LDHA/(PDHA1+PDHB) 0.54 v 0.56); no pairing was fixed in advance in the held sources".
- Add: "PDK1 is lower in all four KO libraries than in both WT libraries (CPM 12.5-16.4 v 17.7, 19.3); PDHA1, PDPR and LDHA are in the authors' up list (padj 5.8E-10, 1.3E-04, 4.9E-06) and PDK3 is nominally up; the set mean hides these."
- Say which set and which test gave P 0.22 (not recoverable from the held files).

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes. Locator: deposit GAD1/RELN rows and PCA Fig EV3A (g004 A); protein at other times Fig 1A/B (g006), Fig EV1B (g011 B), Fig EV2A/B (g009 A, B).

NOT CHECKED: "IT5 same-sets re-analysis" as a run; the definition of the PDK/PDH set and of the LDH/PDH ratio; the P 0.22.

---

## DA-L01-003

VERDICT: MUST CHANGE (one false list statement; one over-reach; two additions).

Verified as worded (ratio CPM, mean of 4 KO / mean of 2 WT; precise values in brackets):
- Counts. IL6 raw 0, 0, 0, 0, 0, 0 (all six) OK. IL1B raw KO 1, 0, 1, 0; WT 1, 11 (range 0-11) OK. TNF raw KO 1, 0, 1, 0; WT 0, 0 (range 0-1) OK. P2RY12 raw 0 in all six OK.
- Ratios: NFE2L2 0.75x (0.7523), KEAP1 0.93x (0.9264), NQO1 0.73x (0.7297), G6PD 0.75x (0.7452), SLC7A11 0.65x (0.6527), BACH1 0.73x (0.7348), HMOX1 1.67x (1.6673), SRXN1 1.33x (1.3333), GSR 1.20x (1.1962). All nine reproduce exactly from mean CPM; median-of-ratios values would be 0.73, 0.90, 0.71, 0.73, 0.64, 0.72, 1.61, 1.29, 1.17.
- 4 v 2 libraries, one laboratory: OK (SOFT file and article, Hebrew University). WT is one parental line: OK (SOFT: hESC line WiBR3 for all six; article Statistics: at least two lines per genotype "with the exception of the WiBR3 WT line"). The two WT survivors of an exclusion: OK (Methods: one WT failed preliminary QC for low read count and low mapping rate, another did not cluster in PCA or dendrogram; the SOFT overall design says "2 WT samples failed quality control"). "post hoc" is the sentence's characterisation; the article says the exclusions came from QC and clustering after sequencing. KO clone and batch not assigned in the deposit: OK (SOFT titles "KO/WWOX 1-4", descriptions CKO1-4, no clone field; design says only "age- and batch-matched").
- NFE2L2 in the authors' list: DOWN, P 9.32E-04, padj 1.43E-02, log2FC -0.58; alpha 0.01 is stated in Methods. OK. NQO1 and HMOX1: in neither list. OK. IL1B, IL6, TNF, KEAP1, SLC7A11, BACH1, SRXN1, GSR also in neither list.
- NFE2L2 and NQO1 lower in all four KO libraries: NFE2L2 CPM KO 19.67-22.38 vs WT 26.05, 29.29; NQO1 CPM KO 4.15, 6.25, 6.82, 8.02 vs WT 8.39, 8.90 (thin margin, 8.02 v 8.39). OK.

MUST CHANGE:
- "only NFE2L2 is in the authors' DE list". G6PD is also in the deposited DOWN list: P 3.15E-04, padj 7.15E-03 (below the 0.01 alpha), log2FC -0.42, and G6PD is one of the nine genes in the same sentence (0.75x; KO CPM 66.3-75.1 vs WT 100.9, 89.0, all four KO lower). Replacement: "NFE2L2 (padj 1.43E-02, log2FC -0.58) and G6PD (padj 7.15E-03, log2FC -0.42) are in the authors' DE list; the other seven genes named are in neither list". For the wider reader: GSTP1 (padj 4.38E-03) and PRDX1 (padj 2.44E-02), both lower, are in the same list.
- "no cytokine-expressing compartment" (after IL6, IL1B, TNF, P2RY12). Counts of IL1B/IL6/TNF (0-11) show no detectable transcripts of those three genes in these unstimulated libraries; they do not show that no cell type expresses cytokines. In the same libraries TGFB1 (KO 1,558-2,151 raw), TGFB2 (55-678), MIF (about 11,200-15,600), IL33 (58-266), IL34 (165-317), CSF1 (198-509) and IL17D (400-783) are well expressed, and a myeloid-lineage signal is detectable (AIF1 157-557 raw, 3.8-14.6 CPM; CD68 346-1,460 raw, 8.8-38 CPM; CSF1R 16-109 raw). Replacement: "no detectable IL1B, IL6 or TNF transcript (0-11 counts) and no P2RY12; other cytokines and weak AIF1/CD68 signal are present, so a cytokine-expressing or myeloid-like compartment is not excluded".

ADD:
- "NFE2L2 and NQO1 transcripts are lower in all four KO libraries ... while HMOX1, SRXN1 and GSR are higher": the higher genes are higher on group means but not in every library: HMOX1 KO 10.72, 6.07, 15.13, 8.71 CPM vs WT 6.28, 5.90 (cko2 6.07 sits between them; 3/4 above both); SRXN1 KO 11.59, 5.69, 14.28, 10.52 vs WT 6.75, 9.02 (cko2 below both, cko4 10.52 above both; 3/4 above both WT); GSR KO 58.87, 53.52, 53.40, 43.94 vs WT 43.03, 44.63 (cko4 sits between them; all four above the WT mean, 3/4 above both). A reader would take "higher" as parallel to "all four"; say "3 of 4".
- "no coherent NRF2 signature": the criterion is not given. Of the nine named genes six are lower (NFE2L2, KEAP1, NQO1, G6PD, SLC7A11, BACH1) and three higher. Outside the sentence, GSTP1, PRDX1, TXNRD1, PGD, FTH1, FTL and GCLM are all lower in all four KO libraries (ratio CPM 0.76, 0.84, 0.91, 0.87, 0.86, 0.81, 0.89), GCLC is 1.14x. Add the criterion (e.g. "mixed direction in the named panel") and note that most canonical target transcripts shown are mildly lower, which is the arm-R-compatible direction the same sentence already states.
- Lists are selected by nominal P < 0.01 and FC > 1.2 (padj up to 0.068), so "in the list" does not mean padj < 0.01.

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes; locators as in the common method. This matters here because the headline is an absence of IL1B/IL6/TNF change.

NOT CHECKED: the "IT11 P2.3 verification" and "arm R" labels; "NRF2 activity" (no activity assay in the held bytes).

---

## DA-W2-012

VERDICT: MUST CHANGE ("nominally" for PDGFRA; one clause with no held source); ADD (panel scope).

Recomputed (CPM, human organoids, 4 KO v 2 WT libraries):
- PDGFRA: raw KO 182, 55, 86, 74; WT 13, 7.3. CPM KO 4.70, 1.34, 2.25, 2.16 (mean 2.61); WT 0.35, 0.25 (mean 0.30). Ratio CPM 8.80; all four KO above both WT. In the authors' UP list: P 2.78E-04, padj 6.55E-03, log2FC 3.02. The article itself names PDGFRA among the top-100 upregulated genes (Results, RNA-seq paragraph, "calcium signaling ... PDGFRA", Fig 4A). So "nominally higher" understates it: it is higher in every KO library and passes the authors' list at padj < 0.01.
- OLIG1: raw KO 4, 4, 33, 25; WT 1, 2. CPM KO mean 0.45, WT 0.05, ratio CPM 9.59; all four KO above both WT; in neither list. "nominally higher" is fair for OLIG1 (1-2 counts in WT).
- SOX10: raw KO 7, 2, 4, 2; WT 4, 2; ratio CPM 1.13, overlapping, neither list. MOG: raw KO 9, 26.3, 31.5, 31.4; WT 23.5, 19.2; ratio 1.03, neither list. OLIG2: raw KO 25, 26, 70, 56; WT 30, 33; ratio 1.25, 2 of 4 KO above both WT, neither list. "SOX10, MOG and OLIG2 are not [higher]" is right.
- "counts are very low": true for these five (CPM 0.05-4.7 per library).

Panel scope (ADD): the sentence covers five genes, but the row says "oligodendrocyte-lineage transcripts" in general, and other lineage genes in the same table are not low or not unchanged: PLP1 raw KO 2,664, 3,066, 7,571, 2,992 vs WT 2,439, 1,461 (CPM 68.8-198 vs 48.7, 65.5; ratio CPM 1.88; all four KO above both WT; neither list); MBP raw KO 118, 46, 145, 77 vs WT 54, 42 (ratio CPM 1.79; in the UP list, P 5.09E-03, padj 4.46E-02, log2FC 1.41); NKX2-2 raw KO 5, 6, 18, 4 vs WT 2, 0 (ratio CPM 8.0; neither list); CNP flat (0.99). PLP1 is also expressed outside oligodendrocytes, so these are not oligodendrocyte-specific, but the sentence's "counts are very low" is false for PLP1/CNP.

Replacement: "PDGFRA is higher in all four knockout libraries (about 8.8x mean CPM, 2.6 v 0.3; in the authors' up list, padj 6.55E-03) and OLIG1 is higher from very low counts (4-33 v 1-2; in neither list); SOX10, MOG and OLIG2 are not different (ratios 1.13, 1.03, 1.25). PLP1 and MBP, not in this panel, are also higher (1.88x, 1.79x)."

"composition differs": supported in general by the deposit (e.g. GJA1 ratio CPM 5.4, CD44 3.9, GAD1 11.6; all UP-list) and the article (astrocytic and GABAergic differences), OK.

"a week-15 organoid has no compact myelin": NOT CHECKED, no held source states it. The article text mentions myelin only in reference titles (hypomyelination in Wwox-null rat, myelin defects with neuronal Wwox deletion); it makes no statement on myelin in these organoids. Mark it as background knowledge or cite a source.

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes. Matters because the sentence reports unchanged genes (SOX10, MOG, OLIG2).

---

## DA-J01-007

VERDICT: MUST CHANGE (a count criterion and one classification fail as worded; one clause unsourced and contradicted for CD44); ADD (GFAP).

Recomputed (CPM, human organoids, 4 KO v 2 WT libraries):
- Microglial markers: P2RY12 raw 0 in all six. CX3CR1 raw KO 2, 1, 2, 0; WT 2, 0. PTPRC raw KO 7, 2, 6, 1; WT 3, 10. TREM2 raw KO 12, 1, 4, 1; WT 4, 10. All at or below 12 raw counts (<= 0.33 CPM): "at or near zero" OK. "the tissue cannot test a microglial arm" is a conclusion; note AIF1 (raw 157-557, 3.8-14.6 CPM) and CD68 (raw 346-1,460, 8.8-38 CPM) are detectable, so say "microglia-specific markers" rather than all myeloid signal.
- IL1B, IL6, TNF "under 20 raw counts": IL1B max 11, IL6 0, TNF max 1. OK.
- VIM raised: ratio CPM 1.82 (KO 2,761-3,860 CPM vs WT 1,621, 1,908; UP list padj 4.15E-05, log2FC 0.82). CD44 raised: ratio CPM 3.91 (KO 11.3-56.1 vs WT 5.3, 9.9; UP list padj 8.09E-03, log2FC 1.80). OK.
- TIMP1 lower: ratio 0.63, all four KO below both WT, DOWN list padj 4.22E-03. OK. SOCS3 lower: ratio 0.40, all four KO below both WT, DOWN list padj 5.11E-04. OK. SERPINA3 lower: ratio 0.40, all four KO below both WT, in neither list (raw 17-93). OK as a direction, but see below.
- C3: ratio 1.30, 2 of 4 KO above both WT, neither list: "not separated" OK.

MUST CHANGE:
- "of seven reactive-pan genes above 5 CPM": not true for two of the seven. SERPINA3 is below 5 CPM in every library (0.41-3.10 CPM; mean KO 0.95, WT 2.34). C3 is below 5 CPM on the group means (KO 4.56, WT 3.50; per library 1.55-7.56). If the threshold is 5 raw counts or 5 normalised counts, all seven pass, so state the unit. Replacement: "seven reactive-pan genes above 5 counts (CPM 0.4-3 for SERPINA3 and 1.5-7.6 for C3)".
- "C3 and STAT3 not separated": STAT3 is in the authors' UP list (P 2.29E-04, padj 5.74E-03, log2FC 0.52); CPM KO 132.3, 117.3, 169.1, 127.1 vs WT 90.9, 95.5; ratio CPM 1.46; all four KO above both WT. "Not separated" is not what the source shows. The row says classification followed a rule declared before the data (rule not in the held files, NOT CHECKED); if that rule (for example a ratio cut) makes STAT3 "not separated", the sentence must say so. Replacement: "STAT3 is nominally higher (1.46x, in the authors' up list, padj 5.74E-03) but below the declared cut".
- "VIM and CD44 (both radial-glia or progenitor associated)": no held source for this. For CD44, the unperturbed human cortical spheroid time course GSE150123 (hCS, hiPSC lines, 62 libraries, day 25-652, RiboZero total RNA, rsem counts; CPM from per-sample raw counts) shows the opposite: CD44 rises with culture age (Spearman rho +0.92 with differentiation day over all 62 libraries; +0.93 in batch 1, n = 15; +0.91 in batch 2, n = 47; median CPM 2.9 at day <= 80, n = 19, vs 76.2 at day >= 220, n = 28, 26x). GJA1 behaves the same (rho +0.67; 27 to 321 CPM, 12x), VIM falls slightly (rho -0.17; ratio 0.74). Different laboratory, protocol, line and RNA prep from GSE156243, so only a direction check; it does not support a progenitor reading for CD44. Remove the parenthesis or label it "literature association, not from the held sources".

ADD:
- GFAP, the usual reactive marker, is not in the seven. Deposit: GFAP raw KO 4,102, 1,649, 9,293, 5,212; WT 6,874, 3,732; CPM mean KO 135.4, WT 154.5; ratio CPM 0.88; not in either list; S100B ratio 1.60 (not in a list); AQP4 ratio 3.4 (UP list, padj 5.69E-02). The article reports GFAP and S100B protein higher in week-15 KO organoids by immunofluorescence (Fig 3A, g003 panel A) while its own week-15 qPCR shows GFAP flat and S100B and AQP4 raised (Fig 3B, g003 panel B; GFAP qPCR rises at week 24, Fig 3C). A reader of "not a gliosis measurement" needs that protein/RNA split to know why RNA is silent on GFAP.
- Other reactive-pan genes absent from the seven: HSPB1 ratio 0.82 (3/4 KO below both WT), S1PR3 0.83 (4/4 below), OSMR 1.46 (4/4 above, CPM < 1), none in a list.

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes. The headline here is NO_CHANGE / absent microglial signal, so it matters.

NOT CHECKED: the declared classification rule; the identity of the "seven" (not named in the held sources).

---

## DA-K01-002

VERDICT: ADD (the numbers and the culture-time statement are right; the normalisation label, the per-gene qualifiers and the dataset caveats are missing). No false statement found among the checked items.

Recomputed (human organoids, 4 KO v 2 WT libraries; KO raw counts listed cko1-4, then WT):
- Printed ratios. EPAS1 3.80 (3.7972; raw 351, 117, 190, 180 | 44, 52); HK2 4.73 (4.7296; 3,056, 3,681, 3,579, 2,059 | 736, 429); SLC2A1 2.67 (2.6743; 5,578, 5,565, 8,018, 4,657 | 2,321, 1,637); ARNT 1.46 (1.4626); HIF1A 0.84 (0.8420); PDK1 0.78 (0.7813). All six reproduce exactly as ratio of mean CPM (total-count normalisation). The row says "ratio of normalised counts"; with median-of-ratios normalisation the values are 3.70, 4.60, 2.59, 1.42, 0.82, 0.76. Without any normalisation they would be 4.37, 5.31, 3.01, 1.66, 0.95, 0.89. State "ratio of mean CPM".
- List membership: EPAS1 UP (padj 1.87E-03, log2FC 1.97); HK2 UP (padj 8.75E-34, 2.46); SLC2A1 UP (9.99E-10, 1.44); ARNT UP (9.21E-03, 0.40); HIF1A and PDK1 in neither list. ADM (1.63E-11), P4HA1 (2.17E-06), BHLHE40 (4.54E-08), ANKRD37 (2.78E-03), EGLN3 (2.43E-05), DDIT4 (1.03E-05) and HK2 are all in the UP list: "ADM, HK2, P4HA1, SLC2A1, BHLHE40, ANKRD37, EGLN3, DDIT4 up" OK. PGK1 (0.94), ALDOA (1.13), ENO1 (1.17), PKM (1.13), PFKP (1.00), NDRG1 (1.11), CA9 (1.05) are in neither list: "flat" OK on ratio and list (ENO1 and PKM sit above both WT in 3 of 4 KO libraries, ratio about 1.15, so "flat" means "not in the list").
- "HIF1A mRNA 0.84 times (flat)": CPM KO 39.15, 43.61, 33.53, 39.54 vs WT 49.51, 43.03: 3 of 4 KO below both WT; log2 -0.25. "Flat" is acceptable as "not in the list", not as "no shift"; PDK1 0.78 is below both WT in 4 of 4.
- "MYC +0.56 log2": reproduces as log2 of the ratio of mean NM counts (+0.564); with CPM it is +0.608 (ratio 1.52); MYC is in neither list. The sentence therefore mixes a CPM ratio for the six headline genes with an NM log2 for MYC.
- "observed +2.18, +1.40 and +0.75 [log2 for HK2, SLC2A1, LDHA]": meanlog2(CPM+1) = +2.174, +1.382, +0.740; log2 of ratio CPM = +2.242, +1.419, +0.763; log2 of ratio NM = +2.202, +1.374, +0.720; deposited list log2FC = 2.46, 1.44 and 0.91 (LDHA UP list, padj 4.92E-06). The printed values are within 0.02 of the first set; the method is not stated; add it.
- "the glycolytic genes also fall with elapsed culture time in unperturbed spheroids": GSE150123 (human cortical spheroids from six hiPSC lines, 62 libraries, day 25-652, two batches, RiboZero total RNA, rsem raw counts, different laboratory from GSE156243). CPM from raw counts. Spearman rho against differentiation day, all 62 / batch 1 (n = 15) / batch 2 (n = 47); median CPM day <= 80 (n = 19) v day >= 220 (n = 28): HK2 -0.54 / -0.72 / -0.47; 293.0 v 107.8 (0.37x). SLC2A1 -0.46 / -0.83 / -0.34; 331.9 v 140.2 (0.42x). LDHA -0.56 / -0.74 / -0.43; 347.2 v 135.3 (0.39x). DDIT4 -0.60 / -0.76 / -0.57 (0.40x). So the statement is right for HK2, SLC2A1, LDHA and DDIT4. It is not true for the whole hypoxia panel: ADM -0.08 (0.83x), BHLHE40 -0.00 (1.01x), P4HA1 -0.23 (0.71x), ANKRD37 -0.40 (0.62x), EGLN3 +0.38 (1.53x, rises). The flat genes (PGK1, ALDOA, ENO1, PKM, PFKP, NDRG1, CA9) were NOT CHECKED in the time course (the held files used here give no ENSG for them, and I did not use any other mapping file). Name the genes and the dataset (hCS, day 25-652, other laboratory) in the sentence.
- "four versus two libraries, one laboratory": OK.

Not checkable from the held files: the "12 progenitor and neuronal marker genes", the maturity-offset prediction (median +0.08 to +0.16 log2) and its "calibration from another laboratory" (NOT CHECKED; the genes and the calibration set are not named); "IT10 P2.1 (premises a2, a3)", "IT7 six-gene readout" and "guard IT7_READOUT6" (NOT CHECKED). The row direction INCREASE covers HIF1A (0.84) and PDK1 (0.78), which fall.

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes. The headline is an increase, so the check bears on whether the KO produced it, not on its absence.

---

## DA-I01-001

VERDICT: ADD (statements right; the reconciliation the sentence says is missing can be given; two clauses a reader needs).

Recomputed (human organoids, PDK1, 4 KO v 2 WT libraries; PDK1 is in neither list):
- "PDK1 -0.39": log2 of the ratio of mean NM counts = -0.392; meanlog2(NM+1) = -0.401. OK.
- "the earlier card E03 prints -0.34 for the same comparison; the two runs differ in method and the difference is not reconciled here": reconciled by normalisation. meanlog2(CPM+1) = -0.341 (total-count library sizes; PDK1 CPM KO 13.76, 16.35, 12.50, 15.22; WT 17.69, 19.32) versus -0.392/-0.401 with median-of-ratios size factors (1.057, 1.113, 1.100, 0.953 | 1.006, 0.809). The smallest WT library (cwt2, 29.98M total, size factor 0.809) is what moves it. Add: "-0.34 is the CPM (total-count) value and -0.39 the median-of-ratios value of the same six libraries."
- "LOWER IN SIGN ONLY ... inside the single-gene null (p about 0.30)": the null is not defined in the held files (NOT CHECKED as stated); my empirical fraction of genes with |shift| >= |PDK1 shift| is 0.27-0.39 depending on normalisation and expression filter (see DA-GSE-PDK-003). Add that PDK1 is below both WT libraries in all four KO libraries (KO 12.5-16.35 vs WT 17.69, 19.32 CPM; same under NM) and that with 4 v 2 libraries no rank test can give P below 0.133 two-sided, so "inside the null" reflects the size of the shift against other genes and the small n, not a mixed direction.
- "The PDK set as a whole is indistinguishable from chance": NOT CHECKED (set not defined). PDK1-4 as a set has mean shift +0.10 (random-set P 0.73, same method as above), consistent with the sentence; but the set hides opposite signs: PDK1 -0.39, PDK2 -0.17 (KO below both WT in 4/4 under NM), PDK3 +0.59 (UP list, P 7.39E-03, padj 5.65E-02; 4/4 KO above both WT), PDK4 +0.40 (3/4 above both WT).
- "The maturity confound of this deposit applies": no maturity measurement is in the sentence; the held time course shows that culture age moves HK2, SLC2A1, LDHA and DDIT4 down by 0.37-0.42x (GSE150123, see DA-K01-002), but PDK1 and the PDH genes were NOT CHECKED there (PDHA1 rho -0.13, 0.86x; PDPR +0.03, 1.17x were computed; PDK1 was not).

Replacement or added clause: "PDK1 -0.39 (median-of-ratios normalisation; -0.34 with CPM normalisation, the same six libraries) ... lower in all four knockout libraries than in both wild-type libraries".

CHECK CLASS: CHECK PRESENT (see common method). In-study check: yes. The headline is a not-changed (not raised) result, so it matters.

---

## Summary table

| id | class | in-study | verdict |
|---|---|---|---|
| DA-GSE-PDK-003 | CHECK PRESENT (effect at week 15 in the deposit; WWOX protein loss shown at weeks 6, 10, 24, not 15; WWOX transcript not reduced) | yes | MUST CHANGE |
| DA-L01-003 | CHECK PRESENT (same) | yes | MUST CHANGE |
| DA-W2-012 | CHECK PRESENT (same) | yes | MUST CHANGE |
| DA-J01-007 | CHECK PRESENT (same) | yes | MUST CHANGE |
| DA-K01-002 | CHECK PRESENT (same) | yes | ADD |
| DA-I01-001 | CHECK PRESENT (same) | yes | ADD |

## Files opened

- /home/desktop/.claude/jobs/ae0002e7/tmp/adv282/blind/BLIND_SENTENCES_ADV282_INC1_SCI_20261125.md (input)
- /home/desktop/legend-development/files/geo/GSE156243/GSE156243_CWT_2_CKO_4_Salmon_gene_count_table.txt.gz
- /home/desktop/legend-development/files/geo/GSE156243/GSE156243_CKO_CWT_1246_upregulated_genes.txt.gz
- /home/desktop/legend-development/files/geo/GSE156243/GSE156243_CKO_CWT_1021_downregulated_genes.txt.gz
- /home/desktop/legend-development/files/geo/GSE156243/GSE156243_family.soft.gz
- /home/desktop/legend-development/files/fulltext/PMID34268881_Steinberg2021_PMC_r2.xml (read through a plain-text conversion of my own)
- /home/desktop/legend-development/files/figures/PMID34268881_r2/EMMM-13-e13610-g002.jpg, g003, g004, g005, g006, g008, g009, g010, g011, g013 (viewed); g007 and g012 were converted to PNG only and not viewed
- /home/desktop/legend-development/files/geo/GSE150123/GSE150123_series_matrix.txt.gz, filelist.txt, the 62 per-sample files in raw/ (read by script), and the file list of GSE150123_RAW.tar (names only)
- Directory listing only (names, not opened): GSE156243/hgnc_complete_set_20261022.json and GSE156243/tool_responses_verbatim/ (outside the four named files; not used)
- My own scripts and outputs in /home/desktop/.claude/jobs/ae0002e7/tmp/adv282/blind/ (an.py, sets.py, lists.py, tc.py, xml2txt.py, article.txt, hyp.txt, ko.txt, figs/), all run with python3 -I -P -E and file paths as arguments. No network use; no other repository text opened.
