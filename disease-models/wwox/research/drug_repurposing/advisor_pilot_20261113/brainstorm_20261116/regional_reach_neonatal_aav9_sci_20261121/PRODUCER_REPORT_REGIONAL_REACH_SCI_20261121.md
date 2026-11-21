# Producer report, verbatim: regional reach of neonatal ICV AAV9 with a neuron-restricted promoter (producer: legend-delegate; brief stated model sonnet and effort medium; read back by `framework/scripts/session_model_census.py` from the subagent transcript: model claude-sonnet-5-5, effort high, 28 turns, peak context 106,253 tokens: the Agent tool has no effort parameter, so the stated "medium" was not applied)

Persisted from the session transcript (not the agent output file). The producer tabulated only; the verdict is in `RESULT_REGIONAL_REACH_SCI_20261121.md`. Ratios in this report are the producer's arithmetic on printed means. Scratch copies named at the end of the report were in the producer's /tmp and are not kept.

PRODUCER REPORT: regional reach of neonatal ICV AAV9 with a neuron-restricted promoter, cerebellum against cortex. SCI window V, 2026-11-21. Settings used: sonnet, effort medium, about 31 tool calls, no agents started, no files written in the repository (scratch only in /tmp). I tabulate only. I do not compute the verdict and do not say whether the prediction held. PubMed content used through the PubMed tool: PMIDs 24882721, 24191919, 41457644, 41311060, 33577387, 39033321 (DOIs are in the tables).

HEADLINE COUNT (a label, not a verdict). Four papers meet the qualifying-row definition on the first pass, from four different senior-author groups. Only ONE of them (Voronin 2024) has cerebellum and cortex numbers printed in the main text or a table. One (McLean 2014) was reached at abstract level only. Two (Repudi 2021, Lukashchuk 2016) have the per-region numbers only in a figure, and the figure values were not read. The "figure-only" rows are not read, so they may or may not carry a ratio.

====================================================================
(1) ROUTE LOG
====================================================================
Europe PMC REST search (lite and core, plain client, generic user-agent), with field-tagged queries. Hit counts:
- TITLE_ABS AAV9 + (synapsin|hSyn|Syn1) + cerebell* + (neonatal|P0|ICV): 3 hits (Galvan 2021, McLean 2014, Huda 2014).
- TITLE_ABS AAV9 + (synapsin|hSyn) + intracerebroventricular + mouse: 5 hits (Liu 2026, Fernandez 2025, Galvan 2021, Hunanyan 2021, Lukashchuk 2016).
- AAV9 + synapsin/hSyn/Syn1/"synapsin I" + (neonatal|P0|newborn|postnatal) + mouse|mice: 12 hits. This is where Repudi 2021, Voronin 2024 and Obeid 2026 appear.
- AAV9 + ICV|intracisternal + neonatal + gene therapy/rescue + mouse, 2012 to 2026: 27 hits.
- AAV9 + (hSyn|synapsin|neuron-specific|neuronal promoter) + (neonatal|P0|P1) + (gene therapy|rescue|transduction): 9 hits (adds Jones 2024 DNM1, Jackson 2016, Geard 2025).
- Full-text query, open access only (FULL:AAV9, hSyn, ICV, P0, cerebellum, cortex, vector genome): 1 hit, Galvan 2026 MiniPromoters, which is midbrain-dopaminergic and was not pursued.
- AAV9 + synapsin/neuronal promoter + cerebell* in title or abstract: 6 hits (new: Lunev 2025 GNAO1 RNAi, Bey 2017 intrathecal adult, Zhou 2016 p25. None are of the neonatal ICV design.)
Full text read by Europe PMC fullTextXML (parsed text, figure references stripped by my parser, so figure numbers are partly lost): PMC8649866 (Repudi), PMC5731760 (Hammond), PMC4362361 (Huda), PMC11785923 (Guo), PMC12978470 (Epstein), PMC12940312 (Rioux), PMC13320503 (Norman), PMC12164150 (Fernandez), PMC11489538 (Jones), PMC12115231 (Geard), PMC5095393 (Jackson), PMC4756767 (Lukashchuk).
Full text read by the PMC article page: PMC11489525 (Voronin, page loaded, no challenge). PMC12856983 (Piermarini) loaded as a short page (about 50 kB) and matched none of my cerebellum, promoter or age patterns, so I could not confirm anything from it.
Blocked or failed routes:
- PMC8182483 (Hunanyan 2021), PMC article page: reCAPTCHA challenge. Route stopped: challenge. Europe PMC fullTextXML for it gave HTTP 500. Not reached.
- PMC8236560 (Galvan 2021), Europe PMC fullTextXML: HTTP 500. I did not try the PMC page. Not reached.
- Europe PMC fullTextXML for PMC11489525 and PMC12856983: HTTP 500; the PMC page was used for Voronin instead.
- journals.sagepub.com DOI page for Liu 2026 (CLN5): HTTP 403 "Just a moment" challenge. Route stopped: challenge. Not in PMC. Not reached beyond the abstract.
- doi.org to linkinghub.elsevier.com for McLean 2014: returned only a redirect page. sciencedirect.com page by WebFetch: HTTP 403. Route stopped. McLean is abstract-level only.
No e-mail or personal detail was sent to any service. No browser header was spoofed. No retry was made on a blocked route.

