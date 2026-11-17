# Ketamine — bounded literature census (HE, 2026-11-17)

Status: CENSUS, not evidence. Hypothesis-prompt material for the 13:46Z meeting. Not medical advice; no dose, no recommendation.
Method: PubMed tool only, one short query at a time, no bursts, no contact data. Every item below is **ABSTRACT-LEVEL**
(title + abstract through the PubMed metadata tool). **No item was read in full text.** Time-boxed (about 40 minutes); one metadata call was
refused by a rate limit, so four retrieved PMIDs are listed as UNREVIEWED.
Aggregates only: no per-patient detail from case reports is carried here (CLINICAL_CASE_LINKAGE gate).

## Queries run (what each returned)

| Q | Query (PubMed syntax, shortened) | Hits | Reviewed |
|---|---|---|---|
| Q1 | (ketamine OR esketamine) AND refractory status epilepticus AND (child OR pediatric) | 84 | 8 of top 15 |
| Q2 | ketamine AND (DEE OR epileptic encephalopathy OR neurodevelopmental disorder) AND (child OR infant) | 131 | 4 of 12 |
| Q3a | (transient OR temporary) improvement AND (fever OR anesthesia OR sedation OR intensive care) AND (neurodevelopmental / Rett / autism / epileptic encephalopathy) | 80 | 0 (too broad; titles not opened) |
| Q3b | fever effect autism behavioral improvement during fever | 20 | 3 of 8 (1 relevant) |
| Q4a | ketamine mechanism disinhibition interneuron BDNF mTOR plasticity anti-inflammatory (long form) | 0 | — |
| Q4b | ketamine rapid antidepressant mechanism NMDA receptor disinhibition synaptic plasticity review | 4 | 2 |
| Q4c | ketamine microglia inflammation | 30 | 2 of 6 (the first metadata call was rate-limited and was repeated) |
| Q5a | ketamine adverse effects children SR emergence neurotoxicity developing brain (long form) | 0 | — |
| Q5b | ketamine pediatric safety adverse events systematic review | 31 | 2 of 8 |
| Q5c | ketamine developmental neurotoxicity neonatal apoptosis | 9 | 2 of 6 |

## (1) Ketamine in children with refractory status epilepticus / severe neurodevelopmental disorders

| Item | Level | Design / population | Aggregate finding (as stated in abstract) |
|---|---|---|---|
| PMID 35817569, doi 10.1212/WNL.0000000000200889 | abstract | Retrospective single-centre cohort, 69 children and neonates, ICU, RSE | Seizure termination 46%, reduction 28%, no change 26%; adverse events needing intervention 4% (hypertension, delirium); Class IV evidence |
| PMID 38881333, doi 10.1111/epi.18035 | abstract | Systematic review / meta-analysis, 6 case series and cohorts, 172 patients | SE cessation 51% (95% CI 43-59) when ketamine was added; heterogeneity low; case reports excluded for reporting bias |
| PMID 42424871, doi 10.1016/j.seizure.2026.07.004 | abstract | Retrospective cohort, 77 children, ketamine + midazolam vs midazolam | Unadjusted success 73% vs 40%; adjusted OR 4.16 (0.99-17.44), not significant; no serious treatment-limiting adverse events |
| PMID 32822230, doi 10.1177/1535759720928269 | abstract | AES systematic review, third-line agents | Ketamine: insufficient evidence (level U; 25 class IV studies) |
| PMID 36609129, doi 10.1016/j.yebeh.2022.109066 | abstract | Rationale paper (animal data, add-on in benzodiazepine-refractory SE) | Ketamine terminates benzodiazepine-refractory SE in animal studies; proposes a trial; advocacy-level |
| PMID 32198865, doi 10.1007/s13312-020-1759-0 | abstract | Narrative review RSE / super-refractory SE | Ketamine named among the main anaesthetic infusions; no outcome beyond seizure control |

**Does not cover / gap:** Q2 returned no abstract that reports ketamine in a *defined* developmental and epileptic encephalopathy or in a defined genetic syndrome with developmental outcomes; the 4 abstracts opened were sedation reports in autism (PMID 42874046, 42003546), a paediatric review (PMID 42538882) and the cohort above. Reported **durations of benefit beyond the seizure endpoint** (days to weeks), and any **developmental or functional outcome after a single exposure**, were not found in what was opened. 131 Q2 hits and 84 Q1 hits are mostly unopened.

