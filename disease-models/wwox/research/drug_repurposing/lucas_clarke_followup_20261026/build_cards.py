#!/usr/bin/env python3
"""Writes the four E-series packets of the Lucas-Clarke follow-up into ../cards/ and builds each stored card with
repurposing_bridge.build_card (the same builder check_cards.py re-runs). scientist-c, 2026-10-26.

Why a script and not four hand-typed JSON files: the disease-side assertions are shared between cards and a typed copy
drifts. The packets and cards are still ordinary files in cards/ and check_cards.py treats them like the A-D series.
Run from the repository root: python3 disease-models/wwox/research/drug_repurposing/lucas_clarke_followup_20261026/build_cards.py
"""
import sys as _sys
if any(a in ("-h", "--help") for a in _sys.argv[1:]):  # a documented command must answer --help without touching the network or any file
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

PAPER = "PAPER 567 (published Lucas-Clarke 2026 article; Drosophila Alzheimer's-amyloid model; NOT WWOX EVIDENCE: a fly amyloid model, not WWOX-DEE)"
MAN = "disease-models/wwox/research/deepdive_manifests/PMID42909904.json verbatim_locators.entries"
RECEIPT = "FTR-20261026-42909904-01"
GSE = "GSE156243, the deposit of the 2021 organoid paper (PMID 34268881); exploratory set-level analysis by scientist-c"
FLY = "Drosophila neuronal Wwox RNAi (about half of control mRNA by qPCR, no protein level) in an Abeta42 model; NOT WWOX-DEE EVIDENCE"


def fly_ctx(genotype, cell="adult fly head or brain (whole head for metabolomics and RNA-seq)"):
    return {"disease_id": "Drosophila model of Alzheimer's amyloid pathology (not WWOX-DEE)", "genotype": genotype,
            "species": "Drosophila melanogaster", "cell_type": cell, "developmental_stage": "adult, day 14 for omics and Atf4 imaging"}


ABETA = "neuronal Wwox RNAi plus neuronal Abeta42 (Arctic) versus control RNAi plus Abeta42"
NOAB = "neuronal Wwox RNAi versus control RNAi in a LacZ (no amyloid) background"
ORG = {"disease_id": "WWOX-deficient human cerebral organoid model (engineered knockout; NOT a patient allele; no amyloid)",
       "genotype": "WWOX knockout versus wild type (4 versus 2 libraries, one laboratory)", "species": "human",
       "cell_type": "cerebral organoid, bulk RNA", "developmental_stage": "organoid, culture week 15"}


def d(id_, target, endpoint, direction, source, locator, status, depth, ctx, note, receipt=None):
    row = {"id": id_, "target_id": target, "endpoint": endpoint, "direction": direction, "source": source,
           "locator": locator, "epistemic_status": status, "reading_depth": depth, "context": ctx,
           "measured_result_note": note}
    if receipt:
        row["receipt"] = receipt
    return row


# ------------------------------------------------------------------ shared disease-side assertions, one per contrast
D_ATF4_AB = d("DA-LC-ATF4-001", "fly Atf4 protein signal (immunofluorescence, brain)", "Atf4 fluorescence intensity", "INCREASE",
              PAPER, f"{MAN}[57], [59]; Fig 5H-I", "DATO", "complete_fulltext_read", fly_ctx(ABETA),
              "About 1.0 to about 1.2-1.3 normalised, n 6 brains, one antibody, four small regions of interest, y axis not at zero. Correlational. "
              "Atf4 is never knocked down or activated in the paper; PERK and eIF2 alpha phosphorylation are not measured.", RECEIPT)
D_ATF4_NO = d("DA-LC-ATF4-002", "fly Atf4 protein signal (immunofluorescence, brain)", "Atf4 fluorescence intensity", "NO_CHANGE",
              PAPER, f"{MAN}[58]; Supplementary Fig 5E", "DATO", "complete_fulltext_read", fly_ctx(NOAB),
              "No change without amyloid (t 0.0894, P 0.9305, n 6 brains). A measured null in a different contrast, not an unmeasured cell.", RECEIPT)
D_ISR_KO = d("DA-GSE-ISR-003", "ATF4 / integrated-stress-response canonical target transcripts (12 genes, declared before the set test)",
             "set-level transcript shift, knockout minus wild type", "DECREASE", GSE,
             "disease-models/wwox/research/drug_repurposing/gse156243/prediction_isr_ldh_chain_20261026.md, RESULT table", "INFERENZA",
             "queried_not_full_read", ORG,
             "Mean shift lower than 10,000 random same-size sets (P 0.0005); the gene-level direction of three genes had been seen before the sets were fixed; "
             "nine set tests across two analyses, none corrected for multiplicity; six libraries, genotype and composition confounded. Transcripts cannot see "
             "eIF2 alpha phosphorylation or ATF4 protein. EXPLORATORY NEGATIVE for the transcript signature without amyloid; not evidence that the ISR is normal.")
D_LDH_AB = d("DA-LC-LDH-001", "fly Ldh transcript", "Ldh log2 fold-change in head RNA-seq", "INCREASE", PAPER,
             f"{MAN}[29], [30], [31]; Supplementary Table 3", "DATO", "complete_fulltext_read", fly_ctx(ABETA),
             "About +1.29 log2 over Abeta42 alone, 4 pools of 10 heads. Abeta42 alone also raises Ldh (+1.11 in the table, 1.19 in the text). Ldh is not among the genes changed by knockdown in the LacZ background.", RECEIPT)
D_LAC_AB = d("DA-LC-LAC-001", "fly L-lactate (whole-head HILIC LC-MS)", "relative lactate abundance", "INCREASE", PAPER,
             f"{MAN}[39], [40], [43]; Supplementary Table 4; Fig 5C", "DATO", "complete_fulltext_read", fly_ctx(ABETA),
             "Interaction F 23.606, adjusted P 0.0174; knockdown effect +1.30 log2 under Abeta42. 5 pools of 10 heads, two-way ANOVA on the top 200 features by variance, 10 percent FDR. No flux, no isotope tracing, no NAD/NADH.", RECEIPT)
D_LAC_NO = d("DA-LC-LAC-002", "fly L-lactate (whole-head HILIC LC-MS)", "relative lactate abundance", "DECREASE", PAPER,
             f"{MAN}[40]; Supplementary Fig 5A", "DATO", "complete_fulltext_read", fly_ctx(NOAB),
             "Nominal -0.43 log2 without amyloid (simple effect not tested for significance). The lactate rise is conditional on amyloid.", RECEIPT)
D_CLIMB = d("DA-LC-CLIMB-001", "fly startle-induced climbing performance", "climbing height at days 14, 21 and 28", "DECREASE", PAPER,
            f"{MAN}[19], [53]; Fig 5E", "DATO", "complete_fulltext_read",
            fly_ctx("neuronal Abeta42 plus neuronal Wwox RNAi (the comparator and the test arm of the Ldh experiment share this background)", "whole fly"),
            "Climbing is lower with Wwox knockdown plus Abeta42 than with control RNAi plus Abeta42; N 4-6 vials.", RECEIPT)
D_LDHA_KO = d("DA-GSE-LDH-002", "human LDHA transcript", "log2 shift, knockout minus wild type", "INCREASE", GSE,
              "disease-models/wwox/research/drug_repurposing/gse156243/prediction_isr_ldh_chain_20261026.md, RESULT", "INFERENZA",
              "queried_not_full_read", ORG,
              "LDHA +0.75 by the script's shift (+0.91 on the authors' list, padj 5e-6). LDHA also falls with elapsed culture time in WWOX-unperturbed spheroids, so the rise is as consistent with a less advanced tissue as with a WWOX effect. Transcript, not activity.")
