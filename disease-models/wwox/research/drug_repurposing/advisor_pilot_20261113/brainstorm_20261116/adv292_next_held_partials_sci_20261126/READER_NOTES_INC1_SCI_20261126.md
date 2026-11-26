# ADV-292 increment 1: first reader's working notes (SCI, window 47022d33, 2026-11-26)

Hypothesis level; reference genotype class only; nothing here is medical advice. Written while reading, before the blind reader sees anything. Held bytes only. Files are read from the root checkout `files/` (copies were extracted to a scratch folder; no held file was modified). Labels follow figure or sheet, panel and row; the replicate unit and species are stated beside each value.

## 1. 39216838 (Wang 2024, GABRA1 variants, hispidulin and TP003; card A03)

Held and now looked at: `supplement/PMID39216838_r2/` NIHMS2024199-supplement-1.docx (Supplementary Figures S1 to S7, eight images), supplement-2.pdf (17 pages of uncropped blots for Figures 1C-F, 3B-D, 4A, 5C-E, 6A-C and Supp S3A-C, S4A-B), supplement-3.xlsx (Table S1, 151 GABRA1 variants with Rhapsody probabilities), supplement-4.xlsx (Table S2, qPCR primers), supplement-5.xlsx (Table S3, F values). The main text and figures had been read on 2026-10-21 (receipt `FTR-20261021-39216838-01`, supplementary not read).

Consumer sentences (card A03 `input.abstention_card.adjacent_context_not_wwox_evidence[0]` and `input.p4_card.sources.external_not_wwox_evidence[0]`, repeated in the packet):

> GABRA1 receptor-binding modulators raised variant protein and current together (measured in HEK293T, one knock-in iPSC line)

Also `p4_card.evidence_for_and_against.transfer_limits` and `p4_fields.cellular_context.limits`: "Client-specific rescue in the adjacent literature came from ligands that bind the client; none is known for this protein, and an active-site binder can also inhibit a variant with low baseline activity." R1 note (repurposing_10h_scientist-a_20261021.md line 147): "a case of a ligand that binds the client protein itself".

What the sources show (species and unit beside each value; HEK293T cells and human iPSC-derived GABAergic neurons, no animal):

* **Which modulators.** Supp Fig S3A-C (HEK293T stable lines D219N, G251D, P260L; n = 3 lysates per bar): ten compounds were screened at 10 micromolar for 24 h on total alpha1. Midazolam, hispidulin and TP003 raised alpha1 in all three lines (bars about 1.9 to 2.9 times DMSO); CL218872 raised it in D219N (about 1.5, one star) and P260L (about 2.8) but not G251D; florazepam, chlormezanone, GABA, bretazenil and CGS20625 were not significant in any line; ZK93423 lowered D219N (about 0.25) and was not significant in G251D and P260L. So the class raised protein in four of ten; the sentence's plural "modulators" holds for hispidulin and TP003 (the two carried on).
* **Current.** Main Fig 4b (HEK293T, whole-cell, n = 4 to 11 cells): hispidulin raised the peak current for all eight variants; TP003 for six of eight (D219N 1819 to 2330 pA and R214C 501 to 874 pA did not reach significance). Midazolam and CL218872 current was not measured. Current was **not** measured in the iPSC neurons.
* **iPSC line.** Fig 7 and Supp Fig S7 (Sanger trace, G251D GGC>GAC, heterozygous, two silent changes marked): the end points in the iPSC-derived neurons are surface immunofluorescence intensity (alpha1, beta2/3, gamma2; 50 to 75 neurons from at least three differentiations) and proximity-ligation puncta (35 to 70 neurons). No current, no total-protein Western in the iPSC neurons. The text says "The enhanced surface presence of GABAA receptors would likely correct the impaired GABAergic input" (inference).
* **"Bind the client".** The paper never measures binding to a variant (no thermal shift, no binding curve, no docking). The binding statement is from the known benzodiazepine-site pharmacology of the compounds ("directly bind GABAA receptors at the benzodiazepine sites", a literature premise) and the Discussion says "Presumably, binding of Hispidulin and TP003 to the alpha1(G251D) variant improves stability". The shared-assay premise is therefore: a known receptor ligand, tested on variants, with the binding to the variant presumed.
* **Wild type (sibling panel, side finding, not a card sentence).** The text says hispidulin and TP003 "had minimal effects on wild type alpha1 protein levels" (Supp Fig S4). Supp Fig S4A (HEK293T alpha1beta2gamma2, n = 3): hispidulin 5 micromolar about 1.44 and 10 micromolar about 1.46 times control, both marked with one star; F = 6.10 in Table S3 (S4A), 0.73 for TP003 (S4B, all NS). So a roughly 45 percent rise of wild type at the dose used for every other figure (10 micromolar) sits under "minimal". No card sentence repeats "no wild-type effect" for this paper.
* **EC50 shifts (Supp Fig S5, HEK293T, n = 3 to 4 per curve).** Hispidulin G251D 28.4 to 15.2 micromolar (marked significant); D219N 10.4 to 7.1 and P260L 6.2 to 3.4 not significant; TP003 not significant in all three. Not a consumer sentence.
* Table S1 is a list of 151 variants with Rhapsody probabilities (no experimental data); Table S2 primers; Table S3 F values (85 entries, read).

