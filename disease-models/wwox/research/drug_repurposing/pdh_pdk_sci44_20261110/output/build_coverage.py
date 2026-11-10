"""SCI44 A5 (in silico, runs now): for each cell class and dataset of isoform_expression.tsv with RNA values for all four kinases, the share of the four-kinase RNA carried by each isoform and, for each tool, the share carried by isoforms with a MEASURED row for that tool (from a3/activity_primary.tsv conclusions, fixed below with the V1 corrections).
A share of RNA is not a share of kinase activity or of PDH restraint; it only says which tool rows a cell class would exercise. Descriptive, INFERENZA. Writes tool_by_cell_coverage.tsv.
  python3 build_coverage.py"""
import csv, sys
from collections import defaultdict
from pathlib import Path
H = Path(__file__).resolve().parent
# measured rows per tool (condition kept): AZD7545 core-bound inhibition PDK1 (87 nM), PDK3 (0.60 uM); PDK4 core-free stimulation only; PDK2 not measured in any source opened (repository 8.19 unverified)
AZD_INHIB = {"PDK1", "PDK3"}; AZD_OTHER = {"PDK2", "PDK4"}
def main():
    rows = [r for r in csv.DictReader(open(H / "isoform_expression.tsv", encoding="utf-8"), delimiter="\t") if r["measure"] == "RNA" and r["gene"] in ("PDK1", "PDK2", "PDK3", "PDK4")]
    g = defaultdict(dict)
    for r in rows:
        key = (r["source_pmid_or_doi"][:40], r["species"].split(" (")[0], r["cell_class"], r["age_stage"], r["unit"].split(" ")[0])
        g[key][r["gene"]] = float(r["value"])
    out = []
    for (src, sp, cc, age, unit), v in sorted(g.items()):
        if set(v) != {"PDK1", "PDK2", "PDK3", "PDK4"}: continue
        t = sum(v.values()); sh = {k: x / t for k, x in v.items()} if t else None
        if not sh: continue
        dom = max(sh, key=sh.get)
        out.append([src, sp, cc, age, unit] + [f"{sh[k]:.2f}" for k in ("PDK1", "PDK2", "PDK3", "PDK4")] + [dom, f"{sum(sh[k] for k in AZD_INHIB):.2f}", f"{sum(sh[k] for k in AZD_OTHER):.2f}", "1.00", "1.00"])
    with open(H / "tool_by_cell_coverage.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["source", "species", "cell_class", "age_stage", "unit", "share_PDK1", "share_PDK2", "share_PDK3", "share_PDK4", "dominant", "AZD7545_share_with_core_bound_inhibition_row (PDK1+PDK3)", "AZD7545_share_without_one (PDK2 unmeasured, PDK4 core-free stimulation only)", "VER-246608_share_with_IC50_row (all four; construct and species unverified)", "DCA_share_with_in_vitro_row (all four; mM; PDK4 core-free only)"])
        w.writerows(out)
    print(len(out), "dataset-class rows")
if __name__ == "__main__":
    if len(sys.argv) > 1: print(__doc__)
    else: main()
