#!/usr/bin/env python3
"""IT10 P2.1: offline lookup of each alternative in the compound catalogue (catalog/catalog.jsonl.gz; cache via LEGEND_CATALOG_CACHE).
Writes catalogue_lookup_it10_p21.tsv: the query string, every catalogue row returned (id, name, modality, status, access category, targets, origin).
A name with 0 rows is 'not in the catalogue under that string', not 'absent from the world'."""
import csv, os, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; CAT = HERE.parent / "catalog" / "catalog_build.py"
Q = ["PX-478", "echinomycin", "quinomycin", "acriflavine", "proflavine", "KC7F2", "topotecan", "digoxin", "BAY 87-2243", "belzutifan", "PT2385", "daprodustat", "vadadustat", "molidustat", "enarodustat", "desidustat", "roxadustat", "IOX2", "dimethyloxalylglycine", "DMOG", "N-oxalylglycine"]
rows = []
for q in Q:
    p = subprocess.run([sys.executable, "-I", str(CAT), "query", "--name", q, "--limit", "8"], capture_output=True, text=True, cwd=str(CAT.parent), env=dict(os.environ))
    lines = [l for l in p.stdout.splitlines() if l.strip()]
    n = (p.stderr.strip().splitlines() or [l for l in lines if "match" in l] or ["?"])[0][:40]
    body = [l for l in lines if l.startswith("CAT:")]
    if not body: rows.append([q, n, "", "", "", "", "", "", ""])
    for l in body: rows.append([q, n] + l.split("\t")[:7])
with (HERE / "catalogue_lookup_it10_p21.tsv").open("w", newline="") as h:
    c = csv.writer(h, delimiter="\t"); c.writerow(["query", "catalogue_answer", "catalogue_id", "name", "modality", "status", "access_category", "targets", "origin"]); c.writerows(rows)
for r in rows: print("\t".join(r))
