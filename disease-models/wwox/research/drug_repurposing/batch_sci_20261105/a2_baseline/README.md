# A2 baseline: symptomatic response versus developmental outcome in IESS and other early-onset DEEs

Scientist `sb-a2`, task `ORCH-SCIBATCH-DR-20261105`, challenge `CH-SB-CONCORDANCE` part 2, 2026-11-05. Corrected on 2026-11-06 after the blind locator audit (`verify/audit_A2/`) and the adversarial review (`verify/review_A/`); every finding and its answer are in `RESPONSE.md`. Non-canonical research material. Not medical advice: no dose, schedule, route or clinical preference is given for any species, and exposures are described qualitatively. Public edition: the subject is the WWOX-DEE reference genotype class, and published cases appear only as group counts. Nothing outside this directory was edited, nothing was committed, and the receipts are staged, not recorded.

Table: `evidence_a2.tsv` (44 rows, 20 columns). Roles: support 20, counter 17, context 7. Here `support` means evidence that a short-term symptomatic response does not by itself carry a developmental gain, or that a responder with poor development is common. `counter` means evidence that the two are coupled, or that treatment choice or timing moves development. The first word of `effect_on_development` gives the direction: favourable 8, adverse 8, null 8, descriptive 15, not_applicable 3, not_measured 2. Depth labels use a closed vocabulary: `abstract_only` (21 rows), `partial_fulltext` (19 rows; the sections read are named in `design_limits`), and `reused_prior_complete_read` (4 rows: three TSC trials that the module read completely and this package did not re-read). No source was read by this package to complete full-text depth.

## 0. Decision (answer first)

1. **DATO.** In the IESS trials that measured both endpoints, no developmental arm difference was demonstrated despite an early difference in spasm cessation of 15 to 19 points: UKISS VABS +1.0 at 14 months (95% CI -4.9 to 7.0) and no significant difference at 4 years; ICISS 73.9 vs 72.7 at 18 months; all read at abstract level. The comparisons had about one chance in four of detecting the difference that full mediation would predict (line 6), so this is an undemonstrated difference, not a shown absence. In TSC, two randomised trials of pre-onset prevention, EPISTOP and PREVeNT (module-held complete reads), changed seizure endpoints without changing development to 36 months. They test prevention before onset, not response after onset, and in PREVeNT the spasm comparison was neither prespecified nor tested (rows A01-A08, C01-C03).
2. **DATO.** Within children, response and development do move together in mixed IESS cohorts. ICISS children with early cessation scored 15.9 VABS points higher (95% CI 12.4 to 19.5; abstract level, where the group sizes 229 and 129 are printed with the seizure outcome rather than with the VABS comparison). None of 61 non-responders reached a favourable outcome in a prospective cohort of 236. A West syndrome cohort reports OR 5.2. A population cohort shows global delay in 82% with drug resistance vs 34% without (rows A09, B01, B05, B07).
3. **DATO.** Responders with poor development are the majority in IESS:
   * 126 of 175 responders (72%, computed from Table 1) were unfavourable at 3 years on Bayley-II (TSC excluded).
   * 40 of 62 (65%) had a social quotient below 55. That source prints 61 responders in its Table 2 and 62 in its Tables 3-4, so the figure is 65% on the larger denominator and about 66% on the smaller if the numerator is unchanged.
   * In an all-comers infant-onset cohort, 13 of 38 (34%) without drug resistance had global delay.

   Rows B02, B06, B08.
4. **DATO.** In genetic strata a favourable outcome is absent whatever the response:
   * None of 49 genetic-aetiology children were favourable at 3 years. This count is over all 49 and is not a responder rate, because the responder count among them is not in the text read.
   * All nine genetic IESS infants had global delay "despite good seizure control in the majority"; most had trisomy 21.
   * In STXBP1-DEE, development did not correlate with age at seizure remission (p 0.64).
   * In Dravet syndrome, DQ/IQ did not correlate with epilepsy variables, apart from seizure type after age 3.
   * A 110-child early-infantile DEE cohort reports profound intellectual disability in most "irrespective of genotype". This is at abstract level, without response-conditional data.

   Rows B03, B08, D01, D03, D04, D14.
