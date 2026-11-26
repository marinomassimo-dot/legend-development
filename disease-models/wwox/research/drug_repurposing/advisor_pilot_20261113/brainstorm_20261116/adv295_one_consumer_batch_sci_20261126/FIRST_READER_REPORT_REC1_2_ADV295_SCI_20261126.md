# ADV-295 block 1, records 1 and 2: FIRST READER report as delivered (legend-delegate; models {'claude-sonnet-5-5': 94}; effort {'high': 94}; reply text extracted verbatim from its transcript hand-back call; 2026-11-26)

REPORT ADV-295 block 1, first reader (SCI delegate, sonnet, effort high; date 2026-11-26). No web, no e-mail, no acquisition. Obeid / 42422765 files not opened. Nothing written in the repo or files/. Scratch only in /home/desktop/.claude/jobs/c6d4dd83/tmp/adv295_a/. No openpyxl, docx or PIL here, so I parsed xlsx and docx with zipfile and ElementTree, and converted images with ImageMagick `convert`.
Verdict words follow the matching rule: CORRECT, ADD, WRONG, INCOMPLETE, NOT ASSESSABLE. Strict needs a blind reader to confirm MUST CHANGE, so every "strict candidate" below is mine only. The root checkout `.claude/worktrees/sci_at_20261126` is the repository path; the files/ root is /home/desktop/legend-development/files/.

====================================================
RECORD 1. PMID 42807679 (Khadija 2026, Front Genet). Consumer: CLAIM 032, claim_registry_current.md line 679.
====================================================
OPENED (sha256, in full)
| file | sha256 |
|---|---|
| fulltext/PMID42807679_Khadija2026_PMC.xml | e907bc5520981633a38355c42df452f7216f9ac9791a459b9e760a29685736aa |
| fulltext/PMID42807679_Khadija2026_supplement/Supplementaryfile1.docx | 8fee38f22d9fec6e5a4250ed58e6b288af8077533f562c097b88d1cfa6e55c63 |
| figures/PMID42807679/fgene-17-1815268-g003.webp | 39505ed2a1a5e2b78e2e4fd125139788d4e60ee1ad12235018a422addba75ee5 |
| ...g004.webp | 978e0d77a750f97ed623838193b1706650b1ddfda0bc7d3dbb4699ce34ada846 |
| ...g005.webp | c90a24aa2b7291e814cbfee6f7735014d03e3022f3448f2b76d4ebbe2fe8c57f |
| ...g006.webp | 31b4bc97617a8d5366bc4a4edad0fad6d3905cf9ee560f210fc1117b406bc2b6 |
| ...g007.webp | 3586dcbd5827357a37c70bcb4a6bf1dd9588b21b922022f93f5a6046d6568fd9 |

I viewed each webp as a 1600-px PNG made with `convert` (PNG sha256 prefixes: g3 5e334a33, g4 62bfcf45, g5 f0c86b57, g6 a4bba1c1, g7 686f9ec3). I also viewed crops of Fig 3B chromosome 16 and of Fig 7A around WWOX.

COULD NOT BE COMPLETED
- Figures 1 and 2 are not held. I listed files/fulltext, files/figures and files/supplement* and searched by identifier and filename. Only g003 to g007 exist for this PMID. I have only their legends from the XML.
  - Fig 1 is the CNV-classification flowchart.
  - Fig 2 is the facial photographs, labelled P1, P2, P3, P4, P5, P7, P11, P12, P14, P15, P17, P18 in the legend. P8 is not in that list.
- Table 3 and the text were read from the XML. Tables are not images.

SUPPLEMENT: Supplementaryfile1.docx is a STROBE checklist only. It has 1 table (header plus items 1 to 18, 19 rows), 78 paragraphs, no images and no genomic data. Every item points to a manuscript section. It adds nothing about P8 or WWOX.

