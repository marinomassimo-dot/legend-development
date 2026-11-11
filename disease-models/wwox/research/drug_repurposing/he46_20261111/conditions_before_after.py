#!/usr/bin/env python3
"""HE46 H1: comparison_state of every compound of the five comparison packages with the conditions reader before and after pH/temperature.

Same inputs for both runs (one git ref); only framework/scripts/assay_conditions.py differs (--old-ref names the earlier one, the working tree is the new one).
Writes one row per (package, compound) and, for the pairs whose state changed, one row per pair with the reasons.

    python3 conditions_before_after.py --old-ref 142f6c5f > conditions_before_after.tsv
"""
import argparse, csv, io, subprocess, sys, types
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
DR = "disease-models/wwox/research/drug_repurposing/"
ENGINE = DR + "generation_it43_20261110/comparison_engine.py"
AC = "framework/scripts/assay_conditions.py"
PACKAGES = {"ro25_6981_sci44_20261110": "INV-05", "pdh_pdk_sci44_20261110": "INV-07", "nmda_composition_discrim_20261109": "INV-05", "ampa_comparison_it41_20261109": "INV-05"}  # the registered pharmacological_comparison packages
sys.path.insert(0, str(REPO / "framework/scripts"))
import hypothesis_package as hp  # noqa: E402


def show(ref, path):
    return subprocess.run(["git", "-C", str(REPO), "show", f"{ref}:{path}"], capture_output=True, text=True, check=True).stdout


def tsv(path):
    return list(csv.DictReader(io.StringIO((REPO / path).read_text(encoding="utf-8")), delimiter="\t"))


def load(name, code, file):
    mod = types.ModuleType(name)
    mod.__file__ = str(REPO / file)
    exec(compile(code, name, "exec"), mod.__dict__)
    return mod


def engine_with(ac_code):
    """The engine bound to a given assay_conditions: the module of that name is swapped while the engine imports it."""
    import measurement  # noqa: F401  (the reader imports it)
    saved = sys.modules.get("assay_conditions")
    sys.modules["assay_conditions"] = load("assay_conditions", ac_code, AC)
    code = (REPO / ENGINE).read_text(encoding="utf-8").replace("HERE = Path(__file__).resolve().parent; DR = HERE.parent", f"HERE = Path('{REPO / DR}generation_it43_20261110'); DR = HERE.parent")
    eng = load("ce", code, "x.py")
    if saved is not None:
        sys.modules["assay_conditions"] = saved
    return eng, eng.ac


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--old-ref", required=True)
    a = ap.parse_args()
    old, old_ac = engine_with(show(a.old_ref, AC))
    new, new_ac = engine_with((REPO / AC).read_text(encoding="utf-8"))
    items_all = tsv(DR + "generation_it41_20261109/compound_view.tsv")
    out = csv.writer(sys.stdout, delimiter="\t", lineterminator="\n")
    out.writerow(["package", "inv", "item_id", "compound", "state_before", "state_after", "changed", "reason_after"])
    pairs = []
    for folder, inv in PACKAGES.items():
        pkg = hp.load_comparison(REPO / DR / folder)
        items = [r for r in items_all if r["inv_id"] == inv]
        before = {(r["item_id"], r["name"]): r for r in old.derive(items, pkg, folder)}
        for r in new.derive(items, pkg, folder):
            b = before[(r["item_id"], r["name"])]["comparison_state"]
            out.writerow([folder.split("/")[0], inv, r["item_id"], r["name"], b.split(":")[0], r["comparison_state"].split(":")[0],
                          "CHANGED" if b.split(":")[0] != r["comparison_state"].split(":")[0] else "same", r["comparison_state"].partition(": ")[2][:300]])
    for f in subprocess.run(["git", "-C", str(REPO), "grep", "-l", "species_system_age_prep_exposure_readout", "--", "*decisive.tsv"], capture_output=True, text=True).stdout.split():
        rows = tsv(f)
        cells = {r["prop_id"]: r.get("species_system_age_prep_exposure_readout", "") for r in rows}   # one package at a time: local ids repeat across packages
        ids = sorted(cells)
        for i, x in enumerate(ids):
            for y in ids[i + 1:]:
                o = old_ac.compare(old_ac.parse(cells[x], cells), old_ac.parse(cells[y], cells))["state"]
                n = new_ac.compare(new_ac.parse(cells[x], cells), new_ac.parse(cells[y], cells))
                pairs.append((f.split("/")[-3] if "/output/" in f or "/engine/" in f else f.split("/")[-2], x, y, o, n["state"], "; ".join(n["reasons"])[:200]))
    sys.stderr.write(f"pairs of propositions per package, state before -> after (every pair, not only the pairs the engine uses)\n")
    from collections import Counter
    c = Counter((p[3], p[4]) for p in pairs)
    for k, v in sorted(c.items()):
        sys.stderr.write(f"  {k[0]} -> {k[1]}: {v}\n")
    with open(HERE / "conditions_pairs_before_after.tsv", "w", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["package", "prop_a", "prop_b", "state_before", "state_after", "reasons_after"])
        w.writerows(p for p in pairs if p[3] != p[4])


if __name__ == "__main__":
    main()
