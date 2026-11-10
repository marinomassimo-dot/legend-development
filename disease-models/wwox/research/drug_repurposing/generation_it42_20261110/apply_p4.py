"""IT42 P4: propagate the IT41 corrections to the consumers that still carried the earlier wording. Idempotent; marker [IT42].
 1. INV-05 next_test (both tables): 'same triheteromer ceiling' becomes a per-molecule statement.
 2. comparators.tsv: ifenprodil row (same wording); identity cells of NBQX, GYKI 53655 and perampanel replaced by the Harness identity statements (identity_it41_20261109/identity_table.tsv)."""
import csv, io
from pathlib import Path
R = Path(__file__).resolve().parent.parent; T = "[IT42] "; log = []
OLD = "a second NAM controls chemotype only, same site and same triheteromer ceiling;"
NEW = "a second NAM of the same site controls chemotype only, and only if its own maximum on triheteromers is known (ifenprodil 32 percent, radiprodil 45 percent in rat: each molecule has its own);"
for f in ("ranking_it8_p9_20261029/investigations_it20.tsv", "ranking_it8_p9_20261029/investigations.tsv"):
    s = (R / f).read_text()
    if OLD in s: (R / f).write_text(s.replace(OLD, NEW)); log.append((f, "next_test"))
C = "comparators_it39_20261109/output/comparators.tsv"; rows = list(csv.reader(io.StringIO((R / C).read_text()), delimiter="\t")); h = rows[0]; ix = {k: i for i, k in enumerate(h)}
ID = {"NBQX": "identity: NAME_EXACT, catalogue parent CHEMBL222519, salt not stated (identity_it41_20261109); the evidence level for GRIA1 and GRIA2 is source interaction, not a curated mechanism",
      "GYKI 53655": "identity: DECLARED CHEMBL267450, a different structure from GYKI 52466 (C19H20N4O3 against C17H15N3O2); registries label the two inconsistently, so evidence for one is not evidence for the other (identity_it41_20261109)",
      "perampanel": "identity: NAME_EXACT, CHEMBL1214124, curated mechanism on GRIA1 and GRIA2 (identity_it41_20261109)"}
for r in rows[1:]:
    if r[0] != "INV-05": continue
    if r[1] == "ifenprodil" and "same site, same triheteromer ceiling" in r[ix["what_it_separates"]]:
        r[ix["what_it_separates"]] = r[ix["what_it_separates"]].replace("(same site, same triheteromer ceiling)", "(same site; each molecule has its own maximum on triheteromers, so the ceiling is not assumed to be shared)"); log.append((C, "ifenprodil"))
    if r[1] in ID and " | identity:" in r[ix["target_and_action"]]:
        head = r[ix["target_and_action"]].split(" | identity:")[0]; r[ix["target_and_action"]] = head + " | " + ID[r[1]]; log.append((C, r[1]))
o = io.StringIO(); csv.writer(o, delimiter="\t", lineterminator="\n").writerows(rows); (R / C).write_text(o.getvalue())
for l in log: print(*l)
