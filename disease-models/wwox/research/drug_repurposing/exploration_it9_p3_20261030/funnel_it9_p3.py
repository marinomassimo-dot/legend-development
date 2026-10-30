#!/usr/bin/env python3
"""IT9 P3: funnel table per question and arm from the P2 funnel JSONs, per_question_counts and the consolidated selection. Usage: funnel_it9_p3.py --consolidated candidates_consolidated.tsv --out funnel.tsv"""
import argparse, collections, csv, glob, gzip, json, os
from pathlib import Path
D = Path(__file__).resolve().parent.parent; R = D / "generation_it9_p2_20261030/results"
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--consolidated", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
cons = list(csv.DictReader(open(a.consolidated), delimiter="\t"))
pq = {r["seed_set"]: r for r in csv.DictReader(open(R / "per_question_counts.tsv"), delimiter="\t")}
inv = list(csv.DictReader(gzip.open(D / "ranking_it8_p9_20261029/inventory_families.tsv.gz", "rt"), delimiter="\t"))
n_res_usable = sum(1 for r in inv if r["origin"] == "chembl_selected" and r["mnet_usable"] == "yes")
rows = []
cols = ["question", "seed_set", "arm", "catalogued", "identity_resolved(ChEMBL)", "usable_by_method", "usable_AND_identity_resolved(intersection)", "usable_with_gene_symbol", "examined(target_in_graph)", "non_zero", "seed_specific(z>3_or_<-3_both_nulls)", "candidates_taken_to_deepening", "note"]
sets = ["Q1_expression_tiersABC", "Q1_protein_tiersABC", "Q2_expression_tiersAB", "Q3_expression_tiersAB", "Q4_expression_tiersAB", "Q4_protein_tiersAB", "Q5_expression_tiersAB", "Q6_expression_tiersAB", "Q6_protein_tiersAB", "Q7_phospho_tiersAB"]
def taken(sset, arm):
    if sset == "Q6_protein_tiersAB": return "see Q6_expression (same MYC seed, identical proposals)"
    n = 0
    for r in cons:
        if not r["disposition"].startswith("selected"): continue
        if arm == "direct_search": n += int(r["seed_specific"] == "0" and (sset + ":direct_search") in r["sets_arms"].split(";") and r["disposition"] == "selected:reference")
        else: n += int(r["best_set"] == sset and r["direction"] == arm)
    return n
for s in sets:
    f = json.load(open(R / ("funnel_p1_%s.json" % s))); p = pq[s]
    base = [s.split("_")[0], s]
    common = [f["catalogued_families"], f["resolved_identity_families"], f["mnet_usable_families"], n_res_usable, f["mnet_usable_with_a_gene_symbol"], f["examined"]]
    note_all = "usable and resolved are NOT nested: %d families are both (ChEMBL-resolved and usable); %d usable families are DGIdb-only (identity unresolved)" % (n_res_usable, f["mnet_usable_families"] - n_res_usable)
    undef = "UNKNOWN direction for all seeds: no robust proposal possible" if p["Zind_robust_gt3_both_nulls_opposes"] == "0" and p["Zind_robust_lt_minus3_both_nulls_mimics"] == "0" else ""
    rows.append(base + ["NET-IND opposes"] + common + [f["examined_with_nonzero_in_any_arm"], p["Zind_robust_gt3_both_nulls_opposes"], taken(s, "opposes"), (undef + "; " if undef else "") + "non_zero counts families in any arm (not per direction); " + note_all])
    rows.append(base + ["NET-IND mimics"] + common + [f["examined_with_nonzero_in_any_arm"], p["Zind_robust_lt_minus3_both_nulls_mimics"], taken(s, "mimics"), undef])
    rows.append(base + ["DIRECT (any action on a seed gene)"] + common + [f["examined_hit_a_seed_gene_with_any_action"], "n/a (hop 0 search, no null)", taken(s, "direct_search"), "examined_hit_a_seed_gene_with_any_action; seeds are transcript/protein states, a target hit assumes expression direction = activity direction"])
    sg = json.load(open(R / ("sig_p1_%s.json" % s))) if os.path.exists(R / ("sig_p1_%s.json" % s)) else None
    if sg:
        rows.append(base + ["SIGNATURE (LINCS neural-lineage, phase I)", f["catalogued_families"], f["resolved_identity_families"], f["mnet_usable_families"], n_res_usable, "", sg.get("families", ""), "", "not informative" if not (sg.get("Uplus_informative") or sg.get("Uminus_informative")) else "informative", 0, "seed units eligible after guards: %s of %s; families with a signature: %s (28,776 catalogue records have no structure key: UNKNOWN for this arm)" % (sg.get("seed_units_total", 0) - sg.get("seed_units_excluded_by_guard", 0), sg.get("seed_units_total"), sg.get("families"))])
rows.append(["ALL", "-", "method exclusions (global)", 40268, 16475, 13379, n_res_usable, 13307, 12560, "", "", "", "26,889 catalogue records have no usable signed action (UNKNOWN, not inactive); 72 usable families without gene symbol (e.g. RNAi agents); %d usable-with-symbol families have no target in the graph; 28,776 records without structure key (signature arm); 2,381 distinct signed target symbols, 1,887 in the graph (79 percent); 21 percent of target symbols unmapped (alias errors not audited)" % (13307 - 12560)])
tot_pool = sum(1 for r in cons if r["seed_specific"] == "1")
rows.append(["ALL", "-", "consolidated across sets", "", "", "", "", "", "", "", "%d parent compounds seed-specific in at least one set" % tot_pool, sum(1 for r in cons if r["disposition"].startswith("selected")), "parents = families collapsed by ChEMBL parent; Q6 expression and protein are one MYC seed (counted once in the consolidation, twice in this per-set table)"])
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(cols)
    for r in rows: w.writerow([str(x).replace("\t", " ") for x in r])
