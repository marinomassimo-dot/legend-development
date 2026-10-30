#!/usr/bin/env python3
"""Reserved-row check (Amendment 3): relation between P1 reserved (held-out) rows and the engine's seed sets and proposals. Descriptive; feeds nothing back.

  reserved_check.py --p1 DIR --seeds-dir DIR --actions DIR --results DIR --out FILE.tsv
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import argparse, csv, glob, gzip, os, collections
ap = argparse.ArgumentParser()
for k in ("p1", "seeds_dir", "actions", "results", "out"): ap.add_argument("--" + k.replace("_", "-"), required=True)
a = ap.parse_args()
rd = lambda p: list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
res = [r for r in rd(os.path.join(a.p1, "seeds.tsv")) if r["reserved_for_evaluation"] == "yes"]
resgenes = sorted({r["entity_symbol"] for r in res if r["entity_symbol"] and r["entity_type"] in ("gene", "protein")})
resids = {r["seed_id"] for r in res}
anyt = collections.defaultdict(set)
for r in csv.DictReader(gzip.open(os.path.join(a.actions, "family_targets_any.tsv.gz"), "rt"), delimiter="\t"): anyt[r["target_symbol"].upper()].add(r["family_id"])
out = [["seed_set", "reserved_gene", "gene_is_a_seed_in_this_set", "reserved_row_ids_in_seed_table", "families_with_any_action_on_gene", "families_in_proposals", "best_rank_by_Z_ind_robust", "of_proposals", "families_that_are_direct_hits"]]
for f in sorted(glob.glob(os.path.join(a.seeds_dir, "*.tsv"))):
    if f.endswith("manifest.tsv"): continue
    sd = rd(f); sn = os.path.basename(f)[:-4]
    genes = set()
    for r in sd:
        genes |= set(x for x in r["members"].split(";") if x) if r["kind"] == "process" else {r["gene"]}
    inseed = [r["seed_id"] for r in sd if any(i in r["source_ref"] for i in resids)]
    prop = list(csv.DictReader(gzip.open(os.path.join(a.results, f"proposals_p1_{sn}.tsv.gz"), "rt"), delimiter="\t"))
    rank = {r["family_id"]: i + 1 for i, r in enumerate(prop)}
    for g in resgenes:
        fams = anyt.get(g.upper(), set()); inp = [rank[x] for x in fams if x in rank]
        dh = sum(1 for r in prop if r["family_id"] in fams and float(r["Q_direct"]) != 0)
        out.append([sn, g, g.upper() in genes, ";".join(inseed) or "none", len(fams), len(inp), min(inp) if inp else "", len(prop), dh])
with open(a.out, "w", encoding="utf-8", newline="") as fh: csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(out)
print(len(out) - 1, "rows ->", a.out)
