# Blind report on sentences S1 to S8 (ADV-285 census), independent checker, 2026-11-25

Hypothesis-level reading of published papers; not medical advice. Scope limit: only the files named in the dispatch were opened (list at the end). The two PDFs/XML were read as untrusted data with python3 -I -P -E scripts in the work folder. Where I could not check something it says NOT CHECKED.

## Summary table

| Sentence | Verdict | One-line reason |
|---|---|---|
| S1 | MUST CHANGE | Numbers match the sources, but "N1 (myelinated-fibre)" and "N2 (unmyelinated-fibre)" are not stated by Repudi (recorded in neocortical layer V, no fibre class defined); the n order (5 against 6) is reversed against the legend; +- is SEM, not SD; control n may be a copy |
| S2 | STANDS | Both statements are supported (no drug arm for the readout; muscle response in a model with peripheral demyelination; slices counted, not animals). Optional addition: heterozygote latency is prolonged with myelin "similar" |
| S3 | ADD | Zero is consistent with the table row W4 (PubMed 1, Europe PMC 1, both the mouse paper), but the search string is only partly named and omits common neurophysiology terms; Obeid 2026 (W3) was not audited |
| S4 | ADD | 13 = 5 central + 8 peripheral is correct by row and PMID count; but the 13.7 against 42.9 m/s is an untreated genotype difference, not a 4-AP effect; legend says P < 0.001 while text says P < 0.01 for the same t(29) = 4.3; four of the 13 are patient studies, not models; 11 genetic-medicine papers are excluded |
| S5 | MUST CHANGE | Clause "cannot be assumed to move in the direction of a structural myelin count" is contradicted by Palma: EM myelinated axons were fewer and N1 slower (same direction); what diverged was the mature-oligodendrocyte count |
| S6 | ADD | Abstract wording matches; needs "CAP amplitude, not velocity", genotype not stated in the abstract, and the "none" is a title/abstract census result |
| S7 | MUST CHANGE | "The one measurement that would separate the explanations" is not logically true: neuron-dependent and non-myelin explanations make the same N1 predictions; needs the g-ratio and a seizure/hyperexcitability alternative; the paper already reports O-KO with no gross phenotype and no major MBP change at P17 |
| S8 | MUST CHANGE | v2 does carry the Cheng 2020 Tc-MEP values of the global null (add-on 5(f), as a heterozygote carrier candidate); "never in vivo" is in the slice package v2, not in the pup brief text |

---

## S1 — MUST CHANGE

Parts: (a) Cheng 2020, Fig 2 numbers; (b) Repudi 2021, Fig 5D numbers; (c) the fibre-class labels.

### (a) Cheng 2020 — values re-read, all match
Source: PMID32000863_Cheng2020_PMC_r2.xml, Results "Nerve degeneration and demyelination in Wwox-/- mice", and the image 40478_2020_883_Fig2_HTML.png (viewed, 1418x1576).
Species and design: mouse, global Wwox+/+, +/-, -/-, 3 weeks of age, in vivo, chloral hydrate anaesthesia, scalp stimulation, needle recording in intrinsic plantar muscles of both forelimbs.
- Amplitude: +/+ 59.2 +- 9.0 microvolt (n = 10); -/- 11.8 +- 5.4 (n = 4), P < 0.05; +/- 59.6 +- 17.2 (n = 5), n.s. Text matches S1.
- Onset latency (Results wording): +/+ 1.39 +- 0.13 ms; -/- 2.44 +- 0.37 ms, P < 0.01; +/- 2.13 +- 0.22 ms, P < 0.05 against +/+; +/- against -/- n.s. (Fig 2c).
- Figure check: bar heights and one-sided error bars in Fig 2b and 2c agree with the text (WT amplitude bar about 59.5, error to about 68.5; KO 11.8 to about 17.5; latency WT about 1.4, KO about 2.45 with error to about 2.8). The legend of both panels reads N = 10 / 5 / 4, so the same 4 against 10 applies to latency and amplitude (S1 wording is right).
- ADD: "+-" is SEM (legend: "means +- SEM"; Methods: "standard error of the mean"; test: one-way ANOVA). SD would be 10.8 (KO amplitude, n = 4) and 28.5 (WT, n = 10) if converted; S1 should print "SEM".
- ADD: the Methods define latency as "from the onset of the electrical shock artifact to the major positive peak"; the Results call it "onset latency". The source is inconsistent; S1 uses the Results word. Suggested: "latency (artefact to major positive peak per Methods; called onset latency in Results)".
- Unit: N is described in the legend as N only; both forelimbs were recorded ("bilateral"); the paper does not state whether the value per animal is an average of the two sides. NOT CHECKED beyond the legend.