D_PDK_KO = d("DA-GSE-PDK-003", "human PDK1 transcript and the PDK/PDH transcript set", "log2 shift, knockout minus wild type", "DECREASE", GSE,
             "disease-models/wwox/research/drug_repurposing/gse156243/prediction_hif1a_pdk_chain_20261025.md and prediction_pyruvate_fate_20261026.md", "INFERENZA",
             "queried_not_full_read", ORG,
             "PDK1 -0.34; the PDK/PDH set +0.17 (P 0.22, not different from chance); LDH-to-PDH ratio not shifted (inside the spread of the two wild-type libraries). EXPLORATORY NEGATIVES: transcripts are not PDH activity, flux or metabolite, and do not show that PDH or lactate are normal.")
D_PDH_NONE = d("DA-LC-PDH-001", "fly PDH, PDK, pyruvate or pyruvate-to-TCA flux", "any measurement", "UNKNOWN", PAPER,
               f"{MAN}[44], [49]; dossier section 3 (pyruvate not reported; Fig 5D draws a TCA node with no data attached)", "DATO",
               "complete_fulltext_read", fly_ctx(ABETA),
               "The study measured no pyruvate, PDH, PDK, flux, oxygen consumption or NAD/NADH. Whether pyruvate was tested is unknown; the MetaboLights deposit is not publicly retrievable (mtbls12344.md). Pdk, Pdha, Pdhb are absent from the significant gene lists, which is not a test. The paper's own heading and abstract speak of pyruvate metabolism, but that rests on transcript pathway over-representation (KEGG, including Ldh itself; Pepck2, CG11052 and Adh lower), not on a pyruvate, PDH or PDK measurement.", RECEIPT)
D_MRS = d("DA-BIO008-001", "human brain lactate (MRS)", "brain lactate level in one WWOX patient", "DECREASE",
          "discovery_ledger_current DL-BIO-008 (one patient; reading depth not re-verified by this card)", "DL-BIO-008", "INFERENZA", "UNKNOWN",
          {"disease_id": "WWOX-DEE, one reported patient (class level)", "genotype": "UNKNOWN", "species": "human", "cell_type": "brain MRS voxel", "developmental_stage": "child"},
          "Reported extremely low in one patient; the same entry records raised mouse serum lactate. Not combined with the fly rows: different species, tissue and context.")
D_MRS["sign_vs_contrast"] = {"DA-LC-LAC-001": "OPPOSITE (DECREASE against INCREASE under Abeta42)",
                             "DA-LC-LAC-002": "SAME SIGN (DECREASE, nominal, without Abeta42); not a replication: other species, tissue and context"}


def p4_fields(endpoint, functional, limit, ctx):
    return {"endpoint_pursued": endpoint, "functional_evidence_available": functional, "temporal_or_model_limit": limit, "cellular_context": ctx}


def base(cid, name, axis, route, track, depth_note, diseases, drugs, f, card, not_known, against, gaps, abst=None):
    translation = {k: "UNKNOWN" for k in bridge.TRANSLATION}
    translation.update(card.pop("_translation", {}))
    packet = {
        "schema_version": 1,
        "axis": axis,
        "route": route,
        "mission_dimensions": {
            "track": track,
            "track_definition": "mission.md section 5: Track A = variant-independent WWOX loss of function; Track B = variant or allele-class specific (e.g. the Q230P missense class); Track C = repurposing, which is a method of reaching A or B, not a third lesion class",
            "route": route,
            "route_definition": "RECUPERO_PROFONDO = deep recovery of the lost function; BENEFICIO_PRECOCE = concrete partial benefit, symptomatic control or protection of function, with paediatric feasibility and time in view",
            "route_note": depth_note,
            "the_two_dimensions_are_independent": "a card keeps both: a variant-independent lever can be a partial-benefit lever, and a lesion-specific one can aim at deep recovery",
        },
        "candidate": {"id": cid, "name": name},
        "disease_assertions": diseases,
        "drug_assertions": drugs,
        "p4_fields": f,
        "p4_card": card,
        "not_known": not_known,
        "evidence_against": against,
        "bridge_gaps_exposed": gaps,
        "translation": translation,
        "p4_roadmap_fields": {"indication_and_transfer": card["indication_and_transfer"],
                              "verification_scope": json.dumps(card["scope_of_checks"], ensure_ascii=False)},
        "label_lookup": {"status": "NOT_ATTEMPTED"},
        "card_conventions": [
            "IPOTESI throughout; the bridge forces it. No score, rank, probability or blended index is carried.",
            "directional_summary compares signs only where target, endpoint and every context dimension match; UNRESOLVED is a statement about the record, not about the biology.",
            "Every disease-side row from the Drosophila article is NOT WWOX-DEE EVIDENCE; the organoid rows are exploratory transcript analyses of one deposit.",
            "Abstract-level statements from PubMed are labelled abstract_only; none carries a receipt.",
            "label_lookup is NOT_ATTEMPTED in the bridge: the bridge has no network. The openFDA adapter was run separately and is recorded in lucas_clarke_followup_20261026/compounds_and_sources.md.",
            "No dose, route, schedule or paediatric suitability appears; assay concentrations of the sources are deliberately not reproduced.",
        ],
        "no_new_reading": "No paper was newly read in full for these cards. The Lucas-Clarke reading is scientist-a's (receipt " + RECEIPT + "); the compound statements are abstract-level PubMed reads and registry-database retrievals (lucas_clarke_followup_20261026/).",
    }
    if abst:
        packet["abstention_card"] = abst
    return packet


COMMON_Q = ("UNKNOWN. No paediatric suitability is presumed by this card, for the candidate or for any historical authorisation of it for another use.")
SCOPE = {"support_and_replication": "No independent replication of any fly row is held; the organoid rows are one laboratory's deposit.",
         "formal_checks": "Disease-side fly rows carry verbatim locators in the manifest (104 entries; entries 31, 49, 89, 94 SUPPORTED by a blind audit, entry 95 narrowed after an OVERSHOOT finding); the compound statements are abstract-level and unaudited.",
         "card_inferences_owed_audit": "Statements marked INFERENZA, including every statement about what a compound would do in WWOX-deficient tissue, are OWED a blind audit by another actor."}
CLIN = ("Clinical census, ClinicalTrials.gov API v2, 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven queries returned no registered WOREE interventional study; "
        "it answers seven queries against one registry on one date and a missing hit does not prove that no study exists. Not re-run for this card.")

PACKETS = {}