====================================================================
(2) TABLE OF QUALIFYING ROWS (mouse, neonatal ICV or neonatal intracisternal, AAV9, neuron promoter)
====================================================================
Rows are Q1 to Q4. "Not stated" means not found in what I read. Ratios appear only where both values are printed in the same table or panel. They are arithmetic on printed means, computed by me, and labelled.

Q1. Voronin et al. 2024, PMID 39033321, DOI 10.1016/j.ymthe.2024.07.012, Mol Ther 32(10):3331-3345.
- First author: G. Voronin. Last and corresponding author: M. Weetall (PTC Therapeutics). Group: PTC Therapeutics.
- Capsid: AAV9. Promoter: human synapsin ("AAV9.Syn.hCDKL5", transgene hCDKL5, bGH polyA).
- Route and age: ICV at PND0 (also ICM at PND0 compared). Quote: "The current study in mice administered the gene therapy on the first day of life, postnatal day (PND) 0." Injection volume: not stated (not found).
- Dose, with the unit as printed: "vector genomes per gram of brain (vg/g)". Table 1 for study 1: ICV 3.60e11, 1.20e12, 3.60e12 vg/g brain, N=8 per group. Study 2 doses: 3e9, 3e10, 3e11 vg/g brain. Total vg per animal: not stated.
- Harvest age: study 1 about 5 weeks ("approximately 5 weeks (35-37 days) post injection"). Study 2 and 3 harvest ages for the protein data in Table 2: not stated in the passages I extracted.
- Readout: transgene protein, human CDKL5, by MSD electrochemiluminescence immunoassay, expressed as % of wild type. This is a "protein relative to a wild-type reference" readout. Vector DNA by qPCR (Tfrc reference) and mRNA by RT-qPCR were also measured per region (Figure S1, a supplement figure; not read). Region ISH (RNAscope) is reported only as % NeuN-hCDKL5 double-positive cells in one hemisphere, not split by region in what I read.
- Denominator: % of WT CDKL5 protein level.
- n and statistic: Figure 1 legend, "Symbols represent the mean +/- SEM of 4 mice per group"; Table 1 lists N=8 per group for study 1. Table 2 shows mean +/- SEM; n per row is not printed in Table 2.
- Cerebellum and cortex are whole regions, not a cell type. Cerebellum is "cerebellum" tissue (the Methods list: olfactory bulb, prefrontal cortex, striatum, hippocampus, motor/parietal cortex, cerebellum, midbrain/brainstem). The cortex measure is a cortical tissue sample (Table 2 column "Cortex"; which cortical sample: not stated in Table 2).
- Cerebellum value and cortex value, as printed (Table 2, "CDKL5 protein % wild type (mean +/- SEM)", columns HPC, Cortex, Cerebellum):
  - 3.0e9 vg/g, study 2: cortex 1.3 +/- 0.2; cerebellum 1.0 +/- 0.2 (hippocampus 1.8 +/- 0.3).
  - 3.0e10, study 2: cortex 2.2 +/- 0.6; cerebellum 0.9 +/- 0.2 (hippocampus 3.9 +/- 1.0).
  - 3.0e11, study 2: cortex 30 +/- 14; cerebellum 10 +/- 2 (hippocampus 33 +/- 12).
  - 3.0e11, study 3: cortex 73 +/- 22; cerebellum 18 +/- 5 (hippocampus 123 +/- 32).
  - 5e11, study 3: cortex 136 +/- 21; cerebellum 33 +/- 9 (hippocampus 347 +/- 98).
  - Ratios, computed by me from printed means in the same table (ratio of means, no error propagation): cerebellum/cortex 0.77 (3.0e9), 0.41 (3.0e10), 0.33 (3.0e11, study 2), 0.25 (3.0e11, study 3), 0.24 (5e11, study 3).
  - Main-text quote, Results: "At a dose of 3e11 vg/g i.c.v., CDKL5 protein expression reached measurable levels with average values from the two studies of 14%, 78%, and 61% of WT mice in the cerebellum, hippocampus, and cortex, respectively." and "Less increase in CDKL5 protein levels was seen in the cerebellum than in the hippocampus or the cortex."
  - Study 1 text: "At the lowest tested i.c.v. dose, 3.6e11 vg/g, higher CDKL5 protein expression was seen in the olfactory bulb (96% of WT) and hippocampus (76% of WT), and lower levels in the striatum (35% of WT) and the cerebellum (41% of WT)." Cortex for study 1 is in Figure 1 only and was not read as a number. Also: "delivery of vector via i.c.v. resulted in more widespread and higher CDKL5 protein expression than i.c.m. delivery, except in the cerebellum" (Figures 1A-1G).
