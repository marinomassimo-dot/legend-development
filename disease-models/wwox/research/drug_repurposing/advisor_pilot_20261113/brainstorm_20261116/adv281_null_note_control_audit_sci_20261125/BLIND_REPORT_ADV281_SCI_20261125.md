# Blind report, ADV-281 (SCI, 2026-11-25)

Reader: independent blind reader (claude-sonnet-5-5, effort high, as stated by the Orchestrator). Hypothesis level; nothing here is medical advice.
Input read: only the 13-block sentence file and the held sources it names. No acquisition, no contact, no spend. Search date for every "searched" statement: 2026-11-25.
Method notes: figures were rendered or opened and looked at where stated; values read off a graph are marked "by eye"; every number carries its figure/table/panel and unit. Python that read downloaded files ran with `-I -P -E`. No scipy was available, so p values were recomputed with a hand-written incomplete-beta / incomplete-gamma routine (checked against values the papers print).

---

## DR-A01-003 (Shah 2025, PMID 40485335)

**Q1 class: CHECK PRESENT** (allele-mismatched; same fly assay, driver, dose and exposure). In-study check: **yes**.
- The null: 1 mM 4-phenylbutyrate (4-PBA), 48 h in food, in G443D flies (ALRM-Gal4 astrocyte driver, heat-induced seizure): "The seizure phenotype of G443D flies stayed unaltered upon 4-PBA exposure (Figure 6G)". Fig 6G (file g004.jpg, panel G, by eye): G443D control about 46 %, 10 % glycerol about 42 %, 1 mM 4-PBA about 48 % of flies with seizure-like episodes; no star.
- The check: the same dose, time, driver and assay in G443V flies. Fig 6I (g004.jpg panel I): AL volume of G443V protein, control about 30 vs 4-PBA about 230 (median, um^3, by eye), *** (text: "yielding an impressive 14-fold increase in AL expression"). Fig 6H: G443V seizure about 43 % control, about 20 % with 4-PBA, *** (Dunnett). So the manipulation demonstrably acts in this preparation and moves this exact behavioural readout.
- Limits of the check for the allele in the null: no readout shows 4-PBA acting on G443D itself ("4-PBA and glycerol did not markedly alter the expression of WT GAT-1 or G443D (Figure 6B,C)"; G443D already reaches the membrane, Fig 5D and 5H). In vitro, 10 mM 4-PBA on G443D (HEK293, 24 h) is "irresponsive" (Fig 3B, file g007.jpg panel B: about 1.6 % of untreated-WT uptake vs control about 0.1 %, no star, by eye).
- Glycerol in the fly (10 %, 48 h): weak own check (G443V expression "only a minor effect", Fig 6I; seizure ns, Fig 6G and 6H). Glycerol's activity on G443D is shown only in HEK293 (10 %, 24 h, Fig 3B *** about 6 % of untreated-WT single-concentration uptake; Fig 4D, Vmax 165.3 vs WT control 298.2 pmol per 10^6 cells per min), a different system.
- Assay control only: none needed to separate; the G443V arm is an effect check, not only a sensitivity control.

**Q2 verdict: ADD.**
- True as worded in its facts (4-PBA null in G443D flies; glycerol rescued G443D in vitro: Fig 3B, 4D-E). Omitted: the arm is 4-PBA 1 mM 48 h; glycerol also did not rescue G443D in the fly; "this class" is ambiguous because glycerol is itself an osmolyte-type class member that did act in vitro.
- Added clause (verbatim-checkable): "Arm: 1 mM 4-PBA, 48 h, G443D flies (Fig 6G, 'stayed unaltered'); 10 % glycerol was also not significant in G443D flies ('slightly lower ... not statistically significant', Fig 6 legend G-H), so no tested chaperone rescued G443D in vivo; the same 4-PBA dose cut G443V seizures (Fig 6H, ***); G443D already reaches the membrane (Fig 5D, 5H); in vitro 4-PBA 10 mM also did not rescue G443D (Fig 3B)." Replace "this class" by "4-PBA".

Not looked at: Fig 2 and Fig 5 images (g002, g005), Supplementary tif s001-s004 (siRNA, co-expression, calnexin figures), Fig 1 beyond the graphical abstract. File-to-figure mapping inferred from content: g001 graphical abstract, g003 = Fig 4, g004 = Fig 6, g006 = Fig 1, g007 = Fig 3.

---

