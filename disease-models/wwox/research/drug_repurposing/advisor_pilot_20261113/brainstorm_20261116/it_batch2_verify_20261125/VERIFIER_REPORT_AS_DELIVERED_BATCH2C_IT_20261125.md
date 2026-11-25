# Blind verifier report, batch 2 call C (units U9 to U16), as delivered (2026-11-25)

Dispatch: `legend-delegate`, model sonnet, effort high (stated in the dispatch), 8 statements as (statement, source, anchor), no candidate and no conclusion given; statements in `statements_batch2c.tsv`. Hand-back text below, unchanged except for this header. The delegate could not write a report file; this file is the saved hand-back. Read-back (`session_model_census.py` on the delegate transcript): `claude-sonnet-5-5`, effort `high` on 42 of 42 turns, 43 tool uses, 28,217 output tokens, 129,568 subagent tokens in the notice (a total with context, not output); the delegate itself says it could not read its runtime setting back, so the transcript is the source.

---

BLIND SOURCE VERIFICATION, units U9-U16 (call2_units_b.tsv)
Setting read: sonnet, effort high as requested; I could not read back the runtime setting. No agents started. No contact with anyone. Python reading untrusted files ran with -I. Scratch images only, in /home/desktop/.claude/jobs/6739e4ff/tmp/b2/out2/s/ (s8-10.png, f3-06.png, f3crop-06.png, rep-12.png, mmc1.txt, mmc2.txt). All files read are under /home/desktop/legend-development/files/fulltext/.

KEY FINDINGS (details per unit below)
- U9: 75 is the paper's combined analysis set (13 + 62), not "the cohort" (the paper's cohort is 13). "New" is not the paper's word: Patients 6 and 7 were "briefly reported" before.
- U12: the Figure 3 legend text prints no n, but the in-plot key of Figure 3B prints n per arm: WT+RI n=20, KO+RI n=10, KO+WWOX(LD) n=20, KO+WWOX(HD) n=30. The Methods say exact n are in the legends.
- U13: n=3 (P3) and n=7 (P5) are in Figure S8, read from the plot key in the image. The S8 legend text gives only "n=3-7".
- U14: "n = 20" is printed twice in the Figure 5 legend, but "mice are 5 per group" is not printed for Figure 5 (OVERSHOOT).
- U15: the named file PMID34214506_Saadane2021_epmc.xml is not the article. It is a 150-byte HTTP 500 error JSON ({"status":500,"error":"Internal Server Error","path":"/europepmc/webservices/rest/PMC8579242/fullTextXML"}). I used the sibling file adv262_20261125/PMC8579242_page.txt (the PMC article page, 85,765 bytes, same folder, not an excluded file name). It holds the full text including the Figure 9 legend. The Figure 9 image was not viewed.

======== U9 Oliver 2023 (PMID 36779245), PMC_r2.xml; whole XML searched (abstract, intro, methods, results, legends, refs). The assets folder holds only two figure JPGs (EPI-64-1351-g003/g004), not opened.

Replicate unit: individual patients, and families. Species: human.

9.1 "The cohort is 75 individuals": OVERSHOOT (wording).
- Printed: Results 3.7: "We compared our cohort (n = 13) with 62 individuals with WWOX-DEE from the literature ... (i.e., excluding six published SCAR12 cases)". Then: "We stratified all 75 cases into one of three genetic groups: (1) null/null (n = 45), (2) null/missense (n = 15), (3) missense/missense (n = 15)." Figure 4 legend: "Survival analysis for 75 individuals with WWOX developmental and epileptic encephalopathy".
- The abstract does not state 75. It says "We studied 13 patients from 12 families".
- Corrected wording: "The paper's cohort is 13 patients from 12 families. The genotype-survival analysis pools these with 62 literature individuals, 75 in total (Results 3.7, Figure 4)." The 75 is printed as "all 75 cases"; the 13 + 62 sum is arithmetic that matches.

9.2 13 patients from 12 families: SUPPORTED.
- Abstract Methods: "We studied 13 patients from 12 families with WWOX-DEE". Methods 2: "we ascertained 13 patients (12 families) with biallelic WWOX pathogenic variants from five epilepsy centers". Results 3.1: "We recruited 13 patients (seven female) from 12 families".

9.3 "new" patients: OVERSHOOT (minor).
- Methods 2: "...including two patients (Patients 6 and 7) briefly reported. 29, 30". The paper uses "novel" only for variants (abstract/intro: "nine novel WWOX pathogenic variants"). It never calls the patients "new".
- Corrected wording: "13 patients (two of them, Patients 6 and 7, briefly reported earlier)".