## (2) Transient improvement of previously lost capacities after ICU stay, intubation, anaesthesia, sedation or febrile illness

| Item | Level | Finding |
|---|---|---|
| PMID 37119025, doi 10.1002/aur.2935 | abstract | Simons Simplex Collection analysis: about 1 in 6 children with ASD reported with behavioural improvement during febrile episodes; association with maternal infection in pregnancy and GI dysfunction; authors propose pro-inflammatory cytokine involvement (consistent, they say, with mouse models). Parent-report, retrospective. |

**Does not cover / gap:** nothing was retrieved on transient improvement after **ICU stay, intubation, anaesthesia or sedation** in neurodevelopmental disorders (Q3a was too broad and its 12 first PMIDs were not opened; the conclusion "none" is therefore NOT supported, only "not found in this census"). The fever-effect literature beyond the one item above was not opened. Explanations given by authors in the one item: immune/cytokine signalling.

## (3) NMDAR-antagonist "indirect" effects relevant to plasticity, inhibitory interneurons, inflammation

| Item | Level | Species / system | Tier (what kind of claim) |
|---|---|---|---|
| PMID 32616214, doi 10.1016/bs.apha.2020.03.002 | abstract | Review of mouse and human work: NMDAR block on GABAergic interneurons -> disinhibition -> glutamate surge -> BDNF release -> transient mTOR activation -> synaptic protein synthesis; a drug-on phase of about 2 h, then days of structural maturation of new synapses and **enhanced GABAergic inhibition** (somatostatin interneurons, eEF2) | mechanistic model, mostly rodent; review |
| PMID 41923438, doi 10.1111/cts.70527 | abstract | Esketamine nasal-spray review (adult depression): NMDAR antagonism on interneurons disinhibits glutamate release, downstream plasticity pathways | review, human clinical + translational; industry authors |
| PMID 36371060, doi 10.1016/j.nbd.2022.105923 | abstract | Mouse, neonatal exposure (postnatal day 7): impaired mossy-fibre pruning and lasting increase of excitatory transmission in CA3 | in vivo mouse, harm-side plasticity effect |

| PMID 31514224, doi 10.1111/fcp.12508 | abstract | Mouse BV2 microglial cell line, LPS challenge: ketamine reduced cytokine and NF-kB readouts through NMDAR block, lower Ca2+ and CaMKII phosphorylation; reversed by an NMDAR co-agonist | in vitro, cell line; mechanism only |
| PMID 37793489, doi 10.1016/j.bbi.2023.09.026 | abstract | Mouse LPS depression-like model: (R)-ketamine linked to lower hippocampal CD38, less microglial activation and reversed synaptic defects; the CD38 manipulations carry the causal weight, not the drug | in vivo mouse; enantiomer-specific; one lab |

**Unreviewed (Q4c, ketamine and microglia / inflammation, 30 hits):** PMIDs 41254322, 41572340, 41082017, 41135741 — titles not opened. The inflammation arm of item 3 rests on two abstracts, both preclinical, both in an LPS challenge; nothing was retrieved on inflammation in a genetic neurodevelopmental model.
**Relevance to the reference genotype's mechanisms** (plasticity, interneuron function, inflammation) is a *mapping to be made at the meeting*; nothing here links ketamine to the reference genotype.

## (4) Adverse-effect profile in children (harms beside benefits; no balance implied)

| Item | Level | Aggregate finding |
|---|---|---|
| PMID 35817569 (above) | abstract | 4% of 69 had adverse events needing intervention: hypertension (2), delirium (1) |
| PMID 42218597, doi 10.1111/pcn.70091 | abstract | Systematic review, 18 placebo-controlled trials of **oral** (es)ketamine incl. paediatric premedication (n=239): transient neurological effects; dizziness, sedation, dissociative symptoms more frequent than control; serious events rare; **certainty low, long-term safety uncertain** |
| PMID 42003546, doi 10.1111/scd.70171 | abstract | 28 children with ASD, 37 sedation appointments with a combination IM protocol: 14% adverse events; confounded by co-administered agents |
| PMID 36371060 (above), PMID 31852437 (doi 10.1186/s12868-019-0542-4) | abstract | Neonatal rodent exposure: altered circuit pruning / impaired integration of developmentally generated granule neurons and spatial-memory deficit later. Rodent, early postnatal window; human extrapolation unestablished |
| PMID 42538882, doi 10.1176/appi.focus.20250040 | abstract | Paediatric review incl. adverse effects, contraindications, route-dependent bioavailability (not read beyond the abstract) |

