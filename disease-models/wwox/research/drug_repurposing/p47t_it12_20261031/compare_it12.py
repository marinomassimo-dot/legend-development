#!/usr/bin/env python3
"""IT12 P2-P47T: side-by-side table P47T (this package, recomputed) | human KO organoid GSE156243 (carried from IT10/IT11 tables) | mouse P17 Wwox deletion (carried from IT10 table).
Usage: compare_it12.py run --genes genes_it12.tsv --it10 DIR_hif_it10_p21 --it10nrf2 organoid_nrf2_rows.tsv --out FILE   (stdlib only; --help prints this)"""
import sys, csv, collections
if len(sys.argv) < 2 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
def arg(n): return sys.argv[sys.argv.index(n) + 1]
P = {}
for r in csv.DictReader(open(arg("--genes")), delimiter="\t"):
    if r["kept_by_expression_filter"] != "": P[(r["gene"], r["region"])] = r
org = {}
for r in csv.DictReader(open(arg("--it10") + "/maturity_stress_check_it10_p21.tsv"), delimiter="\t"):
    org.setdefault(r["gene"].capitalize() if False else r["gene"], r["KO_vs_WT_log2_shift_GSE156243"])
import math
for r in csv.DictReader(open(arg("--it10nrf2")), delimiter="\t"):
    org.setdefault(r["gene"], "%+.2f" % math.log2(float(r["meanKO_over_meanWT_cpm"])))
p17 = collections.defaultdict(dict)
for r in csv.DictReader(open(arg("--it10") + "/mouse_p17_hif_genes_it10_p21.tsv"), delimiter="\t"):
    p17[r["gene"]][r["contrast"]] = r["log2_KO_over_ctl_(+0.1)"] + ("*" if r["animal_separated"] == "yes" else "")
groups = [("HIF_SEL_UP6 (organoid up)", ["Adm", "Bhlhe40", "P4ha1", "Ankrd37", "Ddit4", "Egln3"]),
          ("HIF_FLAT6 (organoid flat)", ["Pgk1", "Aldoa", "Eno1", "Pkm", "Pfkp", "Ndrg1"]),
          ("HIF_OTHER", ["Vegfa"]), ("NRF2_5", ["Nqo1", "Hmox1", "Gclm", "Srxn1", "Txnrd1"]),
          ("IT7_OBS6 (observation only)", ["Slc2a1", "Hk2", "Ldha", "Ldhb", "Bnip3", "Pdk1"]),
          ("regulators (observation)", ["Hif1a", "Epas1", "Egln1", "Egln3", "Nfe2l2", "Keap1"])]
cn = ["Cortex_S_neuron-targeted", "H_S_neuron-targeted", "H_N_progenitor-targeted", "H_germline_null"]
hdr = ["group", "gene", "P47T_HPC_log2FC(p)", "P47T_CTX", "P47T_PFC", "P47T_CB", "organoid_KO_vs_WT_log2 (4v2)"] + ["P17_" + c + "_log2(*=animal-separated)" for c in cn]
out = [hdr]
for gname, genes in groups:
    for g in genes:
        row = [gname, g]
        for reg in ["HPC", "CTX", "PFC", "CB"]:
            r = P.get((g, reg))
            row.append("NA" if r is None else "%+.2f (p %.2g)" % (float(r["log2FC_P47T_over_WT"]), float(r["welch_p"])))
        row.append(org.get(g.upper(), "NA"))
        for c in cn: row.append(p17.get(g, {}).get(c, "NA"))
        out.append(row)
with open(arg("--out"), "w", newline="") as fh:
    csv.writer(fh, delimiter="\t", lineterminator="\n").writerows(out)
print("rows", len(out) - 1)
