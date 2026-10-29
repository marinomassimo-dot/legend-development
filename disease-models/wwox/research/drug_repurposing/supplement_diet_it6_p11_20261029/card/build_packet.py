#!/usr/bin/env python3
"""Writes P11_magnesium_nmdar_gate.packet.json (IT6-P11, scientist-b). The packet is data; this script exists so the
text is reviewable as code. Build the card with:
  python3 framework/scripts/repurposing_bridge.py <packet> > <card>
No dose, concentration, route, schedule or paediatric suitability appears here (check_cards.py forbids the tokens)."""
import sys as _sys
if len(_sys.argv) > 1 and _sys.argv[1] in ('-h', '--help'):
    print(__doc__)
    raise SystemExit(0)

import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MAN = "disease-models/wwox/research/deepdive_manifests/PMID34634460.json"
REC = "FTR-20260810-34634460-02"  # the receipt the manifest itself names
SLICE = {
    "disease_id": "Wwox-null neuron-specific knockout mouse neocortex (ex vivo slice)",
    "genotype": "Synapsin-Cre Wwox knockout versus wild type and heterozygote",
    "species": "mouse",
    "cell_type": "layer II/III neocortex, local field potential and pyramidal-cell patch",
    "developmental_stage": "juvenile, about two weeks of age (as printed; not re-derived here)",
}
UNKNOWN_CTX = lambda d, s, c, g: {"disease_id": d, "genotype": g, "species": s, "cell_type": c, "developmental_stage": "UNKNOWN"}


def da(i, target, endpoint, direction, locator, note, entry_receipt=True):
    return {"id": i, "target_id": target, "endpoint": endpoint, "direction": direction,
            "source": "PAPER 031 (Breton 2021, neuron-specific Wwox knockout mouse slices)", "locator": locator,
            "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "context": SLICE,
            "measured_result_note": note, "evidence_scope": "WWOX_EXPERIMENT_IN_DEE_SYSTEM", "receipt": REC}


disease = [
    da("DA-P11-001", "neocortical spontaneous bursting (local field potential)", "fraction of slices with bursts", "INCREASE",
       MAN + " verbatim_locators.entries[0]",
       "Wild type 0 of 11 slices, heterozygote 4 of 23, knockout 36 of 42, all in an ACSF that contains magnesium (manifest entries[21]; the recording perfusate is not stated separately from the incubation ACSF, so that the bath was the same is an inference carried by the manifest, not a sentence of the paper)."),
    da("DA-P11-002", "layer II/III pyramidal neuron resting membrane potential", "resting membrane potential (mV)", "INCREASE",
       MAN + " verbatim_locators.entries[14]",
       "Table 1: wild type -79.25, heterozygote -75.51, knockout -73.62 mV; the text states the knockout pyramidal neurons were depolarised against wild type. The Discussion adds that the in vitro preparation holds neurons more hyperpolarised than in vivo. Cell numbers 13, 15 and 40 neurons from 5, 6 and 15 animals."),
    da("DA-P11-003", "layer II/III pyramidal neuron spontaneous inhibitory current", "sIPSC amplitude", "DECREASE",
       MAN + " verbatim_locators.entries[7]",
       "Control 57.3 +/- 31.0 pA against knockout 27.5 +/- 19.4 pA, pooled events; spontaneous excitatory amplitude differs by about six per cent (entries[6]). Reduced inhibition is the larger synaptic change in this paper."),
]

