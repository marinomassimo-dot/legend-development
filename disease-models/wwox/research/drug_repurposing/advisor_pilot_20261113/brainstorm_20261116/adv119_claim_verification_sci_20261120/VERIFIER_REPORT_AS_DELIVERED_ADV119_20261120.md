# Blind verifier report as delivered (SubagentHandback parsed from the subagent transcript; legend-delegate, model claude-sonnet-5-5, effort high read back from the transcript with session_model_census.py: 28 turns, effort high on all 28; not edited; hypothesis level; not medical advice)

Model: sonnet. Effort: high. Blind verification of C1 to C12 (ADV-119, hypothesis level, not medical advice). Attribution: According to PubMed, with article DOIs where PubMed was used: 10.1111/epi.13335 (C1, C2), 10.1111/epi.18190 (C3), 10.1007/BF00332355 (C4), 10.1093/toxsci/kfn270 and 10.1097/ALN.0b013e3181d3e0c2 (C6), 10.1007/s00213-005-0291-1 (C7), 10.1038/s41390-018-0185-7 (C8), 10.1016/j.ejpn.2023.07.008 (C9), 10.1111/epi.14563 (C10), 10.1523/JNEUROSCI.1342-23.2023 (C11), 10.1002/epi4.70289 (C12).

Route caveats that apply throughout:
- The PubMed full-text tool returned full text for PMC5214840, PMC11827727, PMC6215509 and PMC13395050. It returned an empty body for PMC2721655 and PMC10869160.
- The PMC article page gave a reCAPTCHA check for PMC2721655, PMC10869160 and PMC5214840. I stopped there, with no workaround. It loaded once, for PMC6215509.
- Europe PMC fullTextXML returned HTTP 500, and the Europe PMC render and PDF routes and the JNeurosci page returned 403.
- WebFetch is a summarising reader. Values taken through it (C5 registry records, C10 Table 1) are as the reader returned them, not raw JSON or HTML. Say so if you cite them as verbatim.

---

C1: SUPPORTED_WITH_LIMIT | PubMed full-text tool, PMC5214840 (Methods, Results, Abstract) |
- Single dose, Results: "retigabine at doses of 5, 15, or 30 mg/kg did not induce apoptosis in orbitofrontal cortex". Later: "retigabine did not induce neuronal apoptosis in thalamus after a single exposure on P7". Abstract: "Acute (single) exposure to retigabine, even at doses of 30 mg/kg was also without effect on apoptosis."
- Route, Methods: "Drug treatments were administered intraperitoneally".
- Repeated dose, Results: "3 x 15 mg/kg of retigabine induced a significant increase in apoptosis in laterodorsal thalamus (Mann Whitney U = 8.5, P=0.021), cingulate cortex (U=2, P=0.0087), primary motor cortex (U=10.5, P=0.043), retrosplenial cortex (U=11, P=0.025), and somatosensory cortex (U=9, P=0.0472). No significant increase was found in orbitofrontal cortex, nucleus accumbens, and ventromedial thalamus (Ps = 0.24, 0.17, and 0.07, respectively)."
- P range: 0.0087 to 0.0472. The claim's 0.009 to 0.047 is a rounding of this range. Five of eight regions is correct.

Dosing schedule statements. Three places state it, and they do not read identically:
- Methods: "An additional group of animals was treated three times (spaced by 4 h) with either retigabine (15 mg/kg) or vehicle".
- Results: "this time after 3 exposures over a 12 h period. This dosing interval was selected based on the T1/2".
- Abstract: "treated repeatedly (3x) with retigabine (15 mg/kg) or vehicle over 24". The unit is lost in the tool's rendering, so I cannot tell what follows "24".
- All three agree on 3 doses at 15 mg/kg. They differ on the window: 4 h interval (so first to third dose is 8 h), "12 h period", and "24" in the abstract. The text never reconciles these.
- Single-dose animals were killed 24 h after treatment ("Treatments occurred on P7, 24 h before sacrifice"). Whether the repeated-dose animals were killed 24 h after the first or the last dose is not stated in the text I could read.

