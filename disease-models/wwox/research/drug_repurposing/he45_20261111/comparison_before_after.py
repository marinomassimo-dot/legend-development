#!/usr/bin/env python3
"""HE45 H1: comparison_state of every compound of five comparison packages, by the engine before HE45 and by the engine now.

The inputs (decisive / comparison / new_measurements tables, compound_view) are read from one git ref, the earlier engine from another, so the table can be reproduced:

    python3 comparison_before_after.py --input-ref 8edf3852 --old-ref 3f8f17fb > comparison_before_after.tsv
"""
import argparse, csv, io, subprocess, sys, types
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
DR = "disease-models/wwox/research/drug_repurposing/"
ENGINE = DR + "generation_it43_20261110/comparison_engine.py"
PACKAGES = {"ro25_6981_sci44_20261110/output": "INV-05", "pdh_pdk_sci44_20261110/engine": "INV-07", "nmda_composition_discrim_20261109/output": "INV-05",
            "glun2b_comparators_sci42_20261110/output": "INV-05", "ampa_comparison_it41_20261109/output": "INV-05"}
sys.path.insert(0, str(REPO / "framework/scripts"))


def show(ref, path):
    return subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{path}"], capture_output=True, text=True).stdout


def tsv(ref, path):
    return list(csv.DictReader(io.StringIO(show(ref, path)), delimiter="\t"))


def engine(name, code):
    code = code.replace("HERE = Path(__file__).resolve().parent; DR = HERE.parent", f"HERE = Path('{REPO / DR}generation_it43_20261110'); DR = HERE.parent")
    mod = types.ModuleType(name)
    mod.__file__ = str(REPO / "x.py")
    exec(compile(code, name, "exec"), mod.__dict__)
    return mod


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--input-ref", default="HEAD")
    ap.add_argument("--old-ref", required=True)
    a = ap.parse_args()
    old = engine("ce_old", show(a.old_ref, ENGINE))
    new = engine("ce_new", (REPO / ENGINE).read_text(encoding="utf-8"))
    items_all = tsv(a.input_ref, DR + "generation_it41_20261109/compound_view.tsv")
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["package", "inv", "item_id", "compound", "state_before", "state_after", "reason_after"])
    for folder, inv in PACKAGES.items():
        pkg = {"dec": {r["prop_id"]: r for r in tsv(a.input_ref, DR + folder + "/decisive.tsv")},
               "cmp": {r[next(iter(r))]: r for r in tsv(a.input_ref, DR + folder + "/comparison.tsv")},
               "meas": {r["meas_id"]: r for r in tsv(a.input_ref, DR + folder + "/new_measurements.tsv")}}
        items = [r for r in items_all if r["inv_id"] == inv]
        before = {(r["item_id"], r["name"]): r for r in old.derive(items, pkg, folder)}
        for r in new.derive(items, pkg, folder):
            b = before[(r["item_id"], r["name"])]["comparison_state"]
            out.writerow([folder.split("/")[0], inv, r["item_id"], r["name"], b.split(":")[0], r["comparison_state"].split(":")[0], r["comparison_state"].partition(": ")[2][:300]])


if __name__ == "__main__":
    main()
