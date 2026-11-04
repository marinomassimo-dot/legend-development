"""IT27 P5: read-only reconstruction of the hand-over representative of a mechanism cluster, and sensitivity of the 15 hand-overs to the order terms.
Reads results_s7 (IT26 A1) and calls select_handoff / order_key of run_generation_it21.py unchanged. Writes TSVs next to this file. Changes nothing else."""
import csv, importlib.util, sys, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = HERE.parent
S7 = DR / "generation_it26_a1_20261104" / "results_s7"
GEN = DR / "generation_it21_p2_20261103" / "run_generation_it21.py"
sys.path.insert(0, str(HERE.parents[4] / "framework" / "scripts"))
spec = importlib.util.spec_from_file_location("gen", GEN)
g = importlib.util.module_from_spec(spec)
spec.loader.exec_module(g)


def rd(p):
    return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))


def wr(name, rows, cols):
    with open(HERE / name, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        for r in rows:
            w.writerow([r.get(c, "") for c in cols])


props = rd(S7 / "proposals_it21.tsv")
handed = {r["proposal_id"] for r in rd(S7 / "handoff_it21.tsv")}
elig = [p for p in props if p["handoff_eligible"] == "yes"]
CL = [("Q2", "H_HARM", "HDAC5"), ("Q2", "H_HARM", "XIAP"), ("Q5", "H_HARM", "EZH2"), ("Q8", "H_HARM", "EZH2"), ("Q5", "H_HARM", "ROCK2")]

# 1. order_key reconstruction
out = []
for k in CL:
    rows = [p for p in elig if (p["question"], p["hypothesis"], p["main_target"]) == k]
    keyed = sorted(rows, key=g.order_key)
    best = g.order_key(keyed[0])
    for i, p in enumerate(keyed, 1):
        ok = g.order_key(p)
        out.append(dict(question=k[0], hypothesis=k[1], main_target=k[2], proposal_id=p["proposal_id"], compound=p["compound"], handed_over="yes" if p["proposal_id"] in handed else "no",
                        k1_cluster_work_done=ok[0], k2_seed_support_limited=ok[1], k3_unmeasured_at_main=ok[2], k4_minus_n_origins=ok[3], k5_chain_edges=ok[4], k6_minus_zmin=ok[5],
                        rank_in_cluster=i, exact_tie_with_first="yes" if ok == best else "no", n_exact_ties_with_first=sum(1 for q in keyed if g.order_key(q) == best) if ok == best else "",
                        zmin_text_ascending_rank=sorted(rows, key=lambda r: (-int(r["n_origins"]), int(r["chain_edges"]), float(r["zmin"]))).index(p) + 1))
wr("order_key_reconstruction_it27p5.tsv", out, list(out[0]))

# 2. variants
def sel(rows, key):
    best = {}
    for r in rows:
        k = (r["question"], r["hypothesis"], r["main_target"])
        if k not in best or key(r) < key(best[k]):
            best[k] = r
    res, cnt = [], collections.Counter()
    for r in sorted(best.values(), key=lambda r: (r["question"], r["hypothesis"]) + tuple(key(r))):
        gk = (r["question"], r["hypothesis"])
        if cnt[gk] < 3:
            res.append(r); cnt[gk] += 1
    return res

V = {
    "V0_code_as_is(select_handoff)": lambda rs: g.select_handoff(rs),
    "V1_text_literal_zmin_ascending_no_k1_k3": lambda rs: sel(rs, lambda r: (-int(r["n_origins"]), int(r["chain_edges"]), float(r["zmin"]))),
    "V2_text_with_zmin_descending_no_k1_k3": lambda rs: sel(rs, lambda r: (-int(r["n_origins"]), int(r["chain_edges"]), -float(r["zmin"]))),
    "V3_code_zmin_ascending": lambda rs: sel(rs, lambda r: (g.order_key(r)[:5]) + (float(r["zmin"]),)),
    "V4_code_input_order_reversed": lambda rs: g.select_handoff(rs[::-1]),
    "V5_code_ties_by_compound_name": lambda rs: sel(rs, lambda r: g.order_key(r) + (r["compound"].lower(),)),
}
base = {(r["question"], r["hypothesis"], r["main_target"]): r["compound"] for r in V["V0_code_as_is(select_handoff)"](elig)}
assert {r["proposal_id"] for r in V["V0_code_as_is(select_handoff)"](elig)} == handed, "reconstruction does not reproduce the 15 hand-overs"
vr = []
for name, fn in V.items():
    res = fn(elig)
    cur = {(r["question"], r["hypothesis"], r["main_target"]): r["compound"] for r in res}
    same_cluster_set = set(cur) == set(base)
    changed = [f"{'/'.join(k)}: {base[k]} -> {cur[k]}" for k in cur if k in base and cur[k] != base[k]]
    new_c = [f"{'/'.join(k)}={cur[k]}" for k in cur if k not in base]
    lost_c = ["/".join(k) for k in base if k not in cur]
    vr.append(dict(variant=name, n_handed=len(res), same_cluster_set="yes" if same_cluster_set else "no", n_representatives_changed=len(changed), representatives_changed=" | ".join(changed), clusters_entering=" | ".join(new_c), clusters_leaving=" | ".join(lost_c)))
wr("rule_variants_it27p5.tsv", vr, list(vr[0]))
print("OK", len(out), "order rows;", len(vr), "variants")

# 3. alternatives classification (rule-based from exported columns + short curated notes; classes are labels for reading, not decisions)
NOTES = {
 ("HDAC5", "pracinostat"): "REPRESENTATIVE. Pan-HDAC (class I and IIb inside 10 nM-ish GtoPdb IC50s 40-49 nM; HDAC5 47 nM GtoPdb/20197387, 5113 nM ChEMBL/29360358, Ki 21 nM ChEMBL/25637120); oral, phase 3 oncology; CNS exposure not found in repo",
 ("HDAC5", "tmp269"): "class IIa-selective probe: GtoPdb IC50 HDAC4 157, HDAC5 97, HDAC7 43, HDAC9 23 nM (one document 23524983, abstract not read here); only HDAC5-only engine contribution (P6 SINGLE_TARGET); ChEMBL id CHEMBL3110004 exists in catalog/ligand_reconciliation_not_merged.tsv (chembl_id_active_but_not_in_catalogue_selection) and GtoPdb ligand 7491; tool compound, no human exposure statement (IT9 F5)",
 ("HDAC5", "ss-208"): "HDAC6-selective (HDAC6 12 nM v HDAC5 6910 nM, IC50, 31414801): a negative-selectivity control for HDAC5 rather than a candidate; identity not in catalogue",
 ("HDAC5", "ka1010"): "HDAC6-selective (HDAC6 8 nM v HDAC5 1093 nM, IC50, 27222932): same remark as SS-208",
 ("HDAC5", "martinostat"): "class I/IIb-selective (HDAC1 0.3, HDAC3 0.6, HDAC6 4.1, HDAC5 352 nM IC50 in GtoPdb, 25203558); values exist in the GtoPdb cache but the family is NOT_ASSESSABLE; PubChem/ChEMBL structure agreement exists but only as a weak R4-type check (identity_gsrs_it26_a1_20261104/verify_rows.tsv), not in the 19 firm R4 rows",
 ("HDAC5", "scriptaid"): "pan-HDAC, HDAC6 Ki 0.25 nM v HDAC5 Ki 1000 nM (20139990); identity not in catalogue",
 ("HDAC5", "nanatinostat"): "decided in IT21 P4a (REJECTED_INFORMATIVE) for its OWN potency profile (HDAC5 IC50 200 nM v HDAC1 3 nM); decision scope is molecule-specific and was not transferred to the cluster (IT22 P1)",
 ("HDAC5", "vorinostat"): "HDAC5 Ki 3600 v HDAC1 1.3 nM (2769-fold; 20139990): screen WEAK_ATTRIBUTION (convention: fold >= 10 and main > 100 nM)",
 ("HDAC5", "romidepsin"): "catalogue types it protein_or_peptide (cyclic depsipeptide natural product); HDAC5 Ki 550 v HDAC1 0.0015 nM: class I-selective in the Ki panel",
 ("HDAC5", "cudc-101"): "dual action: EGFR IC50 2.4 nM and HER2 15.7 nM are more potent than HDAC5 11.4 nM (20143778); EGFR/HER2 inhibition is a concomitant action the chain does not carry",
 ("HDAC5", "quisinostat"): "most potent HDAC5 value in the cluster (IC50 3.69 nM, 19861438) but 33.5-fold weaker than HDAC1 (0.11 nM): BORDERLINE_POTENT; ranks last of the nine unflagged eligible rows only because zmin is 3.16",
 ("HDAC5", "belinostat"): "approved; HDAC5 Ki 175 nM v HDAC1 0.85 (20139990): HDAC5 is a secondary action ~200-fold weaker than class I",
 ("HDAC5", "givinostat"): "approved (EU, DMD); HDAC5 Ki 600 v HDAC1 2 nM (20139990): secondary action ~300-fold weaker",
 ("HDAC5", "dacinostat"): "HDAC5 Ki 420 v HDAC1 0.55 nM (20139990): secondary action",
 ("HDAC5", "trichostatin a"): "tool compound; HDAC5 Ki 260 v HDAC1 0.2 nM (20139990); no human exposure",
 ("HDAC5", "panobinostat"): "approved; no HDAC5 value in the table (EC50 at HDAC1-4,6-9 only) so ranked after measured rows (k3); P6 CONFLICT_BETWEEN_TARGETS (HDAC8/SIRT1 contrary, SIRT6/7 favourable)",
 ("HDAC5", "abexinostat"): "no HDAC5 value (HDAC1 7, HDAC3 8.2 nM IC50 only) so k3 demotes it",
 ("HDAC5", "valproic acid"): "different action class: short-chain fatty acid, weak HDAC1 IC50 400000 nM, no HDAC5 value; antiseizure drug (FAERS seizure-report limit is confounded by indication); k3 demotes it",
 ("HDAC5", "4-phenylbutyric acid"): "short-chain fatty-acid-type HDAC inhibitor and chemical chaperone: ER-stress/ISR actions are a concomitant mechanism; no HDAC5 value; identity only via R4 (firm)",
 ("HDAC5", "pivaloyloxymethylbutyrate"): "butyrate prodrug; no HDAC5 value; identity only via R4 (firm)",
 ("XIAP", "astx-660"): "REPRESENTATIVE. non-peptidomimetic IAP antagonist: XIAP IC50 2.8 nM, cIAP1 (BIRC2) IC50 0.22 nM (12.7-fold in favour of cIAP1)",
 ("XIAP", "xevinapant"): "XIAP Ki 66.4 nM (BIR3, 21443232) v cIAP1 Ki 1.9 nM: cIAP-preferring (35-fold); Ki not comparable with ASTX-660 IC50",
 ("XIAP", "idronoxil"): "identity firm via R4 (CID 219100 / CHEMBL1957038); XIAP pair rests on a listing-only DGIdb claim (ClearityFoundationClinicalTrial, alias_scan_it26_a2); no affinity (NOT_ASSESSABLE); KG pointers (CTD, NCIT) report XIAP abundance/degradation, an indirect action: not read here; limit KEPT",
 ("XIAP", "azd5582"): "IC50 XIAP 15, cIAP1 15, cIAP2 21 nM (24320998): the most balanced XIAP/cIAP profile in the table; identity not in catalogue",
 ("XIAP", "bv-6"): "Kd 1.3 nM at XIAP BIR2-BIR3 (18022362): only target measured (no cIAP1 value), so no selectivity statement; identity not in catalogue",
 ("XIAP", "sm-122"): "Ki XIAP 26 v cIAP1 1 nM (19049347): cIAP-preferring 26-fold; identity not in catalogue",
 ("XIAP", "sm-337"): "Ki XIAP 26 v cIAP1 1.5 nM (19049347): cIAP-preferring 17-fold; identity not in catalogue",
 ("XIAP", "gdc-0152"): "Ki XIAP 28 nM (BIR3, 22413863); catalogue types it protein_or_peptide (peptidomimetic)",
 ("EZH2", "gsk2816126"): "SAM-competitive EZH2 inhibitor, IC50 9.9 nM (only target measured; 23051747/22904200); phase 1; no brain exposure data in repo",
 ("EZH2", "tazemetostat"): "approved (phase 4); identity firm via R4 for the DGIdb twin and a ChEMBL family; both NOT_ASSESSABLE in the table, yet the GtoPdb cache holds EZH2 IC50 11 nM for ligand 7011 (23620515, not read here) that no family joins",
 ("EZH2", "mevrometostat"): "Ki < 0.1 nM (29211475): Ki, not comparable with the IC50 values of GSK2816126 and tazemetostat; phase 2",
 ("EZH2", "gsk343"): "tool probe, already qualified KEPT_CONDITIONAL (IT21 P4a, Q5 cytokine axis; EZH2 IC50 4 nM v EZH1 240 nM, 60-fold): work done, not an exclusion",
 ("EZH2", "valemetostat"): "dual EZH1/EZH2 (GtoPdb EZH2 5.1, EZH1 16 nM, 28741798): flagged highest-risk for the myelin axis by the IT22 EZH2 dossier; no catalogue family",
 ("EZH2", "tulmimetostat"): "dual EZH1/EZH2 class; no catalogue family and no value",
 ("ROCK2", "sar-407899 free base"): "REPRESENTATIVE. ROCK2 IC50 102 nM v ROCK1 276 nM (2.7-fold; 19597037), Ki ROCK2 36 nM; clinical candidate phase 2",
 ("ROCK2", "belumosudil"): "ROCK2 IC50 105 nM v ROCK1 24000 nM (~230-fold, radiometric cell-free, 18832915); approved (phase 4)",
 ("ROCK2", "fasudil"): "pan-ROCK, Ki ROCK1 100 v ROCK2 271 nM (21145740/19597037); also hits PKA/PKG-type kinases (not in the table)",
 ("ROCK2", "ripasudil"): "IC50 ROCK2 19 v ROCK1 51 nM, PRKACA 2100 nM (24502505); topical ophthalmic",
}
alt_rows = []
for k in [("Q2", "H_HARM", "HDAC5"), ("Q2", "H_HARM", "XIAP"), ("Q8", "H_HARM", "EZH2"), ("Q5", "H_HARM", "EZH2"), ("Q5", "H_HARM", "ROCK2")]:
    members = [p for p in props if (p["question"], p["hypothesis"], p["main_target"]) == k]
    el = sorted([p for p in members if p["handoff_eligible"] == "yes"], key=g.order_key)
    first = g.order_key(el[0]) if el else None
    rep = next((p for p in members if p["proposal_id"] in handed), None)
    seen = set()
    for p in members:
        bn = p["base_name"].lower()
        if bn in seen:
            continue
        seen.add(bn)
        b = p["handoff_blocker"]
        if p["proposal_id"] in handed:
            cls = "REPRESENTATIVE"
        elif b == "identity_not_resolved":
            cls = "missing_data (no catalogue identity)"
        elif b == "decided_in_earlier_qualification_record":
            cls = "worked_earlier (priority only)" if bn == "gsk343" else "scientifically_excluded (own record, molecule-specific)"
        elif b == "main_target_weak_attribution":
            cls = "scientifically_excluded (attribution screen, a convention)"
        elif b.startswith("modality"):
            cls = "differing_modality (catalogue typing)"
        elif p["handoff_eligible"] == "yes":
            ok = g.order_key(p)
            if ok == first and k[2] != "HDAC5":
                cls = "capacity_only (exact tie on every order term; representative set by input order)"
            elif ok[2] == 1:
                cls = "capacity_only (ranked lower: no measured value at main target, k3)"
            elif ok[0] == 1 and rep is None:
                cls = "capacity_only (cluster demoted by k1 work_done and Q5 cap of 3)"
            else:
                cls = "capacity_only (ranked lower on zmin, k6)"
        else:
            cls = "other"
        pos = ""
        if p["handoff_eligible"] == "yes":
            pos = str(sorted(el, key=g.order_key).index(p) + 1) + " of " + str(len(el))
        alt_rows.append(dict(cluster="/".join(k), proposal_id=p["proposal_id"], compound=p["compound"], class_=cls, exported_blocker=b, order_position=pos, zmin=p["zmin"],
                             main_target_nM=p["attribution_main_nm"], main_measure=p["attribution_main_measure"], best_other_target=p["attribution_best_target"], best_other_nM=p["attribution_best_nm"],
                             fold_main_over_best_other=p["attribution_fold"], attribution_state=p["attribution_state"], max_phase=p["max_phase"], note=NOTES.get((k[2], bn), "")))
wr("alternatives_classification_it27p5.tsv", [dict(r, **{"class": r.pop("class_")}) for r in alt_rows], ["cluster", "proposal_id", "compound", "class", "exported_blocker", "order_position", "zmin", "main_target_nM", "main_measure", "best_other_target", "best_other_nM", "fold_main_over_best_other", "attribution_state", "max_phase", "note"])
print("alternatives", len(alt_rows))