drug = [
    {"id": "DR-P11-001", "target_id": "NMDAR (tool compound d-APV, competitive, full block)", "endpoint": "fraction of slices with bursts / burst frequency",
     "direction": "DECREASE", "source": "PAPER 031 (Breton 2021, neuron-specific Wwox knockout mouse slices)",
     "locator": MAN + " verbatim_locators.entries[2]; Results 2.2, the sentence that begins Blocking glutamatergic neurotransmission with d-APV and ends eliminated the spontaneous bursting events",
     "epistemic_status": "DATO", "reading_depth": "complete_fulltext_read", "context": SLICE,
     "measured_result_note": "Burst frequency fell to zero and returned on washout; five slices from three animals. The paper's own inference is that NMDAR-mediated transmission is 'a requirement' for the bursts: permissive dependence is not distinguished from raised NMDAR function.",
     "evidence_scope": "WWOX_EXPERIMENT_IN_DEE_SYSTEM", "receipt": REC},
    {"id": "DR-P11-002", "target_id": "extracellular Mg2+ (the physiological voltage-dependent NMDAR pore blocker)", "endpoint": "NMDA-evoked whole-cell current",
     "direction": "DECREASE", "source": "Basic pharmacology, J Physiol 2014 (PMID 24614743, PMC open access); NOT WWOX EVIDENCE and not cortex",
     "locator": "PMC4027860 abstract and Results; local copy sha256 1ecd1c7d8cdc744a7354557fbf71b218ef330da9eae77636e54a5c9c78dce28b; quotation L12 of supplement_diet_it6_p11_20261029/locators.tsv",
     "epistemic_status": "DATO", "reading_depth": "queried_not_full_read",
     "context": UNKNOWN_CTX("none (non-disease physiology)", "rat", "substantia nigra pars compacta dopaminergic neurone, whole cell", "wild type"),
     "measured_result_note": "The block grows steeply with hyperpolarisation: the half-inhibitory external Mg2+ concentration is about threefold smaller at -70 than at -50 mV, and about 2.5-fold smaller at -90 than at -70 mV. Mixed GluN2B/GluN2D population at postnatal day 7: not the juvenile cortical population. A staged selected-passage receipt exists (see README).",
     "evidence_scope": "UNQUALIFIED"},
    {"id": "DR-P11-003", "target_id": "intravenous magnesium sulfate added to ACTH versus ACTH alone", "endpoint": "proportion seizure-free at 12 weeks (infantile spasms)",
     "direction": "INCREASE", "source": "Zou 2010 Clin Ther (PMID 20435238), ABSTRACT ONLY; NOT WWOX EVIDENCE",
     "locator": "PubMed/Europe PMC abstract retrieved 2026-10-29; no full text read; no receipt",
     "epistemic_status": "DATO", "reading_depth": "abstract_only",
     "context": UNKNOWN_CTX("infantile spasms (cause mixed; not WWOX)", "human", "infants, median age about nine months", "UNKNOWN"),
     "measured_result_note": "Randomised, open label, 19 infants per arm, China; seizure-free 14 of 19 versus 9 of 19 at 12 weeks and 12 of 19 versus 10 of 19 at 24 weeks; the abstract's conclusion calls the proportions seizure-free from week 4 to week 24 significantly greater with the combination. Abstract only: the exact tests, blinding and design details were not read.",
     "evidence_scope": "OTHER_DISEASE_PRECEDENT"},
    {"id": "DR-P11-004", "target_id": "magnesium sulfate by injection for three days then an oral magnesium preparation for three months, on top of ACTH and antiseizure drugs", "endpoint": "seizure control (clinical response) at 3 months (West syndrome)",
     "direction": "NO_CHANGE", "source": "Yadav 2022 Iran J Child Neurol (PMID 35222658, PMC open access); NOT WWOX EVIDENCE",
     "locator": "PMC8752995 Results; locators.tsv L17 to L22; staged receipt dated 20261029 for this paper (see README)",
     "epistemic_status": "DATO", "reading_depth": "partial_fulltext_read",
     "context": UNKNOWN_CTX("West syndrome (mostly symptomatic, perinatal hypoxic-ischaemic injury commonest; not WWOX)", "human", "children 3 months to 5 years", "UNKNOWN"),
     "measured_result_note": "Open-label randomised, 52 recruited and 48 analysed per protocol, comparator syrup held calcium and vitamin D without magnesium, no blinding. Seizure control p 0.69 and development p 0.09 (no difference); EEG improvement p 0.04 in the Results and p 0.003 in the Discussion (internal inconsistency). No post-treatment serum magnesium is reported in the text read although the Discussion says supplementation raised it.",
     "evidence_scope": "OTHER_DISEASE_PRECEDENT"},
    {"id": "DR-P11-005", "target_id": "intravenous magnesium sulfate with ACTH after first-line failure (single arm)", "endpoint": "seizure-free state at the end of a two-week course (infantile spasms)",
     "direction": "UNKNOWN", "source": "Wang 2023 Pediatr Investig (PMID 36967744, PMC open access); NOT WWOX EVIDENCE",
     "locator": "PMC10030695 Results and Discussion; locators.tsv L23 to L26; staged receipt dated 20261029 (see README)",
     "epistemic_status": "DATO", "reading_depth": "partial_fulltext_read",
     "context": UNKNOWN_CTX("infantile spasms after first-line failure (not WWOX)", "human", "infants and young children 2 to 24 months", "UNKNOWN"),
     "measured_result_note": "Retrospective, 229 enrolled, no control group (the authors say so); 48.5 per cent seizure-free and 72.1 per cent resolution of hypsarrhythmia; 21.4 per cent had adverse events. Direction is UNKNOWN because there is no comparator in the study.",
     "evidence_scope": "OTHER_DISEASE_PRECEDENT"},
    {"id": "DR-P11-006", "target_id": "oral magnesium sulfate versus oral magnesium L-threonate in drinking water", "endpoint": "cerebrospinal-fluid magnesium",
     "direction": "NO_CHANGE", "source": "Hou 2019 Neuropsychiatr Dis Treat (PMID 31806980, PMC open access); NOT WWOX EVIDENCE",
     "locator": "PMC6857673 Results, normal-mouse arm; locators.tsv L13 to L16; staged selected-passage receipt dated 20261029 (see README)",
     "epistemic_status": "DATO", "reading_depth": "queried_not_full_read",
     "context": UNKNOWN_CTX("none (healthy mice; the paper's disease arm is an MPTP model)", "mouse", "cerebrospinal fluid and serum", "wild type"),
     "measured_result_note": "Oral magnesium sulfate: serum magnesium rose, cerebrospinal-fluid magnesium did not change. Magnesium L-threonate: cerebrospinal-fluid magnesium rose by about 30 per cent from the Results values (the Discussion prints 21.6 per cent, an unexplained difference). Six mice per subgroup in the sampling design. Mouse; no human cerebrospinal-fluid value for oral magnesium was found.",
     "evidence_scope": "UNQUALIFIED"},
]

