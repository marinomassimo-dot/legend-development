# Blind report, ADV-282 increment 5 (verbatim, SCI 2026-11-26)

Delegate: legend-delegate, model sonnet, effort high stated in the dispatch; census of its transcript: 18 {'high': 18} {'claude-sonnet-5-5': 18} 37940 1342319 131200 (turns, effort, model, output tokens, cache-read, peak context). Delivered by its SubagentHandback call and copied byte for byte from the delegate transcript (subagents/agent-a76d3cc3ed649fde2.jsonl). Packet: `BLIND_SENTENCES_ADV282_INC5_SCI_20261126.md` (sha256 2b269f78...). My first reading was frozen before the report (FIRST_READ_ADV282_INC5_SCI_20261126.tsv, sha256 3f976ba5...). DR-L01-003 was not in the packet (NOT ASSESSABLE, HTTP 503).

---

BLIND VERIFIER REPORT, ADV-282 increment 5 (7 blocks). Date of query 2026-11-26. No network, no email sent, nothing written in the repository. Scratch text extracts are in /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/ (alek.txt, cpp.txt).

Note on the rule: where a check is only a citation of another paper I applied "PRESENT BUT NOT MATCHED". Where an abstract reports an engagement or pathway readout I applied "PRESENT".

=====================================================================
DR-E01-003 (2BAct, PMID 42179084, abstract only)
=====================================================================
Class (main null: "amyloid burden not reduced"): CHECK PRESENT (abstract-reported, pathway-level proxy).
- In-study check: yes. The Methods sentence says "ISR inhibition was evaluated by examining the phosphorylation level of eIF2α using immunofluorescence ... and analyzing ISR-related markers via RNA sequencing". The Results sentence says "Reduced levels of phosphorylated eIF2α were also confirmed by immunofluorescence staining". This is the same mice and the same dose (10 mg/kg/day i.p., 23 days).
- Caveats:
  - p-eIF2α sits upstream of the drug's direct target. The row calls 2BAct an eIF2B activator, so it is not a direct eIF2B readout.
  - The brain region and the n are not given.
  - The RNA-seq result is not stated in the abstract.
  - If the Orchestrator wants a strict reading of "direct readout", this becomes NOT ASSESSABLE (abstract).
- Other effect on other endpoints: yes. NORT performance improved, microglial activation fell, and tau accumulation fell (Results sentence). Donepezil was the positive control for behaviour, not an engagement check.
- Check locator: PMID42179084_efetch.xml, AbstractText, Methods and Results sentences.
Verdict: ADD.
Findings:
- Each clause matches the abstract: improved object recognition, attenuated microglial activation and tau, no reduction of Aβ, reduced p-eIF2α, 10-month-old mice, 10 mg/kg/day, 23 days.
- A reader needs these qualifications, none of which are in the note:
  - The mice are 5xFAD amyloid-transgenic, so "amyloid not reduced" is in an amyloid-overexpression model.
  - Only the object recognition test is reported as improved. The abstract does not state the Morris water maze or open-field results.
  - One dose, i.p., against vehicle and a donepezil comparator. No n and no statistics are given.
  - The authors themselves call the effects "limited".
  - The abstract calls 2BAct an "ISR inhibitor". "eIF2B activator" is not in the abstract.
Proposed wording: "In 10-month-old 5xFAD mice, 2BAct 10 mg/kg/day i.p. for 23 days improved novel-object recognition and reduced microglial activation and tau, but not amyloid-beta burden; p-eIF2 alpha was lower. Other behavioural tests are not reported in the abstract; one dose, one study, authors call the effects limited."

=====================================================================
DR-W2-004 (Alekseeva 2026, PMC13509269, full text and figures)
=====================================================================
Class:
- Memantine ("fully blocked" NMDAR claim): CHECK PRESENT BUT NOT MATCHED. This is citation-only. Discussion: "the dosages, timing (60 min pre-treatment), and routes of memantine administration strictly corresponded to those validated in vivo protocols, ensuring that NMDA receptors were fully blocked". The cited work is on other seizure models, at 5–20 mg/kg. No in-study measurement of NMDAR block, drug level, or receptor effect.
- Perampanel: CHECK PRESENT BUT NOT MATCHED, also citation-only. Doses were "chosen based on established literature data" (Methods 2.3, refs 18 and 20). I found no level, occupancy, or EEG readout.
- In-study check on target engagement: no, for both drugs.
- Other in-study readouts, recorded separately:
  - The MSO positive control (Fig 2A and 2B, 5 ATA, 50 and 100 mg/kg) shows the model detects acceleration by glutamate accumulation. It is a different drug and a different pressure.
  - A perampanel dose-response on stage latency (Fig 4A and 4B) shows pharmacological activity on the seizure endpoint.