### (b) Repudi 2021 — values re-read
Sources: PMID33914858_Repudi2021_OUP_browserprint_pdftotext.txt (Results, Fig 5 legend, Methods) and page 27 of the PDF rendered at 200 dpi (whole page) and 400 dpi (crop of panel 5D(ii)), viewed.
Species and design: mouse, Synapsin-Cre; Wwox flox/flox (S-KO) against Wwox +/+ ; Synapsin-Cre (S-Control, Cre-positive), acute slices, mice P13 to P17 (Methods: "aged P13 to P17"; the census table W1 says P13-P18, which does not match), callosal stimulation, recording in neocortical layer V, "at a vertical distance of 250 micrometre from the stimulator" (one distance).
- Figure read, panel 5D(ii): axis calibrated on the tick marks (0, 5, 10, 15, 20 ms at crop rows 636, 488, 339.5, 190, 42). N1 latency: S-Ctrl about 2.45 ms, S-KO about 3.15 ms (mean lines); N2 latency: S-Ctrl about 6.7 ms, S-KO about 8.3 ms (S-KO has two points at about 14.6 and 16.2 ms and one control at about 13 ms). Panel (ii) shows "*" over N1 and "n.s." over N2. So "about 3.2 against 2.5 ms" is right; N1 P = 0.0104 and N2 P = 0.5737 (Wilcoxon rank sum) are in the legend and agree with the star and n.s. in the panel.
- n: legend "n = 8 slices, five subjects; S-Control; n = 8 slices, six subjects S-KO". Tests are over slices.
- The N2 result: the KO mean is about 1.6 ms longer than control, with huge scatter; "not different (P = 0.5737)" is absence of significance with 8 slices per group, not evidence of equality. ADD "numerically about 8.3 against 6.7 ms, n.s., wide scatter".

### MUST CHANGE words and why
1. "N1 (myelinated-fibre) latency ... N2 (unmyelinated-fibre) latency" — the held Repudi text and legend never define N1 or N2 as myelinated or unmyelinated fibres (searched: no occurrence of "myelinated fibre" or a definition; the Results say only "latency of neural conductivity ... consistent with impaired myelination" and "amplitude ratio of N1 and N2"). The Methods describe layer II/III LFP recording after layer V stimulation; the callosal-stimulation, layer V-recording protocol is not described in Methods. The responses are recorded in cortex, not as a callosal compound action potential in white matter (the Palma paper, where the N1 = myelinated and N2 = "partially myelinated" (Methods) / "unmyelinated" (Results) convention comes from, records inside the contralateral corpus callosum at four distances). Replacement: "the latency to the first (N1) and second (N2) peak of the response in neocortical layer V to callosal stimulation (the paper does not say which fibre class each peak is; by analogy with callosal CAP work N1 is usually read as the myelinated and N2 as the later, unmyelinated or partly myelinated, component)".
2. The n clause "8 slices from 5 animals against 8 slices from 6" follows a "KO against control" order (3.2 against 2.5; 11.8 against 59.2) and so reads as KO 5, control 6, which is the reverse of the legend (control 5 subjects, KO 6 subjects). Replacement: "8 slices from 5 control mice, 8 slices from 6 knockout mice".
3. ADD (n provenance): the same legend numbers appear in the Fig 2F legend of the same paper as "S-HT, n = 8 slices, five subjects; S-KO, n = 8 slices, six subjects" (S-Control there is 6 slices, three subjects). The control n of Fig 5D equals the S-HT n of Fig 2F, so a copied n cannot be excluded (the pup brief v2 states the same doubt). Add "the control n equals the S-HT n in Fig 2F, possible copy".
4. ADD: control mice carry the Cre transgene (S-Control is Wwox +/+ ; Synapsin-Cre +).

NOT CHECKED: whether other held Wwox papers (for example the Obeid 2026 gene-therapy paper, row W3, "NOT AUDITED" in the table, or other held full texts) carry a conduction readout; the sentence's "two" is a statement about the audited held set only and should say so.

---

## S2 — STANDS

