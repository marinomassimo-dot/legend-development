# RP-005 / ADV-109: SCORER SHEET, a TRUTH TABLE to fill (IT, 2026-11-20; hypothesis level; no dose, no recommendation; reference genotype class only; not medical advice)

For SCI. **You see no prediction of any arm.** The predictions of all arms are sealed in one file whose SHA-256 is `79c45decb7a3d328a996884a6fe20680704c41d04340685d3149bb0969dc3cd9`; the file is committed only after your truth table is on main, and IT computes every hit mechanically against your table. Read THIS file only (do not open the pre-registration `PREREG_RP005_ADV109_IT_20261120.md` beyond what is copied here: its later sections hold the predictions). Nobody has read the three bodies for this test; the abstracts below were read by IT and HE.

## Your task
For each of the 28 slots, read the full text named and report the **true option letter** the body supports, with a quoted sentence (verbatim) and a locator (section plus the opening words of the paragraph, or table or figure legend title). Rules:
* If the body does not settle the slot, or only in a figure or table cell you cannot read, write `NOT DETERMINABLE` and say why.
* `OTHER / NOT REPORTED` options are chosen only after you searched the body, legends, methods and table titles, and you say what you searched ('found by these routes'; never 'the paper does not').
* Where an option is ambiguous or two options both fit, give the option you think best and a SECOND reading (which letter under the other reading). The first stays primary.
* If a text cannot be obtained when you try, write `TEXT NOT OBTAINABLE` for all its slots, say which route failed and stop; do not substitute another route, do not retry after a reCAPTCHA page (a stop), do not use an aggregator, do not send any contact address.
* One plain request per route, no bursts, generic client name, no contact parameter. Do not record a receipt unless you read the whole text and the usual rules for a complete read are met; this is a scoring pass, not a receipt.
* Add, per text, a short list of ambiguities you met (as in ADV-106). Do not guess the arms; there is nothing to guess from.
Commit your file as `TRUTH_TABLE_RP005_ADV109_SCI_20261120.md` in this folder.

## Routes (status-checked by IT on 2026-11-20 without reading content)
| Text | Route | Status when checked |
|---|---|---|
| T1 Guo 2009 (PMID 18509642) | PMC article page https://pmc.ncbi.nlm.nih.gov/articles/PMC2752825/ | HTTP 200, 187 KB |
| T2 Masicampo 2018 (PMID 29912275) | PMC article page https://pmc.ncbi.nlm.nih.gov/articles/PMC6104618/ | HTTP 200, 174 KB, 53 paragraph tags, 3 figures, on the SECOND request (the first returned a 21 KB reCAPTCHA page; the route is intermittent) |
| T3 Walters 2019 (PMID 30631446) | NCBI efetch, keyless: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=6321982&rettype=xml | HTTP 200, 120 KB, body present, 12 figures, 1 table; the PMC article page returned a reCAPTCHA page for IT (a stop) |

## Abstract coverage (what the slots exclude)

## T1 (Guo 2009, 10058-F4 in mice)
**Abstract as read by IT (the slots below ask for what it does not give):**

> Title: Efficacy, pharmacokinetics, tissue distribution, and metabolism of the Myc-Max disruptor, 10058-F4 [Z,E]-5-[4-ethylbenzylidine]-2-thioxothiazolidin-4-one, in mice. (Cancer Chemother Pharmacol 2009)
> Abstract: c-Myc is commonly activated in many human tumors and is functionally important in cellular proliferation, differentiation, apoptosis and cell cycle progression. The activity of c-Myc requires noncovalent interaction with its client protein Max. In vitro studies indicate the thioxothiazolidinone, 10058-F4, inhibits c-Myc/Max dimerization. In this study, we report the efficacy, pharmacokinetics and metabolism of this novel protein-protein disruptor in mice. SCID mice bearing DU145 or PC-3 human prostate cancer xenografts were treated with either 20 or 30 mg/kg 10058-F4 on a qdx5 schedule for 2 weeks for efficacy studies. For pharmacokinetics and metabolism studies, mice bearing PC-3 or DU145 xenografts were treated with 20 mg/kg of 10058-F4 i.v. Plasma and tissues were collected 5-1440 min after dosing. The concentration of 10058-F4 in plasma and tissues was determined by HPLC, and metabolites were characterized by LC-MS/MS. Following a single iv dose, peak plasma 10058-F4 concentrations of approximately 300 muM were seen at 5 min and declined to below the detection limit at 360 min. Plasma concentration versus time data were best approximated by a two-compartment, open, linear model. The highest tissue concentrations of 10058-F4 were found in fat, lung, liver, and kidney. Peak tumor concentrations of 10058-F4 were at least tenfold lower than peak plasma concentrations. Eight metabolites of 10058-F4 were identified in plasma, liver, and kidney. The terminal half-life of 10058-F4 was approximately 1 h, and the volume of distribution was >200 ml/kg. No significant inhibition of tumor growth was seen after i.v. treatment of mice with either 20 or 30 mg/kg 10058-F4. The lack of significant antitumor activity of 10058-F4 in tumor-bearing mice may have resulted from its rapid metabolism and low concentration in tumors.
> 

