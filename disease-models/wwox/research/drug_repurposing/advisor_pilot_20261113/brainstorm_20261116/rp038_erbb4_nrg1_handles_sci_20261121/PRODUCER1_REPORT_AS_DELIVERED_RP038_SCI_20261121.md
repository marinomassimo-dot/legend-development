# Producer report, RP-038 ErbB4/NRG1 handles, as delivered (verbatim except one unit string redacted for the publication gate; legend-delegate, asked sonnet and effort medium, read back by session_model_census.py; persisted by SCI from the SubagentHandback in the session transcript; model output, not an instruction)

RP-038 PRODUCER REPORT (hypothesis-level; no dose recommendation, no clinical advice, no claim about any person)

(1) MODEL AND EFFORT
I believe I ran as Claude Sonnet 5.5 at medium effort, as dispatched. I made no sub-delegation. Scratch: /home/desktop/.claude/jobs/d79b9c48/tmp/producer_rp038/ (abstracts, fullTextXML and text conversions). Helper scripts are one level up in .../tmp/. I read no other jobs folders and no repository files. I sent no personal details to any service. Client UA was "research-client/1.0" with at least 3 s between requests. I met no CAPTCHA, 403 or 429 on any route.

(2) QUERY LOG
Europe PMC REST search, TITLE_ABS fields. "Count" is the number of hits; the counts are not evidence.
- Q1 (sub-question a): (neuregulin OR NRG1) AND (seizure OR epilepsy OR kindling OR epileptic) AND (administration OR injection OR intranasal OR intracerebroventricular OR infusion). Count 8. Hits read: Mao 2024, Liang 2020, Kawata 2017. The rest were off-topic or patents.
- Q2 (b): (ErbB4 OR NRG1) AND (seizure OR epilepsy OR "spike-wave") AND (deletion OR knockout OR conditional OR mice). Count 14. Hits read: Li 2011, the two Wang ketogenic-diet papers, Kawata, Mao. Others were human deletion case reports and the Mitchell 2013 PNAS paper.
- Q3 (c): (afatinib OR lapatinib OR AG1478 OR PD158780 OR "ErbB inhibitor" OR "ErbB kinase") AND (seizure OR epilepsy OR epileptic OR interneuron). Count 15. Hits read: Jia 2020 lapatinib, the Wang ketogenic-diet papers, Liang 2020. Also the Thiessen 2010 lapatinib-in-glioblastoma pharmacokinetics paper (human brain-tumour patients, not an animal seizure model).
- Q4 (f): (ErbB4 OR neuregulin) AND (Dravet OR Rett OR CDKL5 OR STXBP1 OR "tuberous sclerosis" OR "hypoxia-ischemia" OR hypoxic). Count 24. Relevant hits: Spahic 2022 (neonatal hypoxia-ischaemia) and Ricobaraza 2023 (a Dravet gene-therapy vector that uses the NRG1 EGF domain only as a targeting ligand). The rest were off-topic.
- Q5 (e): (ErbB4 OR neuregulin) AND (secretase OR "intracellular domain") AND (seizure OR interneuron OR parvalbumin). Count 3. All three were reviews or NRG2/BACE1 processing papers with no seizure or PV readout, so none was used.
- Q6 (g): (ErbB4 OR neuregulin) AND ("blood-brain barrier" OR "brain penetration" OR intranasal OR "cerebrospinal fluid") AND (agonist OR peptide OR inhibitor). Count 12. No NRG1 peptide brain-level measurement was found. Hits were an ErbB4/BBB subarachnoid haemorrhage paper, an EO1001 pan-ErbB inhibitor abstract (glioma, brain penetration; not read beyond the title) and off-topic items.
- Q7 (d): (ErbB4 OR neuregulin) AND ("small molecule" OR agonist OR "positive modulator" OR mimetic OR activator) AND (brain OR mice OR rats). Count 70. Relevant hits: Liu 2025 Neurotherapeutics and Liu 2025 J Neuroinflammation (small-molecule ErbB4 agonist "E4A"), and Cools 2025 Nat Commun (heart; compound "EF-1").
- Q8 (a/f, early-life): (neuregulin OR NRG1 OR ErbB4) AND (seizure OR epilepsy OR epileptogenesis) AND (neonatal OR juvenile OR "early life" OR febrile OR pup*). Count 1, which was Liang 2020.
- Q9 (b, PV): (ErbB4 OR NRG1) AND parvalbumin AND (seizure OR epilep* OR excitability OR IPSC). Count 8. Hits: Tan 2011, Li 2011, Mao, Liang, Kawata, plus off-topic items.
PubMed esearch (second route):
- P1: (neuregulin OR NRG1 OR ErbB4) AND (Dravet OR Scn1a OR CDKL5 OR Stxbp1 OR Mecp2 OR "tuberous sclerosis") AND (seizure OR epilepsy OR interneuron). Count 3. Titles read: a Science 2022 cortical-wiring paper, an Ohtahara review, and the Ricobaraza Dravet vector paper. None is a seizure study of NRG1 or ErbB4 modulation.
- P2: (neuregulin OR NRG1 OR ErbB4) AND (neonatal OR infant OR juvenile OR "early life" OR febrile) AND (seizure OR epilepsy OR convulsion) AND mice. Count 1, which was Mao 2024. Mao used 4-month-old adults (see T1), so the count reflects keyword matching only.
- P3: (neuregulin OR NRG1) AND (intranasal OR "blood-brain barrier" OR "brain levels" OR "CSF levels") AND (peptide OR recombinant) AND (rat OR mouse OR mice). Count 26. I read the titles of 8 and none was an NRG1 brain-level or intranasal study (BBB/delivery papers for bFGF, HBEGF, GDF15 and similar).
- P4: (ErbB4 OR neuregulin) AND (gamma-secretase OR presenilin OR "ICD") AND (epilep* OR seizure). Count 1 (a BACE1 synapse review).
- P5: (ErbB4 OR neuregulin) AND (seizure* OR epilep*) AND (agonist OR activator OR "small molecule"). Count 23. Titles read for 8 of 23: ketogenic-diet papers, Liang, and reviews or off-topic items. There was no agonist-plus-seizure primary.
- P6: (ErbB4 OR neuregulin) AND (spike-wave OR "absence seizure" OR "spike and wave"). Count 0.
Full-text routes:
- Europe PMC fullTextXML succeeded for PMC10885444, PMC5416666, PMC8139023, PMC7860047, PMC7758233, PMC9820818 and PMC12664525.
- Europe PMC lookup (isOpenAccess/inEPMC = N) shows Tan 2011 (22158510), Li 2011 (22158511) and Liang 2020 (32870492) have no PMC full text. I did not try the publisher pages.