# ============================================================== E01 ISR
PACKETS["E01_isr_modulators"] = base(
    "P4-E-01", "Integrated-stress-response modulators (eIF2B activators of the ISRIB class, PERK-arm inhibitors, repurposed translational-repression reversers)",
    "E / Lucas-Clarke follow-up: integrated stress response", "BENEFICIO_PRECOCE", "A",
    "Downstream of an unresolved lesion: even a correct ISR readout would change a consequence, not restore WWOX function. Deep recovery would need WWOX restored (card C01). "
    "Track B (Q230P class): whether the missing mutant protein state engages the ISR is not measured; nothing here is lesion-specific.",
    [D_ATF4_AB, D_ATF4_NO, D_ISR_KO], [
        d("DR-E01-001", "ISR biomarkers (blood cells and cerebrospinal fluid)", "ISR biomarker output under an eIF2B activator", "DECREASE",
          "Nat Commun 2025 phase 1b abstract, PMID 40825784; NOT WWOX EVIDENCE", "PubMed abstract (DOI 10.1038/s41467-025-63031-y)", "DATO", "abstract_only",
          {"disease_id": "amyotrophic lateral sclerosis (not WWOX)", "genotype": "sporadic and familial ALS, not WWOX", "species": "human", "cell_type": "peripheral blood mononuclear cells and CSF", "developmental_stage": "adult"},
          "Target engagement shown for DNL343, a brain-penetrant eIF2B activator."),
        d("DR-E01-002", "ALS functional rating and survival (joint model)", "disease rate ratio relative to placebo", "NO_CHANGE",
          "JAMA Netw Open 2026 randomised trial abstract, PMID 42771346; NOT WWOX EVIDENCE", "PubMed abstract (DOI 10.1001/jamanetworkopen.2026.34809)", "DATO", "abstract_only",
          {"disease_id": "amyotrophic lateral sclerosis (not WWOX)", "genotype": "sporadic and familial ALS, not WWOX", "species": "human", "cell_type": "whole organism, clinical endpoint", "developmental_stage": "adult"},
          "Ratio 1.04 (95 percent credible interval 0.83 to 1.32) over a 24-week placebo-controlled period: no benefit despite target engagement and proof of mechanism in the earlier phase. Adults with ALS; says nothing about a developmental encephalopathy."),
        d("DR-E01-003", "object-recognition memory, microglial activation, tau and amyloid burden", "recognition memory under an eIF2B activator (2BAct)", "INCREASE",
          "J Alzheimers Dis 2026 abstract, PMID 42179084; NOT WWOX EVIDENCE", "PubMed abstract (DOI 10.1177/13872877261450638)", "DATO", "abstract_only",
          {"disease_id": "5xFAD mouse model of Alzheimer's disease (not WWOX)", "genotype": "5xFAD transgenic", "species": "mouse", "cell_type": "whole animal behaviour", "developmental_stage": "ten-month-old adult"},
          "Better recognition memory and less microglial activation and tau; amyloid burden not reduced; p-eIF2 alpha lower. Mouse, adult, 23 days, one study."),
        d("DR-E01-004", "time to loss of walking with support in vanishing white matter (an eIF2B disease)", "hazard of loss of walking under guanabenz", "DECREASE",
          "Lancet Neurol 2026 single-arm phase 1/2 abstract, PMID 42586097; NOT WWOX EVIDENCE", "PubMed abstract (DOI 10.1016/S1474-4422(26)00241-3)", "DATO", "abstract_only",
          {"disease_id": "vanishing white matter (eIF2B lesion, not WWOX)", "genotype": "biallelic EIF2B variants, not WWOX", "species": "human", "cell_type": "whole organism, clinical endpoint", "developmental_stage": "children, onset at six years or younger"},
          "Hazard ratio 0.33 (0.16 to 0.69) against matched registry controls, non-randomised; serious adverse events in three quarters of 33 children, hallucinations in over half, severe constipation in three. A paediatric tolerability dataset in a disease whose lesion IS the ISR regulator."),
    ],
    p4_fields("A WWOX-linked ISR readout that a compound moves: ATF4 protein and eIF2 alpha phosphorylation (and ATF4-target transcripts) in WWOX-deficient human neural cells at matched maturity, with and without a defined proteotoxic challenge; then a functional endpoint (network, synaptic or myelin) after eIF2B activation.",
              "None for WWOX. In the fly, Atf4 signal rises only with Wwox reduction plus amyloid and Atf4 is never perturbed. In the one human knockout transcriptome the ISR target set is lower than chance (exploratory).",
              "Fly amyloid model with partial RNAi; one human knockout transcriptome without amyloid; every compound datum is from another disease, mostly adult.",
              {"target_expression": "ISR genes are expressed in neural tissue generally; the WWOX-dependent state is UNKNOWN.",
               "cells_tissue_stage": "fly neurons (Atf4 signal, whole-mount) and bulk organoid RNA; no cell-type resolution in either.",
               "coverage": "UNKNOWN for any WWOX system at protein level.",
               "limits": "The only signed human readout points the opposite way from the fly (ISR targets lower), and the fly readout needs amyloid."}),
    {"identity": "ISR attenuators: eIF2B activators (ISRIB and its clinical-stage successors), PERK-arm inhibitors, and repurposed compounds that reverse eIF2 alpha-P-mediated translational repression; guanabenz as the paediatric-experience member. Full per-compound table: lucas_clarke_followup_20261026/compounds_and_sources.md section 2.1.",
     "indication_and_transfer": "WWOX-DEE only IF a WWOX-dependent ISR elevation is shown in a human neural system. Today the transfer rests on a fly amyloid model; the one human knockout transcriptome does not show the signature. No Q230P or null-allele datum exists.",
     "novelty_for_woree": "NON_TROVATO_NELLA_RICERCA as a test: no source retrieved links an ISR modulator to WWOX deficiency; coverage is DGIdb, ChEMBL, Open Targets, PubTator 3 gene censuses and eight PubMed searches on 2026-10-26, and DGIdb, ChEMBL and Open Targets are themselves empty for the eIF2B activators. A zero is a statement about those queries.",
     "state_of_known_roads": "not in the earlier hand-made series (A-D); first ISR card.",
     "pathway_and_objective": "BENEFICIO_PRECOCE (partial benefit through a downstream lever); Track A (variant-independent), Track B conditional and unmeasured.",
     "expected_contribution": "UNKNOWN. If the ISR were elevated and harmful, attenuation could protect function; if it is adaptive, attenuation could add harm. Neither is measured for WWOX.",
     "mechanism": "Target: eIF2B (five-subunit complex, EIF2B1-5, HGNC:3257-3261) or the PERK arm (EIF2AK3, HGNC:3255); direction: attenuate the ISR; context: amyloid-stressed fly neurons in the paper; UNKNOWN in WWOX-DEE.",
     "sources": {"internal": ["PAPER 567", "CLAIM 025", "DL-MECH-020", "gse156243/prediction_isr_ldh_chain_20261026.md", "lucas_clarke_followup_20261026/biological_needs.md S1"],
                 "external_not_wwox_evidence": ["eIF2B-activator trial in ALS: target engaged, no clinical benefit (adults)", "eIF2B activator in a mouse amyloid model: memory and tau improved, amyloid not", "guanabenz in children with vanishing white matter: non-randomised benefit with frequent adverse events", "PERK inhibitor in a Parkinson mouse model: neuroprotection with signs of pancreatic toxicity"]},
     "evidence_for_and_against": {
         "for": ["The fly reports a raised Atf4 signal with Wwox reduction plus amyloid (n 6, one antibody).", "An eIF2B activator improved memory and tau in a mouse amyloid model.", "A paediatric dataset for an ISR-attenuating drug exists in a different, eIF2B-driven disease."],
         "against": ["Without amyloid the fly Atf4 signal does not change.", "In the human knockout organoid the ATF4/ISR target transcripts are lower than chance (exploratory, no amyloid).", "The ALS trial engaged the target and showed no benefit.", "Atf4 is not perturbed in the paper: the Atf4-to-Ldh step is the authors' inference.", "The paper reports that Ldh knockdown is detrimental in other fly amyloid models, a reminder that attenuating a stress arm has a cost."],
         "transfer_limits": "Amyloid load is the context of the fly effect; WWOX-DEE has no stated amyloid load. Adult neurodegeneration trials do not transfer to a developmental encephalopathy."},
     "time_to_access": "UNKNOWN. Compounds range from research tools to clinical-stage; availability for WWOX research is not assessed.",
     "time_to_benefit": "UNKNOWN.",
     "pharmacology": "Per compound in compounds_and_sources.md: no eIF2B activity in ChEMBL for ISRIB or fosigotifator; DGIdb and Open Targets empty for the eIF2B complex; PERK inhibitors have enzyme potency in ChEMBL.",
     "paediatrics_and_interactions": COMMON_Q,
     "scope_of_checks": SCOPE,
     "question_history": ["mandate 2026-10-26 (Lucas-Clarke follow-up)", "prediction_isr_ldh_chain_20261026.md"],
     "predictions": "None; no engine, no score.",
     "next_measurement": "Stage 1 (decides everything after it): eIF2 alpha phosphorylation, ATF4 protein and ATF4-target transcripts in WWOX-deficient versus isogenic human neural cells at matched maturity, with and without a defined proteotoxic challenge. If not elevated, park with the reopening condition below. Stage 2 (only if elevated): an eIF2B activator versus vehicle on that readout and on one functional endpoint. In the fly: an Atf4 loss-of-function arm with the Ldh and lactate readouts.",
     "status": "hypothesis",
     "value_added": "Turns 'ATF4 raised' into a context-labelled need (amyloid-conditional, fly) and shows that the only signed human readout points the other way, so the first experiment is the readout, not a drug.",
     "clinical_census": CLIN,
     "_translation": {"pediatric_suitability": "UNKNOWN for WWOX; guanabenz paediatric experience exists in vanishing white matter (abstract-level).", "functional_rescue": "UNKNOWN"}},
    ["Whether any WWOX-deficient human neural system has raised eIF2 alpha phosphorylation or ATF4 protein, with or without a proteotoxic load.",
     "Whether the fly Atf4 rise is upstream of Ldh (no Atf4 perturbation in the paper).",
     "Whether the PERK arm or another eIF2 kinase (the paper's Discussion names GCN1/GCN2) is the one engaged.",
     "Whether attenuating the ISR would help or harm a WWOX-deficient developing brain."],
    ["The organoid ISR target set is lower than chance (exploratory, uncorrected multiplicity across nine set tests).", "No Atf4 perturbation in the source paper.", "ALS trial: target engagement without benefit."],
    ["The bridge compares fly and organoid rows only where target, endpoint and context match; none match, so the directional summary is UNRESOLVED by construction."])