More or less than the claim:
- "Produced no apoptosis" is "did not induce / no significant increase versus vehicle" (ANOVA with Holm-Sidak, planned comparisons). It is not zero apoptosis.
- Dorsal striatum was not assessable: "a high density of artifactual staining near the lateral ventricle precluded an assessment of this region".
- Male Sprague-Dawley pups only. Vehicle is sterile water with 0.1% tween-20.
- The repeated-dose P values are Mann-Whitney, with one-tailed testing declared in the Statistics paragraph and no correction across the eight regions stated. Outlier removal by ROUT applied to the parametric tests.
- The repeated-dose arm had no pharmacokinetics: "we did not measure pharmacokinetics with this repeated administration".
- Minor: levetiracetam is 200 mg/kg in "Drug solutions" and 250 mg/kg in "Selection of drug doses". This is not part of the claim.

---

C2: SUPPORTED_WITH_LIMIT | PubMed full-text tool, PMC5214840 (Results; Supporting Table 1 not reachable) |
- Results: "retigabine concentrations peaked 1–2h after IP administration. Retigabine was cleared with a half-life of 2.2–2.5 h. We were unable to generate a fit for 5 mg/kg data, so half-life and Vd are not reported for this dose. ... retigabine reached appreciable concentrations in brain (330, 1296, and 2013 ng/ml of tissue for 5, 15, and 30 mg/kg respectively)."
- Abstract: "The half-life of retigabine in plasma was 2.5 h, with appreciable concentrations reached in the brain within 1 h of administration."

My arithmetic, using MW 303.3 and ng/ml = µg/L:
- 330 µg/L ÷ 303.3 = 1.088 µM.
- 1296 µg/L ÷ 303.3 = 4.273 µM.
- 2013 µg/L ÷ 303.3 = 6.637 µM.
- These match the claim's 1.1, 4.3 and 6.6 µM. The conversion assumes 1 ml of tissue is about 1 g; the paper gives "ng/ml of tissue" and no density.

Limits:
- The paper does not say "total" brain concentration or "free". Brain was homogenised and extracted in methanol and acetonitrile, so the value is presumably total, but that is my inference.
- The text does not say at what time point the 330/1296/2013 values were measured. The claim implies peak, and the text does not tie them to a time. Supporting Table 1, which would hold this, was not available in the text I could read.
- "Peaked 1-2 h" is stated for retigabine concentrations without separating plasma from brain.
- The half-life 2.2 to 2.5 h applies only to 15 and 30 mg/kg. The 5 mg/kg group had no fit.
- Male SD P7 pups, i.p.

---

C3: SUPPORTED_WITH_LIMIT | PubMed full-text tool, PMC11827727 (Abstract, Results 3.2) |
- 35.5% is 27/76, not "of 80". Results 3.2.1: "Prevalence of 'VABAM possibly VGB-related' ... concerned 35.5% of patients (27/76 patients, after excluding the four patients with VABAM-like abnormalities before and during VGB treatment)". The raw figure is "In 31 of 80 VGB-treated patients (38.8%), VABAM was seen on MRI during VGB treatment."
- 13.5% is not TSC-only. Results 3.2.2: "In two of 23 TSC patients without VGB treatment and in five of 29 epilepsy patients without TSC and VGB treatment, VABAM-like MRI abnormalities were seen ... Prevalence ... was, therefore, 13.5% (7/52 patients)". Abstract: "13.5% of all patients without VGB". The comparison group is 23 TSC non-VGB plus 29 non-TSC epilepsy controls.
- RR: "VGB was significantly and independently associated with the detection of VABAM (RR = 3.57, 95% confidence interval [CI] = 1.43–6.39)", Table 2 p = .02. This is from a multivariable logistic regression (VGB, refractory epilepsy, TSC), with odds ratios converted to risk ratios. It is not the crude 35.5/13.5 ratio.
- Resolution: "In all 13 VGB-treated patients with 'VABAM possibly VGB-related' for whom posttreatment MRIs were available, VABAM entirely resolved after VGB discontinuation with a median time of 10.8 months". That is 13 of the 27 affected patients, which the claim's "13 of 13 with follow-up" matches.

Omitted: the 13.5% non-VGB group also had resolution on follow-up and was mostly non-TSC epilepsy. The paper's conclusion is that the MRI abnormalities are not specific to vigabatrin or TSC, and that no significant association with clinical symptoms was found (RR 2.76, 95% CI .68-8.77).

