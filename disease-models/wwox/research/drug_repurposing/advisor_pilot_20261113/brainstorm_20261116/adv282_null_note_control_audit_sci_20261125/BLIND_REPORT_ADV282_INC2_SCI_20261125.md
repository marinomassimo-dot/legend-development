# Blind report, ADV-282 increment 2 (eight sentences)

Reader: independent blind checker (sonnet, high effort). Hypothesis-level reading of published open-access papers; not medical advice.
Scratch work: /home/desktop/.claude/jobs/ae0002e7/tmp/adv282/blind2/ (text extractions, page renders, one t-distribution script, run with python3 -I -P -E). No network use. No repository text other than the files named in the input file was opened.

Convention: "figure held" means an image file or a PDF page that can be rendered. Values read from a figure are "by eye" and say so.

---

## DA-J01-006 (Tochigi 2019 rat Fig 6D; Repudi 2021 mouse Fig 1J-O, Supp Fig 1)

**VERDICT: ADD** (every number and the two main findings are right; four things a reader needs are missing or ambiguous).

Checked and right:
- "No Wwox signal in Iba1-positive microglia": Tochigi Results 2.3, "Iba1-positive microglia in the cerebral cortex and CC were not immunostained with antibody to Wwox (Figure 6D)". Figure image held (ijms-20-03596-g006.jpg, 724x305) and viewed. Panel D shows Iba1 (green) cells marked by arrows next to red Wwox-positive cells in the same field (cortex layer V and corpus callosum).
- Repudi legend Fig 1: "G-Control, n = 8; G-KO, n = 9 ... P-value 1.0, no significance, log-rank". Fig 1M and 1N (picture and weight) and 1O (survival) are held in the PDF (rendered, page 6). The KO and control weight curves overlap; the survival curves are flat at 100% to about 120 days.
- "does not report EEG or seizures for it": right. The Results say only "observed no phenotype abnormalities". Seizures and EEG are reported only for N-KO and S-KO.

Wording to add or change:
1. "the paper does not report GFAP or Iba1 immunoreactivity". Not exact. Supplementary Figure 1F (brain-2020-02464-File009.pdf, page 7, held and viewed) shows a GFAP immunostain (green) of G-Control and G-KO at P18, used to identify astrocytes and show WWOX loss in them. Results: "Validation of conditional deletion ... is shown by immunofluorescence staining for CC1 and GFAP". What is not reported is any GFAP or Iba1 reactivity read-out (area, intensity, count, morphology) for G-KO. Replacement: "GFAP staining is shown only to mark astrocytes for the WWOX-loss validation (Supp Fig 1F, one representative field, P18); no GFAP or Iba1 reactivity measure, EEG or seizure record is reported for G-KO."
2. Species and cohorts are not given, and two unlike sources are fused. The microglia statement is rat (lde/lde rat colony, wild-type +/+ male rats, PND 21, single double-staining image, "representative of three independent experiments", no count). The GFAP-Cre statement is mouse (Gfap-cre 77.6, P17 to P18 imaging, survival followed to about 120 days by the x-axis of Fig 1O). Add "rat" and "mouse".
3. "(control 8, knockout 9)": the legend gives these n for panels N and M (weight and appearance); the survival panel O has no n of its own (the "P-value 1.0" sentence is shared). Add "n for the weight and appearance panels; survival n not separately stated".
4. "the authors say a cell-autonomous astroglial function is not excluded": the Discussion says "though we cannot exclude the cell autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders" (rep.txt, Discussion). Add "in other neurological disorders" and "(oligodendrocytes as well)".

CHECK CLASS:
- Wwox in microglia (staining null): CHECK PRESENT. In-study check yes. Same antibody (HPA050992), same PND 21 +/+ sections, Wwox signal in NeuN neurons, APC oligodendrocytes and GFAP astrocytes (Fig 6A-C; Results 2.3). Caveat: representative images only; no Wwox-null section control in Fig 6.
- GFAP-Cre deletion (phenotype null): CHECK PRESENT. In-study check yes. Supp Fig 1F (File009.pdf page 7): WWOX signal absent in GFAP-positive cells of G-KO versus sparse faint signal in G-Control, P18. Weak points: G-Control signal is itself faint, a single field per genotype, no quantification, no later time point. The recombination is therefore shown but not its completeness.

