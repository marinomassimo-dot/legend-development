#!/usr/bin/env python3
"""Reach audit: later-age purified neuron table (Cahoy 2008, GSE9566, GPL1261 Affymetrix MOE430 2.0; neurons P7, P16, P26; astrocytes P7, P8, P17).

    python3 reach_cahoy.py --help
    python3 reach_cahoy.py run <downloads_dir> <out_tsv>

Reads GSE9566-GPL1261_series_matrix.txt.gz and GPL1261.annot.gz (public GEO downloads, digests in access.tsv). Per gene: mean expression of the best (highest mean) probe
in neurons at P7, P16 and P26 and astrocytes at P7, P8 and P17 (normalised log2-scale values as deposited), differences in log2 units. Microarray, 1 to 4 arrays per group: descriptive only.
"""
import sys
if len(sys.argv) != 4 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, gzip, re, statistics
D = sys.argv[2]
ann = {}; hd = None
for l in gzip.open(f"{D}/GPL1261.annot.gz", "rt", errors="replace"):
    if l[0] in "#^!": continue
    a = l.rstrip("\n").split("\t")
    if hd is None: hd = a; continue
    r = dict(zip(hd, a)); ann[r["ID"]] = r.get("Gene symbol", "")
lines = gzip.open(f"{D}/GSE9566-GPL1261_series_matrix.txt.gz", "rt", errors="replace").read().splitlines()
titles = [x.strip('"') for x in [l for l in lines if l.startswith("!Sample_title")][0].split("\t")[1:]]
i0 = [i for i, l in enumerate(lines) if l.startswith("!series_matrix_table_begin")][0]
hdr = lines[i0 + 1].split("\t"); data = {}
for l in lines[i0 + 2:]:
    if l.startswith("!series_matrix_table_end"): break
    a = l.split("\t"); data[a[0].strip('"')] = [float(x) if x not in ("", "null") else float("nan") for x in a[1:]]
groups = {"Neurons P7": [], "Neurons P16": [], "Neurons P26": [], "Astros P7": [], "Astros P8": [], "Astros P17": []}
for j, t in enumerate(titles):
    for g in groups:
        if t.startswith(g.replace("Neurons P16", "Neurons P16")) and (g != "Neurons P16" or t.startswith("Neurons P16")):
            groups[g].append(j)
GENES = ["Scn1a", "Scn2a", "Scn3a", "Scn8a", "Scn1b", "Scn2b", "Slc6a1", "Slc6a11", "Grin2a", "Grin2b", "Slc12a5", "Slc12a2", "Gabrg2", "Gabra1", "Gabra5", "Nr3c1", "Snap25", "Wwox", "Erbb4", "Adk", "Adora1", "Srr"]
rows = []
for g in GENES:
    probes = [p for p, s in ann.items() if g.lower() in [x.strip().lower() for x in re.split("///|;", s)] and p in data]
    if not probes: rows.append((g, "no probe", *(["no probe"] * len(groups)))); continue
    best = max(probes, key=lambda p: statistics.mean(x for x in data[p] if x == x))
    out = [g, best]
    for gr, idx in groups.items():
        v = [data[best][j] for j in idx if data[best][j] == data[best][j]]
        out.append(f"{statistics.mean(v):.2f} (n{len(v)})" if v else "NA")
    rows.append(tuple(out))
with open(sys.argv[3], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["gene", "probe"] + list(groups)); w.writerows(rows)
print({g: len(i) for g, i in groups.items()})
for r in rows: print(r)
