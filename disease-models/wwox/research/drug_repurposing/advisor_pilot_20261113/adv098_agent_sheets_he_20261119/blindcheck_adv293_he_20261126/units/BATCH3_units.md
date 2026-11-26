# Sheet batch 3: BATCH3_ganaxolone_gaboxadol_HE_20261119.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## COMPARABLE?
U3.1 (L6) **Ganaxolone and gaboxadol: not comparable.**
U3.2 (L6) Ganaxolone is read as a positive allosteric modulator (potentiation of the GABA response, EC50); gaboxadol as a direct agonist (activation EC50 or binding).
U3.3 (L6) A modulator's EC50 and an agonist's EC50 are different quantities, and each depends on the GABA concentration used, which the ChEMBL text rarely gives.
U3.4 (L6) No order is read.
U3.5 (L7) **Ganaxolone, alpha1beta2gamma2 against alpha4beta3delta (the synaptic-against-extrasynaptic question):** EC50 266 nM at alpha1beta2gamma2 (LTK cells) and 103 nM at alpha4beta3delta (CHO cells) in one document (CHEMBL3425450, 2015).
U3.6 (L7) Two cell lines in one paper: a 2.6-fold difference is an indication, not an identified contrast; the GABA concentration used, the efficacy (maximal potentiation) and the temperature are not in the text.
U3.7 (L7) Alpha1beta2gamma2 across documents: 260 nM (oocytes, 1997), 266 nM (LTK cells, 2015), 200 nM (oocytes, 2018): consistent within a factor of 1.3 across three assay systems.
U3.8 (L7) Alpha2beta1gamma2 100 nM against alpha1beta2gamma2 200 nM in the same oocyte document (CHEMBL5260830, 2018): within one document, a 2-fold difference.
U3.9 (L8) **Gaboxadol on delta-containing receptors: no value.**
U3.10 (L8) The only functional human value found is EC50 14 microM (14.1 and 14.0 microM, two rows) at alpha1beta2gamma2S (FLIPR, TSA201 cells, 2013); no alpha4beta3delta or alpha4beta2delta row exists in ChEMBL under this id.
U3.11 (L8) The delta preference usually attributed to the compound is **not found by these routes** in measured rows.
U3.12 (L8) So "extrasynaptic versus synaptic" cannot be read for gaboxadol from these sources.
U3.13 (L9) **Species and system:** most gaboxadol binding values are rat brain membranes (IC50 31.5 to 160 nM, [3H]muscimol or [3H]GABA displacement, 1983 to 2013), which measure the high-affinity site binding, not function.

## Ganaxolone (ChEMBL CHEMBL1568698, NAME_EXACT)
U3.14 (L12) **Targets and potency:** 8 rows.
U3.15 (L12) EC50 (potentiation) 266, 260 and 200 nM at alpha1beta2gamma2 (three systems), 103 nM at alpha4beta3delta (CHO), 100 nM at alpha2beta1gamma2 (oocytes); [35S]TBPS or [3H]TBPS displacement IC50 80 and 42 nM in rat cortical membranes; Ki 790 nM (unspecified receptor preparation, 2024).
U3.16 (L12) The ChEMBL symbols for the multi-subunit rows list every GABA-A alpha subunit (a ChEMBL target-group mapping), so gene-level attribution is not read.
U3.17 (L13) **Selectivity / off-targets:** no row outside GABA-A: the one entry counted apart from the human subunit rows is the rat GABA-A binding row; `NOT_ASSESSED`.
U3.18 (L13) Not found: efficacy (maximal potentiation) per subunit, activity at other receptors, any neurosteroid-site or tonic-current measurement in these rows.
U3.19 (L14) **Rodent exposure (PubMed, titles read):** a rat pharmacokinetic and intravenous study exists (PMID 30552296, 2019, ganaxolone blocks diazepam-resistant lithium-pilocarpine status epilepticus in rats) and a 2001 LC-MS/MS method paper "for the determination of pharmacokinetics" (PMID 11232855, title truncated; the animal species not read).
U3.20 (L14) Brain concentrations: not confirmed by titles.
U3.21 (L14) First search "ganaxolone brain concentration plasma rat mice" 0 records (a long AND query: not an absence); "ganaxolone pharmacokinetics rat" 5 records; a general "neonatal OR juvenile rodent" query was unusable (11,333 records, no ganaxolone paper among the first five).
U3.22 (L14) **Not found by these routes:** a juvenile exposure and a free brain concentration.
U3.23 (L15) **Related, titles only:** "Ganaxolone enhances microglial clearance activity and promotes remyelination in focal demyelination in the corpus callosum" (PMID 31332963, 2020): a myelination-relevant record that bears on the broad objective too, not read.
U3.24 (L16) **Label (openFDA SPL, 1 label, effective 2026-09-04):** indicated for seizures associated with CDKL5 deficiency disorder in patients 2 years of age and older; pediatric section states safety and effectiveness established from age 2 years for that indication.
U3.25 (L17) **Not measured or not found:** efficacy per subunit at one GABA concentration; any measured tonic-current effect; juvenile exposure.

