# Repurposing batch, group R2, relay b (scientist-b, 2026-10-22)

> Public edition, disease-level, de-identified. Every paper below is **NOT WWOX EVIDENCE** unless it is marked WWOX-DIRECT. Class-level only: no dose, no administration recommendation, no paediatric suitability is presumed. Nothing here is medical advice. Task `REPURP-10H-R2b-B-20261022`; continues `repurposing_10h_scientist-b_20261021.md` (sections 0 to 29), whose conclusion stands with its qualifiers and is not restated or moved: the ethosuximide genotype contrast (DL-MECH-170) is plausible as a category but NOT established for Wwox; it rests on the late phase of a six-animal null arm; the two PTZ-alone null control cohorts differ by a comparable order to the drug effect; there is no interaction test; an ethosuximide effect does not imply T-type excess; seizure suppression is symptomatic in every paper that looks.

## 0. What this relay did, in one table

| PMID / id | Paper | Depth | Receipt (staged) | Manifest | Verdict for the lead |
|---|---|---|---|---|---|
| 34483921 | Iizumi 2021, GluA1 C811S mouse, phenytoin and trimethadione | partial, Results in full, Fig 2 read as an image | FTR-20261022-34483921-01 | PASS | **the missing kind of experiment exists, in another mutant, and runs opposite** (section 1) |
| 30175250 | Ogiwara 2018, Scn2a haplodeficiency | partial, ethosuximide spans, Fig 5 image | FTR-20261022-30175250-01 | PASS | abstract reaches further than the body (section 2) |
| 32678276 | Jin 2020, aged APP/PS1 mice, SWDs and drugs | partial, Methods and Results, Fig 4 image | FTR-20261022-32678276-01 | PASS | an effect "restricted" to one state beside a halved, unstarred mean (section 3) |
| 27616982 | Aguado 2016, Cav3.1 and Cav3.2 ontogeny, mouse | partial, Fig 3 image | FTR-20261022-27616982-01 | PASS | age window of T-type protein; text and panel disagree for thalamus (section 4) |
| 32751129 | Bouron 2020, Ca2+ transport transcripts in embryonic cortex | targeted, Methods and 3.1.1 | FTR-20261022-32751129-01 | PASS | T-type genes are the dominant calcium-channel transcripts E11 to PN1 (section 5) |
| GSE158681, GSE158682 | Wwox null and neuronal-deletion RNA-seq, P17, public deposits | dataset, no receipt | none (a dataset, see 6) | n/a | **WWOX-DIRECT**: T-type transcripts lower, not higher (section 6) |

Five readings plus one dataset reading, against a cap of twelve. Parked or not opened: section 7. Searches and what their zeros license: section 8. Two leads staged (not numbered): `lead_trimethadione`, `lead_wwox_ttype_mrna`. The R2 commit candidate and the R2 manifests are untouched.

## 1. PMID 34483921 (Iizumi 2021): phenytoin and trimethadione in a palmitoylation-deficient AMPA-receptor mutant mouse. NOT WWOX EVIDENCE

**Question written before opening:** does any developmental or genetic model report a drug-by-genotype interaction test for a T-type-class blocker, and in which direction?

**What the paper establishes (DATO, from the printed numbers).** Adult wild-type and GluA1 C811S mice, PTZ provocation, Racine score 0 to 6. Vehicle: wild type 4.86 +/- 0.14 (n = 14), mutant 4.90 +/- 0.07 (n = 20), p = 0.8575, so a ceiling in both. Trimethadione: wild type 1.43 +/- 0.37 (n = 7), mutant 4.00 +/- 0.82 (n = 6); genotype x treatment interaction F(1,43) = 20.43. Phenytoin: wild type 2.70 +/- 0.33 (n = 12), mutant 4.58 +/- 0.23 (n = 12); interaction F(1,54) = 26.22. For the AMPA antagonist the interaction was not significant (F(3,61) = 2.157, p = 0.1023, first dose series). The mechanism label for trimethadione (T-type inhibition) is a citation; no current was measured.

