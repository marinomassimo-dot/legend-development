#!/usr/bin/env python3
"""IT21 P3b: writes the proposal, qualification, phenotype-first, Path D and negatives tables from the records below.

The records are authored text with pointers; nothing here is computed from a model. The Path B tables (pathb_levers_it21.tsv, pathb_compounds_it21.tsv)
come from pathb_it21.py and are checked against these records by test_p3b_it21.py.

  python3 build_p3b_it21.py        writes proposals_it21_p3b.tsv, qualification_it21_p3b.tsv, phenotype_first_it21_p3b.tsv, path_d_it21_p3b.tsv, negatives_it21_p3b.tsv
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv
from pathlib import Path

HERE = Path(__file__).resolve().parent

MECHANISMS = ("stability_residual_function", "compensation", "metabolism", "redox_nrf2", "cellular_stress", "glia_myelination", "development")
ORIGIN_PATHS = ("B_compound_to_WWOX", "PF_phenotype_first", "D_perturbation_context", "B_bidirectional_check")
# DISFAVOURED_BY_SIGN_PRECEDENT (P8-fix): an analogy from another model disfavours a route; it is not a measurement and closes nothing. It promotes nothing either.
DISPOSITIONS = ("KEPT_CONDITIONAL", "QUALIFIED_HYPOTHESIS", "REJECTED_INFORMATIVE", "INCONCLUSIVE", "DISFAVOURED_BY_SIGN_PRECEDENT")
NOVELTY = ("new_molecule_for_LEGEND", "new_relation_in_WWOX_context", "new_member_of_known_class", "probe", "development_candidate", "insufficiently_evaluated")
ARM_STATUS = ("CONDITIONAL_H_HARM", "CONDITIONAL_H_PROTECT", "DIAGNOSTIC_ONLY", "NOT_APPLICABLE")
GOALS = ("deep_recovery", "partial_benefit", "none")
TRACKS = ("A", "B", "A_and_B", "none")

PROPOSAL_COLS = ["id", "origin_path", "mechanism", "wwox_level_observed", "generating_premise_and_pointer", "decisive_assumption", "lever_gene", "intervention",
                 "documented_action_and_level", "goal_depth", "dependence_on_variant_track", "arm_if_process_harmful", "arm_if_process_protective",
                 "novelty_perimeter_searched_2026_11_03", "selected_for_qualification", "disposition"]

P = []


def prop(**k):
    assert set(k) == set(PROPOSAL_COLS), set(PROPOSAL_COLS) ^ set(k)
    P.append(k)


prop(id="G01", origin_path="B_compound_to_WWOX", mechanism="stability_residual_function", wwox_level_observed="abundance (protein not detected with transcript comparable, Q230P-class; faster turnover, P252A over-expressed)",
     generating_premise_and_pointer="need NEED-WWOX-MISSENSE-PROTEIN-RESCUE (HSPA8 is a pathway_member, role HSC70 co-immunoprecipitated with P252A); discovery_ledger DL-MECH-047 and DL-MECH-048; the catalogue row of FORIGERIMOD carries a curated HSPA8 inhibitor action that the compound-to-need route files as not_evaluable",
     decisive_assumption="the clearance of the destabilised SDR missense protein runs through an HSC70-associated lysosomal step in neural cells, and protein spared from it regains function (ERLIQ degron and GSK3B docking may be one conformational event)",
     lever_gene="HSPA8", intervention="HSC70 blockade by forigerimod (peptide), with chloroquine as the known lysosomal comparator and HSPA8 or LAMP2 knockdown as the genetic control",
     documented_action_and_level="ChEMBL curated mechanism, INHIBITOR of HSPA8, single protein; potency not carried; selectivity: one documented target (the P140 literature also names MHC class II binding)",
     goal_depth="deep_recovery", dependence_on_variant_track="B (needs an allele that makes protein; null and canonical splice alleles have none)",
     arm_if_process_harmful="CONDITIONAL_H_HARM: clearance of the mutant protein is the bottleneck -> blocking HSC70 raises abundance (function still to be shown)",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: HSC70 assists folding or removes a toxic species -> blocking it lowers functional protein or raises aggregate (the card-A05 harm hypothesis, mirrored)",
     novelty_perimeter_searched_2026_11_03="forigerimod: 0 record directories, 0 registry records; HSPA8: named in needs, cards A04/A05 packets and 6 package directories as a pathway member, never as an inhibited lever; chloroquine: 7 package directories (known)",
     selected_for_qualification="yes (Q01)", disposition="KEPT_CONDITIONAL")
prop(id="G02", origin_path="PF_phenotype_first", mechanism="metabolism", wwox_level_observed="function (behavioural seizure stage, preweaning Wwox-null mice, provoked); lithium effect present in all three genotypes",
     generating_premise_and_pointer="phenotype_first.tsv U24 (lithium, PMID of the Cheng 2020 mouse paper, complete read, manifest entries 1, 4, 18, 23, 28, 29 of deepdive_manifests/PMID32000863.json); the catalogue lists IMPA1 beside GSK3A/GSK3B for lithium and card G01 argues GSK3 only",
     decisive_assumption="inhibition of inositol monophosphatase 1 (inositol depletion) contributes to lithium's protection in the provoked-seizure assay",
     lever_gene="IMPA1", intervention="lithium decomposed by myo-inositol add-back and by a structurally unrelated GSK3 inhibitor, in the same assay",
     documented_action_and_level="ChEMBL curated mechanism: INHIBITOR of IMPA1 (single protein) and of GSK3A/GSK3B (protein family); same three references for both; potency not carried",
     goal_depth="partial_benefit", dependence_on_variant_track="A (acts whatever the allele, if at all)",
     arm_if_process_harmful="CONDITIONAL_H_HARM: the provoked seizure is the harmful process -> an IMPA1 contribution to protection would be a lever",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: in the cholinergic precedent inositol depletion is proconvulsant -> IMPA1 inhibition would worsen seizure (a safety signal on the same need)",
     novelty_perimeter_searched_2026_11_03="IMPA1: 0 record directories (3 bulk generator tables only); inositol: 1 passing mention in the M01 card as a risk flag; lithium as a molecule: 36 directories (known), via GSK3",
     selected_for_qualification="yes (Q02)", disposition="DISFAVOURED_BY_SIGN_PRECEDENT")
prop(id="G03", origin_path="B_compound_to_WWOX", mechanism="glia_myelination", wwox_level_observed="function (EM myelinated-axon counts, CC1+/PDGFRa+ counts: OPC up, mature oligodendrocytes down) and marker (PV/GABAergic deficit)",
     generating_premise_and_pointer="needs NEED-MYELINATION and NEED-INHIBITORY-HYPOFUNCTION; glia_maturation_it14_p4 evidence rows E02, E04, E09, E15; the catalogue holds 13 families with a signed THRA/THRB agonist action and none has a LEGEND record",
     decisive_assumption="the oligodendrocyte-lineage maturation block (and the PV deficit) in WWOX-deficient tissue is thyroid-hormone-receptor responsive and is a cause of harm rather than a consequence of seizures or illness",
     lever_gene="THRA,THRB", intervention="thyroid-hormone-receptor agonist probe: tiratricol or liothyronine, with a THRB-selective agonist and T3 deprivation as controls",
     documented_action_and_level="ChEMBL curated mechanism: AGONIST of THRA/THRB (scope: protein complex in ChEMBL; single-protein agonist per isoform in the Guide to Pharmacology rows); no isoform selectivity for tiratricol or liothyronine",
     goal_depth="partial_benefit", dependence_on_variant_track="A (allele-blind)",
     arm_if_process_harmful="CONDITIONAL_H_HARM: the OPC accumulation / maturation block is harmful -> a pro-differentiation push could help",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: the delay is secondary or compensatory, or myelin is activity-dependent and the signal is absent -> a push is neutral or advances maturation out of step",
     novelty_perimeter_searched_2026_11_03="tiratricol, liothyronine: 0 record directories, 0 registry records ('thyroid' hits are thyroid carcinoma); clemastine/benztropine (CHRM1) are the myelin compounds LEGEND examined, and PAPER 475 is a negative developmental-myelination result for clemastine",
     selected_for_qualification="yes (Q03)", disposition="KEPT_CONDITIONAL")
prop(id="G04", origin_path="B_compound_to_WWOX", mechanism="redox_nrf2", wwox_level_observed="function (ROS reporter, opposite signs in two non-neural systems); transcript (NRF2 organoid panel); ferroptosis (two non-neural abstracts, unread)",
     generating_premise_and_pointer="need NEED-REDOX-OXIDATIVE-STRESS (targets: SOD1 only); registry CORPUS-STUB-028 and CORPUS-STUB-066 (WWOX-ferroptosis titles, status not_processed); card L01 covers NFE2L2/KEAP1 only; ALOX15 is reached from the ferroptosis side",
     decisive_assumption="WWOX-deficient neural cells are more susceptible to ferroptosis (lipid peroxidation) than isogenic controls, and ALOX15 contributes",
     lever_gene="ALOX15", intervention="ALOX15 inhibitor tool compounds (ML351, PD-146176) against a radical-trapping ferroptosis inhibitor and iron chelation",
     documented_action_and_level="DGIdb rows from the Guide to Pharmacology: inhibitor, single protein ALOX15; no status, no potency carried; isoform selectivity (ALOX12, ALOX5) not assessed here",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     arm_if_process_harmful="CONDITIONAL_H_HARM: ferroptotic susceptibility in WWOX loss is harmful -> inhibiting ALOX15 protects",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: WWOX is pro-ferroptotic in the HCC abstract (loss protective) -> the same inhibitor adds nothing or removes a signalling lipid",
     novelty_perimeter_searched_2026_11_03="ALOX15: 2 directories, both incidental off-target panel rows; ML351, PD-146176: bulk tables only; ferrostatin: 1 early directory and 3 registry records on ferroptosis and epilepsy",
     selected_for_qualification="yes (Q04)", disposition="INCONCLUSIVE")
prop(id="G05", origin_path="B_compound_to_WWOX", mechanism="cellular_stress", wwox_level_observed="none measured (the ISR and ER-stress needs are uncertain-direction, transcript-level)",
     generating_premise_and_pointer="needs NEED-ISR-ATTENUATION (ERN1 and XBP1 are named, SIGMAR1 is not); SIGMAR1 reached by 16 signed families, 8 agonists and 8 antagonists, none with a LEGEND record",
     decisive_assumption="an ER-chaperone / ER-mitochondria coupling deficit exists in WWOX-deficient neurons (no datum)",
     lever_gene="SIGMAR1", intervention="sigma-1 receptor agonist probe (blarcamesine; PRE-084 as a tool) against an antagonist (opposite effect)",
     documented_action_and_level="DGIdb / Guide to Pharmacology: agonist, single protein SIGMAR1 for blarcamesine; the ChEMBL record of blarcamesine has 0 target rows (twin records are not merged on name)",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     arm_if_process_harmful="CONDITIONAL_H_HARM: ISR / ER-stress over-activation is harmful and sigma-1 agonism dampens it (sign not documented)",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: the ISR response is protective -> an agonist that dampens it harms",
     novelty_perimeter_searched_2026_11_03="SIGMAR1 / sigma-1: 3 directories each, all scouting records or off-target panel rows; pridopidine: 0 (not in the catalogue as a signed row: unknown, not negative)",
     selected_for_qualification="yes, short (Q05)", disposition="INCONCLUSIVE")
prop(id="G06", origin_path="B_compound_to_WWOX", mechanism="cellular_stress", wwox_level_observed="function (ATM-linked DNA-damage competence, ATR checkpoint support; non-neural, murine B-cell and cell-line evidence)",
     generating_premise_and_pointer="working model CLAIM 029 and PAPER 030, PAPER 080; Path B reached ATM, ATR, CHEK1, WEE1 and PARP1 through 80 signed inhibitor family-gene pairs, none named in a need",
     decisive_assumption="DNA-damage-response competence is reduced in WWOX-deficient proliferative developmental compartments",
     lever_gene="ATR,CHEK1,WEE1,PARP1,ATM", intervention="DNA-damage-response inhibitors (ATR, CHK1, WEE1, PARP, ATM)",
     documented_action_and_level="ChEMBL and DGIdb rows: inhibitors, single protein; all 'down'; no agonist in the table",
     goal_depth="none", dependence_on_variant_track="none",
     arm_if_process_harmful="CONDITIONAL_H_HARM: no scenario in the record makes DDR over-activity the harmful process",
     arm_if_process_protective="CONDITIONAL_H_PROTECT: if DDR competence is protective and already reduced, an inhibitor is an aggravator (harm flag, not a lever)",
     novelty_perimeter_searched_2026_11_03="held as a harm flag; no card or need aims at DDR",
     selected_for_qualification="no (rejected on direction)", disposition="REJECTED_INFORMATIVE")
prop(id="G07", origin_path="B_bidirectional_check", mechanism="glia_myelination", wwox_level_observed="function (OPC accumulation with fewer mature oligodendrocytes)",
     generating_premise_and_pointer="Path B found GPR17 (an OPC differentiation brake) reached by 11 signed families, all agonists, 0 inhibitors; absent from needs, cards and registries",
     decisive_assumption="an antagonist exists and the brake is engaged in WWOX-deficient OPCs",
     lever_gene="GPR17", intervention="none available in the guarded table",
     documented_action_and_level="11 DGIdb-only agonist families (ATP and lead compounds); no signed antagonist (pranlukast is in the catalogue without a signed GPR17 row: unknown, not negative)",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     arm_if_process_harmful="DIAGNOSTIC_ONLY", arm_if_process_protective="DIAGNOSTIC_ONLY",
     novelty_perimeter_searched_2026_11_03="GPR17: 1 directory (partial_benefit_it6_p10)", selected_for_qualification="no (lever without a compound)", disposition="INCONCLUSIVE")
prop(id="G08", origin_path="B_bidirectional_check", mechanism="stability_residual_function", wwox_level_observed="abundance and localisation (ITCH K63 polyubiquitination, nuclear accumulation; HSC70 and LAMP2 named by the lysosomal-route record)",
     generating_premise_and_pointer="DL-MECH-047, DL-MECH-048, PAPER 079; handles_it21.tsv rows H_STAB",
     decisive_assumption="a compound with a documented action on the E3 ligase or the CMA receptor exists in the catalogue",
     lever_gene="ITCH,LAMP2,UBE2N,VCP", intervention="none available in the guarded table",
     documented_action_and_level="0 signed families on ITCH, LAMP2, UBE2N and VCP (pathb_levers_it21.tsv)",
     goal_depth="deep_recovery", dependence_on_variant_track="B",
     arm_if_process_harmful="DIAGNOSTIC_ONLY", arm_if_process_protective="DIAGNOSTIC_ONLY",
     novelty_perimeter_searched_2026_11_03="ITCH/ACK1 chain: ack1_it11_p24 and ack1_it13 packages (known)", selected_for_qualification="no (lever without a compound)", disposition="INCONCLUSIVE")
prop(id="G09", origin_path="B_bidirectional_check", mechanism="metabolism", wwox_level_observed="none at flux level (Warburg-like transcript state; human metabolism measured as normal in DL-BIO-009)",
     generating_premise_and_pointer="SDR domain as an NAD(P)-dependent fold is an architecture fact, not a WWOX function measurement; Path B: NAMPT reached only by 2 inhibitors (wrong direction), NMNAT2 by none; nicotinamide riboside has a catalogue record with 0 target rows",
     decisive_assumption="a cofactor-supply limit exists in WWOX-deficient cells (no datum)",
     lever_gene="NAMPT,NMNAT2", intervention="NAD precursor supplement (nicotinamide riboside)",
     documented_action_and_level="no documented target action for the supplement in the catalogue (0 target rows): unknown, not negative",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     arm_if_process_harmful="DIAGNOSTIC_ONLY", arm_if_process_protective="DIAGNOSTIC_ONLY",
     novelty_perimeter_searched_2026_11_03="NAD+: 2 registry records, both about the ketogenic state; nicotinamide: 0", selected_for_qualification="no (no WWOX-level premise)", disposition="INCONCLUSIVE")
prop(id="G10", origin_path="B_compound_to_WWOX", mechanism="glia_myelination", wwox_level_observed="as G03",
     generating_premise_and_pointer="Path B: S1PR1 reached by 39 and S1PR5 by 18 signed families (siponimod among them); alternative arm of G03",
     decisive_assumption="as G03, plus an OPC-side S1P receptor is engaged",
     lever_gene="S1PR1,S1PR5", intervention="S1P receptor modulator (siponimod) as the receptor-level alternative to G03",
     documented_action_and_level="ChEMBL and DGIdb rows: agonist (functional antagonism of S1PR1 on lymphocytes is a separate effect not encoded in the sign)",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     arm_if_process_harmful="CONDITIONAL_H_HARM: as G03", arm_if_process_protective="CONDITIONAL_H_PROTECT: as G03, plus immune effects in an infant brain",
     novelty_perimeter_searched_2026_11_03="siponimod: bulk table only; S1PR: 0 directories; fingolimod: card J01 (glial reactivity)",
     selected_for_qualification="no (arm of G03; IT14 P4 RESTRICT holds)", disposition="INCONCLUSIVE")

QUAL_COLS = ["id", "proposal", "compound_identity_and_form", "documented_action_level_selectivity", "assay_conditions_that_decide", "wwox_context_compatibility",
             "alternatives_and_opposite_effects", "counter_evidence", "feasibility", "f1_foundation", "f2_decisive_assumption", "f3_counter_evidence",
             "f4_next_test", "f5_result_that_changes_the_decision", "goal_depth", "dependence_on_variant_track", "novelty_class", "disposition", "owed_or_unread"]
Q = []


def qual(**k):
    assert set(k) == set(QUAL_COLS), set(QUAL_COLS) ^ set(k)
    Q.append(k)


qual(id="Q01", proposal="G01",
     compound_identity_and_form="forigerimod (ChEMBL parent CHEMBL3989409; the acetate salt record CHEMBL3989801 carries the mechanism row); a spliceosomal-derived phosphopeptide, modality protein_or_peptide, ChEMBL max_phase 3 for some indication; a DGIdb-only twin record (CAT:DGIDB:2acb3ffe1e90, 1 target row) is a separate catalogue family and is not merged on name",
     documented_action_level_selectivity="curated INHIBITOR of HSPA8 (CHEMBL1275223), single protein, references PubMed 19390596 and 21173017; the second abstract says the peptide impaired HSC70 refolding properties, decreased HSC70 and stable MHC class II dimers in B cells and increased p62 and LC3-II, read there as down-regulated lysosomal degradation in autophagic flux; the abstract does not name chaperone-mediated autophagy; the peptide also binds MHC class II; potency not carried",
     assay_conditions_that_decide="documented in murine lupus (MRL/lpr) lymphocytes only; biodistribution in that paper accumulated in lungs and spleen; no neural cell, no dose, no WWOX system. For the WWOX side the decisive condition is a missense WWOX protein at endogenous level in a neural cell, with a cycloheximide chase and a function read-out",
     wwox_context_compatibility="P252A over-expressed in non-neural thyroid-carcinoma lines: lower protein, faster turnover, restored by chloroquine and ammonium chloride, not by MG-132 or 3-MA, HSC70 co-immunoprecipitates (need record, abstract-level for the route name); Q230P-class: one blot, protein not detected, transcript comparable; no read-across between missense alleles (transfer firewall). Compatible as a question; no datum for the Q230P class or for neurons",
     alternatives_and_opposite_effects="chloroquine and ammonium chloride (known, lysosomal, non-selective); LAMP2 / HSPA8 genetics; opposite effect: HSP70 induction (card A05) is proposed for the same need with a stated harm hypothesis; HSC70 blockade could lower folding and also touches other needs (antigen processing, autophagy) in cells that depend on it",
     counter_evidence="MG-132 did not act on wild type or mutants (it does not favour a proteasome route, which is not the claim here); DL-MECH-065: the ERLIQ degron and GSK3B function may be one conformational event, so protection from clearance could return inert protein; the ACK1 packages found no WWOX turnover assay on a variant; the chain rests on one over-expression paper of Tier C",
     feasibility="peptide, parenteral, brain exposure not shown (lungs and spleen in the one distribution study); cell delivery of a peptide is an assay problem; no paediatric or CNS data. As a development candidate: not supported. As a cell-level probe of the route: feasible",
     f1_foundation="a destabilised SDR missense protein is cleared by an HSC70-linked lysosomal step in over-expressing cells, and a documented HSC70 inhibitor with a lysosomal-flux effect is in the catalogue",
     f2_decisive_assumption="the same step clears the Q230P-class protein in neural cells, and protein spared from it is functional (GSK3B docking, L404 intact)",
     f3_counter_evidence="stable-but-inert risk (DL-MECH-065); HSC70 is also a folding chaperone; one over-expression paper; MG-132 negative result shows the route is not proteasomal but says nothing about which lysosomal branch",
     f4_next_test="in a neural cell expressing the missense WWOX at endogenous level: abundance by chase under forigerimod, HSPA8 knockdown, LAMP2 knockdown and chloroquine against vehicle, then GSK3B-docking function (pTau S396/S404, L404A control)",
     f5_result_that_changes_the_decision="knockdown of HSPA8 or LAMP2 does not raise protein -> route closed for that allele (REJECTED_INFORMATIVE); protein rises without docking function -> stable-but-inert, deep recovery closed on this route; both rise -> the route earns a variant-specific preclinical question (still not a qualified candidate)",
     goal_depth="deep_recovery", dependence_on_variant_track="B (protein-making alleles only)",
     novelty_class="new_member_of_known_class (lysosomal-route probes; chloroquine already examined) with probe use; the inhibitor-direction reading of HSPA8 is new to the need file",
     disposition="KEPT_CONDITIONAL",
     owed_or_unread="PMID 41124647 (P252A) read at the abstract and repository-census level only, not a complete read; abstracts of the two P140 papers are not reads; no label, safety or CNS-exposure lookup")
qual(id="Q02", proposal="G02",
     compound_identity_and_form="lithium carbonate (CAT:CHEMBL1200826, approved) and lithium citrate (CAT:CHEMBL1201170): salts of one active ion, counted once; DGIdb-only twin family CAT:DGIDB:50ccc7b5c33e carries the same two targets from the Guide to Pharmacology and a ChEMBL copy (one origin)",
     documented_action_level_selectivity="ChEMBL curated mechanism rows: INHIBITOR of IMPA1 (single protein) and INHIBITOR of GSK3A/GSK3B (protein family); both with the same label reference and a review (PubMed 22707923); potency not carried here; lithium acts at both within a narrow therapeutic range (not quantified here)",
     assay_conditions_that_decide="Cheng 2020 Figure 7d, preweaning littermates, LiCl intraperitoneal 60 mg/kg three times within 1 h before PTZ, Racine stage each minute for 60 min; null PTZ N=6 vs PTZ+LiCl N=7, wild type N=12 vs 8; significance bracket in all three genotypes (manifest entries 1, 18, 23, 28, 29; blind locator audit SUPPORTED 2026-10-21); the null control in 7d (late stage about 0.3 to 1.7) differs from the null control in 7b (about 1.6 to 2.8)",
     wwox_context_compatibility="the lithium suppression is not Wwox-specific (it is as significant in +/+); the GSK3 attribution rests on lithium alone and the paper's own Discussion lists other actions (entry 4); card G01 and the IT15 Q-B package keep GSK3 compounds as tools. The precedent for the IMPA1 action has the opposite sign: lithium plus low-dose pilocarpine produces limbic seizures reversed stereospecifically by myo-inositol (PubMed 17602744, 8110911) and inositol-deficient food augments it (25679134)",
     alternatives_and_opposite_effects="selective GSK3 inhibitors (IT15 Q-B maps classes); myo-inositol add-back; the homeostatic-plasticity action of lithium (PAPER 565, SNAP25 mouse, precedent); opposite effect: an IMPA1 contribution would be proconvulsant in the cholinergic model",
     counter_evidence="the sign precedent above; lithium is protective in controls, so it does not discriminate WWOX biology; PTZ (GABA-A) and pilocarpine (muscarinic) are different provocations, so the precedent does not close the question for PTZ",
     feasibility="lithium is approved, narrow-index; the question is mechanistic (attribution), not a regimen. Inositol add-back timing is 1 to 8 h before the provocation in the precedent (abstract of 8110911)",
     f1_foundation="a signed in vivo result (lithium suppresses provoked seizure in Wwox-null preweaning mice) and a documented second action of the same molecule",
     f2_decisive_assumption="IMPA1 inhibition contributes to that protection",
     f3_counter_evidence="the one documented behavioural consequence of IMPA1 inhibition in rodents is proconvulsant; protection in wild type; N of 6 to 8 per arm",
     f4_next_test="same assay and genotypes: LiCl alone, LiCl after myo-inositol, a structurally unrelated GSK3 inhibitor, vehicle; time-resolved Racine stage; blinded scoring",
     f5_result_that_changes_the_decision="myo-inositol leaves the lithium effect unchanged -> IMPA1 route closed for this phenotype; inositol reverses it -> the protection is inositol-dependent, the GSK3 attribution of card G01 falls and IMPA1 becomes a lever with a sign opposite to the precedent (needs explanation); a GSK3 inhibitor reproduces the effect -> GSK3 attribution supported, still not WWOX-specific",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     novelty_class="new_relation_in_WWOX_context (the IMPA1 side of a molecule LEGEND already holds via GSK3)",
     disposition="DISFAVOURED_BY_SIGN_PRECEDENT",
     owed_or_unread="the IMPA1 record rests on a ChEMBL curation row and a review abstract; the pilocarpine papers are abstracts only; the sign precedent is an analogy from the lithium-pilocarpine model, not a measurement in the Wwox assay, so it disfavours IMPA1 as a mediator and a lever and does not exclude it (nothing about lithium itself is closed); Cheng 2020 also ran a pilocarpine model in Wwox mice, so the objection that the provocations differ is testable in the same system; reopen condition: inositol reverses the lithium effect in the Wwox-null assay")
qual(id="Q03", proposal="G03",
     compound_identity_and_form="tiratricol (CAT:CHEMBL41632, clinical_candidate, max_phase 3, ATC D11AX08 / H03AA04) and its DGIdb twin (CAT:DGIDB:a7fad23af16a); liothyronine (CAT:CHEMBL1544 in family CAT:CHEMBL1201119, approved) and levothyroxine; THRB-selective set in the table: resmetirom, sobetirome, KB-141, eprotirome",
     documented_action_level_selectivity="ChEMBL curated: AGONIST of THRA and THRB (protein complex scope); Guide to Pharmacology rows: single-protein agonist on each isoform; tiratricol and liothyronine are not isoform-selective; the DGIdb twin of tiratricol also lists HIF1A and NFE2L2 and CYP2C9 from a different source with the action unstated (not signed, flagged)",
     assay_conditions_that_decide="precedent only, other disease: Triac in Mct8/Oatp1c1 double-knockout mice (PubMed 36834863 abstract), daily over the first three postnatal weeks normalised myelination, cortical GABAergic interneuron differentiation, electrophysiology and locomotion (the abstract attributes the normalisation to 400 ng/g; 50 ng/g was the lower arm), and only when started within those weeks (weeks 3 to 6 failed). For WWOX the deciding assay is the seizure-free neuron-OPC co-culture (IT14 row E09) or the pre-onset lineage census, not a drug trial",
     wwox_context_compatibility="IT14 P4: myelin deficit follows neuron-restricted deletion, is restored by neuronal add-back, OPC up and CC1 down (a maturation-block pattern), reproduced by one laboratory; the PV/GABAergic deficit is a second WWOX need (INHIBITORY-HYPOFUNCTION). The thyroid-hormone precedent addresses both, by a different cause (hormone uptake). A WWOX thyroid-hormone defect is not documented",
     alternatives_and_opposite_effects="S1P receptor modulators (G10), CHRM1 antagonists (clemastine: PAPER 475 shows impaired developmental myelination in wild-type mice; benztropine), GPR17 (no antagonist); opposite effects on other needs: systemic hypermetabolism against the glycaemia need, heart rate, and a possible shift in excitability (not looked up); unstated HIF1A and NFE2L2 interactions on the tiratricol twin touch cards K01 and L01",
     counter_evidence="IT14 P4 decision RESTRICT: the driver sits upstream of the oligodendrocyte and a seizure- or illness-mediated route is not excluded, so an OPC-side push may find no signal; the add-back window is P0-P5; the precedent window closes within three weeks; no myelin compound has ever been given to a WWOX-deficient system",
     feasibility="liothyronine is approved and tiratricol is a clinical-stage compound for a paediatric hypomyelinating disease (the programme is not verified here); both need endocrine monitoring; no dose is proposed. As a role-resolving probe in cells: feasible with an existing assay",
     f1_foundation="a documented hypomyelination and OPC-maturation pattern in WWOX-deficient neurons-OPC systems and a thyromimetic that rescues myelin and interneuron maturation in another disease with a developmental window",
     f2_decisive_assumption="the WWOX maturation block is thyroid-hormone-receptor responsive and causal for harm",
     f3_counter_evidence="IT14 RESTRICT reasons 1 to 4; clemastine negative developmental result; the precedent disease is a hormone-entry defect, WWOX is not shown to be one",
     f4_next_test="neuron (WT or null) + OPC co-culture (IT14 E09) with T3 or Triac against vehicle, T3-deprived medium and a THRB-selective agonist: OPC differentiation ratio within MBP+ cells and PV count; no seizures in the dish",
     f5_result_that_changes_the_decision="no change of the null shift under any arm -> closed (REJECTED_INFORMATIVE); correction by T3 but also by the control in wild type -> non-specific maturation; correction only in the null condition -> the OPC-side block is receptor-responsive and a pre-onset in vivo arm becomes a defined question; still no benefit claim",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     novelty_class="new_molecule_for_LEGEND (and a new relation in this WWOX context)",
     disposition="KEPT_CONDITIONAL",
     owed_or_unread="isoform expression in OPCs, the Triac clinical programme, the thyroid-hormone effect on seizure threshold: background knowledge, not read; PubMed 36834863 and the review 33669242 are abstracts; IT14 E09 and the preprint E23 are one laboratory")
qual(id="Q04", proposal="G04",
     compound_identity_and_form="ML351 (CAT:DGIDB:8df312c1e8b3) and PD-146176 (CAT:DGIDB:1c0e3d4cc075), tool compounds, no status statement, DGIdb-only families, modality unknown; PD-146176 also lists KAT2A and VDR with the action unstated",
     documented_action_level_selectivity="inhibitor of ALOX15, single protein, from the Guide to Pharmacology; no potency or isoform data carried; ALOX12 / ALOX15B selectivity not assessed here",
     assay_conditions_that_decide="none in a WWOX system. The two WWOX-ferroptosis abstracts disagree in sign: in HCC cells the effect of toosendanin 'was dependent on WWOX' and WWOX activation drives ferroptosis (PubMed 39894307); in lung epithelium WWOX overexpression mitigated erastin- and LPS-induced ferroptosis with p53 deacetylation and SLC7A11 up (PubMed 41443103). Both use ferrostatin-1",
     wwox_context_compatibility="the redox need has no neural WWOX measurement; fly mitochondrial H2O2 is higher after neuronal knockdown while mouse photoreceptors give the opposite; the NRF2 organoid transcripts (NFE2L2 0.75x, NQO1 0.73x, HMOX1 1.67x) are expression, not abundance or activity. Compatible only as a conditional question",
     alternatives_and_opposite_effects="ferrostatin-1 or liproxstatin-type radical trapping and iron chelation (not signed target actions), the NRF2 route of card L01 (a lever on the same process from the other side); the need record refutes NAC/CoQ10 as an assumed monotonic fix",
     counter_evidence="opposite WWOX-ferroptosis signs in two non-neural systems; no neural datum; ALOX15 is one of several lipid peroxidation routes; tool compounds with no exposure data",
     feasibility="tool compounds only; no human exposure; a cell experiment is feasible",
     f1_foundation="two abstracts tie WWOX to ferroptosis regulators (p53, SLC7A11, NRF2, SAT1) in non-neural cells and the redox need is open",
     f2_decisive_assumption="WWOX-deficient neural cells are more ferroptosis-sensitive than isogenic controls and ALOX15 contributes",
     f3_counter_evidence="the two abstracts point in opposite directions; transcript-level NRF2 panel is mixed (NFE2L2 and NQO1 down, HMOX1 up)",
     f4_next_test="isogenic WWOX-deficient neural cells: lipid peroxidation (C11-BODIPY) and cell death under RSL3 or erastin with and without ferrostatin-1; only if sensitised, ALOX15 inhibitors against ferrostatin-1",
     f5_result_that_changes_the_decision="no sensitisation -> closed; sensitisation not rescued by ALOX15 inhibitors but by ferrostatin-1 -> ALOX15 is not the route; rescued by ALOX15 inhibitors -> a defined redox question",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     novelty_class="insufficiently_evaluated (tool compounds; LEGEND holds the two ferroptosis titles unprocessed)",
     disposition="INCONCLUSIVE",
     owed_or_unread="CORPUS-STUB-028 and CORPUS-STUB-066 were not read (abstract only); a complete read of either would not supply a neural datum")
qual(id="Q05", proposal="G05",
     compound_identity_and_form="blarcamesine (CAT:CHEMBL4297224, clinical_candidate, max_phase 3, 0 target rows) and the DGIdb twin CAT:DGIDB:ad143870abaf (SIGMAR1 agonist from the Guide to Pharmacology; CHRM1 and ERBB2 listed with the action unstated)",
     documented_action_level_selectivity="agonist of SIGMAR1, single protein, one source; the muscarinic row is unstated and touches the CHRM1 target of the myelination need without a sign",
     assay_conditions_that_decide="none in a WWOX system",
     wwox_context_compatibility="no WWOX datum on sigma-1, ER-mitochondria contacts or ER calcium; the ISR need has an unresolved direction",
     alternatives_and_opposite_effects="dextromethorphan (SIGMAR1 agonist with GRIN2A block, already in the NMDAR thread), antagonists such as BD-1047 (opposite effect), pridopidine (not signed in the catalogue)",
     counter_evidence="the lever was reached from the compound side and no WWOX observation supports it",
     feasibility="clinical-stage compounds exist; any paediatric use is not looked up here",
     f1_foundation="a gene that 16 signed families reach and no LEGEND file names",
     f2_decisive_assumption="an ER-stress or ER-mitochondria coupling deficit exists in WWOX-deficient neurons",
     f3_counter_evidence="no premise at all; a lever found is not a premise found",
     f4_next_test="measure ER-stress / ISR markers and mitochondria-ER contact in WWOX-deficient neurons before any compound (the ISR measurement gap already on record)",
     f5_result_that_changes_the_decision="an ISR or ER-stress signal of known sign in a WWOX-deficient neural cell would open the sigma-1 question; none -> stays unqualified",
     goal_depth="partial_benefit", dependence_on_variant_track="A",
     novelty_class="insufficiently_evaluated", disposition="INCONCLUSIVE",
     owed_or_unread="no source read for the WWOX side because none exists in the module")

PF_COLS = ["unit_id", "intervention", "signed_result_in_WWOX_system", "pmids_depth", "thread", "what_this_package_did", "outcome"]
PF = [
    dict(unit_id="U24", intervention="Lithium", signed_result_in_WWOX_system="behavioural seizure stage after one provoking injection, preweaning null mice: decrease; also decrease in wild type", pmids_depth="Cheng 2020 mouse paper, complete read, manifest entries audited",
         thread="outside excitability for this question (the second action IMPA1; GSK3 is card G01)", what_this_package_did="decomposed the molecule's documented actions (G02/Q02); fixed a prediction with a sign from the inositol precedent", outcome="IMPA1 route disfavoured by a sign precedent (DISFAVOURED_BY_SIGN_PRECEDENT: an analogy, not a measurement); GSK3 attribution unresolved"),
    dict(unit_id="U17", intervention="Ethosuximide", signed_result_in_WWOX_system="PTZ-provoked seizure score, late phase of the hour: decrease in null only (n.s. in +/+ and +/-)", pmids_depth="Cheng 2020, same paper",
         thread="excitability (T-type, card H01 and need T-TYPE-CALCIUM)", what_this_package_did="not regenerated: carried by existing card and need; recorded here because the genotype-specificity is the one signed result that does not appear in the lithium arm", outcome="carried, no new proposal"),
    dict(unit_id="U20", intervention="Vigabatrin", signed_result_in_WWOX_system="clinical cessation of spasms: mixed (queried, not full read)", pmids_depth="queried_not_full_read",
         thread="excitability / GABA (card H02, need SEIZURE-CONTROL-SYMPTOMATIC)", what_this_package_did="not regenerated; its opposite effect on the myelination need (card H02 exposure question) is the reason the myelin proposals G03/G10 keep seizure-secondary readings separate", outcome="carried, no new proposal"),
    dict(unit_id="U15", intervention="Ketogenic diet", signed_result_in_WWOX_system="seizure control: 1 benefit, 1 no change", pmids_depth="complete read", thread="metabolism (card E04)", what_this_package_did="not regenerated; out of the small-molecule graph", outcome="carried, no new proposal"),
    dict(unit_id="U21", intervention="d-APV", signed_result_in_WWOX_system="burst frequency: decrease (tool compound)", pmids_depth="complete read", thread="excitability (F01/F04)", what_this_package_did="not regenerated (outside the brief)", outcome="carried"),
    dict(unit_id="U10", intervention="A51", signed_result_in_WWOX_system="layer-neuron fraction: no change", pmids_depth="complete read", thread="development (card D01)", what_this_package_did="no catalogue identity; nothing to search", outcome="carried"),
    dict(unit_id="U07", intervention="AAV9-WWOX", signed_result_in_WWOX_system="spike-wave discharge: decrease", pmids_depth="complete read", thread="gene addition", what_this_package_did="outside method modality", outcome="carried"),
]

D_COLS = ["context", "what_exists", "compound_side", "wwox_side", "usable_for_path_D", "reason"]
D = [
    dict(context="PTZ time course in Wwox littermates (Cheng 2020 Fig 7b, 7d)", what_exists="dose, timing, genotype and PTZ-alone control recorded; N 6 to 20 per arm", compound_side="lithium and ethosuximide only", wwox_side="behavioural, whole animal",
         usable_for_path_D="yes, for the two compounds already tested; used in Q02", reason="a perturbation with controls exists for these two molecules and no other"),
    dict(context="LINCS compound signatures in neural-lineage cells (NPC, NEU)", what_exists="compound signatures with cell, dose, time", compound_side="none of lithium, tiratricol, liothyronine, forigerimod, blarcamesine has a strict neural signature (record_usability.tsv.gz of IT7 P2: Msig_neural_strict = 0)", wwox_side="no WWOX-deficient disease signature of known direction; the shRNA WWOX knockdown signature in NPC cannot be verified (WWOX is not a landmark gene, IT21 P6)",
         usable_for_path_D="no", reason="no pair of (disease signature, compound signature) in the same cell type exists; the earlier signature-reversal query was inconclusive then negative (IT7 P2). Not forced"),
    dict(context="organoid transcript panels (NRF2, Wnt, glycolysis)", what_exists="knockout versus wild type transcripts, six libraries, confounded with maturity", compound_side="none", wwox_side="expression only, no compound arm",
         usable_for_path_D="no", reason="no perturbation with a compound; expression is not abundance, activity or function"),
]

N_COLS = ["id", "what_was_not_found_or_closed", "kind", "unknown_is_not_negative_note"]
N = [
    dict(id="N1", what_was_not_found_or_closed="IMPA1 as a mediator of the lithium benefit (G02)", kind="DISFAVOURED_BY_SIGN_PRECEDENT (an analogy from the lithium-pilocarpine model, not a measurement in the Wwox assay)", unknown_is_not_negative_note="PTZ and pilocarpine are different provocations, but Cheng 2020 also ran a pilocarpine model in Wwox mice, so the difference is testable in the same system; the Wwox-null add-back experiment has not been run"),
    dict(id="N2", what_was_not_found_or_closed="DNA-damage-response inhibitors as levers (G06)", kind="REJECTED_INFORMATIVE (harm flag)", unknown_is_not_negative_note="post-mitotic neuronal DDR competence in WWOX loss is unmeasured; the flag is about the direction the record supports"),
    dict(id="N3", what_was_not_found_or_closed="a signed compound on ITCH, LAMP2, UBE2N, VCP, ATF6, HSF1, GCLC, ACSL4, NQO1, IMPA2, INPP1, BPNT1, NMNAT2, BDH1, EBP", kind="lever with no compound in the guarded table", unknown_is_not_negative_note="absence from a guarded table is a catalogue statement; a dropped group-level or republished record is not an absent compound"),
    dict(id="N4", what_was_not_found_or_closed="an antagonist of GPR17 (G07)", kind="lever without a compound", unknown_is_not_negative_note="eleven agonist families only"),
    dict(id="N5", what_was_not_found_or_closed="a WWOX-level premise for NAD supply and for sigma-1 (G05, G09)", kind="no premise", unknown_is_not_negative_note="a missing measurement"),
    dict(id="N6", what_was_not_found_or_closed="a variant-independent deep-recovery compound path", kind="not generated", unknown_is_not_negative_note="the only variant-independent deep-recovery route in the module is gene addition; no compound path reaches it from the documented-action table"),
    dict(id="N7", what_was_not_found_or_closed="any QUALIFIED_HYPOTHESIS", kind="by construction", unknown_is_not_negative_note="every surviving row depends on a role or a premise that no WWOX-deficient neural measurement resolves; the pipeline's status vocabulary does not allow a conditional hypothesis to be called qualified"),
]


def write(name, cols, rows):
    with open(HERE / name, "w", newline="") as f:
        w = csv.DictWriter(f, cols, delimiter="\t", lineterminator="\n")
        w.writeheader()
        for r in rows:
            assert all("\t" not in str(v) and "\n" not in str(v) for v in r.values()), r["id"] if "id" in r else r
            w.writerow(r)


def main():
    write("proposals_it21_p3b.tsv", PROPOSAL_COLS, P)
    write("qualification_it21_p3b.tsv", QUAL_COLS, Q)
    write("phenotype_first_it21_p3b.tsv", PF_COLS, PF)
    write("path_d_it21_p3b.tsv", D_COLS, D)
    write("negatives_it21_p3b.tsv", N_COLS, N)
    print(len(P), "proposals", len(Q), "qualifications")


if __name__ == "__main__":
    main()
