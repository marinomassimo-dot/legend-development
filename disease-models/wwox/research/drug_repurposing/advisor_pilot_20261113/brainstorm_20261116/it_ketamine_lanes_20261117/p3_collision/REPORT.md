# P3 (lane B5) report: the five collision papers, claim K6. Producer: legend-delegate (sonnet, medium). Copied by IT from the delegate's hand-back message (its Write of REPORT.md was refused); content unchanged except layout. Non-canonical; not medical advice; reference genotype class only.

## ANSWER FIRST
* **K6 verdict.** The descriptive table is PARTLY SUPPORTED. The sentence "the expected harm in a WOREE infant is larger than in a neurologically intact child receiving the same exposure" is NOT SUPPORTED. Route: abstracts and full texts held in sources/ (SOURCES.tsv). No paper compares a ketamine exposure in a Wwox-deficient brain with a wild-type brain. "Same direction" is two separately measured findings placed side by side (INFERENZA); "larger harm" is an IPOTESI.
* **Q1.** The WWOX baseline quotes are verbatim in the abstracts of 33914858, 30290271 and 34634460. Three ketamine-side quotes are altered or lose context: 25477370: "gamma-aminobutyric acid" is replaced by "GABA" inside the quotation marks and "but not layer 5" is dropped; 31263401: "decreased the expression of p-GSK-3beta" is followed in the abstract by "in vitro" (neural stem cell culture); 42808560: the 16-h return to baseline is omitted.
* **Q2.** None of the five is comparable to the Kuki 2024 regimen on duration (hours versus a median of 7.5 days). Age mapping and intensity are not determinable. 41618072 is the only multi-day exposure, in adult male mice at daily i.p. dosing.
* **Q3.** The IPOTESI list is in section 4.
* **Q4.** Ketamine-specific human data exist but are weak: 24659739 (infants with repeated anaesthetic ketamine, Bayley scores lower after 3 exposures); 37440275 (observational, infants with congenital heart disease, dose-associated lower Bayley motor score). None met reports ketamine neurotoxicity in children with WWOX loss of function, or in status-epilepticus infusion cohorts.
* **Access blocks (stopped, no retry or bypass).** 42808560: SAGE, Cloudflare. 25477370: OUP, Cloudflare. 30290271: PMC page, reCAPTCHA (abstract used). Europe PMC fullTextXML returned HTTP 500 for PMC9831613 and PMC7104842; the PMC page worked for PMC9831613.

## 1. Per-paper table (all rodent; DATO unless marked; full rows in COLLISION_PAPERS.tsv)
| PMID | species and age | sex | amount as stated (descriptor only) | n and window | comparator | persistence | depth |
|---|---|---|---|---|---|---|---|
| 42808560 | SD rat, PND7 | both | 20 mg/kg i.p. | 5 injections, 90 min apart; brains at 2 h and 16 h | age-matched controls (saline not stated) | acute; baseline by 16 h | abstract |
| 31263401 | SD rat PND7; rat NSCs | not stated | 40 mg/kg loading, then 30% about every 40 min for 4 h; NSC 100 uM, 24 h | one 4-h session | saline | acute (12 h) and lasting (water maze PND42-47) | full text |
| 25477370 | mouse, "second postnatal week" | not stated | not stated | not stated | not stated | lasting (adult mPFC) | abstract |
| 36371060 | CD1 mouse, PND7 | both; no sex difference | 40 mg/kg i.p. ("sedative dose") | 4 injections every 90 min "over 6 h" | vehicle | lasting (PND20-40) | full text |
| 34666787 | SD rat, 7-day-old | half male, half female | 20 mg/kg i.p. | 5 doses every 90 min; samples 90 min after last; water maze at day 60 | saline | acute and lasting | full text |
| 33733293 | SD rat, 7-day-old | not stated | 20 mg/kg | 6 doses every 90 min | saline | not stated in abstract | abstract |
| 41618072 | C57BL/6J mouse, 8 weeks | male | 100 mg/kg i.p. daily | 7 days | saline | during dosing | full text |

