# ADV-095 oligodendrocyte-class agent unit: producer report as delivered (legend-delegate, sonnet, effort medium, one round, no sub-delegation; delivered 2026-11-19; persisted verbatim by SCI from the subagent transcript; the brief is `OL_CLASS_AGENT_UNIT_PRODUCER_BRIEF_SCI_20261119.md`). Producer output, NOT yet verified by SCI or a second reader: every number is a producer claim until the verifier pass; the producer marks its own coverage PARTIAL and did not re-verify every quote by script (those are marked printed).

ADV-095 oligodendrocyte-class agent unit: producer report (SCI 2026-11-19). Hypothesis level only: no dose, no schedule, no recommendation for or against any use of any agent in any person. Research concentrations and animal doses are findings of the sources. Reference genotype class only; not medical advice.

**Status: PARTIAL.** I did one round at medium effort. The rows are thinner than the brief asks for. Receptor affinities (Ki/IC50) were not retrieved for any agent. Juvenile brain exposure was not found for any agent. Label and age-restriction text was not retrieved for clemastine, benztropine or the thyromimetics. The "up to two more" agents are named from the sterol and azole literature only, not examined in depth.

**Routes tried.**
- PubMed search and metadata tools.
- Europe PMC fullTextXML: HTTP 500 for PMC6394402, 6170028, 4431622, 4830134, 6621548, 6538346 and 6154442. Retries returned full text for PMC11502491, 8970281, 9966820, 10171952 and 10393406.
- PMC article page: reCAPTCHA challenge, so that route was stopped.
- NCBI efetch db=pmc (plain HTTP, no contact parameter): full text for PMC6170028, 4431622, 4830134 and 6621548. No body for PMC6394402, 6538346 and 6154442.
- PubMed full-text tool for PMC6538346: empty full_text, so that paper is AB only.

**Repository checks.**
- `files/fulltext` held 3 relevant files: PMID35372341_Palma2022_PMC_r2.xml, PMID38942888_Odell2024_PMC_r2.xml and PMC6423962_PMID30046109_europepmc_fulltext_2026-11-13.xml (Hubler 2018, the sterol/azole paper).
- Not run: `fulltext_receipts.py`. It was not consulted, so I make no receipt-ledger claim.
- The HE sheet folder `adv098_agent_sheets_he_20261119` does not exist in the worktree. `/home/desktop/legend-development/files/adv098_agent_sheets_raw_he_20261119` holds 12 other agents (for example ketamine, memantine) and none of clemastine or sobetirome. No database origin was used.

Access levels: FT = full text read in the passage, AB = abstract only. Every quote below was taken from fetched bytes. Quotes marked "(printed)" were extracted from the fetched text during the session. I did not run a separate substring re-verification script for them.

## Rows

### 1. Clemastine (M1 muscarinic antagonist, H1 antagonist)
- **Target and potency, in vitro.**
  - Mei 2014 (PMID 24997607, FT): the screen was run at 1 µM on OPCs on micropillar arrays. Quote: "Both compounds were most effective at 500 nM but promoted differentiation at as low as 10 nM."
  - Same paper: clemastine, benztropine or T3 "promoted differentiation and myelination without altering the number of oligodendroglial cells". This is the one place in my set where progenitor number and mature-cell number are separated: no change in total cell number.
  - The preparation (species, medium, exposure time) is only partly captured. The screen used 3 d of exposure with MBP and PDGFRα staining. The exact species and medium for the dose-response were not read.
  - No Ki or IC50 was retrieved. This is a gap.
- **Exposure.**
  - Odell 2024 (PMID 38942888, FT): oral clemastine at 7.5 mg/kg/day to hypoxia-exposed mouse pups from P3 (a research finding, not a patient dose). Quote: "Cmax 44.0 ng/mL, t1/2 4.6 h, and AUC24 280.1 ng*hr/mL". The matrix is plasma, steady state on day 8. Total concentration only.
  - No brain, CSF or unbound neonatal value was found. I did not invent one.
