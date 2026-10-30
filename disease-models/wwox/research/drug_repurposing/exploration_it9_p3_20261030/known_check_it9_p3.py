#!/usr/bin/env python3
"""IT9 P3: is each selected compound known to LEGEND? Names searched (case-insensitive) in cards and packets, needs, the IT8 P9 ranking tables (units, members, queue, uncarded items, selections), the heading lines of the hypothesis ledger,
and, through registry_records.py (never grep), the record-level theme query over the seven indexed registries. Usage: known_check_it9_p3.py --selected selected_stage.tsv --out known_check.tsv (run from the repository checkout)."""
import argparse, csv, glob, re, subprocess, sys
from pathlib import Path
H = Path(__file__).resolve().parent; D = H.parent; REPO = H.parents[4]
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--selected", required=True); ap.add_argument("--out", required=True); a = ap.parse_args()
sel = list(csv.DictReader(open(a.selected), delimiter="\t"))
files = {"card": sorted(glob.glob(str(D / "cards/*.json")) + glob.glob(str(D / "cards_early/*.json")) + [str(D / "join/cards.json")]), "need": [str(D / "needs/needs.json"), str(D / "needs/needs.md")], "ranking": sorted(glob.glob(str(D / "ranking_it8_p9_20261029/*.tsv"))),
         "hypothesis_ledger_headings": [str(REPO / "disease-models/wwox/research/therapeutic_hypotheses_ledger_current.md")]}
txt = {}
for k, fl in files.items():
    for f in fl:
        t = open(f, errors="ignore").read()
        if k == "hypothesis_ledger_headings": t = "\n".join(l for l in t.splitlines() if l.startswith("#"))
        txt[(k, f)] = t.lower()
rows = []
for s in sel:
    names = [s["name"]] + [x for x in (s.get("chembl_name") or "").split("|") if x]
    names = [n.lower() for n in names if len(n) >= 4]
    hit = {}
    for (k, f), t in txt.items():
        if any(re.search(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])", t) for n in names): hit.setdefault(k, []).append(Path(f).name)
    rec = set(); nh = 0; err = ""
    for n in names:
        p = subprocess.run([sys.executable, str(REPO / "framework/scripts/registry_records.py"), "get", "--theme", n, "--hops", "0", "--root", str(REPO)], capture_output=True, text=True)
        if p.returncode != 0: err = "registry_records exit %d" % p.returncode; continue
        m = re.findall(r"hits: (\d+)", p.stdout); nh += sum(int(x) for x in m)
        rec |= set(re.findall(r"^### ([A-Za-z0-9_.-]+(?: —)?)", p.stdout, re.M))
    rows.append([s["parent"], s["name"], ";".join(sorted(hit.get("card", []))), ";".join(sorted(hit.get("need", []))), ";".join(sorted(hit.get("ranking", []))), ";".join(hit.get("hypothesis_ledger_headings", [])) and "yes" or "", nh, ";".join(sorted(rec)).replace(" —", ""), err])
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["parent", "name", "cards_or_packets_naming_it", "needs_files_naming_it", "ranking_tables_naming_it", "hypothesis_ledger_heading_match", "registry_records_theme_hits", "registry_records_headings", "error"]); w.writerows(rows)
