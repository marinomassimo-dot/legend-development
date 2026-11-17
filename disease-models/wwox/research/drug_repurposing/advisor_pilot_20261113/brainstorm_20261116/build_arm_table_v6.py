"""Build ideas_arm_table_v6 from v5: add a unique cell_id and a table_origin column for duplicated keys.

Reads v5 and SCI's transfer table; refuses (AssertionError) when cell_id is not unique or an origin_row id
is missing from the transfer table. Run from the repository root.
"""
import csv, collections

B = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
rows = list(csv.reader(open(B + "ideas_arm_table_v5_20261117.tsv"), delimiter="\t"))
tq = list(csv.DictReader(open(B + "deepening_sci_20261116/TRANSFER_QUALIFICATION_SCI_20261117.tsv"), delimiter="\t"))
tq_ids = {r["reading_id"] for r in tq}
head = rows[0]
dups = {k for k, n in collections.Counter((r[0], r[1]) for r in rows[1:]).items() if n > 1}
out = [["cell_id"] + head + ["table_origin"]]
for i, r in enumerate(rows[1:], 1):
    note = r[6]
    t = ""
    if (r[0], r[1]) in dups:
        t = "v1_table" if "U1 v1 table" in note else ("v3_table" if "U1 v3" in note else "unclear")
    out.append(["C%03d" % i] + r + [t])
ids = [r[0] for r in out[1:]]
assert len(ids) == len(set(ids)), "cell_id not unique"
for r in out[1:]:
    oc = r[head.index("origin_row") + 1]
    if oc != "none":
        for x in oc.split(";"):
            assert x in tq_ids, "origin_row id %s not in the transfer table" % x
assert all(len(r) == len(out[0]) for r in out)
with open(B + "ideas_arm_table_v6_20261117.tsv", "w", newline="") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
print("cells", len(out) - 1, "duplicated keys", sorted(dups), "table_origin", collections.Counter(r[-1] for r in out[1:]))
