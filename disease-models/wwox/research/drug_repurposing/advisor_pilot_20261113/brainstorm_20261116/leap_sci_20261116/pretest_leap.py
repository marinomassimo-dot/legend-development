#!/usr/bin/env python3
"""PRESIDIO-014 held-data pre-test: read the committed gene-level mouse tables for a fixed gene list and print what they say.

Reads only: wwox_data_it24_p4_20261104/results/mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv (neuron-targeted deletions,
GSE158681/2; rows exist only where |centred log2 ratio| >= 0.585; n 2 to 4 per arm, descriptive only) and
p47t_all_regions_tested_genes.tsv.gz (P47T hypomorph, independent laboratory, all tested genes). No network, no writes except the
TSV given as the second argument.

Usage: pretest_leap.py REPO_ROOT OUT_TSV
"""
import csv
import gzip
import sys

DR = "disease-models/wwox/research/drug_repurposing/wwox_data_it24_p4_20261104/results/"
GENES = {
    "H1 chloride": ["Slc12a5", "Slc12a2", "Wnk1", "Stk39", "Oxsr1", "Gabra1", "Gabrb2", "Gabrb3", "Gabrg2"],
    "H2 rebound": ["Cacna1g", "Cacna1h", "Cacna1i", "Hcn1", "Hcn2", "Hcn4"],
    "H3 NMDAR": ["Grin1", "Grin2a", "Grin2b", "Grin2c"],
    "H4 activity-dependent": ["Fos", "Arc", "Npas4", "Egr1", "Bdnf"],
    "H5 region/NPY": ["Wwox", "Npy", "Pvalb", "Sst", "Gfap", "Kcnj10", "Atp1a2"],
}


def main(root, out):
    de = list(csv.DictReader(open(root + "/" + DR + "mouse_p17_descriptive_genes_cLFC_ge0.585_separated.tsv"), delimiter="\t"))
    f = gzip.open(root + "/" + DR + "p47t_all_regions_tested_genes.tsv.gz", "rt")
    h = f.readline().rstrip("\n").split("\t")
    p47 = {}
    for l in f:
        r = dict(zip(h, l.rstrip("\n").split("\t")))
        p47[(r["symbol"], r["region"])] = r
    rows = []
    for hyp, gl in GENES.items():
        for g in gl:
            hits = [r for r in de if r["symbol"] == g]
            if not hits:
                rows.append((hyp, g, "neuron-deletion tables", "-", "not among |cLFC|>=0.585 rows (smaller change or filtered)", "", "", ""))
            for r in hits:
                rows.append((hyp, g, "neuron-deletion " + r["contrast"], r["direction"], f"TPM KO {r['mean_TPM_KO']} v control {r['mean_TPM_control']}",
                             r["centred_log2_ratio"], f"n {r['n_KO']} v {r['n_control']}", "background-confounded" if r["BACKGROUND_CONFOUNDED"] == "1" else ""))
            for rg in ("CTX", "HPC", "PFC"):
                r = p47.get((g, rg))
                if r:
                    rows.append((hyp, g, "P47T " + rg, "up" if float(r["log2FC_centred"]) > 0 else "down", f"WT norm count {float(r['mean_norm_count_WT']):.0f}",
                                 r["log2FC_centred"], f"FDR (no sex term) {float(r['FDR_no_sex']):.2g}; n {r['n_WT']} v {r['n_P47T']}", ""))
    with open(out, "w", newline="") as fo:
        w = csv.writer(fo, delimiter="\t", lineterminator="\n")
        w.writerow(["hypothesis", "gene", "table", "direction", "values", "centred_log2_ratio", "n_or_FDR", "flag"])
        w.writerows(rows)
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2)
    sys.exit(main(sys.argv[1], sys.argv[2]))