5. **INFERENZA.** The coupling depends on the stratum. It is carried by unknown aetiology: the only randomised developmental arm effect is UKISS in infants without an identified aetiology (VABS +9.3 at 14 months and a median +14 at 4 years; abstract level). It is also carried by a normal neurological examination at onset. In genetic and structural strata, a responder with poor development is the expected case, so the WWOX observation in CLAIM 031 (n = 2) is not, by itself, a WWOX-specific feature. The comparison holds only as a binary, favourable or not: the baseline rests on instruments with a cut, and the WWOX reports describe development without a scale (rows A03, A05, B09).
6. **INFERENZA.** The trial nulls are weak evidence of decoupling. If the ICISS person-level association were fully causal, the 15.0-point arm gain in response would predict about 2.4 VABS points (0.150 x 15.9), which lies inside the observed confidence interval. The trial had about one chance in four of detecting it (power 0.24, computed from the reported standard errors). The discriminating evidence is the stratified person-level data (line 4), not the arm nulls (README 1.1).
7. **DATO + INFERENZA.** Development tracks aetiology and baseline neurological status more than treatment arm. Lead time is associated with development in four sources, all read at abstract level, including both trials. In the one source read beyond the abstract, the association was not independent of aetiology and was absent within unknown aetiology (p 0.63). Lead time is therefore a transfer condition whose confounding is unresolved and whose supporting evidence is abstract-level (rows A06, A10, B04, B10, B11).
8. **DATO (counter).** Three genetic-DEE sources link treatment or early severity to development:
   * In a KCNQ2 cohort of 282, the abstract asserts that early sodium channel blocker initiation was associated with better development after adjustment for seizure control by one month. The model cannot be read from the abstract, so the claim is carried as that abstract's own assertion.
   * In Dravet syndrome, longer use of contraindicated medication was associated with worse cognition (abstract only).
   * In Dravet syndrome, baseline epilepsy severity predicted the 10-year adaptive score (p 0.003; read at partial full-text depth).

   Rows D06, D08, D11.
9. **IPOTESI.** In the WWOX-DEE class, symptomatic response leaves the slope of the developmental trajectory unchanged, not only its level. The discriminating test is a within-child continuous score on one instrument before and after response, compared with the genetic-DEE reference slopes above. A cut at 70 cannot test it, because in these strata almost every child is below it.
10. **Consequences fixed in the brief.**
    * Row 1 fires for the genetic and structural strata only. Its condition also requires the arm-level null in the unknown stratum, and rows A03 and A05 record a randomised developmental arm difference there (abstract level). So the base rate is stated with sources (README 1.3), and `INV-10` is reworded as a feature of the genetic and structural strata, not of DEE generally.
    * Row 2 fires: `INV-10` gets transfer conditions for aetiology stratum, baseline neurological status, lead time and instrument.
    * Row 3 does not fire: the association is reported, numerically in five sources and as a null in three (`module_inputs.md`).

## 1. Evidence by theme

### 1.1 Randomised arm contrasts: a symptomatic gain without a demonstrated developmental gain, except in unknown aetiology

UKISS (abstracts only; rows A01-A06): hormonal treatment stopped spasms more often at days 13-14 (73% vs 54%). By the final clinical assessment at 12-14 months, spasm absence was equal (75% vs 76%) and no VABS difference was demonstrated (78.6 vs 77.5). At 4 years, the 77 children traced by a blind telephone VABS showed medians of 60 vs 50 (p 0.091). Among infants with no identified aetiology, development favoured the hormonal arm at both 14 months (88.2 vs 78.9) and 4 years (median 96 vs 63, n 21 vs 16), and the lead-time paper reports a treatment by aetiology interaction.