VALUES READ
Figures were read by eye. I made no pixel measurement of the figures here. The replicate unit is the patient (n = 1 per panel). The species is human for every panel.
- Fig 3A (workflow): "107 patients with CCA; Karyotype (n=107) 4 abnormal (3,7%); Array CGH (n=54) 10 CNV pathogenic/Likely Pathogenic (18,5%); CNV confirmation FISH (7 cases), MLPA NSD1 exon 2 in P10; WES (n=6) 4 VUS".
  - The text and Table 4 say 3 abnormal karyotypes (2.8%), so Fig 3A disagrees with the paper's own text.
  - The WES box lists variants only for P16 (WLS and ERCC8), P17-P18 (VPS39) and P7 (MID1). The other two WES patients are not identified anywhere.
- Fig 3B (ideogram): a red star (pathogenic or likely pathogenic) sits on the distal long arm of chromosome 16, consistent with P8. I counted 9 red stars against 10 pathogenic patients.
- Fig 4: karyotype panels for P5, P11 and P14 only. No P8 panel.
- Fig 5: FISH panels P1, P2 (twice), P3, P4, P6, P11 and P14, which is 7 patients. No P8 panel.
- Fig 6: array-CGH and MLPA montage with P1, P2, P3, P5, P6 (two images), P7, P9, P10, P11, P12-13, P14, P15 (two images), P16 and P17. There is no P8 profile and no P4 profile. The legend also omits P4 and P8.
- Fig 7: STRING and GeneMANIA networks of cohort genes. This is exploratory context (the text calls it "exploratory"), not evidence.
  - STRING panel A shows WWOX linked to AFG3L2 by several line colours and to CYFIP1 by a magenta (experimentally determined) line.
  - ANKRD11 is linked to ZNF778, which links to CDH15 and then to a node labelled CDH1.
- Table 3, P8 row (cell-wise from the XML):
  - Sex/age: M1 M. The abbreviations list gives M as both Male and Months, so this reads as male, 1 month.
  - CCM: "Dysgenesis of CC". Phenotype: "Hydrocephaly Microcephaly".
  - Karyotype/FISH/MLPA: "46,XY".
  - Array: "Arr16q(74,718,513 87,891,103)x1" (hg18).
  - CNV (G/L): "L". Size: "L" (no size printed).
  - Genes: WWOX ANKRD11 ZNF778 CDH15 CDH13.
  - Inheritance: De novo. ACMG: P. ClinVar: SCV007596007.
  - Interpretation: "Consistent with 16q23q24 microdeletion syndrome, including corpus callosum dysgenesis".
- Computed over the printed interval: 87,891,103 minus 74,718,513 = 13,172,590 bp, i.e. 13.17 Mb.
- Where P8, WWOX, ANKRD11 and CDH13 occur in the XML body (searched now, 2026-11-26, in Python between "Introduction" and "Acknowledgments"):
  - `\bP8\b` appears 3 times: the Fig 6 patient list sentence, the Table 3 row, and the Discussion list.
  - WWOX, ANKRD11 and CDH13 each appear once, in the Table 3 row.
  - "follow-up" appears 0 times.
  - Epilepsy appears in the rows of P4, P11 and P12 but not in P8's.
  - There is no per-patient text about P8.

CONSUMER SENTENCES (claim_registry_current.md line 679, verbatim, split by me; the labels S1 to S6 are mine)
S1: "🔴 **A third heterozygous observation with a phenotype — intake wave 7, 2026-10-04 (`CC-20261004W7-B-CNV-CARRIER-01`); again not a haploinsufficiency datum.**"
- CORRECT. It is an interpretation label. The source gives x1, de novo and a pathogenic call, and no allele-level or haploinsufficiency datum.

S2: "[[paper_registry_current#PAPER 208]] (PMID 42807679): a de novo heterozygous ~13 Mb 16q23q24 deletion including WWOX, ANKRD11 and CDH13 in a male infant with callosal dysgenesis, hydrocephaly and microcephaly (no epilepsy recorded)."
- CORRECT. Table 3 P8 gives "De novo", x1, genes of interest WWOX/ANKRD11/CDH13, M 1 month, "Dysgenesis of CC", "Hydrocephaly Microcephaly".
- The "no epilepsy recorded" negative is verified by my search now (2026-11-26; queries `\bP8\b`, `[Ee]pilep`, `follow[- ]?up` over the XML body).
- ADD (loose): ACMG class P, ClinVar SCV007596007, age 1 month. The paper's interpretation is "Consistent with 16q23q24 microdeletion syndrome".
- Caveat: "including WWOX, ANKRD11, CDH13" rests on the paper's "Genes of interest" cell, not on a coordinate check by the paper.