# ============================================================== E02 LDH
PACKETS["E02_ldh_inhibition"] = base(
    "P4-E-02", "LDH inhibition or lowering (stiripentol as the approved paediatric member; LDHA tool compounds; an LDHA-directed oligonucleotide approved for another disease)",
    "E / Lucas-Clarke follow-up: lactate dehydrogenase", "BENEFICIO_PRECOCE", "A",
    "A downstream metabolic lever with one genetic precedent in a fly (partial locomotor benefit). Not deep recovery; WWOX function would remain lost. Track B (Q230P class): no allele-specific rationale; the lever is allele-blind and untested for any allele.",
    [D_LDH_AB, D_LAC_AB, D_LAC_NO, D_CLIMB, D_LDHA_KO, D_MRS],
    [d("DR-E02-GEN-001", "fly startle-induced climbing performance", "climbing height at days 14, 21 and 28", "INCREASE",
       PAPER + "; GENETIC perturbation of the target, not a compound", f"{MAN}[51], [53], [54], [55], [56]; Fig 5E", "DATO", "complete_fulltext_read",
       fly_ctx("neuronal Abeta42 plus neuronal Wwox RNAi (the comparator and the test arm of the Ldh experiment share this background)", "whole fly"),
       "Partial rescue to or above the control line at day 28; once; no Ldh-alone arm; Wwox mRNA not reported in the double-RNAi line; lactate not measured in it; lifespan and amyloid load not tested; the authors cite Ldh knockdown as detrimental in other fly amyloid models.", RECEIPT),
     d("DR-E02-001", "human LDH5 and LDH1 enzyme activity (cell-free, UV-vis, pyruvate substrate)", "enzyme inhibition by stiripentol as comparator in a chemistry series", "DECREASE",
       "ChEMBL document CHEMBL4311969 = Bai 2019, Eur J Med Chem (PMID 31539780: alpha-asaronol esters as anticonvulsant LDH inhibitors; stiripentol is the comparator); NOT WWOX EVIDENCE", "lucas_clarke_followup_20261026/chembl_named_activities.tsv; document identity from the ChEMBL document record (sada_ldh_precedent_p2a_20261026.md section 4)", "DATO", "queried_not_full_read",
       {"disease_id": "enzyme assay, not a disease", "genotype": "recombinant human enzymes", "species": "human", "cell_type": "cell-free", "developmental_stage": "not applicable"},
       "Single-digit percent inhibition at the highest concentration tested, which is in the millimolar range, and no value for the lower concentration row; no IC50. The article is not read (paywalled; abstract only): substrate level, enzyme source and replicates are unknown. The same document holds stiripentol rows for a GABA-A receptor and for mouse seizure and rotarod assays, so the LDH row is one weak measurement among several. It is the lowest of three single-concentration measurements (see DR-E02-004 and DR-E02-005) at the highest concentration, and is not evidence of inefficacy: the stiripentol enantiomers in DR-E02-004 sit near the figure attributed to DR-E02-005, the racemate is lower, and no study reports a fitted potency for stiripentol."),
     d("DR-E02-004", "human LDHA enzyme activity (recombinant, fluorescence of NADH, saturating pyruvate)", "enzyme inhibition by stiripentol (racemate and enantiomers) against synthetic stiripentol-related compounds", "DECREASE",
       "Rico-Molina 2024, Int J Mol Sci (PMID 39769031, open access); NOT WWOX EVIDENCE", "deepdive_manifests/PMID39769031.json entries; Table 2; Supplementary Figures S65 to S67", "DATO", "partial_fulltext_read",
       {"disease_id": "enzyme assay (primary hyperoxaluria context, not WWOX)", "genotype": "recombinant human LDHA", "species": "human", "cell_type": "cell-free", "developmental_stage": "not applicable"},
       "Stiripentol racemate about a tenth inhibition at one high-micromolar concentration; its enantiomers about a third each in the same assay (racemate below both of its enantiomers, undiscussed, and the same racemate-outside-enantiomers scatter, up to two-fold, recurs in the analogue table); iso-stiripentol about a fifth; the IC50 entry for stiripentol is a bound, not a fitted value, and no curve is reported for it (curves only for the analogues; that none was run is an inference). Four analogues reach 46 to 72 percent at that concentration with fitted IC50 between about 100 and about 214 micromolar, steep curves (slope unconstrained by one or two points), no detergent named, 5 percent DMSO, positive-control result not shown: a screen-grade analogue series, no cell, brain or animal datum."),
     d("DR-E02-005", "LDH enzymes (purified mammalian), neuronal membrane potential, mouse seizure model", "LDH inhibition by stiripentol and by a stiripentol analogue (Sada 2015, Science)", "DECREASE",
       "Sada 2015, Science (PMID 25792327; paywalled, no lawful full text found); abstract plus secondary descriptions only; NOT WWOX EVIDENCE", "PubMed abstract; secondary statements in PMID 39769031 (about 40 percent inhibition at one high-micromolar concentration, both directions), PMID 41570991 (non-competitive) and PMID 36278433 (blood-brain-barrier crossing and cerebral LDH inhibition in mice)", "DATO", "abstract_only",
       {"disease_id": "epilepsy models (subthalamic neurons; a mouse seizure model; not WWOX)", "genotype": "UNKNOWN (the indexing terms list an inbred ICR mouse strain)", "species": "mouse", "cell_type": "neurons, purified enzyme", "developmental_stage": "UNKNOWN"},
       "Abstract: LDH inhibition hyperpolarised neurons (reversed by pyruvate), suppressed seizures in a mouse model, stiripentol is an LDH inhibitor, and a chemical modification gave a more potent inhibitor that suppressed seizures in vivo. The article was NOT read: its enzyme and in vivo numbers, exposure, controls and the analogue's identity are UNKNOWN to this card. The about-forty-percent figure is another laboratory's description of it."),
     d("DR-E02-006", "LDH activity in glioblastoma cell lysate and cell viability, and NADH-oxidising enzymes (complex I, malate dehydrogenase)", "cellular effect of stiripentol versus enzyme-level LDH inhibition", "DECREASE",
       "Glioblastoma papers (PMID 42035940, 2026; PMID 36278433, 2022) and a complex I paper (PMID 41570991, 2026), targeted passages read, all open access; NOT WWOX EVIDENCE", "sada_ldh_precedent_p2a_20261026.md sections 2.2 and 2.3", "DATO", "queried_not_full_read",
       {"disease_id": "glioblastoma and small-cell lung cancer cell lines, isolated mitochondria (not WWOX)", "genotype": "cancer cell lines", "species": "human and mouse", "cell_type": "tumour cell lines; heart and liver mitochondria", "developmental_stage": "not applicable"},
       "Cell viability and extracellular acidification fall at tens of micromolar, but LDH activity in lysate falls significantly only at the highest, hundreds-of-micromolar concentrations, and oxygen consumption and complex I NADH oxidation are inhibited directly and immediately; the complex I paper reports no inhibition of malate dehydrogenase. Cellular effects of stiripentol are therefore not attributable to LDH on the available data. In a mouse glioblastoma xenograft stiripentol prolonged survival (log-rank P 0.002; the dose is given differently in the Results and the Methods, which may describe different cohorts). Tumour models: no seizure, neurodevelopment or WWOX meaning."),
     d("DR-E02-007", "stiripentol exposure versus in vitro effective concentration (review-level)", "total plasma, estimated free tissue and liver exposure compared with concentrations that inhibit LDH in vitro", "UNKNOWN",
       "Bacq 2024, Adv Ther review (PMID 38443647, open access; targeted passages read); NOT WWOX EVIDENCE", "sada_ldh_precedent_p2a_20261026.md section 2.4", "INFERENZA", "queried_not_full_read",
       {"disease_id": "Dravet syndrome patients and rats (review of pharmacokinetics; not WWOX)", "genotype": "UNKNOWN", "species": "human and rat", "cell_type": "plasma and tissue", "developmental_stage": "children and adults"},
       "The review states that concentrations inhibiting LDH in vitro (tens to hundreds of micromolar) lie at or above total plasma levels at effective antiseizure doses and well above the estimated free tissue level, that brain to plasma ratio in the rat is near one, and that a liver to plasma ratio of about thirty-five was measured once in the rat; it ranks LDH inhibition last in sensitivity among stiripentol's mechanisms. Secondary statement of other people's measurements; not re-derived."),
     d("DR-E02-002", "human LDHA enzyme activity (cell-free)", "enzyme inhibition by GSK2837808A", "DECREASE",
       "ChEMBL activity rows of CHEMBL3335794; NOT WWOX EVIDENCE", "lucas_clarke_followup_20261026/chembl_named_activities.tsv", "DATO", "queried_not_full_read",
       {"disease_id": "enzyme assay, not a disease", "genotype": "recombinant human enzymes", "species": "human", "cell_type": "cell-free", "developmental_stage": "not applicable"},
       "Low-nanomolar potency on LDHA and about sixteen-fold selectivity over LDHB in the cited assays; a research tool with no CNS, paediatric or clinical datum."),
     d("DR-E02-003", "hepatic oxalate in primary hyperoxaluria", "LDHA lowering by an oligonucleotide (nedosiran)", "DECREASE",
       "Open Targets drugAndClinicalCandidates for ENSG00000134333 (approval stage); NOT WWOX EVIDENCE", "lucas_clarke_followup_20261026/opentargets_lists.tsv", "DATO", "queried_not_full_read",
       {"disease_id": "primary hyperoxaluria (not WWOX)", "genotype": "AGXT, GRHPR or HOGA1 variants", "species": "human", "cell_type": "hepatocyte-directed", "developmental_stage": "children and adults"},
       "Shows that lowering LDHA in humans is clinically tolerated in the liver; says nothing about brain exposure, and the route is liver-directed.")],
    p4_fields("A WWOX-linked lactate/LDH readout that a compound moves: LDH activity and the lactate-to-pyruvate relationship (enantiomer- or isotope-resolved) in WWOX-deficient versus isogenic human neural cells at matched maturity; then a locomotor, network or myelin endpoint.",
              "None for WWOX in humans. Fly: a single partial locomotor rescue by Ldh RNAi in the amyloid-plus-Wwox-reduction genotype. Human knockout organoid: LDHA transcript up but confounded with maturity.",
              "Fly amyloid model, whole-head metabolomics, partial RNAi; the human row is a transcript.",
              {"target_expression": "LDHA and LDHB are broadly expressed; LDHC is testis-restricted by convention and absent from the organoid expression universe.",
               "cells_tissue_stage": "whole fly head (glia carry the highest Wwox mRNA, so neuronal origin of lactate is not established); bulk organoid RNA.",
               "coverage": "UNKNOWN.",
               "limits": "Lactate rises only with Wwox reduction plus amyloid and falls nominally without amyloid; one human MRS datum reports lactate extremely low."}),
    {"identity": "LDH-directed levers: stiripentol (approved for a paediatric developmental epilepsy; weak LDH inhibition in vitro), GSK2837808A and other research LDHA inhibitors, and the LDHA-directed oligonucleotide nedosiran (approved for primary hyperoxaluria, liver-directed). Per-compound table: compounds_and_sources.md section 2.2.",
     "indication_and_transfer": "WWOX-DEE only IF lactate or LDH activity is shown to be a driver in a WWOX-deficient human neural system. The one fly precedent is amyloid-conditional; human lactate readouts in WWOX deficiency are normal or low in the cited sources (DL-BIO-008, DL-BIO-009).",
     "novelty_for_woree": "NON_TROVATO_NELLA_RICERCA as a test: no source retrieved links an LDH inhibitor to WWOX deficiency; coverage is the six sources of compounds_and_sources.md and ten PubMed abstracts on 2026-10-26. Update 2026-10-26 (scientist-b, P2a): the 2015 report usually cited for stiripentol and LDH in epilepsy (PMID 25792327) is now identified, is paywalled with no lawful full text found, and is known here only through its abstract and three open-access secondary descriptions; it is a stiripentol-LDH precedent in epilepsy models, not a WWOX datum.",
     "state_of_known_roads": "not in the earlier hand-made series; relates to map record N-06 (lactate as a readout) and HYP-20260709-01.",
     "pathway_and_objective": "BENEFICIO_PRECOCE; Track A, Track B untested.",
     "expected_contribution": "UNKNOWN. A partial locomotor benefit was seen once in the fly with Ldh RNAi; no human or WWOX datum.",
     "mechanism": "Target: LDHA (HGNC:6535, P00338) and LDHB (HGNC:6541, P07195); direction: lower LDH activity or lactate production; context: amyloid-stressed fly head in the paper; UNKNOWN in WWOX-DEE. For stiripentol the LDH link is not the established basis of its antiseizure use.",
     "sources": {"internal": ["PAPER 567", "CLAIM 025", "DL-BIO-008", "DL-BIO-009", "N-06", "HYP-20260709-01", "gse156243/prediction_isr_ldh_chain_20261026.md", "lucas_clarke_followup_20261026/biological_needs.md S2"],
                 "external_not_wwox_evidence": ["ChEMBL activity rows for stiripentol and GSK2837808A (document CHEMBL4311969 is Bai 2019)", "Open Targets: nedosiran as the only LDHA clinical candidate", "Rico-Molina 2024 enzyme paper (partial full-text read, staged receipt)", "Sada 2015 (abstract only; full text not acquired)", "glioblastoma 2022 and 2026 papers, a 2026 complex I paper and a 2024 mechanism review (targeted passages of open-access full texts)", "sada_ldh_precedent_p2a_20261026.md"]},
     "evidence_for_and_against": {
         "for": ["Ldh RNAi improved climbing in the amyloid-plus-Wwox-reduction fly genotype (once).", "Ldh transcript and lactate rise together in that genotype.", "Stiripentol is an approved paediatric epilepsy drug with an LDH link published in epilepsy models (2015 report; abstract-level here) and an LDH-directed analogue series exists; nedosiran shows LDHA lowering is tolerated in humans in the liver."],
         "against": ["The Ldh rescue lacks an Ldh-alone arm, a Wwox-mRNA check and a lactate readout, and the authors cite Ldh knockdown as detrimental in other fly amyloid models.", "Without amyloid lactate falls nominally and Ldh does not change.", "Stiripentol inhibits LDH only weakly in the single-concentration measurements held (none gives a fitted potency, and the one at the highest concentration is the lowest), and it has other targets, including direct inhibition of mitochondrial complex I, that act at lower concentrations; any benefit would not be attributable to LDH.", "LDHA in the organoid is as consistent with immaturity as with WWOX loss.", "Human lactate in WWOX deficiency is reported normal or extremely low."],
         "transfer_limits": "The fly effect needs amyloid; stiripentol's approved use depends on co-administration with another antiseizure drug and does not establish brain LDH engagement."},
     "time_to_access": "UNKNOWN for research use; stiripentol is marketed for another indication (label retrieved, openFDA 2026-04-27).",
     "time_to_benefit": "UNKNOWN.",
     "pharmacology": "Stiripentol: marketed formulation with a paediatric label for Dravet syndrome with clobazam; weak LDH inhibition in single-concentration enzyme measurements (no fitted potency; sizes differ between racemate, enantiomers and a database document), effective concentrations for LDH above total plasma levels and far above estimated free tissue levels in a review, other targets at lower concentrations; brain LDH engagement in vivo is asserted by secondary sources citing the 2015 report but not verified here. GSK2837808A: potent on LDHA in vitro, no in vivo or CNS datum retrieved. Nedosiran: liver-directed.",
     "paediatrics_and_interactions": "Stiripentol label: indicated for Dravet syndrome seizures in patients taking clobazam, from six months of age (openFDA label 2026-04-27); the same label means any use here would sit on top of clobazam co-therapy, an interaction this card does not assess. No paediatric suitability for WWOX-DEE is presumed.",
     "scope_of_checks": SCOPE,
     "question_history": ["mandate 2026-10-26 (Lucas-Clarke follow-up)", "prediction_isr_ldh_chain_20261026.md"],
     "predictions": "None; no engine, no score.",
     "next_measurement": "In the fly: lactate (enantiomer- or isotope-resolved) in the Ldh-RNAi double genotype, an Ldh-alone arm, and Wwox mRNA in the double line. In human neural cells: LDH activity and the lactate-to-pyruvate relationship in WWOX-deficient versus isogenic cells at matched maturity. Only then a compound arm: stiripentol against a selective LDHA tool at matched exposure, so that its other pharmacology is separable from LDH. The designed comparison (question, model, controls, endpoint, result that would change interpretation) is in sada_ldh_precedent_p2a_20261026.md section 6; it is a proposal, nothing is authorised to run.",
     "status": "hypothesis",
     "value_added": "Separates the LDH lever into measured (fly, conditional), asserted (the Ldh-to-lactate step) and unmeasured (any human WWOX system), and records that the approved paediatric candidate inhibits LDH only weakly in the retrieved measurements.",
     "clinical_census": CLIN,
     "_translation": {"pediatric_suitability": "Stiripentol paediatric label for another indication (Dravet, with clobazam); WWOX-DEE UNKNOWN.", "cns_exposure": "UNKNOWN for LDH engagement."}},
    ["Whether lactate or LDH activity is altered in WWOX-deficient human neural cells, independent of maturity.",
     "Whether stiripentol engages LDH in brain at tolerated exposures (the 2015 report is the claimed source and was not readable; its exposure and enzyme numbers are unknown here).",
     "What the real potency of stiripentol on LDH is: only single-concentration measurements exist and no fitted value.",
     "Which of stiripentol's effects on tumour-cell metabolism and respiration are LDH-mediated and which act through complex I.",
     "Whether Ldh lowering is beneficial or harmful without the amyloid context.",
     "Why lactate falls nominally with Wwox reduction without amyloid."],
    ["Ldh knockdown is detrimental in other fly amyloid models (the authors' own citation).", "Weak LDH inhibition by stiripentol in the retrieved measurements (a weak measure is not general inefficacy: assay, substrate level and enzyme source differ, and the 2015 report is unread).", "Direct inhibition of mitochondrial complex I by stiripentol, so a metabolic effect is not an LDH effect.", "Human lactate in WWOX deficiency reported normal or extremely low."],
    ["Fly and organoid rows do not share a context, so no directional comparison is formed between them; the one fly-internal comparison (Ldh RNAi against Wwox knockdown on climbing) is a genetic, not a pharmacological, comparison.",
     "The stiripentol enzyme rows (DR-E02-001, -004, -005) differ in enzyme source, substrate level and single concentration, so no direction is compared across them and no potency is derived."])
