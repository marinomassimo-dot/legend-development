# P5 (KDS lane C evidence): randomised paediatric evidence for DEE alternatives and the status-epilepticus rescue niche. Producer: legend-delegate (sonnet, medium). Copied by IT from the delegate's hand-back message (its Write of REPORT.md was refused); content unchanged except layout. Non-canonical producer output. Not medical advice. Reference genotype class only. No dose or recommendation.

> **PRODUCER REPORT, CORRECTED ROWS (IT, 2026-11-18, ADV-048).** This is the delegate's final message copied unchanged. After ADV's blind verification these rows were corrected and are not to be read as written: P5-13, P5-28 (cenobamate: all 16 patients), P5-43 (the harms quote lost its subject), P5-56, P5-57. See `it_ketamine_lanes_20261117/CORRECTIONS_AFTER_BLIND_VERIFICATION_IT_20261117.md`.

Labels: DATO = stated by the source (quote and locator in the TSV); INFERENZA = reasoning; TRANSFER = other disease or age. Depth is ABSTRACT for almost every row (Europe PMC record bytes held and checked; where a full-text XML is held only funding and statement paragraphs were read). Many NEJM, Lancet and Neurology full texts are not open, so "not stated" means "not in the abstract", not "absent from the paper".

## ANSWERS FIRST
**Q1 (DATO).** Randomised placebo-controlled trials found and read at abstract level for: cannabidiol (Dravet 2 trials, LGS 2); fenfluramine (Dravet 3, LGS 1); stiripentol (Dravet, 1 small trial, 2000); ganaxolone (CDKL5, 1); everolimus (TSC: EXIST-3 and its paediatric post-hoc analysis); vigabatrin and hormonal therapy in infantile spasms (the placebo-controlled 1999 trial, the 2001 dose comparison, UKISS and ICISS); ACTH vs prednisone (a 1996 trial plus meta-analyses); ketogenic diet (5 randomised trials in children or infants). Cenobamate has no paediatric DEE RCT (only a 16-patient single-centre retrospective LGS series). Rufinamide and clobazam (LGS) were added as the two allowed extras.
**Q2 (DATO).** Established-SE evidence: randomised paediatric evidence exists: ESETT (225 children in the paediatric stratum; the three drugs each succeeded in about half); EcLiPSE and ConSEPT (levetiracetam vs phenytoin, neither significantly superior); a 110-child Indian trial stopped for futility. Refractory-SE anaesthetic infusions: no placebo-controlled paediatric RCT; small open randomised comparisons (midazolam vs diazepam infusion n=40; valproate vs midazolam infusion n=70), observational data and systematic reviews, a Cochrane propofol vs thiopental review with one 24-adult trial ("low quality evidence"). Ketamine: KETASER01 (NCT02431663) randomised ketamine against thiopental, midazolam and propofol in children and was halted after 10 patients: "No conclusions can be drawn regarding the objectives of the study." Othman 2025 is an RCT of ketamine plus midazolam vs placebo plus midazolam as FIRST-line treatment in generalized convulsive SE (n=144), not a refractory-SE trial. The comparative retrospective cohorts disagree in direction on survival. No paediatric systematic review with GRADE-type grading wording was found; reviews state strength of evidence in prose.
**Q3 (DATO).** No randomised paediatric epilepsy/DEE trial was found for dextromethorphan, amantadine, radiprodil or esketamine. Radiprodil: a phase 1b in 3 infants with infantile spasms (non-randomised) and registrations; NCT07224581 is a randomized, triple-masked phase 3 in GRIN-related disorder, recruiting, no results held. Dextromethorphan: only sibling and case reports in non-ketotic hyperglycinaemia. Amantadine: a 12-child retrospective series. Esketamine: one paediatric NORSE case report. Memantine not duplicated (P1 scope).
**Q4.** No Q1/Q3 agent has an agent-specific measurement in a Wwox model in the repository cards. Clinical-report or class-level cards exist for cannabidiol, vigabatrin, ACTH/corticosteroids and the ketogenic diet. The only WWOX-system NMDAR pharmacology is d-APV on neuron-specific Wwox-knockout slices (PAPER 031).

