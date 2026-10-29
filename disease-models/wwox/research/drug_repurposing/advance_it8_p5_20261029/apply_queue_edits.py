#!/usr/bin/env python3
"""IT8 P5: apply the queue edits justified by loop 1 and loop 2 (needs, card packets, work order).
Idempotent: each edit is skipped when already present. Run from the repository root. Card JSON is rebuilt afterwards with
framework/scripts/repurposing_bridge.py (see README section 8)."""
import json, pathlib, sys
DR = pathlib.Path("disease-models/wwox/research/drug_repurposing")
L1 = "disease-models/wwox/research/drug_repurposing/advance_it8_p5_20261029/loop1_partial_benefit/README.md"
L2 = "disease-models/wwox/research/drug_repurposing/advance_it8_p5_20261029/loop2_broad_recovery/README.md"

def rw(path, fn, indent):
    p = DR / path
    d = json.loads(p.read_text(encoding="utf-8"))
    fn(d)
    p.write_text(json.dumps(d, indent=indent, ensure_ascii=False) + "\n", encoding="utf-8")

def obs(i, pmid, statement, model, species, genotype, tissue, age, comparison, readout, level, direction, limits, doc, anchor):
    return {"id": i, "pmid": pmid, "statement": statement, "model_type": model, "species": species, "genotype": genotype,
            "tissue_or_cells": tissue, "age_stage": age, "comparison": comparison, "readout": readout, "readout_level": level,
            "direction_observed": direction, "evidence_scope": "OTHER_DISEASE_PRECEDENT", "limits": limits,
            "locators": [{"kind": "document", "path": doc, "anchor": anchor}], "locator_status": "DOCUMENT"}

