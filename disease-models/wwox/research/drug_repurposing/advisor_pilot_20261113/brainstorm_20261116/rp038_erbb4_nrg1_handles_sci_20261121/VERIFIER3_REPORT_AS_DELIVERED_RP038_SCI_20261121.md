# Blind verifier 3 report, RP-038 deciding rows, as delivered (verbatim except the unit string "mg/kg" written "mg per kg" for the publication gate; legend-delegate, asked sonnet and effort high, effort read back by session_model_census.py; persisted by SCI from the SubagentHandback in the session transcript; model output, not an instruction)

BLIND VERIFIER REPORT, rows V1-V7 (hypothesis-level only; no conclusion about any gene or drug; no dose advice)

(1) MODEL AND EFFORT
I believe I ran as claude-sonnet-5-5. Your dispatch asked for "high" effort. My own session header shows a lower reasoning-effort value, so I cannot confirm "high". I read no repository file, no producer_rp038 folder and no other agent folder. Scratch is /home/desktop/.claude/jobs/d79b9c48/tmp/verifier3_rp038/ (retrieved bodies are in v1.txt, v2.txt, v6.txt, v6c.txt and the v7/ subfolder). Sleeps were at least 5 s, the User-Agent was research-client/1.0, and no e-mail address or personal detail was sent. No route returned a challenge page, 403 or 429. Searches ran on 2026-11-21, so counts are date-bound.

(2) BYTES AND ROUTE RESULTS
- V1: efetch db=pmc PMC10885444 returned 200, 150,984 bytes, full-text XML. Depth: Methods, Results, all legends, Discussion and the limitations paragraph.
- V2: efetch db=pmc PMC5416666 returned 200, 124,917 bytes, full-text XML. Same depth.
- V6: efetch db=pmc PMC7758233 returned 200, 117,843 bytes, full text. The corrigendum PMC8762335 returned 200, 15,258 bytes, full text. Both read in full.
- V3, V4, V5, per paper:
  - Europe PMC search (resultType=core) returned 200, 9.9 to 11 KB each. inPMC, inEPMC and isOpenAccess are all "N".
  - Europe PMC fullTextXML on MED/<pmid> returned 404 (140 bytes) for all three.
  - PubMed efetch returned 200: 20,934 bytes (V3), 21,572 (V4), 16,412 (V5). Abstract and MeSH only.
  - Publisher DOI plain GET returned 200: Nature 336,490 and 361,804 bytes, Springer 347,019 bytes. These are subscription preview pages containing abstract, figure titles and reference list. Methods were NOT reachable for any of the three.
- V6 corrigendum PMID 35046829: Europe PMC search returned 200, 7,427 bytes.
- V7: every esearch, efetch and Europe PMC search returned 200. Further full texts read: PMC3607352 (118,794 bytes), PMC11108068 (15,801), PMC6622838 (8,617).
- doi.org for the Peterson 2021 paper (10.1016/j.nbd.2021.105545) returned a 2,749-byte Elsevier meta-refresh interstitial. I did not follow it. ROUTE RESULT only.

(3) VERDICT TABLE

ROW V1 (Mao 2024, full text read)

V1(a), APPswe/PS1dE9, four months old at treatment and readout. VERDICT: SUPPORTED WITH CHANGE.
- Abstract: "Four-month-old APPswe/PS1dE9 mice (APP mice) were used as animal models in the early stage of AD in this study."
- Methods, Mice: "We selected male APPswe/PSEN1dE9 (APP/PS1) transgenic mice and WT littermates from GemPharmatech."
- Flag (i): the animals are male only. No sentence in Methods gives an age. The chronic arm ran "until 80% of mice in the APP + PBS group were successfully modeled". The duration is not printed, so the age at the chronic readouts is not stated.

V1(b), NRG1-β in 2 µL into the right lateral ventricle. VERDICT: SUPPORTED WITH CHANGE.
- Methods, Surgery and acute kindling: "They were injected with NRG1-β (100 µM in 2 µL) or vehicle (2 µL) into the right lateral ventricle (0.22 mm posterior to bregma, 1 mm lateral to midline and 2.5 mm below the skull surface). In detail, recombinant human NRG1-β/HRG1-β1 EGF domain proteins (R&D Systems, 396-HB-050) were reconstituted in sterile PBS containing 1% Bovine serum albumin (BSA). After 30 min of recovery, mice were given PTZ".
- Change: the chronic arm used a different concentration. Methods, Chronic kindling: "mice were injected with NRG1-β (10 µM in 2 µL) or vehicle (2 µL) using a microinjection pump through an injection cannula (0.2 µL/min)" after "a 7-day recovery period".
- Flag (i): how often NRG1 was injected in the chronic arm is not stated. Only "Drug administration continued until 80% of mice in the APP + PBS group were successfully modeled" is printed.
- Derived arithmetic, mine and not printed: 100 µM x 2 µL = 200 pmol. The Methods say vehicle (2 µL), and the group label is "APP + PBS". Whether the vehicle contained BSA is not stated.