S3: "What was examined in the carrier: karyotype and array-CGH (hg18); inheritance."
- INCOMPLETE (loose).
- Karyotype was printed as 46,XY at 450 to 550 bands. P8 has no FISH or MLPA entry and no panel in Fig 4, 5 or 6.
- "De novo" is a cell that appears in all 17 Table 3 rows. The Methods say inheritance is assessed "when parental samples were available". The Limitations say "parental segregation studies were incomplete". The paper does not state whether P8's parents were tested.
- Replacement: "Examined in P8 (Table 3): a normal 46,XY karyotype and array-CGH (hg18; Arr16q(74,718,513 87,891,103)x1); inheritance is printed as 'De novo', but the paper does not state that P8's parents were tested, and no array, FISH or karyotype panel for P8 is shown (Figs 4 to 6)."

S4: "**Not examined:** the remaining WWOX allele (exome was done in six other patients), RNA, protein, follow-up."
- INCOMPLETE, and strict candidate for the parenthesis "six other patients".
- The paper says WES was done in six selected patients "carrying CNVs and/or presenting parental consanguinity". It names only four (P7, P16, P17, P18, Table 1) and says the other two had no clinically relevant variants. It never says who they are, so P8 cannot be excluded. Table 3's "+/- WES" key is not applied to any row. The "-" in P7's row sits in the genes cell.
- No RNA, protein or follow-up for P8 appears anywhere (searches above). That part is CORRECT.
- Replacement: "(exome was done in six selected patients, four named in Table 1 (P7, P16, P17, P18) and two not identified; whether P8 was one of the two is not stated)".

S5: "Dozens of genes are deleted, ANKRD11 among them, so the phenotype neither fires nor refutes the trigger above for WWOX."
- ANKRD11 being in the interval is CORRECT per the Table 3 gene list.
- "Dozens" is NOT ASSESSABLE from the class. The paper gives no gene count, only five "genes of interest". It is the reader's annotation.
- The inference clause is labelled INFERENZA and is not testable here.

S6: "⚠️ **Integrator amendment (blind audit):** the source's Table 3 states **no size** for this patient's deletion — its `CNV (G/L)` and `Size` cells both read `L` — so the ~13 Mb figure is derived from the printed hg18 interval, not quoted from the paper."
- CORRECT, verified cell-wise (P8: "L", "L"). The derived value is 13.17 Mb.

The rest of line 679 (the PAPER 209 / PMID 41345172 gnomAD sentence) is not about this record. I did not assess it.

Other repository places that name 42807679 are pointers only, not assessed: paper_registry_current.md lines 9869 and 9885 (PAPER 208), literature_tracking_log_current.md lines 14164 to 14201, reading_state.md line 1974, and commit_candidates CC-20261004W7-B-*. I did not open any earlier reader's notes.

ADDS that no consumer holds (Record 1)
1. P8 has no panel in any held figure (Figs 3 to 7), and the Fig 2 legend lists no P8. The WWOX-bearing deletion is evidenced only by one Table 3 row. The array profile is shown for other patients.
2. P8's karyotype prints as normal 46,XY at about 450 to 550 bands, against a printed 13.17 Mb interval. Fig 3A shows "4 abnormal (3,7%)" while the text and Table 4 say 3 (2.8%). The paper never reconciles this. I draw no inference about P8 from it.
3. The abstract and Results give the cytoband as 16q23.1–q24.3, while Table 3 prints only "Arr16q".
4. The paper declares no WWOX-specific analysis. WWOX appears only in the Table 3 gene list and as a node in Fig 7.

