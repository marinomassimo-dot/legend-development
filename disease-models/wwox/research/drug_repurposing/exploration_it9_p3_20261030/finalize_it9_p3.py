#!/usr/bin/env python3
"""IT9 P3: assemble selected.tsv, new_vs_known.tsv, p4b_work_order.tsv from the consolidated tables, the search log, the known-check and the path/mechanism fetch.
Usage: finalize_it9_p3.py --work DIR (with o/, known_check.tsv, search_log.tsv, wwox_hits.tsv, paths_mech.tsv, selected_stage.tsv, chembl_profile.tsv) --out DIR"""
import argparse, collections, csv, gzip, json
from pathlib import Path
H = Path(__file__).resolve().parent; D = H.parent; P1 = D / "generation_it9_p1_20261030"; P2 = D / "generation_it9_p2_20261030"; RK = D / "ranking_it8_p9_20261029"
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--work", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
W = Path(a.work); OUT = Path(a.out)
def rd(p, gz=False): return list(csv.DictReader(gzip.open(p, "rt") if gz else open(p), delimiter="\t"))
def wr(p, rows, cols):
    with open(p, "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols)
        for r in rows: w.writerow([("" if r.get(c) is None else str(r.get(c))).replace("\t", " ").replace("\n", " ") for c in cols])
sel = rd(W / "o/selected_core.tsv"); allc = rd(W / "o/candidates_consolidated.tsv")
known = {r["parent"]: r for r in rd(W / "known_check.tsv")}; pm = {r["parent"]: r for r in rd(W / "paths_mech.tsv")}
stage = {r["parent"]: r for r in rd(W / "selected_stage.tsv")}; prof = {r["chembl_id"]: r for r in rd(W / "chembl_profile.tsv")}
slog = rd(W / "search_log.tsv"); hits = rd(W / "wwox_hits.tsv")
p1 = rd(P1 / "seeds.tsv"); inv = {r["family_id"]: r for r in rd(RK / "inventory_families.tsv.gz", True)}
fam_t = collections.defaultdict(list)
for r in rd(P2 / "results/family_actions.tsv.gz", True): fam_t[r["family_id"]].append(r)
# ---- P1 seed lookup by (question, symbol, level) among usable rows
procm = {r["process_id"]: set(r["members_hgnc"].split(",")) for r in rd(P1 / "process_ids.tsv")}
def seed_rows(q, sym, level):
    g = [r for r in p1 if r["question_id"] == q and r["entity_symbol"] == sym and r["level"] == level and r["usable_for_generation"] == "yes"]
    if g: return g
    return [dict(r, entity_symbol=r["process_id"] + " (member " + sym + ")") for r in p1 if r["question_id"] == q and r["process_id"] and sym in procm.get(r["process_id"], set()) and r["direction"] in ("up", "down") and r["level"] == level and r["usable_for_generation"] == "yes"]
SETLVL = {"Q2_expression_tiersAB": ("Q2", "expression"), "Q4_protein_tiersAB": ("Q4", "protein"), "Q5_expression_tiersAB": ("Q5", "expression"), "Q6_expression_tiersAB": ("Q6", "expression"), "Q6_protein_tiersAB": ("Q6", "expression")}
SET_TXT = {
 "Q2": ("Transcripts of the glycolysis genes (SLC2A1, HK2, LDHA, LDHB, BNIP3) are higher in WWOX-knockout organoid and in shWWOX hNPC (human neural, one method); PDK1 and PDHA1 direction is UNCERTAIN",
        "no protein, flux, PDH activity or lactate measurement; not that the shift is harmful or adaptive (maturity rival stated in P1); no compound response",
        "that the compound's action on the network edge changes the transcript in the direction shown, and that a transcript change means a pathway change"),
 "Q4": ("GAD1 and GAD2 protein lower in the Wwox-null mouse hippocampus (western, five lanes per genotype, tier B, mouse)",
        "a lower GAD protein in one mouse system and age; not that the human organoid agrees (it is UNCERTAIN there, rows kept out of the seed set), nor any interneuron function or E/I balance",
        "that raising or lowering GAD1/GAD2 expression via the edge is a useful direction, and that a protein change maps to a regulatory edge at transcript level"),
 "Q5": ("IL1B, TNF and IL6 transcripts higher in two mouse models (Wwox-null hippocampus; P47T cerebellum), tier B; reactivity direction is UNCERTAIN (down in the rat)",
        "inflammatory-gene transcripts in two mouse systems; no cytokine protein, no microglial state, no human data; the rat disagrees",
        "that damping these transcripts is beneficial (protective-versus-harmful valence is unresolved) and that edge direction applies in glia"),
 "Q6": ("MYC transcript higher in WWOX-deficient human radial glia (single-cell) and the MYC-positive fraction higher in knockout and patient-line organoids (tier A, human)",
        "a MYC increase in one cell type of organoids; not MYC activity, valence or maturity independence; one seed gene only, so every proposal is a MYC-neighbour proposal",
        "that moving MYC (or its upstream regulators) in the stated direction is relevant to a neurological outcome; the seed is shared with oncology, where most agents were made"),
}
# hand-authored notes per parent: (adds_vs_known, specific_inferred, feasibility_judgment)
N = {
 "CHEMBL4585668": ("HIF-2alpha (EPAS1) inhibitor; the Q2 axis is carded through HIF1A/PDK/LDH (E02, E03, E04) but not this isoform or class. Adds: different node of the HIF axis.", "EPAS1 -> LDHA edge sign is from the context-free network; HIF-2alpha role in WWOX-deficient neural cells is not measured", "oral, approved (VHL disease, per ChEMBL phase 4); anaemia and hypoxia class effects; oncology label"),
 "CHEMBL1218": ("Melatonin MT1/MT2 agonist; no carded unit on melatonin receptors. Adds: a different class, outside antiseizure and metabolic cards; a MIMICS-arm proposal (relevant only if the glycolytic shift is adaptive).", "3-hop path via GNAO1 and HES1; the mimic direction means the compound would RAISE BNIP3-type signals", "approved oral sleep drug; paediatric use outside its label; CNS-active"),
 "CHEMBL5095251": ("O-GlcNAcase (OGA) inhibitor; no mention in any searched LEGEND surface. Adds: a new target class (O-GlcNAc cycling) reaching PFKP by one network edge.", "OGA -> PFKP edge from the network; WWOX/O-GlcNAc link is not established; identity is name-matched only (UNVERIFIED)", "clinical-stage CNS-directed compound per ChEMBL phase 2; availability unknown; status of programme not checked"),
 "CHEMBL1201346": ("Mesalazine prodrug (PPARG route) in a MIMICS arm; no LEGEND mention. Adds: PPAR gamma axis.", "PPARG -> SLC2A1 edge; PPARG is a hub (degree 209); conditional on PDK1/PDHA1 direction", "colon-delivered prodrug with minimal systemic exposure of the parent: CNS relevance doubtful; kept only because the rule has no exposure axis"),
 "CHEMBL1200598": ("Estrogen receptor agonist prodrug (ERbeta route); ERbeta is hit by 29 of 606 seed-specific parents, so this stands for a hub-driven cluster. Adds: a hormonal route to GAD2 not carded.", "ESR2 -> GAD2 edge sign +; the Q4 seed is a mouse protein decrease, the edge is a transcriptional relation; ESR2 degree 170", "hormonal anticancer drug, chronic paediatric neurological use implausible; selective ERbeta ligands would be the real class (not in the catalogue family)"),
 "CHEMBL2105804": ("Microsomal triglyceride transfer protein inhibitor reached through P4HB (PDI, the MTTP beta-subunit); no LEGEND mention. Adds: an ER-stress/UPR relay to GAD1 (3 hops).", "P4HB -> ERN1 -> XBP1 -> GAD1 net sign -1: a chain through UPR genes, vulnerable to the target-to-subunit mapping; probably an artefact of how the complex target is coded", "discontinued for hepatic steatosis (ChEMBL phase 2); no CNS rationale"),
 "CHEMBL140": ("Natural product, EP300 route; the glial-reactivity modulators axis is carded (J01, abstention) without naming it. Adds: nothing mechanistically new beyond a promiscuous agent; kept as a Q5 representative.", "EP300 -> TNF edge; curcumin's catalogue entry has 2 signed targets but is a known multi-target/assay-interference compound, so the promiscuity diagnostic UNDERESTIMATES it", "poor exposure; PAINS-type; listed only because it passed the pre-written feasibility tests"),
 "CHEMBL2107819": ("Caspase-1 inhibitor (prodrug of VX-765's active acid). Named in the glial-reactivity card J01 (abstention). Adds: a Q5 seed-specific route (IL1B via CASP1) that confirms an already-carded axis, so it is a reference more than a new idea.", "CASP1 -> IL1B edge sign +; the seed IL1B is a mouse transcript rise (tier B)", "oral prodrug, phase 2 (ChEMBL); seizure models in the literature; CNS exposure not checked"),
 "CHEMBL3545357": ("RORgamma antagonist (RORC route to IL6); no LEGEND mention. Adds: a nuclear-receptor immune route in Q5.", "RORC -> IL6 edge; the compound's CNS exposure and indication (autoimmune) are unrelated to the seed system", "phase 1 only (ChEMBL); sparse public data"),
 "CHEMBL215152": ("Aurora B kinase inhibitor reached through AURKB -> MYC; no LEGEND mention. Adds: a MYC upstream-kinase route (the carded MYC-adjacent items are A51 and tankyrase, D01/D02).", "AURKB -> MYC edge sign +; the MYC seed is a radial-glia transcript rise", "antimitotic oncology agent: under a strict reading of F1 (cytotoxic) it would be excluded; kept because the written test is ATC/mechanism-text based and was not met"),
 "CHEMBL43452": ("Cereblon-modulating immunomodulator; no LEGEND mention. Adds: a ubiquitin-ligase route to MYC (MIMICS arm).", "ChEMBL codes the mechanism as 'CRL4(CRBN) inhibitor' so the signed action on CUL4A is -1 and CUL4A -> MYC is -1; the real mechanism is a molecular glue degrading IKZF1/3 which LOWERS MYC in myeloma, so the sign is probably wrong for this class", "teratogenic class (REMS); oncology/haematology indication"),
 "CHEMBL3414626": ("DOT1L inhibitor; no LEGEND mention. Adds: an epigenetic route to MYC.", "DOT1L -> MYC edge sign +; identity name-matched only (UNVERIFIED)", "intravenous oncology drug, phase 2; CNS exposure not expected"),
 "CHEMBL269538": ("DYRK1A inhibitor (beta-carboline) in a MIMICS arm; DYRK1A is a neurodevelopmental kinase; no LEGEND mention. Adds: a neurodevelopment-linked target not carded.", "DYRK1A -> MYC edge sign -1; MIMICS means the compound would reproduce the MYC rise; identity name-matched only (UNVERIFIED)", "natural alkaloid, MAO-A inhibitor, psychoactive, phase 1 only; selectivity poor"),
 "CHEMBL495727": ("ARTEFACT CONTROL: multi-kinase inhibitor (14 signed targets) reaching MYC via AURKB. Shows what promiscuity does to the ranking.", "AURKB -> MYC; most of the 14 targets also lie near MYC", "oncology; not a candidate"),
 "CHEMBL848": ("ARTEFACT CONTROL: lenalidomide, same CRBN/CUL4A route and sign problem as pomalidomide.", "CUL4A -> MYC sign problem as above", "oncology/haematology; not a candidate"),
 "CHEMBL1094": ("REFERENCE: felbamate, antiseizure with NMDAR (glycine-site) action; on the IT8 P9 deepening queue and in the NMDAR intervention card F04.", "direct hit on GRIN2C (a seed gene in the direct-search arm), not a network proposal", "approved but boxed warning for aplastic anaemia/hepatic failure (to be confirmed by P4b)"),
 "CHEMBL807": ("REFERENCE: memantine, NMDAR channel blocker; carded (F01, F04, P11) and on the deepening queue.", "direct hit on a GRIN2C seed gene, not a network proposal", "approved oral"),
 "CHEMBL306823": ("REFERENCE: dichloroacetate, PDK inhibitor; carded (E03, I01) with an IT5 closed-loop reading.", "recovered only via its own target (PDK1 is both an uncertain seed and its target); P2 T3 flags RECOVERED_ONLY_VIA_OWN_TARGET", "experimental/approved status mixed in the catalogue; peripheral neuropathy known (to confirm)"),
 "CHEMBL413": ("REFERENCE: sirolimus, mTOR inhibitor; early-benefit card EB-MTOR-AX-01 and unit U19.", "Q3 direct-search item (ISR set), not a seed-specific proposal", "approved immunosuppressant"),
 "CHEMBL1650595": ("REFERENCE: AR-12 (OSU-03012), named in the join card Q-N-08 (dichloroacetate) only as an example of the PDK1/PDPK1 symbol collision; not a card subject. It is a PDPK1 inhibitor: its presence in the Q2 direct-search arm comes from the PDK1 symbol collision (PDK1 is an alias of PDPK1), not from the pyruvate dehydrogenase kinase.", "symbol-alias artefact in the direct-search arm of Q2", "phase 1 oncology compound"),
}
# ---- order and ids
order = {"slot": 1, "overall": 1, "fill": 2, "reference": 3, "artefact_control": 4}
def okey(r):
    w = r["selection_reason"].split(":")[0]; return (order.get(w, 9), r["best_set"] or r["q_arms"], r["parent"])
def okey2(r):
    w = r["selection_reason"].split(":")[0]; grp = 2 if w == "artefact_control" else 1 if w == "reference" else 0
    return (grp, (r["best_set"] or r["q_arms"])[:2], r["direction"], r["parent"])
sel.sort(key=okey2)
rows = []; nvk = []; p4b = []
for i, r in enumerate(sel, 1):
    cid = "P3-%02d" % i; par = r["parent"]; pr = prof.get(r["chembl_parent"], {}); st = stage[par]
    s, lvl = SETLVL.get(r["best_set"], ("", ""))
    refrow = r["selection_reason"] == "reference"
    qn = s or (r["q_arms"].split(";")[0].split(":")[0])
    seedtxt = SET_TXT.get(qn, ("", "", ""))
    srows = seed_rows(qn, r["top_seed"], lvl) if (s and r["top_seed"]) else []
    sids = ";".join(x["seed_id"] for x in srows)
    sdesc = "; ".join("%s %s %s %s tier %s %s" % (x["seed_id"], x["entity_symbol"], x["level"], x["direction"], x["context_tier"], x["species_observed"]) for x in srows)
    if refrow:
        sdesc = "direct-search/top-list reference: seed gene %s (arm %s); no seed-specific proposal" % (r["main_target"] or r["top_seed"] or "n/a", r["q_arms"])
    tgts = fam_t.get(r["family_ids"].split(";")[0], [])
    tdesc = "; ".join("%s(%s,%s)" % (t["target_symbol"], t["mean_sign"], t["groups"]) for t in tgts[:8])
    pmrow = pm.get(par, {})
    k = known[par]; kl = []
    if k["cards_or_packets_naming_it"]: kl.append("named in " + k["cards_or_packets_naming_it"])
    if k["needs_files_naming_it"]: kl.append("needs: " + k["needs_files_naming_it"])
    if k["ranking_tables_naming_it"]: kl.append("IT8 P9: " + k["ranking_tables_naming_it"])
    if k["hypothesis_ledger_heading_match"]: kl.append("hypothesis ledger heading")
    if k["registry_records_headings"]: kl.append("registry_records records: " + k["registry_records_headings"])
    legend = "; ".join(kl) if kl else "no mention found in the searched LEGEND surfaces (cards, packets, needs, IT8 P9 tables, hypothesis-ledger headings, 7 indexed registries through registry_records.py)"
    status = "KNOWN_TO_LEGEND (compound named)" if (k["cards_or_packets_naming_it"] or k["ranking_tables_naming_it"]) else "NOT_FOUND_IN_SEARCHED_LEGEND_SURFACES"
    if par == "CHEMBL1650595": status = "KNOWN_TO_LEGEND (named only as a symbol-collision example in the DCA join card)"
    if par == "CHEMBL2107819": status = "KNOWN_TO_LEGEND (listed among catalogue compounds of the abstention card J01)"
    ls = {x["search"][:1]: x for x in slog if x["parent"] == par}
    def hv(x): return "pubmed %s / europepmc %s" % (x["pubmed_hits"], x["europepmc_hits"]) if x else "not run"
    a_, b_, c_ = ls.get("A"), ls.get("B"), ls.get("C")
    wh = [h for h in hits if h["parent"] == par]
    note = N.get(par, ("", "", ""))
    ident = "verified (catalogue ChEMBL id)" if r["identity_route"] == "catalogue_chembl" else "UNVERIFIED (%s)" % r["identity_route"]
    rows.append(dict(cand_id=cid, slot=r["selection_reason"], parent_chembl_id=par, name=st["name"], aliases_searched=st["chembl_name"], question=qn, seed_set=r["best_set"] or r["q_arms"], arm_direction=r["direction"], compatible_action=r["direction"] if not refrow else "n/a (reference)",
                     conditional_on_uncertain_seed=r["conditional"], Z_total_null=r["best_Z_total"], Z_indegree_null=r["best_Z_indeg"], top_seed_gene=r["top_seed"], top_seed_direction=r["top_seed_direction"], p1_seed_ids=sids, wwox_datum=sdesc, hop="hops1-3" if r["hop"] in ("hops1-3",) else r["hop"],
                     main_target=r["main_target"], target_degree=r["main_target_degree"], hub_target=r["hub_target"], n_signed_targets=r["n_signed_targets"], promiscuous=r["promiscuous"], network_paths=pmrow.get("paths_(target_to_seed_gene)", ""), mech_group=r["mech_group"],
                     datum_supports=seedtxt[0], datum_does_not_support=seedtxt[1], still_inferred=seedtxt[2] + "; " + note[1], identity=ident, max_phase=r["max_phase"], atc=r["atc"], status_class=r["status_class"], feasibility_flags=r["feasibility_flags"], feasibility_judgment_UNVERIFIED_general_knowledge=note[2],
                     class_asm_nmdar_tcalcium=r["class_asm_nmdar_tcalcium"], evaluation_guard=r["guard"] or "none", legend_status=status, hub_note=("target is a hub" if r["hub_target"] == "1" else "")))
    nvk.append(dict(cand_id=cid, name=st["name"], slot=r["selection_reason"], question=qn, legend_status=status, legend_where=legend, class_level=("axis carded" if qn in ("Q2", "Q4", "Q5", "Q6") and any(x in (k["cards_or_packets_naming_it"] + k["ranking_tables_naming_it"]) for x in ["E0", "F0", "J0"]) else ""),
                    search_A_compound_x_WWOX=hv(a_), search_B_compound_x_epilepsy_DEE=hv(b_), search_C_compound_x_phenotype=hv(c_), WWOX_hits_listed=len(wh), WWOX_hits_reading="; ".join(h["title"][:90] for h in wh) + (" [titles only; abstracts not opened]" if wh else ""),
                    literature_status=("WWOX-query hits exist (see reading)" if wh else "no hits for compound x WWOX in the stated perimeters on %s" % (a_["date"] if a_ else "")), adds_relative_to_known=note[0], date=(a_ or {}).get("date", "")))
    gen = ["identity: InChIKey, salt/parent, ChEMBL vs source record (%s)" % ident, "target potency and selectivity at the main target %s and at the other signed targets (%s) from ChEMBL/GtoPdb activity records; a value with assay and species" % (r["main_target"] or "n/a", r["n_signed_targets"]),
           "human exposure: route, dose range, half-life, CSF/brain penetration, paediatric data, label (boxed warnings, contraindications)", "safety and counter-evidence: seizure-lowering or seizure-provoking reports, neurodevelopmental toxicity, interactions with antiseizure drugs",
           "edge evidence: source database and context of the network edge(s) %s (SIGNOR/CollecTRI record, tissue)" % (pmrow.get("paths_(target_to_seed_gene)", "")[:120] or "n/a"), "target expression in the relevant neural cell types and age (the network is context-free)", "trials: ClinicalTrials.gov in epilepsy, DEE, hypomyelination, neurodevelopment; WWOX-system measure if any (none expected)",
           "define a measurable response in a WWOX-deficient system that would discriminate adaptive from harmful valence (conditional arms)"]
    spec = {"CHEMBL1218": "check MT1/MT2 expression in the system and the GNAO1/HES1 edges; melatonin as a related reference", "CHEMBL5095251": "confirm structure and programme status; OGA brain PK; OGA inhibition effect on glycolysis genes in neural cells", "CHEMBL4585668": "HIF-2alpha versus HIF-1alpha expression in WWOX-deficient neural cells; haematological safety in children",
            "CHEMBL43452": "re-code the mechanism (glue, neosubstrates IKZF1/3) and decide the sign of the MYC effect before any use; teratogenicity", "CHEMBL848": "as pomalidomide; keep only as control", "CHEMBL1200598": "identify ERbeta-selective ligands in the catalogue; hormonal safety in children", "CHEMBL2105804": "check how MTTP is mapped to P4HB in the catalogue; likely drop",
            "CHEMBL140": "assay-interference/PAINS review; exposure", "CHEMBL2107819": "reference for J01; CASP1/IL1B edge; exposure of the active acid in CNS", "CHEMBL3545357": "obtain any published human data (phase 1)", "CHEMBL215152": "decide on the cytotoxic reading of F1; likely drop for chronic use",
            "CHEMBL3414626": "confirm structure; IV only: likely drop", "CHEMBL269538": "confirm structure; DYRK1A selectivity versus MAO-A; psychoactivity", "CHEMBL495727": "none (control)", "CHEMBL1201346": "systemic exposure of the active species; likely drop",
            "CHEMBL1094": "reference: boxed-warning review", "CHEMBL807": "reference: existing card F01/F04", "CHEMBL306823": "reference: existing closed-loop; no new fetch beyond the standard list", "CHEMBL413": "reference: existing card EB-MTOR-AX-01", "CHEMBL1650595": "reference: confirm PDPK1 identity of the target in the Q2 direct-search arm"}
    p4b.append(dict(cand_id=cid, name=st["name"], slot=r["selection_reason"], priority=("control/reference" if r["selection_reason"] in ("reference", "artefact_control") else "first"), fetch_items=" | ".join("(%d) %s" % (j + 1, g) for j, g in enumerate(gen)), candidate_specific=spec.get(par, ""), do_not=("no efficacy claim; a compatible action is not a benefit; conditional arms stay open"), identity_state=ident))
cols = list(rows[0]); wr(OUT / "selected.tsv", rows, cols)
wr(OUT / "new_vs_known.tsv", nvk, list(nvk[0])); wr(OUT / "p4b_work_order.tsv", p4b, list(p4b[0]))
# profile table (first-pass)
prof_rows = []
for r in sel:
    pr = prof.get(r["chembl_parent"], {}); st = stage[r["parent"]]; pmrow = pm.get(r["parent"], {})
    f0 = r["family_ids"].split(";")[0]; tgts = fam_t.get(f0, [])
    prof_rows.append(dict(cand_id=[x["cand_id"] for x in rows if x["parent_chembl_id"] == r["parent"]][0], name=st["name"], chembl_parent=r["chembl_parent"], chembl_pref_name=pr.get("pref_name", ""), parent_pref_name=pr.get("parent_pref_name", ""), n_catalogue_families_in_parent=r["n_families"], family_ids=r["family_ids"],
                          max_phase=pr.get("max_phase", ""), molecule_type=pr.get("molecule_type", ""), oral=pr.get("oral", ""), parenteral=pr.get("parenteral", ""), topical=pr.get("topical", ""), withdrawn=pr.get("withdrawn_flag", ""), first_approval=pr.get("first_approval", ""), atc=pr.get("atc", ""), black_box_warning_flag=pr.get("black_box_warning", ""), chembl_fetched=pr.get("fetched", ""),
                          catalogue_signed_targets=("; ".join("%s mean_sign=%s sources=%s" % (t["target_symbol"], t["mean_sign"], t["groups"]) for t in tgts) or "none signed"), chembl_curated_mechanism_live=pmrow.get("chembl_curated_mechanism_live", ""),
                          access_categories=r["access_categories"], modality=r["modality"], lincs_neural_signature=inv.get(f0, {}).get("msig_neural_strict", ""), atc_nervous_system=("yes" if "N" in [x[:1] for x in (r["atc"] or "").split(";") if x] else "no" if r["atc"] else "UNKNOWN(no ATC)"), existing_cards=known[r["parent"]]["cards_or_packets_naming_it"] or "none found"))
wr(OUT / "profiles_first_pass.tsv", prof_rows, list(prof_rows[0]))
print(len(rows), "selected;", collections.Counter(r["slot"].split(":")[0] for r in rows), file=__import__("sys").stderr)