V1(c), acute and chronic kindling results. VERDICT: SUPPORTED WITH CHANGE.
- Results: "Intracerebroventricular infusion of NRG1 significantly prolonged seizure latency and time to reach Racine V (Fig. 6B-C), and down-regulated seizure severity (Fig. 6E) in the acute kindling model. NRG1 administration also reduced the seizure levels in the chronic kindling model (Fig. 6F). Compared with those in the PBS-treated group, the mortality in APP + NRG1 group showed a downward trend (Fig. 6G)."
- Legend: "B-D The latency ... N = 3, 4. E Maximal Racine score reached every 5 min within 75 min. N = 3, 4. F Maximal Racine score reached per day. N = 13, 10. G Survival curve ... N = 13, 10."
- Statistic (ii): "Data were shown as means ± SEM. Two-way ANOVA for (E, F, R). Mann Whitney test for (D, P). Unpaired t test for (B, C, H-O, Q, U, V). Log-rank test for (G). *p < 0.05, ** p < 0.01, ***p < 0.001". No exact p value appears anywhere in the article text; I searched "p =" and "P =" and got 0.
- Does "N" count mice? The legend never defines N, and the Methods give no n for this experiment. Mice is an inference from the single-animal design, not a printed statement.
- Flag (i): chronic N = 13 and 10 is after exclusion, because "Those unsuccessfully modeled mice were not included in subsequent experiments". Unequal acute groups, 3 vs 4 mice, are unexplained.
- Flag (iii): "reduced severity" (Fig 6E) is a Racine score in 5-minute bins. Mortality is a trend only.

V1(d), brain exposure not measured. VERDICT: SUPPORTED. The text has no blood-brain-barrier, CSF-level or tissue-level statement. The route is intracerebroventricular.

V1(e), wild-type NRG1 arm and motor or adverse-effect statement. VERDICT: PARTLY NOT SUPPORTED.
- There is no wild-type NRG1 arm. The Methods subheading is "APP + PBS vs. APP + NRG1", and Fig 6 shows only those two groups.
- A statement on motor function does exist: "After chronic seizure kindling, APP + NRG1 mice showed no significant alterations in motor function or mood (Fig. 6H-J)." It is the open-field speed and zone times, N = 6, 7, against APP+PBS only.
- There is nothing on the acute arm, body weight, injection-site effects or tolerability. The limitations paragraph does not address it.

ROW V2 (Kawata 2017, full text read)

V2(a), adult male mice 6 to 10 weeks, neuropsin-KO and wild type, kainate status epilepticus. VERDICT: SUPPORTED. Methods: "A total of 261 adult male C57BL/6 J mice (aged 6–10 weeks ...) and 82 neuropsin-KO mice and corresponding 70 wild-type mice (aged 6–10 weeks) were used".

V2(b), NRG1(177-246) intracerebroventricularly 10 min or 3 h after kainate, "5 μm". VERDICT: SUPPORTED WITH CHANGE.
- Methods: "Recombinant human epidermal growth factor-like domain of NRG1 (5 μm in PBS; NRG1177-246; PeproTech ...) or vehicle was delivered either 10 min or 3 h after KA administration via a Hamilton syringe mounted on an infusion pump (CFV-2100 ...) at a flow rate of 0.2 μl min−1 for 10 min. Control infusions used only PBS."
- Unit: in the PMC XML the unit is typeset as "5 μ<sc>m</sc>", which is a small-capital m. That reads as µM typographically. Plain-text extraction gives "5 μm". No other sentence or legend states the unit.
- Volume: no volume is printed. The flow rate and duration are printed, so 2 µL (about 10 pmol) is my derived arithmetic, not stated.
- Timing: the Results tie the 3 h injection to the c-Fos data. The legend for the seizure panel says only "The arrow denotes the point of vehicle or NRG1177-246 injection". The seizure-experiment injection time is therefore not stated in the text, and 3 h is inferred from the adjacent Results sentence.