---

C4: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstract (PMID 7271442). No PMC full text exists. The Springer page redirected to a cookie/authorisation endpoint, so no full text was obtained. |
- Abstract: "In 5- and 15-day-old rats, acute toxicity is much higher than in adults." And: "Thus the age-dependence of lithium toxicity stems from the age-dependent pharmacokinetic parameters of lithium, such as distribution and renal elimination."
- The claim's wording matches the abstract. Species and age are correct (rats, 5 and 15 days old, versus adults).
- I could not read the dose, route, LD50 values or n. The abstract says "stems from", which is the author's inference from renal diuresis experiments, not a direct test of distribution.
- Omitted detail: the abstract adds that two sublethal doses (75% of LD50) given at a shorter interval in young rats gave the same 50% mortality, and that renal lithium elimination was measured after lithium pretreatment.

---

C5: SUPPORTED | ClinicalTrials.gov API v2 JSON for NCT04639310 and NCT04912856, read through the WebFetch summariser (not raw JSON) |

NCT04639310 holds the enrolment, the seizure numbers and the stop reason:
- "Overall status: TERMINATED", "whyStopped: Sponsor decision; Not a safety decision".
- Enrolment 8 ACTUAL, with XEN496 n=5 and Placebo n=3.
- Primary outcome: "Percent Change From Baseline in Monthly (28 Day) Countable Motor Seizure Frequency During the Blinded Treatment Period". XEN496 mean -46.0% (SD 23.49), placebo 25.6% (SD 46.84).
- No statistical analysis is listed (no p-value, CI or model).
- Eligibility: 1 Month to 6 Years, stdAges CHILD.
- The summariser labelled the drug "XEN496 (ezogabine)"; I could not check that parenthetical verbatim.

NCT04912856 (the open-label extension) holds the adverse-event numbers:
- Status TERMINATED, "Sponsor decision; not a safety decision". Enrolment 8.
- Group 1 is "XEN496 Treatment in Preceding Study" (at risk n=5). Group 2 is "Placebo Treatment in Preceding Study" (n=3). The labels XEN496/XEN496 and Placebo/XEN496 do not appear on the page.
- Other events: "Retinal Pigmentation: Group 1 1/5; Group 2 0/3" and "Urinary retention: Group 1 1/5; Group 2 0/3".

Omitted or changed:
- Both events are listed under other (non-serious) events.
- Group 2 had urinary hesitation 1/3.
- The extension's serious events were gastroenteritis 1/3 in Group 2, and in Group 1 pneumonia, seizure cluster and intestinal malrotation, 1/5 each.
- Of the 8 extension participants only 1 completed.
- The primary record lists 1/5 treatment-related TEAE on XEN496 and no retinal pigmentation.

---

C6: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstracts for PMID 19126600 and PMID 20418696. Zou full text: tool body empty, PMC page behind CAPTCHA, Europe PMC 500/403. Soriano: Anesthesiology, no PMC record found. |

Zou 2009, abstract wording:
- "Postnatal day 7 rats were administered 5, 10, or 20 mg/kg ketamine using single or multiple injections (subcutaneously) at 2-h intervals, and the potential neurotoxic effects were examined 6 h after the last injection. No significant neurotoxic effects were detected in layers II or III of the frontal cortex of rats administered one, three, or six injections of 5 or 10 mg/kg ketamine. However, in rats administered six injections of 20 mg/kg ketamine, a significant increase in the number of caspase-3- and Fluoro-Jade C-positive neuronal cells was observed in the frontal cortex."
- "...ketamine administration results in a dose-related and exposure-time dependent increase in neuronal cell death during development."
- The claim's 1/3/6 injections, 2-h intervals and 6 x 20 mg/kg match.
- Limits: the route is subcutaneous (the claim says nothing). The "no effect" is stated for frontal cortex layers II/III only, not whole brain. Measures were caspase-3 and Fluoro-Jade C, and the tissue was examined 6 h after the last injection.