**Recomputed from the printed means, SEMs and Ns (pooled-variance two-way contrast):** trimethadione F(1,43) = 20.4, which reproduces the printed 20.43; phenytoin F(1,54) = 23.7 against 26.22 printed, which does not reproduce exactly (direction and significance unaffected). An unequal-variance (Welch-type) z for the trimethadione contrast is 2.8, because the cell SDs run from about 0.3 (mutant vehicle) to about 2.0 (mutant drug); the pooled test is the more favourable. Ordinal scores analysed as continuous, as in the paper.

**Surfaces looked at.** Methods (statistics, ages: 3 months for these two drugs), every Results section, Figures 1 and 3 captions, and Figure 2 as an image (points are integer scores and were read individually: wild-type trimethadione 3, 2, 2, 1, 1, 1, 0; mutant 6, 5, 5, 2, 1 plus a sixth inferred at 5 from the printed mean). The vehicle means and Ns printed for phenytoin and trimethadione are identical (4.86 +/- 0.14, n = 14; 4.90 +/- 0.07, n = 20), so the two drug experiments share one vehicle control group (whether it was run concurrently is not stated); the AMPA-antagonist series printed different vehicle values, so controls were not shared across all experiments. The Discussion was not read past its first paragraphs (receipt says so).

**What it says about DL-MECH-170 (INFERENZA).**
1. The experiment the lead's falsifier asks for, a drug-by-genotype interaction test with a T-type-class drug on a PTZ endpoint, has been run and reported, in a different mutant, and an interaction was detectable at group sizes of 6 to 20 on a ceiling-limited ordinal score. That makes the Wwox design feasible at that size, which section 23 of the earlier note had sized at about 15 per cell on a different footing.
2. Its direction is opposite to the lead: the mutant lost the blocker's effect. So "a hyperexcitable genotype shows more T-type-blocker effect" is not a general rule, and the Wwox contrast cannot borrow plausibility from hyperexcitability alone. The lead's own direction (effect present in the null, absent in wild type) needs a reason specific to Wwox.
3. A ceiling in both vehicle groups is a design feature that produces an interaction without any change in target biology; the Wwox arm has the reverse problem (a floor in wild type, noted in the earlier note, section 9).
4. It does not test ethosuximide, a succinimide; trimethadione is a different chemical class, so the lead's second falsifier clause (a different-class T-type blocker showing no genotype dependence) is not decided either way by a different mutant.

**Not supported.** Nothing about Wwox, about T-type current, about spontaneous seizures, or about development; one adult male-only cohort. **Uniqueness (a negative claim): where I looked.** PubMed title/abstract queries of 2026-10-22 for ethosuximide or T-type blocker x knockout, knock-in or mutant x wild-type or littermate x interaction or two-way (zero to nine hits, none other with an interaction test in the abstract), and a Europe PMC full-text query for genotype-by-treatment wording with a T-type or ethosuximide term (28 hits, titles screened; the epilepsy-model titles among them were not all opened). The licence is "no other such paper found in those queries", not "none exists" (D-37: full text does not reach supplementary tables).

## 2. PMID 30175250 (Ogiwara 2018): Nav1.2 haplodeficiency and ethosuximide-sensitive absence-like seizures. NOT WWOX EVIDENCE

Screened earlier as "ethosuximide only in the mutant arm"; read now for the claim itself.

**Established (DATO).** Heterozygous knock-out and RX knock-in mice show spike-wave discharges at adult stages; a conditional heterozygous deletion in dorsal-telencephalic excitatory neurons (Emx1-Cre) reproduces them at about a tenfold higher rate than the RX line, and the inhibitory-neuron deletion does not. The only ethosuximide experiment is in the conditional line: vehicle versus ethosuximide within animals, t(5) = 5.683, P = 0.0024, N = 6 (Figure 5f read as an image: vehicle about 35 events per 2.5 h, individual points about 8 to 60, ethosuximide about 1 to 2).

**The finding that matters for the lead's evidence standard.** The abstract says both the knock-out and the RX knock-in mice "exhibit ethosuximide-sensitive" seizures, and the Discussion opens "Here we demonstrated ethosuximide-sensitive absence-like seizures ... in mice heterozygous for ... RX". A text search of the persisted XML finds ethosuximide in seven places (abstract, Figure 5 legend, two sentences of Results, two in the Discussion, Methods) and **none ties a drug test to the knock-out or RX lines**; the 21-page supplementary PDF returns no hit for the drug (its text layer is live: the same search finds other terms). So the abstract and Discussion claim reach one step beyond the body that was read. I cannot say the drug test was not run (it may be in the earlier paper cited for the knock-out line, not read); I can say it is not in this paper's body, legends or supplement. This is the same shape as the earlier note's finding for Cheng 2020: a statement stronger than the panel that carries it.

