# Blind verifier report, batch 2 call B (units U1 to U8), as delivered (2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high (stated in the dispatch), 8 statements as (statement, source, anchor), no candidate and no conclusion given; statements in `statements_batch2b.tsv`. Hand-back text below, unchanged except for this header and one redaction required by the public release gate (marked where it stands). Read-back (`session_model_census.py` on the delegate transcript): `claude-sonnet-5-5`, effort `high` on 25 of 25 turns, 28 tool uses, 27,936 output tokens, 119,812 subagent tokens in the notice (a total with context, not output), first-turn context 24,342. The delegate could not write a report file; this file is the saved hand-back.

---

**Blind source verification, units U1–U8, call 1**

I opened only the primary source files and my own extractions of them. I did not open anything under disease-models/ or ledger/. I did not open the READING_NOTE_20261121.md or FULLTEXT_READ_RECEIPT_20261121.json files in the 2026 supplement folder, because they are prior readings. I also did not open the *_derived.txt or *_review_derived.txt files in the 2021 assets folder.

Method: I extracted my own text from the PMC XML for 2021 and Breton, and read the 2026 fitz.txt and the original supplement File010/011/009 .txt. I rendered Supplementary Figure 1 and 2 pages from the supplement PDF, and looked at the 2026 Figure 1 image and 2021 Figures 2 and 3. I cross-checked the 2021 legends against the 2021 PDF text. No external requests were made. My scratch files are in /home/desktop/.claude/jobs/6739e4ff/tmp/b2/out1 (scripts/ and work/).

**Summary**

| Unit | Verdict |
|---|---|
| U1 | SUPPORTED |
| U2 | SUPPORTED, with qualifiers |
| U3 | SUPPORTED, with a qualifier |
| U4 | SUPPORTED |
| U5 | SUPPORTED. The family count of three and the siblings are inferred, not printed. |
| U6 | Mixed. The Figure 6 facts are SUPPORTED. The Supplementary Figure 10 "n=8" fact is OVERSHOOT. |
| U7 | SUPPORTED. The statement omits the genotypes, which are printed. |
| U8 | WRONG as worded. The anchor is the wrong legend, and "5 versus 8" is not a comparison. |

---

### U1: 2021 field potentials, 14 vs 14 slices, from 5 and 8 organoids, 3 batches

Source: Steinberg 2021 (EMBO Mol Med), human WiBR3 hESC-derived cerebral organoids, week 7, local field potential in slices.

| Fact | Verdict | Quote and locator |
|---|---|---|
| 14 slices WT vs 14 slices KO | SUPPORTED | "(WT: n = 14 slices, 5 organoids, and 3 batches; KO: n = 14 slices, 8 organoids, and 3 batches)". Figure 2 legend, panel B. The same string is in the PDF text. |
| From 5 and 8 organoids | SUPPORTED | Same quote. The bars in Figure 2C (image) are labelled "14(5)" and "14(8)", read as slices(organoids). The Figure 2C legend says "The numerals in all bars indicate the number of analyzed slices and organoids (i.e., slices (organoids))". |
| From 3 batches | SUPPORTED | Same quote. "3 batches" is given for both WT and KO. |

- Replicate unit: slice. Slices are nested in organoids, and the test is Welch's t-test on slices. The legend says this and does not mention nesting.
- The KO group is pooled and its clone composition is not printed for 2C. The Figure 2G legend says "WT line, 2 KO lines".
- The legend of Figure EV1 panels G and H repeats the same 14/5 and 14/8 numbers (for the 30–79.9 Hz range).
- No correction is needed.

### U2: 2021 cell-attached, 24 (parent), 41 (patient), 40 (rescued) neurons, from 4, 3, 3 organoids, one patient family

| Fact | Verdict | Quote and locator |
|---|---|---|
| 24 / 41 / 40 neurons | SUPPORTED | "Average firing rate over 24 neurons from WSM P COs (4 organoids), 41 neurons from WSM S COs (3 organoids), and 40 neurons from WSM S W-AAV organoids (3 organoids)". Figure 5 legend, panel C. Results repeats the 41, 24 and 40 counts. |
| From 4 / 3 / 3 organoids | SUPPORTED | Same quote. |
| One patient family | SUPPORTED | The whole group is "WSM": "the first family carries a c.517-2A>G splice site mutation… (referred to as WSM family)". The rescue is WSM S5 W-AAV3 / W-AAV6. |