Soriano 2010, abstract wording:
- "Each rat pup received five intraperitoneal doses of either saline or ketamine (5, 10, and 20 mg/kg/dose) at 90-min intervals over 6 h."
- "Ketamine mediated a dose- and time-dependent increase in expression of cell cycle proteins and activated caspase-3."
- The five doses at 90 min match. The route is intraperitoneal, the doses are 5, 10 and 20 mg/kg per dose, and the time axis for "cyclin D1 ... increased at 12 h and peaked at 24 h" is in vitro. The abstract does not give the in vivo numbers.
- The claim's phrase "raised cell-cycle proteins and caspase-3" is stated at dose-dependent level. Which of the three doses did so in vivo is not in the abstract.

Both papers were read at abstract level only.

---

C7: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstract, PMID 16416331. No PMC record shown. |
- Abstract: "Animals were given a single injection of 0, 2.5, or 5.0 mg/kg CGP 43487 on PD 5. On PD 20 subjects were given paired or unpaired presentations of either an olfactory or auditory conditioned stimulus (CS) with a 110-dB-white-noise unconditioned stimulus." And: "Pups treated with CGP exhibited impairments in conditioned freezing, but were unaffected in their expression of conditioned changes in heart rate, to both olfactory and auditory stimuli."
- The claim matches. Route, strain detail (MeSH lists Sprague-Dawley rats), n and the statistics are not in the abstract. The impairment was found for both CS types (olfactory and auditory). The effect is stated as "impairments in conditioned freezing" without saying whether each dose did so.

---

C8: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstract, PMID 30237570. No PMC record shown. |
- Abstract: "Male preterm pups were randomized to ganaxolone (Prem-GNX; 2.5 mg/kg subcutaneously twice daily until term equivalence)". And: "However, during the treatment period weight gain was poor, and pups were sedated, ultimately increasing the neonatal mortality rate."
- The claim matches in direction. The abstract does not give group mortality numbers, so "higher neonatal mortality" is the authors' statement, not a number I could check.
- Omitted: male pups only, 2.5 mg/kg subcutaneous (not stated in the claim), and the abstract also reports benefits (behaviour returned to term phenotype, myelin basic protein deficits ameliorated). The authors say "dosing studies are required to reduce the burden of unwanted side effects".

---

C9: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstract, PMID 37639777 (the abstract also cites NCT04106557, which I did not query). No PMC record shown. |
- Abstract: "we randomized children 4-12 years old with a molecular diagnosis of AS ... to either daily administration of weight-based gaboxadol or matching placebo for 12 weeks. The primary endpoint was the CGI-Improvement-AS (CGI-I-AS) score at week 12." And: "mean CGI-I-AS score was 3.3 (SD, 1.00) and 3.2 (SD, 1.05) in the gaboxadol and placebo groups, respectively, yielding a least squares mean difference of zero (p = 0.83)." And: "Gaboxadol was well tolerated in all age groups of this study."
- The claim matches. Omitted: n=47 gaboxadol and 50 placebo aged 4 to 12, plus 7 children aged 2 to 3 given gaboxadol for safety only (so "well tolerated in all age groups" includes those 7). The dose was 0.125 to 0.24 mg/kg by weight range, for 12 weeks. The zero is a least-squares mean difference, with the raw group means differing by 0.1 on the score.

---

C10: SUPPORTED | PubMed full-text tool, PMC6215509 (Results 3.2, 4.2), plus Table 1 via the PMC article page read through the WebFetch summariser |
- Text: "Ezogabine (EZG) was the only ASD of 20 tested that completely blocked REDs at the concentrations tested." And: "Upon bath exchange with 100 µM EZG, all three RED parameters are reduced to 0% of their baseline values within 20 minutes (N=7)."
- And: "these values were 2.8 µM, 11.8 µM, and 21.4 µM for duration, frequency, and amplitude, respectively." The frequency EC50 11.8 µM is as the claim says.
- Table 1 as returned by the reader, % of baseline, mean ± SEM:
  - 0.3 µM: duration 91.6 ± 8.5, no significance mark, N=6.
  - 1 µM: duration 61.1 ± 8.9, p<0.01, N=8.
  - 3 µM: duration 56.1 ± 10.1, p<0.01, N=9.
  - 100 µM: duration, frequency and amplitude all 0.0 ± 0.0, p<0.001, N=7.
