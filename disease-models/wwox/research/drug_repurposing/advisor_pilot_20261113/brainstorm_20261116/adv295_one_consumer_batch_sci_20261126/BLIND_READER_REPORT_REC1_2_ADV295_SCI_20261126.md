BLIND SENTENCE-LEVEL READ, ADV-295 block 1, records 1 and 2 (reader: sonnet, high effort; date 2026-11-26). Hypothesis-level reading of public literature; nothing here is medical advice.

Conventions. "Matching rule" read as given: strict = false or unsupported as written, and a blind reader returns MUST CHANGE. A negative counts only with a dated search whose query and file I state. Plain-text conversions of the two PMC XML files are in /home/desktop/.claude/jobs/8fe7aef9/tmp/blind12/out/ (k.txt = Khadija, q.txt = Qin). Every search below was run on 2026-11-26, one keyword per search, case-insensitive substring unless marked -w (whole word).

====================================================================
(1) STATEMENT TABLE
====================================================================

RECORD 1: PMID 42807679 (Khadija 2026), CLAIM 032 line 679. P8 is the patient of interest.

Source facts used (Table 3 of the PMC XML, raw cell-wise, row P8):
- Sex/Age cell: "M / 1 M". The table's own legend defines "M: Months, M: Male"; the karyotype cell reads 46,XY.
- CCM cell: "Dysgenesis of CC". Phenotype cell: "Hydrocephaly / Microcephaly".
- Karyotype/FISH/MLPA cell: "46,XY".
- Array CGH cell: "Arr16q(74,718,513 / 87,891,103)x1". The two numbers are separated by a line break and the hyphen is missing.
- CNV (G/L) cell: "L". Size cell: "L".
- Genes of interest cell: WWOX, ANKRD11, ZNF778, CDH15, CDH13.
- Inheritance cell: "De novo". ACMG/AMP cell: "P". ClinVar cell: "SCV007596007".
- Clinical interpretation cell: "Consistent with 16q23q24 microdeletion syndrome, including corpus callosum dysgenesis".