- Query: the held XML text, searched for plasma, serum, concentration, occupancy, EEG, electrophys, patch, pharmacokin, confirm and blocked. The only hits were background, MSO and citations.
Verdict: MUST CHANGE.
Findings:
1. "Memantine accelerated every seizure stage" is not true at every dose. In Fig 3A (adult male Wistar, 6 ATA O2, i.p., 1 h pre-treatment, n=8 per drug group as given by the ANOVA df):
   - Mem 1 mg/kg: stages 1 and 2 are asterisked. Stages 3 and 4 are not.
   - Mem 5 mg/kg and Mem 25 mg/kg: all four stages are asterisked.
   - Stage 4, bar heights read from Fig 3A, approximate: control ~37 min, Mem 1 ~32 (not significant), Mem 5 ~26, Mem 25 ~25.
   - Fig 3B: Mem 5 is **, Mem 25 is ***, Mem 1 has no mark.
   - Text 3.3 says "memantine (1–25 mg/kg) shortened the latency to the onset of each successive seizure stage". The figure contradicts that for 1 mg/kg.
2. Perampanel:
   - Fig 4B stage 4: Per 1 mg/kg is ****, Per 5 mg/kg is **, Per 0.2 mg/kg has no mark. Stage 4 bar heights from Fig 4A: control ~37, Per 0.2 ~51, Per 1 ~69, Per 5 ~57 min.
   - The note says it delayed stage 4. Results 3.4 also names stage 3. Fig 4A additionally asterisks stages 1 and 2 at Per 1.
   - Fig 4A asterisks stages 3 and 4 at Per 0.2, but text 3.4 and Fig 4B say 0.2 had no significant effect. This is an internal inconsistency.
3. "Did not prevent seizures" is supported for the 1 mg/kg group only. Results 3.5 says seizures occurred in 100% of control and memantine animals and in "7 out of 8 (87.5%) in each" of the perampanel and combination groups. Fig 5B shows the Per 1 curve ending at 12.5% seizure-free. Incidence for Per 0.2 and Per 5 is not reported.
4. Further internal inconsistencies I found, to add to those already recorded:
   - Methods give the HBO2 control n=14. The ANOVA df F(3,28) implies 8 per group, and the Fig 3B and 5A control scatter shows about 8 points.
   - The HBO2 control bars in Fig 3A and Fig 4A are identical. Yet the Fig 4B control scatter (about 28–54 min) differs from Fig 3B and 5A (about 30–41 min).
   - The text says memantine plus perampanel "did not differ" from perampanel alone, but no bracket in Fig 5A tests it. The medians are about 53 versus about 75 min.
   - The abstract says perampanel prevented CA1/CA3 cell death and that co-administration "completely mitigated" the acceleration. Results 3.6 says the combination "failed to provide a neuroprotective effect".
5. Also true: the combination fixed Mem 5 acceleration in latency (Fig 5A, 5B, p<0.001).
Proposed wording: "In adult male Wistar rats given i.p. drug before 6 ATA oxygen, memantine 5 and 25 mg/kg shortened latency to all four seizure stages (stage 4 about 26 and 25 min against about 37 min in controls; n=8 per group, Fig 3), and 1 mg/kg shortened stages 1 and 2 only. Perampanel 1 and 5 mg/kg delayed stage 3 and 4 onset, but seizures still occurred in 7 of 8 rats at 1 mg/kg (the only incidence reported). No in-study measure of NMDAR or AMPAR engagement; the paper reports internal inconsistencies in n and control data. Non-genetic acute model, not WWOX."