- **Endpoint, developmental dysmyelination or hypomyelination.**
  - Positive:
    - Brain 2018 (PMID 29244098, AB): hypoxic neonatal mouse. Quote: "clemastine dramatically promotes oligodendrocyte precursor cell differentiation, myelination, and improves functional recovery". The effect is stated as "oligodendroglial specific via an effect on the M1 muscarinic receptor on oligodendrocyte precursor cells".
    - Neuron 2018 (PMID 30078577, FT): chronic hypoxia, clemastine or U50488 at 10 mg/kg/day. Quote: "MBP staining for myelin and CC1 positive OL numbers were greatly enhanced at P10 as compared to the vehicle controls". The M1R-ablation experiment is also in this paper.
    - Odell 2024 (FT): in the abstract, hypoxia-induced hypomyelination was rescued with a minimum effective dose of 7.5 mg/kg/day, assessed by IHC and EM at P14.
    - Pitt-Hopkins Tcf4-mutant mouse (PMID 37068912, AB and FT):
      - Quote (printed): "clemastine treatment reduced excess oligodendrocyte precursor cells and normalized oligodendrocyte density".
      - Here the progenitor pool was in excess, not intact.
      - Clemastine 10 mg/kg i.p., P28 to P42.
  - Negative or null in the same column:
    - Palma 2022 (PMID 35372341, FT): healthy mouse, 50 mg/kg/day i.p., P5 to P21. Quote (printed): "despite the increase in the number of oligodendrocytes, conduction velocity of myelinated fibers of corpus callosum decreased in clemastine treated mice". Myelinated axons, nodes of Ranvier and myelin thickness were reduced, and CD11c+ microglia and IGF-1 fell.
    - Pediatr Res 2018 (PMID 29584714, FT/AB): two rat models of Pelizaeus-Merzbacher disease, 10 to 30 mg/kg/day, P1 to P21. Quote (printed): "No changes in neurological phenotype or survival were observed even at the highest dose of clemastine". Mature oligodendrocytes were unaffected.
- **Endpoint, demyelination or other injury.** Several injury papers appeared in the search but were not read: spinal cord injury, traumatic brain injury, an Alzheimer model, social isolation. ReBUILD (PMID 29029896) was found but I did not read it. Cuprizone, lysolecithin and EAE clemastine papers were searched (7545 hits) but not read.
- **Cell autonomy.**
  - The in vitro Mei result used OPC cultures with PDGFRα and MBP staining, but the microfiber and axon wrapping format was not examined.
  - Brain 2018 reports an oligodendroglial-specific effect via M1R on OPCs (AB).
  - Palma 2022 shows a microglial dependence in healthy development, so a neuron-free effect is not the whole picture.
  - Relevance to the neuron-targeted deletion: there is no direct test.
- **Harm and label.**
  - Odell 2024, Discussion (FT): "Clemastine has side effects attributed to muscarinic antagonism, such as sedation, that may limit high doses in neonates."
  - Odell 2024 (FT): "Treated mice did not appear sedated and did not otherwise have any overt behavioral abnormalities."
  - Human adverse findings and age restrictions were not retrieved. I make no claim about conservative safety from over-the-counter or pediatric use.

### 2. Benztropine
- **Target and potency.**
  - Deshmukh 2013 (PMID 24107995, FT): primary rat optic-nerve OPCs in serum-free medium, MBP imaging after 6 days under basal differentiation conditions. Quote (printed): "benztropine (half-maximum effective concentration (EC50) ~ 500 nM)". Mei 2014 gives the same optimum, 500 nM.
  - Mechanism, in the same paper: "direct antagonism of M1 and/or M3 muscarinic receptors". Carbachol blocked the effect.
  - No Ki was retrieved.
- **Exposure.** None retrieved. The paper states the drug "readily crosses the blood–brain barrier". That is a qualitative statement, not a measurement. There is no juvenile value.
- **Endpoint.** Developmental: none found. Demyelination: reduced EAE severity in a relapsing-remitting model (AB, "significantly decreases clinical severity"). I did not read the dose or the cuprizone and lysolecithin data.
- **Cell autonomy.** Isolated OPC cultures: the MBP rise occurs without neurons. The in vivo effect is in tissue with neurons.
- **Harm and label.** Not retrieved. This is a gap.

### 3. Thyroid-hormone class (T3, Triac/tiratricol, sobetirome, Sob-AM2)
- **Target and potency.**
  - T3: in Mei 2014 (FT), T3 acted like the antimuscarinics (no change in cell number).
  - Sobetirome and its CNS-selective prodrug Sob-AM2: in vitro potency not retrieved.
  - Review PMID 32733906 (AB): thyroid-receptor-beta selective. Not a primary source.
- **Exposure.**
  - Sobetirome (PMID 29845892, AB): juvenile Mct8/Dio2 double knock-out mice, sobetirome 1 mg/kg/day or Sob-AM2 0.3 mg/kg/day for 7 days. Quote (printed): "Sob-AM2 treatment in Mct8/Dio2KO animals led to 1.8-fold more sobetirome content in the brain and 2.5-fold less in plasma in comparison to the treatment with the parent drug sobetirome." This is a brain-versus-plasma ratio. An absolute concentration was not read.
  - Triac: no tissue concentration retrieved.
- **Endpoint, developmental.**
  - Triac (PMID 36834863, AB and FT): Mct8/Oatp1c1 double knock-out mice, 400 ng/g/day during postnatal weeks 1 to 3. Quote (printed): "Triac treatment (400 ng/g) induced normalized myelination, cortical GABAergic interneuron differentiation, electrophysiological parameters, and locomotor performance only when administered during the first three postnatal weeks."
    - A later start (postnatal weeks 3 to 6) did not give the same result. This is a timing-dependence point and it matters here.
    - Ditpa at 4000 ng/g gave normal myelination.
  - Maternal Sob-AM2 (PMID 36792926, AB): thyromimetic gene effects in fetal tissue.
  - Sobetirome and Sob-AM2 normalized OPC and oligodendrocyte density and behaviour in the Pitt-Hopkins model (PMID 37068912, AB). Dosing in the FT: 1.0 mg/kg/day, P28 to P42.