| id | verbatim statement | verdict | grounds |
|---|---|---|---|
| R1-S01 | "A third heterozygous observation with a phenotype — intake wave 7, 2026-10-04 (`CC-20261004W7-B-CNV-CARRIER-01`)" | OUT OF SCOPE | Repository bookkeeping; no statement about the paper. |
| R1-S02 | "again not a haploinsufficiency datum." | NO CHANGE | Interpretive. Table 3 gives only a multi-gene "Genes of interest" list for P8. The paper makes no WWOX-specific attribution (grep -w WWOX in k.txt: only line 209, the Table 3 P8 gene list, and line 470, the glossary). |
| R1-S03 | "a de novo heterozygous ~13 Mb 16q23q24 deletion" (de novo part) | ADD | Table 3, P8, Inheritance cell: "De novo". But the Inheritance cell reads "De novo" in all 17 rows P1–P17. The Methods say inheritance was assessed "when parental samples were available" (2.4.3) and give no parental-testing description for P8. The P8 array string lacks the "dn" suffix that P1–P3 carry. Evidence level to add: author-reported in Table 3, basis not described. |
| R1-S04 | "heterozygous" | NO CHANGE | Array "x1" at an autosomal locus = one copy. The word "heterozygous" is the consumer's, not the paper's, and is a fair inference from x1. |
| R1-S05 | "~13 Mb 16q23q24 deletion" | NO CHANGE | Printed hg18 interval 74,718,513 to 87,891,103 gives 87,891,103 − 74,718,513 = 13,172,590 bp. Cytoband: Table 3 interpretation "16q23q24 microdeletion syndrome"; abstract lists "16q23.1–q24.3". No size for P8 anywhere in the paper (see S17). The sentence says "~", and the integrator amendment in the same line says derived. |
| R1-S06 | "including WWOX, ANKRD11 and CDH13" | NO CHANGE | Table 3 P8 Genes-of-interest cell lists all three (plus ZNF778, CDH15). The held sources contain no gene coordinates, so I cannot check that each gene lies wholly inside the interval. The paper only lists them as "genes of interest". (My unverified recollection, not used for the verdict: ANKRD11 sits near the distal end of the interval.) |
| R1-S07 | "in a male infant" | NO CHANGE | Table 3: Sex/Age "M / 1 M"; karyotype 46,XY. |
| R1-S08 | "with callosal dysgenesis, hydrocephaly and microcephaly" | NO CHANGE | Table 3 CCM "Dysgenesis of CC"; phenotype cell "Hydrocephaly, Microcephaly". |
| R1-S09 | "(no epilepsy recorded)" | NO CHANGE | grep "epilep" in k.txt: 12 hits; P8's table row contains none, and "Epilepsy" is printed in the P4 row. grep "P8": the text mentions P8 only in the list of 10 pathogenic patients (line 314) plus the Table 3 row. No individual narrative exists for P8, so "recorded" is accurate (Table 3 only). |
| R1-S10 | "What was examined in the carrier: karyotype and array-CGH (hg18); inheritance." | NO CHANGE | Karyotype cell "46,XY" (all 107 were karyotyped, 2.4.1); array cell with hg18 (Methods 2.4.3: "reported according to the hg18"); Inheritance cell "De novo". See S03 for the basis caveat. |
| R1-S11 | "Not examined: the remaining WWOX allele" | NO CHANGE | Negative verified: grep -w WWOX in k.txt returns only the Table 3 P8 gene list and the glossary. WWOX appears in Fig 7 only as a predicted-interaction node (STRING/GeneMANIA). No WWOX sequence result is reported. |
| R1-S12 | "(exome was done in six other patients)" | ADD | Paper: WES "performed in six selected patients" (2.4.5). Only four are identified (P7, P16, P17, P18; Table 1 and Table 2). The other two are "no clinically relevant sequence variants" (3.4) and unnamed. Table 3 legend defines "+: explored by WES, -: not explored by WES", but P8's row carries no mark. Whether P8 was one of the two unnamed exome patients cannot be decided. "Other" is therefore not supported; borderline MUST CHANGE, but not shown false. |
| R1-S13 | "**Not examined:** ... RNA, protein, follow-up." | NO CHANGE | Negatives verified: grep -w RNA in k.txt gives only the glossary (line 475). grep -w "follow-up" gives 0 hits. grep -w mRNA gives 0 hits. grep -w protein gives only the HGVS-protein column header, gene-function discussion and the interaction-network alt text, never a P8 measurement. Methods are limited to karyotype, FISH (24 patients), array-CGH (54), MLPA (P10 only), WES (6). |
| R1-S14 | "Dozens of genes are deleted" | UNSETTLED | No gene count in the paper. Table 3 lists five genes of interest only. Missing: a gene annotation of hg18 chr16:74,718,513–87,891,103, which is not a held source. |
| R1-S15 | "ANKRD11 among them" | NO CHANGE | Table 3 P8 gene list (and the glossary line 396). Same boundary caveat as S06. |
| R1-S16 | "so the phenotype neither fires nor refutes the trigger above for WWOX" | NO CHANGE | Inference. "The trigger above" is not defined in the packet. Consistent with the paper, which assigns no gene-level cause and writes "the presence of a pathogenic CNV does not imply a uniform phenotype" (5.2). |
| R1-S17 | "the source's Table 3 states **no size** for this patient's deletion — its `CNV (G/L)` and `Size` cells both read `L`" | NO CHANGE | Verified on the raw XML: P8 CNV (G/L) = "L" and Size = "L". Fig 6 caption lists P1, P2, P3, P5, P6, P7, P9, P10, P11, P12-P13, P14, P15, P16, P17; no P8 and no P4. The text gives no P8 size. |
| R1-S18 | "so the ~13 Mb figure is derived from the printed hg18 interval, not quoted from the paper" | NO CHANGE | Recomputed 13,172,590 bp (see S05). Note the printed interval has a line break and no hyphen; the split at the comma groups, 74,718,513 and 87,891,103, is unambiguous. |
| R1-S19 | "**Not a dosage datum either way:** the common WWOX intronic deletion of (wikilink to PAPER 209 elided by the delegate; the target text is not reproduced here) (PMID 41345172; gnomAD AF 0.339, **1447 homozygotes**) removes no exon ..." (plus the PREMISE tag) | OUT OF SCOPE | About another paper; the packet itself says to ignore it. |