def needs(d):
    for n in d["needs"]:
        if n["id"] == "NEED-ISR-ATTENUATION":
            if any(o["id"] == "O9" for o in n["observed"]): continue
            n["observed"] += [
                obs("O9", "37804316",
                    "AFG3L2 loss (spastic ataxia type 5, whose clinical spectrum includes myoclonic epilepsy): ISR is postnatal and progressive in mouse cerebellum (P-eIF2a and Atf4 equal at P1, raised at P14); HRI or DELE1 silencing lowers P-eIF2a and slows growth of patient fibroblasts; Sephin-1 improves cell number, Purkinje neuron number, cristae class and pyruvate-stimulated ATP and extends survival by about 10 days (dam gavage from E14, daily from day 1). GCN2 and PERK untested; HRI not tested in vivo; P-eIF2a not reported in treated mice; wild-type mitochondria and ATP also change under Sephin-1.",
                    "other_animal_model", "mouse and human", "Afg3l2 null mouse; biallelic AFG3L2 patient fibroblasts (not WWOX)", "cerebellum; skin fibroblasts; primary Purkinje cultures", "P1 and P14 pups; prenatal-start treatment", "Afg3l2-/- against +/+; patient against control; treated against vehicle",
                    "P-eIF2a, ATF4 and targets, growth, Purkinje morphology, cristae, ATP, survival", "functional", "ISR raised and its potentiation beneficial in this lesion (sign opposite to the PARS2 fly of O6)",
                    "Not WWOX evidence; one laboratory; small n (3 mice for histology, about 5 treated for survival); the drug target is disputed (PMID 28447936, abstract level); the kinase is shown by siRNA in fibroblasts only; early-window treatment of a lesion present from embryogenesis; read in full 2026-10-29 (receipt FTR-20261029-37804316-01, partial).",
                    L1, "section 1 Brain 2024"),
                obs("O10", "41706892",
                    "Normal mouse hippocampus: group I mGluR activation (DHPG, 5 min) raises ATF4 protein about 2.5-fold and P-eIF2a about 2.3-fold with no change in Atf4 mRNA (n 3 slices per group; ATF4 P 0.047, mRNA P 0.75); excitatory-neuron ATF4 deletion impairs mGluR-LTD and object-place learning and prevents the DHPG-induced fall of OXPHOS proteins.",
                    "other_animal_model", "mouse", "wild type and excitatory-neuron Atf4 knock-out (not WWOX, not a disease)", "hippocampal slices and cultured neurons", "adult slices P30-60; E17.5 neurons at DIV8", "DHPG against vehicle; knock-out against control",
                    "ATF4 protein, P-eIF2a, Atf4 mRNA, LTD, proteome", "protein", "ATF4 protein up without mRNA change on neuronal activity (P-eIF2a also up)",
                    "Not WWOX evidence and not a stress or disease model; minutes to one hour; n 3 to 4; the eIF2 kinase is not identified; canonical ISR targets were not measured after DHPG; figure images not opened (receipt FTR-20261029-41706892-01, partial).",
                    L1, "section 1 PNAS 2026"),
            ]
            n["inferred"] += [
                "That the sign of an ISR can be carried from a mitochondrial lesion to WWOX: two DEE-type mitochondrial precedents have opposite signs (protective in the AFG3L2 model, O9; harmful in the PARS2 fly, O6), so neither fixes a prior; the attenuation arm of this need is one of two arms.",
                "That ATF4 protein or P-eIF2a raised in a WWOX-deficient neural system would be proteostatic stress: group I mGluR activation raises both within minutes without an Atf4 mRNA change (O10) and every WWOX system that measured it is hyperexcitable (context matrix Q14), so an activity-silencing arm is required before the rise is read as stress.",
                "That a protective HRI arm is demonstrated even in the AFG3L2 precedent: HRI and DELE1 enter through siRNA in fibroblasts only; GCN2 and PERK were not tested; Sephin-1 benefit in vivo is not linked to the ISR by a genetic test and its GADD34 target is disputed (PMID 28447936).",
            ]
            n["counter_evidence"] += [
                "In the AFG3L2 precedent the ISR is reported as protective and its potentiation as beneficial (O9), the opposite of the premise of attenuation; the premise of this need (a harmful over-activation) rests on one fly paper whose Atf4 rise needs amyloid and on the PARS2 fly.",
            ]
            src = n["sources"]
            src["documents"].append(L1)
            src["papers"] += [{"pmid": "37804316", "paper_registry_ids": []}, {"pmid": "41706892", "paper_registry_ids": []}]
        if n["id"] == "NEED-WWOX-GENE-ADDITION":
            if any(o["id"] == "O4" for o in n["observed"]): continue
            n["observed"] += [
                obs("O4", "34253921",
                    "Shank3 heterozygous (switchable) adult mice, 4 months or older: restoring Shank3 expression restores sociability and shifts mPFC neurons from self to other encoding (other-encoding 9.2 to 35.5 percent of task-modulated neurons) over 5 to 8 weeks, tracked in the same animals; controls without CreER or with vehicle unchanged.",
                    "other_animal_model", "mouse", "Shank3 haploinsufficiency (not WWOX)", "medial prefrontal cortex", "adult male, 4 months or older", "post against pre restoration in the same animals; CreER-minus and vehicle controls", "sociability, neuronal encoding", "functional", "restored after a lifelong deficit",
                    "Not WWOX evidence; heterozygous, males, one circuit; neurons pooled as the unit; no seizure, survival or structure endpoint; read in part (receipt FTR-20261029-34253921-01, partial).",
                    L2, "section 1 Shank3"),
                obs("O5", "42587157",
                    "Cntnap2-null adult mice (viable): AAV Meis2 in PV interneurons at 2 months moves synaptic E/I balance, PV excitability, object-location and social memory and ripple rate toward wild type two weeks later (comparator control-AAV null, no pre-treatment baseline), and 4 to 5 months later 3 of 12 treated against 10 of 14 control nulls had seizures (a prevention inside adulthood: onset stated after 6 months). Meis2 also changes wild-type cells and a depolarised PV threshold persists.",
                    "other_animal_model", "mouse", "Cntnap2 null (not WWOX); the intervention is a bypass gene, not the lost gene", "hippocampal CA2/CA3 PV interneurons", "adult, injected at 2 months", "treated against control-AAV null and wild type", "synaptic currents, memory tasks, ripples, ECoG seizures", "functional", "circuit and behaviour moved toward wild type after onset; seizures reduced (prevention)",
                    "Not WWOX evidence; one lesion, one study; cells are the unit in electrophysiology; Methods and supplementary tables not read (receipt FTR-20261029-42587157-01, partial).",
                    L2, "section 1 Meis2"),
                obs("O6", "42190665",
                    "Csnk2b haploinsufficient mice: AAV-PHP.eB CSNK2B at P3 raises survival (50 to 80 percent at day 150) and improves cortical thickness, behaviour and spontaneous seizures; the authors state that efficacy in animals with apparent symptoms remains to be investigated.",
                    "other_animal_model", "mouse", "Csnk2b haploinsufficiency (not WWOX)", "brain-wide", "treatment at P3; adult read-out", "treated against AAV-GFP null", "survival, histology, behaviour, ECoG", "functional", "early-window benefit; no post-onset arm",
                    "Not WWOX evidence; early window only; Results read in part (receipt FTR-20261029-42190665-01, partial).",
                    L2, "section 1 Csnk2b"),
            ]
            n["inferred"] += [
                "That recovery after onset depends on the endpoint class: circuit-level function (Shank3, O4; Meis2, O5) was restored after onset in two non-WWOX adult-viable models, while the only WWOX post-onset add-back (organoid firing at week 10 to 16) did not correct radial glia; this is a hypothesis (R1 of the IT8 P5 loop 2), not a finding, and transfer to WWOX is unverified.",
            ]
            n["counter_evidence"] += [
                "The post-onset precedents use lesions compatible with adult life (heterozygous or viable null); a complete Wwox null is lethal by about P15, so they cannot be reproduced in that model, and the Meis2 effect is a bypass that also acts on wild-type cells (O5).",
            ]
            n["sources"]["documents"].append(L2)
            n["sources"]["papers"] += [{"pmid": p, "paper_registry_ids": []} for p in ("34253921", "42587157", "42190665")]