V2(c), seizure score lower "only at 4 h". VERDICT: SUPPORTED WITH CHANGE.
- Legend, Fig 5d: "The seizure score for NRG1177-246-injected mice (black circles; n=5 mice) was significantly lower than that for vehicle-injected mice (white circles; n=5 mice) only at 4 h after KA administration (F(1,8)=1.134; *P=0.019; two-way ANOVA with the Sidak post-hoc test). ... Error bars indicate the SEM."
- Results: "injection of NRG1177-246 significantly reduced seizure severity at 4 h after KA administration in these mice (two-way ANOVA, F(1,8)=1.134, P=0.0186; Figure 5d)".
- Flag (ii): the text gives P=0.0186 and the legend 0.019. F(1,8)=1.134 corresponds to p of about 0.32 by my own computation. The printed F cannot be the test that gave P=0.019. Either the P belongs to the Sidak comparison at 4 h or the F is a misprint, and the text does not say which. By contrast, Fig 2's F(1,20)=5.744 with P=0.0264 is internally consistent.
- Flag (i): n=5 is mice. The same legend says "n=5 mice".
- Flag (iii): the seizure score is a behavioural Racine-type scale. The c-Fos E/I ratio in the same figure is a marker, not seizure function.

V2(d), which genotype received NRG1 in the seizure experiment. VERDICT: knockout only.
- Legend title: "Effect of intracerebroventricular injection of NRG1177-246 on E/I balance and KA-induced seizure in neuropsin-KO mice". Panel d is "vehicle- or NRG1177-246-injected neuropsin-KO mice".
- No wild-type NRG1 seizure arm is printed.
- Wild-type mice received NRG1 only in the slow-gamma experiment (Fig 6, n=6 per group), which is not a seizure readout.

ROW V3 (Tan 2011, abstract level only; Methods NOT read)
- Species and age: not stated. The abstract says "Using rodent models". The Nature page figure titles say "in the rat brain" (Fig 1) and "rat kindling model" (Fig 2). Fig 3 is "heart-rescued Erbb4 knockout mice". MeSH tags: Rats, Sprague-Dawley; Mice, Inbred C57BL; Male. No age appears anywhere.
- NRG1 route and amount: "infusing NRG1 intracerebrally". The amount is not stated.
- Soluble ErbB4 extracellular domain: "neutralizing endogenous NRG1 with soluble ErbB4 extracellular domain". Route and amount are not stated.
- n per group and statistic: not stated. The only hint is the MeSH tag "Analysis of Variance".
- PV-restricted deletion: the abstract says "specific depletion of ErbB4 in parvalbumin-expressing interneurons abolished NRG1-mediated inhibition of epileptogenesis". That implies NRG1 was dosed in that experiment. Dosing, route and n for that experiment cannot be confirmed without Methods.
- Bibliographic qualifier: the paper is Nat Neurosci 15(2):258-266 (2012), per the reference list in PMC11108068, and was online on 2011-12-11 per Europe PMC.

ROW V4 (Li 2011, abstract level only)
- The abstract gives: NRG1 via ErbB4 increased intrinsic excitability of FS-PV interneurons through Kv1.1; "mice with specific deletion of ErbB4 in parvalbumin interneurons were more susceptible to pentylenetetrazole- and pilocarpine-induced models of epilepsy"; "Exogenous NRG1 delayed the onset of seizures and decreased their incidence and stage."
- Not stated: species of the exogenous-NRG1 experiment, age, route, dose, n, statistic.
- MeSH: Male; Female; Mice, Transgenic. Nature page figure titles cover electrophysiology and human tissue, not the seizure experiment.
- Bibliographic qualifier: Nat Neurosci 15(2):267-273 (2012), online 2011-12-11.

ROW V5 (Liang 2020, abstract level only)
- Species: rats (Sprague-Dawley). The title says "Rats" and MeSH says Rats, Sprague-Dawley. They are not mice.
- Neonatal exposure: what was given neonatally was intermittent hypoxia, not NRG1. Abstract: "Neonatal postnatal day 5 (P5) rats were exposed to intermittent hypoxia (IH) or control (CON) room air for 10 days." Tissue and seizure testing were at P54: "Seizure susceptibility tests with ... pentylenetetrazole (PEN) at P54".
- NRG1: "Intracerebroventricular delivery of exogenous NRG1 before seizure induction by PEN significantly reduced the seizure susceptibility for neonatal IH-exposed rats. The ErbB4 inhibitor AG1478 inhibited the exogenous NRG1's effects on seizure susceptibility."
- Age at NRG1 delivery: not stated in the abstract. It is "before seizure induction", and induction was at P54.
- Dose, volume, n and statistic: not stated. The abstract does not say the animals were female. MeSH carries "Female", which is an indexer's tag.

