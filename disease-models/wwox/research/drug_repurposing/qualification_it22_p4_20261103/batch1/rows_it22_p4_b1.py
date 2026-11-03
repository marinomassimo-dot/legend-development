#!/usr/bin/env python3
"""IT22 P4 batch 1: the four qualification records (data only; build_batch1.py writes the tables from this module). English, no individual-level record."""

COLS = ["proposal_id", "cand_id", "compound", "question_arm", "mechanism_cluster_and_seed_origin", "identity_form_state", "target_action_potency_selectivity", "assay_nature",
        "foundation", "decisive_assumption", "counter_evidence", "next_test", "result_that_would_change_the_decision", "wwox_context_expression", "feasibility_note_exposure",
        "classification", "earlier_appearance", "disposition", "reasons", "status_before", "status_after", "unverified", "why_not_proposed_before", "novelty_class"]

SECOND = ("SECOND_SYSTEM_GATE_FAILED: the shWWOX hNPC library of GSE126075 did not show WWOX lower (3.35 v 2.90 TPM), so it is not an independent second system for this seed "
          "(hnpc_gse126075_it5_20261029/RESULTS.md section 1)")

R = []

# ---------------------------------------------------------------- 0005 pracinostat
R.append(dict(
    proposal_id="IT21P2-0005", cand_id="IT22P4B1-01", compound="pracinostat (SB939)",
    question_arm="Q2 H_HARM (lower glycolytic output / lactate load / HIF activity)",
    mechanism_cluster_and_seed_origin=("HDAC5 -T(+)-> SLC2A1; seeds S017 SLC2A1 up and S025 glycolysis/lactate set up; ONE origin (hNPC GSE126075 + organoid GSE156243, shared IT7 derivation, counted once); "
        "cluster of 19 alternatives (4-phenylbutyric acid, abexinostat, belinostat, CUDC-101, dacinostat, givinostat +13) shares the chain; nanatinostat from the same cluster has its own record "
        "(IT21P2-0006, REJECTED_INFORMATIVE) and is not transferred here"),
    identity_form_state=("ChEMBL CHEMBL1851943 PRACINOSTAT (synonyms SB-939, SB939), hydroxamic acid, MW 358.49, InChIKey JHDKZFFAIZKUCU-ZRDIBKRKSA-N, ChEMBL max phase 3 as served 2026-11-03, "
        "oral small molecule, salt form not stated by the source; GtoPdb ligand 8365 joined through the ligand id (FAM:CAT:CHEMBL1851943); VERIFIED (ChEMBL REST + local GtoPdb release)"),
    target_action_potency_selectivity=("TYPED, never pooled across measure types. IC50, recombinant human enzymes, ONE ChEMBL document (PMID 29360358, J Med Chem 2018, pracinostat as comparator): "
        "HDAC1 50 nM, HDAC3/NCoR2 70 nM, HDAC6 93 nM, HDAC10 82 nM, HDAC2 290 nM, HDAC8 2835 nM, HDAC5 5113 nM (class IIa fluorogenic substrate), HDAC4/7/9/11 > 10000 nM; "
        "so inside that panel HDAC5 is 102-fold weaker than HDAC1. IC50 in the local GtoPdb release (assay class unknown): HDAC5 47 nM, HDAC1 49, HDAC3 43, HDAC10 40 (HDAC5 1.2x the most potent other, "
        "the engine's 'ATTRIBUTABLE'). The two IC50 sources for HDAC5 disagree 109-fold (47 v 5113 nM) and no single document gives both sides of the 47 nM figure. "
        "Ki (a different measure type, PMID 25637120 and a 2012 MedChemComm paper): HDAC5 21 nM, HDAC1 16-28, HDAC2 16-27, HDAC3 19, HDAC4 16, HDAC9 24, HDAC10 23, HDAC11 43, HDAC7 107, HDAC6 247 nM; "
        "Ki and IC50 are not compared with each other. Net: a pan-HDAC inhibitor; HDAC5 engagement is documented (Ki 21 nM, IC50 47 nM in one source) but is not separable from class I/IIb engagement. "
        "No curated ChEMBL mechanism row (absent datum, not a negative)"),
    assay_nature=("all rows are cell-free recombinant-enzyme assays (ChEMBL assay type B); the 47 nM GtoPdb value has no recorded assay context; cellular rows (MCF7, MDA-MB-231, T47D IC50 5340 nM) are "
        "antiproliferative and come from a review compilation, not target engagement. Whether any of these predicts loss of HDAC5 scaffold (non-catalytic) function in neural cells is UNVERIFIED"),
    foundation=("Edge HDAC5 -T(+)-> SLC2A1 (CollecTRI/TRRUST/ExTRI2): ONE reference, PMID 22991226 (abstract re-read): knockdown of HDAC5 in human primary muscle cells increased glucose uptake and GLUT4 "
        "and REDUCED GLUT1 (SLC2A1) expression (measurement, expression level, skeletal muscle). The same abstract's pan-HDAC inhibitor (Scriptaid) result names GLUT4 and metabolic flux, not GLUT1: "
        "what a pan-HDAC inhibitor does to SLC2A1 is not stated there (unknown). Seeds: SLC2A1 up 2.67x in KO organoid (4 v 2 libraries) and 1.65x in hNSC WWOX-deleted (one library per arm), descriptive. "
        "Adjacent neural data for this exact compound (abstract level): SB-939 raised BDNF expression and neurite outgrowth in human neural-progenitor-derived neurons (PMID 30841499), and halted EAE in mice through "
        "neuronal IDO1 (PMID 38759372): so the compound acts in neural cells and CNS tissue in some systems, with effects that do not run through SLC2A1"),
    decisive_assumption=("that pracinostat lowers SLC2A1 in WWOX-deficient neural cells THROUGH HDAC5 (not through the class I enzymes HDAC1-3, HDAC6 or HDAC10, all within about 1-2x of HDAC5 in one source), "
        "that the muscle edge holds in neural cells, and that lowering SLC2A1 is the beneficial direction (the role of the observed change is unknown, no source)"),
    counter_evidence=("(1) attribution cannot be established: pan-HDAC profile; where a single document carries the panel, HDAC5 is 102x weaker than HDAC1 (5113 v 50 nM) and above all of the class I and IIb values; "
        "the 47 nM source has no assay context. Genetic HDAC5 knockdown is the only way to isolate the edge. (2) one non-neural reference for the edge (muscle); thin, not refuted (premise_unresolved edge:HDAC5>SLC2A1 transfers "
        "from the nanatinostat record, scope: the edge only). (3) unknown, not negative: no datum was found on what a pan-HDAC inhibitor does to SLC2A1 in neural cells. (4) descriptive and NOT counted as a reason: "
        "HDAC5 transcript lower where SLC2A1 is higher (organoid 0.81x v 2.67x; hNSC 48.99 -> 10.47 TPM v 276 -> 455; neurons SLC2A1 133 -> 41.5). (5) " + SECOND + ". "
        "(6) class-wide HDAC inhibition in progenitors changes many programmes at once (BDNF induction, PMID 30841499), so an SLC2A1 change could not be assigned to the chain"),
    next_test=("Step 0 of the hand-over first (HIF-1/2alpha protein by compartment, then genetic HIF knockdown with lactate and a network/viability endpoint). Compound step, one experiment that also serves every HDAC-cluster member: "
        "WWOX-deficient hNPC/organoid and its corrected counterpart, HDAC5 knockdown v a class IIa-selective inhibitor v pracinostat v a class I-selective inhibitor, SLC2A1/HK2 transcript and glucose uptake; "
        "engagement read as histone H3/H4 acetylation (class I) separately from an HDAC5 substrate readout"),
    result_that_would_change_the_decision=("HDAC5 knockdown lowering SLC2A1 in WWOX-deficient neural cells AND pracinostat doing so with the HDAC5 readout moving at the same concentrations while a class I-selective inhibitor does not: "
        "keeps it KEPT_CONDITIONAL. A class I-selective inhibitor lowering SLC2A1 equally, or HDAC5 knockdown inert: the question becomes a class-wide HDAC one (new record, not this one) and this arm is rejected as written"),
    wwox_context_expression=("organoid cpm (KO 350-423 v WT 468): HDAC5 present and slightly lower in KO; HDAC1 41-55, HDAC2 90-134, HDAC3 67-87, HDAC6 137-245, HDAC10 14-17, SLC2A1 55-62 WT v 135-210 KO. "
        "hNPC TPM (hNSC / hNSC-WWOX-del / neurons / neurons-WWOX-del): HDAC5 49.0/10.5/41.9/12.2; HDAC10 ABSENT. Targets exist; the question is attribution, not presence"),
    feasibility_note_exposure=("CNS exposure: no datum retrieved (UNKNOWN). Paediatric experience exists: a 2026 systematic review of HDAC inhibitors in children (PMID 42415186, abstract) lists pracinostat among six agents, "
        "most studied in CNS tumours, toxicity mainly haematological (thrombocytopenia); no efficacy or brain-concentration datum was read. Feasibility note only"),
    classification="insufficiently evaluated; known thread re-emitted (not a new relation)",
    earlier_appearance=("IT9 P3 exploration excluded.tsv (not_taken:promiscuous(>=5 targets)) and candidates_consolidated (Q2 opposes, HDAC5 cluster); IT10 dispositions_Q2 rank 4 CONDITIONAL_IF_HARMFUL, role unknown; "
        "no qualification record before this one"),
    disposition="INCONCLUSIVE",
    reasons=("The decisive link is the attribution of an SLC2A1 effect to HDAC5, and the data cannot decide it: pracinostat is pan-HDAC, its HDAC5 IC50 is 47 nM in one source and 5113 nM in another (109-fold apart), "
        "and the only edge reference is a muscle knockdown. This is a different position from nanatinostat, whose 67-fold class I selectivity rested on one coherent panel; it is not rejected because HDAC5 engagement is documented "
        "(Ki 21 nM) and nothing contradicts the edge in neural cells, it is not kept because no discriminating readout of the compound alone exists. Missing datum, named: the pracinostat HDAC5 IC50 from a single assay that also "
        "measures HDAC1 and HDAC3, and HDAC5-knockdown SLC2A1 in a neural system"),
    status_before="CONDITIONAL_H_HARM", status_after="CONDITIONAL_H_HARM",
    unverified=("which HDAC5 IC50 (47 nM or 5113 nM) reflects engagement in cells; the body of PMID 22991226 (abstract only here) and whether its pan-HDAC inhibitor changed GLUT1; brain exposure; "
        "whether pracinostat changes SLC2A1 in neural cells in either direction; the other 18 cluster members (not examined)"),
    why_not_proposed_before=("The IT9 generator excluded it at its promiscuity filter (>=5 targets, pan-HDAC), so the HDAC5 chain was never evaluated for this molecule; IT10 carried it as CONDITIONAL_IF_HARMFUL (rank 4) but "
        "no qualification package took it (IT21 P4a qualified only six of the thirteen handed rows and took nanatinostat as the HDAC representative). The missing input was a same-type comparison of HDAC5 with the other HDACs: "
        "IT22 P2 supplied the GtoPdb IC50 set (47 v 40-49 nM) and this record added the ChEMBL document that contradicts it (5113 nM)"),
    novelty_class="known thread re-emitted",
))