- INTERNAL INCONSISTENCY in the source, for the adjudicator: the text says averages "from the two studies" of 14, 78 and 61 for cerebellum, hippocampus and cortex at 3e11. From Table 2 the mean of the two 3.0e11 rows gives cerebellum 14.0 ((10+18)/2) and hippocampus 78.0 ((33+123)/2), which agree. The cortex mean from the same rows is 51.5 ((30+73)/2), not 61. I have not resolved which is right. I also assumed the column order is as in the Table 2 header "HPC Cortex Cerebellum"; the agreement for hippocampus and cerebellum supports that order, but the cortex mismatch remains.
- Marker or function: both. Protein expression (marker) is reported alongside functional rescue. Hindlimb clasp was normalised at 3e11 vg/g, and fear conditioning and open field were improved at higher doses (Table 2 and Figure 3). The per-region numbers are marker readouts.
- Access reached: full text, main text and Table 2 via the PMC page. Supplement (Figure S1 vector DNA and mRNA by region) not read. Figure 1 per-region protein bars not read as numbers.
- Locators: Table 2 ("Table 2. Summary comparing expression levels with functional improvements"); Results section on i.c.v. versus i.c.m. biodistribution (the "41% of WT" sentence); Results sentence "14%, 78%, and 61% of WT". Figure 1 legend: "Increased biodistribution in Cdkl5 knockout mice after i.c.v. injection compared to i.c.m. injection at postnatal day 0".

Q2. McLean et al. 2014, PMID 24882721, DOI 10.1016/j.neulet.2014.05.044, Neurosci Lett 576:73-78.
- First author: J.R. McLean. Senior author: O. Isacson (corresponding). Group: McLean Hospital / Harvard.
- Capsid: rAAV9. Promoter: human synapsin 1 (hSYN1). Route and age: neonatal ICV ("neonatal i.c.v. injection of rAAV9 in mice"). Exact injection day (P0 versus P1), volume and dose: not stated (not reached).
- Harvest age: 6 weeks of age (abstract).
- Readout: neuronal transduction rate by region, GFP-positive neurons. Denominator: not stated (not reached). The abstract calls it "high neuronal transduction rates"; whether the denominator is NeuN-positive neurons is not confirmed. n: not stated (not reached). Statistic as printed: mean +/- SEM (abstract).
- Cerebellum: 29.6 +/- 2.3 (units: % neuronal transduction, per abstract). Motor cortex: 43.5 +/- 3.3. Same abstract list also: substantia nigra pars reticulata 43.9 +/- 5.4, hippocampus 43.1 +/- 2.7, cervical spinal cord 24.9 +/- 3.9, ventromedial striatum 16.9 +/- 4.3. Printed in one list from one study; the ratio is not computed by me because the denominator, n and animal-level pairing are not confirmed.
- Cerebellar number is for the whole cerebellum or a cell type: not stated in the abstract.
- Marker only (GFP reporter, no phenotype).
- Access reached: abstract only (PubMed). Full text routes: Elsevier DOI/linkinghub (redirect only), sciencedirect.com (403). Not in PMC. Route stopped for full text.
- Verbatim quote (abstract): "Region-specific quantification of GFP expression showed high neuronal transduction rates in substantia nigra pars reticulata (43.9+/-5.4%), motor cortex (43.5+/-3.3%), hippocampus (43.1+/-2.7%), cerebellum (29.6+/-2.3%), cervical spinal cord (24.9+/-3.9%), and ventromedial striatum (16.9+/-4.3%), among others."
- Qualifying status: provisional. The definition requires the per-region denominator and n, which I could not check.

