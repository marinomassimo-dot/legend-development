"""IT40 P7 part: for the 15 tools the packages name, does the catalogue record found BY NAME carry the target the package means? (The simple baseline stops at 'a record was found'.) Symbols come from the ChEMBL mechanism rows (human) and from the DGIdb gene ids resolved through the HGNC service (dgidb_named_tools.tsv)."""
import csv, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4] / "framework/scripts"))
import compound_catalog as cc, repurposing_search as rs
es = cc.load(cc.DEFAULT_CATALOG); idx = rs.Index(es)
rev = {}
for sym, lst in idx.chembl_human.items():
    for e, t in lst: rev.setdefault(e["id"], set()).add(sym)
dg = {}
for r in csv.DictReader(open(HERE / "dgidb_named_tools.tsv"), delimiter="\t"):
    dg[r["catalogue_id"]] = {x.split("=")[1] for x in r["dgidb_gene_symbols_resolved_from_HGNC_service"].split(";") if "=" in x}
EXPECT = {"d-APV (D-Ap5)": {"GRIN1", "GRIN2A", "GRIN2B"}, "perampanel": {"GRIA1", "GRIA2"}, "NBQX": {"GRIA1", "GRIA2"}, "GYKI 52466": {"GRIA1", "GRIA2"}, "ifenprodil": {"GRIN2B"}, "Ro 25-6981": {"GRIN2B"},
 "radiprodil": {"GRIN2B"}, "TCN-201": {"GRIN2A"}, "memantine": {"GRIN2B", "GRIN2A", "GRIN1"}, "ZD7288": {"HCN1", "HCN2"}, "ivabradine": {"HCN1", "HCN2", "HCN4"}, "retigabine": {"KCNQ2", "KCNQ3"}, "XE991": {"KCNQ2", "KCNQ3"},
 "carbenoxolone": {"GJD2", "GJA1", "PANX1"}, "brilliant blue FCF": {"PANX1"}}
NAME = {"d-APV (D-Ap5)": ["D-Ap5"], "retigabine": ["retigabine", "ezogabine"], "Ro 25-6981": ["Ro 25-6981", "Chembl:Chembl305195"]}
rows = []
for tool, exp in EXPECT.items():
    hits = []
    for n in NAME.get(tool, [tool]): hits += cc.find(es, name=n)
    seen, got, names = set(), set(), []
    for h in hits:
        if h["id"] in seen: continue
        seen.add(h["id"]); got |= rev.get(h["id"], set()) | dg.get(h["id"], set()); names.append(h["name"])
    exact = any(cc._norm(n) == cc._norm(tool) for n in names)
    if not hits: v = "NOT_IN_CATALOGUE"
    elif not (got & exp): v = "RECORD_WITHOUT_THE_INTENDED_TARGET"
    elif not exact and tool not in NAME: v = "NAME_MISMATCH_RECORD_NAMED_" + "|".join(names[:1]) + "_SAME_COMPOUND_UNDETERMINED"
    else: v = "TARGET_CONFIRMED"
    rows.append([tool, v, ";".join(sorted(got & exp)) or "-", ";".join(sorted(exp - got)) or "-", "|".join(names[:2])])
with open(HERE / "identity_check.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["package_name", "verdict", "intended_targets_found", "intended_targets_missing", "record_names"]); w.writerows(rows)
for r in rows: print(*r, sep="\t")
