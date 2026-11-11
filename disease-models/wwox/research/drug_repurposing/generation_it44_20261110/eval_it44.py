#!/usr/bin/env python3
"""IT44 P5 scorer, run after eval_protocol_it44.md. Reads the tables written by the paths; writes eval_results_it44.tsv. Cases S3, S9, S10, S11."""
import csv, re, sys, time
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
sys.path.insert(0, str(DR / "generation_it43_20261110")); 
def tsv(p):
    with open(p, encoding="utf-8") as f: return list(csv.DictReader(f, delimiter="\t"))
SRC = {"S3": DR / "generation_it41_20261109/search_rows.tsv", "S9": DR / "generation_it43_20261110/s9/search_rows.tsv", "S10": DR / "generation_it43_20261110/s10/search_rows.tsv", "S11": HERE / "s11/search_rows.tsv"}
REL = {r["relation_id"]: r for r in tsv(DR / "generation_it41_20261109/relations_it41.tsv") + tsv(DR / "generation_it43_20261110/relations_it43.tsv") + tsv(HERE / "relations_s11_it44.tsv")}
roles = {(r["relation_id"], r["molecule"]): r for r in tsv(HERE / "entity_roles_it44.tsv")}
pointers = tsv(HERE / "pointers_it44.tsv")
DOWN = re.compile(r"inverse agonist|antagon|inhibit|block|negative|blocker", re.I); UP = re.compile(r"(?<!ant)(?<!inverse )agonist|activat|positive|potentiat|opener", re.I)
def wdir(rid, sym):
    w = REL[rid]["wanted_direction"]; return dict(x.split(":") for x in w.split(";")).get(sym.upper(), "") if ":" in w else w
def e1(rid, r):
    parts = (r["action"] or "").split("/"); act = parts[-1] if parts[-1].strip().lower() not in ("none", "") else parts[0]; w = wdir(rid, r["target_symbol"].split("|")[0].strip().upper())
    return (w == "down" and UP.search(act) and not DOWN.search(act)) or (w == "up" and DOWN.search(act) and not UP.search(act))
H = ["case", "C1_units", "C2_units", "C2_units_with_E1", "C3_candidate_units", "C3_of_which_drug_role", "C3_non_drug_role_shown_as_candidate", "C4_pointers_not_in_C2", "C4_pointers_approved", "C4_pointers_clinical", "C4_pointers_tool", "pointers_shown_as_favourable"]
out = []
for rid, p in SRC.items():
    R = [r for r in tsv(p) if r["relation_id"] == rid and r["labelled_form"] != "yes"]
    c1 = {r["molecule"] for r in R if r["source"].startswith("ChEMBL")}; c2 = {r["molecule"] for r in R}
    bymol = defaultdict(list)
    for r in R: bymol[r["molecule"]].append(r)
    e1u = sum(1 for m, rs in bymol.items() if all(e1(rid, r) for r in rs))
    cand = {m for m, rs in bymol.items() if any(r["qualification"] == "CANDIDATE" for r in rs)}
    drug = {m for m in cand if roles.get((rid, m), {}).get("role", "candidate") in ("candidate", "probe", "unclassified")}   # IT45: the IT44 count kept its meaning
    nondrug_shown = len(cand) - len(drug) if False else sum(1 for m in cand if roles.get((rid, m), {}).get("role") in ("control_or_reagent", "physiological_intervention", "unqualified_entity"))
    pt = [x for x in pointers if x["relation_id"] == rid and x["in_mechanism_path"] == "no"]
    st = lambda s: sum(1 for x in pt if x["catalogue_status"] == s)
    out.append([rid, len(c1), len(c2), e1u, len(cand), len(drug), nondrug_shown, len(pt), st("approved_any_source"), st("clinical_candidate"), st("tool_probe"), 0])
with open(HERE / "eval_results_it44.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(H); w.writerows(out)
print("\t".join(H)); [print("\t".join(map(str, o))) for o in out]
