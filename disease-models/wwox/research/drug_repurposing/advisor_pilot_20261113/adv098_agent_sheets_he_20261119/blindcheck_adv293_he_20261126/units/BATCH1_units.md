# Sheet batch 1: BATCH1_ethosuximide_lithium_memantine_HE_20261119.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## ADV-098 batch 1: data sheets for ethosuximide, lithium, memantine (HE, 2026-11-19)
U1.1 (L5) Routes read, all dated 2026-11-19: identity by `compound_identity.py` (raw answers in `identity/`); measured activities by the ChEMBL adapter by molecule id (raw answers in the root checkout `files/adv098_agent_sheets_raw_he_20261119/` with digests in `SHA256SUMS_raw_activities.txt`, recipe in `RECIPE_pull_activities.txt`, tabulation in `recipe_tabulate_activities.txt`, rows on the expected targets in `activities_expected_targets.tsv`, the others summarised in `other_targets_summary.json`); exposure existence by PubMed searches (titles or abstracts read where named, full texts not read); label by the openFDA adapter (SPL text, indications and pediatric-use sections only).
U1.2 (L5) The assay conditions are the ChEMBL `assay_description` text; the conditions that decide comparability (Mg2+, holding potential, agonist concentration, temperature) are often absent from it, so potencies are **not** set side by side here, and the shipped `assay_conditions.py` reads the package tables' conditions, not ChEMBL text.

## Ethosuximide (ChEMBL CHEMBL696, NAME_EXACT)
U1.3 (L8) **Targets and potency (measured, human or unknown origin):** T-type calcium channel alpha1I (CACNA1I), IC50 greater than 5 mM in a FLIPR assay (document CHEMBL1140166, 2008; ChEMBL flags the value "outside typical range"); T-type calcium channel, unknown origin, IC50 0.6 mM (document CHEMBL4229462), a row ChEMBL leaves **without a mapped gene** (target "Unchecked"), so it does not count as CACNA1G, H or I; ChEMBL flags this row "outside typical range" too.
U1.4 (L8) CACNA1G and CACNA1H: evidence level CURATED_MECHANISM only, no measured value read for them under this id.
U1.5 (L8) The two values are not comparable: a different assay, one at a single channel subtype.
U1.6 (L8) In vivo (CD-1 mouse, intraperitoneal): scPTZ clonic seizure EC50 140.4 mg/kg; the electrical-stimulus assay EC50 greater than 200 mg/kg (document CHEMBL5113514); these are doses, not exposures.
U1.7 (L9) **Selectivity / off-targets:** `NOT_ASSESSED` by design.
U1.8 (L9) 292 activity rows in all, only 1 on an expected target by gene symbol; 127 other targets appear (mostly DrugMatrix panels with no value, "Unchecked"; adenosine receptors, acetylcholinesterase, CYP3A4 each in 2 to 3 rows): a target named in a row shows the compound was reported against it, not that it binds.
U1.9 (L10) **Rodent exposure (PubMed):** published, in adult mice and rats, not juvenile.
U1.10 (L10) El Sayed 1978 (PMID 708147, abstract read): in mice serum and brain concentrations equilibrate within 10 minutes and the half-life is about 1 hour (rats about 10 hours; cerebrospinal fluid reached in dogs within 20 to 30 minutes).
U1.11 (L10) Total brain concentrations measured in mouse drug-interaction studies: PMIDs 17085857, 22789660 (free plasma and total brain), 18566800, 16140589 (abstracts read).
U1.12 (L10) Route 1 (brain, concentration, pharmacokinetics, mice) 19 records; route 2 (cerebrospinal fluid, rat) 1 record, the dog paper.
U1.13 (L10) **Not found by these routes:** a free brain concentration, a cerebrospinal fluid concentration in a rodent, any value in juvenile mice.
U1.14 (L11) **Label (openFDA SPL, 3 labels, newest 2026-05-25):** indicated for absence (petit mal) epilepsy; "safety and effectiveness in pediatric patients below the age of 3 years have not been established".
U1.15 (L12) **Not measured or not found:** potency at CACNA1G and CACNA1H under this id; a T-type value in a native thalamic neuron preparation (not in the rows read); free brain exposure; any juvenile-mouse exposure.