Preliminary reading (not yet blind-checked): the sentence reads "protein and current together" for "modulators" in "HEK293T, one knock-in iPSC line". Two parts are narrower in the sources: the current is HEK293T only (the iPSC neurons carry surface fluorescence and proximity ligation only), and "modulators" is hispidulin and TP003 (TP003 current not significant in 2 of 8 variants), from a screen in which four of ten modulators raised protein.

## 2. 40485335 (Shah 2025, hGAT-1 G443D and G443V; card A01, rows DR-A01-001, -002, -003)

Held and now looked at: `figures/PMID40485335/` seven main-figure jpg (file numbers differ from figure numbers: g003 is Fig 4, g004 Fig 6, g005 Fig 5, g006 Fig 2, g007 Fig 3, g002 Fig 7-type fly expression panels, g001 graphical abstract) and four supplementary TIFF (s001 = Supp Fig 2, s002 = Supp Fig 4, s003 = Supp Fig 3, s004 = Supp Fig 1; legends are inside the images). Receipt `FTR-20261021-40485335-01` had supplementary not read.

Consumer sentences (card A01 `input.drug_assertions`, repeated in the packet):

* DR-A01-001: "The class rescued the fully retained variant and NOT the partly trafficked G443D; the rescued variants recover part of wild-type capacity with altered affinity; wild-type capacity is raised too."
* DR-A01-002: "The class raises wild-type protein in every target of the lot: the effect is not variant-specific." (species field: "cell lines, worm, fly, mouse"; sources include 40485335)
* DR-A01-003: "MEASURED NO RESCUE (behaviour unchanged) ... In the same paper glycerol, an osmolyte-type chemical chaperone, did rescue G443D in vitro" plus the IT note of 2026-11-25 (ADV-281) that already cites Supp Fig 4C.

What the sources show (HEK293 cells, transient transfection; Drosophila adults; unit under n stated):