Numbers recomputed: counts 8 and 9 only (as printed in the legend). Nothing else computable. n = 8 and 9 are mice (the replicate unit).

---

## DA-K01-008 (Lucas-Clarke 2026, Drosophila, sima:GFP)

**VERDICT: ADD.**

Checked and right: t = 0.6623, P = 0.5185, "N = 7-9" (Results; legend "N = 7-9 brains"). Recomputed: two-sided P for t = 0.6623 is 0.5185 at 14 degrees of freedom (0.5203 at 12, 0.5193 at 13, 0.5178 at 15, 0.5172 at 16), so the printed P fits two groups of 7 and 9 (16 brains). The Results say "endogenously tagged sima:GFP"; the legend says "endogenously tagged Sima:GFP reporter"; Methods say "the genetically encoded reporter line UAS-sima:GFP"; the stock table lists w[1118];PBac{y[+mDint2]w[+mC]=sima-GFP.AC.FPTB}VK00037, "sima:GFP, BDSC 42672, GFP tagged sima (2nd chromosome)". All right as quoted. "Not measured under hypoxia, not measured without the transgene": no hypoxia experiment appears in the main XML or the two supplement text files (only "Hypoxanthine" in a metabolomics row, Supplementary_tables_derived.txt line 724). Right.

Wording to add or change:
1. "(a driver-expressed transgene, whose level reports protein stability and not transcription)" is presented as the reading of the Methods name only. The experiment genotype rows in Supplementary Table 1B read "elav-GAL4;sima:GFP/+;Wwox TRiP/TM3/Aβ42" with no UAS; the stock is a PBac insertion of a genomic-tagged construct, not a UAS line. So the "UAS" reading is one of two readings, not established. Add "if the Methods' UAS-sima:GFP is meant; the genotype table shows no UAS element".
2. "The authors attribute the lactate rise to Atf4": the Results say "this could be the mechanism via which Ldh and lactate are upregulated"; the Discussion says "our data suggest that Atf4, rather than the HIF1α orthologue sima, is primarily responsible for the observed Ldh upregulation". Replacement: "The authors suggest Atf4, not sima, as the likely route to the Ldh and lactate rise (hedged: 'could be the mechanism')".
3. Readout geometry. Methods: fluorescence "averaged across four equal sized (415.1 µm 2) ROIs" per brain, unfixed brains, day 14 females. This is four small ROIs per brain, not a whole-brain measure (the row's endpoint says "whole-brain ROI"). Add "four ROIs of about 415 µm2 per brain; replicate unit = brain".
4. "Sima is the single fly HIF-alpha" and "the only neural HIF-alpha protein readout in a WWOX-loss model": not stated in the held paper (it calls sima "HIF1α homolog/orthologue"). NOT CHECKED against held sources; the second is a literature-scope claim that no held file can support.

CHECK CLASS: manipulation = elav-GAL4 > Wwox TRiP (BDSC 51747) knockdown with Aβ42.
- Knockdown itself: CHECK PRESENT BUT NOT MATCHED. Supplementary Fig 1 (legend in Supplementary_material_derived.txt): qPCR of Wwox mRNA, fly heads, elav-GAL4>TRiP, newly eclosed females, N = 3 replicates of 15 heads, "*** p < 0.001"; different age (day 0 versus day 14), no Aβ42, whole head not dissected brain. Figure image not viewed (legend only).
- Same manipulation, same preparation: Atf4 immunostain is up in the same genotype and age (day 14 brains, Aβ42, Wwox TRiP; U = 0, P = 0.0022, N = 6; Fig 5H-I), and metabolomics/lactate at day 14 (Fig 5A-C). That is an effect of the same manipulation at the same age in the same tissue, in separate fly cohorts (Table 1B lists them as separate rows).
- Reporter responsiveness (can sima:GFP move at all?): CHECK ABSENT. No hypoxia, no sima manipulation, no positive control in the held bytes (query: "hypox", "sima" in main XML, Supplementary_material_derived.txt, Supplementary_tables_derived.txt, searched 2026-11-25). A control showing only that the readout can move would be an assay control, not an activity check; none exists either.
In-study check: yes for knockdown effect (Atf4, lactate, head qPCR not matched), no for reporter responsiveness. Locators: Fig 5H-I; Supp Fig 1; Supp Table 1B rows "5F-G".

Numbers: t-test P recomputed (above). Atf4 U = 0, N = 6 per group: exact two-sided Mann-Whitney P = 2/C(12,6) = 0.00216, printed 0.0022; consistent if 6 v 6 (not stated per group). Fig 5G figure image is not held (XML only); no value read by eye.

---

## DA-M01-002 (Steinberg 2026, human organoids, MYC+ of SOX2+)

**VERDICT: MUST CHANGE** (last clause; also two ADD items).

Checked and right: medians read by eye from Fig 3K (accepted-manuscript PDF page 34, rendered at 450 dpi and cropped, figure held): wild type about 19, WWOX-KO about 68, SCAR12 about 47, WOREE about 55 percent; the sentence's 18/68/45/55 agrees within reading error. Significance bars on the figure: KO ***, SCAR12 **, WOREE **** versus wild type (one-way ANOVA with Tukey, legend).

MUST CHANGE:
- "SCAR12 is the clean dissociation case, so the MYC rise is present without that composition phenotype". The same paper reports a composition phenotype in SCAR12 by immunostaining. Results (before Fig 2): "At week 7 ... a significant reduction in SATB2-positive cells concurrent with an expansion of the SOX2-positive population in WWOX-mutant organoids ... genotype-dependent gradient ... KO most pronounced, followed by WOREE and SCAR12". Fig 1F (PDF page 32, viewed at 450 dpi): SOX2+/nuclei, SCAR12 median about 47% versus wild type about 13% (stars between WT and SCAR12), SATB2+/nuclei SCAR12 about 1% versus wild type about 7% (***). So SCAR12 does have a week-7 protein-level composition shift. The "wild-type-like" statements in the sentence are for the week-16 scRNA-seq (Fig 2D-F; text "SCAR12 organoids ... exhibited an RG population similar to WT"; "this was not the case in our patient-derived organoids" for the neuron decrease) and for CTIP2/SATB2 in Fig 6B (text: SCAR12 "similar to WT"). Replacement: "In SCAR12 the week-16 scRNA-seq radial-glia and neuron fractions are wild-type-like (Fig 2D-F) and CTIP2/SATB2 are wild-type-like (Fig 6B), but the week-7 immunostaining shows SOX2+ increased and SATB2+ decreased versus wild type (Fig 1F); MYC (Fig 3K, week 16) is raised in all three, so SCAR12 is a partial, time-dependent dissociation, not a clean one."

ADD:
1. "SCAR12 overlaps the wild-type lower tail": by eye in Fig 3K the SCAR12 lower quartile and lower whisker (about 20% and about 12%) reach into the wild-type upper half (wild-type box about 9 to 31%, median about 19%); the wild-type lower tail (0 to about 9%) is not reached. State instead: "SCAR12's lower whisker overlaps the wild-type interquartile range".
2. Replicate unit and statistics. Legend: "WT n=7 organoids; WWOX-KO n=5; SCAR12 n=8; WOREE n=11 ... one-way ANOVA with Tukey" and "Data represents biological and technical replicates". By eye the dots in Fig 3K are more numerous than the organoids (very roughly 20+ WT, 8 KO, 30 SCAR12, 40 WOREE), so the dots are not organoids and the stars may rest on fields or sections pooled across organoids. Add "n = 7/5/8/11 organoids; plotted points more numerous than organoids, unit not stated; one laboratory not checked".

CHECK CLASS (manipulation = WWOX loss/variant in SCAR12 organoids): CHECK PRESENT. In-study check yes: SCAR12 lines show reduced WWOX by immunoblot in week-16 organoids (Supp Fig 1M, legend in File010.txt; blot not viewed), hyperexcitability (Fig 1D), the MYC rise itself (Fig 3K), and the week-7 SOX2/SATB2 shift (Fig 1F). Same system and lines; time points differ (week 7 versus week 16).

Numbers: medians by eye only (figure held and viewed: PDF page 34 and page 32). "One laboratory": NOT CHECKED. "WOREE shows reduced CTIP2 and SATB2, Fig 6B": text confirms; Fig 6B image not viewed. Species: human iPSC/hESC-derived organoids.

---

## DA-W2-002 (Breton 2021, mouse neuron-specific Wwox knockout, mEPSC)

**VERDICT: ADD.**

Checked and right: "10 cells per genotype from 4 wild-type, 5 heterozygote and 5 knockout animals" (legend Fig 4: S-WT N = 10 cells, 4 animals; S-HT N = 10, 5; S-KO N = 10, 5). Amplitude KO versus WT p = 4.9906e-07, KO versus HT 1.3306e-06 (KS). Frequency: WT versus KO p = 2.4054e-04, HT versus KO 0.5963. Decay: "S-WT 5.18 ± 0.78 ms; S-KO 4.84 ± 1.11 ms; p = 0.2982", authors' reading "no overt change in the proportion of the NMDAR:AMPA response". Holding potential -70 mV with TTX 1 µM. Recording ACSF contains 1.3 mM MgSO4 (Methods 5.2), supporting the inference of Mg block at -70 mV. Direction of the frequency difference is indeed not stated in the text; in Fig 4C (gr4.jpg held, enlarged and viewed) the WT, HT and KO curves are visually almost superimposed and no direction can be read by eye.

ADD:
1. The heterozygote also differs from wild type on both measures: amplitude WT versus HT p = 1.98e-04 and frequency WT versus HT p = 0.0018 (legend). The frequency "difference" KO versus WT is therefore matched by an HT versus WT difference with KO equal to HT; it cannot be read as a knockout effect (wild type is the odd group, 4 animals). Add this clause.
2. "KS test on pooled events" is an inference: the paper says only "KS test" on cumulative probability plots made with ecdf; the very small p values (as low as 1e-135 for sIPSC in the same figure) imply events as the unit, but the text does not say so. The cell-level test is reported only for decay (WT versus KO, test, error type and n not stated; HT not given). Add "event-level KS; decay compared WT versus KO only, test and n not stated".
3. The paper's text cites "Fig. 4C" for amplitude; the legend assigns amplitude to 4B and frequency to 4C (labelling mismatch in the source).
4. "no NMDAR current was measured": true for the mEPSC recordings. The paper does show an NMDAR-dependent component elsewhere: the delayed evoked field response in S-KO is suppressed by d-APV 50 µM (Supp Fig S3C; n = 6 slices, 3 animals) and bursts are NMDAR dependent. Add "an NMDAR-dependent component was shown in evoked field recordings, not in the mEPSC".
5. Isolation of mEPSCs: only TTX is stated; no GABA-A blocker is named in the held text (grep: picrotoxin, bicuculline, gabazine absent). Add "isolation from mIPSCs not described".

CHECK CLASS (manipulation = Synapsin-Cre Wwox deletion, S-KO): CHECK PRESENT BUT NOT MATCHED for the loss of the protein (not shown in this paper; floxed allele cited to Abdeen 2013, Cre line by JAX stock number; the knockout characterisation sits in a different paper) and CHECK PRESENT for an effect of the same manipulation in the same cells (mEPSC amplitude shift; the same slices show bursting; sIPSC amplitude and frequency changed in Fig 4H). In-study check: effect yes (Fig 4B, 4H); protein-loss no. Locator: Fig 4 (gr4.jpg), legend p values.

Numbers: all printed p values and n agree with the legend; none recomputed (KS needs event-level data, not held). Species mouse; the replicate unit for KS is the event (pooled), for animals the legend gives n.

---

## DA-J01-008 (Hussain 2023, P47T heterozygote, Iba1/Gfap)

**VERDICT: STANDS.**

The text (Results 2.5): "evaluations of both Iba1 and Gfap immunostainings were also performed in brain samples from Wwox P47T/WT mice; however no differences were observed when compared with the wildtype mice (data not shown)". The sentence quotes this correctly and its conclusion follows. The heterozygote is absent from Fig 3 (legend: WT/WT and P47T/P47T, n = 3 mice/group, 80 and 250 days), from Fig 4 and from Supp Fig S5 (legend: WWox WT/WT and P47T/P47T only; File "Supplementary_figures.pdf", page with S5 viewed as text). The numbers behind the heterozygote statement (age, n, metric) are not given anywhere in the held bytes. Optional ADD for a reader: "heterozygote age, number and metric not given; homozygote versus wild type shown at 80 and 250 days, n = 3 per genotype".

CHECK CLASS: CHECK ABSENT for the heterozygote readout (no heterozygote Iba1 or Gfap data in the held bytes; queried 2026-11-25: "P47T/WT" and "heterozyg" in the XML, Fig 3/4 legends and Supp S5 legend, and "Iba1/Gfap/P47T/WT" in Supplementary_data_all_sheets_derived.txt, which carries only a GFAP transcript row). In-study check: no. The homozygote showing increased Iba1/Gfap in the same stains (Figs 3 and 4) is an assay control showing the stain can detect gliosis in this line, not an activity check for the heterozygote genotype. Elsewhere the heterozygote shows an intermediate behavioural phenotype (Fig 2a,b) and a non-significant survival reduction (Fig 1b), which shows the allele is not inert in one copy, but nothing about glia. Mouse. Numbers: n = 3 per genotype from Fig 3 legend; nothing printed in the sentence to recompute.

---

## DA-J01-002 (Hussain 2019, Wwox-null hippocampus, IBA1/GFAP area fraction, Il6/Tnf-a)

**VERDICT: ADD.**

Checked and right (XML held; figure and supplement folders are empty, so no figure image is held):
- "Area fraction, not cell number": Results 3.2 and Methods use AF of IBA-1+ and GFAP+ structures (the Discussion loosely says "increased detection of IBA-1+ cells").
- "Results 3.3 reads '( Il6 significant at p < .05)'": verbatim, "We observed > 1.5 fold upregulation of both cytokines ( Il6 significant at p < .05) in Wwox KO ( n = 4) mice in comparison to Wwox WT (n = 4) mice ( Fig. 4 E )".
- Abstract: "overexpression of inflammatory cytokines Tnf-a and Il6"; Discussion: "increased expression of inflammatory cytokines Tnf-a and Il6". Both say both are increased. Right.
- "the paper records no seizure measurement for these animals and leaves cause versus consequence open": no seizure recording in the held text; Discussion: "further investigation is needed to gather additional mechanistic insight on what is cause or consequence upon Wwox loss of function". Right.

ADD:
1. "Il6 about 1.48x ... Tnf-a about 1.85x with a large error bar and no mark" are readings of Fig 4E. NOT CHECKED: the figure image is not held in any file I was given (figure folders empty). The text says "> 1.5 fold ... both cytokines", which sits against an Il6 reading of 1.48; the sentence should say the 1.48 and 1.85 are figure readings that conflict slightly with the text's ">1.5 fold" and cannot be re-read from the held bytes. The legend gives one asterisk definition ("* p value < .05") without naming the bar.
2. "Tnf-a ... no mark": by the text, only Il6 is called significant; Tnf-a's non-significance is by implication (no p value is given for it). Say "no significance is claimed for Tnf-a".
3. Add n and unit: IBA-1 n = 6 WT v 6 KO; GFAP n = 8 KO v 6 WT; qPCR n = 4 v 4 (mice, 2-week-old, controls Cre+ Wwox wt/wt littermates, both sexes, hippocampal tissue, Gapdh, two-tailed unpaired t). Dentate gyrus: text says "marginally higher" for IBA-1 AF and "marginal" for GFAP, so "unmarked" should read "marginal, not marked as significant".
4. The history clauses ("full text re-read 2026-10-31 (IT10 P2.2...)", "corrects the 2026-10-30 'correction'") are repository history and are NOT CHECKED against any held file.

CHECK CLASS (manipulation = germline Wwox knockout via BK5-Cre, 2 weeks): CHECK PRESENT BUT NOT MATCHED for the cytokine null. In-study check: partly. The held paper does not show Wwox mRNA or protein loss in these animals (KO generation cited to earlier papers). Effects of the same manipulation in the same tissue exist: AF changes, PV and NPY loss, Gad65/67 reduction in hippocampi, and qRT-PCR of Grin2c, Grm3, Kcna2 in KO (n = 4) versus WT (n = 4) hippocampi, "*** p < .0001" (Fig 6D legend). The last is the same assay, species, n and tissue, though whether the same four animals is not stated. Locators: Fig 4E, Fig 6D legend, Methods 2.10.

Numbers: n values as printed; fold changes by eye cannot be checked (figure not held). Mouse; the replicate unit is the animal (qPCR in triplicate technical).

---

## DA-M01-007 (Repudi 2021, conditional deletions)

**VERDICT: MUST CHANGE** (one false statement; one overstatement).

MUST CHANGE:
1. "the Synapsin-Cre survival age is not stated" is false. The Results (operator-supplied PDF and the browser-print copy, both held) say of S-KO: "Phenotypic analysis of conditional ablation of WWOX in neuronal cells revealed growth retardation (Fig. 1G and H), and premature death (Fig. 1I) by the age of 3-4 weeks, phenocopying the N-KO and Wwox-null mice"; the abstract says "N-KO or S-KO ... exhibited severe epilepsy, ataxia and premature death by 3-4 weeks". The Kaplan-Meier panel (Fig 1I, S-Control n = 13, S-KO n = 15, log-rank P = 0.0001) shows all S-KO deaths between about day 17 and day 28 by eye (figure held, page 6 rendered). Replacement: "death by 3-4 weeks is stated for both nestin-Cre (100%, n = 14, Fig 1F) and Synapsin-Cre (n = 15, Fig 1I)".
2. "oligodendrocyte and astrocyte deletion do not [reproduce growth retardation, seizures and premature death]". Measured for O-KO and G-KO: delay, weight and survival (Fig 1J-O; O-KO n = 10 v 11, G-KO n = 9 v 8) and, for O-KO only, hind-limb clasping (Supp Fig 2D). No seizure or EEG record for either (seizure video and electrophysiology are shown for N-KO and S-KO only). The authors write "observed no phenotype abnormalities". Replacement: "do not reproduce growth retardation or premature death (measured); seizures were not recorded for them; the authors state no phenotypic abnormalities".

Checked and right: N-KO: growth retardation (Fig 1D-E), "tremors/seizures (Supplementary Video 1)", 100% dead by 4 weeks (n = 14 v 12). S-KO: growth retardation (Fig 1G-H); "uncontrolled spontaneous tonic-clonic seizures beginning at P9 ... 68.5 ± 13.4 s; n = 6 of P14-18"; cortical bursting in 86% of S-KO slices (36 of 42 slices, 24 animals). "Radial-glia state and MYC were not measured in these mice": no "MYC", "radial" or "SOX2" in the article text; right. "Progenitors largely WWOX-intact under Synapsin-Cre is an inference": the paper measured loss in NeuN neurons (Supp Fig 1C) and intact WWOX in CC1 oligodendrocytes of S-KO (Supp Fig 1D); progenitors are not stained under Synapsin-Cre. Right; add "oligodendrocyte WWOX intact was measured, progenitors were not".

CHECK CLASS (nulls = O-KO and G-KO phenotype): CHECK PRESENT. In-study check yes: Supp Fig 1E (O-KO: WWOX absent in CC1+ cells, arrowheads, P18) and Supp Fig 1F (G-KO: WWOX absent in GFAP+ astrocytes, P18); File009.pdf page 7 viewed. Limits: representative field, no quantification, G-Control WWOX signal faint, imaged at P18 while the null survival runs to about 120 days. The nestin and Synapsin positive effects show the Cre-flox system works in the same colony.

Numbers: n values all as in the legend; ages by eye from Kaplan-Meier; none recomputed. Mouse; unit mouse.

---

## DA-L01-001 (Hussain 2019, Il6 and Tnf-a qRT-PCR, Fig 4E)

**VERDICT: ADD.**

Checked and right (text only): the quotation is verbatim; significance is attached to Il6 only; "two-tailed unpaired Student's t, Gapdh, 2-week-old KO versus Cre-positive littermates, n 4 v 4" (Methods 2.1 and 2.10: controls "Cre+; Wwox wt/wt littermates", KO and age-matched controls at 2 weeks; "After normalization to Gapdh ... Student's two-tailed unpaired t-test"); the abstract and Discussion say both cytokines are increased. "Absence of a significance mark is not absence of an effect": sound, with n = 4.

ADD:
1. "the figure shows Il6 about 1.48x with one asterisk and Tnf-a about 1.85x with a large error bar and no mark": NOT CHECKED. No figure image is held in the files given (both figure folders empty). The text itself says "> 1.5 fold upregulation of both cytokines"; a 1.48 reading for Il6 contradicts that by a small margin. Say that the two values are figure readings that cannot be verified from the held bytes and that the text states more than 1.5 for both.
2. "Il6 is the only significant cytokine; Tnf-a is a non-significant increase": by the text, significance is claimed for Il6; Tnf-a's non-significance is implied (no p stated). The "increase" for Tnf-a is the authors' claim ("> 1.5 fold") and the figure reading; it is not tested as significant.
3. "This corrects the IT9 P1 'correction'": repository history, NOT CHECKED.
4. State species and unit: mouse, hippocampal tissue, animals n = 4 per genotype, triplicate technical wells (Methods 2.10).

CHECK CLASS: same as DA-J01-002. CHECK PRESENT BUT NOT MATCHED (no Wwox mRNA/protein loss shown for these animals in the held paper; other qRT-PCR targets in the same type of hippocampal RNA, Grin2c/Grm3/Kcna2 at n = 4 v 4, moved with *** p < .0001, Fig 6D legend, which shows the assay and animal group can detect expression changes; whether it is the same four animals is not stated). In-study check: effect of the same manipulation in the same tissue yes; direct knockout confirmation no.

Numbers: n = 4 v 4 as printed; fold values not recomputable (figure not held).

---

## Summary table

| id | class | in-study | verdict |
|---|---|---|---|
| DA-J01-006 | CHECK PRESENT (Wwox-in-microglia staining, rat; GFAP-Cre deletion, mouse) | yes (Tochigi Fig 6A-D; Repudi Supp Fig 1F) | ADD |
| DA-K01-008 | CHECK PRESENT BUT NOT MATCHED for knockdown (head qPCR, newly eclosed, no Aβ42); same-manipulation effect present (Atf4); reporter responsiveness CHECK ABSENT | knockdown effect yes; reporter no | ADD |
| DA-M01-002 | CHECK PRESENT | yes (Fig 1D, 1F, 3K; Supp Fig 1M legend) | MUST CHANGE |
| DA-W2-002 | CHECK PRESENT BUT NOT MATCHED (protein loss not shown here; effect shown in same cells) | effect yes; protein loss no | ADD |
| DA-J01-008 | CHECK ABSENT (no heterozygote Iba1/Gfap data held) | no | STANDS |
| DA-J01-002 | CHECK PRESENT BUT NOT MATCHED | partial (same-tissue effects yes; KO confirmation no) | ADD |
| DA-M01-007 | CHECK PRESENT (O-KO, G-KO deletion shown, representative only) | yes (Supp Fig 1E, 1F) | MUST CHANGE |
| DA-L01-001 | CHECK PRESENT BUT NOT MATCHED | partial (Fig 6D same assay; KO confirmation no) | ADD |

One-line reasons:
- DA-J01-006 ADD: GFAP staining is in Supp Fig 1F (as astrocyte marker, not a reactivity measure); rat and mouse unlabelled; n 8/9 belongs to the weight and appearance panels; "not excluded" is "in other neurological disorders".
- DA-K01-008 ADD: genotype table shows no UAS element (the driver-expressed reading rests on the Methods name only); the authors say Atf4 "could be" the mechanism for Ldh/lactate; readout is four ROIs per brain; no reporter-responsiveness control.
- DA-M01-002 MUST CHANGE: Fig 1F shows SCAR12 week-7 SOX2+ up (about 47% v about 13%) and SATB2+ down (***), so SCAR12 is not a clean dissociation case; the wild-type-like fractions are week-16 scRNA/CTIP2/SATB2; also the overlap wording is reversed and plotted dots exceed organoid n.
- DA-W2-002 ADD: heterozygote also differs from wild type in amplitude (p 1.98e-4) and frequency (p 0.0018), so the KO-v-WT frequency difference is not a KO effect; KS is event-level by inference; isolation from mIPSC and Wwox-loss confirmation not in the paper.
- DA-J01-008 STANDS (optional: heterozygote age, n and metric are not given).
- DA-J01-002 ADD: Il6 1.48x / Tnf-a 1.85x are figure readings not verifiable here (figure not held) and sit against the text's "> 1.5 fold" for both; n per stain differs (6 v 6, 8 v 6, 4 v 4); dentate gyrus is "marginal" in the text.
- DA-M01-007 MUST CHANGE: Synapsin-Cre death "by the age of 3-4 weeks" is stated (Results, abstract, Fig 1I); and "oligodendrocyte and astrocyte deletion do not" reproduce seizures is unsupported because no seizure or EEG data exist for them.
- DA-L01-001 ADD: the 1.48x / 1.85x values are figure readings not verifiable from held files and conflict slightly with the text's "> 1.5 fold"; Tnf-a non-significance is implied, not stated.

---

## Files opened (all inside the named sets)

Read as text or via extraction:
- /home/desktop/legend-development/files/fulltext/PMID31340538_Tochigi2019_PMC_r2.xml
- /home/desktop/legend-development/files/figures/PMID31340538_r2/ijms-20-03596-g006.jpg (viewed)
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied.txt and .pdf (pdftotext whole; pages 6 and 7 rendered and viewed)
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_OUP_browserprint_pdftotext.txt (grep only)
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_Brain_operator_supplied_supplement/extracted/awab174-suppl_data/brain-2020-02464-File009.pdf (page 7 rendered and viewed) and .txt (legend lines)
- /home/desktop/legend-development/files/fulltext/PMID42909904_PMC13684411.xml
- /home/desktop/legend-development/files/fulltext/PMID42909904_supplement/Supplementary_material_derived.txt and Supplementary_tables_derived.txt (grep and line ranges)
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-AM.pdf (pages 32, 33, 34 rendered and viewed; Fig 3K and Fig 1F cropped at 450 dpi) and PMID42397075_Steinberg2026_OUP-AM_fitz.txt
- /home/desktop/legend-development/files/fulltext/PMID42397075_Steinberg2026_OUP-Supplement/brain-2025-03809-File009.txt, File010.txt (legends), File008/011/012 only by grep over the txt files
- /home/desktop/legend-development/files/fulltext/PMID34634460_Wwox_osc2021_PMC_r2.xml
- /home/desktop/legend-development/files/supplement/PMID34634460_r2/mmc1_text.txt
- /home/desktop/legend-development/files/figures/PMID34634460_r2/gr4.jpg (enlarged and viewed)
- /home/desktop/legend-development/files/fulltext/PMID36828035_Hussain2023_PMC.xml
- /home/desktop/legend-development/files/supplement/PMID36828035/NIHMS1957654-supplement-Supplementary_figures.pdf (pdftotext) and Supplementary_data_all_sheets_derived.txt (grep)
- /home/desktop/legend-development/files/fulltext/PMID30290271_Hussain2019_PMC_r2.xml
- Directory listings only: figures/PMID30290271_r2 (empty), supplement/PMID30290271_r2 (empty), figures/PMID36828035/supp_pages (not opened).

Not opened: the PDF of Hussain 2023, the Hussain 2023 figure pages, the Steinberg Fig 6B and Fig 2 beyond the page render, the READING_NOTE and receipt files in the Steinberg supplement folder (not named), Tochigi figures other than g006.