**Slots and options:**

| Slot | Question | Options |
|---|---|---|
| T1-S1 | Is brain among the tissues analysed, and is a number reported for it? | A analysed and a numeric concentration reported at at least one time point; B analysed and reported only as below the limit of quantification at every time; C brain not named among the tissues analysed; D OTHER / NOT REPORTED |
| T1-S2 | Metabolite assignments | A at least one metabolite is assigned (confirmed or tentative) as a glucuronide, sulfate or glutathione conjugate; B all assigned metabolites are phase I (oxidation, hydrolysis, de-alkylation) products; C metabolite structures not assigned or not reported |
| T1-S3 | Cell-line potency for DU145 or PC-3 proliferation (use the DU145 or PC-3 value; if both are given, the lower) | A under 10 micromolar; B from 10 up to and including 100 micromolar; C over 100 micromolar; D no DU145 or PC-3 value in the paper (other lines only, a range spanning two bands, or none) / NOT REPORTED |
| T1-S4 | Plasma protein binding (any plasma species) | A measured and above 90 percent bound; B measured and 90 percent or less; C OTHER / NOT MEASURED / NOT REPORTED (in this study's own samples) |
| T1-S5 | Age of the mice (AGE RULE: use the stated range; if it straddles a band edge choose the band holding its midpoint; if only weight or only 'adult' is given, D) | A under 6 weeks; B 6 to 10 weeks; C over 10 weeks; D OTHER / NOT REPORTED |
| T1-S6 | Vehicle for intravenous dosing | A the vehicle names DMSO; B cyclodextrin or lipid emulsion; C aqueous (saline, PBS or water) with no organic solvent; D any other organic vehicle (PEG, ethanol, Tween or Cremophor without DMSO) or not reported |
| T1-S7 | Tolerability at the 30 mg/kg efficacy dose | A the paper states no body-weight loss and no toxicity for the 30 mg/kg arm (or both arms combined); B the paper reports any body-weight loss, death or other toxicity at 30 mg/kg (if both statements appear, B); C tolerability not described |
| T1-S8 | Which of fat, lung, liver and kidney had the highest peak tissue concentration, per gram of tissue, in the main tissue table (the abstract gives the set of four, not the order) | A fat; B lung; C liver; D kidney; E OTHER / NOT REPORTED (including two tissues within the reported error with no value highest) |
| T1-S9 | Peak tumour concentration, DU145 compared with PC-3 (ratio of the two lines' peak values) | A ratio 2.0 or less in either direction; B ratio above 2.0; C only one line has a tumour concentration, or no numerical values |

**Your truth table for T1:**

| Slot | True option | Second reading (if any) | Quoted sentence | Locator | Searched (for OTHER / NOT REPORTED) |
|---|---|---|---|---|---|
| T1-S1 |  |  |  |  |  |
| T1-S2 |  |  |  |  |  |
| T1-S3 |  |  |  |  |  |
| T1-S4 |  |  |  |  |  |
| T1-S5 |  |  |  |  |  |
| T1-S6 |  |  |  |  |  |
| T1-S7 |  |  |  |  |  |
| T1-S8 |  |  |  |  |  |
| T1-S9 |  |  |  |  |  |

## T2 (Masicampo 2018, TTA-P2 in withdrawal seizures)
**Abstract as read by IT (the slots below ask for what it does not give):**

> Title: Selective Blockade of T-Type Ca2+ Channels is Protective Against Alcohol-Withdrawal Induced Seizure and Mortality. (Alcohol Alcohol 2018)
> Abstract: We have previously demonstrated that blockade of T-type calcium channels by the non-selective antagonist, ethosuximide (ETX), is effective at reducing electrographical and behavioral correlates of alcohol-withdrawal (WD) seizure. Here, we investigated whether blockade of these calcium channels with the selective antagonist TTA-P2 also reduces alcohol-WD seizure. The non-specific T-type calcium channel antagonist, ETX, is protective against alcohol-WD seizure. However, the mechanism of this effect is unclear. Here, we provide evidence that further suggests selective blockade of T-type calcium channels are protective against alcohol-WD seizure and WD-related mortality. We used an intermittent ethanol exposure model to produce WD-induced hyperexcitability in DBA/2 J mice. Seizure severity was intensified with the chemoconvulsant pentylenetetrazole (PTZ). TTA-P2 (10 mg/kg) reduced seizure severity in mice undergoing alcohol WD with concurrent PTZ treatment (20 mg/kg). Moreover, TTA-P2 (20 and 40 mg/kg) was also protective against PTZ-induced (40 mg/kg) seizure and mortality. These results are consistent with prior results using ETX and suggest that the protective effects of ETX and TTA-P2 against EtOH WD seizures are mediated by T-type calcium channels.
> Indexing terms: Male; Mice, Inbred DBA.
> 

**Slots and options:**

| Slot | Question | Options |
|---|---|---|
| T2-S1 | Route of TTA-P2 administration in the main seizure experiments | A intraperitoneal; B subcutaneous; C oral; D OTHER / NOT REPORTED (including more than one route) |
| T2-S2 | Interval between TTA-P2 and PTZ in the 10 mg/kg withdrawal experiment | A 15 minutes or less; B 16 to 45 minutes; C 46 minutes or more; D OTHER / NOT REPORTED (including an interval that differs between experiments with none stated for that one) |
| T2-S3 | TTA-P2 alone (no PTZ): effect on locomotion, motor coordination or sedation | A any reduction in locomotion, activity, motor coordination or sedation at any TTA-P2 dose tested alone; B TTA-P2 alone tested and no such reduction reported; C not tested, or an increase only, or not reported |
| T2-S4 | Ethanol exposure method | A vapour chamber (with or without pyrazole); B intraperitoneal ethanol injections as the sole route; C liquid diet or gavage; D OTHER / NOT REPORTED |
| T2-S5 | Number of separate exposure-then-withdrawal periods before testing (count days as cycles only if the paper itself calls them cycles) | A one or two; B three or four; C five or more; D OTHER / NOT REPORTED |
| T2-S6 | Seizure severity scoring | A a scale named Racine or described as a modification of Racine; B any other named or described behavioural scale, including handling-induced convulsion; C EEG-based scoring; D NOT REPORTED |
| T2-S7 | Was TTA-P2 at 10 mg/kg tested against PTZ 40 mg/kg in mice without ethanol withdrawal? 'Protective' means a reduction in severity or mortality versus vehicle that the authors call significant | A tested and protective; B tested and not protective; C not tested, or only other doses (such as 20 and 40) reported, or not reported |
| T2-S8 | Percentage of vehicle-treated non-withdrawal mice that died at PTZ 40 mg/kg within the paper's observation window (computed from counts if no percentage is given) | A under 25 percent; B 25 to 75 percent; C over 75 percent; D OTHER / NOT REPORTED (no vehicle mortality, or only a combined value) |
| T2-S9 | Statistical test used for the seizure severity score (if both kinds are used for severity, A) | A a rank-based or ordinal test (Kruskal-Wallis, Mann-Whitney, Dunn, Wilcoxon or similar); B ANOVA or t-test; C OTHER / NOT STATED |
| T2-S10 | Age of the mice (AGE RULE as in T1-S5) | A under 8 weeks; B 8 to 16 weeks; C over 16 weeks; D OTHER / NOT REPORTED |

**Your truth table for T2:**

| Slot | True option | Second reading (if any) | Quoted sentence | Locator | Searched (for OTHER / NOT REPORTED) |
|---|---|---|---|---|---|
| T2-S1 |  |  |  |  |  |
| T2-S2 |  |  |  |  |  |
| T2-S3 |  |  |  |  |  |
| T2-S4 |  |  |  |  |  |
| T2-S5 |  |  |  |  |  |
| T2-S6 |  |  |  |  |  |
| T2-S7 |  |  |  |  |  |
| T2-S8 |  |  |  |  |  |
| T2-S9 |  |  |  |  |  |
| T2-S10 |  |  |  |  |  |

## T3 (Walters 2019, vigabatrin in mice)
**Abstract as read by IT (the slots below ask for what it does not give):**

> Title: Preclinical tissue distribution and metabolic correlations of vigabatrin, an antiepileptic drug associated with potential use-limiting visual field defects. (Pharmacol Res Perspect 2019)
> Abstract: Vigabatrin (VGB; 4-aminohex-5-enoic acid), an antiepileptic irreversibly inactivating GABA transaminase (GABA-T), manifests use-limiting ocular toxicity. Hypothesizing that the active enantiomer of VGB would preferentially accumulate in eye and visual cortex (VC) as one potential mechanism for ocular toxicity, we infused racemic VGB into mice via subcutaneous minipump at 35, 70, and 140 mg/kg/d (n = 6-8 animals/dose) for 12 days. VGB enantiomers, total GABA and beta-alanine (BALA), 4-guanidinobutyrate (4-GBA), and creatine were quantified by mass spectrometry in eye, brain, liver, prefrontal cortex (PFC), and VC. Plasma VGB concentrations increased linearly by dose (3 +/- 0.76 (35 mg/kg/d); 15.1 +/- 1.4 (70 mg/kg/d); 34.6 +/- 3.2 umol/L (140 mg/kg/d); mean +/- SEM) with an S/R ratio of 0.74 +/- 0.02 (n = 14). Steady state tissue/plasma ratios (35, 70 mg/kg/d doses) were highest in eye (5.5 +/- 0.2; P < 0.0001), followed by VC (3.9 +/- 0.4), PFC (3.6 +/- 0.3), liver (2.9 +/- 0.1), and brain (1.5 +/- 0.1; n = 13-14 each). Total VGB content of eye exceeded that of brain, PFC and VC at all doses. High-dose VGB diminished endogenous metabolite production, especially in PFC and VC. GABA significantly increased in all tissues (all doses) except brain; BALA increases were confined to liver and VC; and 4-GBA was prominently increased in brain, PFC and VC (and eye at high dose). Linear correlations between enantiomers and GABA were observed in all tissues, but only in PFC/VC for BALA, 4-GBA, and creatine. Preferential accumulation of the VGB S-isomer in eye and VC may provide new insight into VGB ocular toxicity.
> Indexing terms: Male; Mice, Inbred C57BL.
> 

**Slots and options:**

| Slot | Question | Options |
|---|---|---|
| T3-S1 | Eye-to-plasma concentration ratio (total vigabatrin) at the highest dose compared with the mean of the two lower doses' ratios (the abstract gives only the lower two) | A more than 20 percent above that mean; B within 20 percent of it; C more than 20 percent below it; D OTHER / NOT REPORTED |
| T3-S2 | Brain-to-plasma concentration ratio at the highest dose compared with the mean of the two lower doses' ratios | A more than 20 percent above that mean; B within 20 percent of it; C more than 20 percent below it; D OTHER / NOT REPORTED |
| T3-S3 | Eye sampling | A the eye analysed as one whole sample; B retina analysed as a separate sample; C other ocular dissection (lens, cornea, RPE) without retina, or not reported |
| T3-S4 | Ocular functional or histological readout (ERG, OCT, histology or a visual behavioural test) in this paper's own results | A at least one such result reported; B none, biochemical readouts only; C planned or referred to only |
| T3-S5 | GABA-transaminase enzyme activity measured in this study's own samples | A yes; B no (a cited literature value does not count) |
| T3-S6 | Body weight under vigabatrin | A statistically significant lower body weight than vehicle or the lowest dose at any dose; B the authors state no difference (with or without a test); C weight not reported, or only a non-significant trend described |
| T3-S7 | Age of the mice (AGE RULE as in T1-S5) | A under 8 weeks; B 8 to 16 weeks; C over 16 weeks; D OTHER / NOT REPORTED |
| T3-S8 | Method used to quantify the enantiomers | A chiral derivatisation followed by achiral LC-MS/MS; B a chiral column with MS detection; C GC-MS; D OTHER / NOT REPORTED |
| T3-S9 | Liver S/R enantiomer ratio compared with the plasma ratio | A within 20 percent of the plasma ratio; B more than 20 percent higher S:R; C more than 20 percent lower S:R; D OTHER / NOT REPORTED |

**Your truth table for T3:**

| Slot | True option | Second reading (if any) | Quoted sentence | Locator | Searched (for OTHER / NOT REPORTED) |
|---|---|---|---|---|---|
| T3-S1 |  |  |  |  |  |
| T3-S2 |  |  |  |  |  |
| T3-S3 |  |  |  |  |  |
| T3-S4 |  |  |  |  |  |
| T3-S5 |  |  |  |  |  |
| T3-S6 |  |  |  |  |  |
| T3-S7 |  |  |  |  |  |
| T3-S8 |  |  |  |  |  |
| T3-S9 |  |  |  |  |  |

## Note
The T3 abstract above has the symbols 'S' and 'R' restored by IT: the PubMed text delivered them as blanks. The T3 slots S1, S2 and S9 refer to S/R ratios and tissue/plasma ratios as the abstract uses them.
