# ADV-287 extension, random 20: FIRST READER report as delivered (legend-delegate; models {'claude-sonnet-5-5': 224}; effort {'high': 224}; reply text extracted verbatim from its transcript hand-back call; 2026-11-26)

FIRST READING, PACKET R (20 sentences). Model sonnet, effort high. No web, no acquisition, no edits in the repository or files/. Obeid/42422765 not opened. Recursive greps used --exclude patterns for both names.

COUNTS
CORRECT 6: R-01, R-02, R-03, R-09, R-19, R-25
ADD 5: R-05, R-06, R-08, R-11, R-29
WRONG 2: R-04, R-07 (both are by-eye "about" values that pixel measurement puts about 0.08-0.09 off; borderline, see blocks)
INCOMPLETE 3: R-24, R-34, R-37
NOT ASSESSABLE 4: R-10, R-33, R-39, R-35 (R-35 only in part: "3 of 5" is held and CORRECT; the lactate clause is not held)

R-01 (L01 DA-L01-003). CORRECT. Opened: GSE156243 Salmon count table, all 6 libraries (4 KO, 2 WT), and the SOFT file (full).
Evidence: mean-CPM KO/WT recomputed: NFE2L2 0.752, KEAP1 0.926, NQO1 0.730, G6PD 0.745, SLC7A11 0.653, BACH1 0.735. All match.

R-02 (F04 DR-P9-006). CORRECT. Opened: PMC12677382 page as held (full body, Tables 2 and 3, Results).
Evidence: text prints "five ... reduction in potency ... S810R 1.9-fold". Table 2 IC50 asterisks on A639V, A652G, I655F, S810R and M818T are the only IC50 increases.

R-03 (P11 DR-P11-005). CORRECT. Opened: PMC10030695 full text, Table 1.
Evidence: 64 ACTH failures (50 not seizure-free, 14 relapsed within 1-12 months); all 229 received MgSO4+ACTH; no control group.

R-04 (L01 DA-L01-002). WRONG (minor, borderline). Opened: Fig 9d,e image (nihms-1957654-f0009.jpg) with pixel measurement, Results text, legend.
Evidence: Wwox P47T vs WT mouse cerebellum, qRT-PCR, n 6 v 6 mice. Axis-calibrated bar tops (error about 0.05): Il1b WT 1.90, P47T 3.78, ratio 1.99; dot means 1.93 v 3.82 give 1.98. This is about 2.0x, not 1.9x, and matches the paper's ">= 2-fold". Tnf WT 1.00, P47T 3.29 (dot means 1.01, 3.30): 3.3x holds. Tnf: highest WT dot 1.65 is below lowest P47T dot 1.82 (no overlap, holds). Il1b: highest WT dot 3.14 is above 3 of 6 P47T dots (3.09, 2.76, 2.42), so "marginal" understates it.
Replacement: "by the figure (pixel measurement of bar tops) Il1b is about 2.0x and Tnf about 3.3x of the plotted WT means; for Il1b the highest WT dot (about 3.1) lies above three of the six P47T dots, for Tnf no WT dot reaches the lowest P47T dot (1.65 v 1.82)".

