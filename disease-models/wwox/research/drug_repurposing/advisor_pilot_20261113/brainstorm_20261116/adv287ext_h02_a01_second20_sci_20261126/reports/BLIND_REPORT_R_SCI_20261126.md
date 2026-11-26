# ADV-287 extension, random 20: BLIND READER report as delivered (legend-delegate; models {'claude-sonnet-5-5': 200}; effort {'high': 200}; reply text extracted verbatim from its transcript hand-back call; 2026-11-26)

BLIND READ OF PACKET R (20 sentences), 2026-11-26. Only the PREREG "One matching rule" section and PACKET_R.md were opened in the task folder.

COUNTS: CORRECT 6 (R-02, R-03, R-05, R-06, R-09, R-25) | ADD 8 (R-01, R-04, R-07, R-08, R-11, R-19, R-24, R-29) | WRONG 1 (R-34) | INCOMPLETE 1 (R-37) | NOT ASSESSABLE 4 (R-10, R-33, R-35, R-39) | total 20.

Method note. Figure values are by eye plus pixel measurement against the axis ticks, error about 0.03 to 0.05 axis units. Ratios were recomputed from all rows.

R-01 ADD. Opened: GSE156243 count table (all 6 libraries, 4 KO and 2 WT), SOFT file, and both authors' DE lists.
- KO/WT ratio of mean CPM (CPM taken against each library's summed counts) is NFE2L2 0.752, KEAP1 0.926, NQO1 0.730, G6PD 0.745, SLC7A11 0.653, BACH1 0.735. These match the sentence. SOFT file: "4 KO samples and 2 WT … included in final analysis".
- Add: the authors' DESeq2 down-list carries NFE2L2 (log2FC -0.58, padj 1.43E-02) and G6PD (-0.42, 7.15E-03). In the same panel HMOX1 is 1.67x, SRXN1 1.33x and GSR 1.20x.
- Added sentence: "…; HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x are higher; descriptive, mean CPM."

R-02 CORRECT. Opened: Banke 2026 PMC page HTML, with the body text, Table 2 and Table 3 (no supplements).
Evidence: the text prints "A639V 23-fold, I655F 4.5-fold, A652G 3.2-fold, M818T 2.8-fold and S810R 1.9-fold". Table 2 shows five IC50 asterisks, and S810R is the Grin2b knock-in mouse.

R-03 CORRECT. Opened: Wang 2023 full text (Europe PMC XML).
Evidence: "64 cases who failed the first ACTH treatment (50 … not seizure-free … another 14 who relapsed within 1–12 months)". All 229 received MgSO4+ACTH, single arm.

R-04 ADD. Opened: Hussain 2023 Fig 9 image (panels d and e), crops and a pixel scan, plus the text.
- Axis ticks calibrated. Fig 9d, Il1b, qRT-PCR, n=6 mice per genotype: WT bar about 1.87 and P47T bar about 3.73 (dot means 1.9 and 3.8), so the ratio is 2.0 (range 1.9 to 2.1). The paper's own text says "≥2-fold".
- Fig 9e, Tnfa: WT bar about 0.96, P47T about 3.25. The P47T-to-WT ratio is 3.3 to 3.4.
- Overlap for Il1b is not marginal by count. One WT dot (about 3.1) sits above three of six P47T dots (about 2.4, 2.8, 3.1). For Tnfa there is no overlap: WT maximum about 1.64, P47T minimum about 1.81 (gap about 0.17).
- Replacement: "Il1b about 2x and Tnfa about 3.3x of the plotted means (by eye and pixel, ±0.1); Il1b ranges overlap (one WT dot above three of six P47T dots); Tnfa ranges do not."

R-05 CORRECT. Opened: Karnstedt 2026 full text (PMC XML).
Evidence: "14/19 GoF vs. 3/15 LoF, p = .0049". My Fisher recompute on 14/5 versus 3/12 gives 0.00490.

R-06 CORRECT (text level). Opened: Mijatovic 2024 full text (Europe PMC XML); the Fig 5 and Fig 6 images are not held.
Evidence: ESI had no effect on T191M half-life but activity rose to 244% (p<0.05). For I278T, half-life rose 1.6-fold and activity to 374%. "T191M alone" holds because nothing else dissociates: WT ESI shows half-life 1.4x with only a non-significant 147% activity trend.
The figure tables of half-life values were not seen, so "any change" rests on the text "no effect".

R-07 ADD. Opened: PMID 42397075 accepted-manuscript layout text; Fig 2 page image; the Fig 2F 600-dpi image, pixel-scanned against ticks.
- Fig 2F log2 fold change in RG fraction versus WT, single-cell clusters (each genotype is one pooled organoid set; Fig 2D cell totals are 5,649 WT, 3,020 KO, 3,422 SCAR12, 5,916 WOREE): KO +0.98, WOREE +0.07, SCAR12 -0.26. The "+0.9" is about 0.08 low, so write about +1.0. The text/figure mismatch for WOREE is real: the text says "prominent increase … more pronounced in KO", and Fig 2E also shows WOREE RG about equal to WT.
- Add: SCAR12 RG is -0.26 log2 (about 0.83x), not zero. The text calls it "similar to WT".

R-08 ADD. Opened: PMID 42397075 main text and the supplement PDF File010 (Supp Fig 7F, rendered at 400 dpi).
Supp Fig 7F, SATB2+ % of cells, n = organoids per legend (WT NT 4, WT DMSO 4, KO 6, KO+A51 7), but more dots are plotted: about 15 KO and about 11 KO+A51, so the dots are fields or ROIs. By eye, WT NT is about 1.35, WT DMSO about 1.45, KO about 0.38 and KO+A51 about 0.72. KO+A51 versus both WT arms is ns. Add: KO+A51 versus untreated KO is also ns (Tukey); the main text calls it a "mild increase".

R-09 CORRECT. Opened: openFDA Diacomit label JSON.
Evidence: effective_time 20260427. Section 12.1 says the mechanism is "unknown", with GABA-A and CYP inhibition as possible. 12.3 gives "Protein binding … 99%" and time to peak 2 to 3 h, with no Cmax value.

R-10 NOT ASSESSABLE. Source: SUPER-CAT abstract (PMID 42837646), not held.
Search 2026-11-26 03:02 UTC. The files/ tree (Obeid-named files excluded) was searched for "42837646", "SUPER-CAT" and "postanoxic"; no SUPER-CAT record was found. Only repository card quotes exist (card file, nmdar README). The 77 vs 27 percent figure cannot be checked.

R-11 ADD. Opened: Yadav 2022 full text (Europe PMC XML).
- Table 2 EEG: normal/abnormal 11/2 versus 6/7. Recomputed expected counts 8.5, 4.5, 8.5, 4.5; chi-square 4.248, p 0.0393; Yates chi-square 2.719, p 0.0992; Fisher 0.0968. All match the sentence.
- Add: the Discussion prints "EEG normalization (p=0.003)", which does not reproduce from Table 2 either.

R-19 ADD. Opened: GSE156243 SOFT file.
Series_overall_design says "4 KO samples and 2 WT … after 2 WT samples failed quality control"; the contact laboratory is Aqeilan's, so 4 v 2 and one laboratory hold. Add: the 2 WT libraries are survivors of an exclusion that removed 2 further WT.

R-24 ADD. Opened: Mijatovic 2024 XML text. Fig 5 and Fig 6 images are not held.
- Evidence: bortezomib raised WT half-life 7.7-fold (T191M 6.8, I278T 3.0). Activity with bortezomib: WT 174% was only a "trend", T191M 259% and I278T 574% were significant (p<0.05).
- Not assessable: "does not repair". Absolute activity against the vehicle-WT line (Fig 6) is not seen, because the figure images are not held.
- Added sentence: "…the WT activity gain was a non-significant trend (174%)."

R-25 CORRECT. Opened: Lucas-Clarke 2026 main text and supplement DOCX, including the Supp Fig 5E image.
Evidence: Supp Fig 5E, Atf4 fluorescence in LacZ background, 6 dots per genotype; legend "N = 6 brains … t = 0.0894 p = 0.9305". No cross-background interaction test appears in the main text or supplement text (searched "interaction" 2026-11-26 03:07 UTC).

R-29 ADD. Opened: GSE156243 counts and DE lists.
- Numbers match R-01: NFE2L2 0.75x, NQO1 0.73x.
- The two quoted genes both fall, which is a coherent direction. The incoherence comes from HMOX1 1.67x up, SRXN1 1.33x and GSR 1.20x; also GCLM 0.89x and TXNRD1 0.91x. NFE2L2 is the factor itself, not a target.
- Replacement: "…do not form a coherent signature (NQO1 0.73x, G6PD 0.75x, SLC7A11 0.65x lower; HMOX1 1.67x, SRXN1 1.33x, GSR 1.20x higher)."

R-33 NOT ASSESSABLE (ratio). Opened: PMID 33279441 saved abstract; PMID 25449033 not held.
- The 33279441 abstract says only that the drugs "hardly distributed into the brain", with 6 to 17% unbound in brain at 10 mg/kg i.v. No 0.015 to 0.02 ratio appears in it.
- The ratio is attributed to 25449033, whose abstract is not held (searched files/ for "25449033", 2026-11-26 03:07 UTC; only a spurious hit in a mouse RPKM table). Repository README and card text are pointers only.
- The negative "human brain or CSF exposure" is UNSETTLED. A held commentary (PMC9545618) says "direct chemical measurements from cerebrospinal fluid and from brain tissue" showed lack of CNS access. Its cited CSF reference (Javaheri 1993) is not shown to be human.

R-34 WRONG. Opened: Lukas 2020 full text including Table 1 (assay comparison).
- The 12.9% (23/178) is correct. But the two assays are not near-identical: Table 1 lists the GLP assay versus in-house as HEK293 MSR versus HEK293H cells, 120 h versus 60 h, 10 versus 20 µM DGJ, different transfection, plasmid and lysis, and amenability criteria ≥3% AND 1.2-fold versus ≥5% OR 1.5-fold. With one uniform 7% rule, discordance is 9.0%.
- The paper does state "no established correlation … clinical benefit".
- Replacement: "…'amenable' call differs for 12.9% (23/178) of variants between an in-house and the GLP assay, which differ in cells, DGJ dose, incubation and criteria; no clinical correlation is established (Fabry GLA)."

R-35 NOT ASSESSABLE. The source is a registry statement, with no held passage (the card says so).
Search 2026-11-26 03:09 UTC. A regex sweep over held files/ (Obeid excluded) for "ketogenic|ketone" together with WOREE/WWOX and lactate, "3/5", "3 of 5" or "2.4" found nothing. Piard 2019 (text and four supplement workbooks) has no ketogenic or lactate string.
Held related facts: Al Baradie 2022 says the ketogenic-diet role in WOREE is "not yet well described", and one Gln230Pro patient was seizure-free about nine months on the diet.

R-37 INCOMPLETE. Opened: Steinberg 2021 (PMID 34268881) full text (Fig 4 legends and Results) and the GSE156243 lists.
- Holds: Wnt targets are up (AXIN2, LEF1, SP5, TCF7L2 up, in my recompute and the authors' list). RNA-seq is 2 WT versus 4 KO, and the lists are P-value selected.
- But "transcript only" is untrue for this source. Fig 4E is a nuclear/cytoplasmic β-catenin immunoblot (WT n=2, KO n=4 organoids, about 1.7-fold, no test). Fig 4D is qPCR validation (n=4 v 4, Tukey). Fig EV3C is a week 6 to 24 qPCR time course.
- The next clause on the card ("nuclear beta-catenin unmeasured") is therefore also contradicted.
- Replacement: "…transcripts up on RNA-seq (raw p, 2 WT v 4 KO); nuclear β-catenin by immunoblot about 1.7-fold (2 v 4 organoids, untested); no reporter assay."

R-39 NOT ASSESSABLE (ratio). Same basis as R-33: the 25449033 abstract is not held and the 33279441 abstract carries no 0.015 to 0.02 ratio. The remaining claims (mouse PK, efflux, modelled free brain concentration in the NKCC1-inhibitory range at 10 mg/kg i.v.) are consistent with the held 33279441 abstract. The species of 25449033 is unverified.

FILES OPENED (under /home/desktop/legend-development/):
- .claude/worktrees/sci_at_20261126/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv287ext_h02_a01_second20_sci_20261126/PREREG_ADV287EXT_SCI_20261126.md (rule section only) and PACKET_R.md
- Card packets (cards/*.packet.json), read via python: L01_nrf2_axis, F04_nmdar_intervention_class, E02_ldh_inhibition, J01_glial_reactivity_modulation, E01_isr_modulators, F03_bumetanide_chloride_gradient, A03_client_binding_chaperone, E04_ketogenic_lactate_axis, D01_a51
- Repository pointer files: pharmacological_qualification_it8_p3_20261029/{README.md, cases.json, comparison.tsv, collected.json.gz} and nmdar_pharmacology_it6_p9_20261029/ (file list and grep hits only)
- files/geo/GSE156243/ (count table, SOFT, up and down DE lists)
- files/fulltext/: PMID40994429_ADV272_PMC12677382_pmcpage_20261125.html; PMID36967744_ADV272_PMC10030695_epmc_20261125.xml; PMID35222658_ADV272_PMC8752995_epmc_20261125.xml; PMID36828035_Hussain2023_PMC.xml and _assets/nihms-1957654-f0009.jpg; PMID41489401_Karnstedt2026_Epilepsia_PMC13075606.xml; PMID39041895_Mijatovic2024_PMC11264351_epmc_2026-10-29.xml; PMID42397075_Steinberg2026_OUP-AM_layout.txt; PMID42397075_Steinberg2026_assets/fig2F_600dpi.png and figs/fig_p33_1217x776.jpeg; PMID42397075_Steinberg2026_OUP-Supplement/brain-2025-03809-File009.txt, File010.txt and File010.pdf; ketamine_kds_it_20261117/p5_alternatives/openFDA_label_diacomit.json; PMID42909904_PMC13684411.xml; PMID42909904_supplement/Supplementary_material.docx and Supplementary_material_derived.txt; adv065b_20261118/abs_33279441.txt and PMID35524446_PMC9545618_efetch_pmc.xml; PMID32023956_Lukas2020_PMC7037350.xml; PMID42161426_GLAM76K2026_PMC_r2.xml (read, not the source); PMID34268881_Steinberg2021_PMC_r2.xml; PMID30356099_Piard2019_EPMC.xml and its supplement xlsx files; PMID35792847_AlBaradie2022_JLE_fulltext.html; keyword-sweep contexts only from other held papers.
- Scratch: /home/desktop/.claude/jobs/c6d4dd83/tmp/r_blind/ (scripts, crops, renders). Nothing was written in the repository or files/.

Not done:
- No web or PubMed lookups were made (the PubMed tool was not used).
- The SUPER-CAT abstract and the PMID 25449033 abstract are not held.
- The Mijatovic 2024 Fig 5 and Fig 6 images are not held.
- One grep over the repository's nmdar_pharmacology folder and one over files/adv098_agent_sheets_raw_he_20261119 were refused by the permission classifier (the second looks like an earlier work product); neither was retried.