ROW V6 (Jia 2020, full text read)

Route, dose, duration. VERDICT: as printed.
- Methods: "mice were pretreated p. o. for 21 days on a twice-daily schedule with 100 mg per kg lapatinib alone before PBS administration (5 animals); ... lapatinib groups were received with 50 mg per kg (5 animals) and 100 mg per kg (5 animals) lapatinib for 21 days before KA treatment, respectively".
- The twice-daily wording sits only in the lapatinib-alone group sentence. The schedule for the KA groups is not printed.
- No lapatinib vehicle is named. The text has no "vehicle", "gavage" or "dissolved".
- The model is intrahippocampal kainate: "KA (250 ng/μl) into the hippocampus ... KA (1 µl)". Mice are "Male C57BL/6J mice (6–8 weeks of age, weighing 18–22 g)". Fer-1 was "i. p. for 14 days (3 mg per kg Fer-1)".

n per group. Methods list 5 animals per group. Fig 1 legend: "mean ± SEM (n = 5)".

Statistic sentences.
- Results: "lower seizure score (ANOVA, F (3,16) = 12.61, p = 0.02), shorter seizure duration (ANOVA, F (3,16) = 49.66, p < 0.001) and smaller number of seizures within 90 min (ANOVA, F (3,16) = 19.83, p < 0.001) were observed".
- Methods: "one-way analysis of ANOVA with Tukey's post hoc test among three groups".
- Flag (ii): F(3,16)=12.61 corresponds to p of about 0.0002 by my computation, not 0.02. The Methods say "three groups" but the df imply four. The text also has a garbled sentence: "lapatinib at the dose of 100 mg per kg exhibited more evident protection ... than that by the dose of 50 and 100 mg per kg lapatinib had no significant effect on weight gain". A later sentence says "50 mg per kg ... comparable with treatment at the dose of 100 mg per kg".

Was ErbB4, ErbB2 or EGFR measured? VERDICT: NO.
- The strings ErbB, ErbB4, ErbB2, EGFR and HER2 occur only in the reference list, which begins at character 41,267. The only body text is "Lapatinib is a tyrosine kinase inhibitor which is approved for the treatment of breast cancer", with no receptor named.
- Mechanism measured was GPX4, SLC7A11, 4-HNE and PTGS2.
- Flag (iii): the ferroptosis markers are not an ErbB-target readout.

Corrigendum PMID 35046829.
- Verbatim: "In the original article, there was a mistake in Figure 5F and Figure 6B as published. Due to our carelessness in the process of rearranging these figures, the image in the “Era + Fer-1” group within Figure 5F and the image in the “Lap” group within Figure 6B were uploaded with mistakes. The corrected Figure 5 and Figure 6 appears below."
- Both panels are HT22 cell images. The seizure data (Fig 1) are not mentioned in the corrigendum.

(4) CONTRADICTIONS AND QUALIFIERS FOUND
- V1: the chronic NRG1 concentration is 10 µM, not the acute 100 µM. There is no wild-type NRG1 arm. A motor statement exists (open field, APP+NRG1 vs APP+PBS, N=6,7). N is undefined in the legends. The chronic readout age is not printed.
- V2: the printed F(1,8)=1.134 is incompatible with P=0.019. The text says 0.0186 and the legend says 0.019. The unit is resolved only by small-caps typesetting. NRG1 in the seizure experiment went to knockout mice only.
- V5: the neonatal manipulation was hypoxia, in rats, and testing was at P54. The age at NRG1 dosing is unstated.
- V6: F and p are inconsistent. The method says three groups against the four-group df. No ErbB measurement exists. The vehicle is unnamed.
- Secondary-source route data: a Letter (PMC11108068) describes Peterson 2021 as "25 micrograms per kilogram per day of NRG-1 or 0.1% bovine serum albumin intraperitoneal daily for 7 days" in intrahippocampal-kainate mice. I did not read the Peterson primary Methods. That description is secondary only.
- Brain-exposure context, relevant to V1(d): PMC3607352 (NRG1 EGF-domain, rat, carotid-artery injection) reports measured brain levels ("Cmax was 25.0-30.2 pg/mg") and "Pretreatment with NRG-1 did not protect against seizures in rats exposed to DFP". It is not a V1 paper.