* Funding and conflicts as stated: 31263401, 34666787, 33733293 and 41618072: Chinese national or provincial grants; no competing interests where a statement exists (not seen for 33733293, abstract only). 36371060: NIH NICHD and NIGMS grants plus departmental funds; no conflict. 42808560 and 25477370: not stated in the abstract.
* mg/kg given for all except 25477370 (not stated).
* Clinical relevance as stated by the papers: 36371060 (Methods) ketamine "is clinically used in pediatric intensive care unit for prolonged sedation"; 34666787 (Discussion) "clinical doses of ketamine (20 mg/kg)", no regimen comparison; 31263401 "anesthesia doses"; 41618072 an abuse model. No paper compares its regimen with a defined clinical exposure.
* Co-exposure: none; in 36371060 isoflurane only for terminal perfusion.
* Key results: 42808560: "significant increase in apoptosis and DNA damage at 2 hours, concomitant with an elevation in Olig2-positive cells"; "Neuronal, astrocytic, and microglial cells were unaffected"; "At 16 hours, a return to baseline levels was observed." 36371060: mEPSC frequency at PND20 8.70 Hz versus 5.30 Hz (p=0.009); amplitude at PND20 not different (p=0.25); at PND30+40 amplitude -23.87 versus -18.86 pA (p=0.04) and frequency 8.86 versus 6.42 Hz (p=0.01). 31263401: p-GSK-3beta lowered in vitro only, in NSCs; in vivo it reported cleaved caspase-3 up and proliferation down. 41618072: "decreased P-Akt, P-Gsk-3beta, and Bcl-2 levels along with increased Bax and cleaved-caspase-3".
* Not stated: blinding and denominators, except in 31263401 (random assignment; blind BrdU counting); dose-response; any human-equivalence calculation. "Ser9" appears in neither 31263401 nor 41618072, although the input writes "p-Ser9".
* 33733293: the abstract does not state that ketamine lowered p-GSK3beta; it says GM1 raised p-AKT and p-GSK3beta. The input's attribution is unverified at abstract depth.

## 2. Q1 axis-by-axis check
| Axis | Input ketamine quote: verbatim and as meant? | Input WWOX quote: verbatim? |
|---|---|---|
| Oligodendrocytes | 42808560 "Intrinsic apoptosis primarily involved neurons and oligodendrocytes" is verbatim; the same abstract says neuronal cells were unaffected and that baseline returned at 16 h, both omitted. | 33914858 "Wwox-mutant mice exhibited reduced maturation of oligodendrocytes, reduced myelinated axons and impaired axonal conductivity" is verbatim; the input's table says "OPC maturation failure", the abstract says "oligodendrocytes". |
| GSK-3beta | 31263401: the phrase is verbatim but the abstract continues "in vitro"; "repeated dosing" is maintenance dosing within one 4-h session. | 32000863 is outside this package's scope; not checked. |
| PV interneurons | 25477370 is altered (see answer first); the endpoints are PV expression and GABA release, not loss; the input's graph says "PV loss". | 30290271 "significantly reduced numbers of ... parvalbumin (PV) and neuropeptide Y (NPY) expressing interneurons" is verbatim (the ellipsis replaces "calcium-binding protein"); hippocampus in 2-week-old KO mice, a different region from mPFC. |
| Excitatory drive | 36371060 "lasting increase in excitatory synaptic transmission in hippocampal CA3 neurons" is verbatim; these are miniature EPSCs and amplitude rose only at PND30-40. | 34634460 "elevated amplitude of excitatory post-synaptic currents" is verbatim; neocortex layer II/III, versus CA3 in the ketamine paper. |
| Neuroinflammation | 34666787: the input paraphrases and quotes nothing; the paraphrase is consistent. | 30290271 "activated microglia, astrogliosis, and overexpression of inflammatory cytokines Tnf-a and Il6" is verbatim. |

* INFERENZA: "same" means both findings are adverse changes in a broad shared process; they do not share a measured quantity (species, region, endpoint and timing all differ).
* Side finding on the "opposing" row (DATO, 34634460 full text, Results, Fig 3): "Blocking glutamatergic neurotransmission with d-APV (50 uM) eliminated the spontaneous bursting events." Carbenoxolone "decreased the frequency of the events by 87% (p = 0.008)". The input's "ketamine blocks one of two dependencies" does not match this for APV, so it needs review by the lane owning K1 and K2. These are slice results; carbenoxolone is described as a non-specific gap-junction blocker.

## 3. Q2 comparability with Kuki 2024 (38461760; abstract descriptors only; no dose conversion)
* Descriptors (DATO): n=18, retrospective; "median age at SRSE onset was 1 year 5 months (range: 11 days-24 years)"; "median duration of treatment was 7.5 days (interquartile range: 2.8-15.5 days)"; route and dose not in the abstract.
* 42808560, 31263401, 36371060, 34666787, 33733293: age PND7 rodent versus human infant (the mapping is itself uncertain; 34666787 cites rodent weeks 1-3 against human last trimester to 2-3 years); duration about 4-7.5 h versus days; intensity: mg/kg per injection stated, no equivalence calculation in any paper or here. Verdict: not comparable on duration; age and intensity not determinable.
* 25477370: not determinable; no age, dose, number or route in the bytes held.
* 41618072: not comparable: adult mice, daily bolus i.p., an "abuse" framing; its multi-day duration is the closest.