RECORD 2: PMID 41254692 (Qin 2025), DL-REPO-003.

Source facts used (deposited workbook 12967_2025_7301_MOESM1_ESM.xlsx):
- Sheet "Table S7", titled "Drug prediction based on drug-gene interactions", dimension A1:F13. Header row 2: Chemical name, Chemical ID, Gene, Organism, Interaction actions, Reference PMID.
- Rows 3–7 are the five WWOX rows: Arsenic Trioxide, jinfukang, Sunitinib, Valproic Acid (F6 = 23179753|24935251|26272509|27188386|28001369), Vorinostat. Every one has Organism = Homo sapiens and Interaction actions = Decreases expression.
- Rows 8–13 are the six THBS2 rows: Calcitriol, GSK1210151A, Ifosfamide, JQ1 compound, Valproic Acid (F12 = 29154799), Vorinostat. Every one has Homo sapiens and Increases expression.
- There are no hidden rows or columns, and no merged cells.
- The workbook copy inside s.zip has an identical SHA-256 prefix (c817de13...).
- The other 6 sheets are MR results: S1 and S2 (eQTL and pQTL MR), S3 (UKB-PPP replication), S4 (WWOX phenome-wide), S5 (THBS2 phenome-wide), S6 (THBS2 phenome-wide replication in UKB-PPP).
- Numbering note: the paper text cites the drug screen as "(Additional file 1: Table S6)", but in the deposited file the drug sheet is "Table S7". The consumer's "Table S7" matches the workbook.

