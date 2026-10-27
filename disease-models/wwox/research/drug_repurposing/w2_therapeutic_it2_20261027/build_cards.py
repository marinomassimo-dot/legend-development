#!/usr/bin/env python3
"""Writes the three W2 packets (F01 glutamate-receptor node, F02 myelination, F03 chloride gradient) into ../cards/ and builds
each stored card with repurposing_bridge.build_card (the same builder check_cards.py re-runs). scientist-c, 2026-10-27,
task SC-IT2-THERAPEUTIC-20261027. Templates: the E02 and E04 packets (same shape, every field overridden here).
Run from the repository root: python3 disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/build_cards.py"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
import copy
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
CARDS = HERE.parent / "cards"
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import repurposing_bridge as bridge  # noqa: E402

E02 = json.loads((CARDS / "E02_ldh_inhibition.packet.json").read_text())
E04 = json.loads((CARDS / "E04_ketogenic_lactate_axis.packet.json").read_text())
MAN = "disease-models/wwox/research/deepdive_manifests"
NOTE = "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/README.md"
NWE = "NOT WWOX EVIDENCE"
BRETON = "PAPER 031 (Breton 2021, neuron-specific Wwox knockout mouse slices)"


def ctx(d, g, s, c, st):
    return {"disease_id": d, "genotype": g, "species": s, "cell_type": c, "developmental_stage": st}


KO_SLICE = ctx("Wwox-null neuron-specific knockout mouse neocortex (ex vivo slice)", "Synapsin-Cre Wwox knockout versus wild type and heterozygote",
               "mouse", "layer II/III neocortex, local field potential and pyramidal-cell patch", "juvenile, about two weeks of age (as printed; not re-derived here)")
ORG = ctx("WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele; no amyloid)",
          "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)", "human", "cerebral organoid, bulk RNA", "organoid, culture week 15")
GRIN = ctx("GRIN-related developmental and epileptic encephalopathy (not WWOX)", "pathogenic GRIN1/GRIN2A/GRIN2B/GRIN2D variants classified by in-vitro assays as gain of function",
           "human", "individuals, mostly children", "median age 9 years (as reported)")
GRIN_LOF = dict(GRIN, genotype="GRIN variants classified loss of function, indeterminate or no effect")
RAT = ctx("hyperbaric-oxygen seizure model in adult rats (not WWOX, not a genetic epilepsy)", "wild-type adult male rats", "rat", "whole animal", "adult")
ADULT = ctx("WWOX-DEE adult case report (one individual, long disease course)", "WWOX-DEE; allele per the source", "human", "individual", "adult, decades after onset")
COMMON_CHECKS = {"support_and_replication": "One laboratory for every WWOX row used here; no independent replication.",
                 "formal_checks": "Breton rows carry verbatim locators in the manifest (receipt FTR-20260810-34634460-02); the n values of the d-APV arm and the mEPSC text were re-read first-hand from the shared full-text XML on 2026-10-27 without a new receipt. GRIN and rat rows are at the reading depth stated per row.",
               "card_inferences_owed_audit": "Every statement marked INFERENZA, and every card-level synthesis, is owed a blind audit by someone other than the producer."}


def base(template, cid, name, axis, note):
    p = copy.deepcopy(template)
    p["axis"] = axis
    p["candidate"] = {"id": cid, "name": name}
    p["mission_dimensions"]["route_note"] = note
    p["target_census"] = {"dir": "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027", "symbols": []}
    p.pop("no_new_reading", None)
    p["no_new_reading"] = "W2 (scientist-c, 2026-10-27): no new full-text receipt; first-hand re-reads of already-receipted papers and of open PubMed Central text are described in the W2 record."
    return p


def row(i, tid, ep, dr, src, loc, tag, depth, c, note, scope, receipt=None):
    r = {"id": i, "target_id": tid, "endpoint": ep, "direction": dr, "source": src, "locator": loc, "epistemic_status": tag,
         "reading_depth": depth, "context": c, "measured_result_note": note, "evidence_scope": scope}
    if receipt:
        r["receipt"] = receipt
    return r


# ---------------------------------------------------------------- F01
f1 = base(E02, "P4-F-01", "Glutamate-receptor node of the neuron-specific Wwox bursting phenotype: memantine (NMDAR pore blocker) and perampanel (AMPAR antagonist)",
          "F / W2 therapeutic: postsynaptic glutamatergic gain", "Partial benefit / protection of function at best (network state); WWOX function stays lost. Variant-independent (Track A); Track B (missense class) unmeasured. Seizure or burst control is not developmental recovery (N-15).")
f1["disease_assertions"] = [
    row("DA-W2-001", "neocortical spontaneous bursting (local field potential)", "fraction of slices with bursts", "INCREASE", BRETON,
        MAN + "/PMID34634460.json verbatim_locators.entries[0]", "DATO", "complete_fulltext_read", KO_SLICE,
        "Wild type 0 of 11 slices, heterozygote 4 of 23, knockout 36 of 42 (the heterozygote fraction is about a sixth of the knockout's).", "WWOX_BIOLOGY_OTHER_CONTEXT", "FTR-20260810-34634460-02"),
    row("DA-W2-002", "postsynaptic miniature excitatory current (mEPSC, clamp at a hyperpolarised potential)", "mEPSC amplitude", "INCREASE", BRETON,
        "PMC XML files/fulltext/PMID34634460_Breton2021_PMC.xml, section 2.3 and Fig 4 legend (re-read first-hand 2026-10-27; not a manifest entry)", "DATO", "complete_fulltext_read", KO_SLICE,
        "Amplitude shifted up in knockout (cumulative distributions, KS test on pooled events; 10 cells per genotype from 4 wild-type, 5 heterozygote and 5 knockout animals); frequency is not different from the heterozygote but does differ from wild type (KS P about 2.4e-4; direction not stated in the text); decay time constant not different, which the authors read as no overt change of the NMDAR:AMPA proportion. INFERENZA (the producer's, not the paper's): at the -70 mV holding potential NMDAR current is largely magnesium-blocked, so the recording is probably AMPAR-weighted; a residual NMDAR component is not excluded and no NMDAR current was measured.", "WWOX_BIOLOGY_OTHER_CONTEXT", "FTR-20260810-34634460-02"),
    row("DA-W2-003", "delayed evoked response (layer V stimulation, layer II/III recording)", "amplitude of the delayed negative deflection", "INCREASE", BRETON,
        MAN + "/PMID34634460.json verbatim_locators.entries[25] (Supplementary Fig S3; supplement figure attested, the PMC bin document was not served)", "DATO", "complete_fulltext_read", KO_SLICE,
        "Present in knockout and absent in wild type, reversibly suppressed by d-APV; the authors read it as dysregulated NMDAR-mediated signalling. A circuit-level NMDAR dependence, not a receptor-level gain.", "WWOX_BIOLOGY_OTHER_CONTEXT", "FTR-20260810-34634460-02"),
    row("DA-W2-004", "human GRIA1 and GRIN-subunit transcripts", "CPM, knockout minus wild type", "UNKNOWN", "GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, " + NOTE,
        "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv", "INFERENZA", "queried_not_full_read", ORG,
        "No consistent GRIN2B or GRIN2D shift at 4 versus 2 libraries; GRIN2A and GRIN3A are low-count; GRIA1 is higher in two knockouts (cko1, cko2) and overlaps wild type in the other two, and the libraries differ in composition (GAD1 and regional-patterning transcripts differ ten-fold). Transcript is not receptor function; direction left UNKNOWN on purpose.", "COMPUTATIONAL_RESULT"),
]
f1["drug_assertions"] = [
    row("DR-W2-001", "NMDAR (tool compound d-APV, competitive, full block)", "burst frequency", "DECREASE", BRETON, MAN + "/PMID34634460.json verbatim_locators.entries[2]; first-hand: Results 2.2 sentence 'eliminated the spontaneous bursting events'",
        "DATO", "complete_fulltext_read", KO_SLICE,
        "Bursting eliminated and recovered on washout; n of the d-APV arm is 5 slices from 3 animals (legend). The authors call d-APV 'a glutamatergic blocker' but d-APV is NMDAR-selective: the AMPAR contribution was never tested in this paper. A full competitive block does not predict the effect of a partial use-dependent pore blocker.", "WWOX_EXPERIMENT_IN_DEE_SYSTEM", "FTR-20260810-34634460-02"),
    row("DR-W2-002", "NMDAR pore blocker memantine; GRIN gain-of-function variants", "clinical improvement (behaviour, development, seizure frequency)", "DECREASE",
        "Karnstedt 2026, Epilepsia (PMID 41489401, PMC13075606; " + NWE + "; other disease)", "PMC full text retrieved through the PMC API on 2026-10-27, results and Table 1 read; supplements not; no receipt", "DATO", "partial_fulltext_read", GRIN,
        "Benefit in 14 of 19 individuals with gain-of-function variants, of whom 4 had an effect that faded (10 sustained; at variant level counting sustained effect only the authors report P = 0.0698, not significant) (behaviour 12 of 17, development 6 of 12, seizure frequency reduced in 7 of 18); three gain-of-function individuals worsened. Retrospective, unblinded, clinician or parent rated.", "OTHER_DISEASE_PRECEDENT"),
    row("DR-W2-003", "NMDAR pore blocker memantine; GRIN loss-of-function, indeterminate or no-effect variants (the comparator group also holds 4 variants the authors call non-pathogenic)", "clinical improvement", "NO_CHANGE",
        "Karnstedt 2026, Epilepsia (PMID 41489401; " + NWE + "; other disease)", "same reading as DR-W2-002; Fisher test reported 14 of 19 versus 3 of 15", "DATO", "partial_fulltext_read", GRIN_LOF,
        "Benefit in 3 of 15 (group of 15 includes 4 non-pathogenic variants), mild and parent-reported only; seizure reduction 2 of 10, not different from the gain-of-function group. The direction of the receptor lesion, not the presence of an NMDAR gene, separated responders.", "OTHER_DISEASE_PRECEDENT"),
    row("DR-W2-004", "NMDAR pore blocker memantine", "progression of oxygen-induced seizure stages", "INCREASE",
        "Alekseeva 2026, Biomedicines (PMID 42652189; " + NWE + "; adult rat, acute provoked seizures), as recorded in the repository", "disease-models/wwox/research/interventions_wave_20261019_scientist-c.md section 14; receipt FTR-20261019-42652189-01", "DATO", "complete_fulltext_read", RAT,
        "Memantine accelerated every seizure stage; perampanel delayed stage 4 but did not prevent seizures. The reading carries unresolved internal inconsistencies noted in that record. A safety-direction datum for a non-genetic model, not WWOX.", "OTHER_DISEASE_PRECEDENT", "FTR-20261019-42652189-01"),
    row("DR-W2-005", "NMDAR (GluN1/GluN2A and GluN1/GluN2B), memantine", "inhibitory potency across recorded assays", "DECREASE", "ChEMBL_37 (2026-05-01), activity table for CHEMBL807; " + NWE,
        "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/README.md section 4", "DATO", "queried_not_full_read",
        ctx("recombinant NMDAR in oocytes, HEK and CHO cells (database aggregate)", "GluN1 with GluN2A/2B/2C/2D; 22 of the 37 rows are human targets and 15 are Rattus norvegicus targets (the rest of the label is unknown-origin where ChEMBL says so)", "human and rat", "heterologous cells", "not applicable"),
        "The recorded IC50 values spread across more than four orders of magnitude between assays (voltage, magnesium, agonist level, read-out). Potency is context-dependent; no value is carried as a target exposure. ChEMBL carries no curated mechanism row for memantine in this release (the adapter returns the molecule without mechanism).", "EXTERNAL_DATABASE_RECORD"),
    row("DR-W2-006", "AMPAR, perampanel", "mechanism and label", "DECREASE", "ChEMBL_37 mechanism row CHEMBL1214124; openFDA label 2026-10-27 (" + NWE + ")",
        "framework/scripts/repurposing_adapter.py query chembl / openfda, run 2026-10-27", "DATO", "queried_not_full_read",
        ctx("approved drug label (partial-onset seizures from 4 years of age; adjunct in primary generalised tonic-clonic seizures from 12 years of age)", "not applicable", "human", "not applicable", "paediatric label as retrieved"),
        "Non-competitive AMPA-receptor antagonist; the label sections returned by the adapter do not include warnings, so the labelled safety profile is NOT assessed here.", "EXTERNAL_DATABASE_RECORD"),
    row("DR-W2-007", "AMPAR (perampanel) among seven antiseizure drugs", "seizure response", "NO_CHANGE", "Teplyshova 2024, Front Genet (PMID 39507621), as recorded in analysis/downstream_wwox_independent_rescue_census_20260921.md W2.5; the drug effect is NOT WWOX EVIDENCE (n = 1, polytherapy)",
        "that file section W2.5; receipt FTR-20261019-39507621-01", "DATO", "complete_fulltext_read", ADULT,
        "'No sustained positive effect of treatment was detected' for the whole list taken over decades in one adult; the drug is not isolated, the exposure and timing are unknown. n = 1 supports no statement about the drug in this genotype.", "WWOX_EXPERIMENT_IN_DEE_SYSTEM", "FTR-20261019-39507621-01"),
]
f1["p4_fields"] = {
    "endpoint_pursued": "In Wwox-deficient neocortical slices or human neurons at matched maturity: spontaneous burst frequency, duration, amplitude and phase-amplitude coupling under a graded memantine exposure versus a perampanel exposure versus the full NMDAR block, with the wild-type and heterozygous slices as internal comparators; then a developmental endpoint (myelin, synaptic maturation), because burst control alone is not recovery.",
    "functional_evidence_available": "d-APV abolishes bursting in the knockout slice (5 slices, 3 animals); the mEPSC amplitude (probably AMPAR-weighted, an inference) is raised; a delayed evoked response is NMDAR-dependent. No memantine or perampanel has been given to any Wwox system. Seven antiseizure drugs including perampanel gave no sustained benefit in one adult human case.",
    "temporal_or_model_limit": "Juvenile mouse slices, one laboratory, acute pharmacology; the authors themselves bound the age window; human organoid and clinical rows do not test the node.",
    "cellular_context": {"target_expression": "GRIN1, GRIN2B and GRIN2D transcripts are present in the week-15 organoid (counts per million in the W2 table); GRIA1 is present; higher in two of four knockouts, overlapping wild type in the other two.",
                         "cells_tissue_stage": "layer II/III neocortical pyramidal neurons for the slice rows; bulk organoid for transcripts.",
                         "coverage": "UNKNOWN.", "limits": "No receptor-level measurement of NMDAR or AMPAR current, subunit composition or surface level exists for any WWOX system."}}
f1["p4_card"].update({
    "identity": "Memantine (approved, uncompetitive NMDAR pore blocker; paediatric safety and effectiveness not established on its label) and perampanel (approved, non-competitive AMPAR antagonist; paediatric label for partial-onset seizures). Tool compounds: d-APV. Both are symptomatic-network levers on one measured phenotype, not WWOX restoration.",
    "indication_and_transfer": "Only IF the neuron-specific Wwox bursting phenotype is driven by a measurable gain in glutamatergic transmission that a partial block of NMDAR or AMPAR corrects without harming activity-dependent maturation. Transfer to the reference genotype is unmeasured for both alleles: the slice model is a Synapsin-Cre knockout, not a missense or splice allele.",
    "novelty_for_woree": "Memantine on the NMDAR node is already map record R-02 (class PROMISING_BUT_MECHANISTIC_GAP). New here: (1) the sign of the receptor lesion decides memantine's response in the one genetic-NMDAR cohort that stratified by function, so the 'GRIN2A corroborates the node' argument (DL-MECH-002) corroborates the node, not the sign; (2) the AMPAR arm, never carried as a node, rests on the only direct synaptic measurement in the knockout (raised mEPSC amplitude), and is untested. Coverage: PubMed searches of 2026-10-27 (GRIN-memantine, neonatal memantine, WWOX myelin), the Karnstedt full text, the repository's perampanel notes; NON_TROVATO_NELLA_RICERCA for any memantine or perampanel arm in a Wwox model, not MAI_TENTATO.",
    "state_of_known_roads": "map R-02 (memantine), Chain B, N-15 (seizure control is not development), DL-MECH-002, DL-MOL-001; perampanel appears only in cohort notes (repurposing_10h_scientist-d_20261022c.md, parked item) and the adult case.",
    "pathway_and_objective": "BENEFICIO_PRECOCE; Track A; Track B untested.",
    "expected_contribution": "UNKNOWN. At best a reduction of a network state; no developmental benefit is implied.",
    "mechanism": "Targets: NMDAR (GRIN1 with GRIN2A/2B/2D) and AMPAR (GRIA1-4). Direction wanted: lower excitatory gain. Context: juvenile neocortical slice, neuron-specific knockout. Memantine is a use-dependent pore blocker with subunit-dependent, assay-dependent potency; d-APV is a competitive full block: the tool result does not transfer quantitatively to the drug.",
    "sources": {"internal": ["PAPER 031", "CLAIM 021", "CLAIM 031", "DL-MECH-002", "DL-MOL-001", "R-02", "Chain B", "N-15", "analysis/downstream_wwox_independent_rescue_census_20260921.md W2.5", "interventions_wave_20261019_scientist-c.md section 14"],
                "external_not_wwox_evidence": ["Karnstedt 2026 Epilepsia (PMID 41489401), PMC full text", "ChEMBL_37 activity and mechanism rows", "openFDA labels (memantine, perampanel) 2026-10-27", "PubMed abstract of PMID 42190144 (gene names are stripped in the retrieved text; the GRIN2A variant class is not stated there)"]},
    "evidence_for_and_against": {
        "for": ["d-APV abolishes bursting in the knockout slice and suppresses a knockout-specific delayed response.", "Postsynaptic mEPSC amplitude is raised in the knockout.", "Memantine benefited most individuals with gain-of-function GRIN variants (precedent in a channelopathy, other disease)."],
        "against": ["The only memantine-responsive genetic NMDAR group is defined by receptor gain of function; loss-of-function and indeterminate GRIN variants did not respond, so 'an NMDAR gene causes the same phenotype' (DL-MECH-002) does not give the sign.", "Dependence of bursting on NMDAR activity is permissive: it does not show that NMDAR function is raised; no NMDAR current or subunit was measured.", "A full competitive block (d-APV) eliminated bursting; a partial pore block at tolerable exposure may not; potency spans orders of magnitude across assays.", "Memantine accelerated provoked seizures in an adult rat oxygen model; its paediatric effectiveness is not established on its label.", "One adult WWOX case on perampanel plus six other drugs showed no sustained benefit (n = 1, not interpretable).", "Suppressing a network state is not correcting a developmental lesion (N-15)."],
        "transfer_limits": "Juvenile slice, one laboratory, knockout not allele; chronic NMDAR or AMPAR blockade in a developing brain also acts on activity-dependent maturation, including myelination (see F02)."},
    "time_to_access": "UNKNOWN for research use; both are marketed drugs (labels retrieved 2026-10-27).",
    "time_to_benefit": "UNKNOWN.",
    "pharmacology": "Memantine: use-dependent channel blocker; recorded potency depends on voltage, magnesium and agonist level and spans several orders of magnitude across assays (README section 4). Perampanel: non-competitive AMPAR antagonist. CNS exposure for both is expected from their indications but is not verified here for the slice-relevant free fraction.",
    "paediatrics_and_interactions": "Memantine label: paediatric safety and effectiveness not established; two controlled paediatric autism studies failed. Perampanel label: partial-onset seizures from 4 years of age. Interactions and labelled warnings were NOT assessed (adapter sections lacked them). No paediatric suitability for WWOX-DEE is presumed.",
    "scope_of_checks": COMMON_CHECKS,
    "question_history": ["map R-02 and Chain B", "DL-MECH-002 (GRIN2A corroboration)", "mandate 2026-10-27 (W2, iteration 2)"],
    "predictions": "Registered before any experiment: (a) if bursting reflects raised NMDAR function, a partial memantine exposure lowers burst frequency in knockout slices dose-dependently and not in wild type; (b) if it reflects raised AMPAR gain, perampanel does and memantine less; (c) if both are permissive routes of a network that recruits NMDAR, only the full block works and neither drug is a lever. Result (c) closes the strand.",
    "next_measurement": "Wet-lab, not done: Wwox-deficient versus parental or isogenic neurons or slices; graded memantine versus perampanel versus d-APV; controls: wild type, heterozygote, vehicle, washout, an NMDAR-selective and an AMPAR-selective evoked-current check to define which receptor is raised (NMDA:AMPA ratio under voltage control, not the mEPSC decay); endpoints: burst frequency, duration, amplitude, phase-amplitude coupling, then a maturation endpoint; discriminating result: a partial block that abolishes bursting in knockout and spares wild-type activity versus one that does not.",
    "status": "hypothesis",
    "value_added": "Separates two things the record had fused: the node (NMDAR-dependent network) and the sign of an intervention on it, and adds the one untested receptor with a direct measurement behind it.",
    "clinical_census": E02["p4_card"]["clinical_census"]})
f1["not_known"] = ["Whether NMDAR current, subunit composition or surface level is raised in any WWOX system.", "Whether the raised mEPSC amplitude is AMPAR-mediated.", "Whether a partial pore block reproduces the full block's effect on bursting.", "Whether either drug affects maturation in a developing Wwox-deficient brain.", "The GRIN2A variant class behind the burst-suppression association in the cohort abstract."]
f1["evidence_against"] = f1["p4_card"]["evidence_for_and_against"]["against"]
f1["bridge_gaps_exposed"] = ["Tool-compound and drug rows share the target but differ in block type, so the bridge's sign comparison for d-APV is not a statement about memantine.", "GRIN cohort rows are a different disease; no sign comparison is formed with the slice rows."]
f1["translation"] = {"pediatric_suitability": "Memantine: not established on its label. Perampanel: labelled from 4 years of age for partial-onset seizures. WWOX-DEE: UNKNOWN.", "cns_exposure": "UNKNOWN for the slice-relevant exposure.", "interactions": "UNKNOWN", "access": "UNKNOWN", "time_to_benefit": "UNKNOWN", "functional_rescue": "UNKNOWN"}
f1["p4_roadmap_fields"] = {"indication_and_transfer": f1["p4_card"]["indication_and_transfer"], "verification_scope": json.dumps(COMMON_CHECKS)}
f1["card_conventions"] = E02["card_conventions"]
f1.pop("abstention_card", None)

# ---------------------------------------------------------------- F02 (abstention)
f2 = base(E04, "P4-F-02", "Pro-myelinating agents and the activity-dependent myelination sign problem", "F / W2 therapeutic: myelination as broad functional recovery",
          "Broad functional recovery would need a developmental endpoint; the strand is held at abstention because no drug has been applied to a Wwox system for any myelin endpoint and the sign of the activity-myelin relationship in this genotype is unmeasured.")
f2["disease_assertions"] = [
    row("DA-W2-010", "MBP immunostaining intensity", "KO relative to WT, corpus callosum, cortex, striatum, anterior commissure", "DECREASE", "Obeid 2026 (PMID 42422765)", MAN + "/PMID42422765.json verbatim_locators.entries[43]", "DATO", "complete_fulltext_read",
        ctx("Wwox-null full knockout mouse brain", "Wwox -/- (FVB) versus wild type", "mouse", "white and grey matter regions", "about P90 (as printed; panel F age not stated)"),
        "Knockout MBP reduced relative to wild type; the printed Fig 6E labels (48 percent corpus callosum, 30 cortex, 50 striatum, 70 anterior commissure) were read by the independent verifier as the size of the REDUCTION, not the remaining fraction (bars give about 50, 72, 49 and 30 percent remaining); the only MBP quantification in the paper.", "WWOX_BIOLOGY_OTHER_CONTEXT", "FTR-20261019-42422765-01"),
    row("DA-W2-011", "MBP after neuronal AAV9-hSynI-WWOX", "MBP immunostaining (representative images only)", "INCREASE", "Obeid 2026 (PMID 42422765)", MAN + "/PMID42422765.json verbatim_locators.entries[6], [7], [43]", "DATO", "complete_fulltext_read",
        ctx("Wwox-null full knockout mouse brain, neonatal intracerebroventricular AAV9", "Wwox -/- treated with a low or a high vector dose versus wild type", "mouse", "corpus callosum, striatum, cortex", "about P90"),
        "The 'near-complete rescue at high dose, partial at low dose' is the authors' sentence on representative micrographs; no treated-arm quantification, no untreated-knockout column in that panel, no g-ratio or electron microscopy. The oligodendrocyte-promoter vector gave no detectable WWOX, so that arm does not test oligodendroglial relevance.", "WWOX_BIOLOGY_OTHER_CONTEXT", "FTR-20261019-42422765-01"),
    row("DA-W2-012", "human oligodendrocyte-lineage transcripts", "CPM, knockout minus wild type", "UNKNOWN", "GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, " + NOTE, "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv", "INFERENZA", "queried_not_full_read", ORG,
        "PDGFRA and OLIG1 are nominally higher in knockouts, SOX10, MOG and OLIG2 are not; counts are very low and composition differs; a week-15 organoid has no compact myelin. Not myelin evidence.", "COMPUTATIONAL_RESULT"),
]
f2["drug_assertions"] = []
f2["p4_fields"] = {
    "endpoint_pursued": "A myelin endpoint with a quantified treated arm in a Wwox-deficient system (MBP or g-ratio by electron microscopy, oligodendrocyte counts) after a pro-myelinating agent, after chronic activity suppression, and after an activity-raising manipulation, each against a Wwox-deficient vehicle arm.",
    "functional_evidence_available": "Neuron-specific, not oligodendrocyte-specific, Wwox loss reproduces the hypomyelination (genetic evidence of the earlier mouse work, PMID 34268881 manifest); neuronal gene replacement is reported to restore MBP by image. No pro-myelinating compound has been given to any Wwox system.",
    "temporal_or_model_limit": "Mouse, early postnatal window; the AAV rescue works to the earliest days tested and later ages were not testable in the null.",
    "cellular_context": {"target_expression": "Oligodendrocyte-lineage transcripts are barely detectable in the week-15 organoid.", "cells_tissue_stage": "in-vivo mouse white matter for the disease rows.", "coverage": "UNKNOWN.", "limits": "Myelin is measured as MBP image intensity; the treated-arm quantification does not exist."}}
f2["p4_card"].update({
    "identity": "Pro-myelinating agents (muscarinic-antagonist class such as clemastine and benztropine, thyroid-hormone and antipsychotic routes) and, as a separate question, activity manipulation as a myelin lever.",
    "indication_and_transfer": "Only IF the Wwox-deficient oligodendrocyte lineage is itself the limiting compartment, which the neuron-versus-oligodendrocyte genetic arms argue against. Transfer unmeasured.",
    "novelty_for_woree": "N-13 stands. New: the earlier record (DL-MECH-031 point 2) proposed that reducing seizure load might itself improve myelination because myelination is activity-dependent. The best-matched non-WWOX datum points the other way for a seizing network: Knowles 2022, Nat Neurosci (PMID 35501379, abstract read; absence-seizure models, not WWOX) reports that seizure-driven activity increases oligodendrogenesis and myelination in the seizure network, is prevented by seizure suppression, and that blocking activity-dependent myelination lowers seizure burden. The Wwox-null brain is hypomyelinated despite bursting, so neither simple sign is established. Also found: the 'near-complete MBP rescue' of the neuronal AAV is image-only (DA-W2-011).",
    "state_of_known_roads": "map N-13, DL-MECH-031, HYP-20260709-07, N-15.",
    "pathway_and_objective": "BENEFICIO_PRECOCE if ever; broad recovery needs the developmental endpoint.",
    "expected_contribution": "UNKNOWN.",
    "mechanism": "Target (if pursued): oligodendrocyte differentiation or the axon-oligodendrocyte activity signal. Direction wanted: more compact myelin. The causal compartment is neuronal, so a drug acting on oligodendrocytes alone is not expected to reach the cause.",
    "sources": {"internal": ["CLAIM 003", "DL-MECH-031", "N-13", "N-15", "HYP-20260709-07", "PMID 42422765 manifest", "PMID 34268881 manifest"], "external_not_wwox_evidence": ["Knowles 2022 Nat Neurosci (PMID 35501379), abstract only", "Saab 2016 Neuron (PMID 27292539), title only: oligodendroglial NMDA receptors and axonal energy metabolism"]},
    "evidence_for_and_against": {"for": ["Myelin is reduced in the knockout and activity-dependent myelination exists in other systems."],
        "against": ["Oligodendrocyte-lineage deletion shows no anomaly while neuronal deletion reproduces it.", "The oligodendrocyte-promoter AAV arm gave no detectable protein, so it neither supports nor refutes oligodendroglial relevance.", "In a seizure network, activity drives maladaptive myelination in the other-disease precedent: suppressing activity may lower or raise myelin depending on the system; the sign here is unmeasured.", "Oligodendroglial NMDA receptors support axonal energy metabolism in the other-disease precedent, so chronic NMDAR block (F01) has a myelin-side cost that is unmeasured.", "The myelin window closes early."],
        "transfer_limits": "Absence-seizure and healthy-brain systems; adult versus neonatal; no Wwox arm."},
    "time_to_access": "UNKNOWN.", "time_to_benefit": "UNKNOWN.",
    "pharmacology": "Not assessed: no compound is carded.",
    "paediatrics_and_interactions": "Not assessed.",
    "scope_of_checks": COMMON_CHECKS,
    "question_history": ["map N-13", "DL-MECH-031", "mandate 2026-10-27 (W2)"],
    "predictions": "Registered: if hypomyelination is driven by loss of an axonal signal, an oligodendrocyte-directed compound leaves it unchanged in Wwox-deficient neurons and corrects it only after neuronal restoration; if activity raises myelin in this genotype, chronic suppression lowers MBP; if activity suppression helps, MBP rises. The three outcomes are separable by one chronic-suppression arm and one activity-raising arm against vehicle.",
    "next_measurement": "Wet-lab, not done: Wwox-null (or conditional neuronal) mice or co-cultures; arms: vehicle, chronic activity suppression, activity-raising manipulation, one pro-myelinating agent; controls: wild type with the same arms, neuronal-restoration positive control; endpoints: quantified MBP and g-ratio by electron microscopy, oligodendrocyte counts; discriminating result: the direction of the myelin change under suppression versus under activity.",
    "status": "abstention",
    "value_added": "Records that the seizure-load-improves-myelin inference was an assumption with a counter-precedent, and that the neuronal rescue's myelin evidence is image-level.",
    "clinical_census": E04["p4_card"]["clinical_census"]})
f2["abstention_card"] = {"kind": "ABSTENTION",
    "missing_datum": "A quantified myelin endpoint in a Wwox-deficient system after any pro-myelinating compound or any chronic activity manipulation; never done.",
    "search_record": "PubMed 2026-10-27: WWOX with oligodendrocyte and remyelination returned nothing; WWOX with myelin returned nine records, none a pro-myelinating drug arm; Knowles 2022 found by a targeted query. Reopening condition: a Wwox-system myelin result under activity or compound manipulation, or evidence of a cell-autonomous oligodendroglial WWOX function (the residual gap the neuronal rescue left, which the authors attribute to it as their hypothesis).",
    "adjacent_context_not_wwox_evidence": ["activity-dependent maladaptive myelination in absence-seizure models (Knowles 2022, abstract)"],
    "an_abstention_is_a_result": "N-13 stays deprioritised; the added content is the unresolved sign and the image-level qualification."}
f2["not_known"] = ["Whether activity raises or lowers myelin in the Wwox-deficient brain.", "Whether any pro-myelinating agent acts on Wwox-deficient oligodendrocytes.", "The quantified MBP or g-ratio after neuronal AAV rescue.", "Whether an oligodendroglial WWOX function exists under remyelination stress."]
f2["evidence_against"] = f2["p4_card"]["evidence_for_and_against"]["against"]
f2["bridge_gaps_exposed"] = ["No drug assertion exists, so no comparison is formed."]
f2["translation"] = {k: "UNKNOWN" for k in ("pediatric_suitability", "cns_exposure", "interactions", "access", "time_to_benefit", "functional_rescue")}
f2["p4_roadmap_fields"] = {"indication_and_transfer": f2["p4_card"]["indication_and_transfer"], "verification_scope": json.dumps(COMMON_CHECKS)}

# ---------------------------------------------------------------- F03 (abstention)
f3 = base(E04, "P4-F-03", "Bumetanide and the chloride gradient (E_GABA premise)", "F / W2 therapeutic: GABA polarity", "Symptomatic network lever on an unmeasured premise; the single decisive experiment is specified, not run.")
f3["disease_assertions"] = [
    row("DA-W2-020", "SLC12A2 (NKCC1) over SLC12A5 (KCC2) transcript ratio", "ratio per library", "UNKNOWN", "GSE156243 (PMID 34268881 deposit); descriptive panel by scientist-c, " + NOTE, "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv", "INFERENZA", "queried_not_full_read", ORG,
        "Ratio 0.24, 0.29, 0.13, 0.14 in the four knockouts and 0.29, 0.30 in the two wild types: not higher in knockouts, so no transcript-level hint of a more depolarising chloride gradient; SLC12A2 is flat and SLC12A5 is higher in two knockouts. Composition-confounded (GAD1 about ten-fold different), transcript not function, direction left UNKNOWN.", "COMPUTATIONAL_RESULT"),
    row("DA-W2-021", "GABRB2 and GABRB3 transcripts", "CPM, knockout minus wild type", "DECREASE", "GSE156243 descriptive panel by scientist-c (the marker pattern behind DL-MECH-035)", "disease-models/wwox/research/drug_repurposing/w2_therapeutic_it2_20261027/organoid_panel_cpm.tsv", "INFERENZA", "queried_not_full_read", ORG,
        "GABRB2 about a quarter and GABRB3 about half of wild type; the same libraries carry more GABAergic-lineage transcripts. Reduced receptor transcript is not a chloride gradient.", "COMPUTATIONAL_RESULT")]
f3["drug_assertions"] = []
f3["p4_fields"] = {"endpoint_pursued": "Perforated-patch GABA reversal potential in Wwox-deficient versus isogenic neurons or slices at matched maturity, with NKCC1 and KCC2 protein and the GABA response itself; only if depolarising, a bumetanide effect on bursting.",
    "functional_evidence_available": "None: no chloride, E_GABA, NKCC1 or KCC2 protein, or GABA pharmacology has been measured in any Wwox system.",
    "temporal_or_model_limit": "Depolarising GABA is an early developmental state; the window may be closed in the juvenile slice.",
    "cellular_context": {"target_expression": "SLC12A2 and SLC12A5 transcripts are present in the week-15 organoid.", "cells_tissue_stage": "bulk organoid.", "coverage": "UNKNOWN.", "limits": "Transcript ratio is not E_GABA."}}
f3["p4_card"].update({
    "identity": "Bumetanide (approved loop diuretic). Identity check 2026-10-27: ChEMBL_37 curates its mechanism as inhibition of the NKCC2 transporter only; NKCC1 appears in three activity rows (two single-concentration inhibition readings in HEK cells and one fitted value in HT-29 cells by rubidium uptake), so the NKCC1 target of the repurposing idea is an activity-table fact, not a curated mechanism.",
    "indication_and_transfer": "Only IF GABA is depolarising in Wwox-deficient neurons at the relevant age; unmeasured. The CNS penetration of bumetanide is a known limitation (map R-07).",
    "novelty_for_woree": "Map R-07 stands as INSUFFICIENT_EVIDENCE. New: (1) the transcript-level ratio in the one human knockout deposit does not point to a depolarising gradient (descriptive, confounded); (2) the target-identity note above; (3) the single experiment is written out with controls. Neonatal-seizure and autism trials exist (titles retrieved: NEMO open-label dose-finding in newborn hypoxic-ischaemic seizures, PMID 25765333; a phase 3 autism programme, PMID 35292925; a phase 2 autism trial, PMID 32730977); their outcomes were NOT read here.",
    "state_of_known_roads": "map R-07, Chain M3, DL-MECH-035.", "pathway_and_objective": "BENEFICIO_PRECOCE; Track A.", "expected_contribution": "UNKNOWN.",
    "mechanism": "Target NKCC1 (SLC12A2); wanted direction: lower intracellular chloride so GABA hyperpolarises; sign depends on an unmeasured quantity.",
    "sources": {"internal": ["map R-07", "DL-MECH-035", "PMID 30361190 reading (receipt FTR-20261003-30361190-01)"], "external_not_wwox_evidence": ["ChEMBL_37 mechanism and activity rows for CHEMBL1072", "PubMed titles PMID 25765333, 35292925, 32730977 (outcomes not read)"]},
    "evidence_for_and_against": {"for": ["GABAergic-lineage and receptor-subunit transcripts differ in the knockout organoid."], "against": ["No transcript-level hint of a raised NKCC1:KCC2 ratio in the knockout organoid.", "Poor CNS penetration is a known limitation.", "Window may be closed.", "No measurement of the premise."], "transfer_limits": "Bulk organoid transcripts; juvenile slice."},
    "time_to_access": "UNKNOWN.", "time_to_benefit": "UNKNOWN.", "pharmacology": "NKCC1 activity: one fitted value and two single-concentration readings in ChEMBL (values in the README). Brain exposure not verified here.",
    "paediatrics_and_interactions": "Not assessed.", "scope_of_checks": COMMON_CHECKS, "question_history": ["map R-07", "mandate 2026-10-27 (W2: note the single-experiment ask)"],
    "predictions": "Registered: if GABA is hyperpolarising in the knockout at the age studied, the card closes; if depolarising, bumetanide at a brain-relevant exposure lowers burst frequency, and a negative result at that exposure does not refute the premise.",
    "next_measurement": "Gramicidin perforated-patch E_GABA in Wwox-deficient versus parental neurons or slices at three ages (including the earliest culturable), NKCC1 and KCC2 protein by immunoblot or immunostaining, GABA puff response; controls: wild type and heterozygote, bicuculline or gabazine sensitivity, an NKCC1 knockdown arm in place of the drug; discriminating result: a depolarised E_GABA specific to the knockout that an NKCC1 manipulation shifts.",
    "status": "abstention", "value_added": "Names the premise measurement, corrects the target identity record, adds a transcript-level negative hint.", "clinical_census": E04["p4_card"]["clinical_census"]})
f3["abstention_card"] = {"kind": "ABSTENTION", "missing_datum": "E_GABA, NKCC1 and KCC2 protein in any Wwox system; never measured.",
    "search_record": "Map R-07 and DL-MECH-035 searches; ChEMBL and an organoid transcript panel on 2026-10-27. Reopening condition: an E_GABA measurement, in either direction.",
    "adjacent_context_not_wwox_evidence": ["neonatal-seizure and autism bumetanide trials (titles only)"], "an_abstention_is_a_result": "R-07 stays INSUFFICIENT_EVIDENCE with the experiment written out."}
f3["not_known"] = ["E_GABA in any Wwox system.", "NKCC1 and KCC2 protein levels.", "Brain exposure of bumetanide at a relevant dose."]
f3["evidence_against"] = f3["p4_card"]["evidence_for_and_against"]["against"]
f3["bridge_gaps_exposed"] = ["No drug assertion exists, so no comparison is formed."]
f3["translation"] = {k: "UNKNOWN" for k in ("pediatric_suitability", "cns_exposure", "interactions", "access", "time_to_benefit", "functional_rescue")}
f3["p4_roadmap_fields"] = {"indication_and_transfer": f3["p4_card"]["indication_and_transfer"], "verification_scope": json.dumps(COMMON_CHECKS)}

for name, p in (("F01_glutamate_receptor_node", f1), ("F02_myelination_activity_sign", f2), ("F03_bumetanide_chloride_gradient", f3)):
    (CARDS / f"{name}.packet.json").write_text(json.dumps(p, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    (CARDS / f"{name}.card.json").write_text(json.dumps(bridge.build_card(p), indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", name)