* Supp Fig 1 (HEK293, single-point [3H]GABA uptake, at least three experiments in triplicate, four to five points per bar): siRNA against HSP70 or HSP90 raised G443D uptake to about 1.8 and 1.9 percent of untreated WT and G443V to about 1.1 and 2.7 percent (stars shown), and WT to about 160 and 165 percent (no star shown). Not a card sentence.
* Supp Fig 2 (HEK293): G443V at 1:1 with WT lowers WT uptake by about 50 percent and WT mature band to about 0.65 of control; G443D does not (about 1.0). Not a card sentence.
* Supp Fig 3 and Supp Fig 4 (fly brains, GAD1-Gal4): G443D shows a broad expression like WT and the membrane marker (panel C and C'), G443V shows no presynaptic fan-shaped-body expression (D, D'). This is the panel IT's note cites as "Supp Fig 4C": the citation is correct.
* Fig 3 (g007, HEK293, single-point uptake, normalised to untreated WT = 100): WT is raised by 4-PBA 10 mM (about 180, one star), pifithrin-mu (about 180), 17-DMAG (about 220), lumacaftor (about 210) and liothyronine (about 190); G443D: 4-PBA about 1.6 (no star), glycerol about 6 (three stars), pifithrin-mu about 2.7 (one star); G443V: 4-PBA about 8 (three stars), glycerol about 5 (two stars), pifithrin-mu, 17-DMAG, lumacaftor one star.
* Fig 4 (g003, HEK293, Michaelis-Menten; WT control Km 6.5, Vmax 298; glycerol Vmax 556; 4-PBA Vmax 812 pmol per 10^6 cells per min, text values): G443D with glycerol Km 22.9, Vmax 165; G443V with 4-PBA Km 39.2, Vmax 116. So WT capacity is raised by both compounds in HEK293 (text and Fig 4A) and the rescued variants reach about 55 percent (G443D, glycerol) and about 39 percent (G443V, 4-PBA) of the untreated-WT Vmax, with higher Km; against the treated-WT Vmax they are about 30 and about 14 percent.
* Fly arm (Fig 6B and 6C, g004, brain antennal-lobe astrocytes): "4-PBA and glycerol did not markedly alter the expression of WT GAT-1 or G443D"; 1 mM 4-PBA for 48 h; seizure arm Fig 6G (G443D, unaltered) and 6H (G443V, reduced, three stars).

Preliminary reading (not yet blind-checked): DR-A01-001 stands (HEK293 values; the fly arm is not what "wild-type capacity" refers to). DR-A01-002 says the class raises wild-type protein "in every target of the lot" and lists the fly among the species; in the one fly measurement of this paper WT hGAT-1 expression was **not** markedly altered by 1 mM 4-PBA (Fig 6B); the HEK293 raise is in uptake (Fig 3A, 4A) and mature band (Fig 4B, 4C), a different quantity from "protein". DR-A01-003 stands as corrected by IT; the size of the in-vitro glycerol rescue is about 6 percent of untreated-WT uptake at the single point of Fig 3B (about 55 percent of the untreated-WT Vmax in Fig 4D), which the sentence does not give.

## 3. 41178115 (Fu 2025, IRE1/XBP1s activators IXA62, IXA554, IXA105, GABRA1 variants; card A04)

Held and now looked at: `supplement/PMID41178115/cn5c00227_si_001.pdf` (18 pages: Supp Figs S1 to S4 with legends, uncropped blots for Figs 1A-F, 2A-G, 3A-F, 4A-E, 5A, S1E, S2, S3, a Figure S5 page, Table S1 of qPCR primers). Receipt `FTR-20261021-41178115-01` had the supplementary PDF "retrieved, not read".

Consumer sentence (card A04 `abstention_card.adjacent_context_not_wwox_evidence[0]` and `p4_card.sources.external_not_wwox_evidence[0]`, repeated in the packet):

> selective IRE1/XBP1s activators raised post-transcriptionally variant protein, surface protein and current for GABRA1 variants (research compounds, not approved drugs; HEK293T and one iPSC line)

What the sources show (HEK293T stable lines; heterozygous G251D knock-in iPSC-derived GABAergic neurons; no animal):

* **Variants and read-outs, by variant.** D219N: total protein 2.4, 1.6, 2.8 fold (IXA62, IXA554, IXA105), surface protein, GABRA1 mRNA unchanged (Fig 1B), peak current 2.2, 3.0, 2.4 fold (100 micromolar GABA, Fig 2K-L). G251D: total 2.6, 1.8, 3.1 fold, surface 3.0, 3.1, 2.3 fold, peak current 2.1, 2.6, 1.6 fold (1 mM GABA, n = 8, Fig 5F-G). P260L (Supp Fig S4, n = 4 total and n = 5 surface): total 2.3, 1.9, 2.6 fold, surface 1.4, 1.9, 1.5 fold; **no current**. So the current was measured for two of the three variants; the mRNA control that supports "post-transcriptionally" is shown for D219N only (the text infers it for the others by the same mechanism).
* **iPSC line (Fig 6A, heterozygous G251D).** Surface immunofluorescence of alpha1, beta2/3, gamma2 with IXA62 and IXA554 only (19 to 35 neurons from at least three differentiations); proximity-ligation puncta; no total protein, no current, no IXA105. The Discussion states current for HEK293T cells only.
* **Selectivity (Supp Fig S1D-E, HEK293T D219N).** The XBP1-Rluc reporter induction by the three compounds is abolished by the IRE1 RNase inhibitor 4u8C; CHOP (PERK arm) is not induced by the compounds, induced by thapsigargin. Supports "selective" for IRE1/XBP1s against PERK in this line.
* **Wild type (Supp Fig S2, HEK293T alpha1beta2gamma2).** IXA62 lowers wild-type alpha1 at 0.1 and 0.25 micromolar (about 0.80, one star each) and is flat at 1 to 25; IXA554 flat; IXA105 10 micromolar about 1.18 (one star); surface wild type (S2D, n = 5) not significant. No card sentence repeats a wild-type statement for this paper.
* **ERAD factors (Supp Fig S3, D219N, n = 3).** HerpUD1 rises with IXA62 (about 1.8, one star); the other factors are flat.

