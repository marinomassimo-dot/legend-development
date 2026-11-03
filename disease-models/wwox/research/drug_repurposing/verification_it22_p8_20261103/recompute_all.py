#!/usr/bin/env python3
"""Verifier: recompute the attribution state of every proposal row whose family id is a ChEMBL record, from the raw GtoPdb file, with an independent implementation."""
import csv, collections, statistics, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import recompute_attr as ra
P = list(csv.DictReader(open("../generation_it22_p1_20261103/results_p4/proposals_it21.tsv"), delimiter="\t"))
bychembl = collections.defaultdict(set)
for l in ra.LIG:
    if l["ChEMBL ID"]: bychembl[l["ChEMBL ID"]].add(l["Ligand ID"])
bylig = collections.defaultdict(list)
for r in ra.INT: bylig[r["Ligand ID"]].append(r)
def typed_for(lids):
    d = collections.defaultdict(list)
    for lid in lids:
        for r in bylig[lid]:
            g = r["Target Gene Symbol"].upper()
            if not g or "|" in g: continue
            nm = r["Original Affinity Median nm"]
            if nm: nm = float(nm)
            elif r["Affinity Median"]: nm = 10 ** (9 - float(r["Affinity Median"]))
            else: continue
            if nm <= 0: continue
            t = r["Original Affinity Units"]
            if t in ("", "-"):
                a = r["Affinity Units"]; t = a[1:] if a.startswith("p") else a
                if t in ("-", ""): t = "?"
            d[(lid, g, t)].append((nm, (r["Original Affinity Relation"] or "=").strip() or "="))
    out = {}
    for (lid, g, t), v in d.items():
        ex = [x for x in v if x[1] == "="]
        use = ex or v
        e = (statistics.median(x[0] for x in use), "=" if ex else use[0][1])
        cur = out.get((g, t))
        if cur is None or e[0] < cur[0]: out[(g, t)] = e
    return out
def mine(out, main, strict_bounds=True):
    genes = {g for g, t in out}
    if not out: return "NOT_ASSESSABLE", None, None
    if main not in genes: return "UNMEASURED_AT_MAIN_TARGET", None, None
    if len(genes) == 1: return "SINGLE_MEASURED_TARGET", None, None
    folds = collections.defaultdict(list)
    for (g, t), (nm, rel) in out.items():
        if g != main: continue
        for (g2, t2), (nm2, rel2) in out.items():
            if g2 == main or t2 != t: continue
            if rel == "=" and rel2 == "=": ok = "ok"
            elif rel == ">" and rel2 == "=": ok = "lb"
            elif strict_bounds: ok = None
            elif rel in ("=", ">") and rel2 == "<": ok = "lb"       # best-target upper bound: fold can only be larger
            elif rel == "<" and rel2 in ("=", ">"): ok = None
            else: ok = None
            if ok: folds[t].append((nm / nm2, g2, nm, rel, nm2, ok))
    if not folds: return "NOT_COMPARABLE_MEASURES", None, None
    per = {}
    for t, v in folds.items():
        # most potent other target of that type
        per[t] = min(v, key=lambda x: x[4])
    f, g2, nm, rel, nm2, ok = min(per.values(), key=lambda x: x[0])
    if f < 10: s = "ATTRIBUTABLE"
    elif nm <= 100 and ok == "ok": s = "BORDERLINE_POTENT_MAIN_TARGET"
    elif nm <= 1000 and ok == "ok": s = "SECONDARY_ACTIVITY_MEASURED"
    else: s = "WEAK_ATTRIBUTION"
    return s, round(f, 1), g2
rows = []
mism = collections.Counter(); details = []
for r in P:
    fid = r["family_id"]
    lids = set()
    if fid.startswith("FAM:CAT:CHEMBL"):
        lids = bychembl.get(fid.split(":")[-1], set())
    st_mine, f, g2 = ("NOT_ASSESSABLE", None, None) if not lids else mine(typed_for(lids), r["main_target"].upper())
    st_mine2 = st_mine if not lids else mine(typed_for(lids), r["main_target"].upper(), strict_bounds=False)[0]
    rows.append((r["proposal_id"], r["compound"], r["main_target"], r["attribution_state"], st_mine, st_mine2, f, r["attribution_fold"]))
    if r["attribution_state"] != st_mine:
        mism[(r["attribution_state"], st_mine)] += 1; details.append(rows[-1])
print(len(rows), "rows;", sum(1 for x in rows if x[3] == x[4]), "agree with producer (family-by-ChEMBL-id join only; DGIdb twins bridged by the producer are excluded)")
for k, v in mism.most_common(): print(v, k)
print("rows where relaxed bound rule changes state:")
for x in rows:
    if x[4] != x[5]: print("  ", x)
with open("recomputations_all_rows.tsv", "w") as fh:
    fh.write("proposal_id\tcompound\tmain_target\tproducer_state\tverifier_state_strict_bounds\tverifier_state_bound_aware\tverifier_fold\tproducer_fold\n")
    for x in rows: fh.write("\t".join("" if v is None else str(v) for v in x) + "\n")
print("details of disagreements (non-NOT_ASSESSABLE):")
for d in details:
    if d[4] != "NOT_ASSESSABLE" and d[3] != "NOT_ASSESSABLE": print(d)