9.4 Two brothers: SUPPORTED.
- Printed: "one duplication (brothers, Patients 9 and 10; Supplementary Material)" (Methods 2.3). Also Results: "For brothers, Patients 9 and 10, RT-PCR suggested that their maternally inherited exon 5 duplication resulted in premature termination".
- Same family is printed indirectly: "Of the 12 unrelated individuals, six had homozygous and six compound heterozygous variants" (3.6). The Table 1 family column was not separately checked.

9.5 62 literature patients from 45 families: SUPPORTED.
- Introduction: "has been reported in 62 individuals from 45 families" (refs 7-24). Results 3.7: "62 individuals with WWOX-DEE from the literature".
- No total family count (57) is printed. If any unit uses 57 families, it is the producer's sum.

9.6 75 = 13 + 62: SUPPORTED (see 9.1).

======== U10 Gao et al., Neurology 2025 (PMID 40875931), PubMed abstract only, fetched via the PubMed MCP tool with no personal parameters. DOI 10.1212/WNL.0000000000213883. Per PubMed: Neurology 2025 Sep 23; 105(6):e213883 (epub 2025 Aug 28).

Replicate unit: individuals, in families. Parent- or guardian-completed REDCap questionnaires. Human.

10.1 "50 individuals in 45 families": SUPPORTED.
- Quote (Results): "we have collected and analyzed data from 50 individuals with biallelic WWOX variants across 45 families, identifying 25 variants that have not been previously reported."
- Caution: Oliver's literature set is also "62 individuals from 45 families" (U9). The two 45s are different counts in different papers.
- INFERENCE (not printed): the genotype percentages (56.8%, 29.5%, 13.6%) fit 25/13/6 of 44 individuals. That suggests the genotype analysis used 44 of the 50, but the abstract does not say so.
10.2 "2025 Neurology": SUPPORTED. 10.3 "(abstract)" as locator: SUPPORTED.

======== U11 Repudi 2021 Brain (PMID 33914858). The .txt (two-column interleaved) and the PDF (page 12 rendered and viewed) were both read. Supplement: the zip extracted folder holds brain-2020-02464-File009 (pdf/txt, grep for DRG/co-culture/Figure 6: no hits), File010/011 mp4, File012-014 xlsx (only sheet names read: RNA-seq comparison and primer/antibody tables; no co-culture data).

System: mouse E13.5 embryonic DRG neurons plus wild-type OPCs (mouse), in vitro.

11.1 n = 4 per condition: SUPPORTED.
- Figure 6 legend (D): "Results are shown in a box plot from two independent experiments (WT-DRGs + WT-OPCs, n = 4; KO-DRGs + WT-OPCs, n = 4). **P < 0.01".
11.2 From two independent experiments: SUPPORTED (same quote).

11.3 "Biological unit (embryos or animals) is not stated": UNDERSHOOT.
- Printed: the legend does not define n. The counted object is "oligodendrocytes counted (area covered 14 mm diameter)".
- Methods: "DRG neurons were isolated from mouse embryos at embryonic Day 13.5. Embryos were genotyped and the DRGs were collected". "OPCs (200 000/coverslip) were seeded on DRG neuronal cultures". "Pre-cleaned 13 mm diameter glass coverslips".
- The Methods do not give the number of embryos, litters or coverslips per genotype, nor which of these n=4 counts. The Statistical analysis section says only "Student's t-test".
- Searched: whole .txt (legend, Methods, Statistical analysis, Results) and the supplement File009. No definition of n found.
- Corrected wording: "Legend: n = 4 per condition from two independent experiments; n is not defined (counts are per area, 'area covered 14 mm diameter'). Methods say the DRGs come from genotyped E13.5 mouse embryos but give no embryo, litter or coverslip numbers."

======== U12 Obeid 2026 (PMID 42422765), PMC_r2.xml. Figure 3 legend and the whole XML searched. Figure 3 image examined in assets/mmc2.pdf p.6 (Document S2, article plus supplement).

Replicate unit: mouse (Wwox-null/KO and WT, neonatal ICV AAV9).

12.1 The Figure 3 legend text prints no n per arm: SUPPORTED.
- Legend B: "Kaplan-Meier survival analyses of Wwox-null mice treated with HD or LD AAV9-SynI-WWOX compared with KO and WT mice injected with the RI. HD produced survival comparable to WT animals (p = 0.78) ... (p < 0.0001)". The legend has p values and no "n =" in any panel (A-H). The Results sentence before it has none either.

