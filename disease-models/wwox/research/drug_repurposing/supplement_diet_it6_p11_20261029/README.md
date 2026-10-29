# IT6-P11 — one supplement or nutrient chosen on biological grounds: extracellular magnesium as the physiological NMDAR gate

Non-canonical research material. Actor `scientist-b`, task `ORCH-ROADMAP-IT6-20261029` package P11, written 2026-10-29 in
worktree branch `task/it6-p11`. Nothing here changes the four scientific current files or the receipt ledger. **Not medical
advice. No dose, preparation, route, schedule or individual recommendation is given**; any decision for an individual belongs to
the treating clinical team. Evidence ladder used throughout: **association is not modulation, and modulation is not rescue**.
Statements are tagged DATO (a reported measurement), INFERENZA (this record's inference, owed a blind audit by someone else) or
UNVERIFIED (not checked). The language of the sources is English; quotations are verbatim and machine-checked (section 9).

---

## 0. Verdict in one screen

| | |
|---|---|
| **Chosen** | **Magnesium, as the extracellular divalent cation that gates the NMDA receptor** (any preparation; the preparation is an open question, section 6). Not a diet. Not a restoration of WWOX function. |
| **State** | `hypothesis`, route `BENEFICIO_PRECOCE` (partial benefit at best), Track A (allele-blind); Track B unmeasured. A CARD in repository format is in [`card/`](card/) and passes `check_cards.py`. |
| **Why this one** | It is the only candidate where **three WWOX observations from one receipted paper converge on a physiological regulator that is a nutrient**: (1) the knockout slice bursts and **d-APV abolishes it**; (2) the knockout pyramidal neurons **rest 5.6 mV more depolarised** (wild type -79.25, heterozygote -75.51, knockout -73.62 mV, Table 1) and the heterozygote sits between; (3) spontaneous **inhibitory current amplitude is roughly halved** (57.3 to 27.5 pA). The NMDAR pore is blocked by extracellular Mg2+ in a voltage-dependent way, so (2) and (3) both predict a weaker block at rest. No other candidate had even one WWOX observation that a nutrient could act on (section 1). |
| **The concern you asked me to check** | *Does the knockout bursting depend on a low-Mg2+ bath?* **Not shown, and probably not.** The Methods state the incubation ACSF only (1.3 mM MgSO4, 1.5 mM CaCl2, 3.5 mM KCl); wild-type slices in the same preparation do not burst (0 of 11). **The recording bath is not stated**, so that the bursting occurs at 1.3 mM Mg2+ is an inference (carried by the earlier manifest, entry 21), not a sentence of the paper. If the recording medium equals the incubation ACSF, the bursting is not a magnesium-free artefact. UNVERIFIED as a sentence. |
| **What the evidence is not** | There is **no** WWOX measurement of Mg2+, of NMDAR current, or of magnesium block anywhere in the records read. Zero WWOX and magnesium hits in PubMed titles and abstracts. The bridge from "NMDAR-dependent" to "magnesium-sensitive" is mechanism plus arithmetic (section 3.3), not data. |
| **Strongest counter-data** | (a) In the one mouse study read, **oral magnesium sulfate raised serum Mg and left cerebrospinal-fluid Mg unchanged**; only the threonate raised it (about +30 percent, healthy mice, six per subgroup). (b) In the one randomised open-label infant trial read that used a magnesium arm with an oral phase (West syndrome, 48 analysed; the arm had three days of intramuscular magnesium sulfate, then an oral syrup; both arms received ACTH and antiseizure drugs) there was **no difference in seizure control** (p 0.69); the positive randomised signal used **intravenous magnesium sulfate with ACTH** and is abstract-only. (c) d-APV is a complete block; a graded rise in an ion that is already present removes only part of the residual conductance (arithmetic: a rise of about 30 percent offsets the genotype's resting-potential effect, no more). (d) Bursting depends on NMDAR **permissively as far as measured**; the sign of an NMDAR-lowering intervention depends on the lesion in the one genetic NMDAR cohort that stratified (memantine, card F01). |
| **Decisive missing datum** | One cheap ex vivo experiment, not a supplement trial: a **graded bath-Mg2+ titration in knockout, heterozygote and wild-type slices in the source's own medium**, with d-APV as the ceiling; plus **serum and cerebrospinal-fluid Mg in the knockout mice** and the response to one oral preparation (section 8). Prediction (b) of the card closes the strand if bursts need a rise beyond anything reachable. |
| **Abstentions (searches actually run)** | PDH-axis cofactors (thiamine, lipoate, carnitine), NAD+ precursors, pyridoxine/PLP, omega-3, vitamin D, taurine, creatine: **abstain**; no WWOX observation exists that the nutrient could act on, and the repository's own needs file marks the relevant directions `uncertain` (section 1). The ketogenic diet was not searched again (E04); dichloroacetate was not touched. |
| **Accessibility, with its uncertainty** | US supplement labels exist for magnesium and its salts by name (DSLD probe, name-only); the **threonate has an EU Novel Food entry (authorised)** whose conditions of use I did not read; the EU health-claim register carries general nervous-system wording for magnesium and nothing about seizures. **Italy: not checked** (register behind a bot challenge, not bypassed). Catalogue: no entry for the threonate; target queries by GRIN symbols would never have surfaced any magnesium record (section 6). |
| **Commit / receipts** | See the final report of the delegate for the commit SHA. Five staged receipts dated 20261029 in `receipt_staging/scientist-b/` (section 9). |

---

## 1. Selection: candidates weighed on what the WWOX record shows, not on category or accessibility

Sources of the WWOX side: [`needs/needs.json`](../needs/needs.json) (22 needs, directions and counter-evidence already
curated), the cards, and the receipted manifests. "Hits" are PubMed (MCP) titles/abstracts unless stated; the complete query log
with counts is [`searches.tsv`](searches.tsv) (S01 to S41).

| Candidate | What WWOX observation would make a nutrient relevant | What the record actually shows | WWOX-specific searches (counts) | Decision |
|---|---|---|---|---|
| **Magnesium** | NMDAR-dependent network state; depolarised resting potential; reduced inhibition | `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR`: d-APV abolishes bursting (n 5 slices, 3 animals); Table 1 resting potential gradient; sIPSC amplitude halved | PubMed WWOX AND magnesium: **0**; WWOX AND NMDA/NR2B/GluN2B: **1** (the source paper) | **Chosen** |
| Thiamine, lipoate, carnitine (PDH-axis cofactors) | A PDH flux deficit that a cofactor limits | `NEED-PDH-PYRUVATE-AXIS`: direction `uncertain`; "PDK1 transcript is DOWN in the organoid and PDH activity shows no difference in the one human cell measurement"; no cofactor level measured anywhere; dichloroacetate excluded by the brief | WWOX AND (thiamine OR lipoic OR carnitine): **1** (a type 2 diabetes metabolome GWAS naming a locus; irrelevant); Europe PMC title/abstract: thiamine 0, lipoic 0, carnitine 1 (same paper) | **Abstain**: the premise (a limiting cofactor) has no observation behind it |
| NAD+ precursors | A lowered NAD+ pool or an LDH/NAD+ imbalance | `NEED-LACTATE-LDH` direction `uncertain`: "human lactate normal or extremely low"; the fly Ldh rescue is amyloid-conditional; WWOX itself is an NAD(P)+-using SDR enzyme (21476439, in vitro steroid substrates), which says nothing about the NAD+ pool in neurons | PubMed WWOX AND (nicotinamide OR NAD): **3** (renal-cancer pharmacogenetics, a metabolism review, SDR enzymology); none tests a precursor | **Abstain** |
| Pyridoxine / pyridoxal phosphate | A GABA-synthesis (GAD) or GABA-degradation defect that PLP limits | `NEED-INHIBITORY-HYPOFUNCTION` direction `uncertain` ("a measured loss of spontaneous inhibition names a deficit, not an intervention"); no GAD or PLP measurement; the GABA-AT axis is already card H02 | PubMed: **1** (38407561, a WOREE case given vitamin B6 and zonisamide without relief, n of 1, abstract-level); Europe PMC title/abstract 2 (the same + an unrelated phenotype paper) | **Abstain**; the n-of-1 is recorded as counter-data |
| Omega-3, vitamin D | Any WWOX lipid or calcium-hormone observation | none in the needs file | PubMed: **0**; Europe PMC title/abstract: 0 and 0 | **Abstain** |
| Taurine, creatine (also counted) | A redox or energy deficit | `NEED-REDOX-OXIDATIVE-STRESS`: the loss-to-ROS relation is non-monotonic and context dependent; antioxidant assumptions "refuted as an assumption" | Europe PMC title/abstract: 1 and 1, both unrelated papers | **Abstain** |
| Ketogenic diet | (E04) | not repeated: no new datum and no new question | not searched | untouched |
| Dichloroacetate | (E03/I01) | excluded by the brief | not searched | untouched |

Full-text co-occurrence counts in Europe PMC (`WWOX` AND term; S27) were: magnesium 101 (query with "Mg2+" ORed in; the plain query `"magnesium" AND "WWOX"` of S24 gives 74, which reproduces), thiamine 23, lipoic 13, carnitine 60, NAD
precursor 94, pyridoxine/PLP 67, omega-3 49, vitamin D 94, taurine 43, creatine 71. They are dominated by incidental mentions
(reference lists, methods) and were **not triaged and not used as evidence**; for magnesium the top five by relevance were
opened by title (livestock genome-wide association studies, a sheep study, a review of epilepsy networks, a syndromes review,
a bovine vesicle study): none concerns magnesium in WWOX. The other 69 magnesium hits were not opened. An unexamined hit is not
an absence, and the abstentions above rest on the two title/abstract engines plus the curated needs file, not on full text.

---

## 2. Reconstruction of the chosen item

**Actual intervention (what is being proposed for study).** Raising the extracellular Mg2+ available to the NMDAR pore. In a
slice that is a bath concentration; in an animal or a child it would have to be a nutrient or supplement (or a prescription
route) that raises **brain extracellular free Mg2+**, which is not the serum value (section 5). Nothing in this record is a diet.
**Hypothesised mechanism (INFERENZA).** Extracellular Mg2+ blocks the NMDAR pore in a voltage-dependent way. A more depolarised
resting potential (observation 2) and weaker inhibitory restraint on depolarisation (observation 3) relieve the block, raise
NMDAR gain at rest and during synchronised input, and lower the threshold for the NMDAR-dependent burst that d-APV abolishes
(observation 1). Direction wanted: **down** on NMDAR gain, by restoring block rather than removing the receptor's contribution.
**Measurement context of the WWOX data.** Acute neocortical slices, layer II/III, P13-P17, Synapsin-Cre Wwox knockout against
heterozygote and wild type, one laboratory (PMID 34634460, Neurobiology of Disease 2021). Not an allele-specific model.

### 2.1 WWOX evidence table (all from the receipted paper; the manifest carries the verbatim locators)

Receipted complete reads of this paper: `FTR-20260810-34634460-02` (the receipt the manifest names) and `FTR-20261019-34634460-01`
(same r2 file as read here, fingerprint b01bfa4f...). This package adds one **selected-passage** re-read (staged receipt
`FTR-20261029-34634460-04`) asked a question outside the earlier readings: *what is the magnesium content of the medium, and how
far apart are the resting potentials*. Locators `L01` to `L11` are in [`locators.tsv`](locators.tsv).

| # | Observation (DATO unless marked) | Value | Locator | Scope / limits |
|---|---|---|---|---|
| E1 | Burst incidence by genotype | wild type 0 of 11 slices (7 animals); heterozygote 4 of 23 (14 animals); knockout 36 of 42 (24 animals) | L02; manifest entries[0] | The Discussion calls the heterozygote bursts "similar"; they are one sixth of the knockout's rate |
| E2 | Slice medium contains magnesium | ACSF with 1.3 mM MgSO4, 1.5 mM CaCl2, 3.5 mM KCl, 10 mM glucose | L01; manifest entries[21] | Incubation ACSF only is stated; recording perfusate equal to it is **inferred** |
| E3 | NMDAR block abolishes bursts | d-APV: bursts eliminated and recovered on washout; n 5 slices, 3 animals | L03; manifest entries[2] | One drug; competitive full block; AMPAR not tested; the paper says "a requirement" (L05), not "a gain" |
| E4 | Knockout-specific delayed evoked response is NMDAR-mediated | suppressed reversibly by d-APV | L04; manifest entries[25] | Supplementary Figure S3; six animals |
| E5 | Resting potential gradient | -79.25 ± 1.99 (wild type), -75.51 ± 1.81 (heterozygote), -73.62 ± 1.36 mV (knockout); 13, 15, 40 neurons from 5, 6, 15 animals | L06, L07; manifest entries[14], [15] | Means with spread as printed; both mutants marked different from wild type |
| E6 | Inhibitory current amplitude halved | sIPSC 57.3 ± 31.0 (controls) against 27.5 ± 19.4 pA (knockout) | L08; manifest entries[7] | Pooled events, not animals; excitatory amplitude differs by about six percent (L09; manifest entries[6]) |
| E7 | The slice sits further from threshold than the animal | "neurons being more hyperpolarized ... than neurons recorded in vivo, shifting away from the threshold for spontaneous bursting activity" | L10 | The authors' own bias statement; direction: in vivo the block relief could be larger (INFERENZA, untested) |
| E8 | mEPSCs were measured at a hyperpolarised holding potential | -70 mV with TTX | L11 | So they do not test the voltage-dependent gate; "raised mEPSC amplitude" cannot be read as an NMDAR finding |

**Two caveats added after the independent check.** (a) The Methods (5.3) say the authors did **not correct for liquid junction potential**, so the printed resting potentials carry an uncorrected offset of unknown size; the genotype difference is less exposed than the absolute values, but the absolute values feed the arithmetic of section 3. (b) The burst incidence is cited in this paper to "Repudi et al., 2021", a paper from the same group: the incidence figures may overlap with that paper and are not independent replications of each other (the overlap was not checked).

**What these seven rows do not contain:** an NMDAR current, an NMDA:AMPA ratio, a subunit, a magnesium concentration varied by the
experimenter, or any measurement of magnesium in tissue or fluid.

---

## 3. Mechanism check by arithmetic (INFERENZA; not a measurement, not a model of the burst)

### 3.1 Inputs, both read at the source, both from a different cell type than the question

* Resting potentials of E5.
* External-Mg2+ half-inhibitory concentrations of the whole-cell NMDA-evoked current in **P7 rat substantia nigra dopaminergic
  neurones** (J Physiol 2014, PMID 24614743): about 20.9, 53.3 and 173 µM at -90, -70 and -50 mV (L12), a mixed GluN2B/GluN2D
  population.

### 3.2 Assumptions that are NOT from a source (UNVERIFIED for cortex)

Single-site occupancy (Hill coefficient 1); log-linear voltage dependence of the half-inhibitory concentration between -90 and
-70 mV; the dopaminergic population standing for the GluN2A/GluN2B population of juvenile cortex; recording bath equal to the
stated ACSF. The classical Jahr and Stevens parameters (PMID 1697902, PMC6570236) would be the better input: the Europe PMC XML
endpoint returned HTTP 500 and the render endpoint returned an HTML page, which I did not pursue. **That paper was not read.**

### 3.3 Result (`mg_block_arithmetic.py`, output in `mg_block_arithmetic_output.txt`)

| Genotype | Resting potential | Unblocked fraction of the Mg-free current at 1.3 mM Mg2+ | After a rise of 15 percent | After a rise of 30 percent |
|---|---|---|---|---|
| wild type | -79.25 mV | 2.59 % | 2.25 % (at 1.5 mM) | 1.99 % (at 1.7 mM) |
| heterozygote | -75.51 mV | 3.07 % | 2.67 % | 2.37 % |
| knockout | -73.62 mV | **3.35 %** | 2.91 % (0.87 of the value at 1.3 mM) | **2.58 % (0.78)** |

Reading: (i) the knockout's depolarisation alone leaves about **1.3 times** the wild-type fraction of NMDAR conductance unblocked
at rest; (ii) a rise in extracellular Mg2+ of about **30 percent** brings the knockout back to the wild-type value in this crude
model; (iii) d-APV takes the fraction to zero. The size of (ii) happens to resemble the cerebrospinal-fluid rise seen with the most
brain-penetrant salt in healthy mice (0.89 to 1.17 mM, +31 percent, L14). **That coincidence of two crude numbers from different
animals and different compartments is not a prediction**: brain parenchymal free Mg2+ is not cerebrospinal-fluid total Mg, and
the burst is a regenerative event whose dependence on a 25 percent change in resting NMDAR conductance is unknown. Parameter range (verifier's check against Jahr-Stevens-type, steeper block): the 1.3 times becomes 1.2 to 1.6 times and the offsetting rise +25 to +57 percent, depending on the voltage slope used (the shallow dopaminergic slope used here is the low end of the steepness); the conclusion is unchanged. What the
arithmetic does establish is the **order of magnitude**: a reachable rise corrects at most the resting-potential excess, and it
does not approach a complete block.

---

## 4. External precedent (none of it is WWOX evidence)

| Source | What it shows (DATO as reported) | Depth read here | Direction for the node | Limits |
|---|---|---|---|---|
| Zou 2010 Clin Ther, PMID 20435238 | Randomised open-label, 19 infants per arm, China: ACTH + intravenous magnesium sulfate against ACTH alone, seizure-free 14/19 vs 9/19 at 12 weeks, 12/19 vs 10/19 at 24 weeks; the abstract calls the proportions "significantly greater" | **abstract only** (no open full text) | supports (other aetiology) | Open label, 38 infants, prescription route, combination with ACTH; exact tests not read |
| Wang 2023 Pediatr Investig, PMID 36967744 | Retrospective single arm, 229 infants after first-line failure: 48.5 % seizure-free, 72.1 % resolution of hypsarrhythmia, 21.4 % adverse events (infections 31, low potassium 7, diarrhoea 4, hypertension 2) | text read (staged receipt `...36967744-01`, partial because the flow chart image and a supplement table were not opened) | not estimable | "this study lacked a control group" (L25); intravenous route with ACTH; aetiology mixed (structural/metabolic 46.7 %, genetic 10.5 %, unknown 47.8 % as printed, but 98/229 is 42.8 %, a typo of the paper; the printed percentages therefore sum to 105) |
| Yadav 2022 Iran J Child Neurol, PMID 35222658 | Open-label randomised, West syndrome, 52 recruited, 48 analysed: intramuscular magnesium sulfate for three days then an oral magnesium syrup for three months, against a syrup with calcium and vitamin D only; **seizure control p 0.69, development p 0.09, EEG p 0.04 (Results) or 0.003 (Discussion)** | text read (staged receipt `...35222658-01`) | **null on seizures**; EEG signal inconsistent | No blinding; no placebo; per-protocol; Table 3 rows do not add up to the analysed numbers (intervention 27 against 26, comparator 21 against 22); the Discussion asserts a serum-Mg rise that the text read never reports (L21); the authors attribute the null to dose, duration and "erratic bioavailability of oral preparation" (L22); **verifier additions:** the EEG p 0.04 (or 0.003) is not reproducible from Table 2 (a Fisher test gives about 0.10); EEG denominators are 26 in one place and 22 in another; Table 3 margins disagree with Table 2 |
| Hou 2019 Neuropsychiatr Dis Treat, PMID 31806980 | Healthy mice, oral magnesium in drinking water: sulfate raised serum Mg to about 2.2 mM and left cerebrospinal fluid unchanged; threonate raised cerebrospinal-fluid Mg from 0.89 to 1.17 mM (L13, L14); the CSF value is "actively regulated" (L16) | selected passages (staged receipt `...31806980-01`) | exposure datum, mouse | Six mice per subgroup in the design; the Discussion prints "21.6 %" for what the Results values make +31 % (L15); an MPTP Parkinson model arm was not read |
| J Physiol 2014, PMID 24614743 | The voltage dependence above | selected passages (staged receipt `...24614743-01`) | physiology | Not cortex; not WWOX |
| Slutsky 2010 Neuron, PMID 20152124 | Magnesium L-threonate raising brain Mg in rats improved learning and increased NR2B-containing NMDAR expression (abstract) | **abstract only**; no open full text | exposure and a cautionary NMDAR-upregulation signal | Rat, behaviour; the NR2B upregulation is a possible compensation to chronic raised Mg2+ and is unmeasured in any WWOX system |
| Epilepsy Res 2012 hypothesis article, PMID 22406257 | States that low-Mg2+ perfusate is "a common method of generating spontaneous epileptiform discharges" from rat hippocampal slices | abstract only | supports the premise only | A hypothesis article, not data |
| Febrile seizure children, PMID 30193581 | Lower serum ionised Mg in children with febrile seizures than in controls | abstract only | association only | The abstract itself says causation is not shown |
| Cochrane, PMID 26259048 | One trial of magnesium sulfate for post-traumatic seizure prevention: late seizure RR 1.07 (0.53 to 2.17) | abstract only | null | Different aetiology; intravenous |
| Eclampsia reviews, PMID 39054515 | Magnesium sulfate is "the most utilized anticonvulsant" for eclampsia (abstract) | abstract only | a different mechanism and population | Serum levels there are far above any supplement; not an NMDAR-gate argument |

Association (low serum Mg in febrile seizure) is not modulation (Mg lowers NMDAR gain in physiology and abolishes none of the
WWOX bursts in any experiment), and neither is rescue. Nothing above reaches the third rung for WWOX-DEE.

---

## 5. Counter-evidence and rivals to the mechanism, in one place

1. **Permissive, not necessarily gain.** The paper says NMDAR transmission is "a requirement" (L05). A partial reduction of a
   permissive component need not stop bursts. Card F01 holds the same objection for memantine.
2. **The slice already has magnesium** (E2), so the knockout bursts despite a normal block. The lever is the excess relief, not
   a missing block.
3. **Exposure.** Brain extracellular Mg2+ is regulated; oral sulfate did not change cerebrospinal-fluid Mg in the mouse, and no
   human cerebrospinal-fluid response to an oral preparation was found (S22: six hits, none on this).
4. **Infants.** In the one randomised trial read with an oral phase (intramuscular magnesium sulfate for three days then oral, on top of ACTH and antiseizure drugs in both arms), seizure control did not change; the positive signal is
   intravenous and abstract-level.
5. **Sign by lesion.** Memantine benefit in GRIN-variant epilepsy depends on whether the receptor lesion is gain-of-function
   (14 of 19) or not (3 of 15) (needs O5, abstract- and card-level). A Mg2+ rise lowers NMDAR gain whatever the lesion, so if the
   receptor is hypofunctional in a subpopulation of neurons, lowering gain could be harmful. Unmeasured in WWOX.
6. **Chronic NMDAR dampening in a developing brain.** Activity-dependent myelination and synaptic maturation depend on glutamate
   signalling (needs `NEED-MYELINATION`; cards F02/H02). No Mg2+ datum in a WWOX system. Slutsky 2010 describes NR2B upregulation
   with chronic raised brain Mg (abstract), a possible compensation.
7. **No deficiency premise.** No serum or cerebrospinal-fluid Mg measurement exists for WWOX-DEE; any intervention would be
   supplementation above baseline, not repletion. The infant trial's subgroup finding (response better with normal initial serum
   Mg, p 0.003) points away from a repletion logic and rests on subgroups of 9 and 18 (intervention arm) whose table rows do not add up.
8. **Not the pannexin/gap-junction node.** The burst is also reduced by carbenoxolone and raised (untested) by a pannexin blocker
   (needs O4); magnesium does not address that arm.
9. **Heterozygote.** Bursts in 4 of 23 heterozygote slices (17 %) with an intermediate resting potential; human carriers are
   clinically well. A Mg2+ effect that scales with resting potential would predict an intermediate effect in them: untested.

---

## 6. Chemical form, composition, accessibility, with uncertainty

The active species is the Mg2+ ion; **the preparation decides what reaches the brain** in the single mouse dataset read, and
nothing else about forms is sourced here (salt elemental content, absorption and gastrointestinal tolerance of each form are
UNVERIFIED in this record).

| Form | Catalogue record (checked with `catalog_build.py query`, not grep) | DSLD name probe 2026-10-29 (full-text hits; sample of 50 labels with an ingredient named exactly so) | EU registers (name match, EU Open Data Portal files) | Brain-exposure datum read |
|---|---|---|---|---|
| Magnesium (element) | `CAT:CHEMBL1201230` MAGNESIUM, `marketed_unapproved_us`; Rx 2 and OTC 5 NDC products by UNII; supplement via DSLD group 82 "Magnesium" (name-only) | 77,199; 50 of 50 | health claims: 31 entries (18 authorised, 13 not) | — |
| Sulfate | `CAT:CHEMBL3989857` MAGNESIUM SULFATE, `approved_any_source`, Rx 56 and OTC 34 NDC products; **ChEMBL mechanism "Unknown"** | 358; 19 of 50 | 0 | mouse oral: serum up, CSF unchanged (L13); human intramuscular/intravenous in the infant series |
| L-threonate | **no catalogue entry** (L-threonic acid `CAT:CHEMBL2152047` is a different record, `experimental`) | 184; 13 of 50 ("Magnesium L-Threonate") | **Novel Food catalogue: "Authorised novel food"** (Union list, Implementing Regulation (EU) 2017/2470; conditions of use not read by me; the verifier reports Commission Implementing Regulation (EU) 2024/2694: **adult food supplements only, pregnant and lactating women excluded**, so the authorisation does not cover children; the maximum level could not be verified, two summaries disagree) | mouse oral: CSF +31 % (L14) |
| Citrate | `CAT:CHEMBL3989480`, Rx 1, OTC 76, supplement | 29,280; 1 of 50 | 0 | none |
| Oxide | `CAT:CHEMBL1200572`, supplement | 12,366; 8 of 50 | 1 health-claim entry, non-authorised | none |
| Glycinate / bisglycinate | `CAT:CHEMBL2108424` (glycinate; the bisglycinate query returns the same record) | 16,847 / 806; 4 / 7 of 50 | 0 | none |
| Chloride | `CAT:CHEMBL3185229` | 305; 29 of 50 | 0 | none |
| Taurate, malate | no entry | 92 / 28,813; 8 / 11 (+16 by group) of 50 | 0 | none |
| Aspartate | `CAT:CHEMBL2109228` | 2,512; 4 of 50 | 0 | none |

* DSLD counts are **full-text hits in the US label database**, name-only; "N of 50" is among the first 50 returned, not a
  frequency. All forms sit under DSLD ingredient group 82 "Magnesium" (mineral) or group 7577; the nonsense control returned 0
  (`dsld_probe_magnesium.tsv`, `dsld_groups_magnesium.tsv`).
* EU health-claim register: the authorised wordings that contain "magnesium" are about tiredness and fatigue, electrolyte
  balance, energy-yielding metabolism, normal functioning of the nervous system, muscle function, protein synthesis,
  psychological function, bones, teeth and cell division (`eu_mg_probe.py` prints them). **Nothing about seizures, epilepsy or
  children**, and claim wording attaches to foods meeting conditions of use that I did not read.
* **Italy was not checked.** The Italian supplement register is behind a bot challenge and was not bypassed; The catalogue README's look of 2026-10-28 found no supplement list in the AIFA or EMA open data (not verified here). US classification and EU-register presence are not Italian status. UNVERIFIED.
* **Catalogue limitations found.** An ion is not a ligand: ChEMBL curates mechanism "Unknown" for the sulfate; the DGIdb record
  carries the NMDA receptor only as a TTD claim named `N-METHYL-D-ASPARTATE RECEPTOR` with gene `NULL` (licence class C,
  identifiers only); and **target queries by GRIN1, GRIN2B and the receptor's claim name return 74, 94 and 0 entries, none of
  them magnesium**. A target-to-compound search would therefore not have surfaced this lever. Proposed: add the physiological
  ion to the catalogue's non-molecule or "endogenous modulators" handling (a curator decision; section 7).

---

## 7. Proposed edits (patch files; none applied)

All patches apply with `git apply` at the base commit of this branch and were checked by running the repository tools on the
patched tree before reverting it (section 9).

| Patch | Effect | Checked by |
|---|---|---|
| [`proposed_needs_edit.patch`](proposed_needs_edit.patch) | `needs/needs.json`: two observations (O6 resting-potential gradient; O7 the bath contains magnesium) and one inference on `NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR`; two counter-evidence lines; the do-not-assume sentence; this README as a document source | `needs/check_needs.py` -> OK, 22 needs, 73 observations (71 before) |
| [`proposed_cards_edit.patch`](proposed_cards_edit.patch) | `cards/F01_glutamate_receptor_node.packet.json` and its rebuilt `.card.json`: cross-reference to the magnesium card and one `not_known` line; `catalog/card_identity_declarations.tsv`: one row (`CHEMBL1201230`, role `identity`, the element record; salts not asserted) for the new card id | `cards/check_cards.py` -> 0 problems |
| New card, not in the patch because adding it changes derived counts | [`card/P11_magnesium_nmdar_gate.packet.json`](card/P11_magnesium_nmdar_gate.packet.json) and `.card.json` (built by the bridge, `directional_summary` UNRESOLVED, `assessment` REQUIRES_QUALIFICATION) | copied into `cards/` for the check: 25 packets, 0 problems; then removed |

Applying the card additionally needs the derived files regenerated by their own tools (`join/`, `view/`, `card_links.json`,
`catalog_stats.json`, the module README's card count). That was not done here. `needs.md` says "63 observations" while
`check_needs.py` counts 71 on the unpatched tree; I left it alone.

---

## 8. What would decide it (measurements, in order of cost) and the card's preregistered predictions

1. **Ex vivo titration (cheapest, decisive for the node).** Knockout, heterozygote and wild-type neocortical slices at P13 to P17
   in the source's own medium; bath Mg2+ varied in both directions around the slice's value, then d-APV; endpoints burst
   incidence, frequency, duration, amplitude; then NMDA:AMPA ratio under voltage control. Predictions registered before any
   result: (a) a rise no larger than what the most brain-penetrant preparation produced in mouse cerebrospinal fluid lowers
   bursts in knockout slices and leaves the other genotypes alone; (b) bursts that need a rise beyond any reachable exposure
   close the strand, d-APV remaining the ceiling; (c) lowering Mg2+ raises burst incidence in wild-type and heterozygote slices
   more than in the knockout (ceiling effect).
2. **Exposure.** Total and ionised Mg in serum and cerebrospinal fluid of knockout versus control mice, then the cerebrospinal-fluid
   response to one oral preparation in the same animals. A human value for any preparation is the second missing datum.
3. **Safety of the direction** before any chronic use: a myelination and synaptic-maturation endpoint in the developing
   knockout under graded Mg2+.
4. **Premise check:** is Mg2+ different in WWOX-DEE at all? Surplus samples from existing studies could answer it.

---

## 9. Provenance, reading depth, receipts, reproduction

* **Reading depth, honestly.** `PMID 34634460`: selected passages (queried, not a full re-read), after two earlier complete reads
  receipted in the ledger. `PMID 35222658` and `PMID 36967744`: main text read, depth `partial_fulltext_read` (flow-chart image
  not opened, supplement not accessed, references not read, no verbatim-locator work manifest built). `PMID 31806980` and
  `PMID 24614743`: selected passages only (`queried_not_full_read`). `PMID 20435238`, `20152124`, `22406257`, `30193581`,
  `26259048`, `39054515`, `37406874`, `32241292`, `38407561`: abstract only (an abstract is not a read). PMC6570236 (Jahr and
  Stevens): not read.
* **Staged receipts** (never written to the ledger): `disease-models/wwox/research/receipt_staging/scientist-b/`
  `FTR-20261029-34634460-04.json`, `...-35222658-01.json`, `...-36967744-01.json`, `...-31806980-01.json`,
  `...-24614743-01.json`, all validated with `validate_receipt` and `validate_new_receipt` and containing no claim about the
  ledger's contents. The integrator records them.
* **Where the bytes are.** The five article files are not in git (`files/` is ignored) and were **not** copied into the shared
  checkout (instructed not to touch it): the 34634460 file is `files/fulltext/PMID34634460_Wwox_osc2021_PMC_r2.xml`, sha256
  `b01bfa4f...`; the other four were fetched with `curl` (GET, no registration, no contact string) from
  `https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML` on 2026-10-29: PMC8752995 `6f8ae74e32433cdcb0347bf364b9dc4c52e676d1a924740797687c96f23ab348`,
  PMC10030695 `1f08e87990e3ba67605bb6155e8c0aa244db86e47db9f982ac83d064a1207895`, PMC6857673
  `3e9d335fdcea20c7d5cfeede9aa10ce318688b7dd6f945355770c7fa89394724`, PMC4027860
  `1ecd1c7d8cdc744a7354557fbf71b218ef330da9eae77636e54a5c9c78dce28b`. Python's default `urllib` agent received HTTP 503 from
  the same endpoint while `curl` received 200; I did not vary the agent further. A verifier re-acquires by this recipe and checks
  the digest; a digest difference is a finding about the publisher, not tampering by default.
* **Quotations.** [`locators.tsv`](locators.tsv) lists 26 verbatim quotations; `quote_check.py` extracts a text layer from the
  XML exactly as documented in its header and requires each quotation to appear in it. Run on 2026-10-29 against the files above:
  26 of 26 match, 0 failures (`python3 -I quote_check.py KEY=path ...`; output in `quote_check_output.txt`). Table 1 is quoted with its cells run together because
  that is how the text layer renders them. The quotations were not hand-corrected.
* **Probes.** DSLD: `catalog_build.py probe-dsld` and `probe-dsld-groups` with `LEGEND_CATALOG_CACHE` pointed at an empty
  scratch directory so the shared cache stayed untouched; the tool nevertheless rewrote the tracked `catalog/cache_manifest.json`
  (it pins the probe files by digest), which I restored from `HEAD` before committing. **Finding for harness engineering:** a
  scratch `LEGEND_CATALOG_CACHE` does not isolate `probe-dsld` from the tracked manifest. EU registers: the already-cached files
  read by `eu_mg_probe.py`; nothing was fetched. No e-mail or contact string was sent to any service (the tool's user-agent
  carries none).
* **Tool problems met.** `lookup_article_by_citation` rejected my parameters; a PubMed query with OR between gene names was
  split by the engine (S11) and discarded; PubMed full-text retrieval was not used because Europe PMC returned the open XML.
* **Files in this directory.** `README.md`; `searches.tsv`; `locators.tsv` + `quote_check.py`; `mg_block_arithmetic.py` +
  `mg_block_arithmetic_output.txt`; `quote_check_output.txt`; `dsld_probe_magnesium.tsv`, `dsld_groups_magnesium.tsv`; `eu_mg_probe.py`, `eu_mg_probe.tsv`;
  `proposed_needs_edit.patch`, `proposed_cards_edit.patch`; `card/` (builder, packet, card).

## 10. UNVERIFIED (explicit list)

1. That the recording perfusate in PMID 34634460 equals the incubation ACSF (no sentence says so).
2. Every parameter of the arithmetic that is not a quoted value (section 3.2); the Jahr and Stevens source was not read.
3. Whether the NMDAR dependence of the burst involves magnesium-sensitive receptors at all (no subunit data).
4. Brain extracellular free Mg2+ response to any preparation in any human; any human cerebrospinal-fluid Mg after oral intake
   (S22 found none; the search is limited to what the PubMed engine returned).
5. The conditions of use of the EU Novel Food authorisation of magnesium L-threonate; the population it covers.
6. Everything about Italian availability or classification.
7. Salt-specific elemental content, absorption, tolerability and interactions (not sourced here).
8. All abstract-only items of section 4, including the inferential statistics of Zou 2010.
9. The remaining 69 full-text WWOX and magnesium hits in Europe PMC (S24) and the 25 WWOX/spasm hits of S07.
10. Whether a longer search (for example in Chinese-language trials of magnesium in infantile spasms) changes section 4.
11. Every INFERENZA in the card and in section 3: owed a blind audit by someone other than the producer.