## Q1 evidence table (full quotes, harms and locators in ALTERNATIVES_RCT_EVIDENCE.tsv)
| Agent | Setting | Trial | n | Primary result (DATO, abridged) | Harms (DATO) | Funding |
|---|---|---|---|---|---|---|
| cannabidiol | Dravet | 28538134 / NCT02091375 | 120 | convulsive seizures/month 12.4 to 5.9 vs 14.9 to 14.1 (diff -22.8 pts, P=0.01) | more diarrhoea, vomiting, fatigue, pyrexia, somnolence, abnormal liver tests; more withdrawals on drug | GW Pharmaceuticals |
| cannabidiol | Dravet, 2 doses | 32119035 / NCT02224703 | 198 | 48.7% / 45.7% vs 26.9% reduction | transaminase rise 13 vs 3 (all on concomitant valproate) | GW Research |
| cannabidiol | LGS | 29768152 / NCT02224560; 29395273 | 225; 171 | drop seizures 41.9% / 37.2% vs 17.2%; 43.9% vs 21.8% | AE 86% vs 69%; AE withdrawals 14% vs 1%; elevated aminotransferases 9% | GW |
| fenfluramine | Dravet | 31862249; 31790543 (with stiripentol); 37543865 | 119; 87; 143 | 62.3%; 54.0%; 64.8% greater MCSF reduction vs placebo | decreased appetite, fatigue, somnolence; no valvular disease or PAH in these trials | Zogenix |
| fenfluramine | LGS | 35499850 / NCT03355209 | 263 | drop seizures -19.9 pts vs placebo (P=.001) | appetite loss 22%, somnolence 13%, fatigue 13% | Zogenix |
| stiripentol | Dravet, with valproate and clobazam | 11089822 (STICLO) | 41 | responders 71% vs 5% | moderate AEs in 21 vs 8 patients; resolved on co-medication reduction in 12 of 21 | not stated |
| ganaxolone | CDKL5 | 35429480 / NCT03572933 | 101 | median 28-day major-motor-seizure change -30.7% vs -6.9% (p=0.0036) | AE 86% vs 88%; serious AE 12% vs 10% | Marinus |
| everolimus | TSC focal seizures | 27613521 / NCT01713946; 30169322 | 366; 299 paediatric | response 15.1% placebo vs 28.2% / 40.0% | grade 3-4 AE 11% / 18% / 24% | Novartis |
| vigabatrin vs hormonal | infantile spasms | 15541450 (UKISS) | 107 | no spasms d13-14: 73% hormonal vs 54% vigabatrin | AE 55% vs 54% | not stated |
| vigabatrin + hormonal vs hormonal | infantile spasms | 27838190 (ICISS) | 377 | 72% vs 57% spasm-free d14-42 | 33 serious reactions needing hospital (16 vs 17) | not stated |
| vigabatrin vs placebo | infantile spasms | 10565592 | 40 | spasm reduction 78% vs 26% (5-day double-blind phase) | no AE withdrawals | not stated |
| ACTH vs prednisone | infantile spasms | 8604274 | 29 | 13/15 vs 4/14 responders | not in held abstract | not stated |
| hormonal therapy (SR/NMA) | infantile spasms | 35222241 | 19 RCTs, 1279 | oral steroids vs ACTH RR 0.85 (0.41-1.76) | low-dose vs usual ACTH: lower AE risk | not stated |
| ketogenic diet | childhood epilepsy | 18456557; 27027847 | 145; 57 | 62.0% vs 136.9% of baseline seizures; 50% vs 18.2% responders | constipation, vomiting, hunger; GI symptoms | charities; not stated |
| ketogenic diet vs antiseizure medicine | infants | 37977712 (KIWE) | 136 | seizures/day similar (IRR 1.33, 0.84-2.11) | 3 deaths, all in the diet arm (judged unrelated by investigators) | NIHR |
| ketogenic diet vs ACTH | infantile spasms | 30801699; 40570615 | 101; 87 | remission similar | AE needing intervention 30% vs 94%; any AE 59.5% vs 95.1% | not stated |
| rufinamide; clobazam (extras) | LGS | 18401024; 21956725 | 139; 238 | total seizures -32.7% vs -11.7%; drop seizures -41.2 / -49.4 / -68.3% vs -12.1% | somnolence, vomiting; somnolence, pyrexia | not stated |