ICISS (abstracts only; rows A07-A10): the combination arm stopped spasms more often (72% vs 57%). At 18 months no difference was demonstrated in development (73.9 vs 72.7) or epilepsy (30.0% vs 29.2%). A short commentary (row A11, read whole at partial full-text depth) restates these results. In an editorial passage it also says that hormonal-arm non-responders were quickly given vigabatrin and that combination therapy may enhance outcomes. That is the commentators' opinion, not trial data; whether such rescue was part of the protocol is not stated in what I read. If it was, it would dilute the arm contrast. The pooled analysis of hormone types (row A12) is non-discriminating: small, non-significant differences on both endpoints.

The TSC trials were read completely in the module on 2026-10-21 (receipts `FTR-20261021-33180985-01`, `FTR-20261021-37638552-01`, `FTR-20261021-41061327-01`; manifests `disease-models/wwox/research/deepdive_manifests/PMID33180985.json`, `PMID37638552.json`, `PMID41061327.json`). I cite their locators and did not re-read them; their depth label in the table is `reused_prior_complete_read`. Both trials test prevention before onset, not response after onset.

* EPISTOP lowered drug-resistant epilepsy at 2 years in its randomised part (31% vs 77%, p 0.047) and did not change the neurodevelopmental endpoint (row C01).
* PREVeNT found no difference in Bayley-III cognitive or Vineland-II composite at 12 or 24 months. The authors write that delay or prevention of spasms had no measurable effect on cognition. The spasm comparison (hazard ratio 0.263) was not prespecified or tested, and placebo infants received the drug a median of 44 days later (row C02).
* At 36 months there was still no arm difference on the composites (row C03).

The blind audit adds caveats from the tables: EPISTOP's open-label figures differ between text and Table 3, and PREVeNT's 36-month tables print untested drug-resistance counts and an unadjusted Vineland-II subdomain p 0.0495 (rows C01, C03).

How much the arm nulls can say (INFERENZA). Under full mediation, the expected developmental arm difference equals the arm difference in response times the person-level difference in development.

* For ICISS: 0.150 x 15.9 = 2.4 VABS points. The reported confidence interval is -4.9 to 2.6 (sign as printed; combination 1.2 points higher), which contains 2.4. With standard errors of 1.3 and 1.4, the power to detect 2.4 points at two-sided 0.05 is about 0.24.
* For UKISS, borrowing the ICISS association gives 0.189 x 15.9 = 3.0 points, inside -4.9 to 7.0.

Both trials were therefore unable to separate "response causes development" from "response marks a better prognosis". The TSC trials measured development on continuous standard scores, which removes the threshold artefact, but both arms were exposed and the samples were small.

### 1.2 Person-level association: strong, but carried by aetiology and baseline status

* **ICISS** (row A09, abstract): mean VABS 79.1 vs 63.2 by early cessation. The abstract prints the group sizes 229 and 129 with the seizure outcome, not with the VABS comparison. This is an observational contrast inside the trial, not adjusted for aetiology in the abstract.
* **Jang 2026** (rows B01-B04; partial full-text depth; TSC excluded) gives a complete concordance table, computed from Table 1: of 175 responders, 49 were favourable and 126 unfavourable; of 61 non-responders, 0 were favourable. Both aetiology (genetic vs unknown adjusted OR 0.023; structural 0.085) and non-response (adjusted OR 0.030) were independent predictors.
* **Aramanadka 2021** (rows B05-B06; partial full-text depth): structural aetiology in 80%; responders 22 above and 40 below a social quotient of 55, non-responders 5 and 47, OR 5.2. Tables 3-4 count 62 responders where Table 2 prints 61.
* **Jonsson 2024** (rows B07-B09; partial full-text depth; a prospective population cohort of infant-onset epilepsies): global delay in 18 of 22 with drug resistance vs 13 of 38 without (82% vs 34%). Table 2 prints RR 4.2 on this row and on the reverse row; from the cells, the ratio in this direction is 2.4. Cohorts that mix self-limited epilepsies with DEEs inflate this association.

### 1.3 The base rate A1 needs: responders with poor development, by stratum