====================================================
RECORD 2. PMID 41254692 (Qin 2025, J Transl Med). Consumer: discovery_ledger_current.md DL-REPO-003 (lines 3781 to 3796).
====================================================
OPENED (sha256, in full)
| file | sha256 |
|---|---|
| fulltext/PMID41254692_Qin2025_PMC.xml | f2aef589deeb92bdbf3ba2c20ecd7c3e89c504bb4293a20219ca217d6c59292a |
| supplements/PMID41254692/12967_2025_7301_MOESM1_ESM.xlsx | c817de13b411f83612db7ad2ee467ef75b66763fd69a755f4dc6020dea880c31 |
| supplements/PMID41254692/12967_2025_7301_Fig7_HTML.jpg | 7d8bca7d656d122afbfa6a9c67cdcad5734d915ac86cfbf015172958d473eda1 |
| supplements/PMID41254692/MOESM1_TableS7_rows.txt (derived text; I used it only to compare with my own parse of sheet 7) | 9aae8a1fa3813b18e4fab28cad2f74f138378cc202b69cea1e1999b18407cc81 |
| supplements/PMID41254692/s.zip | 8f1639ea849695b7e337d72ad326d35b18dee2238867a8ac138847f446ede453 |

FILES HELD THAT THE DISPATCH SAID WERE NOT HELD. The dispatch said main Figs 1 to 6 are not held. They are inside s.zip, which I extracted to scratch and read. Its contents:
- Fig1 to Fig7 .jpg and .gif thumbnails, and two equation .gif files.
- The xlsx inside is byte-identical to the loose xlsx (`cmp` confirmed).
- The Fig7 jpg inside has the same sha256 as the loose one.
- sha256 of the zip's jpgs:

| figure | sha256 |
|---|---|
| Fig1 | b0aad322be381e18cb1a96888c1a05118a09f372442cab274c5367fa8a2c90d8 |
| Fig2 | 94ab030dd43e6e292616ec0d27db806f31d22f63e79b872b496d9d340fd57bcc |
| Fig3 | e449a60674760a6facf18fb73607aecf68ca8838c96b835a39abcbadded7bd8e |
| Fig4 | 21ab6048e362e69123ba16cf0257474c656b124655f5265fbed575ced9303b9b |
| Fig5 | 90a9c0f068d1eee55a45bd415b131d7979678e5b176c3d23a0986137f3820638 |
| Fig6 | 1e794fc22e77928fb29b89ba4e0e7346e8f8b4ee371a09938cd99016b4ecbc8c |
| Fig7 | 7d8bca7d656d122afbfa6a9c67cdcad5734d915ac86cfbf015172958d473eda1 |

I viewed Figs 1 to 7 as 2x upscales. The source jpgs are 669 px wide, so they are low resolution. The .gif thumbnails (hashes in the scratch folder) and the two equation gifs were not viewed. There is no files/figures/PMID41254692 folder and no files/supplement/PMID41254692 folder. Only s.zip carries the main figures.

WORKBOOK 12967_2025_7301_MOESM1_ESM.xlsx, 7 sheets. All rows were parsed, and counts include the title and header rows.
| sheet | title (from cell A1) | rows | data rows |
|---|---|---|---|
| Table S1 | blood eQTL-MR | 3608 | 3605 (IVW 3123, Wald 482; 59 with FDR < 0.05) |
| Table S2 | plasma pQTL-MR, deCODE | 1178 | 1175 (7 with FDR < 0.05) |
| Table S3 | replication, UKB-PPP | 1289 | 1286 (14 with FDR < 0.05) |
| Table S4 | phenome-wide MR of WWOX | 856 | 853 (all IVW) |
| Table S5 | phenome-wide MR of THBS2; cell A1 reads "Table S4 Phenome-wide MR analysis of THBS2" | 855 | 852 |
| Table S6 | replication of THBS2 phenome-wide findings, UKB-PPP | 102 | 99 |
| Table S7 | Drug prediction based on drug-gene interactions | 13 | 11 |

The row counts for S1 to S3 and S6 match the text.