Rows not in this table: 37233891 (modified Atkins vs ketogenic diet, n=40); 40116235 (vigabatrin plus prednisolone vs vigabatrin alone, early-terminated, 17 vs 24 infants, 77% vs 33% remission). Not held: the Wanigasinghe prednisolone-vs-ACTH RCT (not returned by search); the Acthar label (not retrievable).

### Regulatory wording (openFDA label JSON field indications_and_usage; open, US only, one label version each; quoted exactly)
* Epidiolex (20260529): "EPIDIOLEX is indicated for the treatment of seizures associated with Lennox-Gastaut syndrome (LGS), Dravet syndrome (DS), or tuberous sclerosis complex (TSC) in patients 1 year of age and older."
* Fintepla (20261022): "FINTEPLA is indicated for the treatment of seizures associated with Dravet syndrome (DS) and Lennox-Gastaut syndrome (LGS) in patients 2 years of age and older."
* Diacomit (20260427): "DIACOMIT is indicated for the treatment of seizures associated with Dravet syndrome (DS) in patients taking clobazam who are 6 months of age and older and weighing 7 kg or more."
* Ztalmy (20260904): "ZTALMY is indicated for the treatment of seizures associated with cyclin-dependent kinase-like 5 (CDKL5) deficiency disorder (CDD) in patients 2 years of age and older."
* Afinitor Disperz (20260601): "AFINITOR DISPERZ is a kinase inhibitor indicated for the adjunctive treatment of adult and pediatric patients aged 2 years and older with TSC-associated partial-onset seizures."
* Sabril (20211020): "SABRIL is indicated as monotherapy for pediatric patients with infantile spasms 1 month to 2 years of age for whom the potential benefits outweigh the potential risk of vision loss"
* Banzel (20221215): "BANZEL is indicated for adjunctive treatment of seizures associated with Lennox-Gastaut Syndrome (LGS) in pediatric patients 1 year of age and older, and in adults."
* Onfi (20261016): "ONFI is a benzodiazepine indicated for adjunctive treatment of seizures associated with Lennox-Gastaut syndrome (LGS) in patients 2 years of age or older."
* Xcopri (20250825): "XCOPRI is indicated for the treatment of partial-onset seizures in adult patients." INFERENZA: this label version has no paediatric indication.
* Ketalar (20260327): "KETALAR is a general anesthetic indicated: as the sole anesthetic agent for diagnostic and surgical procedures that do not require skeletal muscle relaxation". No status-epilepticus indication on this page.

