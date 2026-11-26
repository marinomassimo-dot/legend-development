"""IT28: apply edits_287ext_it28.py (fragment replacements) to the card packets; rebuild cards afterwards with repurposing_bridge.py. Idempotent; --dry writes nothing. Run from the repository root."""
import importlib.util, json, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
DR = Path("disease-models/wwox/research/drug_repurposing")
spec = importlib.util.spec_from_file_location("e", HERE / "edits_287ext_it28.py"); E = importlib.util.module_from_spec(spec); spec.loader.exec_module(E)
def j(s): return json.dumps(s, ensure_ascii=False)[1:-1]
def locate(packet, where):
    """return (container, key) so that container[key] is the string field"""
    if not where.startswith("P:"):
        i, field = where.split(":")
        for k in ("drug_assertions", "disease_assertions"):
            for a in packet.get(k, []):
                if a["id"] == i: return a, field
        raise SystemExit("no assertion " + i)
    cur = packet; parts = where[2:].split(".")
    cont, key = None, None
    for n, part in enumerate(parts):
        m = re.fullmatch(r"([A-Za-z0-9_]+)\[(.+)\]", part)
        name, idx = (m.group(1), m.group(2)) if m else (part, None)
        cont, key = cur, name; cur = cur[name]
        if idx is not None:
            if idx.isdigit(): cont, key = cur, int(idx); cur = cur[int(idx)]
            else:
                a = next(x for x in cur if x["id"] == idx); cur = a; cont, key = None, None
    return cont, key
def run(dry):
    by = {}
    for x in E.X: by.setdefault(x["card"], []).append(x)
    n = 0
    for card, items in by.items():
        p = DR / f"cards/{card}.packet.json"; raw = p.read_text(encoding="utf-8"); before = raw
        for x in items:
            packet = json.loads(raw); cont, key = locate(packet, x["where"]); old = cont[key]
            if x["new"] in old: print("  already", x["tag"]); continue
            if old.count(x["old"]) != 1: raise SystemExit(f"FRAGMENT COUNT {old.count(x['old'])} for {x['tag']} in {card}: {x['old'][:50]}")
            new = old.replace(x["old"], x["new"], 1); occ = raw.count(j(old))
            if occ < 1: raise SystemExit("NO RAW MATCH " + x["tag"])
            raw = raw.replace(j(old), j(new)); n += 1
            print(f"  {x['tag']}: {card} field occurrences {occ}")
        json.loads(raw)
        if raw != before and not dry: p.write_text(raw, encoding="utf-8")
    return n
if __name__ == "__main__":
    print("edits", run("--dry" in sys.argv))