Preliminary reading: the sentence is a compression of three variants, three read-outs and two cell systems. The parts that are narrower in the sources: current in two of three variants (not P260L, not the iPSC neurons), mRNA control for one variant, the iPSC neurons carry surface fluorescence and proximity ligation for two of the three compounds.

## 4. 42268630 (Frick 2026, 4-PBA and 16 analogues in stxbp1 zebrafish; card A01, row DR-A01-004)

Held and now looked at: `supplement/PMID42268630/PRP2-14-e70285-s001.xlsx` (one sheet, "Supplemental Table 1: Statistics", 125 rows; parsed in full). The main text is `fulltext/PMID42268630_Frick2026_PMC13251787.xml`. Receipt `FTR-20261021-42268630-01` had the statistics workbook not read.

Consumer sentence (card A01 `drug_assertions[3]`, DR-A01-004, repeated in the packet): target "stxbp1a/stxbp1b null alleles", endpoint "movement deficit and ictal-like events", genotype "frameshift nulls", species zebrafish larva; note "MEASURED NO RESCUE in null alleles, protein not measured, bath concentration bounded by larval toxicity, assay separation of controls unestablished; INCONCLUSIVE for a protein-expressing missense allele. Encoded NO_CHANGE."

What the sources show (zebrafish larvae, unit under n stated):

* **Sheet1 row 3 to 5 (Fig 1A).** Total distance over 10 min: WT 910.8 +/- 63.38 SEM (n = 88), stxbp1a 277.3 +/- 15.44 (n = 72), tetracaine 200 micromolar (noise-floor control) with the mean cell F5 reading 63.38 and SEM 0.73 (n = 170); one-way ANOVA F(2, 327) = 122.3, stxbp1a against tetracaine P = 0.9983. **The F5 cell repeats WT's SEM (G3 = 63.38); the tetracaine mean cannot be 63.38 with P = 0.9983 against 277.3.** The Methods give 279 mm as the aggregated tetracaine mean and the text says tetracaine cut WT by 69 percent (910.8 x 0.31 = about 282). The assay does not separate the mutant from the anaesthetic floor (P = 0.9983), which supports "assay separation of controls unestablished". Label: Sheet1, row 5, column F, a workbook typing error.
* **Rows 24 to 32 (Fig 1E, 4-PBA locomotion, one larva per well).** WT 670 (n = 20), 25 and 50 (units written "mM") 1140 and 994 (n = 40); stxbp1a 284 (n = 38), 279 and 300 (n = 72), P = 0.8223; stxbp1b 920 (n = 40), 737 and 1007 (n = 78), P = 0.1683. The workbook writes the 4-PBA doses as "25 mM" and "50 mM"; the text says 25 or 50 micromolar and toxic above 50 micromolar; the Figure 1 legend says 10 and 25 micromolar (Fig 1D) and 100 percent survival at 10 and 25 micromolar (Fig 1C). The dose is stated three ways in one paper; the card gives none.
* **Rows 33 to 34 (Fig 1H in the workbook, Fig 1F-G in the text and legend).** stxbp1b local field potential, Type II ictal-like events per 15 min: baseline 7.56 +/- 2.29 SEM, 4-PBA 8.22 +/- 2.91, "baseline = 9, 4-PBA = 9", unpaired t test P = 0.8593, t = 0.1802, df = 16; the legend gives the 95 percent CI of the difference as -7.18 to 8.51. The Methods say nine homozygous stxbp1b larvae were used for electrophysiology, and the legend describes baseline (0 to 15 min) and 45 to 60 min of continuous 50 micromolar bath exposure in one 60-min trace: the nine larvae were recorded in both windows and compared as if unpaired. A CI of -7.18 to +8.51 events per 15 min around a baseline mean of 7.56 does not exclude a large fall.
* **Other rows (Fig 2A to 2P, 16 analogues, 25 and 50 "mM", one-way ANOVA with Dunnett).** No stxbp1a comparison is significant in the rows parsed; several WT comparisons are (for example guanfacine WT 839 to 453 and 368).
* **Alleles and protein.** Results: a 4-bp frameshift deletion in stxbp1a and "a 12-base-pair loss-of-function deletion in stxbp1b"; the caveat paragraph calls both "homozygous frameshift loss-of-function deletions ... predicted to result in the absence or severe truncation"; Discussion: "We were unable to directly assess stxbp1a or stxbp1b protein levels ... lack of suitable validated antibodies". A 12-bp deletion is a multiple of three, so by arithmetic it is in-frame unless it disturbs splicing; the paper does not say which. This is a main-text point, outside the supplementary class read here.

