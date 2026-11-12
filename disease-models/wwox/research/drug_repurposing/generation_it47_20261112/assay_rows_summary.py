"""IT47 P2: a mechanical consumer for the SCI46 value table (keap1_nrf2_sci46_20261111/engine/assay_rows.tsv, 57 rows): per compound role, how many value rows are in neural cells, which of them have an NRF2-loss arm,
and whether the loss was verified; it checks the prose statements the dashboard carries ("no source has the binder in primary neurons or astrocytes with an NRF2-loss arm"). Rows tagged [CH]
(database copies) are counted apart and never raise a tier.  python3 assay_rows_summary.py -> assay_rows_summary_it47.tsv"""
import csv, re
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent
csv.field_size_limit(10**9)
SRC = DR / "keap1_nrf2_sci46_20261111/engine/assay_rows.tsv"
NEURAL = re.compile(r"neuron|neuronal|luhmes|cortical|hipsc|dopaminergic|sh-sy5y|hippocamp|cerebell|brain", re.I)
ASTRO = re.compile(r"astrocyt", re.I)
MICRO = re.compile(r"microgli|n9|bv-?2", re.I)


def klass(cell, species):
    c = cell or ""
    if ASTRO.search(c): return "astrocyte"
    if NEURAL.search(c) and not MICRO.search(c): return "neuron_or_brain"
    if MICRO.search(c): return "microglia"
    return "non_neural"


def build():
    rows = list(csv.DictReader(open(SRC, encoding="utf-8"), delimiter="\t")); out = []
    for r in rows:
        k = klass(r["cell_or_tissue"], r["species"]); arm = r["nrf2_loss_arm"].lower()
        has_arm = not (arm.startswith("none") or arm == "")
        out.append(dict(row_id=r["row_id"], compound_or_tool=r["compound_or_tool"], role=r["role"], cell_class=k, cell=r["cell_or_tissue"], loss_arm=r["nrf2_loss_arm"], loss_arm_present="yes" if has_arm else "no",
                        loss_verified=r["nrf2_loss_verified"], database_copy="yes" if r["kind"].strip() == "[CH]" else "no", depth=r["depth"], readout_class=r["readout_class"]))
    return out


def summary(out):
    by = defaultdict(Counter)
    for r in out:
        key = (r["role"], r["cell_class"])
        by[key]["rows"] += 1
        by[key]["with_loss_arm"] += r["loss_arm_present"] == "yes"
        by[key]["loss_verified_yes"] += r["loss_verified"].lower().startswith("yes")
        by[key]["database_copy"] += r["database_copy"] == "yes"
    return by


if __name__ == "__main__":
    out = build()
    with open(HERE / "assay_rows_it47.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, list(out[0].keys()), delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(out)
    by = summary(out)
    with open(HERE / "assay_rows_summary_it47.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["role", "cell_class", "rows", "with_loss_arm", "loss_verified_yes", "database_copy"])
        for (role, cls), c in sorted(by.items()):
            w.writerow([role, cls, c["rows"], c["with_loss_arm"], c["loss_verified_yes"], c["database_copy"]])
    print(len(out), "rows")
    for (role, cls), c in sorted(by.items()): print(role, cls, dict(c))
