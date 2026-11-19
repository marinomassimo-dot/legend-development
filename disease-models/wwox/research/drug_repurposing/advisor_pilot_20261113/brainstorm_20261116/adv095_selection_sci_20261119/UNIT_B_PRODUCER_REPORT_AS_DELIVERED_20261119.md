# ADV-095 unit B: producer report as delivered (legend-delegate, sonnet, effort medium, one round, no sub-delegation; delivered 2026-11-19; persisted verbatim by SCI from the subagent transcript, which is the only place it lived; the brief is `UNIT_B_EXPOSURE_TABLE_PRODUCER_BRIEF_SCI_20261119.md`). Producer output, NOT yet verified by SCI or a second reader: every number below is a producer claim until the verifier pass; abstract-level rows are marked AB by the producer.

ADV-095 UNIT B PRODUCER REPORT (SCI 2026-11-19). Hypothesis level only. No dose, no schedule, no recommendation for or against any use of any agent in any person. Research concentrations in model systems only. Reference genotype class only. Not medical advice.

SCOPE REACHED: PARTIAL. One round at effort medium, no sub-delegation, no repository file edited.
- Done: the Wwox-null regimen (quoted from the held Cheng 2020 full text), a set of verified abstract-level potency rows for ethosuximide, the Kv7 openers and XE991, and the tonic-inhibition agents, with the ganaxolone and ethosuximide label text.
- Done: lithium targets (GSK-3), vigabatrin and one mouse exposure paper for retigabine.
- Not done, or done only partly: most mouse brain or unbound exposures, juvenile exposure for every agent, protein binding, the IMPase constant, the ketogenic-diet ketone values, the d-APV in-vivo question, and the NMDAR mouse-exposure rows. See "Not reached" below.
- Quotes: every quote was checked as a substring of bytes I fetched. Abstracts came from the Europe PMC core record by PMID. Cheng 2020 is the held full text. The Bettio table is the PMC12346480 full text (Europe PMC XML, open access). The labels are openFDA JSON. Whitespace and HTML tags were normalised only.
- Level tags: AB = abstract only, FT = full text read in the passage, LAB = label text. Everything below is AB unless marked.
- Routes: Europe PMC REST search and core record, Europe PMC fullTextXML (Bettio), openFDA label API, held files/fulltext (Cheng 2020), the ADV-050/054/046/067 folders. No e-mail or personal detail was sent to any service. No browser-header spoofing. No challenge page was met.
- Receipts ledger: I did not run fulltext_receipts.py.

HELD FINDINGS (cited, not redone)
- Ethosuximide Wwox-null regimen. Source: PMID 32000863 (Cheng 2020), FT, from files/fulltext/PMID32000863_Cheng2020_PMC_r2.xml.
  - Quote 1: "Ethosuximide (i.p., 150 mg/kg), a T-type Ca 2+ channel blocker that has anticonvulsant activity (Luszczki et al., 2005), was injected into mice 45 min before PTZ-induced clonic seizures."
  - Quote 2 (Fig. 7 legend): "Higher seizure activity was observed in Wwox −/− mice after injection of PTZ (30 mg/kg)... Pretreatment of ethosuximide (ETS, 150 mg/kg) suppressed PTZ-induced seizure activity in Wwox −/− mice."
  - Lithium arm, same paper: "LiCl (i.p., 60 mg/kg) were pretreated three times within 1 h before PTZ injection."
  - Cheng reports no drug level, matrix or time-resolved exposure in the passages I searched (regex on "mg|kg|i.p"; the Methods and the Fig. 7 legend).
  - The animals are described as pre-weaning. P20 is stated for the GSK3β Ser9 blot. The ages used for the drug tests are not stated.
  - The ADV-046 review (Part A) reports group sizes (-/- 6 against 6 for ethosuximide) and that no genotype x treatment test is possible.
- NMDAR kinetics (ADV-050, in the held kinetics table). Memantine IC50: 0.5 to 0.8 µM at 0 Mg2+, -66 mV (PMC2679254, FT), and 1.6 to 13.4 µM at 1 mM Mg2+ (2A 13.4, 2B 10.4, 2C 1.61, 2D 1.76). Ketamine: 0.31 to 0.83 µM at 0 Mg2+ and 1.18 to 5.35 µM at 1 mM Mg2+. Memantine is partially trapped (about 5/6 in Blanpied 1997, 71% in Mealing 1999) and ketamine more fully (86%). For d-APV the held table has only DL-AP5 at 100 µM, blocking about 39% of GluN1/2A and about 18% of GluN1/2D (PMC10245146). All other d-APV kinetics are "not found" there. I did not redo any of this.
- Lithium regimen (ADV-067): brain or serum lithium at the time of PTZ is not reported in any regimen paper except the chronic arm of 29102713 (serum level mentioned, figure omitted). Hanak 2015 (25354763): "Brain lithium distribution was rapid (as early as 15 min), inhomogeneous and with delayed elimination (over 78 h)", from a poisoning model. Singh 1981 (7324073): lithium is "initially... high in blood and negligible in the brain".