## Q2 table
| Source | Population | n | Result (DATO) | Harm (DATO) | Design |
|---|---|---|---|---|---|
| ESETT 31774955 / NCT01960075 | benzodiazepine-refractory convulsive SE, children and adults | 384 | levetiracetam 47%, fosphenytoin 45%, valproate 46% | hypotension and intubation numerically more on fosphenytoin, deaths numerically more on levetiracetam, "not significant" | blinded adaptive RCT (stopped for futility) |
| ESETT age strata 32203691 | 225 children | | 52% levetiracetam / 49% fosphenytoin / 52% valproate | intubation in children differed by drug | pre-specified subgroup |
| EcLiPSE 31005385 | paediatric convulsive SE | 286 | cessation 70% vs 64%; HR 1.20 (0.91-1.60) | one hypotension serious adverse reaction on phenytoin | open-label RCT |
| ConSEPT 31005386 | paediatric | 233 | 60% phenytoin vs 50% levetiracetam; RD -9.2% (-21.9 to 3.5) | 1 death, unrelated | RCT |
| Vignesh 32198861 | 3 months to 12 years | 110 | 89% / 83% / 94% (P=0.38) | 1 shock, 1 death | double-blind, stopped for futility |
| Abbaskhanian 34706856 | third-line | 70 | valproate infusion 91.4% vs midazolam infusion 85.7% | intubation 2 vs 8 (p=0.023) | randomised; masking not stated |
| Singhi 11952069 | refractory CSE, 2-12 years | 40 | midazolam 86% vs diazepam infusion 89% | mortality 38% vs 10.5% | open-label RCT (2002) |
| Cochrane 28155226 | adults, propofol vs thiopental | 24 | 6/14 vs 2/7, "low quality evidence" | mortality 3/14 vs 1/7 | one trial |
| Claassen 11903460 | all ages, 28 studies | 193 | pentobarbital: lower short-term failure (8 vs 23%) | hypotension 77 vs 34%; mortality 48% | SR, no RCT |
| Tasker 27500721 | paediatric RSE, 9 US hospitals | 111 | seizure termination 94% by second cycle; midazolam first-line 78%, pentobarbital second-line 82% | not in held abstract | prospective observational |
| Johnson 40297557 | paediatric midazolam infusions | 448 | 81% aborted seizures | "All studies had concerns regarding the risk of bias." | SR (3 RCT of 19) |
| Au 38466294 | all ages | 1637 | "CIVAD choice and EEG type were not predictors of mortality." | hypotension differed by agent | SR |
| KETASER01 35833327 | paediatric RCSE, ketamine vs thiopental | 10 | 2/5 vs 2/5 | not stated | halted RCT |
| Othman 40186980 / NCT05779657 | generalized convulsive SE, first-line, 6 months to 16 years | 144 | seizures stopped at 5 min: 76% vs 21% | intubation 4.2% vs 20.8% | RCT (abstract only) |
| Jacobwitz 37783824 | paediatric RSE, first-line infusion | 117 | termination 61% ketamine vs 28% midazolam | survival to discharge 55% ketamine vs 82% midazolam | retrospective, confounded by indication |
| Horvat 39875684 | RSE with cardiac disease | 34 | 73% vs 63% needing one infusion | no difference in attributable AE | retrospective |
| Yavuz 42424871 | RCSE | 77 | adjusted OR 4.16 (0.99-17.44; p=0.052) | no serious treatment-limiting AE | retrospective |
| Kuki 38461760 | paediatric SRSE | 18 | ">50% seizure reduction" in 15 (83%) | 3 (17%) transient AE needing intervention | uncontrolled |
| Rosati 23197747 | paediatric RSE | 9 | resolution in 6 | none serious | open-label series, "Class IV evidence" |

**Ketamine-review wording on strength of evidence (DATO, quoted):**
* Chiriboga 2024 (paediatric; 6 series/cohorts, 172 patients): "SE cessation was attained in 51% (95% confidence interval = 43-59) of cases with the addition of ketamine." Also: "Without strong recommendations and evidence regarding preferred agents, this review provides evidence that ketamine may be considered in managing SE in the pediatric population." The abstract states no formal grade.
* Rosati 2018 (29 children among 248 individuals): "We found no results from randomised controlled trials." Also: "available studies are hampered by methodological limitations that prevent any firm conclusion."
* Yan 2024: "there are currently no randomized controlled trials internationally assessing the efficacy of ketamine for treating super-refractory status epilepticus".
* Troya-Cordova 2026: "the independent effect of ketamine on sustained seizure control, survival, and functional recovery remains uncertain."
* Aldhafeeri 2025: "Subgroup analysis showed efficacy rates of 59% in adults and 50% in children". Lele 2026 is adults only (64%).

INFERENZA: no paediatric review uses GRADE-type certainty labels in its abstract (one Europe PMC abstract query plus a grep of the full text of 4 open-access reviews: Adhikari, Yan, Pin, Aldhafeeri; the only hit was a reference title); not an exhaustive absence claim.
INFERENZA on the input: its paediatric series figures match the abstracts held (Kuki 15/18, Rosati 6/9, DeVine 3 patients); its "uncontrolled case series" framing omits the randomised KETASER01 (halted at 10 patients) and the Othman first-line RCT; the only comparative cohort with survival data (Jacobwitz) shows lower survival to discharge on the ketamine side, termination higher on ketamine, the authors stating ketamine was used more often for acute symptomatic seizures. The input's 24/30 pooling was not tested (outside P5).