## Gaboxadol (= THIP; ChEMBL CHEMBL312443, NAME_EXACT; "THIP" returned only unrelated partial matches and was not used)
U3.26 (L20) **Targets and potency:** 19 rows; 5 on neither GABA-A nor GABA-rho (two SARS-CoV-2 cytotoxicity rows, one GABA-B, two GABA uptake: no activity up to limits of 20 to 500 microM) and two on GABA-rho1 (formerly GABA-C), Ki 100 microM.
U3.27 (L20) GABA-A binding IC50 31.5 to 130 nM and Ki 160 nM (rat brain membranes); functional: EC50 14 microM at human alpha1beta2gamma2S (FLIPR, TSA201); EC50 335 microM for chloride uptake into mouse brain synaptoneurosomes (2002); EC50 55 microM for inhibition of the CA1 population spike in rat hippocampal slice (1991).
U3.28 (L21) **Selectivity / off-targets:** GABA-B IC50 above 100 microM (rat cortex), GABA uptake IC50 above 300 to 500 microM, GABA-C rho1 Ki 100 microM (HEK293): the high-concentration non-GABA-A rows are listed as read.
U3.29 (L22) **Rodent exposure (PubMed):** "Plasma and CNS concentrations of Gaboxadol in rats following subcutaneous administration" (PMID 17362924, 2007, title read; adult rat, abstract not read).
U3.30 (L22) A mouse brain-concentration search returned 26 records, all pharmacology papers by title (not read).
U3.31 (L22) **Not found by these routes:** neonatal or juvenile exposure (the query "gaboxadol neonatal rat seizures" returned 0 records; a query shape, not an absence; SCI's delegate reports THIP action in P6 to P9 neonatal slices, which is a slice effect, not an exposure).
U3.32 (L23) **Label (openFDA):** NO_MATCH_FOUND for "gaboxadol": not found by this route, not a statement about development status.
U3.33 (L24) **Not measured or not found:** any delta-containing receptor value; free brain exposure; juvenile exposure.

## What changes for SCI's exposure-effect choice (batch 3)
U3.34 (L27) For the synaptic against extrasynaptic question the data separate the two agents unequally: ganaxolone has one cross-cell-line pair (103 against 266 nM, an indication), gaboxadol has none on delta receptors.
U3.35 (L28) Neither agent has a juvenile or free brain exposure by these routes; ganaxolone has a label from 2 years of age for a defined seizure disorder.
U3.36 (L29) Gaboxadol's functional potency (14 microM) sits about 50 to 140 times above ganaxolone's modulation EC50 under different readouts: this difference describes the readouts as much as the agents and is not read as potency order.