## Lithium (ChEMBL CHEMBL1201333 "LITHIUM", NAME_EXACT; salts CHEMBL1200826, CHEMBL1201170 not merged)
U1.16 (L15) **Targets and potency:** the ChEMBL answer for the parent record holds **no activity row** (0 of 0, coverage COMPLETE) and no curated mechanism row by the name route; for the expected GSK3B, IMPA1 and IMPA2 every source read returned EMPTY_RESULT.
U1.17 (L15) So no measured GSK-3 or inositol monophosphatase potency is available from these routes; whatever is known for lithium on these enzymes is in the primary literature, not read for this sheet.
U1.18 (L15) Not found by these routes, not zero.
U1.19 (L16) **Selectivity / off-targets:** `NOT_ASSESSED`; nothing to assess from these sources.
U1.20 (L17) **Rodent exposure (PubMed):** published, adult mice.
U1.21 (L17) Heurteaux 1991 (PMID 1860065, abstract read): plasma total lithium kept near 0.28 mM, brain 0.65 mM (cerebellar white matter) to more than 2 mM (thalamus), brain-plasma exchange within minutes; Bhuiyan 2025 (PMID 40095208): brain and blood lithium after oral or intranasal LiCl in wild-type mice, brain/blood ratios; also PMIDs 6543005, 21306560 (serum and brain lithium in strains), 707123, 1005485.
U1.22 (L17) Route 1: 17 records.
U1.23 (L17) **Not found by these routes:** juvenile-mouse values; the brain concentration at a dose that is stated as a free concentration.
U1.24 (L18) **Label (openFDA SPL, 3 labels, newest 2026-04-27):** mood stabilizer for bipolar I disorder; the pediatric section states safety and effectiveness established for ages 7 to 17 years in an acute-phase trial for monotherapy (text read in part).
U1.25 (L19) **Not measured or not found:** every potency value for the targets of interest; the ion's effective brain concentration at the target; juvenile exposure.

## Memantine (ChEMBL CHEMBL807, NAME_EXACT; the hydrochloride record CHEMBL1699 is separate)
U1.26 (L22) **Targets and potency (measured):** 84 activity rows; 38 on NMDA receptor subunit symbols, 22 of them human.
U1.27 (L22) Human recombinant GluN1/GluN2A IC50 spans 0.95 nM to 31.6 microM across documents; GluN1/GluN2B 0.78 to 25.6 microM; GluN2C 3.2 microM and GluN2D 10 microM in one 2025 document (CHEMBL6115009, CHO cells).
U1.28 (L22) Within one 2024 document (CHEMBL6083260) the same receptors read 0.84 and 0.78 microM in one assay and 28 and 26 microM in another: the assay, not the receptor, drives the spread.
U1.29 (L22) Rat native NMDA receptor, cerebellar granule neurons: IC50 1.5 microM against an NMDA-induced calcium signal and 55 microM against a glutamate-induced signal in the same documents (CHEMBL1151696, CHEMBL1152149, CHEMBL1157696).
U1.30 (L22) Binding Ki 0.54 to 1.2 microM (several documents, symbol list covers all NMDA subunits at once).
U1.31 (L22) The 0.95 nM value (document CHEMBL2396530) is an outlier by three orders; it is kept as reported and should be read before any use.
U1.32 (L23) **Comparability:** the values are **not** set side by side: Mg2+, holding potential and agonist concentrations are not in these text cells (some say -75 mV holding in oocytes).
U1.33 (L23) Any exposure-to-effect step must pick the assay first.
U1.34 (L24) **Selectivity / off-targets:** `NOT_ASSESSED`; 24 other (target, species) entries outside the human subunit rows, which include rat NMDA receptor rows as well as acetylcholinesterase, cholinesterase and parasite targets; not selectivity.
U1.35 (L25) **Rodent exposure (PubMed, titles read):** published in rats and mice: "Distribution of memantine in brain, liver, and blood of the rat" (PMID 6891224, 1982); "Acute pharmacokinetics of memantine in the mouse" (PMID 22068149, 2011); "Pharmacokinetic Properties of Memantine after a Single Intraperitoneal Administration and Multiple Oral Doses in Euploid Mice and in the Ts65Dn Mouse" (PMID 28557265, 2017); 133 records in a rat brain-concentration search and 30 in a mouse pharmacokinetics search.
U1.36 (L25) Abstracts and full texts were not read.
U1.37 (L25) A first search combining rat, mouse and cerebrospinal fluid returned 0 records: a query-shape result, not an absence.
U1.38 (L25) **Not found by these routes (not read):** juvenile-mouse values and free brain concentration.
U1.39 (L26) **Label (openFDA SPL, 3 labels, newest 2026-09-01):** moderate to severe dementia of the Alzheimer's type; "safety and effectiveness in pediatric patients have not been established"; the label states failed efficacy in two 12-week controlled studies in children with autism spectrum disorders.
U1.40 (L27) **Not measured or not found:** a Mg2+-matched potency per GluN2 subunit in one assay (SCI asked for this for ketamine and d-APV in batch 4; ADV-050 already holds memantine and ketamine kinetics: cite it, do not recollect); juvenile exposure.