R-05 (F01 DR-W2-003). ADD. Opened: PMC13075606 full text, supplement S2 clinical xlsx (Group 4 rows).
Evidence: text "14/19 GoF vs 3/15 LoF, p=.0049"; my Fisher test gives 0.0049. The 15 comparators include 5 VUS individuals (#8, #19, #28, #29, #31). Supplement S2: #28 (seizure-free 10 months) and #29 (3-4/day to 1 per 3 months) show seizure improvement but are scored "no effect". The 3 improvers are #9, #15, #23 (parent-reported). Counting #28 and #29 gives 5/15 (Fisher p 0.036).
Add: "scoring #28 and #29 (VUS) as improved would give 14/19 v 5/15, p 0.036".

R-06 (A02 DR-A02-008). ADD. Opened: PMC11264351 full text (Results 3.3-3.4, Discussion). Figures 5 and 6 images are NOT held; numbers come from the text.
Evidence: eeyarestatin I: T191M no half-life effect, activity 244% (p<0.05); I278T half-life 1.6x, activity 374%. Both hold.
Add: WT with bortezomib has half-life 7.7x but activity only a trend (174%, n.s.), and WT with bafilomycin has half-life 1.4x but activity 88%. So activity/turnover mismatches also occur in WT and in magnitude (I278T bortezomib 3.0x half-life v 574% activity). Inhibitors showed cell damage at the effective doses. HEK293A CBS-KO cells, human CBS, activity by live-cell probe (4 areas x 3 wells).

R-07 (M01 DA-M01-003). WRONG (minor, borderline). Opened: Fig 2F image (fig2F_600dpi.png) with pixel measurement, Results text, legend.
Evidence: pixel, 152.75 px per log2 unit, error about 0.03. RG: KO +0.98, WOREE +0.07, SCAR12 -0.27. Neurons: KO -2.38, WOREE -0.06, SCAR12 +0.19. So KO is about +1.0, not +0.9. WOREE +0.05 holds (+0.07). Text/figure mismatch confirmed. SCAR12 RG is -0.27 (about 0.83x), not "wild-type-like" in the figure (the text says "similar to WT"). Single scRNA-seq dataset per genotype, no test.
Replacement: "Fig 2F shows RG log2FC about +1.0 in the knockout, about +0.07 in WOREE and about -0.27 in SCAR12 (text: SCAR12 'similar to WT'; WOREE 'prominent increase')".

R-08 (D01 DR-D01-002). ADD. Opened: Supplementary Fig 7F in File010.pdf p12 (213 dpi, pixel-calibrated) and legend; main-text Results.
Evidence: SATB2+ % of cells, by eye/pixel (error about 0.05): WT NT 1.33, WT DMSO 1.43, KO 0.4, KO+A51 0.71. Brackets: KO+A51 v WT NT ns, v WT DMSO ns, v KO ns. KO v WT * (both). Sentence holds.
Add: the legend gives n = 4, 4, 6, 7 organoids, but the plot shows about 6, 6, 15 and 11 dots, so dots are not organoids. One KO clone, one experiment. The main text says a "mild increase in SATB2+" although KO v KO+A51 is ns.

R-09 (E02 p4_card/pharmacology). CORRECT. Opened: openFDA Diacomit label JSON (effective_time 20260427), sections 12.1-12.3 and all fields searched.
Evidence: mechanism "unknown"; possible GABA-A and CYP inhibition; protein binding 99%; only time to peak (2-3 h) given, no Cmax.

R-10 (F04 DR-P9-013). NOT ASSESSABLE. The SUPER-CAT abstract (PMID 42837646) is not held. Search 2026-11-26 in files/, query "42837646", "SUPER-CAT" and "postanoxic super-refractory": only an unrelated RPKM table matched. Only the repository README/gen script quote "77 against 27 percent"; nothing was checked against a source. Needs: abstract (PubMed) to confirm 77 v 27 percent and that it is cholestatic liver injury.

R-11 (P11 DR-P11-004). ADD. Opened: PMC8752995 full text, Tables 1-4.
Evidence: Table 2, final EEG in initially abnormal EEG: normal/abnormal 11/2 (Mg) v 6/7 (control). Recomputed chi-square 4.248, p 0.0393; Yates 2.719, p 0.0992; Fisher 0.0968; expected counts 8.5, 4.5, 8.5, 4.5. All match.
Add: Results print EEG p=0.04, but the Discussion prints "EEG normalization (p=0.003)". Seizure control p=0.69 (Table 2).

R-19 (J01 DA-J01-007 genotype). CORRECT. Opened: GSE156243 count table and SOFT file.
Evidence: 4 KO and 2 WT libraries; the contact lab is a single laboratory (Aqeilan lab, Hebrew University); 2 of 4 WT organoids excluded after QC.

R-24 (A02 against[0]). INCOMPLETE. Opened: PMC11264351 full text (Fig 5/6 images not held).
Evidence: WT half-life 7.7x with bortezomib is correct. But the sentence treats this as "the gain" and "multiplies residual function". WT activity rose only as a non-significant trend (174%), while mutant activity rose significantly and more (T191M 259%, I278T 574%). Half-life gains: T191M 6.8x, I278T 3.0x. "Does not repair" needs the Fig 6 WT-threshold line, which is not held.
Replacement: "Proteasome inhibition also raised wild-type CBS half-life about 7.7-fold, but wild-type activity rose only as a non-significant trend (174%) against significant rises in T191M (259%) and I278T (574%); whether treated mutants reach the wild-type level is in Fig 6, not held."

R-25 (E01 against[0]). CORRECT. Opened: PMC13684411 full text, Supplementary_material_derived.txt, Supplementary Fig 5 image (docx image5).
Evidence: Supp Fig 5E, LacZ background: "N = 6 brains", t=0.0894, p=0.9305. p=0.9305 is exactly df 10, so 6 v 6; the plot shows 6 dots per group. No interaction test reported.

R-29 (L01 against[1]). ADD. Opened: GSE156243 count table.
Evidence: NFE2L2 0.752 and NQO1 0.730 are correct. Both are down, so the incoherence rests on other genes.
Add: HMOX1 1.67, SRXN1 1.33, GSR 1.20 are up (mean CPM, 4 KO v 2 WT libraries, one parental line, no test). Also NFE2L2 is the factor itself, not a target.

R-33 (F03 not_known[2]). NOT ASSESSABLE for the number. Opened: abstract of 33279441 (held, abs_33279441.txt). Abstract of 25449033 not held (searched 2026-11-26 in files/ by PMID and by title words "novel prodrug-based strategy" and "Tollner"; none).
Evidence: the 33279441 abstract gives no brain-to-plasma ratio. It says "hardly distributed into the brain", brain unbound fraction 6-17%, 10 mg/kg i.v. The 0.015-0.02 ratio exists only in repository READMEs and cards. The "Human exposure unknown" part is a negative, UNSETTLED.
Replacement: "mouse brain distribution of bumetanide is poor (PMID 33279441 abstract: hardly distributed into the brain, 6-17% unbound; the numerical ratio is not in the held abstract)".

R-34 (A03 adjacent_context[1]). INCOMPLETE. Opened: PMC7037350 full text (Lukas 2020, Results 2.3-2.4, Tables 1-3, Discussion).
Evidence: 12.9% (23/178) is correct, but it compares the GLP-validated assay with its criteria v the in-house assay with its own criteria. The assays differ in cell line (HEK293 MSR v HEK293H), incubation (120 v 60 h), DGJ (10 v 20 µM), replicates and criteria. With the GLP criteria applied to in-house data the discordance is 18.0% (32/178); 6.2% (11/178) when in-house criteria are applied to the GLP data; 9.0% at a single 7% threshold. "To date, there is no established correlation ... clinical benefit" is correct.
Replacement: "...differs for 12.9% (23 of 178) of GLA variants between the GLP-validated HEK assay and a similar in-house HEK assay that differs in incubation, chaperone concentration and criteria (18.0% with the GLP criteria applied to both); no clinical correlation established".

R-35 (E04 not_known[2]). NOT ASSESSABLE in part. Opened: PMID36537114 Chong 2023 (Scholar Gateway chunks plus JSON; partial text, 29.9k chars), Al-Baradie 2022, Riva 2022, Oliver 2023, Piard 2019 text and supplement.
Evidence: "3 of 5" is CORRECT. Chong 2023 reports 5 WOREE patients, KD responders patients 1, 2 and 4. The card's "no held source passage" is therefore false for that clause. Lactate 2.4-3.3 mmol/L in one individual is not found. Search 2026-11-26, query lactate|lactic|mmol in the Chong files and "2.4-3.3" across files/fulltext: nothing. UNSETTLED.
Add: other held WOREE KD reports are less favourable: Riva 2022 "KD did not significantly improve seizures and was suspended"; Oliver 2023 "only 1 of 3 who started KD continued it".
Replacement: "A ketogenic-diet response is reported in 3 of 5 WOREE patients (Chong 2023, PMID 36537114, patients 1, 2, 4); other WOREE reports are mixed (Riva 2022 no benefit; Oliver 2023 1 of 3 continued); the lactate value is unsourced."

R-37 (D01 p4_fields target_expression). INCOMPLETE. Opened: Steinberg 2021 full text and figures (PMC XML, Fig 4 in figures/PMID34268881_r2), GSE156243 DE tables.
Evidence: 2 WT v 4 KO is correct (week-15 RNA-seq, 8 samples sequenced, 2 WT excluded). But "raw p" misleads: the DE lists carry pvalue and padj. For example AXIN2 padj 0.0126, LEF1 0.0122, WNT8B 0.0031, SP5 8.8e-5. GBX2 (0.065) and FZD1 (0.058) fail padj<0.05. "Transcript only" is untrue of the same source. Fig 4E shows nuclear beta-catenin N/C 1.76 and 1.67 v WT 1.0 (immunoblot, 2 WT and 4 KO organoids, run twice), so the neighbouring clause "nuclear beta-catenin is unmeasured" is contradicted (no reporter assay).
Replacement: "Wnt target transcripts are up in the knockout (4 KO v 2 WT organoid RNA-seq, DESeq2 padj reported, e.g. AXIN2 0.013, LEF1 0.012), with nuclear beta-catenin N/C about 1.7-fold by immunoblot (2 v 4 organoids, two runs); no reporter assay".

R-39 (F03 translation/cns_exposure). NOT ASSESSABLE for the ratio. Same as R-33: 33279441 abstract is held and has no ratio ("hardly distributed", 6-17% unbound, 10 mg/kg i.v., free brain bumetanide in the NKCC1-inhibitory range). 25449033 abstract not held (search 2026-11-26 as above). The "modelled free brain concentrations in the NKCC1-inhibitory range" half is supported by 33279441. The 0.015-0.02 figure is only a repository quote.

FILES OPENED (all read-only)
Packet and rule: .../adv287ext_h02_a01_second20_sci_20261126/PACKET_R.md; PREREG_ADV287EXT_SCI_20261126.md (rule section only); framework/protocols/delegation_budget.md §2 and §7.
Cards: cards/L01_nrf2_axis, F04_nmdar_intervention_class, J01_glial_reactivity_modulation, E01_isr_modulators, E02_ldh_inhibition, F03_bumetanide_chloride_gradient, A03_client_binding_chaperone, A02_proteasome_inhibitor_class, E04_ketogenic_lactate_axis, D01_a51 (.packet.json). Also drug_repurposing/pharmacological_qualification_it8_p3_20261029/README.md and comparison.tsv (grep lines only), nmdar_pharmacology_it6_p9_20261029/README.md and gen_f04_packet.py (grep lines only).
Held in files/: geo/GSE156243 (count table, SOFT, DE lists); fulltext/PMID36828035 Fig 9 image + PMC text; PMID40994429 PMC page; PMID36967744 xml; PMID35222658 xml; PMID41489401 xml + S2 xlsx; PMID39041895 xml; PMID42397075 layout text, fig2F_600dpi.png, OUP-Supplement File010.pdf (p12-13) and File009/010/011 txt (grep only); PMID34268881 PMC xml + figures/PMID34268881_r2 images; openFDA_label_diacomit.json; PMID42909904 xml + supplement docx/derived txt; adv065b abs_33279441.txt; PMID32023956 xml; PMID36537114 chunks and JSON; PMID35792847, PMID35573960, PMID36779245, PMID30356099 (+supplement xlsx), PMID27495153, PMID42558002 (searched or read for lactate/ketogenic).
Scratch: /home/desktop/.claude/jobs/c6d4dd83/tmp/r_first/ (scripts, extracted text, crops).