# ---------------------------------------------------------------- 0043 desidustat
R.append(dict(
    proposal_id="IT21P2-0043", cand_id="IT22P4B1-02", compound="desidustat (ZYAN1)",
    question_arm="Q2 H_PROTECT (mimic: sustain or amplify the HIF-type adaptation)",
    mechanism_cluster_and_seed_origin=("EGLN2 -P(-)-> FOXO3 -T(+)-> BNIP3; seeds S021 BNIP3 up and S017 SLC2A1 up; ONE origin (hNPC GSE126075 + organoid GSE156243, shared IT7 derivation); "
        "cluster of 5 alternative records (compound 6Ee of PMID 22364528, molidustat, roxadustat, vadadustat, a second vadadustat record) shares the chain; roxadustat was DROPPED in IT9 (E-02) for properties of that molecule and for an edge this chain does not contain"),
    identity_form_state=("ChEMBL CHEMBL4650314 DESIDUSTAT (synonyms Zyan-1, ZYAN1), free acid (glycinamide N-oxy-quinolone, SMILES O=C(O)CNC(=O)c1c(O)c2ccccc2n(OCC2CC2)c1=O), MW 332.31, "
        "InChIKey IKRKQQLJYBAPQT-UHFFFAOYSA-N, ChEMBL max phase 3 as served 2026-11-03 (a 2025 Exp Neurol paper, read, states a first approval in 2022 for CKD anaemia and an ongoing Indian phase IV study); oral; "
        "DGIdb/GtoPdb claim joined through the ligand id; VERIFIED (ChEMBL REST); attribution state in the hand-over NOT_ASSESSABLE (no GtoPdb affinity)"),
    target_action_potency_selectivity=("NAME TRAP: EGLN2 = PHD1, EGLN1 = PHD2, EGLN3 = PHD3. IC50 (cell-free, one ChEMBL document, PMID 40263713, J Med Chem 2025): EGLN1/PHD2 1300 nM; FIH 21700 nM; "
        "gamma-butyrobetaine dioxygenase (BBOX) 420 nM (3.1x MORE potent than PHD2 inside that same document and measure type; assay conditions not read); AspH 9900; JMJD5 48300; KDM4A > 100000 nM. "
        "EGLN2 (PHD1) and EGLN3 (PHD3) were NOT measured in ChEMBL or in the local GtoPdb release (class_alternatives_it22 EGLN2 returns no ligand with a value): the engine's main target has no potency; "
        "unknown, not negative. The class action (HIF prolyl-hydroxylase inhibition) is a label statement in the 2025 paper, not an isoform measurement. No curated ChEMBL mechanism row"),
    assay_nature=("cell-free recombinant enzymes for the six values; the 1300 nM PHD2 value is a single measurement of unrecorded 2-oxoglutarate conditions; no cellular PHD1 engagement datum. "
        "In mice and in human iMG cells (1 microM, PMID 39914641) the compound has biological effects but no HIF, FOXO3 or BNIP3 readout was taken (those strings do not occur in the article text)"),
    foundation=("Edge 1 EGLN2 -P(-)-> FOXO3 (SIGNOR, one reference, PMID 24990963, an earlier ledger reading FTR-20261030-24990963-01 plus abstract and targeted passages re-read here): EglN2 hydroxylates FOXO3a on two prolyl residues, "
        "blocks USP9x binding, promotes proteasomal degradation; 'various pharmacological prolyl hydroxylase inhibitors' (the legend names 200 microM CoCl2, 1 mM DMOG, 200 microM DFO, no desidustat) raised FOXO3a in EglN2-proficient "
        "T47D breast cancer cells and did not further raise it in EglN2-depleted cells (measurement, protein level, breast cancer cell lines, HIF-independent per the paper). "
        "Edge 2 FOXO3 -T(+)-> BNIP3 (about 33 CollecTRI/CollecTRI2 references, one read): PMID 20181828 abstract (full text only matched for the quotes): in cardiomyocytes/U2OS, p8 knockdown increased FoxO3 association with the bnip3 promoter "
        "and bnip3 RNA and protein; a de-repression experiment, not FOXO3 gain of function. Seeds: BNIP3 up 1.38x in KO organoid, hNSC-WWOX-del 23.6 -> 39.8 TPM. "
        "Neural context for the compound (PMID 39914641, text read): in adenine-CKD mice after embolic stroke desidustat 15 mg/kg orally improved long-term neurological scores and lowered p-NFkB/ADAM17 in brain sections; "
        "not a WWOX system, adult male mice"),
    decisive_assumption=("that desidustat engages EGLN2/PHD1 in WWOX-deficient neural cells enough to stabilise FOXO3a, that this FOXO3 route (rather than the compound's direct action on all PHDs and on HIF) is what changes BNIP3, "
        "and that sustaining the BNIP3/HIF-type adaptation is protective (role of the observed change unknown, no source)"),
    counter_evidence=("(1) no EGLN2 potency exists and the compound is a pan-PHD inhibitor by class: any change cannot be assigned to EGLN2, and the FOXO3 edge itself was shown with non-selective agents (CoCl2, DMOG, DFO) "
        "and EglN2 knockdown in breast cancer cells only. (2) the seed readouts cannot discriminate routes: BNIP3 and SLC2A1 are, from general knowledge not verified in this package, also HIF-responsive, so a rise after a PHD "
        "inhibitor would be expected by the direct route alone. (3) role unknown: BNIP3 up could be a harmful (mitophagy/cell death) or a protective programme; the second seed SLC2A1 is carried as H_HARM in the same question "
        "(pracinostat row), so one question holds both signs for the same readout. (4) " + SECOND + ". (5) sibling decisions: roxadustat's DROP (E-02) rests on its EU-label properties and on a FOXO3 -> SLC2A1 repression "
        "reference; the first is a property of that molecule and the second of an edge this chain does not use: neither transfers (decision_scope_it22). Whether desidustat shares a seizure or thyroid liability is "
        "UNKNOWN, no datum retrieved. (6) BBOX (carnitine biosynthesis) is inhibited more potently than PHD2 in the one document that measures both (420 v 1300 nM), an off-target axis nobody has examined in neural cells"),
    next_test=("Step 0 first (role of HIF-type adaptation in WWOX-deficient neural cells). Compound step, only if step 0 supports a protective role: WWOX-deficient hNPC/organoid and corrected control, desidustat v EGLN2/PHD1 knockdown "
        "v EGLN1 knockdown v HIF1A/EPAS1 knockdown; FOXO3 protein (stability, with USP9x), BNIP3, SLC2A1 transcript and protein, mitochondrial content and viability; engagement read as hydroxylated HIF1alpha-Pro564 "
        "and a PHD1-selective readout. One experiment also serves the other PHD inhibitors of the cluster"),
    result_that_would_change_the_decision=("FOXO3 stabilisation that follows EGLN2 knockdown and desidustat but not EGLN1 knockdown, with BNIP3 rising and HIF1A/EPAS1 knockdown not blocking it: the FOXO3 route is real here and the arm stays conditional "
        "with a named mechanism. BNIP3/SLC2A1 rising only through HIF with FOXO3 unchanged: the proposal collapses into the generic PHD-inhibitor (HIF) question, already carried, and the EGLN2 -> FOXO3 chain is closed for this compound"),
    wwox_context_expression=("organoid cpm KO v WT: EGLN2 88-97 v 103-104 (0.89x), EGLN1 26-30 v 30-33, EGLN3 20-24 v 11-13 (1.82x), FOXO3 85-102 v 69-84 (1.19x), BNIP3 56-76 v 47-49 (1.38x), HIF1A 34-44 v 43-50, EPAS1 3-9 v 1.2-1.7; "
        "hNPC TPM EGLN2 108/115/48/21 (hNSC/hNSC-del/neurons/neurons-del), FOXO3 12.1/6.1/3.7/2.5, BNIP3 23.6/39.8/16.7/8.6, EGLN3 and EPAS1 ABSENT. EGLN2 is the dominant PHD transcript in both systems: the target exists"),
    feasibility_note_exposure=("CNS exposure: no brain-concentration datum (UNKNOWN); mouse blood PK only (15 mg/kg oral: Cmax 23.7 ug/mL, T1/2 2.1 h, PMID 39914641 text). Brain effects in stroke mice imply some CNS action but not exposure. "
        "No paediatric datum retrieved. Feasibility note only"),
    classification="insufficiently evaluated; known thread re-emitted",
    earlier_appearance=("IT9 P3 candidates_consolidated (Q2 mimics, EGLN2 cluster, not_seed_specific(top-list_only)); IT9 v3 README names 'HIF prolyl hydroxylase inhibitors (daprodustat, roxadustat, desidustat) via EGLN2 -P-> FOXO3 -T-> ...'; "
        "IT10 dispositions_Q2 rank 8 CONDITIONAL_IF_PROTECTIVE; no qualification record before this one"),
    disposition="INCONCLUSIVE",
    reasons=("Two decisive data are missing and the readout cannot separate them: EGLN2/PHD1 potency of this compound was never measured, and the only chain edge for EGLN2 was shown with non-selective PHD inhibitors, "
        "while the seed genes respond to the compound's direct HIF action. No link is contradicted in neural cells, so it is not rejected; nothing identifies the FOXO3 route, so it is not kept. "
        "Missing datum, named: desidustat IC50 at EGLN2 (PHD1) in a panel that also measures EGLN1 and EGLN3, and FOXO3 stability after PHD1 knockdown in a neural cell"),
    status_before="CONDITIONAL_H_PROTECT", status_after="CONDITIONAL_H_PROTECT",
    unverified=("the PHD1 potency; the assay conditions of the 1300 nM PHD2 value; HIF-responsiveness of BNIP3/SLC2A1 in neural cells (background knowledge only); the body of PMID 20181828 beyond the abstract and of the 32 other FOXO3 -> BNIP3 references; "
        "brain exposure; any desidustat seizure liability; the 2022 approval statement (taken from the 2025 paper, not checked against a label)"),
    why_not_proposed_before=("In IT9 the EGLN2 route reached the seeds only as a top-list entry (not_seed_specific); in IT10 it was held CONDITIONAL_IF_PROTECTIVE because the role of the HIF-type adaptation is unknown (step 0 never run), "
        "and the attribution screen had no affinity for desidustat (no GtoPdb value at any EGLN isoform). IT21 P4a did not take it. The missing input is an isoform-level PHD1 measurement, which no source in the local releases holds"),
    novelty_class="known thread re-emitted",
))