## DR-A01-004 (Frick 2026, PMID 42268630)

**Q1 class: CHECK ABSENT** (for 4-PBA activity). In-study check: **no**.
- Searched: full text XML (Abstract, Results, Discussion, Methods 4.4-4.7), Figs 1 (viewed), Table S1 (the only supplement, all rows read), on 2026-11-25. No protein readout ("We were unable to directly assess stxbp1a or stxbp1b protein levels in larval zebrafish due to the lack of suitable validated antibodies"), no target-engagement or dose-response of 4-PBA (two doses only, 25 and 50 uM, Fig 1D; one dose 50 uM in LFP, Fig 1G). WT larvae with 4-PBA: no significant effect (Table S1 "1E": WT 0 = 670 mm vs 25 uM 1140 mm, P = 0.06; vs 50 uM 994 mm, P = 0.2342; mm distance moved), not an activity check.
- Assay control only: tetracaine 200 uM lowers WT movement 69 % (Fig 1A) and PTZ raises WT movement (Fig 1B; Table S1 "1C": 5 mM P < 0.0001, 20 mM P = 0.0002; the figure labels differ between text, figure legend and Table S1) but not stxbp1a. These show the readout can move in WT; they do not test 4-PBA. The mutant sits on the floor: Fig 1A stxbp1a vs tetracaine ns (Table S1: P = 0.9983; stxbp1a 277.3 mm, tetracaine 63.38 mm); Z'-factor reported -5.936 (Methods 4.7), which the authors call satisfactory.