## 4. Q3 additional evidence needed to claim larger harm in a Wwox-deficient brain (all IPOTESI)
* Oligodendrocytes: compare single-day and multi-day ketamine in neuronal Wwox-deleted and wild-type pups at matched age; Olig2, cleaved caspase-3, MBP and myelinated axon counts, with a recovery time point; test the genotype x ketamine interaction.
* GSK-3beta: measure in vivo p-GSK-3beta (Ser9 stated) in Wwox-null versus wild-type brain after identical exposure; show whether the baseline is already high, so that the ketamine effect is additive, saturating or absent.
* PV interneurons: PV and NPY counts and layer 2/3 GABA release in Wwox KO versus wild-type after ketamine, same region for both genotypes (the two baselines come from hippocampus and neocortex).
* Excitatory drive: mEPSC and sEPSC in the same region and age, in KO with and without neonatal ketamine; check for a ceiling effect.
* Neuroinflammation: microglia, astrocyte and cytokine readouts in KO with and without ketamine, alongside the pyroptosis readouts of 34666787.
* Human: a ketamine-exposed child with biallelic WWOX loss of function compared with exposed non-WWOX children, on validated neurodevelopmental scales; none exists in the sources met.
* Common: a 2 x 2 genotype by exposure design, pre-registered endpoints, sex reported, exposure matched to a defined paediatric regimen. This is not a recommendation.

## 5. Q4 human infant or child neurotoxicity from ketamine (abstract depth)
| PMID | Design | Quote | Limits |
|---|---|---|---|
| 24659739 | prospective, preliminary; infants with 1-3 ketamine anaesthetics for facial laser surgery | "Bayley Scales of Infant Development-Second Edition scores after the last procedure were lower than those before the first surgery in the Ket(3) group (P < .05)"; "Our results suggest that 3 or more exposures to anesthetic ketamine have the potential to adversely affect neurodevelopment in infants." | no unexposed comparator stated; small; sample size not read |
| 37440275 | retrospective; infants with congenital heart disease | "each mg/kg increase in ketamine exposure was associated with a 0.34 (95% CI, -0.64 to -0.05) point decrease in Bayley III motor scores (P = 0.024)" | observational; confounded by disease |
| 21507125 | prospective follow-up; infant cardiac surgery | "no evidence of an association between dose and duration of sedation/analgesia drugs ... and adverse neurodevelopmental outcomes" | ketamine is one of five drug classes |
| 38762850 | prospective PICU cohort | "Delirium occurred in 16 (22%) patients with ketamine and 15 (7.6%) patients without ketamine (p = 0.006)" | acute delirium, not neurotoxicity |
| 40926573 | review | "Animal studies have found that repeated or high-dose subanesthetic ketamine administration results in consistent excitotoxic neuronal damage and lasting cognitive deficits, especially in perinatal animals" | no paediatric neurodevelopment data in the abstract |
| 42850468 | lactation systematic review | "No study measured infant plasma concentrations or long-term neurodevelopment." | not treatment exposure |

* Absence claim: no source met reports ketamine neurotoxicity in infants or children with WWOX loss of function, or in status-epilepticus infusion cohorts. Routes: three PubMed queries (82, 43 and 7 hits; titles screened for 46 distinct PMIDs) and the Kuki abstract. Only the first page of the two large searches was screened and the second route is thin (no registry or full-text search): provisional.

## 6. Limits
42808560, 25477370 and 33733293 read at abstract depth only; 33914858, 30290271 and 38461760 also abstract-only but the quoted phrases were found there. Text extracted by tag stripping; quotes checked against the saved bytes. No dose, schedule or recommendation is given; the mg/kg values only describe what each study did.

## Files (/tmp/it56_ket/p3_collision/)
COLLISION_PAPERS.tsv, SOURCES.tsv, SEARCHES.tsv, totext.py, txt/, sources/ (the three BLOCKED_* files are challenge pages, kept as evidence of the block).

**Update 2026-11-17 (IT; after blind verification of sampled rows):** corrections for this package are in `../CORRECTIONS_AFTER_BLIND_VERIFICATION_IT_20261117.md`; the text above is unchanged.
