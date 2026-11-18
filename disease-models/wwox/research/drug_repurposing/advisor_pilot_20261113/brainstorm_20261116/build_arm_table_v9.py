"""Build ideas_arm_table_v9 from v8: add the origin ids that SCI's transfer table revision 5 names by cell_id.

Only the origin_row column may change, and only by ADDING reading ids; every value, sign, status, owner and note of v8 is kept.
Stops (AssertionError) if cell_id is not unique, a cell_id of the transfer table is not in the arm table, an origin id is missing
from the transfer table, an old id would be removed, or any column other than origin_row differs from v8. Run from the repository root.
An origin row is not support: it names a reading, it does not change a sign.
"""
import csv

B = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
rows = list(csv.reader(open(B + "ideas_arm_table_v8_20261117.tsv"), delimiter="\t"))
tq = list(csv.DictReader(open(B + "deepening_sci_20261116/TRANSFER_QUALIFICATION_SCI_20261117.tsv"), delimiter="\t"))
H = rows[0]
ix = {h: i for i, h in enumerate(H)}
tq_ids = {r["reading_id"] for r in tq}
arm_ids = [r[0] for r in rows[1:]]
assert len(arm_ids) == len(set(arm_ids)), "cell_id not unique"
named = {}
for r in tq:
    for c in r["cell_id"].replace(" ", "").split(";"):
        if c.startswith("C"):
            assert c in arm_ids, "cell_id %s of the transfer table is not in the arm table" % c
            named.setdefault(c, [])
            if r["reading_id"] not in named[c]:
                named[c].append(r["reading_id"])
out, changed = [H], []
for r in rows[1:]:
    r = r[:]
    old = [] if r[ix["origin_row"]] == "none" else r[ix["origin_row"]].split(";")
    new = old + [x for x in named.get(r[0], []) if x not in old]
    assert all(x in tq_ids for x in new), "origin id missing from the transfer table in %s" % r[0]
    if new != old:
        changed.append((r[0], r[ix["arm"]][:40], r[ix["idea"]], ";".join(old) or "none", ";".join(new)))
        r[ix["origin_row"]] = ";".join(new)
    out.append(r)
for a, b in zip(rows, out):
    assert len(b) == len(H)
    assert [v for i, v in enumerate(a) if i != ix["origin_row"]] == [v for i, v in enumerate(b) if i != ix["origin_row"]], "a column other than origin_row changed in " + a[0]
    assert set(a[ix["origin_row"]].split(";")) - {"none"} <= set(b[ix["origin_row"]].split(";")), "an old origin id was removed in " + a[0]
with open(B + "ideas_arm_table_v9_20261117.tsv", "w", newline="") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
print("cells", len(out) - 1, "cells whose origin_row gained ids:", len(changed))
for c in changed:
    print(c)
