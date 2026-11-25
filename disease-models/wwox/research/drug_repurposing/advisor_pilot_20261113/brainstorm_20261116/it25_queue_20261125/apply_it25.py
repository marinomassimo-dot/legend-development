"""IT 2026-11-25 (IT25): applies edits_it25.py to the card packets and to needs/needs.json with the text-level, idempotent machinery of apply_it23.py.
Cards are rebuilt by repurposing_bridge.py afterwards. Run from the repository root. `--dry` reports match counts and writes nothing.
Hypothesis level; nothing here is medical advice."""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
PREV = HERE.parent / "it_adv280_281_238_20261125"
DR = Path("disease-models/wwox/research/drug_repurposing")
def load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
A = load("apply_it23", PREV / "apply_it23.py")
E = load("edits_it25", HERE / "edits_it25.py")

def run(dry):
    by = {}
    for x in E.EDITS: by.setdefault(x["card"], []).append((x["mode"], x["old"], A.units(x["new"]), x["id"]))
    total = 0
    for c, items in by.items():
        p = DR / f"cards/{c}.packet.json"; raw = p.read_text(encoding="utf-8"); before = raw
        for mode, old, new, tag in items:
            occ = raw.count(A.j(old))
            raw, k = A.apply_one(raw, mode, old, new, tag); total += k
            print(f"  {tag} {c}: old string occurrences before = {occ}, replaced = {k}")
        json.loads(raw)
        if raw != before and not dry: p.write_text(raw, encoding="utf-8")
    p = DR / "needs/needs.json"; raw = p.read_text(encoding="utf-8"); before = raw
    for x in E.NEEDS:
        occ = raw.count(A.j(x["old"]))
        raw, k = A.apply_one(raw, x["mode"], x["old"], A.units(x["new"]), x["id"]); total += k
        print(f"  {x['id']} needs.json: old string occurrences before = {occ}, replaced = {k}")
    json.loads(raw)
    if raw != before and not dry: p.write_text(raw, encoding="utf-8")
    return total

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    print("edits", run(dry), "(dry run)" if dry else "")