**Q2 verdict: STANDS.**
- Each clause checks: nulls in homozygous stxbp1a (4-bp frameshift deletion) and stxbp1b (12-bp deletion) larvae; protein not measured; bath bounded by toxicity ("4-PBA was toxic to larval zebrafish at concentrations above 50 uM", Fig 1C); assay separation unestablished (Fig 1A, Z' above); missense case left open ("may not exclude a potential role for 4-PBA in STXBP1 patients harboring specific missense variants").
- Optional clarifications, not required: the stxbp1b allele is a 12-bp deletion (length divisible by 3, my arithmetic; the paper calls it "loss-of-function" and later "frameshift" without protein or transcript data); the dose actually tested was 25 and 50 uM for 48 h (locomotion; the Fig 1D legend says "10 and 25 uM", contradicting the axis and text) and 50 uM for 45-60 min in 9 stxbp1b larvae (ictal events per 15 min, 7.56 vs 8.22, P = 0.8593, t 0.1802, df 16, Table S1 "1H").

Not looked at: Fig 2 and Fig 3 images (g002, g003); the 16 other candidates' rows were scanned, not analysed.

---

## DR-A02-002 (Clausen 2024 PMID 38378758; Grønbæk-Thygesen 2024 PMID 38740822)

**Q1 class: CHECK ABSENT** for chloroquine (CQ) itself, in both papers. In-study check of CQ: **no**.
- The null: 20 uM CQ, 16 h, HEK293T landing-pad cells, GFP:mCherry flow profile of the whole library. Clausen: "no substantial changes were observed with chloroquine (Fig. 3C)" (Fig 3 viewed; n 495,000 vs 516,000 cells, representative histogram). Grønbæk: "little effect of treating the cells with the autophagy-inhibitor chloroquine (CQ) (Fig. 4F)" (viewed); Supplementary Fig 8E (MOESM1 p.10, viewed): C152W and WT unchanged by CQ.
- Searched: both full texts, both supplement PDFs (text) and both peer-review files for chloroquine, lysosom*, autophag*, LC3, p62, LAMP, LysoTracker, acidif*, bafilomycin: no readout shows CQ inhibiting lysosomal degradation in these cells.
- Nearest (different manipulation, so not a CQ check): Clausen Supplementary Fig 1B (MOESM1) uses bafilomycin A (1 uM, 4 h, with antimycin/oligomycin) on the mt-Keima mitophagy reporter in the same HEK293T landing-pad line (grey n = 6,215 cells). Different inhibitor and assay.
- Assay control only: bortezomib 15 uM, 16 h in the same cells moves the readout (Clausen Fig 3A, a modest shoulder shift; Grønbæk Fig 4E, a clear shift; Supplementary Fig 8D shifts C152W modestly). This shows the readout can move; it says nothing about CQ.

**Q2 verdict: ADD.**
- Facts fit: library flow shift only; the perturbations were not sorted or sequenced ("we do not sort and sequence the cells after the perturbations", Grønbæk peer-review reply, MOESM2).
- Overstated or omitted: "did nothing" vs the authors' "little effect" / "no substantial changes"; the loss is placed on the proteasome only for "most" low-abundance variants ("most low abundance variants are proteasome targets"; Grønbæk: "most of the low-abundant ASPA variants are targeted by the ubiquitin-proteasome system"); CQ activity unchecked; Grønbæk's own caveat.
- Added clause: "chloroquine 20 uM, 16 h; no readout shows it blocked lysosomal degradation in these cells; the authors report 'no substantial changes' (Clausen Fig 3C) and 'little effect' (Grønbæk Fig 4F) and write 'we cannot exclude that autophagy will not play a role under conditions where the expression of the ASPA variants persists for longer'; the proteasome attribution is for 'most' variants."

Not looked at: both variant-level xlsx files (MOESM4), other main figures; Grønbæk Methods give bortezomib 10 uM while the Fig 4 legend gives 15 uM (noted, not resolved).

---

## DR-A02-009 (Collard 2023, PMID 38051092)

**Q1 class: CHECK PRESENT** (same cells, same transfection and time; allele differs for the activity effect). In-study check: **yes**.
- The null: co-expression of HSPA1A or HSF1 (30 ug plasmid, Lipofectamine, 48 h, A23 hamster DON fibroblasts stably expressing human CBS I278T): "In case of CBS I278T, there was no rescue of enzymatic activity" (Results, Fig 3B).
- Checks in the same source: HSF1 "clearly upregulated" on Western blot and HSPA1A overexpression confirmed by V5 tag (Results, Fig 3A); soluble I278T and R125Q protein rose ("substantial recovery of CBS in soluble fractions", Fig 3A); the same manipulation raised R125Q activity "5-7-fold ... cca 10 % of CBS WT levels" (Fig 3B). Caveat: "Western blot with HSP70 antibody failed to observe an increase in steady-state levels of HSP70" (endogenous HSP70; antibody specificity raised by the authors in the Discussion).
- Searched: full XML text (no supplement: `pmc-prop-has-supplement no`). Figure images are not in the held file and I found none under files/figures, so Fig 3A/B bar values were not viewed; "no rescue" is the text's wording only.
- Assay control only: none.

**Q2 verdict: MUST CHANGE** (one clause) plus a wording ADD.
- Card: "although the same allele is rescued by proteasome inhibition in mice and in the kidney line". Source (Discussion): "CBS I278T was functionally rescued by proteasome inhibitor treatment when heterologously expressed in yeast, in human patient fibroblasts and transgenic HCU mice. 15, 25, 28". No kidney line appears in the text (the only HEK293 mention is "other cells like yeast or HEK293 perhaps respond differently to expression of pathogenic CBS variants"). The host line of this paper is a hamster lung fibroblast ("Chinese hamster DON lung fibroblast A23"). The claim is also a citation, not a result of this paper; proteasome inhibitors (MG132, carfilzomib) were tested here on R125Q only (Fig 4C-D).
- Replacement: "although the paper cites rescue of I278T by proteasome inhibition in yeast, human patient fibroblasts and transgenic mice (refs 15, 25, 28); proteasome inhibitors were tested here on R125Q only".
- Also: "did not rise at all" is stronger than the text's "no rescue of enzymatic activity" / "enzymatic activity was rescued only in CBS R125Q" (Fig 3B values not viewed). The rest checks: R125Q 5-7-fold and about 10 % of WT; "endpoint recorded: protein up, activity unchanged"; ER stress ("substantial activation of ER stress in our cellular HCU model ... marked upregulation of BiP").

Not looked at: Fig 1-5 images (not held).

---

## DR-E03-001 (ChEMBL rows, CHEMBL306823 = sodium dichloroacetate; mechanism rows in chembl_mechanisms.tsv)

**Q1 class: CHECK PRESENT BUT NOT MATCHED.** In-study check: **no** (curated database rows; the underlying papers are not held).
- The null: enzyme assay with no half-maximal inhibition: IC50 > 1,000,000 nM (> 1 mM) in chembl_named_activities.tsv, doc CHEMBL1133665 (PDHK from rats), CHEMBL1132309 (PDK), CHEMBL1133733 (porcine PDHK). The three docs carry identical companion values (see next bullet), so they are probably not independent. ChEMBL stores only the censored value; the top concentration tested is not in the rows.
- Effects of the same compound in other systems, same docs: EC50 130,000 nM = 130 uM, lactate oxidation, human skin fibroblasts (all three docs); "70 %" of control lactate in rats in vivo (units garbled between docs: 1 umol/kg vs 1 mM/kg). Different assay systems and species.
- Higher-dose or different enzyme rows in the same retrieval (mixed): CHEMBL4308888 PDK1 (unknown origin) 64.2 % inhibition at 10 mM, EC50 5,700,000 nM; CHEMBL5370584 PDK (unknown origin, 10 min, with ATP) EC50 180,000 nM; CHEMBL4732185 PDK EC50 > 100,000,000 nM; CHEMBL3813671 recombinant human PDK1 Kd > 1,000,000 nM.
- Searched: chembl_named_activities.tsv (DCA, 97 rows), chembl_mechanisms.tsv (4 DCA rows, action INHIBITOR, refs PubMed:20533281; 27803917), chembl_activities.tsv (no CHEMBL306823 rows). No positive-control compound of the same enzyme assay is in these rows.

**Q2 verdict: ADD.**
- The sentence is true for the three > 1 mM rows and for the 130 uM fibroblast row. "The enzyme assay" is singular but the retrieved enzyme-level rows disagree (180 uM to > 100 mM).
- Added clause: "Other retrieved enzyme-level rows differ: EC50 180 uM (PDK unknown origin, 10 min with ATP, CHEMBL5370584), EC50 5.7 mM with 64.2 % inhibition at 10 mM (PDK1, CHEMBL4308888), Kd > 1 mM (human PDK1, CHEMBL3813671), EC50 > 100 mM (CHEMBL4732185); the > 1 mM rows (CHEMBL1133665, CHEMBL1132309, CHEMBL1133733) carry identical companion values and ChEMBL records no top concentration."

Not looked at: the .py scripts, chembl_raw JSON, chembl_target_log.json; the live ChEMBL and Open Targets records (not held).

---

## DR-H01-003 (Kessler 2025, Epilepsia, PMID 40165594; abstract only)

**Q1 class: CHECK PRESENT BUT NOT MATCHED.** In-study check: **yes at abstract level only** (not verifiable at dose or exposure).
- The null: oral ACT-709478 "had no effect on focal onset seizures", tested "in one model of focal onset seizures, the amygdala kindling rat model" (abstract, Methods and Results).
- Same-paper activity: it "suppressed SWDs in WAG/Rij rats and GAERS" and "reduced the severity of generalized convulsive seizures in the AGS mouse model and the MEST in mice, albeit at higher concentration". Different seizure models, one different species (mouse); the abstract gives no dose, plasma or brain exposure, or engagement readout for the kindling arm.
- Searched: abstract text and metadata in PMID40165594_europepmc_core.json (journal Epilepsia, `inPMC` N, `hasPDF` N, `hasSuppl` N, subscription full text); no full text is held.

**Q2 verdict: ADD.**
- The quoted words are in the abstract ("had no effect on focal onset seizures").
- Added clause: "in one model only (rat amygdala kindling); abstract only, with no dose or exposure for that arm; the same abstract reports efficacy in rat absence models and, 'albeit at higher concentration', in mouse generalized-seizure models, and ends 'could possibly also be beneficial for epileptic syndromes presenting with additional seizure types'."

Not looked at: full text (not held).

---

## DR-M01-001 (Steinberg 2026, PMID 42397075; compound arm, A51)

**Q1 class: CHECK PRESENT** (same organoids, same dose and exposure, different readouts; indirect, not MYC protein). In-study check: **yes**.
- The null: A51 125 nM from week 8 to week 15 (main text p.11 "from week 8 to week 15"; Supplementary Methods File009 "MYC inhibition") in WWOX-KO organoids: CTIP2 unchanged. Supp Fig 7G (File010 p.12, rendered and viewed): CTIP2+ KO-1B vs KO-1B+A51 ns (by eye about 0.1 % vs about 0.7 % of cells; WT NT about 12.5 %, WT DMSO about 5.5 %).
- The checks, same organoids: Supp Fig 7F SOX2+ KO-1B vs +A51 ** (about 60 % to about 33 %), SOX2+MYC+ ** (about 72 % to about 48 %); Supp Fig 7G NEUN+ * (about 6 % to about 18 %). Text: "We observed a marked reduction in both progenitor populations, confirming successful MYC inhibition."
- Limits: no MYC protein, Wnt readout or kinase-target readout; A51 is "a multi-kinase inhibitor"; no WT + A51 arm, no dose-response ("submaximal dose"); one clone (WiBR3 KO-1B).
- Assay control only: WT NT and WT DMSO bars show the CTIP2 and NEUN readouts can be non-zero in WT; the KO CTIP2 value is at the floor.

**Q2 verdict: ADD.**
- Facts checked: SOX2+ and SOX2+MYC+ fall, NEUN rises, CTIP2 unchanged ("no change in CTIP2+ neurons"); "one of three experiments without independent differentiations" (Methods: "except for single-cell RNA-seq, MYC inhibition and NSCs CHIP-Seq"); the authors' clause "using multiple biological replicates" is verbatim; "percentages carry no denominators" matches the panels ("Percentage of cells (%)", no denominators in the legend).
- Issues: (a) "upper-layer marker mildly rises (main text)" is the main text's claim; the panel does not carry it: Supp Fig 7F SATB2+ KO-1B vs KO-1B+A51 is **ns** (about 0.4 % vs about 0.75 % of cells; WT about 1.35 %); (b) the source says "No randomization or blinding was applied in this study", stronger than "is stated"; (c) the Supp Fig 7 legend gives "n = number of organoids (WT NT: n=4, WT DMSO: n=4, WiBR3 WKO-1B: n=6; WiBR3 WKO-1B: n=7)" while the CTIP2 panel plots about 6/6/10/9 points ("biological and technical replicates from one experiment"), so the unit of analysis is unclear.
- Added or replacement clauses: "SATB2 KO vs KO+A51 is ns in Supp Fig 7F (the main text says 'mild increase')"; "no randomization or blinding was applied (Methods)"; "Supp Fig 7 legend: n = organoids 4/4/6/7, one experiment, plotted points exceed organoids".

Not looked at: main figure pages, Supp Figs 1-6 and 8-10, the zip brain-awag239.zip and figures-page PNGs. The READING_NOTE and receipt JSON in the supplement folder were deliberately not opened (card or ledger text). The card's label says the supplement is not available locally; the Supplementary figures PDF is in fact held (File010) and Supp Fig 7F-G was viewed directly.

---

## DR-D01-002 (Steinberg 2026, same experiment)

**Q1 class: CHECK PRESENT** (same as DR-M01-001: SOX2+, SOX2+MYC+ and NEUN+ change under the same 125 nM, week 8-15 exposure, Supp Fig 7F-G). In-study check: **yes**. Assay control only: WT NT and WT DMSO arms (readout range).

**Q2 verdict: ADD**, with one conditional MUST CHANGE.
- "knockout-versus-treated not significant for both markers" is correct if the two markers are CTIP2 (Supp Fig 7G ns) and SATB2 (Supp Fig 7F ns). The sentence does not name them. If NEUN were one of them, the statement would be false: NEUN+ KO-1B vs KO-1B+A51 is * (Supp Fig 7G).
- "CTIP2 remaining far below wild type" matches: KO-1B+A51 vs WT NT ****, vs WT DMSO * (Supp Fig 7G).
- Added clause: "markers CTIP2 and SATB2 (KO-1B vs KO-1B + A51 ns, Supp Fig 7G and 7F; NEUN does rise, *); CTIP2 is near zero in both (about 0.1 % and about 0.7 % of cells), so a floor limits the test; one KO clone, one experiment, harvest week 15 only; the main text separately calls the SATB2 change 'mild'."

Not looked at: as DR-M01-001.

---

## DA-LC-ATF4-002 (Lucas-Clarke 2026, PMID 42909904)

**Q1 class: CHECK PRESENT** (knockdown measured, but in newly eclosed heads, not at day 14 or in brain). In-study check: **yes**.
- The null: pan-neuronal Wwox RNAi (elav-GAL4 > TRiP) in LacZ background, Atf4 immunostaining, day-14 female brains: "t = 0.0894 p = 0.9305", N = 6 brains (Supplementary Fig 5D-E, legend; viewed image: both genotypes near-blank, bars about 0.93 vs 0.94, normalised units, points about 0.55-1.1).
- The check: Supplementary Fig 1 (docx image 1, viewed): Wwox mRNA about 0.55 of RNAi control (points by eye about 0.35, 0.63, 0.70; N = 3 pools of 15 heads, newly eclosed females; *** by randomisation test). Knockdown is partial (about 45 % reduction) and was not measured at the day-14 time point of the Atf4 assay. The same neuronal knockdown shortens life ("median lifespans = 57 and 42 days", Fig 1B) in the same driver and genotype.
- Assay control only: Atf4 immunostaining can rise in an Aβ42 background with the same knockdown ("U = 0 P = 0.0022", Fig 5H-I, N = 6): it shows assay sensitivity in a different background, not an activity check of the knockdown in the LacZ context. No Atf4-inducing positive control or secondary-only blank is shown in the LacZ context.

**Q2 verdict: ADD.**
- Numbers verified: with 6 vs 6 brains (df 10) t = 0.0894 gives P = 0.9305; the 95 % interval half-width is 2.228 x sqrt(2/6) = 1.29 pooled SD, so "about plus or minus 1.3 pooled SD" is right ("n 6 brains" is per genotype). "No interaction test" is right: the statistics lines list t test (Supp Fig 5E), Mann-Whitney (Fig 5I), and a two-way ANOVA only for other panels.
- Added clause: "knockdown verified only by head qPCR in newly eclosed females (about 0.55 of control, N 3, Supplementary Fig 1), not at day 14; Atf4 staining in the LacZ background is near blank in both genotypes (Supplementary Fig 5D), so the null may sit at the detection floor; the two backgrounds were tested with different tests (t test vs Mann-Whitney)."

Not looked at: main-figure images of Fig 5 (not rendered from the PDF), Supplementary_tables.xlsx, the zip, other supplementary figures.

---

## DR-AAV-GLU10-HD (Obeid 2026, PMID 42422765; Fig 3E, glucose at P10)

**Q1 class: CHECK PRESENT** (graph-level, same cohort, same dose and day; engagement at P30 only). In-study check: **yes**.
- The null: AAV9-hSynI-hWWOX HD 2.63 x 10^11 vg, neonatal ICV, Wwox-null mice; blood glucose (mg/dL) at P10, Fig 3E (gr3.jpg and native render, viewed): WT+RI about 129, KO+RI about 95, KO+LD about 105, KO+HD about 113 (means, by eye). Brackets: WT vs KO+RI *; WT vs KO+HD ns; KO+RI vs KO+HD ns; KO+LD vs KO+HD ns.
- Checks in the same cohort: body weight at P10, Fig 3C (by eye, g): WT about 7.1, KO+HD about 6.6, KO+LD about 4.8, KO+RI about 4.4 (no test or n printed for panel C); survival "HD produced survival comparable to WT animals (p = 0.78)" (Fig 3B); glucose at P20 HD about 147 vs LD about 128 ** (Fig 3F); engagement at P30 for the same doses (Fig 5A-L: vector DNA, mRNA, WWOX protein), a longer exposure than P10; WWOX protein at P0 injection with lower doses 4 x 10^10 and 8 x 10^10 vg (Fig 2E).
- Assay control only: none.

**Q2 verdict: ADD.**
- Facts verified: HD about 113, ns vs WT and ns vs KO; the text says "both LD and HD treatments partially corrected hypoglycemia" at P10 while the panel shows ns.
- Added clause: "P10, Fig 3E, Student t tests without multiplicity correction (Methods); the KO comparator is reference-item injected (KO+RI, about 95 mg/dL, counted n about 8, wide spread) and differs from WT+RI (about 129 mg/dL, n about 10) only at *; counted n for HD about 11; the panel is low-powered, so 'ns against the untreated knockout' is not evidence of no effect." (n counted from plotted points; the legend gives no n for panel E.)

Not looked at: mmc1.pdf and mmc2.pdf (Fig S3, S5), Fig 5 image (gr5), Fig 1-2 images.

---

## DR-AAV-GLU10-LD (Obeid 2026, same panel)

**Q1 class: CHECK PRESENT BUT NOT MATCHED.** In-study check: **yes**.
- The null: LD 1.23 x 10^11 vg, glucose at P10, Fig 3E: about 105 mg/dL; ns vs WT and ns vs KO+RI (about 95).
- Checks: LD survival "modestly, though significantly, extended" (Fig 3B, p < 0.0001 vs KO+RI); LD glucose at P20 about 128, below WT about 145 (*, Fig 3F), so the first measurable LD glucose effect is later than P10. At P10 body weight LD about 4.8 g vs KO+RI about 4.4 g (Fig 3C, by eye), i.e. no visible LD effect at P10 on the one same-day readout. Engagement for LD at P30 only (Fig 5: "LD-treated mice showed lower but readily detectable expression"), a longer exposure than the null.

**Q2 verdict: ADD.**
- Sentence is true (about 105, ns vs WT and vs KO).
- Added clause: "P10, Fig 3E; LD n about 7, KO+RI about 8 (counted from points); LD shows no visible effect on same-day body weight (Fig 3C) and its WWOX expression is shown at P30 only (Fig 5), so this is a null before the dose's own effects are demonstrable; the text says LD 'partially corrected hypoglycemia' from P10."

Not looked at: as DR-AAV-GLU10-HD.

---

## DR-P11-004 (Yadav 2022, Iran J Child Neurol, PMID 35222658)

**Q1 class: CHECK ABSENT.** In-study check: **no**.
- The manipulation: IM magnesium sulphate 100 mg/kg/day x 3 days then oral Mg 37.5 or 75 mg/day x 3 months (Methods). Searched: whole XML (abstract, Methods, Results, Discussion, Tables 1-4; `has-supplement` no): no post-treatment serum magnesium, no dose-response. Baseline serum Mg only (Table 1: 2.10 +/- 0.52 vs 2.04 +/- 0.55 mg/dL). The Discussion statement "magnesium supplementation increases serum magnesium levels" is an inference from the baseline-stratified response (Table 3), not a measurement.
- The only other same-trial effect, EEG improvement (Table 2), is recomputed below. Assay control only: none.

**Q2 verdict: MUST CHANGE** (two clauses; the rest verified).
- Statement 1: "The EEG p value is not reproducible from Table 2 (about 0.10 by a Fisher test)" and "only the EEG p value of Table 2 does not [reproduce]". The paper's stated test is chi-square ("the chi-square test was used for categorical data"). My recomputation of Table 2 final EEG (intervention normal/abnormal 11/2, non-intervention 6/7): uncorrected Pearson chi-square 4.248, df 1, **p = 0.0393**, which reproduces the printed 0.04; Fisher exact two-sided **p = 0.0968**, Yates-corrected chi-square p = 0.0992. Both smaller expected cells are 4.5 (13 x 9 / 26), two of four cells under 5. So the printed p reproduces under the uncorrected chi-square that also reproduces Table 3, but not under an exact test.
- Statement 2 (support for "only the EEG p fails"): the DQ/SQ p 0.09 of Table 2 does not reproduce either: Table 2 prints only the "Normal" row (4 vs 0); with group sizes 26 and 22, uncorrected chi-square p = 0.055, Fisher p = 0.114, Yates p about 0.16.
- Replacement: "The EEG p of 0.04 reproduces from Table 2 only as an uncorrected chi-square (11/2 vs 6/7: chi-square 4.25, df 1, p 0.039); a Fisher exact test gives 0.097 and a Yates-corrected chi-square 0.099, with two of four expected counts at 4.5; the DQ/SQ p of 0.09 (only the 'Normal' row printed, 4 vs 0) is not reproduced by any standard test (0.055 uncorrected, 0.114 Fisher)."
- Verified as written: 52 recruited (30/22) and 48 analysed per protocol (26/22: 2 lost, 2 excluded for magnesium side effects, all from the intervention arm, which the card could add); open label ("open-labelled"); comparator "syrup containing an equal amount of calcium and vitamin D but without magnesium"; seizure control p 0.69 (my chi-square 0.693) and development p 0.09 as printed; EEG p 0.04 in Results vs "EEG normalization (p=0.003)" in the Discussion; no post-treatment serum Mg; EEG denominators (row label "n=26", cells 11+2 and 6+7 = 13 and 13, row "Abnormal 22 | 22"); Table 3: tfoot row "Low 4 2 3 9" is the second row of the non-intervention group (rowspan 2 with one body row), giving intervention Low 4/4/0 and Normal 2/3/13, non-intervention Low 4/2/3 and Normal 3/2/8, margins matching Table 2 (6/7/13 and 7/4/11); chi-square p 0.0029 and 0.418 (printed 0.003 and 0.42); the wrong assignment (Low 4/4/0 with Normal 3/2/8) gives 0.018; Table 4 chi-square p 0.0038 (printed 0.004).

Not looked at: Figure 1 flow chart (image not held); no supplement exists.

---

## DR-H02-019 (Hu 2025, Sci Rep, vigabatrin DTI, PMID 40670421)

**Q1 class: CHECK PRESENT BUT NOT MATCHED** (split below). In-study check: **yes**.
- The nulls in the sentence: (a) ADC unchanged in the imaging-finding group (Table 2: right median 1209.0 vs control 1280.0; left 1427.0 vs 1366.0, x 10^-6 mm^2/s; ANOVA P = 0.623 and 0.520, my F(2,32) recomputation 0.623 and 0.520); (b) exposed group with normal imaging not below controls (ROFA 0.463 vs 0.427; LOFA 0.390 vs 0.410; Table 2).
- For (a): the children in that group carry in-study effects of the drug (same exposure): symmetrical thalamic DWI hyperintensity "first identified on MRI obtained within 1-2 weeks after VGB initiation" and FA lowered (Table 2), so this null has an in-study effect check (CHECK PRESENT).
- For (b): no activity or engagement readout in those 11 children (no VGB level, no GABA measurement; max daily dose 83 mg/kg/d median, Table 1); the effect shown in the imaging-finding group is in different children, and the groups are defined by the outcome (the DWI finding, "Participants were divided into three groups based on treatment regimen and imaging findings"), so it is not matched.
- Assay control only: none; FVEP "normal ... in all participants" is not an activity check.
- Searched: whole XML text, Tables 1-3, Methods and Discussion (the supplement is not held).

**Q2 verdict: ADD.**
- Verified: Table 3 (six of 11): left 0.273 to 0.367 p 0.044 and right 0.286 to 0.437 p 0.050 reproduce as paired t tests with df 5 (t 2.68297 gives 0.0437; t 2.56884 gives 0.0501, i.e. not below 0.05); the text says "(P < 0.05)" for the rise; no unexposed time control; Table 2 medians and the star on group 1 vs group 3; medians with quartiles reported while "one-way analysis of variance" is named (Methods).
- Omitted limits: the ADC direction is not consistent across sides (right lower than controls, left higher) and the authors say the differences were "not consistent between the left and right optic nerves"; n = 11/11/13; the paired test and the selection of the six are not described (follow-up "only in 6 patients owing to patient partial compliance"); single centre, retrospective.
- Added clause: "ADC differences were 'not consistent between the left and right optic nerves' (right median 1209.0 vs 1280.0 in controls, left 1427.0 vs 1366.0); n = 11, 11 and 13; groups are defined by the DWI finding, and no drug-level or GABA measure exists in the normal-imaging children; the follow-up is six of 11 children, 'owing to patient partial compliance'."

Not looked at: figures (not held); the Discussion's ROC and reference list were read only partly; no supplement is held.

---

## Summary table

| id | Q1 class | in-study check | Q2 verdict |
|---|---|---|---|
| DR-A01-003 | CHECK PRESENT (G443V, same fly assay and dose) | yes | ADD |
| DR-A01-004 | CHECK ABSENT | no | STANDS |
| DR-A02-002 | CHECK ABSENT (chloroquine; bortezomib = assay control only) | no | ADD |
| DR-A02-009 | CHECK PRESENT (R125Q activity, I278T protein, same cells) | yes | MUST CHANGE ("kidney line" not in source) |
| DR-E03-001 | CHECK PRESENT BUT NOT MATCHED | no (database rows) | ADD |
| DR-H01-003 | CHECK PRESENT BUT NOT MATCHED (abstract only) | yes, abstract level | ADD |
| DR-M01-001 | CHECK PRESENT (SOX2+, SOX2+MYC+, NEUN+ in same organoids) | yes | ADD (SATB2 panel ns) |
| DR-D01-002 | CHECK PRESENT | yes | ADD (name markers; NEUN would contradict) |
| DA-LC-ATF4-002 | CHECK PRESENT (head qPCR, newly eclosed, about 0.55) | yes | ADD |
| DR-AAV-GLU10-HD | CHECK PRESENT (P10 weight, graph level) | yes | ADD |
| DR-AAV-GLU10-LD | CHECK PRESENT BUT NOT MATCHED | yes | ADD |
| DR-P11-004 | CHECK ABSENT | no | MUST CHANGE (EEG 0.04 reproduces by uncorrected chi-square; DQ/SQ 0.09 does not) |
| DR-H02-019 | CHECK PRESENT BUT NOT MATCHED (ADC null present; normal-imaging group not matched) | yes | ADD |