**Design limits relevant to a genotype contrast.** Paired vehicle-drug design, no control-genotype drug arm (the control littermates show close to no events, so a wild-type drug arm would have been uninformative: a floor); single time window, adult; the Results text says recordings at 6 to 8 weeks, the legend says over 8 weeks (internal inconsistency in the age statement, recorded as two locators). Age: nothing tested below 6 weeks. The Discussion cites, as the authors' own earlier report, that a Cacna1a deletion in layer VI cells raised T-type current in relay neurons; that precedent is cited, not measured here, and its source (Bomben 2016) is parked (section 7).

## 3. PMID 32678276 (Jin 2020): aged APP/PS1 mice, SWD response to ethosuximide, levetiracetam and others. NOT WWOX EVIDENCE

**Established.** Eleven 17- to 18-month-old male mice, every compound given to every animal in random order with a one-week washout and two saline sessions, double-blinded preparation; the two saline sessions did not differ on any parameter (paired t-test, p > 0.05), so the first was used. Ethosuximide (N = 8, Table 1) reduced SWD number and duration only in the "mixed" behavioural state (Figure 4 read as an image: saline about 108 against about 17, starred), with saline about 88 against about 40 in waking immobility and about 128 against about 115 in sleep, both unstarred.

**Why it is useful here (INFERENZA).** The authors describe the drug as "neutral in sleep and waking immobility". The waking-immobility bar is roughly halved and unstarred at N = 8: a restricted *significance* beside a large point difference, which is the same epistemic situation as the "n.s. in wild type, significant in null" description of the Wwox panel, and the same caution applies: significant in one cell and not in another does not make the effect different between cells (the difference between "significant" and "not significant" is not itself a significance test). The paper adds a second, separate lesson: the apparent site of an effect depends on how the recording is partitioned (state), and sleep scoring is flagged by the authors as unreliable for SWDs because of spindles. A "late phase only" reading in the Wwox null is exposed to the same partitioning problem.

**Not supported.** No wild-type arm (SWDs are rare in wild type); one dose; mechanism (T-type) asserted by citation. Not read: Introduction and most of the Discussion (receipt says so).

## 4. PMID 27616982 (Aguado 2016): Cav3.1 and Cav3.2 protein by region and postnatal age, mouse. NOT WWOX EVIDENCE

**Question written before opening:** at which postnatal ages is T-type protein present, and where? (The age window is unmeasured in every R2 paper; the Wwox ethosuximide assay is labelled preweaning in the R2 manifest of 32000863; I did not re-verify the exact age.)

**Established (DATO, histoblots, n = 3 per age group per the Methods, ages P0, P5, P10, P15, P21, P60, P90).** Cav3.1 is present from P0. Figure 3B read as an image: thalamus pixel density about 3 (P0), 5 (P5), 14 (P10), 16 (P15), 23 (P21), 27 (P60), still highest at P60; cerebellar molecular layer peaking at about 70 at P21. Hippocampal Cav3.1 changes little. Hippocampal Cav3.2 rises to a P21 peak and falls at P60 (text and caption). So in the thalamus, the structure that matters to absence-type circuits, Cav3.1 protein at about P5 to P10 is about a fifth to a half of its adult-range value on this scale (about 5 and 14 of 27, approximate, whole thalamus not the reticular nucleus).

**Internal disagreement, declared as a locator.** The Results text says the thalamic Cav3.1 pattern is "similar" to the cerebellar one (peak at P21, slight decrease at P60); the Figure 3 legend and the panel show a progressive rise to P60 in the thalamus. The panel is the measurement; the text is the loose description. The Methods give n = 3 per group; the legend says four independent experiments averaged; the P90 group listed in Methods does not appear in the panels read. Antibody specificity for Cav3.2 was checked with Cav3.2-knockout tissue; no such control is described for Cav3.1 in the text read.