TABLE 1 · ETHOSUXIMIDE
| Field | Content |
|---|---|
| Target or action | Human T-type Cav3.x, recombinant |
| Preparation | Cloned human α1G, α1H, α1I stably expressed in mammalian cells. Holding potential, temperature and charge carrier are not in the abstract. |
| Potency | Persistent T-current: IC50 = 0.6 mM, a block value. Succinimide analogue MPS (the methsuximide active metabolite), inactivated-state K(I): 0.3 to 0.5 mM for α1G and α1I, 0.6 to 1.2 mM for α1H. |
| Source and level | PMID 11641441 (Gomora 2001, doi 10.1124/mol.60.5.1121), AB. Quote: "T-type channels display current at the end of long pulses (persistent current), and this current was especially sensitive to block (ethosuximide IC(50) = 0.6 mM)". |
| Exposure in mouse | None found. |
| Competing actions | GIRK block (next row). |
| Relation supported | Threshold or state-dependent occupancy only if the inactivated-state K(I) is read as ethosuximide's. That is an assumption, because the MPS figure is not ethosuximide's. Tonic block is state-dependent: "block human T-type channels in a state-dependent manner, with higher affinity for inactivated channels" (same abstract). |

| Field | Content |
|---|---|
| Target or action | GIRK (Kir3), Xenopus oocytes |
| Preparation | GIRK expressed in oocytes with or without Gβγ. |
| Potency | Numeric potency not in the abstract (not read in full text). |
| Source and level | PMID 39814556 (Shalomov 2025), AB. Quote: "ETX is a subunit-selective, allosteric blocker of GIRKs". |
| Exposure in mouse | None found. |
| Relation supported | None until the IC50 is read. "The potency of ETX block is increased by Gβγ" (same abstract) makes occupancy state-dependent. |

Native thalamic neurons, persistent sodium, Ca-activated K and Na/K-ATPase: no potency retrieved. Searches were Europe PMC for "ethosuximide persistent sodium thalamic", "ethosuximide Na+/K+-ATPase" and the Leresche author query. Primary papers were not surfaced; only reviews and a rat-GAERS microinfusion paper (14667436) came up.

Mouse or juvenile exposure, protein binding: not found by two routes. These were Europe PMC searches on brain and serum levels, pup or neonatal pharmacokinetics, microdialysis, and protein binding. The openFDA label (Zarontin) gave pediatric use only: "Safety and effectiveness in pediatric patients below the age of 3 years have not been established" (LAB). Its clinical-pharmacology text has no binding value. Juvenile cells are empty.

