# P2 (lane B3): paediatric ketamine in refractory and super-refractory status epilepticus (K7)
Producer report, 2026-11-17. Non-canonical. Not medical advice; no dose or recommendation (regimen figures are descriptors of what each study did). Reference genotype class only. Labels: DATO / INFERENZA / IPOTESI / TRANSFER.
Files: `SOURCES.tsv`, `SEARCHES.tsv`, `KETAMINE_PAEDIATRIC_SERIES.tsv`, bytes in `sources/`.

## 0. Answers first
* **K7 verdict: PARTLY SUPPORTED, with one arithmetic error, one unsupported inference and one misframed regimen claim.** Route: complete full text of DeVine (PMC page), abstracts (Europe PMC records) of Kuki and Rosati, full text of 5 reviews, full text of the largest paediatric cohort (Jacobwitz 2022, text but not tables).
  1. **Pooled 24/30 is not reproducible as "responders".** 24 = 15 (Kuki, >50% seizure reduction, n=18) + 6 (Rosati, resolution of RSE, n=9) + 3 (DeVine, n=3). DeVine's 3 are all 3 infants counted as responders; the paper reports resolution in 2 of 3 (patient 3 had no EEG resolution, ketamine ran "until time of death"). Corrected on the input's own logic: 23/30 = 76.7% (Wilson 59.1-88.2). The input's 80.0% (62.7-90.5) is reproduced exactly only with the DeVine error. Endpoints are three different things (>50% reduction; resolution of RSE; resolution of EEG seizures in 3 infants with non-genetic aetiologies). DATO from DeVine Table, Figure legend, Discussion.
  2. **"Non-inflammatory genetic etiologies such as WOREE fall in the better stratum" is not a finding of Kuki 2024.** Kuki's abstract names only inflammatory (n=10: meningitis 2, encephalitis 3, FIRES 5) vs non-inflammatory (8 by subtraction, composition not stated in the abstract I could reach). No gene, no genetic DEE group is mentioned. Full text blocked. The statement is an INFERENZA by the input (non-inflammatory -> genetic -> WOREE) with no data behind the middle step; the best that follows is "WOREE is not inflammatory, so it is not in the stratum that did worse", and even that rests on 8 unclassified patients.
  3. **"The regimen with efficacy data is a median 7.5-day infusion" is misframed.** 7.5 d (IQR 2.8-15.5) is Kuki's median treatment duration (n=18), the longest in the paediatric series I could read. The largest paediatric cohort (Jacobwitz 2022, n=69) reports a median total infusion of 85.7 h (IQR 49.7-128.0), best response at 0-6 h in 73% of improvers; DeVine average 5 d; Ilvento 22 h to 17 d range; Rosati (secondary only) 6 d. Kuki's inflammatory group needed longer treatment (p=0.0453) and responded worse: duration is confounded with aetiology and severity there (INFERENZA).
  4. **Prior magnitude:** the better-powered paediatric sources give lower and heterogeneous figures: seizure termination 46% (32/69; Jacobwitz 2022), 61% (23/38; first-line, Jacobwitz 2024), 14/19 episodes (Ilvento), pooled paediatric 50% (41-59) and 51% (43-59) in two secondary meta-analyses (not independent, endpoint = "study-defined cessation"). "80%" is a ceiling from three small series, not a prior.
  5. **No ketamine treatment of a WWOX/WOREE patient was found** (PubMed 0/0/0 on three queries; Europe PMC 2 hits for WOREE+ketamine, both WWOX gene-therapy mouse papers using ketamine only as an anaesthetic). The input's "none" stands (two routes; see Q4).
  6. **Only one randomised paediatric ketamine trial exists (KETASER01): halted, 10 patients, 2/5 vs 2/5, "No conclusions can be drawn".** No controlled paediatric data otherwise; Jacobwitz 2024 is a retrospective comparison.
  7. **Duration/GSK-3beta:** no paediatric source reports outcome or adverse events by infusion duration; none measured GSK-3beta. The clinical sources neither support nor contradict a "harmful side of a duration line" (see Q5).