# ---------------------------------------------------------------- 0052 AT-13148
R.append(dict(
    proposal_id="IT21P2-0052", cand_id="IT22P4B1-03", compound="AT-13148 (AT13148)",
    question_arm="Q4 H_HARM (restore inhibitory tone / lower excitatory gain; seed NPY down)",
    mechanism_cluster_and_seed_origin=("MAPKAPK2 -P(-)-> CDC25A -P(+)-> FOXO1 -T(+)-> NPY; seed S116 NPY down (PMID 34268881 deposited tab, human organoid); ONE origin; cluster of 4 alternatives "
        "(gamcemetinib, MK2A inhibitor, compound 8 of PMID 17480064, a diazepino-thieno-quinolinone) shares the chain; gamcemetinib has its own record (INCONCLUSIVE, premise_unresolved edge:MAPKAPK2>CDC25A)"),
    identity_form_state=("ChEMBL CHEMBL3544960 AT-13148 (AT13148), free base, MW 313.79, InChIKey IIRWNGPLJQXWFJ-KRWDZBQOSA-N, SMILES NC[C@@](O)(c1ccc(Cl)cc1)c1ccc(-c2cn[nH]c2)cc1, ChEMBL max phase 1 (clinical candidate), oral; "
        "VERIFIED (ChEMBL REST); no GtoPdb ligand/affinity (attribution NOT_ASSESSABLE in the hand-over); the first-in-human paper recommended NOT developing it further"),
    target_action_potency_selectivity=("ChEMBL curated mechanism rows: ROCK inhibitor and MAP kinase-activated protein kinase 2 inhibitor, whose reference list is a company pipeline page, PMID 22781553 and PMID 25840982: neither abstract names MK2, "
        "and the full text of the first-in-human paper (PMID 32616501, read) contains no MK2/MAPKAP string. TYPED values: IC50 (biochemical, several documents) ROCK2 < 10 nM (4 nM and ROCK1 6 nM in the paper's text), PKA < 10, "
        "p70S6K 12 (< 10), AKT1 38, AKT3 50, SGK3 50, RSK1 85, AKT2 402 nM; cellular AKT-pathway IC50 (GSK3beta Ser9 in U87MG) 1100 nM. Kd (a different type, kinobead competition in cell lysate, PMID 29191878): "
        "PKN2 9, PRKACB 14, PRKACA 15, PKN1 25, ROCK2 26, ROCK1 27, LATS1 27, PRKCD 44, ADRBK1 170 nM and MAPKAPK2 > 30000 nM (MAPKAPK5 also > 30000). "
        "The ONLY MAPKAPK2 value is that Kd lower bound; there is no MK2 IC50 row, so no same-type ratio is possible and none is claimed; the measured profile is dual ROCK/AKT with PKA and p70S6K"),
    assay_nature=("IC50 rows: recombinant kinase assays (type B) from a patent and from a review compilation; Kd rows: native-kinase competition with immobilised broad-spectrum inhibitors (Science 2017). The same Kd table gives > 30000 nM for AKT1, AKT2 and AKT3, "
        "which the IC50 rows put at 38-402 nM: the kinobead readout misses a target the compound does inhibit, so its MAPKAPK2 > 30000 nM is a non-detection and is NOT evidence of inactivity. Clinical PK (PMID 32616501, text): at the maximum tolerated 180 mg three times a week Cmax about 383-400 nM, AUC about 13,000 nM.h"),
    foundation=("Edge 1 MAPKAPK2 -P(-)-> CDC25A (SIGNOR + SPIKE, references PMID 17292828 and PMID 15629715; abstracts re-read): MK2 phosphorylates Cdc25B/C and, in p53-deficient cells after cisplatin, MK2 depletion abrogates the Cdc25A-mediated S-phase "
        "checkpoint (DNA damage context, cancer lines); the first reference names Cdc25B/C, not Cdc25A. Edge 2 CDC25A -P(+)-> FOXO1 (SIGNOR, PMID 21670150, abstract; the full-text route returned an empty body): Cdc25A enhances Foxo1 stability by dephosphorylating Cdk2 in breast "
        "cancer cells. Edge 3 FOXO1 -T(+)-> NPY (PMID 16783365, abstract): hypothalamic Foxo1 stimulates NPY and AgRP transcription through the PI3K/Akt pathway, mouse hypothalamus. "
        "Seed: NPY 0.05-0.12 cpm in KO v 3.2-7.7 in WT organoid (4 v 2 libraries; near-zero counts); in Wwox-KO mouse hippocampus NPY-expressing interneuron NUMBERS are reduced (PMID 30290271, abstract), i.e. the seed may be cell loss. "
        "Sign logic of the chain: MK2 inhibition relieves CDC25A, FOXO1 rises, NPY rises. Every edge sits in a different cell system and none in a postmitotic NPY neuron"),
    decisive_assumption=("that AT-13148 inhibits MAPKAPK2 in WWOX-deficient neural cells (as opposed to AKT/ROCK/PKA/p70S6K), and that the MK2-CDC25A-FOXO1 route operates in the NPY-producing cell and raises NPY (carried premise from gamcemetinib: not shown)"),
    counter_evidence=("(1) the claimed main target has no positive measurement: the only MAPKAPK2 datum is a kinobead Kd > 30000 nM that is uninformative (AKT, a true target, also reads > 30000 nM there); the compound's measured potencies are ROCK 4-27 nM, PKA/PKN 9-15 nM, AKT 38-402 nM, p70S6K about 10 nM; "
        "its dose-limiting toxicities in humans (hypotension, headache) are attributed by the authors to ROCK inhibition. (2) the curated MK2 mechanism row rests on references that do not name MK2. "
        "(3) the chain is already 'up' downstream while NPY is not: CDC25A 1.50x and FOXO1 2.31x higher in KO organoid, NPY 0.01x (descriptive, 4 v 2 libraries; says nothing about MK2 activity). "
        "(4) NPY_SIGN_CONTESTED carried from the cluster: the NPY direction is contested by the mouse bulk and pooled-nuclei contrasts and by neuron loss in the KO organoid (cell-population sensitive); the mouse paper reports fewer NPY neurons. "
        "(5) MAPKAPK2 is ABSENT from the hNPC table and NPY is ABSENT there too; the hNPC library is also not an independent system for other reasons (gate 1 failed for WWOX in that arm). "
        "(6) the IT21 rerun table classed this Q4 row as GAINED_BY_RERUN_NULL_OR_SIGN_CHANGE_NOT_A_FINDING. (7) clinical: narrow therapeutic index, variable PK, no consistent target biomarker change at 180 mg; "
        "'free drug levels were below those measured in preclinical efficacy experiments' (verbatim locators L8-L11)"),
    next_test=("A cell-free test comes first and is cheap: it needs a positive MK2 IC50 for this molecule (a cell-free MAPKAPK2 assay beside AKT1 and ROCK2 in one panel). The chain question itself is carried by the gamcemetinib record: "
        "Mapkapk2, Cdc25a, Foxo1 and Npy by cell class in the mouse snRNA data (GSE158684, free, not run here), then MK2 knockdown v a selective MK2 inhibitor in a system with NPY-producing neurons"),
    result_that_would_change_the_decision=("A cell-free MAPKAPK2 IC50 within about 10-fold of its AKT1 or ROCK2 IC50 in the same panel, plus MK2-dependent NPY change in an NPY-neuron system, keeps it conditional with a measured target. "
        "A MAPKAPK2 IC50 above about 10 microM in that panel closes the MK2 arm for this molecule (REJECTED_INFORMATIVE in a new record). Nothing about AKT or ROCK lowering NPY is tested here"),
    wwox_context_expression=("organoid cpm KO v WT: MAPKAPK2 136-147 v 149-157 (0.92x), MAPKAPK3 46-57 v 43-51, CDC25A 13.5-19.4 v 10.3-11.7 (1.50x), FOXO1 3.1-5.4 v 1.4-2.5 (2.31x), NPY 0.05-0.12 v 3.2-7.7, AKT1 299-314 v 354-375, "
        "AKT2 87-93 v 94, ROCK1 10-16 v 16-17, ROCK2 10-20 v 22-23; hNPC TPM: MAPKAPK2, NPY ABSENT; CDC25A 22.6/40.0/5.9/3.3; FOXO1 14.8/23.6/0.5/0.8; AKT2 80/97/55/18. The target is expressed in the organoid; NPY is near zero"),
    feasibility_note_exposure=("CNS exposure: no brain datum (UNKNOWN). Human phase 1 (PMID 32616501): 51 patients, MTD 180 mg three days a week, DLTs hypotension (300 mg), pneumonitis and transaminases (240 mg), rash (180 mg), "
        "no responses; the authors recommend not developing the compound. Hypotension and headache are on-target ROCK effects: a liability for any child with seizures. Feasibility note only"),
    classification="experimental probe, clinical-stage multi-AGC kinase inhibitor; insufficiently evaluated for the MK2 arm",
    earlier_appearance=("IT9 v3 / IT10 v4 seed-specific lists: AT-13148 appears in Q5 (opposes, ranks 193/186) and Q6 through ROCK2 -P(+)-> EP300 -T(+)-> TNF/IL6/MYC, never in Q4; IT21 gained_vs_it10: the Q4 MK2 chain "
        "is classed GAINED_BY_RERUN_NULL_OR_SIGN_CHANGE_NOT_A_FINDING; sibling gamcemetinib INCONCLUSIVE (ranking_it8_p9_20261029/it9_records.tsv#P4CD-05); no qualification record for this molecule before this one"),
    disposition="INCONCLUSIVE",
    reasons=("The decisive premise, that AT-13148 inhibits MAPKAPK2, has no positive measurement anywhere in the retrieved sources: the curated MK2 mechanism row rests on references that do not name MK2, the one MK2 value is an uninformative kinobead non-detection "
        "(the same assay also reads > 30000 nM for AKT, a documented target), and the compound's measured activity is dual ROCK/AKT at 4-50 nM, which is what its human toxicity reflects. Because the Kd cannot count as negative evidence, "
        "this is not a rejection: the datum is missing, and it is named (a cell-free MAPKAPK2 IC50 beside AKT1 and ROCK2 in one panel). Until then the arm cannot be tested with this molecule, and the chain downstream of MK2 "
        "still lacks its premise in postmitotic NPY neurons (carried from gamcemetinib). Nothing here says whether AKT or ROCK inhibition (a different chain: the cited hypothalamic abstract makes Foxo1 a PI3K/Akt-controlled NPY driver) changes NPY in WWOX-deficient neurons: unexamined, not negative"),
    status_before="CONDITIONAL_H_HARM", status_after="CONDITIONAL_H_HARM",
    unverified=("why the kinobead readout misses AKT (assay coverage not read); a cell-free MK2 IC50 for AT-13148 (none exists in ChEMBL); the body of PMIDs 17292828, 15629715, 21670150, 16783365 (abstracts only); whether CDC25A and FOXO1 act on NPY in NPY neurons; "
        "brain exposure; the AKT/ROCK -> FOXO1 -> NPY route (adjacent, unexamined, a possible NEW relation if it were ever proposed)"),
    why_not_proposed_before=("In IT9/IT10 the molecule was generated only through ROCK2 (ROCK2 -> EP300 -> TNF/IL6/MYC); the Q4 MK2 chain first appeared in the IT21 rerun, whose own table marks it as a rerun gain 'not a finding'. "
        "Nobody had checked whether the compound binds MK2: the MK2 target came from a curated ChEMBL mechanism row with no activity row behind it. The one earlier MK2 record (gamcemetinib) was about a selective MK2 inhibitor and stopped at the NPY-neuron premise"),
    novelty_class="known thread re-emitted (molecule seen in IT9/IT10 via ROCK2); the Q4 MK2 relation for this molecule is new to LEGEND and is rejected",
))