TABLE 2 · KV7 OPENERS AND XE991
| Agent | Preparation | Potency | Source and level | Mouse exposure | Competing actions | Relation supported |
|---|---|---|---|---|---|---|
| Retigabine, KCNQ2/3 | Human KCNQ2/3 in Xenopus oocytes, 10 µM | About 20 mV left shift of activation. Oocyte hyperpolarisation "(IC(50) = 5.2 microM)" (this is a concentration for a resting-potential effect, not a channel EC50) | PMID 10908292 (Main 2000, doi 10.1124/mol.58.2.253), AB. Quote: "shifted both the activation threshold and voltage for half-activation by approximately 20 mV in the hyperpolarizing direction". | See Bettio row below. | See GABA-A row below. | Voltage shift, not occupancy. The effect grows with the Kv7.2-containing fraction. |
| Retigabine, family order | KCNQ1–4 in CHO cells; native M current in rat sympathetic neurons | Rank order only in the abstract | PMID 11466425 (Tatulian 2001, doi 10.1523/jneurosci.21-15-05535.2001), AB. Quote: "KCNQ3 > KCNQ2/3 > KCNQ2 > KCNQ4". KCNQ1 was not enhanced. | None | None | Subunit selectivity: Kv7.4 is the weakest. EC50 numbers not read. |
| ICA-069673, Kv7.4 and Kv7.5 | Human Kv7.4, Kv7.5 and Kv7.4/7.5 in A7r5 smooth-muscle cells | Not numeric in the abstract. | PMID 24944189 (Brueggemann 2014), AB. Quote: "ICA-069673 robustly activated Kv7.4 channels but was significantly less effective on homomeric Kv7.5 channels". | None | None | Subunit selectivity. Kv7.2/7.3 EC50 for ICA-069673 and ICA-27243: not retrieved. |
| XE991 | Kv7.2 and Kv7.2/3 in CHO cells | State-dependent: "Neither inhibitor was efficacious around the resting membrane potential of cells in physiologic conditions" | PMID 28483800 (Greene 2017, doi 10.1124/jpet.117.241679), AB | None | None | Block efficacy is not fixed by concentration. It depends on voltage and activation state (shift of half-activation voltage proportionally coincides with shift in half-effective potential for XE991 inhibition). Occupancy alone fails. |
| XE991, KCNQ1 comparison | KCNQ1 alone (not KCNQ2/3) | KD = 0.78 ± 0.05 µM (KCNQ1) and 11.1 ± 1.8 µM (KCNQ1+minK) | PMID 10825393 (Wang 2000), AB | None | None | Do not read as the Kv7.2/3 potency. |
| Retigabine, brain exposure | Adult mouse maximal-electroshock (MES) model, oral dose | EC50 plasma 2.26 µM, brain 3.58 µM, B/P 1.58 (mouse). Rat: 1.46 µM, 3.01 µM, B/P 2.06. | PMID 40806162 (Bettio 2025, PMC12346480, doi 10.3390/ijms26157029), FT (table). Table row: "RTG Kv 7 potassium channel potentiator Mouse 42.9 2.26 3.58 1.58 Rat 13.9 1.46 3.01 2.06" (columns ED50 mg/kg, EC50 plasma µM, EC50 brain µM, B/P). Route and time (Table 2): retigabine given PO, 0.5 h pre-treatment, mouse and rat. | Mouse age: not stated in what I read. Total, not unbound. The mouse ED50 (42.9) lies above the tested range of 5 to 35 mg/kg (text: "RTG did not produce a statistically significant anticonvulsant effect in mice at the doses tested (5–35 mg/kg)"), so the mouse EC50 is an extrapolation. | GABA-A (below). | Threshold or exposure-response in adult MES. The mouse EC50 is an extrapolation beyond the tested range. |
| Retigabine, GABA-A | Hippocampal neurons; recombinant α/β/δ and α/β/γ in tsA201 cells | 10 µM enhances δ-containing receptors. Seizure-like activity: "half maximal inhibition at 1 μm". The α1β2δ enhancement "became significant at 1 μm" | PMID 25779225 (Treven 2015, doi 10.1111/epi.12950), AB. Quote: "10 μm retigabine enhanced currents through α1β2δ, α4β2δ, α4β3δ, and α6β2δ receptors, but left currents through α1β2γ2S, α4β3γ2S, α5β3γ2S, and α6β2γ2S receptors unaltered" | None | Kv7 and GABA-A actions overlap at 1 to 10 µM | GABA-A action is at concentrations comparable to the Kv7 action. In slices the inhibition "was lost" when Kv7 and GABA-A were blocked together. The relation is not separable by concentration. |
| Kv7 in immature tissue | Rat hippocampal slices P8-P15, Mg-free seizure model | Not a potency | PMID 17651418 (Qiu 2007), AB. Quote: "augmentation of I(M) is effective in stopping ictal events in immature brain" | None | None | Slice-level sign in immature tissue. Not an in-vivo exposure. |
| Harm information | Clinical, not research | n/a | PMID 39853501 (Perucca 2025, doi 10.1007/s40263-024-01155-3), AB. Quote: "was withdrawn from the market in 2017 due to declining use after discovery of its association with pigmentation changes in the retina, skin, and mucosae". Rosendahl 2026 (42396991) adds that flupirtine was withdrawn in 2018. | None | n/a | Harm information only. The ages at which the changes were seen: not retrieved. The openFDA retigabine and Potiga label returned NOT_FOUND (withdrawn), so no label text. |

Not reached for Table 2: flupirtine potency, retigabine EC50 at Kv7.4/7.5, ICA-069673 EC50 at Kv7.2/7.3, ICA-069673 or ICA-27243 mouse brain exposure, juvenile or neonatal retigabine exposure, the label age at which pigmentation was seen.