- "Neither has a drug arm for the functional readout": Cheng gives lithium chloride (60 mg/kg i.p., three times within 1 h) only before PTZ for seizure suppression (Methods "Induction of seizure"; Fig 7d); Tc-MEPs are untreated. Repudi has no drug at all in the held main text (searched "drug", "treated", "rescue", "inject": nothing relevant). Right.
- "A muscle response along the corticospinal tract and peripheral nerve in a model that also has peripheral demyelination": Cheng's own Results say Tc-MEPs "monitor the descending response that is propagated through the corticospinal tracts to cause a muscle contraction", recorded in forelimb plantar muscles; Fig 3 shows sciatic demyelination, onion bulbs, Schwann-cell apoptosis (N = 3). Right.
- "The slice comparison counts slices, not animals": legend and test (Wilcoxon over slices from 5 and 6 animals). Right.
- Optional clause a reader may want: in Cheng the heterozygotes have a prolonged latency (2.13 ms, P < 0.05) while sciatic "myelin thickness, axonal organization and density of myelinated fibers were similar in Wwox+/- and Wwox+/+ (data not shown)" — an unquantified hint that latency can move without a measured myelin change. Also Repudi S-KO mice seize from P9 (Results), so slices come from animals with seizures. Neither changes the verdict.

---

## S3 — ADD