(5) V7 ABSENCE RESULTS
Counts are PubMed esearch ([tiab] fields) / Europe PMC abstract-level (TITLE_ABS, SRC:MED). Both indexes cover essentially the same PubMed records. In every run Europe PMC returned zero records that PubMed did not. So these are two retrieval engines over ONE bibliographic corpus, not two independent corpora. NRG terms in the queries: neuregulin, NRG1, NRG-1, ErbB4, HER4. The ErbB-inhibitor query terms are listed in the B3 line below.

Queries and counts, all with an agent term set AND a seizure or interneuron term set:
- A1, NRG/ErbB4 AND seizure terms AND neonatal/juvenile/postnatal/pup/infant/immature terms: 5 / 4.
- A2, NRG/ErbB4 AND interneuron/PV/IPSC/GABAergic AND age terms AND administration terms AND rodent: 12 / 14.
- A3, ErbB inhibitors (AG1478, PD158780, afatinib, lapatinib, neratinib, "ErbB inhibitor", "ErbB4 inhibitor/antagonist") AND seizure/interneuron AND age terms: 1 / 1.
- A4, NRG/ErbB4 plus inhibitors AND age terms AND seizure/EEG/PV/interneuron/IPSC/GABA: 35 / 31.
- B1, NRG/ErbB4 AND seizure/interneuron/PV/IPSC/GABAergic (broad): 307 / 291. I read all 307 abstracts with an age-regex screen: 41 passed it.
- B2, NRG/ErbB4 AND seizure terms: 56 / 52.
- B3, ErbB-inhibitor list (AG1478, PD158780, PD153035, afatinib, lapatinib, neratinib, gefitinib, erlotinib, canertinib, dacomitinib, "ErbB inhibitor", "EGFR inhibitor", "tyrosine kinase inhibitor", "pan-ErbB", etc.) AND seizure terms: 82 / 73.
- B4, NRG/ErbB4 plus inhibitors AND systemic-route terms (systemic, subcutaneous, intraperitoneal, intranasal, intravenous, oral, peripheral) AND seizure/PV/interneuron/IPSC: 24 / 22.
- C1, NRG/ErbB4 AND seizure/interneuron/GABA AND aggravate/exacerbate/reduce/decrease/disrupt terms: 294 / 205. I screened it with a regex and read the abstracts that matched.
- Third route, Europe PMC open-access full text (not abstract-only):
  - F1, NRG/ErbB4 AND neonatal terms AND seizure models AND injected/administered, OPEN_ACCESS: 369 hits.
  - F2, NRG/ErbB4 AND systemic routes AND seizure models/PV AND recombinant/peptide, OPEN_ACCESS: 297 hits.
  - I screened only the top 200 returned of each, and only items whose title or abstract mentions NRG or ErbB. A paper that uses NRG1 as a tool without naming it in the abstract would be missed. A full-text-only hit beyond rank 200 would also be missed.

(A) Neonatal or juvenile modulator with a seizure, threshold, EEG spike-wave, interneuron-count or IPSC readout. VERDICT: PARTLY ABSENT.
- Seizure, threshold or EEG spike-wave readout with a neonatal or juvenile modulator: none found in A1-A4, B1-B2, F1. This rests on two retrieval routes over one corpus, plus the open-access full-text sample. Absence is "none found", not exclusion.
- IPSC or interneuron readout: NOT absent.
  - 21490211, Abe et al., J Neurosci 2011. Abstract: "A core peptide common to all NRG1 variants (eNRG1) was subcutaneously administered to mouse pups ... Postnatal eNRG1 treatment significantly enhanced polysynaptic IPSCs, although monosynaptic IPSCs were not affected ... increased AMPA-triggered inward currents ... [in] parvalbumin-containing GABAergic interneurons". I read this abstract only. The pup age is not given in it.
  - 26935991, 2016: "neonatal neuregulin-1 challenge" with "perinatal NRG1 pretreatment diminished inhibitory miniature synaptic currents as well as GABAA receptor sensitivity" at the adult stage. Route and age are not in the abstract.
  - The 2017 meeting abstract PMC5475707 (title only, no PMID) reports NRG1 or EGF given to newborn mice, rats and monkeys with abnormal GABAergic development. It is an abstract, not a primary.