**Does not cover:** emergence reactions, raised intracranial pressure, hepatobiliary / urinary toxicity under repeated exposure, abuse liability, and anaesthetic-neurotoxicity human cohort data were not searched in a way that returned abstracts (Q5a returned 0 because of over-specific AND terms). Treat the list as incomplete, not as a harm profile.

## Recall leads NOT retrieved in this census (from memory; unverified; for follow-up queries only)

NMDAR block -> eEF2 kinase / BDNF translation in mouse hippocampus; hydroxynorketamine as an NMDAR-independent metabolite route; reported mouse work on ketamine in Mecp2-deficient models; the original parental-report fever-effect papers in ASD and the locus-coeruleus / noradrenergic hypothesis. None of these is a claim here.

## Radar and scout (one line)

The HARNESS-SCOUT-2026-W47 table has no ketamine entry; ketamine appears only in the existing F04 NMDAR intervention-class card (pore blockers memantine and ketamine, GluN2A-containing receptors) and in the IT18 radar rating sheet.

## What would close the gaps (cheap, one query each, if the meeting wants them)

1. Open Q2 hits by title (131) and filter for named genetic DEE syndromes. 2. Open Q4c abstracts. 3. A narrow query for improvement after general anaesthesia/sedation in genetic NDDs. 4. A narrow paediatric ICU ketamine-harm query. Estimated 30-45 minutes.

---

## Update 2026-11-17, gap closure (13:00-13:20Z; added to the section above, nothing above was changed)

All items are **abstract-level**; no full text was read. Same rules: aggregates only, no per-patient detail. Each query was run one at a time with pauses; two attempts were refused by a rate limit and repeated.

### Queries added

| Q | Query (shortened) | Hits | Opened |
|---|---|---|---|
| G1 | improvement after general anaesthesia in Rett OR Angelman OR genetic epilepsy | not run (rate limit, twice) | — |
| G2 | Rett syndrome anesthesia improvement after sedation | 0 | — |
| G3 | transient improvement after anesthesia neurodevelopmental disorder children | 2 | 2 |
| G4 | regression recovery of skills after critical illness OR intensive care in children with genetic neurodevelopmental disorder | 614 (OR-parse too broad) | 0 |
| H1 | ketamine emergence reactions children | 83 | 2 of 6 |
| H2 | ketamine intracranial pressure children | 48 | 2 of 6 |
| H3 | anesthetic exposure early childhood neurodevelopmental outcome cohort | 19 | 2 of 6 |
| H4 | repeated ketamine exposure children adverse effects | 7 | 2 of 6 |
| Q2b | ketamine AND (Dravet OR CDKL5 OR GRIN2A OR GRIN2B OR SCN2A OR infantile spasms OR Rett OR Angelman) | 118 | 4 of 10 |

An earlier unparenthesised version of Q2b parsed as 939 hits (the drug term bound only to the first syndrome) and was discarded.

### (a) Transient improvement after ICU stay, intubation, anaesthesia or sedation in neurodevelopmental or genetic disorders

**Result: NOT FOUND in what was opened.** The two abstracts opened (G3) were not relevant to the question: a single-patient dental-rehabilitation report with parent-reported short-term comfort, sleep and weight change, and a 1993 premedication trial in cardiac surgery. G2 returned nothing. G4 was too broad to open anything.
**Does not cover:** any of the 614 G4 hits; the terminology a case report might use (awakening, regained, paradoxical, lucid interval, "after extubation"); non-English or grey literature; reports that do not say "anaesthesia" in the abstract. The absence is a statement about these queries, not about the literature.

### (b) Paediatric harms