12.2 Implication that Figure 3 prints no n: UNDERSHOOT. The figure itself prints n in the plot key of panel B (mmc2.pdf p.6, 400 dpi crop): "WT+RI n=20", "KO+RI n=10", "KO+WWOX (LD) n=20", "KO+WWOX (HD) n=30".
- Statistical analysis (Methods): "Exact sample sizes (n) and p values are reported in the figure legends." That does not hold for Figure 3.
- Corrected wording: "The Figure 3 legend text prints no n, although the Methods say it does. The panel B plot key prints n = 20 (WT+RI), 10 (KO+RI), 20 (KO+LD), 30 (KO+HD), mice."
- The key is printed in the image. I read it by eye at 400 dpi. The figure legend does not state what the n counts, so "mice" is my inference from "survival of ... mice".

======== U13 same paper. Whole XML plus assets/mmc1.pdf (Document S1, Figures S1-S8, 10 pages; Figure S8 is page 10, rendered and viewed) and mmc2.pdf (text grep).

Replicate unit: mouse (Wwox-null, treated at P1-P5 with 2.63x10^11 vg AAV9-hSyn1-hWWOX).

13.1 n = 3 for the P3 injection group: SUPPORTED. Figure S8A key (image): "KO+WWOX (P3) n=3".
13.2 n = 7 for the P5 group: SUPPORTED. Figure S8A key: "KO+WWOX (P5) n=7"; S8B key: "KO+WWOX (P5) n=7".
13.3 Reported in supplementary Figure S8: SUPPORTED. The S8 plot keys (image) also give WT+RI n=6, KO+RI n=6, KO+WWOX (P1) n=6, KO+WWOX (P2) n=6 in panel A; S8B shows only P1 n=6 and P5 n=7.
- Qualification on location. The S8 legend text gives only ranges: "(A) Kaplan-Meier survival analysis (till P40) of Wwox-null treated ... at P1-P5 (n=3-7) compared to Wwox-null and WT mice injected with the reference item (RI) (n = 6)". The per-group n=3 and n=7 are in the in-plot keys (image), not in the legend text.
- The main-text Results (S8 paragraph) cites "Figure S8" and gives no n. It says only "with at least three littermates treated per time point".
- P4 has no survival key in panels A-B (it appears only on the x axis of C and D).
- Optional observation, read by eye from the curves (approximate): the P3 curve drops to about 67% near day 24, and P5 in panel B to about 75% near day 35.
- Corrected wording: "Figure S8A key: P3 n=3, P5 n=7 mice (legend text: n=3-7)."

======== U14 Lin 2022 (PMID 36498839), Lin2022_PMC.xml. Whole XML searched: legends, Methods 4.4-4.8, Results 2.5-2.6. No assets folder; figure images not held or viewed.

System: Wwox heterozygous vs wild-type mice, 3 and 10 months; 11 months for immunohistochemistry.

14.1 The Figure 5 legend contains n = 20 with no stated unit: SUPPORTED.
- Printed twice. (B): "The probe test was quantified as time spent in the target quadrant (Bonferroni's post hoc test and ANOVA: * p < 0.05 ... n = 20)". (C): "TPC6AΔ plaques were significantly upregulated in the heterozygous mice (** p < 0.01 vs. respective control group; n = 20). The number of plaques per microscopic field at 200× is shown."
- For (C) the unit is only hinted (plaques per microscopic field), not defined as the n. For (B) there is no hint.

14.2 "While mice are 5 per group": OVERSHOOT.
- Printed: Figure 5 (A,B): "...are shown (n = 5)". Figure 4: "(n = 5 for each group)". No unit is attached.
- No sentence gives the number of wild-type or heterozygous Wwox mice. Methods 4.4: "five 10-month-old 3xTg mice ... received four consecutive injections of Zfra4-10", which concerns the Zfra treatment group of 3xTg mice, not the WT/het groups. Methods 4.8 gives no n.
- Searched: all legends, 4.4-4.8, Results.
- Corrected wording: "Figure 5 prints n = 5 (panel A, learning curve) without a unit, and n = 20 for the probe test (B) and for plaques per microscopic field (C) without a unit. The number of mice per genotype is not stated."

======== U15 Saadane 2021 (PMID 34214506), from PMC8579242_page.txt (see the source note above).

System: mouse cone-photoreceptor line 661W (siRNA is "against mouse WW domain-containing oxidoreductase"). "Mouse" for the line itself is my inference from the siRNA and the paper's mouse model; it is not printed for the line.