PACKETS["E02_ldh_inhibition"]["no_new_reading"] = ("E02 update 2026-10-26 (scientist-b, P2a): one open-access enzyme paper was read in part by receipt (PMID 39769031; receipt staged, id in CC-20261026-SCIENTIST-B-SADA-LDH-01), four more open-access papers were read at targeted passages without a receipt, and the 2015 Sada report could not be acquired lawfully (abstract only). The Lucas-Clarke rows keep scientist-a's reading (receipt " + RECEIPT + ").")

# ============================================================== E03 PDK / DCA
PACKETS["E03_pdk_inhibition_dca"] = base(
    "P4-E-03", "PDK inhibition (dichloroacetate and research PDK inhibitors) as the pyruvate-oxidation branch, kept separate from what the study measured",
    "E / Lucas-Clarke follow-up: pyruvate dehydrogenase kinase", "BENEFICIO_PRECOCE", "A",
    "A bypass of a postulated bottleneck: partial benefit at best, and only if the bottleneck exists. Not deep recovery. Track B: none.",
    [D_PDH_NONE, D_PDK_KO, D_LDHA_KO],
    [d("DR-E03-001", "PDK activity (family target; rat enzyme assay) and lactate oxidation in human fibroblasts", "pyruvate dehydrogenase kinase inhibition by dichloroacetate", "DECREASE",
       "ChEMBL curated mechanism and activity rows of CHEMBL306823; Open Targets (phase 3, congenital lactic acidosis); NOT WWOX EVIDENCE", "lucas_clarke_followup_20261026/chembl_mechanisms.tsv and chembl_named_activities.tsv", "DATO", "queried_not_full_read",
       {"disease_id": "enzyme assays and a congenital lactic acidosis indication (not WWOX)", "genotype": "UNKNOWN", "species": "rat enzyme and human fibroblast", "cell_type": "enzyme and fibroblast", "developmental_stage": "UNKNOWN"},
       "Curated PDK inhibitor. In the measurements retrieved the enzyme assay shows no half-maximal inhibition at the highest concentration tested and a fibroblast lactate-oxidation effect appears at a high micromolar concentration: weak in vitro. The repository's existing safety position (peripheral neuropathy, BLOCK-1) is unchanged by this card."),
     d("DR-E03-002", "human PDK2 enzyme activity", "PDK2 inhibition by AZD7545 or VER-246608", "DECREASE",
       "DGIdb (Drug Repurposing Hub, Guide to Pharmacology) and ChEMBL activity rows of CHEMBL3392645; NOT WWOX EVIDENCE", "lucas_clarke_followup_20261026/dgidb_interactions.tsv", "DATO", "queried_not_full_read",
       {"disease_id": "enzyme assay, not a disease", "genotype": "recombinant human enzymes", "species": "human", "cell_type": "cell-free", "developmental_stage": "not applicable"},
       "Research tool compounds; no CNS, paediatric or clinical datum retrieved. The symbol PDK1 in DGIdb returns PDPK1 agents (collision documented in target_resolution.tsv); only PDK2-4 rows and UniProt-keyed ChEMBL rows are used.")],
    p4_fields("A WWOX-linked PDH readout that a PDK inhibitor moves: PDH activity (or PDHA1 serine phosphorylation) and pyruvate fate (labelled glucose into acetyl-CoA, citrate, lactate) in WWOX-deficient versus isogenic human neural cells; only then a functional endpoint.",
              "None for WWOX at the activity level. The Lucas-Clarke study measured no pyruvate, PDH, PDK or flux. In the human knockout organoid PDK1 is DOWN, the PDK/PDH set is not different from chance and the LDH-to-PDH ratio is not shifted (transcripts).",
              "Fly study with no measurement in this branch; transcripts from one organoid deposit; compound statements are database rows.",
              {"target_expression": "PDK isoforms are expressed in brain; the WWOX-dependent level is UNKNOWN.",
               "cells_tissue_stage": "none measured in WWOX-deficient human neurons at the activity level.",
               "coverage": "UNKNOWN.",
               "limits": "The transcript negatives are exploratory and do not show PDH activity or lactate are normal; the HIF1A-to-PDK-to-PDH step is unmeasured in any WWOX-deficient human neural system."}),
    {"identity": "Dichloroacetate (PDK inhibitor, phase 3 per Open Targets for congenital lactic acidosis, no US label found) and research PDK inhibitors (AZD7545, VER-246608). Devimistat is NOT counted: DGIdb gives it no action type on PDK2-4.",
     "indication_and_transfer": "WWOX-DEE only IF a pyruvate-oxidation block exists in WWOX-deficient neural cells. Nothing in the Lucas-Clarke study tests that; the branch logic (a raised Ldh pulls pyruvate away from oxidation) is indirect by two steps.",
     "novelty_for_woree": "NOT NEW: HYP-20260709-05 and N-08 already hold this candidate (parked; dominated by the ketogenic hypothesis; peripheral-neuropathy flag).",
     "state_of_known_roads": "HYP-20260709-05, N-08, DL-MECH-020 (HIF1A to PDK to PDH chain).",
     "pathway_and_objective": "BENEFICIO_PRECOCE; Track A.",
     "expected_contribution": "UNKNOWN.",
     "mechanism": "Target: PDK1-4 (HGNC:8809-8812; UniProt Q15118, Q15119, Q15120, Q16654), NOT PDPK1 (HGNC:8816); direction: release PDH from inhibitory phosphorylation; context: no WWOX system.",
     "sources": {"internal": ["HYP-20260709-05", "HYP-20260709-01", "N-08", "DL-MECH-020", "PAPER 567", "gse156243/prediction_hif1a_pdk_chain_20261025.md", "gse156243/prediction_pyruvate_fate_20261026.md", "lucas_clarke_followup_20261026/biological_needs.md S3"],
                 "external_not_wwox_evidence": ["ChEMBL curated mechanism and activity rows for dichloroacetate", "DGIdb PDK2-4 rows", "Open Targets phase 3 candidate"]},
     "evidence_for_and_against": {
         "for": ["The Lucas-Clarke Ldh rise is the kind of change that could draw pyruvate away from oxidation (logic only)."],
         "against": ["The study measured nothing in this branch.", "PDK1 transcript is down and the PDK/PDH set is not different from chance in the human knockout organoid (exploratory transcripts).", "The sima:GFP reporter (the authors' HIF1alpha homologue) is unchanged in one genotype pair; the authors name Atf4 rather than sima as primarily responsible.", "Known neurotoxicity concern for the main compound; the ketogenic hypothesis dominates it on safety."],
         "transfer_limits": "No datum from any WWOX system at the activity or flux level."},
     "time_to_access": "UNKNOWN.",
     "time_to_benefit": "UNKNOWN.",
     "pharmacology": "Dichloroacetate: weak in the retrieved enzyme and cell assays; no label found; spontaneous-report counts exist but are not rates. Research PDK inhibitors: enzyme tools only.",
     "paediatrics_and_interactions": COMMON_Q,
     "scope_of_checks": SCOPE,
     "question_history": ["HYP-20260709-05", "mandate 2026-10-26 (Lucas-Clarke follow-up)"],
     "predictions": "None; no engine, no score.",
     "next_measurement": "The same discriminating assay as the ketogenic hypothesis, one step finer: PDH activity and labelled-glucose fate in WWOX-deficient versus isogenic human neural cells. If PDH activity and pyruvate fate are normal, HYP-20260709-05 stays parked with a stronger negative; if pyruvate oxidation is blocked, this card and the ketogenic hypothesis are both reopened.",
     "status": "deferred with reason",
     "value_added": "Keeps the pyruvate branch SEPARATE from what the paper measured and records that three exploratory transcript tests are negatives that do not show normal PDH or lactate.",
     "clinical_census": CLIN,
     "_translation": {}},
    ["Whether PDH activity or pyruvate oxidation is altered in any WWOX-deficient human neural system.",
     "Whether pyruvate was tested in the fly metabolomics (MTBLS12344 not publicly retrievable).",
     "Whether the Ldh rise diverts pyruvate from oxidation at all."],
    ["Three exploratory transcript tests in the one knockout organoid dataset are negative for the chain.", "The paper does not name dichloroacetate or any PDH/PDK element."],
    ["The fly row has direction UNKNOWN by design: the study did not measure this branch, so no comparison is formed."])