TABLE S7 in full (cols: Chemical name | ID | Gene | Organism | Interaction actions | Reference PMID). Every Organism cell is "Homo sapiens".
| row | chemical | ID | gene | action | PMIDs |
|---|---|---|---|---|---|
| 3 | Arsenic Trioxide | D000077237 | WWOX | Decreases expression | 20458559 |
| 4 | jinfukang | C544151 | WWOX | Decreases expression | 27392435 |
| 5 | Sunitinib | D000077210 | WWOX | Decreases expression | 31533062 |
| 6 | Valproic Acid | D014635 | WWOX | Decreases expression | 23179753\|24935251\|26272509\|27188386\|28001369 |
| 7 | Vorinostat | D000077337 | WWOX | Decreases expression | 27188386 |
| 8 | Calcitriol | D002117 | THBS2 | Increases expression | 26485663 |
| 9 | GSK1210151A | C568713 | THBS2 | Increases expression | 26644586 |
| 10 | Ifosfamide | D007069 | THBS2 | Increases expression | 25596134 |
| 11 | JQ1 compound | C561695 | THBS2 | Increases expression | 26644586 |
| 12 | Valproic Acid | D014635 | THBS2 | Increases expression | 29154799 |
| 13 | Vorinostat | D000077337 | THBS2 | Increases expression | 27188386 |

My parse matches the derived rows txt (cell for cell).

Other WWOX values, read cell-wise from the xlsx:
- S1 row 24: WWOX, IVW, nSNPs 29, beta −0.6288, P 1.13e-4, OR 0.533, FDR 0.0195. This passes FDR and matches text Table 1 (PPH4 0.619 comes from the text).
- S2 row 56: WWOX, IVW, nSNPs 3, beta −2.147, P 7.20e-3, OR 0.1168, FDR 0.1595. This does not pass FDR; the text says 0.160.
- S4: 853 WWOX phenotypes. Minimum FDR 0.130. FDR < 0.05 in 0 rows. Nominal P < 0.05 in 94 rows.
- S5: THBS2 852 phenotypes, with 104 rows at FDR < 0.05.
- S6: 99 rows, with 67 at FDR < 0.05. The text says "99 phenotypes ... 63 replicated". My counts (104 and 67) are not reconciled with those numbers. I did not test why (thresholds or pleiotropy filter).
- THBS2 in S1 (row 1313): FDR 0.726, so no eQTL-level signal. THBS2 in S2: rows 4 and 280 (row 4 FDR 3.8e-7).

FIGURES read by eye (jpg 669 px, species human, cohort GWAS and blood data)
- Fig 1: flowchart. The MR outcome is FinnGen R12 mature T/NK-cell lymphoma, cases = 440, controls = 378,749. The exposures are eQTLGen (n = 31,684), deCODE (n = 35,559) and UKB-PPP (n = 54,219).
- Fig 2B: WWOX sits in the OR < 1 half, at about −log10 FDR 1.7. The replicate unit is genes.
- Fig 3A: WWOX appears among the labelled pQTL points. Fig 3B and C are THBS2.
- Fig 4A: WWOX SMR scatter with eQTL effect against GWAS effect.
- Fig 5A: WWOX expression, control against tumour. By pixel on the 669-px jpg (axis calibrated from label positions, about ±0.1 units, no n in the legend), WWOX is about 5.2 in control and 4.7 in tumour, marked "**". THBS2 is about 4.1 in control and 5.9 in tumour, marked "****". Error bars are SEM. The legend names GSE19067 for the main data and GSE90597 for the validation set.
- Fig 6A: WWOX phenome-wide. Every point is below the FDR 0.05 line (dashed at −log10 = 1.3), maximum about 0.9. Fig 6B is THBS2.
- Fig 7, the one figure held outside the zip: docking poses, one pose per compound, in silico with no replicates.
  - Panel A, WWOX: vorinostat −5.7 kcal/mol (ARG-7, GLN-18, ALA-9, GLY-10), valproic acid −4.2 (ALA-9, GLY-10, ASP-11), sunitinib −6.5 (ARG-7, ALA-9, GLY-10, ASP-11). The structure shown is a small N-terminal fragment.
  - Panel B, THBS2: vorinostat −6.7, valproic acid −4.8, JQ1 −7.4, ifosfamide −5.3, GSK1210151A −8.0, calcitriol −7.9. Residues recur at LYS-1166.
  - All values match the text.