not_known = [
    "Whether NMDAR current, subunit composition or the strength of the magnesium block differs in any WWOX system.",
    "Whether raising bath Mg2+ in the knockout slice lowers burst frequency, and over what range (a titration was never done).",
    "Whether the recording perfusate of the source equals the incubation ACSF stated in its Methods.",
    "Whether any oral or parenteral magnesium preparation raises brain extracellular free Mg2+ in a child, and by how much.",
    "Whether serum or cerebrospinal-fluid magnesium differs in WWOX-DEE (no measurement was found).",
    "Whether sustained NMDAR dampening by a higher Mg2+ tone affects activity-dependent myelination or synaptic maturation in a developing Wwox-deficient brain.",
]
against = [
    "Dependence of bursting on NMDAR is permissive as far as measured: the paper says 'a requirement', no NMDAR current or magnesium sensitivity was measured, and the slice already bursts in a medium that contains magnesium.",
    "The magnesium arithmetic (README) gives a modest effect for a modest rise: a full competitive block removes the burst, a graded rise in an ion that is already present removes only part of the residual conductance; whether the burst is threshold-like enough to follow is unknown.",
    "In the one mouse study read, an oral magnesium salt raised serum magnesium and left cerebrospinal-fluid magnesium unchanged; only the threonate raised it, by about a third, in healthy mice, six per subgroup.",
    "The only controlled infant data for oral magnesium (open label, 48 analysed) found no difference in seizure control; the positive randomised signal (38 infants, abstract only) used intravenous magnesium sulfate with ACTH, which is a prescription route and not a supplement.",
    "Mechanism is not established in the infant trials: they do not show that NMDAR block explains any effect.",
    "One WOREE case received vitamin B6 and zonisamide without relief (abstract-level, n of 1): nothing in the WWOX record says a mineral or vitamin deficiency exists to be repleted.",
]