=====================================================================
DR-H02-008 (CPP-115, PMID 24321005, PMC4102583 page, full text)
=====================================================================
Class: CHECK PRESENT BUT NOT MATCHED, citation-only. The Discussion cites refs 16 and 18 for CPP-115's "high affinity" for GABA aminotransferase, and ref 16 for a cocaine and dopamine readout in adult rats. There is no in-study GABA-AT activity, GABA level, plasma or brain level, or histology of drug effect. Query: GABA level, GABA content, concentration, plasma, brain level, vacuol, white matter, myelin, histolog, inactivat in cpp.txt, 2026-11-26.
- In-study check: no, for target engagement.
- Other effect on other endpoints: yes. CPP-115 reduced behavioural spasms at PN6 at all doses (Fig 1). A single 1 mg/kg dose reduced electroclinical spasms for 1 h and on PN8 (Fig 2). This shows drug activity in the same pups, on a different endpoint.
Verdict: MUST CHANGE (first sentence), with ADD content.
Findings:
1. "CPP-115 only, not vigabatrin" is ambiguous and, in the natural reading, contradicted. Vigabatrin was not tested in this study. Table 1 and the Introduction cite the earlier study (ref 2): "Vigabatrin transiently reduced spasms only on PN5, but was associated with significant sedation and mortality". Table 1 gives vigabatrin 40 mg/kg/day, 100% mortality by PN11, spasm reduction on PN5. So "not vigabatrin" can be read as "vigabatrin did not reduce spasms", which is wrong. The accurate claim is that vigabatrin was not tested here.
2. Abstract statements are accurate, and the abstract does not mention histology:
   - "did not accelerate spasms cessation".
   - "did not alter neurodevelopmental outcomes or visuospatial learning".
3. The full text, which is held, does contain brain histology: thionin-stained hippocampal injury scores at PN20 (n=23: 8, 10 and 5 per group) and autopsy cortical scores (n=30). It is used to correlate model injury with Barnes-maze learning. It is not a white-matter or vacuolation assessment, and no vacuolation or myelin endpoint is reported.
4. The ADD content below is absent from the note. It matters for reading "no change" and "DECREASE":
   - The spasm reduction was transient: PN5–7, with no effect after PN7.
   - 5 mg/kg/day was lethal (9/9 by PN8; 8/9 by PN7). Neurodevelopmental tests used 0.1 and 1 mg/kg only, because the 5 mg/kg group was excluded.
   - Within-group Barnes learning improved in vehicle (P=0.0002) but not in CPP 0.1 or 1 (P=0.40 each). The authors conclude "no effect" only after adjusting for injury, with small groups.
Proposed wording: "Rat multiple-hit infantile-spasms model, CPP-115 0.1–1 mg/kg/day reduced spasms only transiently (PN5–7); 5 mg/kg/day was lethal by PN8. Vigabatrin itself was not tested here (earlier study: transient reduction on PN5 with sedation and mortality). The abstract states that spasm cessation was not accelerated and that neurodevelopmental outcomes and visuospatial learning were unaltered (0.1 and 1 mg/kg only, small n). The abstract does not mention histology; the full text scores model hippocampal and cortical injury but reports no myelin or vacuolation assessment. No GABA-AT engagement measured in the study."

=====================================================================
DR-H02-023 (vigabatrin human neuropathology, PMID 1940119 and 2767014, abstracts)
=====================================================================
Class: NOT ASSESSABLE (abstract). Neither abstract reports a drug level or target effect in the examined people. The 1940119 abstract mentions "extensive clinical, neurophysiologic, neurochemical ... testing", with no values and not tied to these patients.
- In-study check:
  - 1940119: no check. The 10 untreated age-matched cases are a comparison group, not an engagement check. The animal lesion is cited background.
  - 2767014: its abstract reports the animal arm of the same paper, with vacuolation in dosed animals. This is a different species, so not matched.
- Other effect: yes. 2767014 reports myelin vacuolation limited to myelinated tracts, "reversible upon discontinuation", in the animals.
Verdict: MUST CHANGE.
Findings:
1. Supported:
   - 62 patients with refractory epilepsy "on vigabatrin therapy either prior to undergoing neurosurgery ... or before death".
   - "In no case ... any evidence of myelin microvacuolation or myelin sheath splitting that could be attributed to vigabatrin".
   - "Demyelination has never been observed in either the animal or human material".
   - 2767014: "Two postmortem and three operative specimens from humans have revealed no evidence of vacuolation of myelin".
2. Unsupported clause: "a negative in people who were not infants". The note itself says ages are not stated, and the abstract text gives no ages. The only age information is the MeSH list of 1940119 (Child, Adolescent, Adult, Middle Aged, Aged; no Infant heading). That is indexing, not a statement about the 62 patients. "People who were not infants" therefore contradicts the note's own "ages not stated".
3. "The infant lesion the label records" cannot be verified from the listed files. UNSETTLED.
4. Omissions:
   - The 1940119 abstract includes 10 age-matched untreated cases, which are not mentioned.
   - The 2767014 abstract does not explicitly say the five specimens were from vigabatrin-treated patients (the garbled sentence is "or damage uolation ..."). It also does not say whether they overlap with the 62.
   - "Attributable" is a pathologist judgement ("considered"), not a quantified result.
   - Duration of exposure is not stated in the abstract (only the title says long-term).