| Stratum and source (row) | Responder definition | Developmental cut | Responders with poor development |
|---|---|---|---|
| IESS, TSC excluded; Jang 2026 (B02) | no spasms over 24 h and BASED 2 or less | Bayley-II MQ or PMQ below 70 at 3 years | 126 / 175 (72%, computed from Table 1) |
| IESS, genetic, TSC excluded; Jang 2026 (B03) | same | same | all genetic responders, as a bound (0 / 49 favourable over all genetic children, not a responder rate; responder count not in the text read) |
| IESS, structural; Jang 2026 (B03) | same | same | at least all but 3 (3 / 81 favourable overall) |
| West syndrome, structural-predominant; Aramanadka 2021 (B06) | clinical cessation within 14 days, sustained 28 days | social quotient below 55 | 40 / 62 (65%; the source prints 61 responders in Table 2) |
| Infant-onset epilepsies, population based; Jonsson 2024 (B08) | no drug resistance at 24 months | BSID-III below 70 | 13 / 38 (34%) |
| same, abnormal first neurological examination (B09) | same | same | 13 / 16 (81%) |
| same, normal first neurological examination (B09) | same | same | 0 / 22 |
| Genetic IESS, mostly trisomy 21; Jonsson 2024 (B08) | same | same | 7 / 7 (computed from Table 1) |
| ICISS responders (A09, abstract) | cessation days 14-42 | VABS, continuous | mean 79.1, about 1.4 SD below the norm; proportion below 70 not reported |
| KCNQ2, prompt targeted therapy; Jadhav 2026 (D09) | seizure free at 12 months | milestone quotient 69 or less | 4 / 6 |
| KCNQ2 series; Pisano 2015 (D13, abstract) | seizure free in the first year in most | moderate to severe delay | 12 / 15 overall |
| STXBP1-DEE; Balagura 2022 (D01) | seizure freedom | composite score | no difference between remission and active epilepsy; intellectual disability in all aged over 6 |

A 110-child early-infantile DEE cohort with burst suppression (row D14, abstract) reports persistent seizures in 72.5% and profound intellectual disability in most, irrespective of genotype. It gives no count conditional on response, so it enters as context, not as a base rate.

INFERENZA. "Responder with poor development" is the majority outcome in IESS cohorts (65-72%) and the near-universal one in genetic strata at the conventional cuts. It is the minority outcome only when the first neurological examination is normal, or when the aetiology is unknown and the epilepsy self-limited. A WWOX-DEE child who responds and remains profoundly delayed is what the genetic-DEE baseline predicts. That comparison holds as a binary only (section 3, condition 4).

### 1.4 Lead time and age at onset

* **Associated with development**, all four at abstract level:
  * UKISS at 4 years: 3.9 VABS points lower per lead-time category (row A06).
  * ICISS at 18 months: F 6.38, p < 0.001 (row A10).
  * Cryptogenic spasms treated within 1 month: normal cognition 22 of 22 vs 40% (row B10).
  * Hypsarrhythmia lasting over three weeks (row B11).
* **Not independent:** in Jang 2026 (partial full-text depth), lead time was associated univariably but not after adjustment, and not at all within unknown aetiology (p 0.63; row B04).
* **Not testable:** Aramanadka (about 89% treated after 1 month) and Jonsson (too small).
* **Age at onset:** earlier onset was associated with lower VABS in UKISS and with a lower STXBP1 developmental score (p 0.03; row D02).

### 1.5 Other early-onset DEEs (the bounded second axis)

**STXBP1** (rows D01-D02; partial full-text depth). The developmental score did not track age at seizure offset or epilepsy duration. It tracked age at onset, and 46% were impaired before onset.

**Dravet** (rows D03-D07; two sources read at partial full-text depth):
* Nabbout found no correlation between DQ/IQ and epilepsy variables except myoclonic and focal seizures after age 3.
* Nabbout also reports a tendency to a worse psychomotor course in SCN1A-positive cases despite milder epilepsy. The severe-delay contrast is untested, and last DQ/IQ did not differ significantly by genotype.
* Feng found that baseline epilepsy severity predicted the 10-year adaptive score (counter).
* In Feng, the two group-level trends ran in opposite directions, epilepsy improving and adaptive outcome worsening (support). The instrument changed between time points and the authors note a floor effect.

