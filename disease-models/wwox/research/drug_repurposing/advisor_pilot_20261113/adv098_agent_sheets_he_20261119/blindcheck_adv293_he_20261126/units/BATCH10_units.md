# Sheet batch 10: BATCH10_broad_tazemetostat_TMP195_10058F4_HE_20261120.md
Each numbered unit is a sentence of the repository sheet, in order. L = line in the sheet.


## Identity (one line per agent, how it was resolved)
U10.1 (L6) | Agent | Resolution | ChEMBL read | Structure key |
U10.2 (L8) | tazemetostat | `compound_identity.py`: NAME_EXACT (a ChEMBL record and a DGIdb record agree) | CHEMBL3414621 (max phase 4 in the molecule record) | PubChem CID 66558664, InChIKey NSQSAUGJQHDYNO-UHFFFAOYSA-N |
U10.3 (L9) | TMP195 | NOT_FOUND_BY_NAME in `compound_identity.py`; resolved by structure: PubChem name lookup, then the ChEMBL molecule with the same InChIKey | CHEMBL4751615 (no preferred name stored) | PubChem CID 67324851, InChIKey QTCSXAUJBQZZSN-UHFFFAOYSA-N |
U10.4 (L10) | 10058-F4 | NOT_FOUND_BY_NAME in `compound_identity.py`; same structure route | CHEMBL1568415 (no preferred name stored) | PubChem CID 1271002, InChIKey SVXDHPADAXBMFB-JXMROGBWSA-N (the E isomer; the 2009 mouse paper writes [Z,E], and which geometric form each study used is not resolved here) |