# ============================================================== E04 ketogenic / lactate axis
PACKETS["E04_ketogenic_lactate_axis"] = base(
    "P4-E-04", "Ketogenic and lactate-transport interventions (the ketogenic diet; MCT1 blockade as a direction control)",
    "E / Lucas-Clarke follow-up: ketogenic and lactate axis", "BENEFICIO_PRECOCE", "A",
    "Empirically used in developmental and epileptic encephalopathies for seizure control (partial benefit); a WWOX-specific rationale is unresolved. Not deep recovery. Track B: no allele-specific datum; the single null-genotype report is n = 1 and not a refutation for a protein-retaining allele.",
    [D_LAC_AB, D_LAC_NO, D_MRS, D_PDH_NONE], [],
    p4_fields("The existing minimal falsifier of HYP-20260709-01: Seahorse OCR/ECAR on donor-derived cells or the existing organoids; this card adds no new endpoint.",
              "The ketogenic diet in WWOX-DEE: tried in 3 patients in one cohort and continued in 1; a null-genotype report where it was suspended. The Lucas-Clarke study contains no diet, ketone, PDH or pyruvate arm.",
              "n of 3 and n of 1 clinical reports; fly lactate is amyloid-conditional.",
              {"target_expression": "UNKNOWN.", "cells_tissue_stage": "UNKNOWN.", "coverage": "UNKNOWN.",
               "limits": "No metabolic readout of the lever exists in a WWOX-deficient human neural system; the lactate rows have opposite signs in the fly (with and without amyloid) and in one human MRS report."}),
    {"identity": "Ketogenic diet (HYP-20260709-01, map record R-05) and, as a direction control only, MCT1 blockade (AZD3965 in DGIdb). No new compound.",
     "indication_and_transfer": "A decision for the treating clinical team, not for this system; this card only records the consequence of the Lucas-Clarke reading: no direct support and no refutation.",
     "novelty_for_woree": "NOT NEW: existing hypothesis, updated with a consequence note on 2026-10-26.",
     "state_of_known_roads": "HYP-20260709-01 (ranked, proposed-to-L9), R-05, DL-MECH-020, DL-BIO-008, DL-BIO-009.",
     "pathway_and_objective": "BENEFICIO_PRECOCE; Track A.",
     "expected_contribution": "UNKNOWN beyond the empirical seizure-control use.",
     "mechanism": "UNKNOWN for WWOX.",
     "sources": {"internal": ["HYP-20260709-01", "R-05", "N-06", "DL-MECH-020", "DL-BIO-008", "DL-BIO-009", "PAPER 567"], "external_not_wwox_evidence": ["DGIdb SLC16A1 rows: AZD3965 (inhibitor), valproic acid and sodium butyrate (no action type)"]},
     "evidence_for_and_against": {"for": [], "against": [], "transfer_limits": "The fly lactate result is conditional on amyloid and cannot be used for or against the Warburg direction in WWOX-null neurons."},
     "time_to_access": "UNKNOWN.", "time_to_benefit": "UNKNOWN.", "pharmacology": "UNKNOWN.",
     "paediatrics_and_interactions": COMMON_Q,
     "scope_of_checks": SCOPE,
     "question_history": ["HYP-20260709-01", "mandate 2026-10-26 (Lucas-Clarke follow-up)"],
     "predictions": "None; no engine, no score.",
     "next_measurement": "Seahorse OCR/ECAR on donor-derived WWOX-deficient cells (or the existing knockout organoids), as already specified in HYP-20260709-01.",
     "status": "abstention",
     "value_added": "Records that this paper changes nothing for the ketogenic hypothesis and names the one measurement that still decides it.",
     "clinical_census": CLIN,
     "_translation": {}},
    ["Whether a WWOX-deficient human neural cell has a measurable bioenergetic defect that a ketone substrate would bypass.",
     "Whether lactate is raised, normal or low in WWOX-deficient human brain across ages and contexts."],
    ["Four sources report normal human metabolism in WWOX deficiency (DL-BIO-009); one MRS report has lactate extremely low (DL-BIO-008)."],
    ["No drug assertion is supplied: the candidate is a diet."],
    abst={"kind": "ABSTENTION",
          "missing_datum": "A bioenergetic flux measurement (oxygen consumption and extracellular acidification) in WWOX-deficient versus isogenic human neural or donor-derived cells; never done in any WWOX human system (HYP-20260709-01, recalibration of 2026-09-21).",
          "search_record": "Lucas-Clarke 2026 read in full (receipt " + RECEIPT + "): no diet, ketone, PDH or pyruvate arm. Six database sources and ten PubMed abstracts on 2026-10-26 added no WWOX ketone datum. Reopening condition: a flux measurement in a WWOX human system, or the pyruvate rows of MTBLS12344 if released.",
          "adjacent_context_not_wwox_evidence": ["fly lactate rows: up with Wwox reduction plus amyloid, nominally down without amyloid"],
          "an_abstention_is_a_result": "The candidate stays where HYP-20260709-01 holds it; this card names what would end the abstention."})