Preliminary reading: "protein not measured" and "assay separation of controls unestablished" are supported by the paper and the workbook. Three things are not in the sentence: the dose (25 and 50 micromolar by the text), that movement was tested on stxbp1a (stxbp1b movement is normal) and ictal-like events on stxbp1b only (nine larvae, one 50 micromolar bath, a CI that does not exclude a large fall), and that the stxbp1b allele is a 12-bp deletion.

## 5. 41664646 (Ahuja 2026, MyeliMAP on a chip; investigations.tsv row INV-06 and investigations_it20.tsv INV-06, ADV-209 block)

Held and now looked at: `fulltext/PMID41664646_Ahuja2026_imec_VoR.pdf` (15 pages, the final typeset article; no supplementary information is held, so Supp Figs S2 and S3 and the two videos stay unread). Pages 3, 7, 8, 9 and 11 (Figs 1 to 5) were rendered and opened as images; the Results, Methods and Discussion text of the article was searched and read for the statements below. Receipt `FTR-20261124-41664646-01` had figures, introduction, limitations, references, supplementary and tables not read.

Consumer text (INV-06, `next_test` column, the ADV-209 block, identical in both TSV files): human induced neurons with or without induced oligodendrocytes on a microfluidic electrode platform, no WWOX perturbation and no tested drug; "At week 8 the plotted means are about 0.36 against 0.27 m/s (co-culture against monoculture) and, in the same figure, about 1.2 against 3.15 detected responses per microchannel; the authors state that monocultures showed more responses and attribute it to axon excitability, axonal density or arrangement. Speed is the latency at the start of the stimulation train over one path length (1,960 micrometres) assumed for every point, clusters are not tied to identified axons, monocultures are in separate devices, two co-culture networks were excluded for missing stimulation artifacts, and electron microscopy is shown only for co-culture as representative images."

What the sources show (human iPSC-derived iNGN2 neurons with or without iSOX10 oligodendrocyte-precursor spheroids; PDMS network as the unit, N = 5 chips, n = 15 networks):