- These match "no effect at 0.3 µM", "56 to 61 percent" at 1 to 3 µM, and "abolished" at 100 µM. The 0.3 µM "no effect" is read from the absence of an asterisk in the summariser output.

Limits:
- The model is kainate-treated adult male Sprague-Dawley rats (150-200 g), horizontal slices of medial entorhinal cortex, recordings from layer II, in low-Mg/6 mM K+ ACSF. "Adult epileptic rat slice" is accurate but regional.
- At 1 and 3 µM the frequency was not reduced (107.1 and 91.6%, not significant). Only duration fell.
- The 100 µM block "did not reverse with washing for 20 minutes".
- Concentrations tested per Table 1 were 0.3, 1, 3, 30 and 100 µM, with no 10 µM group.

---

C11: ABSTRACT_ONLY_NOT_VERIFIABLE | PubMed abstract, PMID 38176909. PubMed full-text tool body empty; PMC page behind reCAPTCHA (two attempts); Europe PMC XML 500, Europe PMC PDF 403, JNeurosci page 403. |
- Abstract: "neonatal C57BL/6J mice (postnatal day P5–8, both sexes) using acute brain slices ... THIP enhanced GABAergic tonic inhibitory conductances in layer V neocortical and CA1 pyramidal neurons and increased their rheobase without altering sEPSC characteristics. Two-photon calcium imaging demonstrated that enhancing the activity of extrasynaptic GABAARs decreased neuronal firing in both brain regions."
- Not in the abstract: the concentrations (10 and 50 µM), which slices got which, and the statement "50 µM lowered firing without abolishing network activity". Those cannot be confirmed or refuted from the abstract. The abstract also says THIP reduced epileptiform activity "in a dose-dependent manner" in 4-AP and low-Mg models, in neonatal and adult slices.

---

C12: SUPPORTED_WITH_LIMIT | PubMed full-text tool, PMC13395050 (Results 3.2, Methods 2.3, Figures 2-3) |
- "Ethosuximide (200 mg/kg) reduced total seizure incidence by 64% (vehicle 21.4 ± 4.7, range 5–45 vs. ethosuximide 7.7 ± 1.8, range 1–20; t(8) = 2.6, P = 0.03)".
- "Ulixacaltamide (60 mg/kg) reduced total seizure incidence by 64% (vehicle 21.1 ± 2.8, range 5–44 vs. ulixacaltamide 7.5 ± 2.3, range 0–22; t(10) = 3.5, P = 0.006)".
- All claim numbers match. (21.4-7.7)/21.4 and (21.1-7.5)/21.1 both round to about 64%.
- Methods: "Ethosuximide (200 mg/kg), ulixacaltamide (60 mg/kg), CBD (100 mg/kg), or vehicle was administered (i.p.) 30 min before the light–dark transition". Within-subjects Latin-square crossover with one-week washout, 10-week-old male and female mice, one-hour epoch (17:30-18:30). Cumulative totals were "analyzed using paired t-tests".

Limits:
- The genotype string "Gabrb3+/D120N" is not readable in the tool output. Superscripts are stripped from the text, title and abstract, and only "Gabrb3" and "knock-in" are visible. D120N could not be confirmed.
- The claim says "t tests" without saying paired. The two n are 9 (ethosuximide) and 11 (ulixacaltamide), a crossover with its own vehicle runs, and no multiplicity correction applies to these cumulative totals.
- The paper notes injection stress may raise seizure counts in vehicle-treated mice versus untreated animals.
- Total seizure duration fell by 74% (ethosuximide, P=0.01) and 60% (ulixacaltamide, P=0.009). The timecourse analysis found no significant main effect on duration.
- "Reduced by 64 percent" is a drug-versus-own-vehicle contrast in the atypical absence assay, not a population effect.

---

Count line: SUPPORTED 2 (C5, C10); SUPPORTED_WITH_LIMIT 4 (C1, C2, C3, C12); NOT_SUPPORTED 0; ABSTRACT_ONLY_NOT_VERIFIABLE 6 (C4, C6, C7, C8, C9, C11).

Not done: no figures or supplements were read. Supporting Table 1 of PMC5214840 was not reachable, nor were the Zou, Soriano, Hunt, Shaw, Keary, Kersten and Liddiard full texts. No file was written; this message is the report.