**KCNQ2** (rows D09-D13):
* Prompt targeted therapy gave seizure freedom in 6 of 6, yet 4 of 6 had mild-to-moderate delay. None had severe-profound delay, against 13 of 31 diagnosed later (14 in Table 2). The authors could not determine an effect on development.
* A 282-child cohort asserts in its abstract an association of early sodium channel blocker use with better development after adjustment for seizure control. The model is not readable from the abstract.
* A 44-child cohort (abstract) finds no correlation between age at seizure freedom and development.

**Early-infantile DEE with burst suppression** (D14, abstract; WWOX is among its novel gene associations). The cohort reports persistent seizures and profound intellectual disability irrespective of genotype, without crossing the two.

Summary: development follows genotype and intrinsic severity more than seizure control. It can follow treatment choice where a drug is matched to the channel defect or a contraindicated drug is avoided.

## 2. Counter-evidence (sought on purpose; 17 rows)

Each counter row narrows the support:

* The person-level association is strong (A09, B01, B05, B07, C04).
* Randomised development effects exist in unknown aetiology (A03, A05; abstract level).
* Lead time is associated with development in four sources (A06, A10, B10, B11; all abstract level).
* In TSC, early control is followed by better-than-expected outcomes in one uncontrolled series (C05).
* In Dravet, development is linked to seizure type after age 3 (D04), to baseline epilepsy severity (D06) and to contraindicated medication (D08).
* In KCNQ2, it is linked to early sodium channel blocker use (D10; D11 as an abstract-level assertion).

None of these rows contradicts the base rate in genetic strata (1.3). Two of them (D08, D11) say that treatment choice can move development by a route not captured by seizure control; both are abstract-level.

## 3. Transfer conditions and transfer breakers for reading WWOX-DEE cases

Conditions under which the baseline transfers:

1. **Aetiology stratum.** Decoupling is expected in genetic and structural strata and coupling in unknown aetiology.
2. **Baseline neurological status.** With impairment before or at onset, seizure control barely shifts outcome (B09). CLAIM 031 carries the authors' statement that impairment preceded the epileptic encephalopathy, with the order not shown for both children.
3. **Lead time.** It modifies development in unknown aetiology, but it is confounded by aetiology, and its supporting evidence is abstract-level.
4. **The instrument.** A cut at 70 hides change below it, so continuous standard scores or trajectories are needed (C02, D01). The comparison with WWOX reports, which describe development in narratives without a scale, holds only as a binary (favourable or not); no WWOX rate on a scale exists to compare.

Breakers:

* The arm-level nulls are underpowered (power about 0.24 for the mediated effect), so they are not by themselves evidence of decoupling (line 6).
* TSC trials test prevention before onset, not response after onset.
* KCNQ2 and Dravet have a channel-matched or channel-contraindicated drug; WWOX-DEE has none.
* Development in Dravet is normal before onset.
* The "genetic" IESS group in Jonsson 2024 is mostly trisomy 21.
* Most cohorts are single-centre, retrospective, or lose 28-60% of participants.

## 4. What is not established

* Whether symptomatic response changes the developmental slope in a genetic DEE on a continuous measure, rather than the level at a cut. The continuous data read here are arm-level (PREVeNT) or cross-sectional (STXBP1, Dravet).
* An aetiology-stratified person-level association in ICISS. The aetiology paper (PMID 31418851) is subscription only.
* The number of genetic-aetiology responders in Jang 2026. Figure 3 was not viewed and the supplement was not read.
* Whether the UKISS unknown-aetiology developmental effect is mediated by spasm control. No mediation analysis was found.
* Any WWOX-DEE count. That is package A1, and this package reads none. The adversarial review of A1 finds no sustained, instrumented response in the WWOX record (`verify/review_A/review_A.md` section 2), so the responder this baseline would be compared against is not yet in that record.

## 5. What was not reachable (routes tried; nothing inferred from abstracts beyond what they state)