* **Fig 5e (conduction velocity, mean +/- SEM, week 8):** co-culture about 0.357 m/s (three stars), monoculture about 0.268; week 6 co-culture about 0.36 (one star), week 7 about 0.34 (one star); monoculture 0.27 to 0.30 throughout. The sentence's 0.36 and 0.27 reproduce.
* **Fig 5c (number of responses per microchannel, week 8):** monoculture about 3.15 (four stars), co-culture about 1.2. Same figure as 5e. The sentence reproduces. At every week from 2 to 8 the monoculture is higher.
* **Fig 5d (latency):** week 8 monoculture about 7.45 ms, co-culture about 6.05 ms; 1960 um over 6.05 ms is 0.324 m/s, over 7.45 ms 0.263 m/s, against the plotted velocities 0.357 and 0.268 (a mean of per-response velocities is not the distance over the mean latency; the paper states velocity is distance over latency per data point).
* **Attribution of the higher response count:** Results (Fig 5c sentence) "likely reflecting differences in axon excitability or axonal density"; Discussion "likely reflecting differences in axonal arrangement ... physical presence of iSOX10 OPCs ... can partially obstruct axonal trajectories". The sentence combines both passages correctly.
* **Methods:** latency is "the time delay between the stimulus and the induced response at the recording site, at the beginning of the stimulation"; distance "approximated to be 1960 um for all data points, based on the theoretical measurement of shortest possible path and longest possible path"; responses are "extracted via a clustering algorithm" with no per-axon identification stated; "two coculture PDMS microfluidic network" excluded for missing stimulation artifact at all time points; "neuron monoculture conditions were established in separate devices"; Fig 3 TEM (week 6, co-culture only, N = 2 independent experiments, n = 6 networks); the Discussion says further TEM is "data not shown".
* **Unit note not in the sentence:** the legend of Fig 5 gives n = 15 networks for panels b to e without saying how the 15 divide between conditions after two co-culture networks were excluded.

Preliminary reading: every number and every methods statement in the INV-06 block reproduces on the held PDF; no consumer sentence for this record needs a change on the figure class. Supplementary information (Supp Figs S2, S3, Videos S1, S2) is not held, so that class stays unread.

## 6. First reader's verdicts on the ten sentences (frozen 2026-11-26T00:49Z, before the blind report was read)

| id | record | first-reader verdict | reason in one line |
|---|---|---|---|
| S1a | 39216838 | MUST CHANGE (borderline) | the parenthesis attaches "HEK293T, one knock-in iPSC line" to "protein and current"; current was measured in HEK293T only; "modulators" is hispidulin and TP003 (four of ten screened raised protein; TP003 current not significant in 2 of 8 variants) |
| S1b | 39216838 | ADD | binding to the variant is presumed from benzodiazepine-site pharmacology, not measured |
| S1c | 39216838 | ADD | same (ledger line, not a consumer unit) |
| S2a | 40485335 | STANDS | HEK293 numbers reproduce (Fig 3 and 4) |
| S2b | 40485335 | MUST CHANGE (borderline) | "every target" and the fly listed among species: the paper's fly arm shows WT hGAT-1 expression not markedly altered (Fig 6B); the HEK293 raise is in uptake (Fig 3A, 4A) and mature band (Fig 4B-C) |
| S2c | 40485335 | STANDS | already corrected by IT with the right panels; size of the glycerol effect not given (optional ADD) |
| S3a | 41178115 | ADD | current in D219N and G251D only (not P260L, not iPSC neurons); mRNA control for D219N; iPSC surface fluorescence for IXA62 and IXA554 only |
| S3b | 41178115 | STANDS | the paper does not test other clients or global effects |
| S4 | 42268630 | ADD | dose (25 and 50 micromolar by the text), allele-to-endpoint mapping, nine larvae and a CI that does not exclude a large fall; stxbp1b is a 12-bp deletion (main text, outside the class read) |
| S5 | 41664646 | STANDS | every number and methods statement reproduces on the held PDF |

Strict (a) candidates before the blind reader: S1a and S2b (two of five records); both are borderline readings of how a sentence is attached. Strict needs (a) and (b); the blind verdicts decide.

### Addendum to section 3 (first reader, after the blind report; figure re-opened)

Fig 5C of 41178115 (G251D, surface alpha1 by biotinylation, HEK293T, about 4 points per bar): IXA62 about 3.0 (one star), IXA554 about 3.1 (three stars), **IXA105 about 2.3 with no significance mark** (the text gives 2.3-fold). My section 3 listed the three folds without saying that the IXA105 bar is unmarked; the blind reader caught it and the figure confirms it (file `files/figures/PMID41178115/cn5c00227_0005.jpg`). The same figure gives: total alpha1 (5B) all three marked, current (5G, n about 8) all three three stars, confocal surface fluorescence (5E) all three three stars.