- Set aside:
  - 24949465: a review.
  - 28608461: EGF, an ErbB1 ligand, in mouse pups with reduced GAD/PV and mIPSC frequency. Not an NRG1/ErbB4 modulator, though ErbB1/ErbB4 are co-expressed.
  - 32870492: the neonatal manipulation is hypoxia, and NRG1 timing is unstated.
  - 36613949: neonatal hypoxia-ischemia with no modulator.
  - 36460130: pan-ErbB inhibitor "during adolescence", with anxiety and GAD67 readouts.
  - 23380917: perinatal phencyclidine, not an ErbB modulator.

(B) Systemically administered NRG1 or ErbB4 agonist or small molecule with a seizure or PV-interneuron readout. VERDICT: NOT ABSENT.
- 21490211: subcutaneous NRG1 core peptide, with PV-interneuron AMPA-current readout (above). It is also neonatal.
- 22583949, rat: NRG1 EGF-domain and GGF2 given "i.a" into the carotid artery. Seizure scoring: "Pretreatment with either NRG-EGF or NRG-GGF2 had no effect on DFP-induced seizure activity". Brain exposure was measured. Neuronal injury was reduced. The route is intra-arterial, not one of the five you listed. Seizure readout was null.
- 33362556 (V6): oral lapatinib with a seizure readout. It is an ErbB inhibitor, not an agonist, and ErbB was not measured.
- Peterson 2021 (PMID 34742879): intraperitoneal NRG1 per the secondary Letter only. The abstract's outcomes are neuronal death and EAAC1, and no seizure scoring appears in the abstract.
- Set aside:
  - 31720762: intranasal NRG1 after traumatic brain injury, readout neurological function, with PV-ErbB4 knockout mice. Not a seizure or PV readout in the abstract.
  - 40940223: a small-molecule ErbB4 agonist in APP/PS1 mice, with cognition and amyloid readouts. Route and age are not in the abstract.
  - 24433482: NRG1 in a cerebral-malaria model, with a mortality readout.
- Not found: a systemic NRG1 or ErbB4 agonist with a positive seizure outcome. Two retrieval routes over one corpus plus the full-text sample.

(C) Enhancing signalling aggravated seizures or interneuron function; or ErbB-kinase inhibition improved seizures with ErbB4 specifically identified. VERDICT: NOT ABSENT for the first half, and absent for the second half.
- Enhanced NRG1 signalling with reduced inhibition or increased epileptiform tendency (all abstract level):
  - 15132433 (2004): NRG1 "reduces the expression of GABAA receptors alpha subunits in hippocampal slices, and the mean amplitude of GABAergic miniature IPSCs".
  - 24218551 (2013): ErbB4 "reduces synaptic GABAA currents independent of its receptor tyrosine kinase activity".
  - 21878485 (2012): NRG1 type I transgenic overexpression, with "an increased tendency to epileptiform activity" in slices. This is genetic, not an administered agent.
  - 26935991: perinatal NRG1 diminished inhibitory mIPSCs.
  - 33436636: NRG1 overexpression in interneurons gave cortical disinhibition.
  - 33871014: embryonic NRG1 overexpression gave reduced inhibitory neurotransmission.
  - None of these is an in vivo seizure aggravation by administered NRG1. None found.
- ErbB-kinase inhibition improving seizure outcomes with ErbB4 specified as the target: none found.
  - 33362556 improved seizures but did not measure ErbB.
  - 34020711: an ErbB kinase antagonist and the T796G mouse blocked the ketogenic diet's anti-seizure effect. That is the opposite direction.
  - 22381732: ErbB inhibitors improved LTP and fear memory in Angelman mice, with no seizure readout.
  - 24582454 (lestaurtinib): a Trk inhibitor.

(6) WHAT I COULD NOT CHECK
- V3, V4, V5 Methods (age, amount, route, n, statistic): paywalled. The Nature and Springer pages were previews, and no PMC or Europe PMC full text exists. I did not use shadow libraries or institutional access.
- Peterson 2021 primary Methods: no PMC copy, and the Elsevier route returned only an interstitial that I did not follow.
- Abstracts only for all V7 hits except those named as read in full text (22583949, 21490211 header, 38774253 letter).
- V7 coverage is limited to abstract-keyword matches. Full-text-only mentions are covered only by the top-200 open-access sample of F1 and F2.
- Figure images were not viewed, so the V2 injection arrow and any in-figure n labels are unread.
- The p-value checks are my own computation of the F distribution (F(1,8)=1.134 gives p about 0.32; F(3,16)=12.61 gives p about 0.0002). They are not printed in either paper.