Proposed wording: "Abstract level: in 62 epilepsy patients examined after vigabatrin (before neurosurgery or death), compared with 10 untreated age-matched cases, no myelin microvacuolation or sheath splitting was judged attributable to the drug and no demyelination was seen; an earlier abstract reports no myelin vacuolation in two post-mortem and three operative human specimens (drug exposure and overlap with the 62 not stated). Ages and exposure durations are not stated in the abstracts, so whether the finding extends to infants is not shown."

=====================================================================
DR-H02-024 (vigabatrin and GABA, rat cerebellar explants, PMID 2757909, abstract)
=====================================================================
Class: NOT ASSESSABLE (abstract). No GABA-T inhibition or GABA level is reported. The abstract does say the model is "very sensitive", but it reports no positive control for oedema detection.
- In-study check: no engagement or positive-control readout in the abstract.
- Other effect: yes. Mild toxicity for myelinated fibres from both agents (item 3), and "some degenerating myelinated fibres and astrocytic gliosis ... in both experimental conditions", involving axons and myelin sheaths (item 4).
Verdict: ADD (with wording-fidelity fixes).
Findings:
1. Doses are not equimolar. Vigabatrin was 500 nmol/ml and GABA 1000 nmol/ml, up to 14 days, in explants of 14–19 days in vitro. "GABA alone reproduced the mild toxicity" omits that GABA was at twice the concentration. The abstract calls these "high concentrations" and the paper "preliminary data".
2. "No clear difference between them" drops the abstract's hedge: "although vigabatrin seemed slightly more toxic than GABA at these doses".
3. The abstract says "no patent intramyelinic oedema". "No intramyelinic oedema" in the note slightly strengthens this.
4. The note omits the EM findings of degenerating fibres and gliosis in both conditions. The abstract also states "the toxicity ... was surprisingly mild in this very sensitive model".
Proposed wording: "Rat cerebellar explants (14–19 days in vitro) exposed up to 14 days to vigabatrin 500 nmol/ml or GABA 1000 nmol/ml: mild toxicity to myelinated fibres from both, no clear-cut difference although vigabatrin seemed slightly more toxic; EM showed no patent intramyelinic oedema or primary demyelination but some degenerating myelinated fibres and astrocytic gliosis in both. Preliminary data; not a vacuolation finding."

=====================================================================
DR-H02-036 (GABA-B and myelination, PMID 35980256 and 31349008, abstracts)
=====================================================================
Class:
- Main null (GABA-A agonist did not reproduce): NOT ASSESSABLE (abstract). The abstract reports no muscimol engagement or dose. It states only that "None of these effects are mediated by the GABAAR agonist muscimol". It also says that, "in contrast to GABAARs", GABAB1R and GABAB2R are expressed in OLs over time. That is an expression statement, not an engagement readout of muscimol.
- GABA-B arm in 31349008 (baclofen, purified rat OPC cultures): CHECK PRESENT. The effects are "reverted in presence of ... CGP55845", and the baclofen-induced maturation is attenuated by the Src-family inhibitor PP2.
- GABA-B arm in 35980256 (baclofen, LPC mouse spinal cord and cerebellar slices): NOT ASSESSABLE (abstract). No antagonist or engagement readout is reported.
- In-study check for the muscimol null: no.
- Other effect: yes. See the GABA-B effects above.
Verdict: MUST CHANGE.
Findings:
1. "A GABA-A agonist did not reproduce the effect in the coculture study" is not supported. The abstract places muscimol after the purified rat OPC culture results (branching, myelin protein expression, Src phosphorylation). The DRG-OPC coculture result is GABA only (more myelin segments and MBP). A context is assigned to the wrong experiment.
2. "The axis therefore has opposite signs by receptor class" is not supported. The abstracts report GABA-B agonism as positive and the GABA-A agonist as not mediating the effects (no effect). They do not report a GABA-A effect of opposite sign. This is an inference beyond the sources.
3. "GABA-B engagement enhanced ... remyelination": the remyelination result is baclofen alone in adult mice (LPC spinal cord injection). Its receptor specificity is not shown in the abstract. The antagonist reversal is in the culture study.
4. "Signalling studies, not drug exposures of a developing brain" is literally true, since the in vivo arm is adult mice. But 35980256 is an in vivo baclofen administration.
Proposed wording: "Baclofen (GABA-B agonist) enhanced OPC differentiation and myelin protein expression in purified rat OPC cultures (reversed by CGP55845; Src-dependent), and in adult mice after LPC demyelination enhanced OPC differentiation and remyelination (35980256, no antagonist control in the abstract). Exogenous GABA increased myelin segments and MBP in DRG-OPC cocultures. The GABA-A agonist muscimol did not mediate the culture effects (no muscimol activity check or dose in the abstract), so the two receptor classes differ (positive versus no effect), not shown to have opposite signs. Adult or culture signalling studies, not drug exposure of a developing brain."

