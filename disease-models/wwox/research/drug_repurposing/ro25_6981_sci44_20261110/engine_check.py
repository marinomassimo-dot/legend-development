"""SCI44 package B: does the existing comparison engine re-derive the role of Ro 25-6981 from the new inputs with no hand-written exception?
Runs the engine's own `derive` and `merge` (generation_it43_20261110/comparison_engine.py) read-only on the compound-view items of INV-05, first with the registered INV-05 comparison packages only (before), then with this package added (after). Writes engine_check.tsv.
  python3 engine_check.py"""
import csv, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent; ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT / "framework/scripts")); sys.path.insert(0, str(DR / "generation_it43_20261110"))
import hypothesis_package as hp, comparison_engine as ce
def main():
    items = [r for r in csv.DictReader(open(DR / "generation_it41_20261109/compound_view.tsv", encoding="utf-8"), delimiter="\t") if r["inv_id"] == "INV-05"]
    reg = [p for p in hp.load_all() if p.get("role") == "pharmacological_comparison" and p.get("inv_id") == "INV-05"]
    mine = hp.load_comparison(HERE / "output")
    before = ce.merge([r for p in reg for r in ce.derive(items, p, p["dir"].parent.name.split("_")[0])])
    after = ce.merge([r for p in reg + [mine] for r in ce.derive(items, p, "sci44b" if p is mine else p["dir"].parent.name.split("_")[0])])
    B = {(r["item_id"], r["name"]): r for r in before}
    out = []
    for r in after:
        b = B.get((r["item_id"], r["name"]), {})
        if b.get("evidence_tier") != r["evidence_tier"] or b.get("role_derived") != r["role_derived"] or b.get("comparison_state") != r["comparison_state"] or "ro 25" in r["name"].lower():
            out.append([r["item_id"], r["name"], b.get("evidence_tier", ""), r["evidence_tier"], b.get("role_derived", ""), r["role_derived"], b.get("comparison_state", "")[:90], r["comparison_state"][:140], r["tier_props"], r["premise_needed"]])
    with open(HERE / "engine_check.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["item_id", "name", "tier_before", "tier_after", "role_before", "role_after", "state_before", "state_after", "tier_props_after", "premises_after"]); w.writerows(out)
    for o in out: print(o[:8])
if __name__ == "__main__":
    if len(sys.argv) > 1: print(__doc__)
    else: main()
