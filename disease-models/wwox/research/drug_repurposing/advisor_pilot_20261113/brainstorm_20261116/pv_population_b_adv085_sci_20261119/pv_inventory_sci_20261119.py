"""SCI 2026-11-19 (ADV-085): inventory of the held full texts (files/fulltext, top level and one sub-level) that mention WWOX at least 15 times and any PV / interneuron / GABAergic term, with counts per term.  Run:  python3 -I pv_inventory_sci_20261119.py"""
import sys
if any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0)
import re
import sys
from pathlib import Path

root = Path("/home/desktop/legend-development/files/fulltext")
TERMS = {
    "parvalbumin|Pvalb": r"parvalbumin|Pvalb|\bPV\+|\bPV-positive|\bPV interneuron|\bPV cell",
    "interneuron": r"interneuron",
    "GAD": r"\bGAD ?6[57]|\bGad[12]\b|\bGAD1\b|\bGAD2\b",
    "perineuronal|WFA": r"perineuronal|\bWFA\b|wisteria",
    "Kv3|Kcnc": r"Kv3|Kcnc[1-4]",
    "SST|calbindin|VIP": r"somatostatin|\bSst\b|calbindin|calretinin|\bVip\b",
    "IPSC": r"IPSC|inhibitory postsynaptic|inhibitory current",
}
rows = []
files = [p for p in list(root.glob("*")) + list(root.glob("*/*")) if p.is_file() and p.suffix.lower() in (".xml", ".txt")]
seen = set()
for p in files:
    try:
        t = p.read_text(encoding="utf-8", errors="replace")
    except Exception:
        continue
    t = re.sub(r"<[^>]+>", " ", t)
    nw = len(re.findall(r"WWOX|Wwox", t))
    if nw < 15:
        continue
    key = (len(t), nw)
    c = {k: len(re.findall(v, t, flags=re.I if k not in ("parvalbumin|Pvalb",) else 0)) for k, v in TERMS.items()}
    if sum(c.values()) == 0:
        continue
    rows.append((p.relative_to(root).as_posix(), nw, len(t), c))
rows.sort(key=lambda r: -r[3]["parvalbumin|Pvalb"])
print("files with >=15 WWOX hits and any PV/interneuron term:", len(rows))
for r in rows[:60]:
    print(r[0][:70].ljust(70), "WWOX", r[1], "| " + " ".join(f"{k.split('|')[0]}={v}" for k, v in r[3].items() if v))