CONSUMER SENTENCES (discovery_ledger_current.md, verbatim; the labels S1 to S6 are mine)
S1, line 3781, title: "A curated database says valproate LOWERS WWOX expression in human cells, and the paper that carries the row states the opposite: the direction is a reading debt, not a lead".
- CORRECT. S7 row 6 says "Decreases expression" with organism Homo sapiens. The Results say "potentially increasing WWOX expression", and the Discussion says HDACi "can simultaneously upregulate WWOX". S7 gives no cell type.

S2, line 3786 (sentence 1): "[[paper_registry_current#PAPER 222]] (PMID 41254692) proposes raising WWOX as a therapeutic direction and names vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds that *«potentially increase»* WWOX expression."
- CORRECT in substance. The five compounds match the Results list.
- The quotation is not exact: the source wording is "potentially increasing WWOX expression" (and "potentially upregulate" in the preceding sentence). Trivial. Replacement quote: *«potentially increasing»*.

S3, line 3786 (sentence 2): "Its own deposited CTD export, Table S7, records **every one of those five WWOX rows as `Decreases expression`** in *Homo sapiens* — and every THBS2 row as `Increases expression`, again the opposite of the text's intent."
- CORRECT. Rows 3 to 7 and rows 8 to 13 verified above. "CTD" comes from the Methods, not from the sheet title.
- ADD (loose): the main text cites the compound list as "Additional file 1: Table S6", but in the held workbook S6 is the THBS2 UKB-PPP replication and the drug sheet is S7. The ledger's "Table S7" is right for the held file. The sheet numbering differs from the text citation, and sheet S5 labels itself "Table S4".
- ADD: the six THBS2 compounds in S7 are the same six the text lists as "potentially reducing THBS2", so the text inverts both genes.

S4, line 3786 (sentence 3): "🔴 **Two independent auditors verified this cell-wise on the deposited table and found exactly five WWOX rows, with no `Increases expression` row for WWOX anywhere in the sheet.**"
- CORRECT. My independent parse of S7 finds exactly 5 WWOX rows, 0 with "Increases". The count is also 0 for any non-S7 WWOX row of that wording, since the other sheets are MR tables.

S5, line 3786 (sentence 4): "The valproic-acid row cites five reference PMIDs: 23179753, 24935251, 26272509, 27188386, 28001369."
- CORRECT (row 6, pipe-separated).
- ADD: the vorinostat WWOX row (row 7) cites only 27188386, one of the four primaries already read, so the same primary decides that row too. Arsenic trioxide cites only 20458559, jinfukang only 27392435, and sunitinib only 31533062.

S6, line 3787: "The direction is a **database annotation**, not a measurement in this paper; four of the five primaries are now read (see the wave-9 entry below); the fifth is **unread**; cell type, dose, species and readout (transcript or protein) are unknown; CTD rows are extracted from cancer and toxicology experiments; and nothing connects an expression change in a cultured cell to a patient carrying two loss-of-function alleles, ..."
- "Database annotation, not a measurement in this paper": CORRECT.
- "Species ... unknown": INCOMPLETE, a loose candidate. S7 col D states "Homo sapiens" for every row. Cell type, dose and readout are indeed absent from S7, and "Decreases expression" carries no transcript or protein tag.
  - Replacement: "cell type, dose and readout (transcript or protein) are not stated in Table S7, whose organism column reads Homo sapiens".
- "CTD rows are extracted from cancer and toxicology experiments": NOT ASSESSABLE from this class. S7 has no experiment or tissue field.
- The "four of five primaries read" and "fifth unread" clauses are outside the class.

S7, line 3787 (last sentence): "The paper's own protein-level WWOX association does **not** survive multiple-testing correction (FDR-corrected P = 0.160)."
- CORRECT. S2 row 56 gives P 7.2e-3, FDR 0.1595, from 3 SNPs, and the text says 0.160.
- ADD (loose): the WWOX expression-level association does pass FDR (S1 row 24: OR 0.533, FDR 0.0195; text Table 1: PPH4 0.619). The protein level could not be replicated, because WWOX is absent from UKB-PPP (text). A reader of the sentence alone could take the whole WWOX signal as non-significant.

Also checked: paper_registry_current.md PAPER 222, lines 10163 to 10182, repeats the S7 contrast and "FDR-corrected P = 0.160". Both are consistent with S3 and S7 above. I did not otherwise assess it.