## COMPARABLE?
U10.5 (L13) **Tazemetostat, EZH2 enzyme potency across documents: not one number.**
U10.6 (L13) IC50 values for the enzyme run from 0.34 nM (2020, AlphaLISA) through 1.0 to 1.2 nM and 2.2 to 4.3 nM to 22 nM (2023) and 170 nM (2024): about a 500-fold range across documents, with different substrates (nucleosome, H3 peptide, SAM), pre-incubation times and PRC2 constructs.
U10.7 (L13) The inhibition constant 2.5 nM (Ki) appears in five documents, the 2015 original (CHEMBL3414551) and four of 2020 to 2023 that quote it: **one origin, not five confirmations**.
U10.8 (L13) Within one document, wild-type EZH2 and the Y641 and A677G mutants are comparable: 1.2 (wild type), 1.7 (Y641F), 2.2 (Y641N), 2.5 (Y641S), 4.3 (Y641C) and 1.9 nM (A677G) in CHEMBL5634131 (2023): a 3.6-fold spread, all within the same assay.
U10.9 (L14) **EZH2 against EZH1: comparable only within a document.**
U10.10 (L14) CHEMBL5634131: EZH2 1.2 nM against EZH1 93 nM (about 78-fold); CHEMBL5331057: 4 against 392 nM (about 98-fold); CHEMBL5584353: 170 against 1,170 nM (about 7-fold); CHEMBL5729508: 2.45 against 140 nM (about 57-fold).
U10.11 (L14) The four documents disagree by more than tenfold on the ratio, so no single selectivity figure is given.
U10.12 (L15) **Cell readouts are a different quantity from enzyme inhibition.**
U10.13 (L15) Reduction of H3K27me3 in cells (EC50 or IC50): 5 to 64 nM in eight lymphoma lines (2021, one document), 20 nM in HeLa (72 h, 2015), 200 nM in G401 (2016, 2021 quotation).
U10.14 (L15) Antiproliferative values are not one number either: in EZH2-mutant lymphoma lines 2.3 to 299 nM in six documents (Pfeiffer, KARPAS-422, WSU-DLCL2), but 14 to 22 microM for lines of that kind in two others (an EZH2-overexpressing description of WSU-DLCL2 and SUDHL4, 2020; SU-DHL-6, 2024); above 3 microM in six wild-type lines (2025); 1.1 to 1.2 microM in MINO and OCI-Ly7 (2024); micromolar values or bounds in other cancer lines.
U10.15 (L15) The exposure time of those growth assays differs and was not read for every row.
U10.16 (L16) **TMP195, class IIa HDAC enzymes: comparable within one document, and the two documents differ by 1.5- to 7-fold.**
U10.17 (L16) 2021 (CHEMBL4732198): HDAC4 354, HDAC5 216, HDAC7 27, HDAC9 16 nM; class I and HDAC8 weak (HDAC1 45,000 nM; HDAC8 2,100 nM).
U10.18 (L16) 2022 (CHEMBL5154665, a different laboratory's assay set): HDAC4 128, HDAC5 148, HDAC7 7.7, HDAC9 2.4 nM and all of HDAC1, 2, 3, 6, 8, 10, 11 above 5,000 nM (a "greater than" ceiling, not a measured value).
U10.19 (L16) The order of potency inside each document is the same (HDAC9 and HDAC7 more potent than HDAC4 and HDAC5); absolute values are not interchangeable.
U10.20 (L17) **TMP195 in cells is weaker than on the recombinant enzymes (about 6- to 420-fold, depending on the isoform).**
U10.21 (L17) Class IIa activity in four cell lines (THP-1, PANC-1, L3.6pl, HT-29) is 0.9 to 1.0 microM in one 2022 document against 2.4 to 148 nM on recombinant enzymes in the same document; a 2021 THP-1 row gives 3.0 microM.
U10.22 (L17) Class I and IIb in cells: above 5 microM (above 30 microM in THP-1, 2021).
U10.23 (L18) **10058-F4: no comparison is possible on the rows.**
U10.24 (L18) Five rows only, all cell growth after 96 h (one 2025 document): 44.7 microM (MDA-MB-231), 39.8 microM (MDA-MB-468), a row without a value (MCF7), 35.1 microM (P493-6 cells expressing MYC) and 59.5 microM (P493-6 with tetracycline, MYC repressed).
U10.25 (L18) The MYC-expressing cells are 1.7-fold more sensitive than the MYC-repressed cells: a weak dependence on MYC, one document, no second one.
U10.26 (L18) **No row on MYC, MAX or MYC-MAX dimerisation at all.**

## Tazemetostat (CHEMBL3414621)
U10.27 (L21) **Potency (163 rows; 60 on EZH2 or EZH1 by gene symbol):** as above.
U10.28 (L21) Also EED rows (2.0 nM enzyme, 40 nM cells; 2017 document), G9a rows (2.9 and 15 nM; two 2025 documents) and PROTAC-document rows (EZH2 degradation IC50 above 10 nM): tazemetostat's role in those documents (comparator, series member or tested agent) was **not read, so none of these rows is used**.
U10.29 (L21) Rows on other target families are antiproliferative only. `NOT_ASSESSED` for selectivity outside the methyltransferases: no kinase or receptor panel row was found by these routes.
U10.30 (L22) **Exposure (PubMed, title and abstract read):** the 2015 Int J Cancer study (PMID 25868794) tested EPZ-6438 (tazemetostat) in wild-type and transporter-knockout mice: **P-glycoprotein (ABCB1) limits its brain accumulation, and the efflux was completely abrogated by elacridar** (a P-gp inhibitor); BCRP is not the limiting transporter for this compound.
U10.31 (L22) The abstract gives no concentration figure for brain.
U10.32 (L22) A 2026 bioRxiv preprint (PMID 42124576, abstract read, **not peer reviewed, full text not read**) reports tazemetostat combined with elacridar in a mouse social-behaviour model; its effect on brain concentration is not read here.
U10.33 (L22) A 2020 paper on convection-enhanced delivery of an EZH2 inhibitor for glioma (PMID 32674144, title read) (title read only; what it showed about exposure is not read).
U10.34 (L22) "Tazemetostat cerebrospinal fluid": 0 records.
U10.35 (L22) **Not found by these routes:** a measured brain or CSF concentration of tazemetostat given alone.
U10.36 (L23) **Label (openFDA SPL, newest 2026-04-29, TAZVERIK):** epithelioid sarcoma in adults and pediatric patients aged 16 years and older; relapsed or refractory follicular lymphoma in adults (accelerated approval).
U10.37 (L23) Safety and effectiveness in patients younger than 16 years **not established**; a 13-week juvenile rat study (post-natal day 7 to 97) reports T-cell lymphoblastic lymphoma from about 2.8 times the adult human exposure, increased trabecular bone, increased body weight and distended testicles; secondary malignancies in adults (warning), embryo-fetal toxicity (animal skeletal abnormalities).
U10.38 (L23) Label text read in part.
U10.39 (L24) **Trials:** ClinicalTrials.gov API v2 intervention search "tazemetostat" returns 61 studies (status fields and results not read; the count is a pointer, not a finding).

## TMP195 (CHEMBL4751615, identity by structure)
U10.40 (L27) **Potency (35 rows):** class IIa enzymes as in COMPARABLE?; no row on a neuronal or brain cell type.
U10.41 (L27) A research compound without a label and with no clinical trial found (ClinicalTrials.gov intervention search: 0 studies).
U10.42 (L28) **Exposure (PubMed):** "TMP195 brain" 2 records (2025 and 2026 papers on astrocytic HDAC7 in amyloid and tau pathology, titles read; whether TMP195 was given to animals and what brain concentration was measured is **not read**); "TMP195 pharmacokinetics mice" 1 record (a 2026 nano-formulation paper for lung tumour macrophages, title read); "TMP195 in vivo mice" 8 records (kidney injury, leukaemia, pancreatic tumour, vascular smooth muscle: titles read).
U10.43 (L28) **Not found by these routes (not read):** a published brain or plasma concentration of TMP195.
U10.44 (L29) **Label:** none (a research compound).

## 10058-F4 (CHEMBL1568415, identity by structure)
U10.45 (L32) **Potency:** the five cell rows above; the primary MYC-MAX dimerisation measurement is the literature's, **not in these rows**: not found by these routes, and not asserted here.
U10.46 (L33) **Exposure (PubMed, abstract read, PMID 18509642, 2009, mice with prostate-cancer xenografts, intravenous administration):** plasma peak about 300 microM at 5 minutes, below detection by 6 hours, terminal half-life about 1 hour; highest tissue concentrations in fat, lung, liver and kidney; peak tumour concentration at least tenfold lower than peak plasma; eight metabolites; **no significant tumour growth inhibition at the two doses tested**, which the authors attribute to rapid metabolism and low tumour concentration.
U10.47 (L33) Brain is not named in the abstract; the full text (PMC2752825) was not read.
U10.48 (L33) "10058-F4 brain": 2 records, neither an exposure study (titles read).
U10.49 (L34) **Label:** none; no clinical trial found (0 studies).

## What changes for SCI's broad unit C and IT's compound-level units
U10.50 (L37) **Tazemetostat has the most complete public data of the three** (enzyme potency in many documents, cellular H3K27me3 readout, a label, a mouse brain-penetration study).
U10.51 (L37) Its brain exposure is limited by an efflux transporter (P-gp) alone, which is a published mechanism for a missing exposure, not a measurement of the exposure; a pediatric label exists only from age 16 and the juvenile rat study flags findings at young ages.
U10.52 (L38) **TMP195 has a clear class IIa selectivity profile on recombinant enzymes in two documents but no exposure, no label and no brain cell data.**
U10.53 (L38) Its class IIa potency in cells is about 6- to 420-fold weaker than on the recombinant enzymes, depending on the isoform.
U10.54 (L39) **10058-F4 has no on-target measurement in ChEMBL, a cell potency of 35 to 60 microM, and a mouse study with a one-hour half-life and low tumour exposure.**
U10.55 (L39) Any comparison with the other broad agents would rest on literature figures not read here.
U10.56 (L40) Compound-level identity for IT: all three have a ChEMBL id and a structure key above; none has a conflict between the sources read.
U10.57 (L40) The "label_conflict" field of the identity tool was empty for tazemetostat.