* **Could not do:** read Kuki 2024 or Rosati 2012 full text (ScienceDirect 403 Cloudflare; neurology.org Cloudflare "Just a moment"): Q1 columns for these two are abstract-level, the rest "not stated in what I read". Tables 1-4 of Jacobwitz 2022 were not in the HTML bytes.

## Q1. The three series
Depth: Kuki abstract only; Rosati abstract only (+ secondary tables); DeVine complete full text. Full rows in `KETAMINE_PAEDIATRIC_SERIES.tsv`.

| Item | Kuki 2024 (38461760) | Rosati 2012 (23197747) | DeVine 2023 (37139250) |
|---|---|---|---|
| Design | DATO "retrospective observational cohort study ... consecutive series of 18" 2008-2023; 3 hospitals in affiliations; multicentre not stated | DATO "small, open-label, unblinded series with no concurrent control group"; single centre; consecutive ("all children consecutively referred"); prospective/retrospective not stated | DATO case series, 3 infants, single centre, Jun 2019-Jun 2020 |
| Age, n | 18; "median age at SRSE onset was 1 year 5 months (range: 11 days-24 years)". Under 1 year: at least one (min 11 d); count not stated. Includes patients up to 24 y | 9 (secondary 38926769: 1 y 4 m-10 y 5 m, median 4 y 8 m, so none under 1 y; INFERENZA from a secondary table) | 3 infants (29, 52/79 and 60 days; 4 courses): all under 1 y |
| Aetiology, genetic | inflammatory 10 (meningitis 2, encephalitis 3, FIRES 5); non-inflammatory 8, composition not stated; genes not stated | secondary: MELAS 1, "RS" 1, SPE 2, FIRES 2, unknown 5; no gene named | abusive head trauma; ischaemic stroke after vein of Galen malformation; post-cardiac-arrest injury. No genetic |
| RSE/SRSE definition | SRSE per title; definition not in abstract | RSE; SE persisted >24 h in 8 (super-refractory) | DATO "SRSE ... seizures unresolved despite use of continuous infusions of midazolam, pentobarbital, or propofol"; RSE = unresolved after first/second-line |
| Endpoint | ">50% seizure reduction" (seizures/h); response rate | "resolution of RSE" | "resolution of seizures" on EEG (Table); tolerability |
| Result (quote) | "Fifteen (83%) patients achieved >50% seizure reduction"; seizures/h 5.9 -> 0.9, p<0.0001 | "associated with resolution of RSE in 6 children" (6/9); of 3 non-responders "2 were cured by surgical removal of epileptogenic focal cortical dysplasia" | "In 2 of 3 cases, seizures resolved with therapy including ketamine" (Discussion); patient 3 died after limitation of care, "no resolution of seizures on EEG" |
| Prior lines, concurrent | not in abstract (secondary: median 5 ASMs before; 16 had thiopental; INFERENZA via 41409370) | midazolam 9, thiopental 5, propofol 4 before; midazolam add-on "to prevent emergence reactions" | "refractory to an average of 6 antiseizure medications"; average 3 concomitant ASMs |
| Regimen descriptor | not in abstract (secondary: bolus 0.5-2 mg/kg, infusion 1-6 mg/kg/h) | IV continuous infusion, median 40 mcg/kg/min (10-60) | 1-2 boluses 1 mg/kg then infusion from 1 mg/kg/hr (max 6 in one pt); average 5 d |
| Time to response | not in abstract | not in abstract | pt 2: "Seizures ceased within 1 hour of initiation"; pt 1 EEG resolution on hospital day 14 after "5 days of ketamine infusion without successful control of subclinical seizures"; pt 2 second admission resolution on a spot EEG "15 days after discontinuation" |
| Adverse events | "Three (17%) ... transient adverse events requiring intervention within 24 h" (3/18) | "None ... serious adverse events"; secondary: hypersalivation 100%, transaminitis 44% | "no adverse effects such as agitation, arrhythmias, or sialorrhea"; hypoglycaemia attributed to adrenal insufficiency, hypotension to midazolam, lactic acidosis to pentobarbital propylene glycol |
| Mortality | not in abstract | none per secondary (0) | 1/3 died (withdrawal of life-sustaining therapy) |
| Neurological outcome | "higher neurological decline (p = 0.0003)" in inflammatory group; definition not stated | not stated | not stated (EEG only) |
| Funding / COI | "Research Support, Non-U.S. Gov't" (PubMed type); statement not read | Europe PMC record lists Telethon grant GGP05177; statement not read | DATO "no conflicts or financial interest" |

