#!/usr/bin/env python3
"""Per seed set: number of seed genes and of incoming network edges by record mode (T, P, C), i.e. what can physically reach the seeds under each level rule.

  seed_adjacent_edges.py --seeds-dir ../seeds_p1 --out results/seed_in_edges_by_mode.tsv
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import collections, csv, glob, importlib.util, os
from pathlib import Path
HERE = Path(__file__).resolve().parent
_s = list(sys.argv); sys.argv = ["seed_engine_v3.py", "selftest"]
spec = importlib.util.spec_from_file_location("seed_engine_v3", HERE / "seed_engine_v3.py"); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); sys.argv = _s
d = sys.argv[sys.argv.index("--seeds-dir") + 1]; out = sys.argv[sys.argv.index("--out") + 1]
E = m.read_edges3(); inn = collections.defaultdict(collections.Counter)
for s, t, sg, md in E: inn[t][md] += 1
rows = [["seed_set", "readout_level", "seed_genes", "seed_genes_in_network", "in_edges_T", "in_edges_P", "in_edges_C", "genes_with_no_admissible_final_edge", "admissible_final_mode"]]
for f in sorted(glob.glob(os.path.join(d, "*.tsv"))):
    if f.endswith("manifest.tsv"): continue
    sd = list(csv.DictReader(open(f, encoding="utf-8"), delimiter="\t")); genes = set()
    for r in sd: genes |= set(x for x in r["members"].split(";") if x) if r["kind"] == "process" else {r["gene"]}
    genes = {(m.H().canon(g) or g).upper() for g in genes}; lv = sd[0]["readout_level"]; need = "T" if lv == "expression" else "P"
    c = collections.Counter(); none = 0
    for g in genes:
        for k, v in inn.get(g, {}).items(): c[k] += v
        if inn.get(g, {}).get(need, 0) == 0: none += 1
    rows.append([os.path.basename(f)[:-4], lv, len(genes), sum(1 for g in genes if g in inn), c["T"], c["P"], c["C"], none, need])
with open(out, "w", encoding="utf-8", newline="") as fh: csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(rows)
for r in rows: print("\t".join(map(str, r)))