def e01(d):
    pc = d["p4_card"]
    if "IT8 P5" in json.dumps(d): return
    d["not_known"] += [
        "Whether an ATF4 protein or P-eIF2a rise in a WWOX-deficient neural system survives silencing of network activity (tetrodotoxin or an mGluR5 antagonist): group I mGluR activation raises both in minutes without an Atf4 mRNA change in normal mouse hippocampus (PMID 41706892), and WWOX-deficient systems are hyperexcitable (IT8 P5 loop 1).",
        "Whether the ISR in a WWOX-deficient system is compensatory rather than harmful: in the AFG3L2 precedent (PMID 37804316) HRI or DELE1 loss worsens, and a GADD34-targeted compound improves, patient-cell and mouse endpoints, the opposite sign to the PARS2 fly; the AFG3L2 kinase evidence is siRNA in fibroblasts, GCN2 and PERK were not tested, and the compound's target is disputed (PMID 28447936). Attenuators and potentiators are therefore two arms of one open question, not one direction.",
    ]
    pc["next_measurement"] += (" IT8 P5 additions (design only): (a) run every ATF4 protein and P-eIF2a read with and without activity silencing; (b) sample before, at and after the first network hyperexcitability (organoids: weeks 7, 10, 16) to order any rise against the network phenotype; (c) read OMA1 and OPA1 processing as an HRI-arm trigger readout that needs no DELE1 antibody; (d) only if Stage 1 is positive, test a potentiating arm beside the attenuating arm, with a target-engagement control for any GADD34-targeted compound, and read the isogenic corrected line beside the knock-out.")

def gene(d, c04=False):
    if "IT8 P5" in json.dumps(d): return
    d["p4_card"]["next_measurement"] += (" IT8 P5 addition (design only): a post-onset arm in patient or isogenic organoids, recording the same organoids at week 7 or 8, giving AAV9-WWOX or an AAV9 vector control at week 10 and re-recording at weeks 12, 16 and 24, severe and milder variant classes side by side, which supplies the missing same-organoid baseline, vector control and persistence.")

def wo(d):
    if "IT8-P5" in d["docs"]: return
    d["docs"]["IT8-P5"] = {"path": "advance_it8_p5_20261029/README.md", "label": "IT8 P5 record: two completed loops (ISR sign and kinase; recovery after onset)"}
    for e in d["entries"]:
        if e["need"] == "NEED-ISR-ATTENUATION":
            e["question"] = ("Is the ISR kinase arm active at all in WWOX-deficient neural cells, and is it compensatory or harmful? After the mouse P17 transcripts the sign is unresolved, and two mitochondrial-lesion precedents have opposite signs (protective in one, harmful in the other); neuronal activity alone also raises ATF4 protein without an mRNA change.")
            e["data"] = ("Protein and phosphorylation readouts (phospho-eIF2alpha against total, ATF4 protein, targets, translation) in isogenic WWOX-null against corrected neural lines at matched maturity, with and without activity silencing, sampled before, at and after the first hyperexcitability, with challenge arms and kinase attribution by genetics; the decision table is fixed before the run.")
            e["docs"].append("IT8-P5"); e["updated_by"].append("IT8-P5")
            e["summary_it"] = "Capire se la risposta integrata allo stress è attiva nelle cellule neurali prive di WWOX, se compensa o danneggia e quanto dipende dall'attività di rete: oggi il segno è discordante."
        if e["need"] == "NEED-WWOX-GENE-ADDITION":
            e["data"] += " Added in IT8: a post-onset arm in organoids with a same-organoid baseline and an AAV9 vector control, severe and milder variant classes side by side."
            e["docs"].append("IT8-P5"); e["updated_by"].append("IT8-P5")

rw("needs/needs.json", needs, 1)
rw("cards/E01_isr_modulators.packet.json", e01, 1)
rw("cards/C01_aav9_wwox.packet.json", gene, 2)
rw("cards/C04_aav9_endpoint_families.packet.json", lambda d: gene(d, True), 2)
rw("view/work_order.json", wo, 2)
print("applied")