* UKISS 2004, 2005, 4-year and lead-time reports, and ICISS 2017, 2018 and its 2019 aetiology paper: subscription only per Europe PMC. BMJ and Wiley returned HTTP 403 to a plain client and to WebFetch.
* The Cochrane review and the 2012 guideline: the publisher restricts the PMC text. Europe PMC XML gave HTTP 500, the E-utilities PMC route a stub, and the PubMed tool the abstract only. Both are used as pointers only, and the guideline is flagged retired in its PubMed title.
* KCNQ2 2026 cohort (PMID 42610455): the publisher page shows the abstract only.
* Early-infantile DEE cohort (PMID 42190144): no PMC record; abstract only. The module already holds the same abstract in discovery ledger entries DL-MECH-001, DL-MOL-001 and DL-REPO-001.
* Kivity 2004 and de Lange 2018: Europe PMC lists Wiley PDFs. Not attempted after two Wiley refusals.
* Unpaywall and university repositories were not used: the first needs a contact address, the second is outside the routes listed in the brief.
* Figures: captions only. Supplements: not read.
* Not read, by choice of budget: CDKL5 (PMID 31313283) and SCN8A (PMID 34431999). The brief allows three to four axis-2 primaries.

## 6. Queries run

All are in `queries.tsv`, with their strings, UTC times and hit counts:

* 17 PubMed searches through NCBI E-utilities (Q01-Q17);
* two route tests (Q18-Q19);
* 24 route actions (R01-R24; R23 and R24 are the correction-round look-up of PMID 42190144 and the receipt re-check);
* four repository look-ups (M01-M04).

The core strings:

* the full name of UKISS as a phrase search (Q01, 14 hits; the literal string is kept in `queries.tsv` only, because it contains a country name)
* ICISS (6)
* lead time with development (48)
* `"National Infantile Spasms Consortium"` (12, screened: no developmental outcome endpoint)
* IESS with Vineland, Bayley or developmental quotient and response (19)
* response predicting development (15)
* TSC preventive vigabatrin trials (23)
* Dravet seizure burden and cognition (104)
* STXBP1 (39)
* CDKL5 (56)
* SCN2A, SCN8A, KCNQ2 (44)
* two named Dravet primaries (3)
* the genetic-DEE counter search (49)
* hypsarrhythmia duration (126, too broad; followed by a targeted author search, 3)

Exact PubMed strings (NCBI E-utilities esearch, 2026-11-05, UTC time, hits):