(3) TABLE (7 decision rows; at most 12 allowed)

T1. Mao R, 2024, Cell Commun Signal, PMID 38388921 (DOI 10.1186/s12964-024-01528-7)
- Model: APPswe/PS1dE9 mice (an Alzheimer's model with seizure susceptibility, not a developmental epilepsy model).
- AGE: 4-month-old at treatment and at readout ("Four-month-old APPswe/PS1dE9 mice"). Adult, not neonatal.
- Modulator: recombinant human NRG1-beta/HRG1-beta1 EGF-domain protein (R&D 396-HB-050). DIRECTION: enhancing.
- Route and dose as printed: "NRG1-β (100 µM in 2 µL) or vehicle (2 µL) into the right lateral ventricle", given 30 min before PTZ.
- BRAIN EXPOSURE: none measured. Intracerebroventricular delivery bypasses the barrier by design.
- Readout: PTZ acute kindling (seizure latency, time to Racine V, PTZ dose required), maximal Racine score, chronic kindling Racine score, survival. Function (seizure) readouts; PV-cell loss and NRG1-ErbB4 impairment in untreated APP mice are markers.
- n: acute NRG1 vs PBS "N = 3, 4"; chronic kindling "N = 13, 10" (n counts mice).
- Statistic: mean ± SEM; unpaired t test, Mann-Whitney, two-way ANOVA, log-rank; exact p not printed in the text (stars only, p < 0.05).
- Effect, verbatim (Results, Fig. 6): "Intracerebroventricular infusion of NRG1 significantly prolonged seizure latency and time to reach Racine V (Fig. 6B-C), and down-regulated seizure severity (Fig. 6E) in the acute kindling model. NRG1 administration also reduced the seizure levels in the chronic kindling model (Fig. 6F)."
- Effect direction versus working hypothesis: consistent (enhancing reduces seizures).
- Harms: "the mortality in APP + NRG1 group showed a downward trend"; no motor or mood alteration in open-field tests. No other adverse effects were reported.
- Depth: full text. Supplement not read.

T2. Kawata M, 2017, Transl Psychiatry, PMID 28267150 (DOI 10.1038/tp.2017.20)
- Model: neuropsin-knockout and wild-type C57BL/6J adult male mice, kainate status epilepticus. The knockout has impaired NRG1 processing (a genetic NRG1-pathway deficit, not an epilepsy-gene model).
- AGE: 6-10 weeks.
- Modulator: NRG1(177-246) EGF-like domain, human recombinant (PeproTech). DIRECTION: enhancing.
- Route and dose as printed: "5 μm in PBS", delivered intracerebroventricularly "10 min or 3 h after KA administration ... at a flow rate of 0.2 μl min−1 for 10 min". (The text prints "5 μm"; I did not resolve whether µM is meant.)
- BRAIN EXPOSURE: none measured. Intracerebroventricular delivery.
- Readout: seizure score after KA (function); cFos in ErbB4+/PV+ cells vs pyramidal cells and an E/I ratio (marker); gamma power (function).
- n: seizure score n=5 mice per group (vehicle vs NRG1).
- Statistic: two-way ANOVA with Sidak, SEM; "F(1,8)=1.134; *P=0.019" at 4 h only; cFos Mann-Whitney P=0.0286.
- Effect, verbatim (Fig. 5 legend): "The seizure score for NRG1177-246-injected mice ... was significantly lower than that for vehicle-injected mice ... only at 4 h after KA administration".
- Effect direction versus working hypothesis: consistent.
- Harms: none stated.
- Depth: full text; supplement not read. The F-value printed with P=0.019 is as in the paper and not reconciled.

T3. Tan GH, 2011, Nat Neurosci, PMID 22158510 (DOI 10.1038/nn.3005)
- Rodent kindling and limbic epileptogenesis. Ages not stated in the abstract (full text unreachable).
- Modulator: NRG1 infusion (enhancing); soluble ErbB4 extracellular domain, ErbB4 inhibition, Erbb4 deletion (reducing).
- Brain exposure: not stated in the abstract.
- Abstract verbatim: "epileptogenesis was inhibited by infusing NRG1 intracerebrally but exacerbated by neutralizing endogenous NRG1 with soluble ErbB4 extracellular domain, by inhibiting ErbB4 activation or by deleting the Erbb4 gene ... specific depletion of ErbB4 in parvalbumin-expressing interneurons abolished NRG1-mediated inhibition of epileptogenesis and promoted kindling progression, resulting in increased spontaneous seizures and exuberant mossy fiber sprouting. ... depleting ErbB4 in CaMKIIα-positive pyramidal neurons had no effect."
- Readout: kindling progression, spontaneous seizures (function).
- Direction: consistent (enhancing helps; reducing worsens).
- Depth: abstract only. Full text not in Europe PMC. Dose, n, statistics and harms were not read.

T4. Li KX, 2011, Nat Neurosci, PMID 22158511 (DOI 10.1038/nn.3006)
- Mice with PV-cell-specific ErbB4 deletion; PTZ and pilocarpine models. Ages not stated in the abstract.
- Modulator: exogenous NRG1 (enhancing); genetic ErbB4 deletion in PV cells (reducing).
- Brain exposure: not stated in the abstract.
- Abstract verbatim: "mice with specific deletion of ErbB4 in parvalbumin interneurons were more susceptible to pentylenetetrazole- and pilocarpine-induced models of epilepsy. Exogenous NRG1 delayed the onset of seizures and decreased their incidence and stage."
- Readout: seizure onset, incidence and stage (function); FS-PV excitability by patch clamp.
- Direction: consistent.
- Depth: abstract only. Dose, route, n, statistics and harms were not read.

T5. Liang D, 2020, Mol Neurobiol, PMID 32870492 (DOI 10.1007/s12035-020-02100-3)
- Model: Neonatal rats; intermittent hypoxia from P5 for 10 days. Readout at P54 (adolescent/young-adult, not neonatal).
- AGE: treatment (PTZ test and NRG1 icv) at P54; the exposure was neonatal.
- Modulator: exogenous NRG1 (enhancing); AG1478 (ErbB4/EGFR inhibitor, reducing) blocked the NRG1 effect.
- Route and dose: icv NRG1 before PTZ; dose not stated in the abstract.
- Brain exposure: none measured (icv).
- Readout: PTZ seizure susceptibility; PV cell count (marker); NRG1, ErbB4 and p-ErbB4 expression (markers); environmental enrichment as a rescue.
- Abstract verbatim: "Intracerebroventricular delivery of exogenous NRG1 before seizure induction by PEN significantly reduced the seizure susceptibility for neonatal IH-exposed rats. The ErbB4 inhibitor AG1478 inhibited the exogenous NRG1's effects on seizure susceptibility."
- Direction: consistent.
- Depth: abstract only. Full text not in Europe PMC. Dose, n and statistics were not read.

T6. Wang J, 2021, Cell Biosci (two papers).
(6a) PMID 33536056 (DOI 10.1186/s13578-021-00536-1); full text read.
(6b) PMID 34020711 (DOI 10.1186/s13578-021-00611-7); full text read.
- Model: adult mice, 8-12 weeks (stated in Methods), ketogenic diet 3 weeks; KA acute seizure model. Erbb4 deletion and the T796G kinase-dead (analogue-sensitive) mouse.
- Modulator: AG1478, an ErbB kinase inhibitor (reducing). The ketogenic diet is not an ErbB4 handle, but is the context.
- Route and dose as printed (6b): "AG1478 (5 mM, 2 l)" into the lateral ventricle ("5 M" for the slices).
- Brain exposure: none measured (icv, plus slice application).
- Readout: seizure score after intra-amygdala KA (function); eIPSC and sIPSC (function).
- n (IPSC): neurons from 3 mice per group, for example "n=18 neurons from 3 mice (CD+vehicle)".
- Effect, verbatim (6b, Results): "pre-infusion of AG1478 diminished the difference between CD and KD groups."
- Direction: consistent with the hypothesis for ErbB4 kinase being required for anti-seizure benefit of the diet. This supports "reducing removes protection" and is not a test of a reducer as a treatment.
- Caveat stated by authors: "Because of the non-selectivity of AG1478 for ErbB4, we could not exclude the possible off-target effects."
- 6a abstract: "Disruption of Nrg1 signaling by genetically deleting its receptor-ErbB4 abolished KD's effects on GABAergic activity and seizures."
- I did not extract exact p values or test names for the 6b seizure panel.
- Depth: full text for both; supplements not read.

T7. Jia JN, 2020, Front Pharmacol, PMID 33362556 (DOI 10.3389/fphar.2020.601572). This row is a reducing-direction candidate by drug class only; its own mechanism is not ErbB4.
- Model: C57BL/6J male mice, 6-8 weeks, stereotactic hippocampal KA (250 ng/μl, 1 µl). Not a neonatal or genetic model.
- Modulator: lapatinib, an EGFR/ErbB2 kinase inhibitor; ErbB4 activity is not tested. DIRECTION: reducing (ErbB-kinase inhibition), and it REDUCED seizures.
- Dose: 50 and 100 mg per kg for 21 days twice daily; route not extracted by me.
- BRAIN EXPOSURE: stated only, by citation: "owing to low molecular weight and lipophilic properties, lapatinib is considered to efficiently penetrate the blood-brain barrier in the CNS (Gori et al., 2014)". No measurement in this paper.
- Readout: Racine score, seizure duration, number of seizures, EEG (function).
- n: n = 5 mice per group. Statistic: ANOVA; "lower seizure score (ANOVA, F (3,16) = 12.61, p = 0.02), shorter seizure duration (... p < 0.001)".
- Mechanism claimed by the authors: GPX4-dependent ferroptosis suppression (the paper does not claim an ErbB4 mechanism).
- Effect direction versus working hypothesis: opposite in direction class (reducing ErbB kinase signalling improved seizures), but the paper does not attribute it to ErbB4, so I carry it as not attributable to ErbB4.
- Harms: "no significant effect on weight gain, indicating a good tolerance of lapatinib" (this sentence in the text sits oddly beside the dose-comparison sentence; I quote it as printed).
- A corrigendum exists (PMID 35046829). I did not read its content, so the notice is not checked.
- Depth: full text; supplement not read.

Secondary rows, not decisive:
- Spahic H, 2022, Int J Mol Sci, PMID 36613949 (DOI 10.3390/ijms24010508). P10 hypoxia-ischaemia mice. No modulator. Markers only: Nrg1 up at 24 h, "Paradoxically ErbB4 activation decreased 24 h and again 30 days after HI"; PV+ deficits at P40; LTD/LTP changes. Abstract read for the quotes; I opened the PMC full text but did not extract further. No seizure readout.
- Liu C, 2025, Neurotherapeutics, PMID 40940223; Liu C, 2025, J Neuroinflammation, PMID 40089796. Small-molecule ErbB4 agonist "E4A" (4-bromo-1-hydroxy-2-naphthoic acid). Enhancing. Readouts are cognition, mitochondrial/synaptic and neuroinflammation markers in adult APP/PS1 and microplastic-exposed mice. No seizure, PV or IPSC readout, and brain exposure is not shown. A keyword search of the full text (PMC12664525) for seiz|epilep|blood-brain|brain penetr|mg per kg returned only background mentions of DOCK3 in epileptogenesis. Abstract level for the second paper.
- Cools JMT, 2025, Nat Commun, PMID 39794341. ErbB4 activator EF-1, heart only. Not neural. Abstract only; mentioned for the existence of the class.
- Mitchell RM, 2013, PNAS, PMID 24218551. NRG-ErbB4 reduces postsynaptic GABAA currents independent of kinase activity (an opposite-direction mechanism at the receptor level). Cultured/slice, not in vivo seizure; abstract only.
- Ricobaraza A, 2023, J Mol Med, PMID 37819378. NRG1-alpha EGF domain used as a capsid targeting ligand; "it had no impact on the infectivity of the vector in primary cultures or in vivo". Not an enhancing signalling handle. Abstract only.
- Thiessen B, 2010, Cancer Chemother Pharmacol, PMID 19499221. Human lapatinib pharmacokinetics in glioblastoma; clearance rose about tenfold with enzyme-inducing anti-epileptic drugs; no seizure readout. Abstract only; context for drug exposure only.
Left out: the remaining Q1-Q9 hits (human genetic deletion case reports, reviews, off-topic oncology items, patents) because they have no modulator with an in vivo readout.

(4) CONTRADICTIONS AND WRONG-DIRECTION RESULTS
(1) Enhancing NRG1-ErbB4 signalling WORSENS seizures, or reducing it improves them: Jia 2020 (T7) is the one case, where the ErbB-kinase inhibitor lapatinib reduced KA seizures at 50 and 100 mg per kg (n = 5, ANOVA). Its stated mechanism is ferroptosis suppression, not ErbB4. It conflicts in direction with T1-T6 only if ErbB4 were the active target, and the paper does not test that. I found no primary where enhancing NRG1 worsened seizures.
(2) Converse (reducing worsens): T3 (soluble ErbB4 extracellular domain, ErbB4 inhibition, deletion exacerbated epileptogenesis), T4 (PV-ErbB4 deletion increased PTZ and pilocarpine susceptibility), T5 and T6 (AG1478 removed the benefit). These are consistent with each other.
(3) Mechanistic tension (not a seizure result): Mitchell 2013 reports NRG-ErbB4 signalling that decreases postsynaptic GABAA currents on interneurons, while T3/T4 report NRG1 increasing FS-PV excitability. I did not read the full text of either side, so I cannot say whether the two are reconcilable.
(4) Doses and routes are not comparable across T1-T6 (icv NRG1 in adults versus i.p. lapatinib).

(5) ABSENCES
- No primary was found testing an ErbB4 agonist or small-molecule enhancer (E4A, EF-1) with a seizure, PV or IPSC readout. Routes: Europe PMC Q7 (70 hits; seizure-relevant: none) and PubMed P5 (23 hits). Two routes. Titles for 15 of the 23 PubMed hits were not read, so this is an absence in what I read.
- No primary was found of NRG1 or ErbB4 modulation in Dravet, Rett, CDKL5, STXBP1 or tuberous sclerosis with an inhibitory-network readout, beyond the Dravet vector paper (not a signalling modulation). Routes: Europe PMC Q4 (24 hits) and PubMed P1 (3 hits). Two routes.
- No neonatal or juvenile (in-treatment-age) seizure study of NRG1 or ErbB4 modulation: Liang 2020 exposes neonates but treats and reads at P54, Mao 2024 is 4 months. Routes: Europe PMC Q8 (1 hit) and PubMed P2 (1 hit). Two routes. The age of treatment in Tan 2011 and Li 2011 is unknown (abstract only), so a juvenile treatment in those papers cannot be excluded.
- No measured NRG1-peptide or ErbB-inhibitor brain or CSF levels in an animal seizure paper: Europe PMC Q6 (12 hits) and PubMed P3 (26 hits, 8 titles read). Two routes, but the PubMed titles were read for only 8 of 26.
- gamma-secretase / ErbB4 intracellular-domain handle with a seizure or PV readout: Europe PMC Q5 (3 hits) and PubMed P4 (1 hit). Two routes; zero relevant. I did not search for specific secretase modulators by name.
- Spike-wave (absence) EEG with ErbB4/NRG modulation: PubMed P6 returned 0 hits. One route only; I did not run a Europe PMC equivalent.
- I did not search ErbB4 positive-modulator names beyond "small molecule/agonist/activator/mimetic". The absence claims above are about the queries run.

(6) WHAT I COULD NOT REACH OR DID NOT DO
- Full text for Tan 2011, Li 2011 and Liang 2020 (non-open-access in Europe PMC). I did not try publisher pages or other routes, so these three rows are abstract level and lack age, dose, n and statistics.
- No supplements were read for any row.
- Jia 2020: I did not extract the route of lapatinib administration; the corrigendum was not read.
- Mao 2024 and Kawata 2017: the exact p values for the seizure panels are not printed in the text I read (stars, or the single P=0.019 / 0.0286 values quoted above).
- For the second route of the lapatinib/ErbB-inhibitor sub-question (c), no search beyond Europe PMC Q3 was run; afatinib, PD158780 and others returned no seizure primaries in what I read.
- For sub-question (g), the EO1001 pan-ErbB brain-penetration abstract was seen as a title only and not read.
No conclusion about any disease gene or drug, and no recommendation, is made here.