**Pooled 24/30.** Takes 15/18 + 6/9 + 3/3. DATO endpoints: >50% reduction; resolution of RSE; third = tolerability in the input, resolution of seizures in 2 of 3 in the paper. Corrected 2/3 gives 23/30 = 76.7% (Wilson 59.1-88.2). Wilson for 24/30 reproduced: 80.0 (62.7-90.5). Endpoints are NOT comparable (reduction vs cessation vs mixed). Kuki's own "response rate" is not given as a number in the abstract; a secondary table (41409370 Table 1) lists "7 out of 18" seizure termination for Kuki, a figure I could not verify and which would, if true, pull the pooled value far down (24 -> 16/30 under a cessation-only logic; INFERENZA, unverified).

## Q2. Etiology stratification (Kuki 2024)
* DATO (abstract): "The inflammatory etiology group required a longer treatment duration (p = 0.0453) and showed lower seizure reduction (p = 0.0264), lower response rate (p = 0.0044), and higher neurological decline (p = 0.0003) than the non-inflammatory etiology group." Inflammatory n=10 (bacterial meningitis 2, viral encephalitis 3, FIRES 5); non-inflammatory n=8 by subtraction (INFERENZA).
* Not stated in what I could read: composition of the non-inflammatory group (genetic / structural / unknown), any separate genetic DEE, effect sizes, group-wise response numerators, mortality, definition of "neurological decline".
* Secondary report (Yan 2024, 38782798, full text read): seizure frequency fell significantly in both groups (inflammatory p=0.0020; non-inflammatory p=0.0078), pre-ketamine seizure frequency was lower in the non-inflammatory group (p=0.026), neurological function better in non-inflammatory (p=0.0003), and the authors state "due to the small sample size ... we cannot conclusively determine whether this theory holds." So the inflammatory group did respond on the continuous measure.
* Whether a genetic aetiology "such as WOREE" falls in the better stratum: does not follow. It would need (a) the non-inflammatory group's composition, (b) genetic cases being among them, (c) their response. None is in the reachable data. TRANSFER from inflammatory-vs-not to genetic-DEE has no support here. Data permit only: non-inflammatory 8 patients did better than inflammatory 10; the stratum is an exclusion category.

## Q3. Wider literature
Queries and counts: `SEARCHES.tsv` (PubMed: 84 / 24 / 6 / 6 for the four required queries; Europe PMC full-text-wide: 1332 / 201 / 229 / 251). Sources opened: 17 paediatric or review sources beyond the three (see SOURCES.tsv).

**Reviews/meta-analyses (all secondary, non-independent: they re-pool the same series)**
| Source | Design | Paediatric content | Endpoint | Result | Risk-of-bias statement | Depth |
|---|---|---|---|---|---|---|
| Aldhafeeri 2025 Cureus (41409370) | single-arm RE MA, 10 studies | 4 studies, n=138 (list inconsistent) | study-defined seizure termination | overall 56% (51-61), paed 50% (41-59), adult 59% (53-65), p=0.1029 | NIH tool, 8 good 2 fair; "adverse event reporting was inconsistent"; not registered | full |
| Chiriboga 2024 Epilepsia (38881333) | SR/MA, 6 case series/cohorts | 172 | SE cessation | 51% (43-59), I2 0 | case reports excluded "because of reporting bias" | abstract |
| Adhikari 2024 (38926769) | SR, 19 studies, 336 pts | Mewasingh 5, Rosati 9, Wang 18 | seizure resolution; BS; mortality | paed series resolution 66.7-100%; burst suppression 5/9 Rosati, 3/18 Wang | quality assessed, "lack a control group" | full |
| Yan 2024 J Neurol (38782798) | SR, 11 studies, MINORS | Kuki, Rosati, Jacobwitz | termination | narrative | "risk of bias ... low" per authors (not endorsed by me) | full text |
| Lele 2026 (41550426) | SR/MA 14 studies | 0 (388 adults) | cessation | 64% (49-76) | embargoed full text | abstract |
| Troya-Cordova 2026 (42835272) | SR 12 studies | 0 | study-defined | 43.3-100%, survival 45.8-81.8% | NIH tools; "independent effect ... remains uncertain" | full |
| Cornwall 2023 JAMA Neurol (37523161) | SR/MA adult nonanoxic SRSE | 0 | success, mortality, disability | ketamine "not associated with outcome" | tools stated, not read | abstract |