* Q01, 2026-11-05T22:39:33Z, 14 hits: the full trial name of UKISS as a quoted phrase (literal string in `queries.tsv`)
* Q02, 2026-11-05T22:39:34Z, 6 hits: `"infantile spasms" AND vigabatrin AND hormonal AND (ICISS OR "International Collaborative Infantile Spasms Study")`
* Q03, 2026-11-05T22:39:41Z, 48 hits: `("infantile spasms" OR "West syndrome" OR "epileptic spasms") AND ("lead time" OR "treatment lag" OR "treatment delay" OR "time to treatment") AND (development* OR cognit* OR "developmental outcome")`
* Q04, 2026-11-05T22:39:42Z, 12 hits: `"National Infantile Spasms Consortium"`
* Q05, 2026-11-05T22:39:53Z, 19 hits: `("infantile spasms" OR "West syndrome" OR "epileptic spasms") AND (Vineland OR Bayley OR "developmental quotient" OR "Griffiths") AND (cessation OR response OR responder* OR remission OR "spasm freedom" OR "electroclinical")`
* Q06, 2026-11-05T22:39:54Z, 15 hits: `("infantile spasms" OR "West syndrome" OR "epileptic spasms") AND ("spasm cessation" OR "cessation of spasms" OR "response to treatment" OR "electroclinical response") AND ("developmental outcome" OR "neurodevelopmental outcome" OR "cognitive outcome") AND (predict* OR associat* OR correlat*)`
* Q07, 2026-11-05T22:40:02Z, 23 hits: `"tuberous sclerosis" AND vigabatrin AND (preventive OR prevention OR "early treatment" OR presymptomatic OR EPISTOP OR PREVeNT) AND (trial OR randomized OR randomised)`
* Q08, 2026-11-05T22:40:03Z, 30 hits: `"tuberous sclerosis" AND ("infantile spasms" OR "epileptic spasms") AND (vigabatrin) AND (cognit* OR "intellectual" OR "developmental quotient" OR "developmental outcome") AND (early OR delay OR "lead time" OR duration)`
* Q09, 2026-11-05T22:40:15Z, 104 hits: `("Dravet syndrome" OR SCN1A) AND (cognit* OR "developmental quotient" OR "intellectual disability" OR "developmental outcome") AND ("seizure frequency" OR "seizure control" OR "seizure burden" OR "status epilepticus" OR "epilepsy severity") AND (correlat* OR associat* OR predict* OR independent)`
* Q10, 2026-11-05T22:40:16Z, 39 hits: `STXBP1 AND ("intellectual disability" OR "developmental" OR cognit*) AND ("seizure freedom" OR "seizure-free" OR "seizure control" OR "seizure onset" OR "epilepsy severity") AND (cohort OR patients OR individuals)`
* Q11, 2026-11-05T22:40:29Z, 56 hits: `CDKL5 AND (development* OR "developmental score" OR "gross motor" OR "functional abilities") AND (seizure OR epilepsy) AND (associat* OR correlat* OR predict*) AND (cohort OR registry OR "natural history")`
* Q12, 2026-11-05T22:40:30Z, 44 hits: `(SCN2A OR SCN8A OR KCNQ2) AND ("developmental outcome" OR "intellectual disability" OR "developmental trajectory" OR "neurodevelopmental outcome") AND ("seizure freedom" OR "seizure-free" OR "seizure control" OR "early treatment" OR "sodium channel blocker*")`
* Q13, 2026-11-05T22:40:31Z, 3 hits: `("Dravet syndrome"[Title] AND ("not a pure consequence" OR "contraindicated medication"))`
* Q14, 2026-11-05T22:50:16Z, 24 hits: `(ICISS OR "International Collaborative Infantile Spasms Study") AND (Vineland OR developmental OR "lead time" OR etiology OR aetiology OR "secondary analysis")`
* Q15, 2026-11-05T22:52:00Z, 49 hits: `(KCNQ2 OR SCN2A OR SCN8A OR STXBP1 OR CDKL5 OR SCN1A OR "tuberous sclerosis") AND ("early control" OR "early treatment" OR "prompt treatment" OR "early initiation" OR "seizure control") AND ("developmental outcome" OR "cognitive outcome" OR "intellectual" OR "neurodevelopmental outcome") AND (improve* OR better OR associated)`
* Q16, 2026-11-05T22:52:02Z, 126 hits: `("infantile spasms" OR "West syndrome" OR hypsarrhythmia) AND ("duration of hypsarrhythmia" OR "hypsarrhythmia duration" OR "treatment lag") AND (mental OR cognitive OR developmental)`
* Q17, 2026-11-05T22:52:15Z, 3 hits: `Primec ZR[Author] AND (hypsarrhythmia OR "infantile spasms")`

The review's own search S3 found PMID 42190144, which my gene-specific strings could not retrieve. The review's search S4, stratified by aetiology, confirmed that the main axis of this package is complete.

Stop reason: the sub-question is answered for the base rate and the strata. The one discriminating dataset not read (ICISS stratified by aetiology) is route-exhausted.

## 7. Files

* `evidence_a2.tsv`: the evidence table.
* `queries.tsv`: every search and route action.
* `module_inputs.md`: proposals for `INV-10`, the work order `NEED-SEIZURE-CONTROL-SYMPTOMATIC` and CLAIM 031, plus `proposed_registry_changes`.
* `RESPONSE.md`: the author response to the audit and the review, finding by finding.
* `receipts/`: 24 staged receipts `FTR-20261105-<PMID>-22`, all `first_read`, all passing `staged_receipt_check.py --check-doi` on 2026-11-06, and indexed in `receipts/INDEX.tsv`. Eight are `partial_fulltext_read` and 16 `abstract_only`. No receipt was written for the three module-held TSC trials, or for PMID 42190144, which was read at abstract level only.
* No script is kept here. The scratch tools that verified every quote verbatim against its source text stay outside the repository.