Table check (W4, W3): 22 data rows and 45 unique PMIDs overall (counted by script). Row W4 states 0 patient reports; "S3: PubMed 1, Europe PMC 1" and "the only S3 hit (both routes) is W2" (Cheng 2020, mouse). So the sentence is consistent with its own table row. I could not re-run any search (no network); the search itself is NOT CHECKED.
What a reader needs: (1) the actual string and fields, date and counts per route, since the table gives only "WWOX or SCAR12 or WOREE with evoked potential, VEP, ABR, nerve conduction"; that list does not name SSEP, BAEP/BAER, "evoked response", electroneurography/EMG, ERG, "neurophysiology", "electrophysiology", so a report that wrote "brainstem auditory evoked response" or "nerve conduction studies were normal" in the abstract under other words might not match; (2) that MRI white-matter reports (five PMIDs under the table's S2) are not conduction results; (3) that Obeid 2026 (row W3, neuron-specific WWOX gene therapy, "enhanced myelination" in the abstract) was not audited. The sentence's own caveat about full-text-only reports is correct.
Suggested addition: "(string: WWOX or SCAR12 or WOREE with evoked potential, VEP, ABR or nerve conduction; terms such as SSEP, BAEP, EMG, ERG not searched)".

---

## S4 — ADD

### Count check (table rows and PMIDs, by script)
Group b rows A1 to A10. Central: A1 38427650, A2 25716865, A3 20127809 (rows with "CNS hypomyelination", 3 PMIDs) and A4 8880692, A5 38134864 ("CNS leukodystrophy", 2 PMIDs) = 5. Peripheral: A6 34382059 (1), A7 39816792 and 36798471 (2), A8 34889893 and 23250879 (2), A9 22388935 (1) = 6, plus A10 19427269 and 19909499 (2) = 8. Total 13, no duplicate PMID; "other twelve" = 12 (A2 to A10) correct. Read in full text: A1 only (open PMC XML, held as taiep_PMC10906851.xml). Counts are right.
I also read the abstracts of A2 to A10 (PMIDs 25716865, 20127809, 8880692, 38134864, 34382059, 39816792, 36798471, 34889893, 23250879, 22388935, 19427269, 19909499; abstracts file). Each has a drug or enzyme or antibody-type intervention and a conduction or evoked-potential readout. Classification points to flag:
- Four of the 13 are patient studies, not models (A4 digitalis, three boys with PMD; A5 curcumin, nine PMD patients, open label; A10 two ascorbic acid RCTs in CMT1A). S4 says "models ... exist".
- A3 is a dietary iron-deficiency hypomyelination model with a single intracranial apotransferrin injection; VEP latency and amplitude were "substantially normalized" (the table row omits the normalization).
- Null or negative drug results among the 13 that the sentence does not say: A5 "no clear improvement in brain MRI or ABR"; A10 both trials non-significant (MCV difference 1.7 m/s, P = 0.06; 1.3 m/s, P = 0.11); A8 curcumin derivatives raised CMAP but not NCV; A4 VEP shortening not significant, MEP still absent, BAEP waves restored except wave IV.
- Table source errors (not in the sentence): A2 abstract is J Neurosci 2015 (table says Cell Stem Cell); A3 is J Neurosci Res 2010 (table: Neurochem Res); A6 is Brain 2022 (table: JCI Insight); A11 Palma is Front Cell Dev Biol (table: Front Cell Neurosci). Table W1 age P13-P18 against Methods P13-P17.
- Exclusion: A15 (11 PMIDs, ASO, siRNA, CRISPR, AAV, gene transfer with a functional readout in hypomyelinating or CMT models) is excluded from the 13 as "genetic medicine". The sentence should say "13 ... not counting 11 genetic-medicine papers". I cannot check the PREREG that fixes this (not opened).

### The taiep paper (PMC10906851, PLoS One 2024) — values re-read
- Corticospinal conduction velocity 13.7 +- 0.6 (taiep) against 42.9 +- 1.2 m/s (wild type): Results and Fig 6 legend. These are untreated animals (the MEP section contains no 4-AP; 4-AP appears only in the SSEP and locomotion sections). The data are mean +- "E.E.M." (SEM) of eight subjects per group, adult male Sprague-Dawley rats, urethane anaesthesia, test t(12) = 42, P < 0.05. I cannot reproduce t(12) = 42: from the printed means and SEM with n = 8 per group I get t about 21.8 (df 14); with SD in place of SEM about 61.6. NOT a number in S4, but the reader should not infer a drug effect on velocity: S4 puts "4-aminopyridine in the taiep rat" directly before the velocities, and no velocity after 4-AP was reported.
- N2 after 4-AP (taiep): amplitude up and latency down. t(29) = 4.3. The Fig 3 legend gives P < 0.001; the Results text gives P < 0.01 for the same t(29) = 4.3. df = 29 with "eight subjects" implies recordings or sweeps, not animals, as the unit. The latencies are printed in "sec" (5.36 +- 0.03 to 5.06 +- 0.02), obviously ms. SSEP route in Results/legend is intravenous (1 mg/kg, jugular cannula); the table says i.p.; i.p. 1 mg/kg was used for the locomotor test. Design: within animal, saline first then 4-AP, recorded 90 min after.
- Figures not viewed.

Suggested replacement: "...One was read in open full text: in the adult taiep rat (hypomyelination, then demyelination) corticospinal conduction velocity is 13.7 +- 0.6 against 42.9 +- 1.2 m/s in wild type (untreated; mean +- SEM; 8 rats per group), and the N2 somatosensory response was larger and faster after intravenous 4-aminopyridine 1 mg/kg than after saline in the same rats (legend P < 0.001, text P < 0.01; df 29 with eight rats)."

---

## S5 — MUST CHANGE

### Palma 2022 (PMID 35372341; held XML; Front Cell Dev Biol 10:841548) — re-read
- Wild-type C57BL/6 mice, clemastine 50 mg/kg/day i.p. (10% DMSO vehicle) from P5 to P21 (Methods; the Results text says "postnatal day 5-20"). Slices at P21, callosal CAPs, four distances (500 to 2000 micrometre), velocity = slope of distance against latency.
- "N1 slower (P < 0.01, n = 10-12); N2 similar": Results text and Fig 2B legend (vehicle n = 12, clemastine n = 10 to 12; "for each mice, the average measure come from at least four different sections"): unit = animal. Right. No P value is printed for N2; "similar" means not significant. Numeric velocities are not in the text; Fig 2B not available as an image: NOT CHECKED.
- Statistics: "paired Student's two-tailed t-test" for two independent groups (Methods). Worth a clause.

### Is the comparison fair?
S5 does not claim equivalence; it sets two facts side by side and says so ("healthy developing wild-type mice", "demyelinated patients", "abstract level"). They are not comparable and the sentence does not need them to be: species (mouse against human), age (P5 to P21 against adults), state (healthy against chronic demyelinating optic neuropathy), route and dose (50 mg/kg/day i.p. against 5.36 mg orally twice daily, ReBUILD abstract), readout (slice CAP velocity, N1 against in vivo VEP P100 latency), design (parallel vehicle against crossover placebo). ReBUILD abstract text checked: "reduced the latency delay by 1.7 ms/eye (95% CI 0.5-2.9; p = 0.0048)", 50 patients, crossover. Right as worded.

### MUST CHANGE
"...and a conduction readout cannot be assumed to move in the direction of a structural myelin count." In Palma the structural myelin readouts moved in the same direction as conduction: TEM showed a reduced number of myelinated axons, thinner myelin in small axons (g-ratio), fewer nodes of Ranvier, a small MBP reduction (n = 3 mice per group for TEM, n = 6 for histology), together with slower N1. What diverged from conduction was the number of mature oligodendrocytes (CC1 positive cells increased) and, in the abstract, "the number of oligodendrocytes". In ReBUILD no structural count is reported. So the data support "a conduction readout cannot be assumed to follow the oligodendrocyte-differentiation count", not "the structural myelin count". Replacement: "...and neither conduction nor structural myelin can be assumed to follow an increase in mature oligodendrocytes (Palma: more CC1-positive cells, fewer myelinated axons and slower N1)."
Smaller point: "therefore ... needs a wild-type drug-only arm" is a design inference from one drug in one laboratory; add "for clemastine, one study".

---

## S6 — ADD

Abstract of PMID 29490274 (Cell Rep 2018) read: "exogenous glucose deprivation (EGD) abolished compound action potentials (CAPs), which neither lactate nor pyruvate could prevent. Loading an oligodendrocyte with 20 mM glucose using a patch pipette prevented EGD-mediated CAP reduction in about 70% of experiments." All three quoted facts match; the sentence already says "abstract level" (right).
Adds:
- The readout is CAP loss (amplitude), not conduction velocity or latency; "a conduction precedent" should say "CAP survival".
- The abstract does not state the genotype of the 70% experiments (it adds Cx47-lacking mice as a separate experiment); "wild-type tissue" is an inference. Say "mouse corpus callosum slices".
- The "none in a hypomyelinating model with a drug arm" is a result of the title and abstract census: in the table rows A1 to A10 none is an energy-supply intervention (A16 is the only energy row, and its three papers are wild-type callosum, rat optic nerve and rat spinal cord injury, none hypomyelinating). By the table the claim is supported; it should read "none found by title and abstract search".

---

## S7 — MUST CHANGE

### Logic of the predictions
Three explanations: neuron-dependent (non-cell-autonomous), OPC-intrinsic, non-myelin (axon calibre or excitability).
- Neuron-dependent: slow N1 in neuronal deletion; normal in OL-lineage deletion; restored on neuronal re-expression. Follows.
- OPC-intrinsic "the reverse": normal N1 in neuronal deletion, slow in OL-lineage deletion, not restored by neuronal re-expression. Follows, but it is not a full "reverse" of the middle term for a mixed model: a combined neuron plus OPC contribution predicts slow N1 in both deletions. S7 omits the mixed case.
- Non-myelin: "slow N1 with no g-ratio change in the same animals." Follows only if the g-ratio is measured; as written it needs electron microscopy in the same animals, which is not "one measurement".
- The central claim "the one measurement that would separate the explanations" is false as logic: the neuron-dependent and the non-myelin explanations both predict slow N1 in the neuronal deletion, normal N1 in the OL-lineage deletion and (if the neuronal cause is restored) restored N1 on re-expression. N1 velocity alone cannot tell them apart; the g-ratio and a myelinated-axon count in the same animals do. Replacement: "The primary measurement ... together with the g-ratio and myelinated-axon count in the same animals ...".
- A fourth alternative is missing: seizure or hyperexcitability. Repudi S-KO mice have "uncontrolled spontaneous tonic-clonic seizures beginning at P9" and the slices are P13 to P17; the neuronal re-expression arm also normalises seizures, so a restored N1 cannot separate "neuron-dependent myelination" from "seizure-dependent slowing". (The v2 pup material held in the dispatch records the same confound for rescue arms.)

### What the held sources say that bears on the predictions
- Synapsin-Cre neuron-restricted? The paper says Syn-Cre "is expressed at E12.5 and results in Wwox deletion particularly in most of the differentiated neurons (Supplementary Fig 1C)" and that "specific WWOX ablation in neurons, but not in other cells, was validated by observing intact WWOX levels in oligodendrocytes (stained with CC1)" (Supplementary Fig 1D, not held). Only mature oligodendrocytes (CC1) were tested in the main text; leakage in OPCs or astrocytes is not described there. The statement "neuron-restricted" is therefore the paper's claim backed by one cell type in a supplement; "most differentiated neurons", not all. All conditional models carry a Rosa26-tdTomato reporter, so a recombination map is possible; the paper's use of it is in Supplementary Fig 1C, not held.
- OPC-intrinsic effects: the paper reports (i) O-KO (Olig2-Cre; cre/+) and G-KO mice without "phenotype abnormalities" in development, weight and survival (Fig 1J-L; O-Control n = 11, O-KO n = 10), (ii) in Discussion/Results, MBP staining in O-KO and control littermates at P17 with "no major changes" (Supplementary Fig 8, not held), (iii) a co-culture in which wild-type OPCs on Wwox-null DRG neurons differentiate less (two experiments, n = 4 per condition; **P < 0.01), concluding a "non-cell autonomous" function, while stating "we cannot exclude the cell autonomous functions of WWOX in oligodendrocytes or astrocytes in other neurological disorders". So the OPC-intrinsic prediction is already disfavoured structurally in the held text, and Syn-Cre S-KO has the same hypomyelination (EM at P17: myelinated axons per field 180 +- 40 against 55 +- 35, g-ratio higher; n = 3 per genotype). S7 should say that the N1 measurement would test a prediction the paper's structural data already lean against; conduction in O-KO has not been measured (not in the main text).
- Controls: Repudi's S-Control is Cre-positive Wwox +/+; S7's "Cre-negative floxed littermates" would not control for the Cre transgene; add a Cre-positive wild-type group, and note that the Olig2-Cre line is a knock-in (heterozygous Olig2 loss).
- N2 as "within-slice control": in Repudi N2 is numerically longer in S-KO (about 8.3 against 6.7 ms), n.s. with scatter up to 16 ms; N2 identity (unmyelinated or partly myelinated) is stated differently in Palma's Methods and Results. A control that moves in the same direction with large variance is weak. The Repudi geometry (stimulate callosum, record layer V, one distance) differs from the Palma geometry (callosal CAP, four distances) that S7's design copies; the new N1 is therefore not the same quantity as Repudi's N1.
- Age: "P17 to P21": Repudi's electrophysiology was P13 to P17 (Methods), the S-KO mice die at 3 to 4 weeks, and the EM was P17; Palma used P21 slices. Feasibility at P21 in S-KO is not shown in the held text.

---

## S8 — MUST CHANGE

Texts read (by keyword search with context, and the dated-line paragraphs in full): PUP_BRIEF_V2_CONSOLIDATED.md (lines 10, 33, 43, 65-77, 94-101), ORDERING_PAGE.md (rows 8-11, lines 25, 31, 53), SLICE_PACKAGE_V2_CONSOLIDATED.md (lines 42-44), INVIVO_PUP_EXPERIMENT_BRIEF_V1_SCI_20261118.md (lines 76-80, 100, 102). I did not read each file from start to end; claims below that something is "not carried" rest on keyword searches of conduction, evoked, velocity, N1, N2, first-peak, callosal, MEP, Tc-MEP, transcranial, Olig2, oligodendrocyte, distance, drug-only, alone arm, in vivo.

What the pup brief v2 carries:
- Add-on 5(g) "Myelin or conduction endpoints" (under "Cheapest add-ons (all optional ...)"): callosal conduction latency measured once, n = 8 slices from 5 animals (controls) and 8 from 6 (knockout), the control n identical to another experiment's S-HT n (possibly copied), effects read from graphs (first-peak latency about 2.5 against 3.2 ms), neuron-targeted line only, acute slices P13 to P17, "no rescue, no velocity: a candidate needing re-measurement with a rescue arm and animal-level statistics, not yet an endpoint". So S8's first sentence is right, except that "never in vivo" is not in the pup brief v2; it is in SLICE_PACKAGE_V2 section 3.5 ("no velocity, no rescue, never in vivo"). The pup brief v2 5(g) does not say it.
- Add-on 5(f) "A heterozygote carrier readout (candidate, one source)": the Cheng 2020 Tc-MEP values in WT, heterozygote and null (onset latency 1.39 +/- 0.13 ms n = 10, 2.13 +/- 0.22 ms n = 5, 2.44 +/- 0.37 ms n = 4; amplitude 59.2 +/- 9.0, 59.6 +/- 17.2, 11.8 +/- 5.4 microvolt; "3-week-old mice; chloral hydrate; legend SEM; one laboratory"), with the sentence "This brief carries only the heterozygote bursting incidence." Also ORDERING_PAGE row 10 "Heterozygote carrier latency ... Candidate, one source". The same values are in SLICE_PACKAGE_V2 section 3.4.
- Dated lines (v1 brief): line 9.11 (2026-11-19) wrote that the heterozygote Tc-MEP latency was "equal to the null with normal amplitude"; the "Dated correction to 9.11" (line 102, binding) withdraws it ("not equal to the null"; partial latency prolongation). The v2 text carries the corrected form. The v2 text also ends with a pointer (2026-11-21, ADV-143) to a newer governing text, `PUP_BRIEF_CURRENT_IT_20261121.md`, which I was not allowed to open: S8 describes the older record.

MUST CHANGE: "It does not carry ... the in vivo transcranial motor evoked potential of the global null (Cheng 2020)." The v2 brief does carry the Cheng Tc-MEP values for the null (and the heterozygote) in 5(f), as an optional candidate carrier readout, not as an arm or endpoint. Replacement: "It carries the in vivo Tc-MEP of the global null (Cheng 2020) only as an optional heterozygote carrier candidate (5(f)); the design carries no conduction readout in an arm." Also replace "(... 'never in vivo')" by "(slice package v2: 'never in vivo')".

Remaining parts of the sentence: "does not carry the N2 control, a velocity from the distance slope, an oligodendrocyte-lineage arm": consistent with the searches (the only Olig2 text is the cross-region Olig2-against-Mbp contrast from a different paper; no N2, no distance slope). "a wild-type drug-only arm": ambiguous. The pup brief does carry wild-type genotype groups with drugs and a lithium-alone arm (section 2.9, stage 3, readout sedation, righting reflex, weight), but with the seizure readout; it carries no wild-type drug-only arm with a conduction readout. Add "with a conduction readout".

---

## Files opened

Dispatch inputs:
- /home/desktop/.claude/jobs/ae0002e7/tmp/adv285/blind/SENTENCES_ADV285_SCI_20261125.md
- /home/desktop/.claude/jobs/ae0002e7/tmp/adv285/blind/CENSUS_TABLE_ADV285_SCI_20261125.tsv
Held sources:
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_OUP_browserprint_pdftotext.txt (text; sections around lines 150-160, 225-245, 505-520, 550-640, 725-800, 855-873, 1015-1245, 1425-1530)
- /home/desktop/legend-development/files/fulltext/PMID33914858_Repudi2021_OUP_browserprint.pdf (page 27 only, rendered to PNG at 200 and 400 dpi in the work folder; viewed the page and a crop of panel 5D(ii))
- /home/desktop/legend-development/files/fulltext/PMID32000863_Cheng2020_PMC_r2.xml (text extracted)
- /home/desktop/legend-development/files/fulltext/PMID32000863_Cheng2020_assets/40478_2020_883_Fig2_HTML.png (copied to work folder, viewed). Fig7 asset not opened.
- /home/desktop/legend-development/files/fulltext/PMID35372341_Palma2022_PMC_r2.xml (text extracted)
- /home/desktop/.claude/jobs/ae0002e7/tmp/adv285/blind/taiep_PMC10906851.xml (text extracted)
- /home/desktop/legend-development/.claude/worktrees/sci_am_20261125/disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/adv285_functional_myelination_census_sci_20261125/abstracts_adv285.tsv (script scanned the file; printed only PMIDs 29029896, 29490274, 25716865, 20127809, 8880692, 38134864, 34382059, 39816792, 36798471, 34889893, 23250879, 22388935, 19427269, 19909499)
- /home/desktop/legend-development/.claude/worktrees/sci_am_20261125/disease-models/wwox/research/drug_repurposing/experiment_brief_presidio013_sci_20261116/v2_consolidated_sci_20261119/PUP_BRIEF_V2_CONSOLIDATED.md
- .../v2_consolidated_sci_20261119/ORDERING_PAGE.md
- .../v2_consolidated_sci_20261119/SLICE_PACKAGE_V2_CONSOLIDATED.md
- .../invivo_pup_adv059_sci_20261118/INVIVO_PUP_EXPERIMENT_BRIEF_V1_SCI_20261118.md
Work files I wrote (folder /home/desktop/.claude/jobs/ae0002e7/tmp/adv285/blind/work/): fig2.png, p27-27.png, hi-27.png, crop_ii.png, crop_ii.raw, palma.txt, taiep.txt, getabs.py, grepctx.py, cnt.py, meas.py.
Not opened: any other repository file (the delegation-budget protocol named in the generic delegate instructions was not read because the dispatch limits opening to the files above). One keyword search over the pup brief files produced output that the harness saved to a tool-results file; I did not open that file.