packet = {
    "schema_version": 1,
    "axis": "P / IT6 supplement and diet: the physiological NMDAR gate (extracellular magnesium)",
    "route": "BENEFICIO_PRECOCE",
    "mission_dimensions": {
        "track": "A",
        "track_definition": "mission.md section 5: Track A = variant-independent WWOX loss of function; Track B = variant or allele-class specific (e.g. the Q230P missense class); Track C = repurposing, which is a method of reaching A or B, not a third lesion class",
        "route": "BENEFICIO_PRECOCE",
        "route_definition": "RECUPERO_PROFONDO = deep recovery of the lost function; BENEFICIO_PRECOCE = concrete partial benefit, symptomatic control or protection of function, with paediatric feasibility and time in view",
        "route_note": "Partial benefit at best: a network-state lever on one measured phenotype in a neuron-specific knockout, allele-blind (Track A); Track B unmeasured. Burst control is not developmental recovery (N-15). No supplement is a restoration of WWOX function.",
        "the_two_dimensions_are_independent": "a card keeps both: a variant-independent lever can be a partial-benefit lever, and a lesion-specific one can aim at deep recovery",
    },
    "candidate": {"id": "IT6-P11-MG", "name": "Extracellular magnesium as the physiological voltage-dependent NMDAR gate: a nutrient/supplement lever on the d-APV-sensitive bursting node"},
    "disease_assertions": disease,
    "drug_assertions": drug,
    "p4_fields": {
        "endpoint_pursued": "In Wwox-deficient neocortical slices at matched maturity, with wild-type and heterozygous slices as comparators: spontaneous burst incidence, frequency, duration and amplitude over a graded range of bath Mg2+ that brackets the slice's own value, then the NMDAR-selective block (d-APV) as the ceiling, then an NMDA:AMPA ratio under voltage control. Separately: serum and cerebrospinal-fluid total and ionised magnesium in the knockout and control mice, and the cerebrospinal-fluid response to an oral preparation in the same animals. A developmental endpoint (myelin, synaptic maturation) before any chronic exposure is considered.",
        "functional_evidence_available": "d-APV abolishes bursting in the knockout slice and suppresses a knockout-specific delayed response; knockout pyramidal neurons rest about five and a half millivolts more depolarised and receive about half the inhibitory current amplitude. No magnesium manipulation, magnesium measurement or NMDAR current exists for any WWOX system.",
        "temporal_or_model_limit": "Juvenile mouse slices from one laboratory; a Synapsin-Cre null, not a missense or splice allele; the preparation sits more hyperpolarised than in vivo by the authors' own account; acute pharmacology.",
        "cellular_context": {
            "target_expression": "UNKNOWN.",
            "cells_tissue_stage": "layer II/III pyramidal neurons for the slice and patch rows; no subunit-resolved data.",
            "coverage": "UNKNOWN.",
            "limits": "No receptor-level measurement of NMDAR current, subunit composition or magnesium sensitivity exists for any WWOX system. The only magnesium IC50 values read are from non-cortical rat neurones.",
        },
    },
    "p4_card": {
        "identity": "Magnesium, as the divalent cation (ChEMBL element record in the catalogue), delivered by any preparation; the preparation matters for brain exposure and is not settled: one mouse study read separates magnesium sulfate (no cerebrospinal-fluid change) from the threonate (a rise). Not a diet and not a single-molecule reduction of one; no dose appears.",
        "indication_and_transfer": "Only IF the knockout's NMDAR dependence reflects a loss of voltage-dependent magnesium block (a depolarised resting potential plus reduced inhibition) that a modest rise in extracellular Mg2+ can offset, AND a preparation can raise brain extracellular Mg2+ by that amount in a child. Both conditions are untested. The decision for any individual belongs to the treating clinical team; this card gives no recommendation.",
        "novelty_for_woree": "NOT NEW as a clinical idea (magnesium sulfate with ACTH has been tried in infantile spasms outside WWOX); NEW here as a WWOX-specific mechanism link: the knockout's resting-potential gradient and its d-APV sensitivity make the voltage-dependent magnesium gate the physiological handle on the node of card F01, which that card treats only through pore blockers. PubMed titles/abstracts: zero WWOX and magnesium hits on 2026-10-29 (queries in README); Europe PMC full text 74 hits, five inspected by title, none about magnesium in WWOX. NON_TROVATO_NELLA_RICERCA, not MAI_TENTATO.",
        "state_of_known_roads": "F01 (memantine and perampanel on the glutamate-receptor node), need NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR, map R-02, Chain B, N-15, DL-MECH-002, and the E04/I01 metabolic roads this card does not touch.",
        "pathway_and_objective": "BENEFICIO_PRECOCE; Track A; Track B untested.",
        "expected_contribution": "UNKNOWN. At best a reduction of a network state; no developmental benefit is implied.",
        "mechanism": "Extracellular Mg2+ blocks the NMDAR pore in a voltage-dependent way, so a more depolarised resting potential and weaker inhibition relieve the block and raise NMDAR gain. Direction wanted: lower NMDAR gain by restoring block, which is the physiological route to the same node d-APV closes completely. Context: juvenile neocortical slice, neuron-specific knockout. INFERENZA throughout: nothing here measures a magnesium effect in a WWOX system.",
        "sources": {
            "internal": ["PAPER 031", "CLAIM 021", "NEED-EXCITATORY-GAIN-GLUTAMATE-RECEPTOR", "F01_glutamate_receptor_node", "DL-MECH-002", "R-02", "Chain B", "N-15", "disease-models/wwox/research/drug_repurposing/supplement_diet_it6_p11_20261029/README.md"],
            "external_not_wwox_evidence": [
                "J Physiol 2014 (PMID 24614743), PMC open access, selected passages",
                "Hou 2019 (PMID 31806980), PMC open access, selected passages",
                "Yadav 2022 (PMID 35222658), PMC open access, text read",
                "Wang 2023 (PMID 36967744), PMC open access, text read",
                "Zou 2010 (PMID 20435238), abstract only",
                "Slutsky 2010 (PMID 20152124), abstract only",
                "Epilepsy Res 2012 hypothesis article (PMID 22406257), abstract only",
                "Catalogue entries CAT:CHEMBL1201230 and CAT:CHEMBL3989857; DSLD and EU register probes of 2026-10-29",
            ],
        },
        "evidence_for_and_against": {
            "for": [
                "d-APV abolishes bursting in the knockout slice and suppresses the knockout-specific delayed response (NMDAR dependence).",
                "Knockout pyramidal neurons rest more depolarised and heterozygotes sit between wild type and knockout, in step with the burst incidence gradient.",
                "Spontaneous inhibitory current amplitude is roughly halved, so activity-dependent depolarisation is less opposed.",
                "Magnesium sulfate with ACTH outperformed ACTH alone in a small randomised open-label infantile-spasms trial (abstract only), and a larger retrospective series reports seizure freedom after first-line failure (no control).",
            ],
            "against": against,
            "transfer_limits": "A juvenile mouse slice does not transfer to a child; the infant trials are other aetiologies, open label, and either intravenous or low-exposure oral; brain extracellular Mg2+ is not the serum value and is regulated.",
        },
        "time_to_access": "UNKNOWN for research use; magnesium preparations are widely marketed as supplements in the US (catalogue, DSLD name probes) and the threonate has an EU novel-food entry whose conditions of use were not read. Italian status NOT checked (register behind a bot challenge; not bypassed).",
        "time_to_benefit": "UNKNOWN.",
        "pharmacology": "Ion, not a ligand: ChEMBL curates mechanism 'Unknown' for the sulfate and the catalogue's target-to-compound route by GRIN symbols returns no magnesium entry (74 and 94 entries for GRIN1 and GRIN2B, none magnesium), so this lever would never have surfaced from target queries. Brain exposure after oral intake is regulated and preparation-dependent in the mouse data read; human data not found.",
        "paediatrics_and_interactions": "UNKNOWN. No paediatric suitability is presumed. Adverse events reported in the infant series (infections, low potassium, diarrhoea) belong to the combination with ACTH and the intravenous route. Interactions and labelled warnings were NOT assessed.",
        "scope_of_checks": {
            "support_and_replication": "One laboratory for every WWOX row; no replication. The magnesium arithmetic uses an IC50 from another cell type and is not a measurement.",
            "formal_checks": "WWOX rows carry verbatim locators in the manifest (the receipt that manifest names). All other quotations in the README are checked by quote_check.py against the article text layer. Two selected-passage and two section-complete readings were prepared as staged receipts dated 20261029 for the integrator.",
            "card_inferences_owed_audit": "Every statement marked INFERENZA, the arithmetic, and every card-level synthesis, is owed a blind audit by someone other than the producer.",
        },
        "question_history": ["map R-02 and Chain B", "F01 (2026-10-27)", "IT6 package P11 (2026-10-29): which supplement meets a WWOX-relevant need on biological grounds"],
        "predictions": "Registered before any experiment: (a) if the knockout bursts because the depolarised resting potential relieves the magnesium block, a graded rise in bath Mg2+ lowers burst incidence or frequency in knockout slices at a rise no larger than what the most brain-penetrant preparation produced in mouse cerebrospinal fluid (about a third), and slices of the other genotypes are unaffected; (b) if bursts recruit magnesium-insensitive receptor populations or AMPAR-driven recruitment, only a rise far beyond any reachable exposure helps, d-APV stays the ceiling, and the nutrient lever closes; (c) lowering bath Mg2+ increases burst incidence in the heterozygote and wild-type slices more than in the knockout (a ceiling effect). Result (b) closes the strand.",
        "next_measurement": "Wet-lab, not done: Wwox knockout, heterozygote and wild-type neocortical slices at P13 to P17 in the source's own medium; graded bath Mg2+ around the slice value, in both directions, then d-APV; endpoints burst incidence, frequency, duration, amplitude; NMDA:AMPA ratio under voltage control; discriminating result: a rise within the reachable range that lowers bursts in knockout slices without altering wild-type activity versus one that does not. In parallel, total and ionised Mg in serum and cerebrospinal fluid of knockout versus control mice, and the cerebrospinal-fluid response to one oral preparation.",
        "status": "hypothesis",
        "value_added": "Names the physiological regulator of the NMDAR node, shows from the source's own Methods that the bursting slice is not a magnesium-free artefact, and turns the sign question into one cheap ex vivo titration plus one exposure measurement, before any supplement is considered.",
        "clinical_census": "Clinical census, ClinicalTrials.gov API v2, 2026-10-20 (drug_repurposing/clinical_census_20261020.md): seven queries returned no registered WOREE interventional study; it answers seven queries against one registry on one date and a missing hit does not prove that no study exists. Not re-run for this card.",
    },
    "not_known": not_known,
    "evidence_against": against,
    "bridge_gaps_exposed": [
        "Magnesium is an ion, not a ligand: the bridge's drug-target sign comparison has no target row to compare for it, and the catalogue target query by GRIN symbols returns no magnesium record.",
        "The infant trial rows are another aetiology and a prescription route; no sign comparison is formed with the slice rows.",
    ],
    "translation": {
        "pediatric_suitability": "UNKNOWN",
        "cns_exposure": "Mouse only: oral sulfate no change in cerebrospinal fluid, threonate a rise of about a third; human UNKNOWN.",
        "interactions": "UNKNOWN",
        "access": "UNKNOWN for Italy; US supplement labels exist by name (DSLD probe); EU novel-food entry for the threonate, conditions of use not read.",
        "time_to_benefit": "UNKNOWN",
        "functional_rescue": "UNKNOWN",
    },
    "p4_roadmap_fields": {
        "indication_and_transfer": "Only IF the knockout's NMDAR dependence reflects a loss of voltage-dependent magnesium block that a modest rise in extracellular Mg2+ can offset, AND a preparation can raise brain extracellular Mg2+ by that amount in a child. Both conditions are untested. The decision for any individual belongs to the treating clinical team; this card gives no recommendation.",
        "verification_scope": json.dumps({
            "support_and_replication": "One laboratory for every WWOX row; no replication. The arithmetic uses an IC50 from another cell type.",
            "formal_checks": "WWOX rows have verbatim locators in the manifest; the other quotations are checked by quote_check.py against the article text layer; staged receipts dated 20261029 were prepared for the integrator.",
            "card_inferences_owed_audit": "Every statement marked INFERENZA and every card-level synthesis is owed a blind audit by someone other than the producer.",
        }),
    },
    "label_lookup": {"status": "NOT_ATTEMPTED"},
    "card_conventions": [
        "IPOTESI throughout; the bridge forces it. No score, rank, probability or blended index is carried.",
        "directional_summary compares signs only where target, endpoint and every context dimension match; UNRESOLVED is a statement about the record, not about the biology.",
        "Abstract-level statements from PubMed are labelled abstract_only; none carries a receipt.",
        "label_lookup is NOT_ATTEMPTED in the bridge: the bridge has no network. The catalogue, DSLD and EU probes are recorded in the package README.",
        "No dose, route, schedule or paediatric suitability appears; assay and bath concentrations of the sources are deliberately not reproduced here and are in the package README with their locators.",
    ],
    "target_census": {"dir": "disease-models/wwox/research/drug_repurposing/supplement_diet_it6_p11_20261029", "symbols": []},
    "no_new_reading": "P11 (scientist-b, 2026-10-29): five staged receipts dated 20261029 (one selected-passage re-read of PMID 34634460, two section-complete readings of open-access infant trials, two selected-passage readings); see the package README.",
}
(HERE / "P11_magnesium_nmdar_gate.packet.json").write_text(json.dumps(packet, indent=1, ensure_ascii=False) + "\n", encoding="utf8")
print("wrote packet")
