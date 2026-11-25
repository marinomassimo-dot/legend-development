# ADV-276 continued: four routed leads, acquired and read (SCI, 2026-11-25)

Hypothesis level; reference genotype class; nothing here is medical advice. Single reader, targeted reading (not complete reads). None of the four studies WWOX. No canonical file changes.

## Acquisition

| Item | Route and result | Held artefact (under `files/`) |
|---|---|---|
| PMID 40125810 (QO-83) | PMC open-data bucket: XML, PDF, figures, supplement | `fulltext/PMID40125810_Wang2025QO83_PMC_r2.xml`; `supplement/PMID40125810_r2/` |
| doi 10.1038/s42003-026-10958-7 (Fmr1 rat, AIS) | not in PubMed or Europe PMC by DOI on 2026-11-25; open publisher page, "Article in Press" PDF and two supplement PDFs | `fulltext/DOI10.1038_s42003-026-10958-7_AIS2026_inpress_20261125.pdf`; `supplement/DOI10.1038_s42003-026-10958-7/` |
| PMID 42723519 (vigabatrin PK) | bucket gives a restricted stub, Europe PMC XML 500; the PMC article page carries the full text | `fulltext/PMID42723519_VigabatrinPK2026_PMC13563110_pmcpage_20261125.html` |
| PMID 42441989 (vigabatrin MRI case) | PMC open-data bucket | `fulltext/PMID42441989_VigabatrinMRI2026_PMC_r2.xml` |

## 1. QO-83, a Kv7 opener (preclinical)

* Claim in the abstract: more potent than retigabine; effective at 1 mg/kg against retigabine 10 mg/kg in acute and chronic rodent seizure models.
* Limits for any transfer: the in-vivo models described in Methods use male animals of adult weight (rats 180 to 260 g or aged 8 weeks; mice 18 to 25 g). No juvenile or neonatal animal. Queries `rotarod|tolerab` over the main text: no motor-tolerability test found (2026-11-25).
* Exposure (Supplementary, rat, 10 mg/kg intragastric; 10 times the headline dose): brain 94.58 ± 26.48 and plasma 27.52 ± 25.46 ng/g at 15 min; brain 172.25 ± 75.13 and plasma 102.11 ± 96.64 at 1 h. The printed ratios 343.67% and 168.73% recompute. Plasma standard deviations are about as large as the means.
* Safety wording: the main text says no hepatotoxicity; the supplement reports a significantly higher liver-to-body weight ratio in the 20 mg/kg QO-83 group than in control (also in the two comparator groups), with normal histology, n = 4.
* Consumer effect: none. A radar entry for the Kv7 strand; an experimental compound, not a repurposing candidate.

## 2. Axon initial segment development and Kv7 response (Fmr1 knockout rat, article in press)

* Male Fmr1 knockout rats, CA1 pyramidal neurons, P12 to P15 and 6 to 10 weeks.
* Retigabine 2.5 µM changed rheobase, spike shape and neurotransmission in wild-type slices and not in knockout slices at P12 to P15; XE991 5 µM still increased excitability in both genotypes.
* The AIS morphology finding (shorter, broader) is in primary neuronal cultures from embryos (n = 6 per genotype), with a separate slice analysis; the authors' causal link from AIS development to Kv7 inertness is their interpretation.
* The version is unedited and will be replaced by the version of record.
* Consumer effect: no current sentence changes. **Lead for the Kv7 strand:** a Kv7 opener can be inert in a developmental disorder without loss of the channel, so a WWOX-deficient test of any Kv7 opener should include a response measurement at the intended developmental stage. Whether WWOX loss alters the AIS was not searched in this reading.

## 3. Vigabatrin loading-dose pharmacokinetics (adults after cardiac arrest)

* Six comatose adults, age 22 to 68, single enteral load 4500, 2250 or 1125 mg by creatinine clearance, two per dose. Median Cmax 38.1 mg/L, half-life 16.2 h (9.4 to 23.9), AUC0-24 431.2 mg·h/L.
* The medians and dose-normalised values in Table 2 recompute. In Table 1 the serum creatinine summary prints a median of 2.1 mg/dL, but the six listed values give 1.31 (2.1 is the midpoint of the range).
* Consumer effect: none. Critically ill adults with renal injury; no paediatric or brain-exposure information for the vigabatrin note.

## 4. Vigabatrin-associated MRI changes (one case)

* One infant with a perinatal stroke and a 16p13.11 microdeletion, about 160 mg/kg/day; MRI signal changes that regressed after withdrawal; hemispherotomy in between; a later episode with septic shock and cardiomyopathy.
* The report is internally inconsistent in places (for example "without any clinical signs of toxicity" and, for the late postoperative period, "heightened clinical symptoms indicative of toxicity"). Causation of the later changes is attributed by the authors to several factors.
* Consumer effect: none. The vigabatrin note already records MRI changes in WWOX cases and in unexposed comparison children; this case adds no WWOX information.