| Item | Level | Aggregate finding | Limit |
|---|---|---|---|
| PMID 38065480, doi 10.1016/j.jad.2023.12.011 | abstract | RCT, 84 preschool children, intranasal dexmedetomidine with or without esketamine before dental general anaesthesia: lower emergence agitation and lower anxiety with the combination; adverse reactions similar between arms | short follow-up; combination, not ketamine alone |
| PMID 33555694, doi 10.1097/AJP.0000000000000918 | abstract | Review of intranasal ketamine for acute pain: more transient dizziness, bitter taste, fatigue, vomiting than opioids; evidence insufficient | adult and paediatric mixed |
| PMID 36825892, doi 10.1097/CCM.0000000000005806 | abstract | 33 children with severe traumatic brain injury, 127 bolus doses in 22: no ICP rise after sedation doses; ICP fell and cerebral perfusion pressure rose during ICP crises | retrospective, exploratory, one centre; not a neurodevelopmental population |
| PMID 27028535, doi 10.1007/s40262-016-0383-6 | abstract | Pharmacology review: no evidence of raised ICP after ketamine in humans; psychotomimetic and cognitive adverse effects; long-term safety unresolved | review |
| PMID 30883414, doi 10.1213/ANE.0000000000004052 | abstract | Methods review of 76 human studies of general anaesthesia in early childhood: findings contradictory; major confounding by surgery and indication, small samples, short follow-up | general anaesthetics, **not ketamine-specific** |
| PMID 24275940, doi 10.1097/ANA.0000000000000027 | abstract | Review: dual effects; repeated ketamine in immature brain may be neurotoxic without noxious stimuli and possibly neuroprotective (less inflammation) with strong pain stimuli; therapeutic window undefined | preclinical and clinical mix, 2014 |
| PMID 36892030, doi 10.2174/1567205020666230308123718 | abstract | Juvenile rats, 3 days of repeated dosing: highest dose gave later anxiety-like behaviour and spatial-navigation deficit; lower doses little | 32 animals, one lab, rodent |

**Does not cover:** a human cohort with long-term developmental outcome after ketamine specifically (none surfaced); repeated-exposure human series; hepatobiliary and urinary toxicity; abuse liability; interaction with antiseizure medicines. Unopened hits: H1 40801799, 27534393, 41256828, 22157929; H2 24996763, 25245275, 10228376, 19569909; H3 42443755, 21148656, 37283466, 37552011; H4 24659739, 42232094, 40246008, 40024338.

### (c) Q2 follow-up (ketamine in defined genetic syndromes)

The opened abstracts were mechanistic, not clinical: PMID 29532791 (doi 10.1038/mp.2017.255; review, rodent-heavy: NMDAR block at synaptic and GluN2B extrasynaptic receptors and on interneurons, AMPAR activation, BDNF, eEF2, mTOR, GSK-3, and NMDAR-independent routes through (R)-ketamine and hydroxynorketamine; the authors say the mechanisms are not mutually exclusive); PMID 34321660 (doi 10.1038/s41586-021-03769-9; human GluN1-GluN2A and GluN1-GluN2B cryo-EM with S-ketamine; binding site in the channel vestibule, key residues named; structural only); PMID 36630309 (doi 10.1021/acschemneuro.2c00637; mouse brain-wide c-Fos after subanaesthetic ketamine and psilocybin: elevation in many regions including locus coeruleus, habenula, amygdala; a map, not a mechanism); PMID 39215550 (doi 10.33594/000000722; human neuroblastoma cell line, excitotoxicity model, only the non-selective blocker protected). **No clinical report of ketamine in a named DEE or genetic syndrome surfaced among the 14 abstracts opened across Q2 and Q2b.** Unopened Q2b: 27683935, 21424308, 40612906, 41465113, 36051601, 36093918 (and about 108 further hits beyond the first 10).

### Q4c, the four abstracts still unopened

PMIDs 41254322, 41572340, 41082017, 41135741 were **not opened** in this update (time-box); the inflammation arm still rests on the two preclinical abstracts above.

### Net effect of this update on the census

(a) remains empty; (b) now has a paediatric ICP signal (TBI cohort, no rise), an emergence-agitation signal in a combination RCT, and the early-life anaesthetic-neurotoxicity literature (general anaesthetics, contradictory in humans, positive in rodents); (c) adds mechanism and structure but no clinical syndrome report. Estimated further cost to open everything unopened: about 40 minutes.