| id | verbatim statement | verdict | grounds |
|---|---|---|---|
| R2-S01 | "A curated database says valproate LOWERS WWOX expression in human cells" (DL title, line 3781) | ADD | Sheet "Table S7", row 6: Organism = "Homo sapiens", Interaction actions = "Decreases expression". The sheet gives organism only. Paper Methods: "restricted to interactions documented in human tissues". Neither source says "cells" nor names a cell or tissue type. |
| R2-S02 | "and the paper that carries the row states the opposite" | NO CHANGE | Results: "The compounds potentially increasing WWOX expression include Vorinostat, Valproic Acid, Sunitinib, Jinfukang, and Arsenic Trioxide." Discussion: "HDACi (Vorinostat and Valproic Acid) can simultaneously upregulate WWOX expression". |
| R2-S03 | "the direction is a reading debt, not a lead" | OUT OF SCOPE | Repository framing. |
| R2-S04 | "[PAPER 222] (PMID 41254692) proposes raising WWOX as a therapeutic direction" | NO CHANGE | Abstract: "WWOX was identified as a protective factor"; Table 1 WWOX eQTL: OR 0.533 (0.388–0.734), FDR 0.019, PPH4 0.619; screening for compounds that "potentially upregulate WWOX expression". Note: the phenome-wide paragraph says "WWOX inhibition may not lead to widespread adverse effects", so the paper's own wording is inconsistent. |
| R2-S05 | "names vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds that" | NO CHANGE | Same five names in the Results sentence quoted under S02. |
| R2-S06 | "*«potentially increase»* WWOX expression" | MUST CHANGE (quotation form only; substance correct) | The guillemets claim a verbatim quote. grep "potentially increas" in q.txt: only "potentially increasing WWOX expression" (line 169). grep "potentially upregulate": "potentially upregulate WWOX expression". The phrase "potentially increase" does not occur. |
| R2-S07 | "Its own deposited CTD export, Table S7, records **every one of those five WWOX rows as `Decreases expression`** in *Homo sapiens*" | NO CHANGE | Table S7 C3:C7 = WWOX, E3:E7 = "Decreases expression", D3:D7 = "Homo sapiens". Shared strings: "Decreases expression" is used only for these 5 rows. (The paper's text calls this table S6; see the numbering note above.) |
| R2-S08 | "and every THBS2 row as `Increases expression`, again the opposite of the text's intent" | NO CHANGE | Table S7 rows 8–13, 6 THBS2 rows, all "Increases expression". The text intends compounds "potentially reducing THBS2 expression" and lists six: Vorinostat, Valproic Acid, JQ1, Ifosfamide, GSK1210151A, Calcitriol. Six rows match six compounds. |
| R2-S09 | "Two independent auditors verified this cell-wise on the deposited table" | OUT OF SCOPE | Process claim about other readers. |
| R2-S10 | "found exactly five WWOX rows, with no `Increases expression` row for WWOX anywhere in the sheet" | NO CHANGE | Recounted by me: WWOX in C3:C7 only, 5 rows. The only "Increases expression" cells are E8:E13 and all are THBS2. |
| R2-S11 | "The valproic-acid row cites five reference PMIDs: 23179753, 24935251, 26272509, 27188386, 28001369." | NO CHANGE | F6 matches exactly. Caveat: there are two valproic-acid rows. The THBS2 one (F12) cites 29154799. The sentence needs "WWOX" to be unambiguous. |
| R2-S12 | "**This is recorded as a DEBT, not as evidence about valproate...**" | OUT OF SCOPE | Repository framing. |
| R2-S13 | "Valproate is an anti-seizure medicine used in WWOX-DEE patients, and `CC-20261003W3-A-VIGABATRIN-01` already records one L239R child ..." | OUT OF SCOPE | Not from this paper. The paper says only "Valproic acid, an antiepileptic drug". grep "epilep" in q.txt gives that one hit. |
| R2-S14 | "**If** the curated direction were right **and** transferred, a drug that lowers WWOX expression would matter in a disease of WWOX loss. **None of that is established here.**" | OUT OF SCOPE | Repository reasoning. The paper has no DEE or patient content (grep "encephalopathy": 0). |
| R2-S15 | "The direction is a **database annotation**, not a measurement in this paper" | NO CHANGE | The whole text read: CTD data were screened (Methods "Drug prediction and molecular docking"), and docking energies are computed (Fig 7, AutoDock Vina). Conclusion: "validate ... through in vitro and in vivo experiments to compensate for the limitations of computational analysis". No wet-lab experiment appears. |
| R2-S16 | "four of the five primaries are now read (see the wave-9 entry below); the fifth is **unread**" | OUT OF SCOPE | About other papers, per the packet. |
| R2-S17 | "cell type, dose, ... and readout (transcript or protein) are unknown" | NO CHANGE | Table S7 header has no cell-type, dose or readout column (Chemical name, Chemical ID, Gene, Organism, Interaction actions, Reference PMID). grep "dose" and "cell line" in q.txt: 0 hits. |
| R2-S18 | "... species ... are unknown" (same sentence as S17) | MUST CHANGE | Table S7 column "Organism" = "Homo sapiens" in all 11 rows, and the paper restricts the analysis to "interactions documented in human tissues". Line 3786 of the same record also states "in *Homo sapiens*". Unless "unknown" means "not yet read in the primaries", this contradicts the held source. |
| R2-S19 | "CTD rows are extracted from cancer and toxicology experiments" | UNSETTLED | Neither the paper nor Table S7 describes the experiment types behind the rows. The 5 reference PMIDs are not held in this packet. Missing: the primary papers. |
| R2-S20 | "nothing connects an expression change in a cultured cell to a patient carrying two loss-of-function alleles, where the question is **residual function of a specific allele** ..." | OUT OF SCOPE | Repository inference. The paper has no patient-allele content and does not mention cultured cells. |
| R2-S21 | "The paper's own protein-level WWOX association does **not** survive multiple-testing correction (FDR-corrected P = 0.160)." | NO CHANGE | Results: "OR = 0.117, 95% confidence interval (CI): 0.024–0.559, P = 7.2E-03 ... did not reach statistical significance after FDR correction (FDR-corrected P = 0.160)". Workbook sheet "Table S2" row 56: B56 = WWOX, E56 nSNPs = 3, H56 P = 7.1965E-03, I56 OR = 0.11682, J56 FDR = 0.15955, i.e. 0.160. Optional clarifier: the association is of genetically predicted plasma WWOX (deCODE, 3 SNPs) with T/NK-lymphoma risk. |

====================================================================
(2) CORRECTED SENTENCES (MUST CHANGE and ADD only)
====================================================================

- R1-S03 (ADD): "...a heterozygous (array x1) ~13 Mb 16q23q24 deletion that Table 3 lists as de novo (the Inheritance column reads 'De novo' in all 17 rows; the paper does not describe parental testing for this patient) ..."
- R1-S12 (ADD): "**Not examined (as far as the paper reports):** the remaining WWOX allele; no WWOX sequence result is given. Exome sequencing was done in six selected patients, of whom four are named (P7, P16, P17, P18) and two are not; whether P8 was one of them is not stated."
- R2-S01 (ADD): "A curated database (CTD, as exported in the deposited Table S7) lists valproic acid as decreasing WWOX expression in Homo sapiens (cell or tissue type not given), and the paper that carries the row states the opposite."
- R2-S06 (MUST CHANGE): "... names vorinostat, valproic acid, sunitinib, Jinfukang and arsenic trioxide as compounds *«potentially increasing WWOX expression»* (Results); the Discussion says HDAC inhibitors (vorinostat and valproic acid) 'can simultaneously upregulate WWOX expression'."
- R2-S18 (MUST CHANGE): "cell type, dose and readout (transcript or protein) are not given in the deposited sheet; the species is Homo sapiens in every row."

====================================================================
(3) COUNTS PER RECORD
====================================================================

Record 1: 19 statements.
- NO CHANGE 14: S02, S04, S05, S06, S07, S08, S09, S10, S11, S13, S15, S16, S17, S18.
- ADD 2: S03, S12.
- UNSETTLED 1: S14.
- OUT OF SCOPE 2: S01, S19.
- MUST CHANGE 0.
- Loose = 2 (ADD only), strict = 0 from this reader.

Record 2: 21 statements.
- NO CHANGE 10: S02, S04, S05, S07, S08, S10, S11, S15, S17, S21.
- ADD 1: S01.
- MUST CHANGE 2: S06 (quotation form only), S18 (species).
- UNSETTLED 1: S19.
- OUT OF SCOPE 7: S03, S09, S12, S13, S14, S16, S20.
- Loose = 3, strict candidates = 2. S06 is a pure misquote with correct substance; the integrator may treat it separately. S18 is the substantive one.

====================================================================
(4) WHAT I OPENED, WHAT I DID NOT, FAILURES
====================================================================

Opened:
- The PREREG "Matching rule" section only (awk, heading to the next "## ").
- The whole blind packet.
- Record 1: PMID42807679_Khadija2026_PMC.xml, converted to text and read in full (abstract through references). Raw XML of the Table 3 P8 row. Figures g003, g004, g005, g006, g007, all viewed. Supplementaryfile1.docx, extracted and read in full (body and one table): it is a STROBE checklist only, with no patient data. Figures 1 and 2 are not held; I read their captions and alt text in the XML.
- Record 2: PMID41254692_Qin2025_PMC.xml, read in full text up to the reference list (I did not read the references' content). The workbook, extracted into the tmp dir and parsed with zipfile and ElementTree: Table S7 in full (13 rows), the S1–S6 header rows, and the WWOX rows in S1, S2 and S3 (WWOX is absent from S3). 12967_2025_7301_Fig7_HTML.jpg (viewed). s.zip extracted: file list and SHA-256 compared (workbook copy identical); I viewed Fig2 only. Figs 1 and 3–6 and the .gif copies were not viewed; they bear on no statement.

Not opened:
- Any other file of the packet folder.
- Any registry, ledger, receipt, note, checkpoint or memory file; no repository search.
- PMID 42422765 in any form.
- MOESM1_TableS7_rows.txt, which sits in the held supplements folder but is not named by the packet.
- The reference PMIDs behind the CTD rows (not held). This is why R2-S19 is UNSETTLED.

Failures and limits:
- No network, no downloads, no e-mail address used.
- PIL, openpyxl and unzip were absent. I used the Python zipfile module, ElementTree and my own sheet parser (scripts in /home/desktop/.claude/jobs/8fe7aef9/tmp/blind12_scripts/). The Read tool displayed the .webp figures directly.
- No gene coordinates are held, so whether ANKRD11 and the other genes lie wholly inside the P8 interval could not be checked.
- All extractions are under /home/desktop/.claude/jobs/8fe7aef9/tmp/blind12/. No file was written in the repository.