15.1 Figure 9 legend "n = 2 replications of the results": SUPPORTED. Quote: "Data are expressed as means ± SD. n = 2 replications of the results. ∗∗ P ≤ 0.01, ∗∗∗ P ≤ 0.001." (legend of Figure 9 A-C; the legend title also has "66W1" for 661W).
15.2 One cell line (661W): SUPPORTED.
- Methods: "The authors used a cone photoreceptor cell line, 661W". No other cell line was found in the page text (searched "cell line(s)", Methods, Results, legends).
15.3 siRNA from Ambion: SUPPORTED. Methods: "siRNA against mouse WW domain-containing oxidoreductase (WWOX), and control scrambled siRNA obtained from Ambion (Life Technology, Carlsbad, CA)". Both the target and scrambled siRNA are from Ambion.
15.4 5 and 25 pmol versus scrambled: SUPPORTED, with a unit inconsistency inside the source.
- Results: "reduced the superoxide production in high glucose by 27% and 37% in the two different concentrations of siRNA (5 and 25 pmol), respectively, compared with scrambled siRNA (Figure 9C)". Methods: "The siRNA concentrations of 5 pmol/L and 25 pmol/L were selected based on a preliminary dose-response experiment."
- Methods do not say the scrambled control was run at both concentrations.
15.5 Legend does not say the two replications are separate experiments: SUPPORTED.
- The legend, Methods and Statistical analysis never call the two replications independent or separate. The Methods say only "PCR reactions were performed in triplicate" and "In a different set of experiments ...".
- What was replicated (cultures, wells or experiments) is not stated. SD from n=2 is as printed.

======== U16 Tochigi 2019 (PMID 31340538), PMC_r2.xml. Whole XML searched. No assets folder; figure images not viewed.

System: male LDE-strain rats, lde/lde (Wwox mutant) vs +/+, PND 5-21, cerebral cortex.

16.1 Mean of three independent experiments: SUPPORTED.
- Figure 5 legend: "All graphs were shown as mean ± S.D. from three independent experiment." (the legend has this singular typo).
16.2 Each with at least three affected and three normal males: SUPPORTED.
- Methods 4.1: "At least three affected and three normal males were included in each experiment (western blot and immunostaining) and examined each day."
- The match "affected = lde/lde, normal = +/+" is my inference. The legend uses +/+ and lde/lde.

16.3 "GFAP and Iba1 densities": UNDERSHOOT (wording).
- Legend (B, D): "The numbers of GFAP- and Iba1-positive cells were quantified in a subarea of the cerebral cortex containing WM". (E) is western blot band intensity normalised to β-actin. The word "density" is not used for Figure 5.
- Corrected wording: "GFAP- and Iba1-positive cell numbers per cortical subarea (B, D) and western band intensities (E)."

16.4 Number of animals per plotted point not stated: SUPPORTED, with a qualification.
- The legend gives no n per point. The only animal numbers are the Methods 4.1 minimum of at least three per genotype per experiment. Whether each point is a mean of animals within an experiment or across the three is not stated.
- The words "three independent experiments" do not say which animals or litters. Searched: Figure 5 legend, Methods 4.1, whole XML (n = hits).

======== COUNTS
Facts examined: 28.
- SUPPORTED: 22 (9.2, 9.4, 9.5, 9.6; 10.1-10.3; 11.1, 11.2; 12.1; 13.1-13.3; 14.1; 15.1-15.5; 16.1, 16.2, 16.4).
- UNDERSHOOT: 3 (11.3, 12.2, 16.3).
- OVERSHOOT: 3 (9.1, 9.3, 14.2).
- WRONG: 0.
- UNVERIFIABLE: 0.
Statements with a correction needed: U9, U11, U12, U14, U16.

======== NOT OPENED / not examined
- Never opened: anything under disease-models/, ledger/ or other repository folders; READING_NOTE; *_derived.txt; FULLTEXT_READ_RECEIPT.
- Not viewed: Oliver Figure 3/4 JPGs (assets folder listing only). Figure images for Lin, Tochigi and Saadane Figure 9 (not held, or not opened).
- Not opened: PMC8579242_page.html, gao_doi.html, suzuki_pubmed.html (in adv262_20261125); the duplicate dated XMLs (Obeid PMC_2026-09-27.xml, Oliver PMC_2026-09-27.xml).
- Repudi supplement: the xlsx contents were not read (sheet names only); File009 was text-grepped only.
- Obeid mmc2.pdf: only p.6 viewed, plus text grep. mmc1.pdf: only p.10 viewed, plus text grep.
- Repudi PDF: only page 12 rendered. The .txt was read by regex windows, not end to end.
- PubMed: only the abstract record for 40875931 (no full text).
