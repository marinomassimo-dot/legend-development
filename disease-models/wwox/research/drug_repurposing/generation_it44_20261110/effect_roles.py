#!/usr/bin/env python3
"""IT44 P4: what the role vocabulary changes in the shortlists: for each relation, the molecules the engine returns as CANDIDATE by role, and the non-candidate-role molecules that were EXCLUDED but are physiological variables. Writes effect_roles_it44.tsv."""
import csv
from collections import Counter, defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent
rows = list(csv.DictReader(open(HERE / "entity_roles_it44.tsv", encoding="utf-8"), delimiter="\t")); by = defaultdict(Counter); vis = defaultdict(list)
for r in rows:
    if "CANDIDATE" in r["engine_verdicts"].split(";"): by[r["relation_id"]][r["role"]] += 1
    elif r["role"] == "physiological_intervention": vis[r["relation_id"]].append(r["name"])
with open(HERE / "effect_roles_it44.tsv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["relation_id", "engine_candidates", "of_which_drug_candidate", "shown_as_probe", "shown_as_reagent_or_control", "shown_as_physiological", "excluded_but_physiological_variable"])
    for rid in sorted(by, key=lambda s: int(s[1:])):
        c = by[rid]; w.writerow([rid, sum(c.values()), c["candidate"], c["probe"], c["control_or_reagent"], c["physiological_intervention"], "; ".join(vis[rid])])
print(open(HERE / "effect_roles_it44.tsv").read())