Q3. Repudi et al. 2021, PMID 34747138, DOI 10.15252/emmm.202114599, EMBO Mol Med.
- First author: S. Repudi. Senior author: R.I. Aqeilan (to be confirmed from the byline; my parse did not extract the author list). Group: Aqeilan lab. NOTE: Obeid 2026 (PMID 42422765), the benchmark paper in the pre-registration, is the same research programme, so Q3 is not an independent group from the benchmark. Please judge independence.
- Capsid: AAV9. Promoter: human synapsin I (hSynI). Constructs: AAV9-hSynI-mWwox-IRES-EGFP, AAV9-hSynI-hWWOX, control AAV9-hSynI-EGFP.
- Route and age: ICV at P0, free-hand, in Wwox-null mice. Volume and dose: "Approximately 1 µl (2 × 10^10 GC/hemisphere) virus" (Methods). Total per animal: not stated (bilateral per hemisphere).
- Harvest age: P17 (mWwox) and P19 (hWWOX).
- Readout: positive-cell fraction. Denominator: NeuN-positive neurons (percentage of NeuN and WWOX double-positive cells, in cortex, hippocampus and cerebellum). n: n=3 mice for each of two panels; "calculated from 3 identical sagittal sections". Statistic printed: not stated for these graphs in the text I read. Main text: "The percentage of NeuN and WWOX double-positive cells was calculated and found to range between 60 and 70%." (a pooled statement, not split by region).
- Cerebellum and cortex values: FIGURE-ONLY, value not read. Figure legend text (Fig 1, mWwox P17): "Graph showing the percentage of NeuN and WWOX double-positive cells in different parts of the brain (cortex, hippocampus, and cerebellum) from KO mice injected with AAV-mWwox at P17." Fig 2G (hWWOX P19): "Graph represents the percentage of neurons showing the transgene (NeuN and WWOX positive) expression at different parts (cortex, hippocampus, and cerebellum) of the KO brain at P19 after AAV injection." The graph panel letter in Fig 1 was not captured by my parser.
- Cerebellar cell type: the legend says "cerebellum" and does not say Purkinje or granule layer.
- Marker and function: both. WWOX expression (marker) and rescue of growth, hypoglycaemia, seizures, ataxia and survival (function) are reported. The regional graph is a marker readout.
- Access reached: full text, main text and figure legends via Europe PMC XML. Appendix and supplements: not read. Figure values: not read.

Q4. Lukashchuk et al. 2016, PMID 26942208, DOI 10.1038/mtm.2015.55, Mol Ther Methods Clin Dev (PMC4756767).
- First author: V. Lukashchuk. Senior author: M. Azzouz (to be confirmed from the byline; not extracted). Group: Azzouz lab.
- Capsid: scAAV9. Promoter: SYN1 (also CMV, CAG, Hb9 variants tested at the same dose in parallel; the SYN1 arm is the qualifying one). Route and age: intracisternal (cisterna magna) at postnatal day 1, wild-type mice. This is an "intracisternal at neonatal age" row under the pre-registration.
- Dose: "1 × 10^10 viral genomes of five titer-matched scAAV9-GFP vectors". Volume: not stated in what I read.
- Harvest age: 3 weeks post-injection (3-week-old mice).
- Readout: number of GFP-positive cells in a 1 mm^2 area of each brain section (Figure 5 legend, "counting GFP-positive cells in 1 mm 2 area of each brain section and normalizing the ..." and the rest of the sentence was not read), in the cerebellum, motor cortex, brain-stem and hippocampus. The "normalising to" denominator: not read.
- n and statistic: "Bar graphs represent mean +/- SD (n = 3)"; one-way ANOVA followed by Tukey (legend).
- Cerebellum and cortex values: FIGURE-ONLY, value not read. Text: "Quantification of the GFP-positive cells within the chosen brain regions revealed similarities between the targeting properties of CMV, CAG, and SYN1 promoters across all four areas". "All promoters except Hb9e were capable of driving GFP expression within the cerebellum, predominantly within the Purkinje cell layer." The cerebellar number is therefore for the cerebellar section count, with expression described mainly in the Purkinje layer.
- Marker only (GFP).
- Access reached: full text main text and figure legends via Europe PMC XML. The specific panel letters and the numeric values were not captured.