## What changes for SCI's exposure-effect choice (batch 1)
U1.41 (L30) For none of the three agents can a potency at the model's target be paired with a free brain concentration in juvenile mice from these routes.
U1.42 (L30) The pairing needs the primary papers SCI's delegate reads.
U1.43 (L31) Ethosuximide has almost no measured potency in ChEMBL (one gene-mapped row, greater than 5 mM; one unmapped row, 0.6 mM).
U1.44 (L31) A mapping from this class to a T-type effect would rest on a literature value that is not in these sources.
U1.45 (L32) Memantine has many values and they disagree by about two orders by assay (IC50 and Ki rows from 0.54 to 55 microM, one rat Ki above 100 microM), setting aside the 0.95 nM row that the dated lines below judge a probable unit error; the assay must be chosen before the number.
U1.46 (L33) Lithium has no measured target potency here at all.

## Dated line 2026-11-19 (late): the memantine 0.95 nM GluN1/GluN2A value read at source (ADV rule 9)
U1.47 (L36) The row is ChEMBL activity 13348817, IC50 = 0.95 nM (pChEMBL 9.02), document CHEMBL2396530 = Saiki et al., Bioorg Med Chem Lett 2013 (PMID 23692871, "In vitro and in vivo evaluation of polymethylene tetraamine derivatives as NMDA receptor channel blockers").
U1.48 (L36) ChEMBL's assay text: recombinant GluN1/GluN2A (unknown origin) in Xenopus oocytes, glycine/glutamate-induced inward current at -70 mV, two-electrode voltage clamp.
U1.49 (L36) What I could read: the abstract only (no PMC full text, not open access): memantine is the **comparator** and the tetraamines "exhibited stronger channel block activities in comparison to memantine in Xenopus oocytes voltage clamped at -70 mV"; the abstract gives no memantine IC50, and Mg2+ and the agonist concentrations are not in the ChEMBL text.
U1.50 (L36) The 2007 document (CHEMBL1146243) records 911 nM for memantine at GluN1/GluN2A under the same described configuration (oocytes, voltage clamp).
U1.51 (L36) **Status: unresolved, not usable.**
U1.52 (L36) Three orders apart under one described assay means either a different condition that the text omits or a unit or curation error; the full text table would decide, and I could not reach it by these routes.
U1.53 (L36) Treat 0.95 nM as "not confirmed" and keep the 0.84 to 6.7 microM band for human recombinant GluN1/GluN2A as the working range, with the assay stated.
U1.54 (L36) This band is not the range of all rows: it holds six of the eight human recombinant GluN1/GluN2A rows left, and 28.1 microM (CHEMBL6083260, -40 mV) and 31.6 microM (CHEMBL6115009, calcium flux, 24 hours) lie above it.

## Dated line 2026-11-20 (00:30Z): the memantine 0.95 nM value, second step: an internal consistency check inside the source's own assay
U1.55 (L39) ChEMBL assay CHEMBL2399396 (the one behind the 0.95 nM row) holds seven rows: five tetraamine compounds at 4.2, 11.0, 89.3, 256.7 and 315.0 nM, methoctramine at 138 nM, and memantine at 0.95 nM.
U1.56 (L39) The paper's abstract (PMID 23692871, the only part I could read) says that **all** the tetraamines exhibited stronger channel block than memantine in this configuration.
U1.57 (L39) If that is right, memantine's IC50 must be **above** the weakest tetraamine, i.e. above 315 nM.
U1.58 (L39) The ChEMBL entry of 0.95 nM makes memantine the **most** potent compound of the set, which contradicts the abstract.
U1.59 (L39) A value of 0.95 **micro**molar (950 nM) would be consistent with the abstract (above all five tetraamines) and with the 911 nM that the 2007 document gives for memantine at GluN1/GluN2A.
U1.60 (L39) **Reading: very probably a unit error in the ChEMBL record (a micromolar value entered as nanomolar).**
U1.61 (L39) This is an inference from the abstract and the sibling rows; the paper's table was not read (not open access; no route to it here).
U1.62 (L39) Do not use 0.95 nM; use the 0.84 to 6.7 microM human recombinant band with the assay stated, and treat the 0.95 value as 0.95 microM only after the table is read.

