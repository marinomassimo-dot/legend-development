"""SCI 2026-11-19 (ADV-085): check the verbatim quotes of the delegate's evidence table against the held texts, and recount the terms and the EV-table rows it reports (a post hoc step).
Every double-quoted segment of at least 22 characters in the report is split at ' ... ' and each piece searched (whitespace and hyphen variants normalised; matching ignores all whitespace because tag stripping inserts spaces around cross-references) in the pooled text of the source files named in the brief.
Run:  python3 -I check_report_sci_20261119.py <report.md>"""
import html
import re
import sys
from pathlib import Path

if len(sys.argv) != 2 or any(a in ("-h", "--help") for a in sys.argv[1:]):
    print(__doc__)
    raise SystemExit(0 if any(a in ("-h", "--help") for a in sys.argv[1:]) else 2)
R = Path(sys.argv[1]).read_text(encoding="utf-8")
FT = Path("/home/desktop/legend-development/files/fulltext")
FILES = ["PMID30290271_Hussain2019_PMC_r2.xml", "PMID34634460_Breton2021_EPMC_2026-09-27.xml", "PMID34268881_Steinberg2021_PMC.xml",
         "PMID42397075_Steinberg2026_OUP-AM_fitz.txt", "PMID36828035_Hussain2023_PMC.xml", "PMID42422765_Obeid2026_PMC_r2.xml",
         "PMID34747138_Repudi2021_PMC_r2.xml", "PMID33914858_Repudi2021_Brain_operator_supplied.txt", "PMID31340538_Tochigi2019_PMC_r2.xml",
         "PMID32000863_Cheng2020_PMC_r2.xml", "PMID34268881_assets/Table_EV1_EV2_derived.txt"]


def norm(s):
    s = s.replace("‐", "-").replace("‑", "-").replace("−", "-").replace("’", "'").replace("‘", "'").replace("“", '"').replace("”", '"')
    return " ".join(s.split())


T = {}
for f in FILES:
    t = (FT / f).read_text(encoding="utf-8", errors="replace")
    t = html.unescape(re.sub(r"<[^>]+>", " ", t))
    T[f] = norm(t)
ALL = " ".join(T.values())
ALLNS = re.sub(r"\s+", "", ALL)
segs = re.findall(r'"([^"\n]{22,})"', R)
bad = 0
for s in segs:
    for piece in re.split(r"\s*\.\.\.\s*", s):
        piece = piece.strip(" .;")
        if len(piece) < 14:
            continue
        ok = re.sub(r"\s+", "", norm(piece)) in ALLNS
        if not ok:
            bad += 1
        print("FOUND    " if ok else "NOT FOUND", piece[:110])
print("quoted pieces not found:", bad)
print()
for f, k in (("PMID30290271_Hussain2019_PMC_r2.xml", "BK5"), ("PMID30290271_Hussain2019_PMC_r2.xml", "Pvalb"), ("PMID30290271_Hussain2019_PMC_r2.xml", "Gad1"),
             ("PMID34634460_Breton2021_EPMC_2026-09-27.xml", "between 3 and 4 postnatal weeks"), ("PMID42397075_Steinberg2026_OUP-AM_fitz.txt", "interneuron"),
             ("PMID42397075_Steinberg2026_OUP-AM_fitz.txt", "inhibitory"), ("PMID42397075_Steinberg2026_OUP-AM_fitz.txt", "18,007"), ("PMID42397075_Steinberg2026_OUP-AM_fitz.txt", "11 neuronal"),
             ("PMID36828035_Hussain2023_PMC.xml", "parvalbumin"), ("PMID36828035_Hussain2023_PMC.xml", "Pvalb"), ("PMID42422765_Obeid2026_PMC_r2.xml", "parvalbumin"),
             ("PMID42422765_Obeid2026_PMC_r2.xml", "inhibitory"), ("PMID34747138_Repudi2021_PMC_r2.xml", "parvalbumin"), ("PMID31340538_Tochigi2019_PMC_r2.xml", "parvalbumin"),
             ("PMID32000863_Cheng2020_PMC_r2.xml", "parvalbumin"), ("PMID34268881_Steinberg2021_PMC.xml", "parvalbumin"), ("PMID34268881_Steinberg2021_PMC.xml", "dorsal identity")):
    print(f"count {f[:34]} '{k}':", len(re.findall(re.escape(k), T[f], flags=re.I)))
print()
rows = [x.rstrip("\n").split("\t") for x in (FT / "PMID34268881_assets/Table_EV1_EV2_derived.txt").read_text(encoding="utf-8").splitlines()]
want = ["GAD1", "SLC32A1", "LHX5", "TAC1", "PNOC", "LAMP5", "SOX6", "MAF", "GABRB2", "GABRB3", "GABRA3", "GABBR2", "NPY", "PVALB", "SST", "VIP", "GAD2", "SLC12A2", "SLC12A5", "LHX6", "DLX1", "DLX2", "DLX5", "DLX6",
        "CALB1", "CALB2", "CALR", "KCNC1", "SLC17A6", "SLC17A7", "GABRA1", "GABRA2", "GABRG2"]
got = {}
for r in rows:
    if len(r) >= 7 and r[0] in ("EV1_up", "EV2_down") and r[2] in want:
        got[r[2]] = (r[0], r[6], r[5])
for g in want:
    print(g.ljust(8), got.get(g, "0 rows"))