====================================================================
(3) "OTHER" STRATA (not pooled; brief)
====================================================================
O1. Hammond 2017, PMID 29244806, PMC5731760. AAV9 versus AAV2/1 versus AAVDJ8. Promoter: CMV or CMV/chicken-beta-actin hybrid (ubiquitous). ICV at P0, 2 µl, "2X10^10 GC/hemisphere". Readout: GFP-positive cells per region (units of the count not clear in the extracted text; "Quantitation... GFP+ cells"), n=3 per time point. Harvest 3 and 6 weeks. AAV9-GFP+ values as printed (3 weeks, 6 weeks): cortex 39.1 +/- 11.1 and 6.4 +/- 3.3; cerebellum 11.3 +/- 2.7 and 5.9 +/- 2.8 (hippocampus 12.3 +/- 8.2 and 2.4 +/- 0.8). AAV2/1: cortex 38.2 +/- 10.3 and 20.7 +/- 6.7; cerebellum 21.8 +/- 12.3 and 2.9 +/- 1.6. AAVDJ8: cortex 51.7 +/- 15.5 and 38.3 +/- 4.7; cerebellum 3.78 +/- 0.6 and 5.8 +/- 1.1. Stratum: ubiquitous promoter; capsid variants within the paper. Marker only. Access: full text main text. Senior author: not extracted.
O2. Norman 2026, PMID 42389555, PMC13320503. AAV9-NG276, human FMR1 promoter fragment (1,050 bp; endogenous-type promoter, not neuron-restricted by design). ICV at P1-P2, 4 µL (2 µL per side), 1e11 or 3e11 vg/animal. Readout: FMRP western blot relative to beta-actin or total protein, P28-P30, n=4 to 5 per group. Quote: "At the high dose, FMRP expression was also detected in the hippocampus and striatum (E and 1F) but not thalamus and cerebellum of P28-P30 KO mice (G and 1H)". Cortex (auditory and frontal): "sufficient to express FMRP in the auditory and frontal cortex of KO mice to WT levels" (Results heading; P70-P75 n=3). Values: figure-only, not read. Stratum: promoter not neuron-restricted. Marker plus function (EEG and behaviour).
O3. Guo 2024, PMID 39589822, PMC11785923. AAV9 with MeP229 (described as "predominantly neuronal", Mecp2-derived) or JeT (weak ubiquitous), hSLC6A1; ICV at P1. Readout: % of DAPI nuclei expressing hSLC6A1 mRNA, at least 1,000 nuclei per area per sample. Quote: "The greatest expression was seen in the neocortex and hippocampus, with less expression in the midbrain and cerebellum." Printed: JeT ~57% neocortex, ~28% hippocampus, ~21% thalamus; MeP229 ~35% neocortex, ~22% hippocampus, ~3% thalamus. Cerebellum value: not printed in the text I read (figure-only, not read). Stratum: not hSyn; the promoter-class decision for MeP229 is yours. Marker plus function (EEG and behaviour). Senior author: not extracted.
O4. Epstein 2026, PMID 41811855, PMC12978470. AAV9 with EF1alpha(s) or a small Mecp2 promoter ("546") driving hNPC1; ICV and other routes at P1 and other ages; ddPCR in cerebrum, cerebellum and liver at end stage. Numbers not extracted; figure/table not read. Stratum: ubiquitous or non-hSyn promoter; cerebrum is not a cortical region.
O5. Rioux 2026, PMID 41751597, PMC12940312. AAV9/CBh-EGFP (ubiquitous), vg per diploid genome by region at several ages and routes including ICV at P1 (dose "2.5 × 10^11 vg" for P1 ICV). Regions include cortex and cerebellum. Numbers not extracted (tables and figures not read). Stratum: ubiquitous promoter.
O6. Hunanyan 2021, PMID 33577387. AAV9 with human Synapsin promoter (ATP1A3); ICV at P10, not P0 to P2. Full text: route stopped (challenge). Stratum: different injection age. Not tabulated.
O7. Galvan 2021, PMID 33860682. AAV9-PHP.B with SYN1-EmGFP by ICV. Capsid variant, so a separate stratum. Age and regional numbers: not reached (Europe PMC XML returned HTTP 500; PMC page not tried).
O8. Liu 2026, PMID 41457644. AAV9 with hSYN or CAG by ICV in neonatal and juvenile Cln5-/- mice. Whether a per-region cerebellum and cortex readout exists: not reached (Sage page challenge; abstract only). It could be a qualifying paper if such a readout exists. Unknown.