## Q3 table
| Agent | What exists (DATO) | Randomised paediatric epilepsy/DEE evidence |
|---|---|---|
| radiprodil | Phase 1b, 3 infants with infantile spasms (32106360, UCB Pharma): "One infant became spasm-free and two showed clinical improvement without reaching spasm-freedom"; two worsened after withdrawal. Registry: NCT05818943 (phase 1, GRIN-related), NCT06392009 (phase 1/2, non-randomised), NCT07224581 (phase 3, randomized triple-masked, recruiting) | None with results |
| dextromethorphan | NKH sibling comparison (26749113) and a case report (40611912, triple therapy with ketamine and benzoate) | None; ClinicalTrials.gov dextromethorphan + epilepsy returned 0 |
| amantadine | 12-child retrospective series (42044942); 4/5 with D/EE-SWAS vs 1/7 with refractory epilepsy | None |
| esketamine | One paediatric NORSE case with haemorrhagic cystitis (41113565) | None; ClinicalTrials.gov esketamine + status epilepticus returned 0 |
| memantine | Not duplicated (P1) | NCT03779672 appeared in a registry query only |

## Q4: WWOX-system measurement in the repository cards (read-only)
| Agent | Card id | What is held |
|---|---|---|
| cannabidiol | EB-CBD-AX-01 (U16) | clinician-reported seizure control in a WWOX epilepsy cohort plus one severe WOREE case, from the known-roads note ("queried_not_full_read", UNRESOLVED); no Wwox-model measurement |
| fenfluramine | none held | |
| stiripentol | none held for the drug in a WWOX system; E02_ldh_inhibition (U13) holds LDH-axis WWOX-biology readouts, stiripentol appears there only as a comparator from other contexts | |
| ganaxolone, everolimus/mTOR, cenobamate | none held | |
| vigabatrin | EB-VGB-01 (U20) and H02_gabaat_inactivator_myelin_exposure | two WWOX-null children with West syndrome (CLAIM 001); no Wwox-model measurement |
| ACTH / prednisolone | EB-HORM-AX-01 (U18); P11_magnesium_nmdar_gate | class-level curated reports; P11 is about ACTH + magnesium trials outside WWOX |
| ketogenic diet | EB-KD-01 and E04_ketogenic_lactate_axis (U15) | WOREE case-series reading (CLAIM 042); no Wwox-model measurement |
| ketamine | F04_nmdar_intervention_class (U21) | no ketamine measurement in a Wwox system; the Wwox-knockout slice data (PAPER 031) used d-APV only |
| memantine | F01_glutamate_receptor_node, F04 | "No memantine or perampanel has been given to any Wwox system." |
| radiprodil, dextromethorphan, amantadine, esketamine | F04 (class members; radiprodil rows DR-P9-006/007/008 are other-disease precedent) | none held in a WWOX system |

## What is not stated, and limits
* All pivotal-trial rows are abstract-level; harms are only those the abstract lists; denominators, blinding and responder definitions beyond the abstract are "not stated" here. Funding is "not stated" in most older abstracts; where found in full-text XML or Europe PMC grant metadata, the TSV locator says so. No dose or schedule is given; only trial arm labels appear.
* No challenge page was met. Europe PMC fullTextXML returned HTTP 500 for ESETT (Kapur 2019), Chamberlain 2020, Ng 2011, Prabhakar 2017, Tasker 2016, Baram 1996, Downs 2024 and Jacobwitz 2022, so they stay abstract-only (error bodies deleted). The PMC article-page fallback was not tried, for lack of time.
* A first ClinicalTrials.gov query pattern with an OR in the condition field returned unrelated studies and was discarded; the valid queries are in SEARCHES.tsv. Absence claims rest on the two routes and exact queries in SEARCHES.tsv: cenobamate paediatric DEE RCT; dextromethorphan, amantadine and esketamine RCTs; GRADE wording in paediatric ketamine reviews. Nothing is pooled across trials; the comparison is the caller's.
* One XML (Auvin 2020) contains an author e-mail text; it was not used or sent anywhere.

## Files (/tmp/it56_ket/p5_alternatives/)
ALTERNATIVES_RCT_EVIDENCE.tsv (58 rows, 11 columns, every result/harm/funding quote machine-checked as an exact substring of the held bytes, 0 mismatches), SOURCES.tsv (103 byte-checked sources), SEARCHES.tsv (56 searches with exact query strings and counts), sources/.

**Update 2026-11-17 (IT; after blind verification of sampled rows):** corrections for this package are in `../CORRECTIONS_AFTER_BLIND_VERIFICATION_IT_20261117.md`; the text above is unchanged.
