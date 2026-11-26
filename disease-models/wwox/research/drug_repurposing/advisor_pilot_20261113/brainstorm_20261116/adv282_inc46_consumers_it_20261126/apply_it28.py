"""IT 2026-11-26 (IT28): applies edits_it28.py to the card packets (cards are rebuilt by repurposing_bridge.py afterwards). Text-level and idempotent:
the old value is read from the packet itself (by assertion id and field), so the old text is never retyped. Run from the repository root.
`--dry` prints match counts and writes nothing. Hypothesis level; nothing here is medical advice."""
import importlib.util, json, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("edits_it28", HERE / "edits_it28.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def j(s): return json.dumps(s, ensure_ascii=False)[1:-1]

def old_value(packet, x):
    if x["id"] == "N02":
        return packet["p4_fields"]["functional_evidence_available"]
    for k in ("drug_assertions", "disease_assertions"):
        for a in packet.get(k, []):
            if a["id"] == x["id"]: return a[x["field"]]
    raise SystemExit("no assertion " + x["id"])

def run(dry):
    total = 0
    by = {}
    for x in E.NEW: by.setdefault(x["card"], []).append(x)
    for card, items in by.items():
        p = DR / f"cards/{card}.packet.json"; raw = p.read_text(encoding="utf-8"); before = raw
        for x in items:
            packet = json.loads(raw); old = old_value(packet, x)
            if old == x["new"]: print(f"  {x['id']}.{x['field']}: already applied"); continue
            o, n = j(old), j(x["new"]); occ = raw.count(o)
            if occ < 1: raise SystemExit(f"NO MATCH {x['id']} {x['field']}")
            raw = raw.replace(o, n); total += occ
            print(f"  {x['id']}.{x['field']} in {card}: occurrences of the old text = {occ}")
        json.loads(raw)
        if raw != before and not dry: p.write_text(raw, encoding="utf-8")
    return total

if __name__ == "__main__":
    dry = "--dry" in sys.argv
    print("replacements", run(dry), "(dry run)" if dry else "")