**For the lead (INFERENZA).** If the Wwox ethosuximide assay ran at preweaning ages, the thalamic Cav3.1 protein pool at that age is a fraction of the adult pool; this is a plausibility consideration for any T-type-dependent effect at that age, not evidence for or against one, and ethosuximide sensitivity by age was not measured in this or any paper read. Whole-brain histoblot on protein, one strain.

## 5. PMID 32751129 (Bouron 2020): transcripts of calcium-transport genes during embryonic cortex formation, mouse. NOT WWOX EVIDENCE

Targeted reading (Methods and 3.1.1). Cacna1g and Cacna1h were the only voltage-gated calcium channel genes expressed at all time points and the most expressed of the family (TPM about 10 to about 35); Cacna1g was the major one at E11 and E13, Cacna1h predominated at E17 and PN1 and rose about tenfold from E11 to PN1; Cacna1i was not detected at E11 and E13. The window stops at PN1 (no postnatal weeks), the RNA-seq methods are not described in the sections read (a GEO accession is given), replicate number per age is therefore unknown to me. Useful only as the embryonic anchor of the T-type age curve of section 4; it gives no drug or genotype information.

## 6. WWOX-DIRECT: Wwox-null and neuronal-deletion brain RNA-seq at P17 (GEO GSE158681, GSE158682)

**How found.** A GEO DataSets search for Wwox with brain terms (2026-10-22) lists GSE158681 (hippocampus; null KO n = 2 vs WT n = 3; Syn-Cre deletion n = 3 vs 2; Nestin-Cre deletion n = 2 vs 2; P17), GSE158682 (cortex, Syn-Cre deletion n = 3 vs 4), GSE158684 (hippocampal single-nucleus, Syn-Cre deletion, about 2,900 and 3,200 nuclei) and the P47T series GSE215425 (listed, not opened here). The contributor names and summary match the Aqeilan-laboratory neuronal-deletion work; the deposits carry no PubMed link and the summary merges two papers' abstracts, so **I tie the data to the laboratory, not to one PMID, and stage no receipt** (a dataset is not a paper reading; the Brain paper has its own receipts, and its artefacts are absent from this host).

**What I did.** Downloaded the two TPM tables (digests in the lead record), summed transcript TPM per gene over the transcripts that match a current Ensembl lookup (Cacna1g 16 of 16, Cacna1i 6 of 6, Cacna1h 8 of 15, Wwox 9 of 27: a partial mapping, so gene sums are comparable across samples, not across genes), and compared group means. Wwox falls to 0.06 to 0.32 of control in the deletion lines, which is the positive control. No differential-expression test was run (n = 2 per group does not support one).

| Comparison (mutant / control, group-mean ratio) | Cacna1g | Cacna1h | Cacna1i |
|---|---|---|---|
| hippocampus, Wwox null vs wild type (2 v 3) | 0.73 | 0.47 | 0.50 |
| hippocampus, Syn-Cre deletion (3 v 2) | 1.06 | 0.73 | 0.46 |
| hippocampus, Nestin-Cre deletion (2 v 2) | 0.49 | 0.90 | 0.33 |
| cortex, Syn-Cre deletion (3 v 4) | 0.82 | 0.92 | 0.52 |

**Reading (INFERENZA).** Cacna1i is lower in all four comparisons; Cacna1h is lower in the hippocampus; Cacna1g has no consistent direction and is not up. This does not reproduce the P47T knock-in observation of the earlier note (adult hippocampus, Cacna1g up, Cacna1h down) for Cacna1g, and agrees with it for Cacna1h. These are mRNA levels in whole tissue at one age; they say nothing on current density and are exposed to cell-composition effects (interneuron and oligodendrocyte populations are reported reduced in these models by other papers), so they cannot be read as "no T-type excess in neurons". They remove one hoped-for datum: the lead does not get support from transcript direction at P17. Thalamus and reticular nucleus, where the absence-type circuit lives, are not in these deposits.

## 7. Parked, not opened, and the cascade run

