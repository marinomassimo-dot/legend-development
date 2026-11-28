"""ADV-298 screen (IT28, 2026-11-28): count term hits per held full-text file that names WWOX/Wwox. Read-only. Usage: screen_adv298.py > screen_adv298.tsv"""
import re, sys
from pathlib import Path
ROOT = Path("/home/desktop/legend-development/files/fulltext")
TERMS = ["conduction velocity","compound action potential","evoked potential","evoked response","MEP","VEP","ABR","nerve conduction","latency","g-ratio","MBP","myelin basic protein","Olig2","CC1","optic nerve","node of Ranvier","nodal","paranodal","corpus callosum","hypomyelination","myelination"]
EXT = {".xml", ".txt", ".md", ".json", ".html"}
rx = {t: re.compile(r"(?<![A-Za-z0-9])" + re.escape(t) + r"(?![A-Za-z0-9])", re.I) for t in TERMS}
wwox = re.compile(r"wwox", re.I)
print("file\tbytes\twwox_hits\t" + "\t".join(TERMS))
for p in sorted(ROOT.iterdir()):
    files = [p] if p.is_file() else [q for q in p.rglob("*") if q.is_file()]
    for q in files:
        if q.suffix.lower() not in EXT: continue
        try: t = q.read_text(encoding="utf-8", errors="replace")
        except Exception as e: print(f"{q.name}\tUNREADABLE\t{e}"); continue
        w = len(wwox.findall(t))
        if not w: continue
        c = [len(rx[x].findall(t)) for x in TERMS]
        if sum(c) == 0: continue
        print(f"{q.relative_to(ROOT)}\t{len(t)}\t{w}\t" + "\t".join(map(str, c)))