ADDS that no consumer holds (Record 2)
1. The workbook carries MR tables for the other sheets. The WWOX phenome-wide result: 0 of 853 phenotypes at FDR < 0.05 (S4, Fig 6A).
2. The MR outcome is a lymphoma GWAS with 440 cases, using blood eQTL instruments (WWOX: 29 SNPs) and deCODE plasma pQTL instruments (WWOX: 3 SNPs). It models common-variant expression, not any WWOX allele or neural tissue.
3. Fig 7 docks valproic acid to a WWOX N-terminal fragment at −4.2 kcal/mol, the weakest of the three WWOX ligands. Docking is in silico and one pose per compound, and it says nothing about expression direction.
4. Fig 5A shows lower WWOX expression in tumour than control (about 5.2 against 4.7 by pixel; n not given).
5. S5 and S6 row counts (104 and 67 at FDR < 0.05) are not reconciled with the text's 99 and 63. I did not test why, and I make no claim that the text is wrong.

====================================================
SUMMARY FOR THE MATCHING RULE (reader's verdicts; none checked by a blind reader)
====================================================
- Strict candidates (for SCI to check on the original): Khadija S4 "(exome was done in six other patients)", unsupported as written. Qin S6 "species ... unknown", a low-priority candidate: the sheet states Homo sapiens, but the ledger likely means the species of the primary experiments.
- Loose candidates:
  - Khadija S3, inheritance and parental testing not stated.
  - Khadija S2, age, ACMG class and ClinVar accession missing.
  - Qin S3, the S6/S7 numbering shift.
  - Qin S5, the vorinostat row's PMID.
  - Qin S7, the eQTL-level association passes FDR.
- Everything else is CORRECT or NOT ASSESSABLE.
- Dated searches for negatives: all keyword searches were run 2026-11-26 over the held XML text (the 2026-11-26 date comes from the task header). Queries: `\bP8\b`, `WWOX`, `ANKRD11`, `CDH13`, `[Ee]pilep`, `follow[- ]?up`, RNA/expression, parental, segregation, haploinsuff. Search results are in the Record 1 values section.

FILES OPENED (all read-only)
- /home/desktop/legend-development/files/fulltext/PMID42807679_Khadija2026_PMC.xml
- /home/desktop/legend-development/files/fulltext/PMID42807679_Khadija2026_supplement/Supplementaryfile1.docx
- /home/desktop/legend-development/files/figures/PMID42807679/fgene-17-1815268-g003.webp, g004.webp, g005.webp, g006.webp, g007.webp
- /home/desktop/legend-development/files/fulltext/PMID41254692_Qin2025_PMC.xml
- /home/desktop/legend-development/files/supplements/PMID41254692/12967_2025_7301_MOESM1_ESM.xlsx
- /home/desktop/legend-development/files/supplements/PMID41254692/12967_2025_7301_Fig7_HTML.jpg
- /home/desktop/legend-development/files/supplements/PMID41254692/MOESM1_TableS7_rows.txt
- /home/desktop/legend-development/files/supplements/PMID41254692/s.zip (extracted in scratch)
- /home/desktop/legend-development/.claude/worktrees/sci_at_20261126/disease-models/wwox/registries/claim_registry_current.md (CLAIM 032, lines 659 to 683)
- /home/desktop/legend-development/.claude/worktrees/sci_at_20261126/disease-models/wwox/research/discovery_ledger_current.md (lines 3781 to 3796)
- /home/desktop/legend-development/.claude/worktrees/sci_at_20261126/disease-models/wwox/registries/paper_registry_current.md (PAPER 222, lines 10163 to 10182)
- /home/desktop/legend-development/.claude/worktrees/sci_at_20261126/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv295_one_consumer_batch_sci_20261126/PREREG_ADV295_SCI_20261126.md (two named sections only)
- /home/desktop/legend-development/.claude/worktrees/sci_at_20261126/framework/protocols/delegation_budget.md (§2 and §7)
- Scratch (derived, not sources): /home/desktop/.claude/jobs/c6d4dd83/tmp/adv295_a/ (k.txt, q.txt, docx.xml, xl.py, run1.py to run4.py, img/, qimg/, zip/)