- Replicate unit: neuron (cell-attached recording, 4 min each). The cells are nested in organoids, and the stats are a one-way ANOVA (Tukey) with the neuron as n. Species and system: human iPSC-derived cerebral organoids, week 7.
- "Parent" is two people pooled, the two parents of the family (printed with their individual identifiers, F1 and M2, and «collectively referred to as WSM P»); the role words of the delegate's verbatim quotation are redacted here for the public edition (gate rule PARENT_OF_ORIGIN_PAIRING). Patient clones S2 and S5 are pooled as WSM S, and which clones were recorded is not printed.
- The number of batches for the recordings is not printed.
- Appendix Fig S4E, the comparison of F1 against M2, is in the Appendix PDF, which I did not open.
- Optional fuller wording: "24 neurons from the two heterozygous parents (4 organoids), 41 from the homozygous son's lines S2/S5 (3 organoids), and 40 from S5 with WWOX re-expressed (3 organoids), all of the WSM family."

### U3: knockout organoids from at most two clones of one hESC line

| Fact | Verdict | Quote and locator |
|---|---|---|
| Two clones | SUPPORTED | "Two clones that showed consistent undetectable protein levels of WWOX… were picked… WWOX-KO line 1B (WKO-1B, from here on KO1) and WKO-A2 (from here on KO2)". Results, first section. The Figure EV1 legend says "Clone 1B (KO1) and clone A2 (KO2) were selected for the organoid generation". |
| One hESC line | SUPPORTED | "WWOX knockout (KO) clones of the WiBR3 hESC line using the CRISPR/Cas9 system". |
| "At most" | SUPPORTED | Some legends name 2 KO lines: Figure 2G ("WT line, 2 KO lines, and 2 KO lines infected with lenti-WWOX") and Figure EV1I ("WT and 2 KO lines"). Most legends say only "KO". |

- Qualifier: which clone supplied each pooled "KO" n is not printed in the Figure 1, 2B or 2C legends. "At most two" is the safe wording.
- Rescue lines: W-AAV is KO1 with WWOX in the AAVS1 locus ("KO1-AAV4 line… referred as W-AAV"), and lenti-WWOX is applied to KO1 and KO2.
- The Methods say "at least two hPSC lines used for each genotype (with the exception of the WiBR3 WT line)", so the WT is one parental line.
- The WiBR3 hESC-derived WT and KO organoids are in the 2021 paper only. The 2026 paper uses JH-iPS11 iPSC WT and KO clones (see U4).

### U4: 2026 week-7 cell-attached, 14–30 neurons per line, "one experiment"

Source: 2026 Brain (Steinberg), fitz.txt, Figure 1 legend, panel D.

| Fact | Verdict | Quote and locator |
|---|---|---|
| 14 to 30 neurons per line | SUPPORTED | "(WT: n= 30 neurons; WWOX-KO: n=30; WPM S: n=21; WPM D: n=21; WSM S: n=24; LM-iPS: n=14)". Per-line n, by line: WT 30, WWOX-KO 30, WPM S 21, WPM D 21, WSM S 24, LM-iPS 14. |
| Legend says one experiment | SUPPORTED | "…collected from one experiment." The phrase ends the sentence that gives the panel D n values. |

- Replicate unit: neuron, human iPSC-derived week-7 organoids. WT and WWOX-KO are JH-iPS11 lines (iPSC), per the Figure 1C title "(JH-iPS11)". The y-axis is "Spikes/Neuron".
- Organoid count per line is not printed in the legend or in the supplement methods I read. WCH S is not in panel D.
- The phrase "from one experiment" is in the same sentence as the n values. It is not stated for the other panels.
- The WWOX-KO clone (WKO-1C or WKO-2C) is not specified.

### U5: families