TABLE 3 · TONIC-INHIBITION ENHANCERS
| Agent | Preparation | Potency | Source and level | Mouse exposure | Competing actions | Relation supported |
|---|---|---|---|---|---|---|
| Gaboxadol (THIP), δ-subunit | Mouse thalamic VB neurons, whole-cell, -60 mV; WT, δ-null and α1-null | 1 µM THIP current: WT -309 ± 23 pA, δ(0/0) -18 ± 3 pA, α1(0/0) -377 ± 45 pA | PMID 19302153 (Herd 2009), AB. Quote: "THIP (1 mum)-induced inward current in these neurones (WT, -309 +/- 23 pA; delta(0/0), -18 +/- 3 pA; alpha(1) (0/0), -377 +/- 45 pA)" | None found | "THIP did not affect the properties of miniature inhibitory post-synaptic currents" (same abstract) | δ-dependent tonic current. Adult-type preparation, since no age is in the abstract. |
| Gaboxadol, neonatal in vivo | Neonatal C57BL/6J mice P6–9 | Not a potency | PMID 40956609 (Liddiard 2025, doi 10.1172/jci.insight.196152), AB. Quote: "neonatal C57BL/6J mice (P6-9, both sexes)". Also "Blocking α5-GABAARs with L-655,708 did not affect acute neonatal SLE, whereas enhancing δ-GABAARs with THDOC, a neurosteroid, reduced them". | THIP dose and brain level not read. | None | Developmental sign: in this neonatal slice model enhancing δ tonic inhibition reduced seizure-like events. The abstract also states benefit in a kainic-acid in-vivo behavioural model. This is directly relevant to the chloride-gradient question for P6 to P9 mice. The chloride gradient itself is not quantified in the abstract. Contrast with the held ADV-065 chloride work. |
| Allopregnanolone | Murine dentate granule cells, tonic currents | Rank only | PMID 26857959 (Carver and Reddy 2016), AB. Quote: "Allopregnanolone and related pregnane analogs exhibited the highest potency and maximal efficacy in promoting tonic currents" | None | None | Potency rank by structure. EC50 not in the abstract. |
| Ganaxolone, label | n/a | n/a | LAB (openFDA, Ztalmy). Quote: "ZTALMY is indicated for the treatment of seizures associated with cyclin-dependent kinase-like 5 (CDKL5) deficiency disorder (CDD) in patients 2 years of age and older." Also: "Safety and effectiveness of ZTALMY in pediatric patients below 2 years of age have not been established." | None | Juvenile rat oral data: deaths with sedation at the mid and high doses, delayed sexual maturation, decreased brain weight. I did not quote the dose list. | Label age status verified from text. Not a mouse exposure. |
| Ganaxolone, neonatal review | Review | None | PMID 28878622 (Yawno 2017), AB, review. | None | None | R-tier only. |

Not reached for Table 3: δ against γ potency (EC50) for ganaxolone and allopregnanolone as numbers, mouse brain exposure for ganaxolone, allopregnanolone and gaboxadol, any age-resolved tonic-current-against-seizure series from P7 to P21 beyond Liddiard (P6–9). Searches are listed under "Not reached".

TABLE 4 · NMDAR CLASS, EXPOSURE SIDE
All rows: not found by the routes tried (Europe PMC searches below). The "distinguishing" pharmacology is in the held ADV-050 table (above). It was not redone. Radiprodil: PMID 40994429 (Banke 2026), AB, gives structure and the mechanism of GluN2B inhibition and no brain concentration. Held exposure numbers: none.

TABLE 5 · LITHIUM, EXPOSURE SIDE
| Agent | Preparation | Potency | Source and level | Mouse exposure | Competing actions | Relation supported |
|---|---|---|---|---|---|---|
| Lithium, GSK-3β | In vitro kinase, Xenopus/Dictyostelium | Ki = 2 mM (GSK-3β) | PMID 8710892 (Klein and Melton 1996), AB. Quote: "Lithium potently inhibits GSK-3 beta activity (Ki = 2 mM)". | See held rows (Hanak 2015, Singh 1981). | IMPase (not retrieved). | Competitive with Mg2+. Ryves and Harwood 2001 (11162580), AB: "Li(+) is a competitive inhibitor of GSK-3 with respect to magnesium (Mg(2+)), but not to substrate or ATP". The same abstract says the apparent potency depends on Mg2+ and in vivo effect may exceed the in-vitro one. Occupancy with an Mg2+ assumption. |
| Lithium, in vivo Ser9 | Cheng 2020, Wwox-null brain | Not a potency | FT. Quote: "Increased activation of GSK3β was determined in the cerebellum, hippocampus and cerebral cortex of Wwox −/− mice at postnatal day 20". | None | None | Ser9 phosphorylation in treated brain was not found. No brain lithium concentration paired with a Ser9 readout was found. |

Not reached: the IMPase inhibition constant, brain lithium at the Cheng regimen, in-vivo Ser9 phosphorylation after lithium in mouse brain.