====================================================================
(4) PAPERS CONSIDERED AND DROPPED
====================================================================
- Huda 2014 (PMID 26015973): ssAAV9 Syn1 but injections were direct cerebellar cortical, intrathecal and intravenous in older mice, not neonatal ICV or intracisternal at P0 to P2. Dropped.
- Jackson 2016 (PMID 27867348): AAV9 synapsin in rats, intravenous, not mouse ICV. Dropped.
- Jones 2024 (PMID 39127888, DNM1): hSyn1 AAV9, ICV at PND0-PND1, 7.2 × 10^11 vg, but the only "cerebell" hit in the full text was a reference title, so no regional cerebellum readout was found in the text (one route: Europe PMC XML). Dropped on that basis.
- Geard 2025 (PMID 40430940, Gaucher): AAV9.hSynI.hGBA1, ICV at P1, 7.2 × 10^11 vg. No "cerebell" hit in the full text; cortex readouts are for cortex (S1BF) and combined cortex-hippocampus tissue. Dropped on that basis (one route: Europe PMC XML).
- Fernandez 2025 (PMID 40506760): ICV at P0-P1 with AAV9, but hSyn drives only the eGFP reporter and the ATF is under EF1; it states cerebellum expression was "limited" only when citing earlier work (Hammond 2017). No own cerebellum readout found. Dropped.
- Piermarini 2026 (PMID 41311060): SPAST silence-and-replace AAV9, ICV in newborn pups. No synapsin or hSyn match in the PMC page I could parse (short page); not confirmed neuron-restricted. Dropped, route result unclear.
- Obeid 2026 (PMID 42422765): the benchmark paper named in the pre-registration, not tabulated.
- Dirren 2014 (PMID 24191919): AAV6-cmv and AAV9-gfaABC1D, not a neuron-restricted promoter; spinal-cord focus. Dropped.
- Hammond 2017 and the three others listed in (3) were kept as "other", not dropped.
- Not searched: bioRxiv or other preprints; Europe PMC "lite" search results only covered titles and abstracts, so papers that report a cerebellum readout only in the body or a supplement would not have been found unless a full-text query matched them (only one full-text query was run, restricted to open-access).

====================================================================
(5) WHAT I COULD NOT REACH
====================================================================
- McLean 2014: full text (dose, volume, n, denominator, definition of the cerebellar value). Abstract only.
- Repudi 2021 and Lukashchuk 2016: the per-region numeric values (graphs only). Voronin 2024: Figure 1 bars (vector genomes, mRNA and protein by region) and Figure S1.
- Voronin 2024 cortex total: text says 61 for the two-study average at 3e11 while Table 2 gives 51.5; unresolved.
- Hunanyan 2021 (challenge), Liu 2026 (challenge), Galvan 2021 (XML 500, PMC page not tried), Piermarini 2026 (page loaded but not informative).
- Senior authors for Repudi, Lukashchuk, Hammond, Guo, Epstein, Rioux and Norman were not read from bylines. I gave the likely senior author only where I could confirm (Voronin and McLean from PubMed metadata). Please confirm the groups for independence counting.
- No supplement was read for any paper.
- Absence statements (Jones, Geard, Fernandez) rest on one route (Europe PMC XML text search for "cerebell"), so they are not two-route absence claims.
- Scratch copies of the XML and HTML I used are in /tmp/rr_xml (outside the repository) with helper scripts in /tmp/rr_scripts.