## Dated line 2026-11-20: correction from SCI's verified reading (origin: SCI, not re-read by HE)
U1.63 (L42) The sentence "not found by these routes: ... any value ... total brain concentration with a number" for ethosuximide needs this correction: SCI's verified reading reports a mouse **total brain ethosuximide concentration with a number**, 134.9 microg/g at 72.3 mg/kg intraperitoneally (PMID 22315091); nothing at 150 mg/kg (the regimen in Cheng 2020, which reported no levels).
U1.64 (L42) The mouse papers I found by title (17085857, 22789660, 18566800, 16140589) have brain concentrations measured but no absolute value in their abstracts; PMID 22315091 was not among my hits.
U1.65 (L42) Still not found: a free brain concentration, a cerebrospinal fluid concentration in a rodent, a juvenile value.
U1.66 (L42) SCI's round-2 report also separates ezogabine's 2.23 and 3.58 microM brain EC50 as **different experiments** (Kunming mice against CF-1 mice; plasma EC50 9-fold apart): this settles the open "same experiment?" question of batch 2.

## Dated addition 2026-11-20 (evening): the ethosuximide anchor's Methods and the open routes, from SCI's ADV-122 (origin: SCI, not re-read by HE)
U1.67 (L45) Source: SCI's `RESULT_ADV122_SCI_20261120.md` (merge 13efa8e80), with `OUTPUT_quote_check.txt` (two phrases found in the fetched bytes by SCI; I did not open PMID 22315091 myself).
U1.68 (L45) It adds three things to the line above and to the "Rodent exposure" bullet.
U1.69 (L45) Reference genotype class only; hypothesis level; a quoted regimen is not a dose proposal; not medical advice.
U1.70 (L46) **What the anchor's Methods say (PMID 22315091):** whole brains were homogenised in distilled water 1:2 (w:v); the concentration is "expressed in ug/g of wet tissue"; no sentence mentions back-correcting the dilution, so the unit (per g of tissue or per g of homogenate) is not settled by the text.
U1.71 (L46) The row 134.9 microg/g belongs to the arm "ETS (72.3) + saline": **72.3 mg/kg is the ED50 of ethosuximide in combination with sildenafil 40 mg/kg, and the value quoted is the saline-vehicle arm** (male Swiss mice, 24 to 30 g, drug 45 minutes before the test).
U1.72 (L46) The earlier dated line gives 134.9 microg/g at 72.3 mg/kg without this qualifier; read it with it.
U1.73 (L47) **No juvenile level in the sources SCI reached**, at any age and in any matrix.
U1.74 (L47) SCI's prior bound for the P12 to P17 pup at the regimen of Cheng 2020 is a chain of inferences (two routes kept apart; outer bounds roughly 0.2 to 4.2 mM total brain, 5.4 mM central only in the disfavoured per-g-homogenate reading); it is SCI's inference, not a datum, and is not copied into the sheet's rows.
U1.75 (L48) **SCI's mass-balance finding (inference, origin SCI):** the anchor's 0.956 mM (per g of tissue) is at or above the ceiling dose over volume of distribution for 72.3 mg/kg, so the adult anchor is itself uncertain by about a factor 2; the "about 2 to 6 mM" adult band has no other source in the repository than a linear scaling of that anchor.
U1.76 (L48) This bears on how the 0.6 mM and 5 mM-class potency rows above are compared with an exposure; it changes no measured row here.
U1.77 (L49) **Open routes named by SCI (not absences):** full texts of three juvenile pharmacodynamic papers from one laboratory (one may print plasma levels), El Sayed 1978 full text (mouse dose, strain, any table), Mizuno 2023 paediatric population model, Giaccone 1996 full text, mouse Cyp3a11 and Cyp2e1 activity at P12 to P17, mouse renal function at P10 to P20.
U1.78 (L50) Consumption proposed by SCI for v3.1 3.2 and 6.2 and for IT is addressed to ADV; not mine to write.
