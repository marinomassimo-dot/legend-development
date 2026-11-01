"""IT15 Q-B step 2: build relations_qb.tsv rows (selectivity_p6 format) for the target-first census, and the per-compound census.
Reads raw JSON from --raw (scratchpad). Units normalised to nM only for nM/uM/mM/pM; others kept without value."""
import json, glob, os, sys, collections, csv, argparse
H = os.path.dirname(os.path.abspath(__file__))
GENE = {"CHEMBL262": ("GSK3B", "Homo sapiens"), "CHEMBL2850": ("GSK3A", "Homo sapiens"), "CHEMBL3669": ("Gsk3b", "Rattus norvegicus"),
        "CHEMBL1075321": ("Gsk3b", "Mus musculus"), "CHEMBL1075224": ("Gsk3a", "Rattus norvegicus"), "CHEMBL2176843": ("Gsk3a", "Mus musculus")}
LAB = {"CHEMBL262": "Glycogen synthase kinase-3 beta", "CHEMBL2850": "Glycogen synthase kinase-3 alpha", "CHEMBL3669": "Glycogen synthase kinase-3 beta",
       "CHEMBL1075321": "Glycogen synthase kinase-3 beta", "CHEMBL1075224": "Glycogen synthase kinase-3 alpha", "CHEMBL2176843": "Glycogen synthase kinase-3 alpha"}
UNIT = {"nM": 1.0, "uM": 1e3, "mM": 1e6, "pM": 1e-3, "M": 1e9}
def load(raw):
    rows = []
    for f in sorted(glob.glob(os.path.join(raw, "acts*_CHEMBL*.json"))):
        d = json.load(open(f)); rows += d["rows"]
    # dedupe by activity_id (the 7000/429 split and the small-page rerun are disjoint, but be safe)
    seen, out = set(), []
    for r in rows:
        if r["activity_id"] in seen: continue
        seen.add(r["activity_id"]); out.append(r)
    return out
def val(r):
    u = r.get("standard_units"); v = r.get("standard_value")
    if v in (None, "") or u not in UNIT: return None
    return float(v) * UNIT[u]
if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--raw", required=True); a = ap.parse_args()
    rows = load(a.raw)
    print("rows", len(rows), collections.Counter(r["target_chembl_id"] for r in rows))
    json.dump(rows, open(os.path.join(a.raw, "census_rows.json"), "w"))
    # per compound
    comp = collections.defaultdict(lambda: {"name": set(), "docs": collections.defaultdict(set), "n": 0})
    for r in rows:
        c = r["molecule_chembl_id"]; comp[c]["name"].add(r.get("molecule_pref_name") or ""); comp[c]["n"] += 1
        comp[c]["docs"][r["document_chembl_id"]].add(GENE[r["target_chembl_id"]][0] + "/" + GENE[r["target_chembl_id"]][1][:3])
    both = {c for c, d in comp.items() if any({"GSK3B/Hom", "GSK3A/Hom"} <= g for g in d["docs"].values())}
    print("compounds", len(comp), "with GSK3B+GSK3A same document (human):", len(both))
    named = [(c, sorted(n for n in v["name"] if n)) for c, v in comp.items() if any(n for n in v["name"])]
    print("with pref_name", len(named))