- **Endpoint, demyelination.** Hartley 2019 (PMID 30996143, AB only): sobetirome and Sob-AM2 improved remyelination in gliotoxin and genetic models. Quote (printed): "chronic treatment with TH in this model inhibited the endogenous myelin repair and exacerbated disease."
- **Cell autonomy.** In the Pitt-Hopkins paper the OPC density effect is in vitro and in vivo. A neuron-free test for the thyromimetics was not read.
- **Harm and label, separately.**
  - Animals: maternal sobetirome gave spontaneous abortions. Quote (printed): "This secondary effect, probably as a result of a peripheral toxicity effect associated with the dosage". Sob-AM2-treated dams did not show this.
  - Animals: sobetirome and Sob-AM2 at 10 µg/kg/d or more for 29 days in male adult mice depleted T4 and T3 with normal TSH (PMID 29846550, AB).
  - Label: tiratricol (Emcitate) was first approved in the EU on 12 February 2025 for peripheral thyrotoxicosis in MCT8 deficiency, from birth (PMID 40549098, AB, a secondary review, not the regulator text). The regulatory text was not retrieved.
  - Human phase 2 Triac trial (PMID 31377265, AB): the primary endpoint is serum T3. Cardiac, growth and metabolic outcomes in children were not read.

### 4. Candidate: EBP, CYP51 and TM7SF2 sterol-pathway inhibitors (azoles and others), Hubler 2018 (PMID 30046109, FT in the repository) and related papers (PMIDs 30773481, 33636107, 35128409, 35833657)
- **Reason for inclusion.** Primary data on OPC cells, with 8,9-unsaturated sterol accumulation as the mechanism, which is independent of muscarinic and thyroid signalling.
- **Quote.** "miconazole, which targets CYP51, penetrates the mouse blood brain barrier and enhances remyelination in mouse models of demyelination."
- **Cell autonomy.** OPCs were cultured on electrospun microfibers, so this is an axon-free, neuron-free substrate.
- **Endpoint.** Demyelination only (lysolecithin). No developmental dysmyelination data were found. This is a gap.
- **Potency and exposure.** Not retrieved. Harm and label not retrieved.

### 5. Second candidate
None assessed. Metformin and GPR17 antagonists were not examined beyond one empty search. I dropped them rather than pad.

## Conflicts between sources
- Clemastine in healthy development: Palma 2022 (50 mg/kg i.p., P5 to P21) found more oligodendrocytes with less myelin and slower conduction. The hypoxia papers (10 mg/kg and 7.5 mg/kg) found rescue of myelination. The two papers use different doses and states, and the doses differ about fivefold. They are not shown to disagree on the same question.
- Pelizaeus-Merzbacher disease rats: no benefit.

## Failed, null or negative results
1. Clemastine, myelin-deficient and PLP-transgenic rats, 10 to 30 mg/kg/day, P1 to P21: no phenotype, survival or myelin change (PMID 29584714).
2. Clemastine, healthy developing mouse, 50 mg/kg/day: lower conduction velocity, fewer myelinated axons, thinner myelin, despite more oligodendrocytes (PMID 35372341).
3. T3 in a genetic remyelination model: inhibited repair and worsened disease, unlike the selective agonists (PMID 30996143, AB).
4. Triac started in weeks 3 to 6: no normalization (PMID 36834863).
5. Maternal sobetirome: spontaneous abortions at the dose used (PMID 36792926, FT).
Nothing was found for benztropine or the sterol inhibitors in developmental models. No independent failed replication of the hypoxia rescue was found, but my search for one was a single query.

## Where the data are thinnest
1. Juvenile brain or CSF free concentration: none for any agent (only plasma for clemastine, brain/plasma ratio for Sob-AM2).
2. Affinities (Ki or IC50) for the muscarinic and thyroid targets: not retrieved.
3. Benztropine and sterol-pathway inhibitors in developmental hypomyelination: none.
4. Human age-specific harm and label text for clemastine, benztropine and thyromimetics: not retrieved.
5. Neuron-free versus neuron-containing separation for thyromimetics and for the in vivo clemastine effect: not established. The Palma result suggests microglia contribute.

## Files consulted
- `/home/desktop/legend-development/files/fulltext/PMID35372341_Palma2022_PMC_r2.xml`
- `/home/desktop/legend-development/files/fulltext/PMID38942888_Odell2024_PMC_r2.xml`
- `/home/desktop/legend-development/files/fulltext/PMC6423962_PMID30046109_europepmc_fulltext_2026-11-13.xml`
- The `files/adv098_agent_sheets_raw_he_20261119` listing (no relevant agent).
- Scratch copies in `/tmp/ol_unit_xml_x1` (not persisted).

I edited no repository file. No e-mail or personal detail was sent to any service.