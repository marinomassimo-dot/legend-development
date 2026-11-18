#!/usr/bin/env python3
"""I4: where the HDAC-inhibitor families and valproate sit among the 256 families of the held LINCS-type signature table, and a hypergeometric tail.

    python3 i4_hdac_rank.py --repo <repo root> [--out FILE]

Input (read-only): network_comparison_it7_p3_20261029/results/family_scores.tsv, column O_E (family-level opposition of the WWOX-loss glycolysis/lactate module; positive = moves the module against the loss
direction, negative = with it). POST HOC, stated plainly: the HDAC-inhibitor list was assembled AFTER the ranks of every family whose name ends in -stat had been printed (a name search), and 'bottom 50' was
chosen after that; the tail below is therefore descriptive and optimistic, not a test. List: vorinostat, panobinostat, belinostat, quisinostat, mocetinostat, givinostat, entinostat, abexinostat (absent from the
table: reported as absent). Valproic acid is listed separately (a weak HDAC inhibitor by mechanism label; ASSUMED). Not medical advice.
"""
import argparse, csv
from math import comb
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--repo"); ap.add_argument("--out"); a = ap.parse_args()
if not a.repo:
    ap.print_help(); raise SystemExit(0)
rows = list(csv.DictReader(open(Path(a.repo) / "disease-models/wwox/research/drug_repurposing/network_comparison_it7_p3_20261029/results/family_scores.tsv"), delimiter="\t"))
rows.sort(key=lambda r: (-float(r["O_E"]), r["name"])); N = len(rows); rank = {r["name"]: (i + 1, float(r["O_E"])) for i, r in enumerate(rows)}
HDAC = ["VORINOSTAT", "PANOBINOSTAT LACTATE", "BELINOSTAT", "QUISINOSTAT", "MOCETINOSTAT", "GIVINOSTAT", "ENTINOSTAT", "ABEXINOSTAT"]
present = [h for h in HDAC if h in rank]; BOTTOM = 50
k = sum(rank[h][0] > N - BOTTOM for h in present); K = len(present)
p = sum(comb(BOTTOM, i) * comb(N - BOTTOM, K - i) for i in range(k, K + 1)) / comb(N, K)
lines = ["name\trank_of_" + str(N) + "_descending_O_E\tO_E\tin_bottom_" + str(BOTTOM)]
for h in present + ["VALPROIC ACID"]:
    lines.append(f"{h}\t{rank[h][0]}\t{rank[h][1]:.3f}\t{'yes' if rank[h][0] > N - BOTTOM else 'no'}")
notes = []
notes.append(f"# absent from the table: {', '.join(h for h in HDAC if h not in rank) or 'none'}")
notes.append(f"# {k} of {K} HDAC-inhibitor families are in the bottom {BOTTOM} of {N}; hypergeometric P(at least {k} of {K} in a random bottom-{BOTTOM}) = {p:.2g}")
notes.append("# families are drug classes, not independent draws (one table, one module): the tail is descriptive")
t = "\n".join(lines) + "\n"; nt = "\n".join(notes) + "\n"
if a.out:
    open(a.out, "w").write(t); open(str(a.out).rsplit(".", 1)[0] + "_notes.txt", "w").write(nt)    # comment lines never go inside a TSV (the width test would refuse them)
print(t + nt)
