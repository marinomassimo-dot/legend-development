#!/usr/bin/env python3
"""Same-document selectivity table from relations.tsv (chembl_activity + gtopdb rows): for each declared compound and each
document (ChEMBL document id, or PMID for GtoPdb) with two or more distinct targets carrying a numeric '=' value of one
measure type, list the targets and the ratio max/min. A ratio inside one document is not a selectivity claim across
assays; units are nM; species kept. Reads relations.tsv next to this file; writes selectivity_same_document.tsv."""
import argparse, csv, os, collections
H = os.path.dirname(os.path.abspath(__file__))
def main():
    argparse.ArgumentParser(description=__doc__).parse_args()
    R = list(csv.DictReader(open(os.path.join(H, "relations.tsv")), delimiter="\t"))
    g = collections.defaultdict(list)
    for r in R:
        if r["value_nM"] == "" or r["relation"] not in ("=", ""): continue
        if r["source"] == "chembl_activity":
            if r["target_label"] in ("Unchecked", "NON-PROTEIN TARGET") or not r["gene"]: continue
            doc = r["ref"].split(";")[1]; key = (r["compound"], "chembl:" + doc, r["measure_type"], r["species"])
            g[key].append((r["gene"], r["target_label"], float(r["value_nM"])))
        elif r["source"] == "gtopdb":
            pm = r["ref"].split(";")[0]; key = (r["compound"], "gtopdb:" + pm, r["measure_type"], r["species"])
            g[key].append((r["gene"], r["target_label"], float(r["value_nM"])))
    with open(os.path.join(H, "selectivity_same_document.tsv"), "w") as f:
        f.write("compound\tdocument\tmeasure\tspecies\tn_targets\ttargets_values_nM\tratio_max_over_min\n")
        for k, v in sorted(g.items()):
            t = {}
            for gene, lab, val in v: t.setdefault(gene, []).append(val)
            if len(t) < 2: continue
            vals = [min(x) for x in t.values()]
            f.write("\t".join([k[0], k[1], k[2], k[3], str(len(t)), "; ".join(f"{a}={min(b):.3g}" for a, b in sorted(t.items()))[:400], "%.3g" % (max(vals) / min(vals)) if min(vals) > 0 else ""]) + "\n")
if __name__ == "__main__": main()
