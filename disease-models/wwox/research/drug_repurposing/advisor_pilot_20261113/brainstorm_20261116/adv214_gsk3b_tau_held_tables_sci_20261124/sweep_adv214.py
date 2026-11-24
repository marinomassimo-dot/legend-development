"""ADV-214 frozen sweep: tabular files in the directories frozen in the PREREG, searched for the frozen gene and site tokens.
Usage: python3 -I sweep_adv214.py FILES_ROOT OUT_TSV"""
import sys, re, zipfile, gzip
from pathlib import Path
root, out = Path(sys.argv[1]), Path(sys.argv[2])
DIRS = ["supplement", "figures", "reach_audit_downloads", "deepening_downloads", "i18_proteome"]
EXT = {".xlsx", ".xls", ".csv", ".tsv", ".txt", ".gz"}
GENES = "GSK3B GSK3A MAPT AKT1 AKT2 AKT3 PPP2CA CDK5 CDK5R1 DYRK1A MAPK8 MAPK9 MAPK10 MAPK1 MAPK3 MAP2K1 MAP2K2 AXIN1 AXIN2 CTNNB1 DPYSL2 MAP1B MAP2".split()
SITES = ["S9", "Y216", "S21", "Y279", "S396", "S404", "S199", "S202", "T205", "T231", "S262", "S422", "S473", "T308", "T514"]
gre = re.compile(r"(?<![A-Za-z0-9])(" + "|".join(GENES) + r")(?![A-Za-z0-9])", re.I)
pre = re.compile(r"phospho|pS9|pY216|p-?Tau|pTau|Ser9|Ser-?9\b|S396|S404", re.I)
def blob(p):
    suf = p.suffix.lower()
    if suf == ".xlsx":
        with zipfile.ZipFile(p) as z:
            return " ".join(z.read(n).decode("utf8", "ignore") for n in z.namelist() if n.endswith(".xml") and ("sharedStrings" in n or "sheet" in n))
    raw = gzip.open(p).read() if suf == ".gz" else p.read_bytes()
    return raw.decode("latin-1") + " " + raw.decode("utf-16le", "ignore")
rows = []
for d in DIRS:
    for p in sorted((root / d).rglob("*")):
        if not p.is_file() or p.suffix.lower() not in EXT:
            continue
        try:
            t = blob(p)
        except Exception as e:
            rows.append([str(p.relative_to(root)), p.stat().st_size, "UNREADABLE", type(e).__name__, ""]); continue
        g = sorted({m.group(1).upper() for m in gre.finditer(t)})
        ph = sorted({m.group(0).lower() for m in pre.finditer(t)})
        wwox = len(re.findall(r"wwox|wox1", t, re.I))
        if g or ph:
            rows.append([str(p.relative_to(root)), p.stat().st_size, ",".join(g), ",".join(ph), wwox])
out.write_text("file\tbytes\tgene_tokens\tphospho_tokens\twwox_mentions\n" + "\n".join("\t".join(map(str, r)) for r in rows) + "\n")
print(len(rows), "files with a hit")