| Fact | Verdict | Locator and quote |
|---|---|---|
| 2021 patient-line rescue uses one family (plus a knockout hESC line) | SUPPORTED, printed | 2021 Results: WWOX re-expressed only in "the WSM S5 line (referred to as WSM S5 W-AAV3 and W-AAV6)". The WPM family was used for forebrain organoids only, with no rescue. Limitations section: "we generated patient-derived organoids from only two families, one of each syndrome". The knockout hESC line is the WiBR3 KO1/KO2 (see U3). |
| 2026 AAV9 arm uses four patient lines | SUPPORTED, printed | Supplementary Figure 9B legend and Supplementary Figure 10A legend: "WPM S AAV9-EGFP… WPM D… WSM S… LM-iPS AAV9-EGFP: n=3; LM-iPS AAV9-WWOX: n=4". Those are the only four patient lines in the arm. WCH S, a fifth patient line, is not in the AAV9 arm. |
| Three families | Inferred, not printed | The 2026 text never counts families for the AAV9 arm. It is inferred from the following. |
| Two of the lines being siblings | Printed in the 2021 paper, only implied in 2026 | 2021 Results: "their affected homozygous daughter and son (WPM D1 and WPM S1)", with parents "WPM F2 and WPM M3". 2026 Key Resources lists "(WPM S, WPM D) iPS cells, Previous study (23)", and reference 23 is the 2021 paper. The 2026 Figure 1A pictogram shows a SCAR12 male and a SCAR12 female. |

What the inference rests on:
- WPM: SCAR12, c.1114G>C, homozygous (Supplementary Figure 1E table), one family.
- WSM: WOREE, c.517-2A>G, homozygous. In 2021 this is the single son of the WSM family.
- LM-iPS: WOREE, complex heterozygous c.864G>A / 0.9 Mbp deletion. Its own parents are printed as "the healthy parents (JM-iPS and KS-iPS)" (Supplementary Figure 1G legend).
- Distinct genotypes and distinct parents give three families, but no 2026 sentence states "three families".
- Residual flag: the 2026 Key Resources table also lists "(WSM S, WSM D) iPS cells". The 2021 WSM family has only a son. This is probably a table error. It is not used anywhere else in what I read.

Suggested wording: "The 2026 AAV9 arm uses four patient lines (WPM S, WPM D, WSM S, LM-iPS), which appear to come from three families: the WPM siblings (printed in the 2021 paper), the WSM son (2021 paper), and the LM patient with healthy parents. The family count is inferred from line names and genotypes."

### U6: Figure 6 n values, and Supplementary Figure 10 "n=8"

| Fact | Verdict | Quote and locator |
|---|---|---|
| Figure 6 A(i) and B give n=7 organoids | SUPPORTED | "(WT: n=4 organoids, SCAR12 AAV9-EGFP: n=8, SCAR12 AAV9-WWOX: n=8, WOREE AAV9-EGFP: n=7, WOREE AAV9-WWOX: n=7)". It appears for panels A(i), B(ii) and B(iii). |
| Calcium imaging A(ii) gives n=6 organoids | SUPPORTED | "(WT: n=3 organoids, SCAR12 AAV9-EGFP: n=6, SCAR12 AAV9-WWOX: n=8, WOREE AAV9-EGFP: n=6, WOREE AAV9-WWOX: n=6)". The WOREE ROI counts are 40 and 40. |
| Supplementary Figure 10 gives n=8 | OVERSHOOT | See below. |

Supplementary Figure 10 as printed, by panel:
- Panel A has per-line values: WSM S AAV9-WWOX 4 and LM-iPS AAV9-WWOX 4. Adding them gives 8 for the WOREE WWOX arm, but this is my sum and "8" is not printed for WOREE.
- Panel A for WOREE AAV9-EGFP: WSM S 4 and LM-iPS 3, which sum to 7.
- Panels B and C print "WOREE AAV9-EGFP: n=6, WOREE AAV9-WWOX: n=6".
- The only printed "n=8" values in Supplementary Figure 10 are for SCAR12 (panels B and C; in A the SCAR12 total is 4+4).
- Result: Supplementary Figure 10 prints 4 or 3 per line in panel A and 6 per WOREE arm in panels B and C. The statement's "n=8" is true only as a sum of panel A for the WOREE AAV9-WWOX arm.
- Figure 6 prints WOREE AAV9-WWOX as 7, while the Supplementary Figure 10A per-line values sum to 8. That is a printed discrepancy between the figures, and I do not know the cause.

Replicate unit: organoid (human, week 16). The unit is the organoid for A(i) and B, and the ROI for the right-hand calcium plot.

Corrected wording: "Figure 6 gives n=7 organoids per WOREE AAV9 arm in A(i) and B, and n=6 in the calcium imaging A(ii). Supplementary Figure 10A gives n=4 (WWOX) and 4/3 (EGFP) per WOREE line (WSM S, LM-iPS), which sum to 8 and 7. Supplementary Figure 10B and C give n=6 per WOREE arm."