# ---------------------------------------------------------------- 0380 rineterkib
R.append(dict(
    proposal_id="IT21P2-0380", cand_id="IT22P4B1-04", compound="rineterkib (LTT462)",
    question_arm="Q5 H_PROTECT (mimic: support glia-neuron trophic function or the reactive programme; seeds TNF, IL6 up, mouse)",
    mechanism_cluster_and_seed_origin=("MAPK1 -P(+)-> BCL3 -T(-)-> TNF; seeds S085 TNF up and S086 IL6 up (mouse expression, tier B; PMID 30290271 section 3.3, and PMID 36828035); TWO origins (two mouse papers); "
        "cluster of 8 alternative ERK1/2 compounds (Astx029, compound 27 of PMID 29775310, edaxeterkib, ERK inhibitor III, laduviglusib, SCH772984 +2) shares the chain; tizaterkib from the same cluster is INCONCLUSIVE (IT21P2-0374) and the "
        "edge-level limit transfers, its potency does not"),
    identity_form_state=("ChEMBL CHEMBL3909517 RINETERKIB (LTT462), free base, ChEMBL max phase 1, InChIKey YFCIFWOJYYFDQP-PTWZRHHISA-N, oral; GtoPdb ligand 11200 joined through the ligand id; "
        "described as an ERK1/2 inhibitor in a phase 1b abstract (PMID 39383771); no curated ChEMBL mechanism row; VERIFIED (ChEMBL REST + local GtoPdb release)"),
    target_action_potency_selectivity=("TYPED: IC50 at ERK2 (MAPK1) 0.0261 nM (ChEMBL: one row, one document, a 2016 US patent 'Aminoheteroaryl benzamides as kinase inhibitors', activated ERK2 with 20 pM enzyme; the GtoPdb row 0.026 nM "
        "is, on every visible attribute, the same measurement and counts ONCE). It is the ONLY measured target: no selectivity ratio can be built (class_alternatives_it22: 'no other target with a IC50 value: not comparable'), "
        "unknown, not negative. The tizaterkib ERK2 IC50 values (0.3-0.66 nM, P4a) are the same type but from different assays; with a 20 pM enzyme concentration a 26 pM IC50 sits at the assay floor, so no 'more potent' claim is made"),
    assay_nature=("single cell-free biochemical assay of activated ERK2 (type B); no cellular pERK or pathway datum was retrieved for this molecule except an on-treatment DUSP6 mRNA fall of 45.5% in patient samples "
        "when given with the pan-RAF inhibitor naporafenib (PMID 39383771, abstract): an ERK-pathway readout in tumour, confounded by the partner drug"),
    foundation=("Edge 1 MAPK1 -P(+)-> BCL3 (SIGNOR, PMID 28689659, abstract plus targeted passages of the open text read): Akt, Erk2 and IKK1/2 phosphorylate Bcl3; phosphorylation by Erk2/IKK at Ser114 and Ser446 'convert Bcl3 into a transcriptional coregulator "
        "by facilitating its recruitment to DNA', unphosphorylated Bcl3 'acts as classical IkB-like inhibitor, removes p50 and p52 from bound DNA'; p52/Bcl3-driven luciferase was reduced by Erk inhibitor II and in Erk2-knockdown HeLa cells "
        "(measurement, reporter, HeLa/HEK293T; LPS-induced Bcl3 in RAW 264.7 macrophages is described but no TNF readout is in that paper). Edge 2 BCL3 -T(-)-> TNF (CollecTRI family, the network record itself carries stimulation AND inhibition, i.e. mixed sign): "
        "PMID 15465827 (abstract): BCL-3 and p50 negatively regulate LPS-induced TNFalpha in macrophages, with HDAC1 recruitment; PMID 22798670 (abstract): Bcl-3 induction by cyclophilin B reduces TNFalpha, knockdown restores it. "
        "Seeds: TNF and IL6 overexpressed in Wwox-KO mouse hippocampus (PMID 30290271, abstract) and elevated neuroinflammation in the P47T mouse (PMID 36828035, abstract)"),
    decisive_assumption=("that ERK inhibition by rineterkib lowers Bcl3 activity in Wwox-deficient glia so TNF/IL6 repression is relieved (TNF/IL6 up, the arm's intended 'mimic'), and that this beats the direct requirement of ERK for TNF production"),
    counter_evidence=("(1) the sign is unresolved in both directions: either way phospho-Bcl3 is lost, the result in the Mol Cell paper is Bcl3 reduced as coregulator or Bcl3 acting as an IkB-like p50/p52 remover; both predict TNF up, but the direct ERK -> TNF route "
        "(Tpl2/ERK required for LPS-induced TNF, carried from the tizaterkib record at title level) predicts TNF down in the same cell type: the competing route is the carried limit and is unresolved (premise_unresolved edge:BCL3>TNF). "
        "(2) no Bcl3 -> TNF measurement exists in glia or neurons; both edge sources are macrophage lines/primary macrophages (abstracts), the ERK edge is HeLa/HEK293T. (3) in the human neural systems the readouts are unreadable: "
        "BCL3 4-7 cpm (organoid) and ABSENT in hNPC, TNF 0.00-0.03 cpm and IL6 0 (organoid) and ABSENT in hNPC; the seeds are mouse. (4) single measured target, no selectivity data (not comparable, unknown). "
        "(5) ERK is broadly required in neurons and glia; a potent ERK inhibitor at 26 pM enzyme potency may also lower the trophic programme the arm wants to support (no datum retrieved either way). "
        "(6) no CNS datum; the clinical use found is oncology, with lipase elevation the commonest grade 3 event with naporafenib (PMID 39383771, abstract). (7) the two seed origins are both Wwox-null or Wwox-mutant mouse brain, so they are two papers but not two independent systems for this chain"),
    next_test=("Wwox-null v wild-type mouse microglia/astrocyte cultures or slices, rineterkib 1-30 nM with ravoxertinib or SCH772984 and Erk1/2 knockdown as controls (one experiment serves the whole ERK cluster, including tizaterkib): "
        "p-ERK, Bcl3 phosphorylation (Ser114), Bcl3 and p50 occupancy at the Tnf promoter, TNF and IL6 transcript and protein over 6-24 h, with and without LPS; viability and a network readout"),
    result_that_would_change_the_decision=("TNF/IL6 rising with reduced Bcl3 phosphorylation and Bcl3 knockdown phenocopying: supports the chain and keeps it conditional with the role question still open. TNF/IL6 falling with ERK inhibition: "
        "contradicts the arm as posed (re-pose as a lowering probe in a new record). Cytotoxicity at the effective dose: closes it as a probe for this axis"),
    wwox_context_expression=("organoid cpm KO v WT: MAPK1 114-135 v 104-107 (1.20x), MAPK3 121-148 v 143-168, BCL3 5.2-7.2 v 4.3-6.2 (1.17x), TNF 0-0.03 v 0, IL6 0 v 0; "
        "hNPC TPM MAPK1 19.0/29.2/12.2/6.1 (hNSC/hNSC-del/neurons/neurons-del), MAPK3 94.5/87.5/66.0/26.8; BCL3, TNF, IL6 ABSENT. Mouse Mapk1/Bcl3/Tnf values in the Wwox mouse deposits were not extracted here (not checked)"),
    feasibility_note_exposure=("CNS exposure: no datum (UNKNOWN). Human phase 1b with naporafenib in KRAS/BRAF-mutant NSCLC (216 patients across arms): rineterkib 100-300 mg QD, recommended 200 mg QD, DLTs in 16% of 62, antitumour activity limited (PMID 39383771, abstract); "
        "a 2026 paper reports dermatologic toxicities of pan-RAS/RAF inhibitors (title only). Feasibility note only"),
    classification="experimental probe, clinical-stage; insufficiently evaluated; known thread re-emitted",
    earlier_appearance=("IT9 v3 / IT10 v4 seed-specific lists: Q5 mimics, ranks 278 and 252, same chain; not in an IT9 candidate or exclusion table; IT21 P4a took tizaterkib as the ERK cluster representative (the P4a README names 0296 as sharing "
        "the cluster); no qualification record for this molecule before this one"),
    disposition="INCONCLUSIVE",
    reasons=("The chain predicts TNF/IL6 up through relief of Bcl3, while the direct ERK requirement for TNF predicts the opposite in the same cell type, and nothing measured in a Wwox system decides between them; "
        "the molecule adds one number (ERK2 IC50 0.026 nM) and no selectivity. This is the tizaterkib limit transferred only at the level of the edge BCL3 -> TNF (decision_scope_it22 premise_unresolved), "
        "with the molecule assessed on its own data. Missing datum, named: TNF and IL6 after ERK inhibition in Wwox-null glia, with Bcl3 phosphorylation read"),
    status_before="CONDITIONAL_H_PROTECT", status_after="CONDITIONAL_H_PROTECT",
    unverified=("the body of PMIDs 15465827 and 22798670 (abstracts only) and the direct ERK -> TNF route (carried at title level, not re-read here); selectivity of the molecule; cellular potency; brain exposure; "
        "mouse Bcl3/Mapk1 expression in the Wwox deposits; whether the patent value was run with tight-binding correction"),
    why_not_proposed_before=("It sat at rank 278 (IT9) and 252 (IT10) of the seed-specific list and never entered a candidate or exclusion table. The generator could not rank the arm's two opposing routes, and the unresolved Bcl3-derepression "
        "v direct ERK -> TNF competition was named only on 2026-11-03 in the tizaterkib record; IT21 P4a chose one ERK compound for the cluster and left the others unqualified. No selectivity datum exists for this molecule in any local release"),
    novelty_class="known thread re-emitted",
))