TABLE 6 · VIGABATRIN AND THE KETOGENIC DIET (NO OCCUPANCY MAPPING APPLIES)
| Agent | Preparation | Marker | Source and level | Relation supported |
|---|---|---|---|---|
| Vigabatrin | Adult mice, osmotic-minipump infusion 35–140 mg/kg/d for 12 days | Mechanism: irreversible GABA-transaminase (GABA-AT) inhibition. Tissue GABA rose across tissues. AADA rose. | PMID 30822440 (Walters 2019), AB. Quote: "continuous VGB infusion (subcutaneously implanted osmotic minipumps), dose-escalation paradigm (35-140 mg/kg/d, 12 days)" | Turnover: effect is set by new-enzyme synthesis, not by concentration. No C/(C+IC50) mapping. |
| Vigabatrin, PTZ threshold | Mice, 3 or 7 days | Brain GABA rose at 3 and 7 days | PMID 32048251 (Świąder 2020), AB. Quote: "VGB after 3 days or 7 days of administration increased brain GABA concentration" | Time-lagged turnover. Brain GABA against time on a single dose is not stated. |
| Vigabatrin, neonatal | Mouse neonate, regional sensitivity | Title: "A sensitive period of mice inhibitory system to neonatal GABA enhancement by vigabatrin is brain region dependent" | PMID 20043003 (Levav-Rabkin 2010), title only | Not read. |
| Ketogenic diet | none | Ketone-body concentrations in mouse or rat pups on the diet: **not found by two routes** (Europe PMC suckling-rat and mouse queries). Only reviews and metabolic papers returned. | n/a | No occupancy mapping. |

CONFLICTS AND DISAGREEMENTS
1. Ethosuximide potency: Gomora (cloned human) reports a persistent-current IC50 of 0.6 mM and a state-dependent block. The abstract itself says recent rat and cat neuron studies "have failed to confirm inhibition of T-type currents at therapeutically relevant concentrations". Recombinant and native potencies disagree in source.
2. Retigabine: Main 2000 reports a KCNQ2/3 channel effect at 10 µM. Treven 2015 reports GABA-A δ enhancement at 10 µM and half-maximal seizure-like inhibition at 1 µM, so concentrations overlap.
3. Cheng 2020: the text claims the ethosuximide effect only in the knockout. The ADV-046 review says no genotype x treatment test is possible.
4. Lithium: Klein and Melton Ki = 2 mM is in vitro. Ryves and Harwood say in-vivo potency may be higher because of Mg2+ chelation by ATP. The two sources give different relations.
5. Retigabine mouse and rat: Bettio gives mouse brain EC50 3.58 µM against rat 3.01 µM. The mouse figure lies outside the tested dose range.

WHERE THE DATA ARE THINNEST
1. Juvenile free exposure: no juvenile mouse concentration (total or unbound) was found for any agent. All juvenile cells are empty.
2. Ethosuximide: native thalamic potency and competing-target potencies (persistent sodium, Ca-activated K, Na/K-ATPase) were not reached. GIRK potency was not read. No mouse brain level or protein binding.
3. NMDAR exposure and d-APV in vivo: no brain concentration for memantine, ketamine or radiprodil; the d-APV blood-brain-barrier question is unanswered.
4. Lithium: no brain lithium concentration at the Cheng regimen and no paired Ser9 readout.
5. Ketogenic diet: no ketone concentrations in pups; the ganaxolone, allopregnanolone and gaboxadol mouse exposures are also missing.

NOT REACHED (routes tried)
- Europe PMC lite searches (title-field and abstract-field) on each item, with at most five hits read per query: ethosuximide persistent sodium, Na/K-ATPase, brain and serum levels, pup pharmacokinetics, protein binding; retigabine pharmacokinetics; memantine and ketamine mouse brain concentration; radiprodil brain concentration; d-APV and DL-AP5 blood-brain barrier; allopregnanolone and ganaxolone brain levels; gaboxadol brain levels; lithium Ser9 in mouse brain; ketogenic-diet ketone levels in pups.
- Second route used for labels: openFDA (ganaxolone and ethosuximide returned; retigabine and Potiga NOT_FOUND).
- No full text was opened except Cheng 2020 (held), Bettio 2025 (Europe PMC XML, OA) and the held ADV tables. I did not check files/supplement or run fulltext_receipts.py. The absence claims above are therefore "not retrieved by the stated routes", not "absent from the literature".
- Not verified: Kv7.2/7.3 EC50 numbers for retigabine and ICA-069673 beyond the abstracts above.

Files written (all outside the repository): scratch abstracts and scripts in /tmp/u095b_data and /tmp/u095b_scripts. No repository file was edited.