### U7: Breton 2021 bursts

Source: Breton 2021 (PMC XML), Results section 2.1, Synapsin-Cre Wwox mice. The legend is Figure 1, and the counts are in the Results text.

| Fact | Verdict | Quote |
|---|---|---|
| 0 of 11 slices, 7 mice | SUPPORTED | "(0 of n = 11 slices from 7 S-WT mice; 4 of n = 23 slices from 14 S-HT mice; 36 of n = 42 slices from 24 S-KO mice)". Genotype is S-WT, Wwox+/+ Cre+. |
| 4 of 23 slices, 14 mice | SUPPORTED | Genotype S-HT, Wwoxfl/+ Cre+. |
| 36 of 42 slices, 24 mice | SUPPORTED | Genotype S-KO, Wwoxfl/fl Cre+. |

- Replicate units: neocortical slice, with the number of mice given. Mice are P13–P17, both sexes. The Methods describe the animals as "Synapsin I Cre… S-KO, S-HT, S-WT". The text cites "(Fig. 1A; Repudi et al., 2021)" for this count.
- The statement should name the genotypes (WT, HT, KO) and say "neocortical slices".

### U8: Breton sEPSC comparisons

| Fact | Verdict | Quote and locator |
|---|---|---|
| Figure 3 legend | WRONG anchor | The Figure 3 legend covers reversal potentials and d-APV, CBX and BB-FCF, with n = 30 bursts, 5 animals, and so on. No sEPSC. |
| sEPSC data are in the Figure 4 legend, panels E and F | printed | Panel F: "(S-CTLs n = 18 cells from 10 animals, S-KOs n = 17 cells from 10 animals; s-WT: N = 14 cells, 5 animals; s-HET N = 17 cells, 8 animals)". |
| "5 vs 8 animals in one comparison" | WRONG | The 5 (S-WT) and 8 (S-HET) animals are two separate control subgroups. Each is compared with S-KO. The panel F p-values given are "s-WT vrs s-KO" and "s-HT vrs s-KO". The 5 and 8 are never compared with each other. |
| "10 vs 10 animals in the other" | SUPPORTED | S-CTL vs S-KO, 10 animals each (18 cells vs 17 cells). |

Printed inconsistency in the same legend: S-CTL is 18 cells from 10 animals, but S-WT 14 cells plus S-HET 17 cells would be 31 cells from 13 animals. The S-KO group is also given as 10 animals, with no separate cell or animal split by genotype.

Replicate unit and statistics:
- The unit of the stats is the individual event, not the animal. Cumulative distributions are compared by a Kolmogorov–Smirnov test, with p-values such as 3.4659e-23.
- Cells and animals are as above. Mouse, layer II/III pyramidal neurons.
- The mEPSC numbers in the Figure 4C legend are different: "S-WT N = 10 cells, 4 animals; S-HT N = 10 cells, 5 animals; S-KO N = 10 cells, 5 animals". They are not sEPSC.

Corrected wording: "In Figure 4F the sEPSC comparison is S-CTL (18 cells, 10 animals) vs S-KO (17 cells, 10 animals), with subgroup comparisons S-WT (14 cells, 5 animals) vs S-KO and S-HET (17 cells, 8 animals) vs S-KO (the S-KO group is 10 animals). The legend's cell counts are internally inconsistent."

---

**Counts:** 12 facts SUPPORTED outright, 1 UNDERSHOOT-style qualified (U3 clone composition), 1 OVERSHOOT (U6 Supplementary Figure 10 "n=8"), 2 WRONG (U8 "5 vs 8" and the Figure 3 anchor), 2 inferred rather than printed (U5 family count of three, U5 siblings in 2026), 0 UNVERIFIABLE.

**Not opened:**
- 2021 Appendix PDF (EMMM-13-e13610-s001.pdf): Appendix Figures S1–S6 and Appendix Table S1 (exact P-values).
- 2021 Expanded View PDF and the Table EV1/EV2 xlsx.
- Breton Supplementary Materials, including Table S1 and Figures S1–S4.
- 2026 supplementary Files 008, 009 (methods, read only for cell-attached text), 011 (read only for the Key Resources table) and 012. I read File010 in full for the legends.
- 2026 Figure 6 image, which I did not check against its legend.
- PMID42397075_Aqeilan2026_assets and the brain-awag239.zip bundle.
- The prior-reading files named above.