**Largest paediatric primary cohorts**
| Source | n | Design | Endpoint, result | Regimen descriptor | Duration | Harms with denominator |
|---|---|---|---|---|---|---|
| Jacobwitz 2022 (35817569) | 69 (13 neonates) | retrospective single centre, Class IV | cEEG termination 32/69 (46%); reduction 19/69 (28%); none 18/69 (26%) | start 1 mg/kg/h in 66/69; bolus in 65/69 | median total infusion 85.7 h (IQR 49.7-128.0) | AE requiring intervention 3/69 (4%): hypertension 2, delirium 1; "No patients experienced withdrawal symptoms/signs during ketamine wean"; 21/69 (30%) died before discharge; 16/46 survivors new or worse epilepsy; 10/46 still seizing |
| Jacobwitz 2024 (37783824) | 117 (38 ketamine) | retrospective comparative | termination 23/38 (61%) vs midazolam 22/79 (28%), OR 3.97; multivariable OR 4.00 | not in abstract | not in abstract | AE 1/38 vs 20/79; survival to discharge 21/38 (55%) vs 65/79 (82%), P=0.002, "did not attribute any deaths" |
| Ilvento 2015 (26189786) | 13 children, 19 treatments | retrospective protocol series | RCSE resolution 14/19 episodes | 7-60 mcg/kg/min | 22 h-17 d | not in abstract |
| Keros 2017 (28349774) | est. 48 | administrative database | no efficacy endpoint | n/a | n/a | died 29% vs 17% (confounded) |

**Table by endpoint (no cross-endpoint pooling is done)**
| Endpoint | Paediatric figures (study: result) |
|---|---|
| Seizure cessation | Jacobwitz 2022 32/69; Jacobwitz 2024 23/38 first-line; Ilvento 14/19 episodes; Rosati 6/9; DeVine 2/3 (EEG resolution, attribution unclear); KETASER01 2/5 vs 2/5 (thiopental); secondary pooled 50% and 51% |
| Seizure reduction | Kuki 15/18 (>50% reduction); Jacobwitz 2022 19/69 reduction (51/69 = 74% termination or reduction, a mixed figure) |
| EEG burst suppression | Rosati 5/9 (+1/9 transitory; secondary); Ilvento 10/14 responder episodes after initial bolus; Jacobwitz 2022 induced burst suppression 1/69, suppression 2/69; Wang 3/18 (secondary) |
| Neurological outcome | Kuki "higher neurological decline" in inflammatory (p=0.0003, definition not stated); Jacobwitz 2022 16/46 survivors new or worse epilepsy; no standardised long-term outcome in any source |
| Mortality | Jacobwitz 2022 21/69 (30%); Jacobwitz 2024 ketamine 17/38 died (55% survival); DeVine 1/3; Rosati 0 (secondary); Keros 29% vs 17%; Kuki not stated |

**Randomised or controlled paediatric ketamine data:** KETASER01 (NCT02431663; protocol 27311915; results 35833327): "only 10 individuals (five for each study arm) were enrolled", "prematurely halted", "No conclusions can be drawn". Routes: PubMed (Ilvento author query, KETASER search), Europe PMC "(KETASER OR NCT02431663)" 7 hits. Chiriboga's "one nonconclusive clinical trial" is probably the same (INFERENZA). No other randomised paediatric trial found; the only controlled comparison is retrospective (Jacobwitz 2024).

**Cross-source cautions (INFERENZA):** Jacobwitz 2022 (38 first-line ketamine patients) and Jacobwitz 2024 (38 ketamine patients) very probably overlap; Ilvento 2015 overlaps Rosati 2012 in place and start date; so these cannot be added. The two paediatric MAs in the table contain errors I could see (Aldhafeeri: "407 patients" vs 388, "largest study 388" vs max 69 listed, Kuki 7/18; Lele: "0.7%, 3/55"). They are not independent evidence.

