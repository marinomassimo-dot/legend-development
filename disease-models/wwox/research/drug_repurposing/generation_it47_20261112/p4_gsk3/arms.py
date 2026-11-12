"""IT47 P4: arm 1 (simple target search) and the catalogue reference for the named tools, computed mechanically from the local catalogue. python3 arms.py -> arms_it47.tsv and a printed summary."""
import ast, csv, gzip, json, re
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parents[1]
SYMS = {"GSK3B", "GSK3A", "IMPA1", "IMPA2", "EIF2B1", "EIF2B2", "EIF2B3", "EIF2B4", "EIF2B5"}
TOOLS = ["LY-2090314", "CHIR-99021", "laduviglusib", "TDZD-8", "SB-216763", "SB-415286", "ISRIB", "lithium chloride", "lithium carbonate", "lithium"]
by_sym = {s: {} for s in SYMS}; tool_hits = {t: [] for t in TOOLS}
with gzip.open(DR / "catalog/catalog.jsonl.gz", "rt") as f:
    for line in f:
        e = json.loads(line)
        names = [e.get("name", "")] + list(e.get("synonyms") or [])
        low = [str(n).lower() for n in names]
        for t in TOOLS:
            if any(t.lower() == n or (t.lower() == "lithium" and n.startswith("lithium")) for n in low):
                tool_hits[t].append((e["id"], e.get("name"), e.get("modality"), e.get("status_class")))
        tg = e.get("targets") or []
        for t in tg:
            for g in (t.get("gene_symbols") or []):
                if g in SYMS:
                    by_sym[g].setdefault(e["id"], (e.get("name"), t.get("action_type"), e.get("status_class"), e.get("modality")))
rows = []
for s, d in sorted(by_sym.items()):
    for mid, (nm, act, st, mod) in d.items():
        rows.append([s, mid, nm, act, st, mod])
with open(HERE / "arms_it47.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["symbol", "catalogue_id", "name", "action_type", "status_class", "modality"]); w.writerows(rows)
for s, d in sorted(by_sym.items()):
    print(s, len(d), dict(Counter(v[1] for v in d.values())))
print("distinct molecules on GSK3A/GSK3B:", len(set(by_sym["GSK3A"]) | set(by_sym["GSK3B"])))
for t, h in tool_hits.items():
    print(t, [(x[1], x[2], x[3]) for x in h][:3])
