#!/usr/bin/env python3
"""Census of the IT10 v4 Q6 disposition table (read only). Usage: engine_q6_census.py [--help]
Writes engine_q6_census.tsv next to this file. Every figure in README section 3 comes from here."""
import csv, collections, re, sys
from pathlib import Path
if len(sys.argv) > 1:
    print(__doc__); sys.exit(0)
HERE = Path(__file__).resolve().parent
SRC = HERE.parent / "generation_it10_p1_20261031" / "results" / "dispositions_Q6.tsv"
rows = list(csv.DictReader(open(SRC, encoding="utf-8"), delimiter="\t"))
out = []
def add(k, v): out.append((k, str(v)))
add("source", SRC.relative_to(HERE.parents[4]).as_posix())
add("rows_total", len(rows))
for (arm, disp), n in sorted(collections.Counter((r["arm"], r["disposition"]) for r in rows).items()):
    add(f"rows[{arm}|{disp}]", n)
add("candidate_rows_with_one_origin", sum(1 for r in rows if r["n_origins"] == "1"))
add("origin_labels", "; ".join(f"{k or '(none)'}={v}" for k, v in collections.Counter(r["origin_note"] for r in rows).items()))
add("distinct_family_ids", len(set(r["family_id"] for r in rows)))
add("it9_states", "; ".join(f"{k or '(none)'}={v}" for k, v in collections.Counter(r["it9_state"] for r in rows).items()))
first = collections.Counter()
for r in rows:
    if r["arm"] in ("opposes", "mimics"):
        m = re.match(r"([A-Z0-9]+) -", r["chain_status"])
        first[(r["arm"], m.group(1) if m else "other")] += 1
for (arm, g), n in first.most_common(12):
    add(f"first_node[{arm}|{g}]", n)
with open(HERE / "engine_q6_census.tsv", "w", encoding="utf-8") as fh:
    fh.write("key\tvalue\n")
    for k, v in out: fh.write(f"{k}\t{v}\n")
print("\n".join(f"{k}\t{v}" for k, v in out))