# ---- scope and target census: the two things a derived card needs from a curated one (join P1, 2026-10-26)
# evidence_scope says what KIND of evidence an assertion is; it is not the reading depth, and a registered reading never implies
# WWOX-DEE applicability. A source that none of these rules recognises stays UNQUALIFIED (reported, never inferred).
def scope_of(row):
    src = row["source"]
    if src.startswith("PAPER 567"):
        return "WWOX_BIOLOGY_OTHER_CONTEXT"      # neuronal Wwox RNAi in a fly amyloid model: WWOX biology, not WWOX-DEE
    if src.startswith("GSE156243"):
        return "COMPUTATIONAL_RESULT"            # our own set-level reanalysis of a WWOX knockout organoid deposit
    if src.startswith(("ChEMBL", "DGIdb", "Open Targets")):
        return "EXTERNAL_DATABASE_RECORD"
    if "NOT WWOX EVIDENCE" in src and "PMID" in src:
        return "OTHER_DISEASE_PRECEDENT"         # a trial or model in another disease, read at abstract level
    return "UNQUALIFIED"


# Symbols whose target -> compounds census (this folder's *.tsv) belongs to the card; HGNC symbols, as in target_resolution.tsv
CENSUS = {"E01_isr_modulators": ["EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5", "EIF2AK1", "EIF2AK2", "EIF2AK3", "EIF2AK4",
                                 "EIF2S1", "ATF4", "PPP1R15A", "PPP1R15B"],
          "E02_ldh_inhibition": ["LDHA", "LDHB", "LDHC"],
          "E03_pdk_inhibition_dca": ["PDK1", "PDK2", "PDK3", "PDK4", "PDPK1", "PDHA1"],
          "E04_ketogenic_lactate_axis": ["SLC16A1"]}
for name, packet in PACKETS.items():
    for row in packet.get("disease_assertions", []) + packet["drug_assertions"]:
        row["evidence_scope"] = scope_of(row)
    packet["target_census"] = {"dir": str(HERE.relative_to(ROOT)), "symbols": CENSUS[name]}

for name, packet in PACKETS.items():
    # the bridge forbids both singular and plural; plural is used so every contrast keeps its own row
    card = bridge.build_card(packet)
    (CARDS / f"{name}.packet.json").write_text(json.dumps(packet, indent=1, ensure_ascii=False, sort_keys=False) + "\n", encoding="utf-8")
    (CARDS / f"{name}.card.json").write_text(json.dumps(card, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(name, card["directional_summary"], [c["status"] for c in card["comparisons"]])