## Q4. Ketamine in genetic DEE; WWOX / WOREE
| Gene | Source | n given ketamine | Outcome (DATO) |
|---|---|---|---|
| GRIN2D (gain of function) | Li 2016 (27616483), abstract | 1 of 2 probands | "dramatic electroclinical improvement upon treatment with ketamine and magnesium" in refractory SE; memantine to both "mild to moderate improvement" |
| ATP1A2 (DEE-98) | Orgun 2025 (39970743), abstract | 1 | "partially responsive to ketamine ... seizure-free when memantine ... added" (n=1; genotype known after treatment) |
| KCNQ2 | Freibauer 2018 (30530441) | 1 neonate | ketamine started for septic shock/seizures; death after withdrawal of care; response not stated |
| GRIN1 | Xu 2021 (34227748) | 0 (in vitro) | memantine reduced seizure burden |
| SCN, STXBP1, CDKL5, KCNT1 | PubMed query (2 hits) | none found | CDKL5 cohort abstract has no ketamine data |
| GRIN2D mouse | Yam 2026 (40277233), TRANSFER | mice | ketamine 4 or 10 mg/kg "caused seizures", 0.5 mg/kg limited effect |
No paediatric DEE-gene cohort reports ketamine response by gene; Jacobwitz 2022 text has no genetic stratum (tables not read). **WWOX/WOREE:** PubMed "WWOX ketamine" 0; "WOREE ketamine" 0; "WWOX AND (ketamine OR NMDA receptor antagonist OR memantine)" 0. Europe PMC full-text "(WWOX AND ketamine)" 33; "(WOREE AND ketamine)" 2. The 2 WOREE hits opened in full text: ketamine only as perfusion or electrophysiology anaesthetic. The other 31 WWOX+ketamine hits (oncology, lung, bone, conference supplements by title) were not opened. Verdict on "no WWOX patient has received ketamine in any published report": NOT CONTRADICTED by two routes; absence of a report is not absence of use.

## Q5. Duration
* DATO, no paediatric source reports efficacy by infusion duration (Jacobwitz 2022: duration "was not different when ketamine was administered as the first anesthetic ... or after midazolam", p=0.50; that is not outcome by duration). Adverse events by duration: not stated in any paediatric source.
* Adult meta-analysis (Lele 2026, abstract): responders and non-responders both "5.0 +/- 4.2 days", MD -0.07 d (95% CI -1.02 to 0.88): no duration signal for response.
* Long infusions, harms: Adhikari 2024 (secondary) records one adult with temporary hepatic failure after the longest infusion in that series (24 days) and "no mortality related directly to the dose and duration" (Gaspard, Hofler); Cornwall 2023: very long SRSE treatment (>28 d, not ketamine-specific) lower mortality, "increased risk of moderate to severe disability". Tolerance or withdrawal: Jacobwitz 2022 "No patients experienced withdrawal symptoms/signs during ketamine wean" (median infusion 85.7 h; wean median 22.9 h). DeVine: none noted.
* Therefore: nothing in these clinical sources supports or contradicts a "harmful side" of a GSK-3beta duration line. The 7.5 d median is the longest of the paediatric series (Kuki), shorter than the 24-day adult maximum, and tied to aetiology. GSK-3beta is a rodent argument: TRANSFER, not tested here, no human source measured it.

## What the sources do not state
Responder definition and numerators per group (Kuki), under-1-year count (Kuki), Rosati prospective vs retrospective and funding statement, long-term neurodevelopmental outcome (all), blinding and randomisation (all except KETASER01), genetic strata (all), denominator for most harms at abstract level.

## Limits
Two key papers abstract-level; PMC reCAPTCHA pages (PMC12706389, PMC11210084, PMC10391362, PMC9436287) discarded, Europe PMC XML used where it worked, 41550426 embargoed. Europe PMC counts are full-text-wide and not comparable with PubMed. No dose or use recommendation is made or implied.

**Update 2026-11-17 (IT; after blind verification of sampled rows):** corrections for this package are in `../CORRECTIONS_AFTER_BLIND_VERIFICATION_IT_20261117.md`; the text above is unchanged.