- **PPR862391 (Shalomov 2024 preprint, ethosuximide as a subunit- and G-beta-gamma-dependent GIRK blocker).** Europe PMC core record: open access flagged, no PMCID; Europe PMC full-text endpoint HTTP 500; its repository file endpoint 403; the bioRxiv full text, JATS source and PDF HTTP 429 (rate limit; not retried in a loop, no challenge solved). The published version (Br J Pharmacol, with a correction notice after it) is not open. **Abstract only, not evidence:** it reports that the potency of ethosuximide block depends on the G-protein beta-gamma subunits and on channel gating, and that the apparent affinity is highly sensitive to mutations that change gating. That is a candidate non-T-type route by which an ethosuximide effect could be genotype-dependent; whether that applies to anything in Wwox is untested. Recorded as a gap, not a finding.
- **26758833 (Bomben 2016, layer VI Cacna1a deletion, raised T-type current in thalamic neurons, ethosuximide-sensitive seizures).** PMC XML is a restricted stub (publisher disallows XML); Europe PMC PDF render 403; the PMC PDF address returns a 1.8 kB HTML page, not a PDF. Parked; abstract only.
- **41187802 (prenatal valproate model, Cav3.2 and allodynia; control-versus-model blocker comparison), 22589250 (LGI1 rat, ethosuximide; open access via a publisher PDF that returned 403), 31953800 (neonatal sevoflurane, T-type, PMC XML restricted stub).** Parked on lawful access; none solved by a challenge.
- **39637158.** A review, as screened earlier; not opened (no primary datum a review could add to the lead beyond the primary papers).
- **Four Europe PMC WWOX x T-type hits (two organoid or network reviews, a precision-therapy review, a Turkish DEE cohort).** Title-screened only; the cohort paper is gene-list material of the kind the earlier note already treated with the Kilic cohort. Not opened; no claim made from them.

## 8. Searches of 2026-10-22 and what their zeros license (D-37)

PubMed title/abstract: (a) WWOX x T-type or Cav3 or Cacna1g/h or low-voltage-activated or calcium current: one hit, a clinical cohort already in the repository. (b) ethosuximide x knockout or knock-in or mutant x wild-type or littermates x interaction or two-way: zero. (c) the same without the interaction words: nine, of which three were already read in R2, two are read here, one is parked, and three are old or off-topic. (d) T-type blocker or ethosuximide x knockout or mutant plus a list of epilepsy genes: two records, the same already-read paper twice. (e) ethosuximide x neonatal, juvenile or developing x age-dependent: zero. These zeros license only "no paper is indexed in those queries by title or abstract"; full text does not reach supplementary tables, and a drug-by-genotype test may sit in a methods paragraph. Europe PMC full-text queries returned 28 (genotype-by-treatment wording) and 252 (T-type or ethosuximide x age x interaction x mutant) records, titles screened, three chosen for reading. No paper was found that reports ethosuximide sensitivity by age; the age question remains unmeasured in everything read.

## 9. Effect on DL-MECH-170, stated narrowly

Nothing here narrows or removes the lead, and nothing promotes it. What changes:

1. **The missing falsifier is more concrete.** A genotype x treatment interaction test with a T-type-class drug on a PTZ score exists in another mutant (section 1); it was detectable at 6 to 20 per cell, ran the other way, and rested on a ceiling.
2. **Two pressures on the lead's mechanism, neither decisive.** The one WWOX-direct T-type measurement added here (section 6) is mRNA, lower or flat, not higher; the one non-T-type route found for ethosuximide (GIRK gating dependence, abstract only) is a rival for any genotype-dependent ethosuximide effect.
3. **Two reminders about the evidence standard.** Statements in an abstract can run ahead of the body (section 2), and "restricted" effects may be a significance threshold falling between two large point estimates (section 3).
4. **The age window stays open.** T-type protein in thalamus is low at P5 to P10 and rising to the adult range by P21 to P60 (section 4); no paper ran one drug at two ages.

**Owed.** The claims in sections 1 to 3 that bear on the lead are not blind-audited: a locator audit by someone else (rule 9) is OWED for the manifests of 34483921, 30175250 and 32678276 before any of them is cited in a commit candidate. No commit candidate is written here; the held R2 candidate is not edited.

## 10. Defaults taken (also in the task JSON)

GEO TPM tables read as data without a receipt (identity link only by contributor and summary); bioRxiv rate-limit and publisher bot checks not circumvented; a partial transcript mapping accepted and declared rather than rebuilt with an older annotation; no differential-expression statistic computed on n = 2; coverage values understated where a paragraph was printed truncated.