=====================================================================
DR-H02-030 (vigabatrin MRI, PMID 19054414, Europe PMC abstract record)
=====================================================================
Class: NOT ASSESSABLE (abstract). There is no drug level or target-effect readout in the abstract.
- In-study check: yes, but only for assay sensitivity, not engagement. The same abstract and method show a significant exposed-versus-naive difference in infants with infantile spasms: 22% vs 4%, p<0.001, 205 infants aged 24 months or less. That is a different age group and indication, with the same drug and the same blinded MRI definition.
- Other effect: yes (the infant finding above). Also resolution in 6 of 9 subjects with a follow-up MRI.
Verdict: ADD.
Findings:
1. Supported: "no statistically significant difference in the incidence or prevalence of prespecified MRI abnormalities between vigabatrin-exposed and vigabatrin-naive subjects" among "adults and children treated with vigabatrin for CPS".
2. "(668 subjects)" is the number whose images were re-reviewed: "2,074 images from 668 children (aged 2-16 years) and adults (>16 years) with CPS". The abstract does not give how many were exposed or naive or entered each comparison. The test is stated for children and adults together, not band by band.
3. Missing context: these are complex partial seizure patients, a different indication from infantile spasms. The study is a retrospective re-review with blinded neuroradiologists. No dose or duration is given. The infant contrast is the actual comparison for the "age-band" point.
Proposed wording: "Retrospective re-review (blinded readers) of MRIs from 668 children aged 2 to 16 and adults with complex partial seizures: no statistically significant difference in incidence or prevalence of prespecified MRI abnormalities between vigabatrin-exposed and naive subjects (numbers per arm, dose and duration not in the abstract). In infants with infantile spasms in the same study the prevalence was higher with vigabatrin (22% vs 4%, p<0.001, 205 infants). A non-significant difference is not proof of no difference."

=====================================================================
Files actually opened
=====================================================================
- /home/desktop/.claude/jobs/7f7fcdaa/tmp/blind4/BLIND_SENTENCES_ADV282_INC5_SCI_20261126.md
- /home/desktop/legend-development/.claude/worktrees/sci_as_20261126/framework/protocols/delegation_budget.md (section 2 and section 7 only)
- /home/desktop/legend-development/files/fulltext/adv282_abstracts_sci_20261126/PMID42179084_efetch.xml, PMID1940119_efetch.xml, PMID2767014_efetch.xml, PMID2757909_efetch.xml, PMID31349008_efetch.xml, PMID35980256_efetch.xml
- /home/desktop/legend-development/files/fulltext/adv056_it_20261118/B/PMID19054414_x2009_europepmc_core.json
- /home/desktop/legend-development/files/fulltext/PMID42652189_Alekseeva2026_PMC.xml (text-extracted to alek.txt; read to the end of the Conclusions and the start of the reference list)
- /home/desktop/legend-development/files/figure_renders/p42652189/g002.png, g003.png, g004.png, g005.png (Figs 2 to 5; I did not open g001 or g006, nor figures/PMID42652189/ *.webp/*.gif, nor PMID42652189_mA/mB.png)
- /home/desktop/legend-development/files/fulltext/PMID24321005_ADV272_PMC4102583_pmcpage_20261125.html (text-extracted to cpp.txt, read to the end of the Discussion)
- I also listed the contents of the figures and figure_renders directories (no content opened beyond the files above).
- Not examined: the CPP-115 supplementary materials (Supplemental Results, Table 1 and Figures 1 to 3), which are not among the held files. The perampanel Fig 4B and Fig 5A individual data points could not be counted because no image library was available.
