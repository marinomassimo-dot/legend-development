"""Row-level best tier per arm-table cell, from SCI's transfer table keyed by cell_id (revision 4 and later).

A cell's best tier is the minimum tier_cap over the rows of the transfer table that name THAT cell; the older
reading-level figure (minimum over all rows of a reading id, M078) is computed beside it. Stops with an
AssertionError if a cell_id of the transfer table is missing from the arm table or the table has duplicate cell_id.
Run from the repository root.
"""
import csv, collections

B = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
tq = list(csv.DictReader(open(B + "deepening_sci_20261116/TRANSFER_QUALIFICATION_SCI_20261117.tsv"), delimiter="\t"))
arm = list(csv.DictReader(open(B + "ideas_arm_table_v8_20261117.tsv"), delimiter="\t"))
ids = [r["cell_id"] for r in arm]
assert len(ids) == len(set(ids)), "cell_id not unique in the arm table"
rows_by_cell = collections.defaultdict(list)
for r in tq:
    for c in r["cell_id"].replace(" ", "").split(";"):
        if c.startswith("C"):
            assert c in ids, "cell_id %s of the transfer table is not in the arm table" % c
            rows_by_cell[c].append(r)
out = []
for c in ids:
    rs = rows_by_cell.get(c, [])
    if rs:
        best = min(int(r["tier_cap"]) for r in rs)
        out.append((c, best, "+".join(sorted({r["row_type"] for r in rs})), ";".join(sorted({r["reading_id"] for r in rs}))))
with open(B + "ROW_LEVEL_TIER_V8_IT_20261117.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["cell_id", "best_tier_row_level", "row_types", "reading_ids"])
    w.writerows(out)
cnt = collections.Counter(o[1] for o in out)
# reading-level figure (M078 definition): tier of a reading id = minimum over ALL its rows; cell origin from v8 origin_row
rt, tier = {}, {}
for r in tq:
    rt.setdefault(r["reading_id"], set()).add(r["row_type"])
    tier[r["reading_id"]] = min(int(tier.get(r["reading_id"], 9)), int(r["tier_cap"]))
rl12 = rl3 = 0
for r in arm:
    o = r["origin_row"]
    if o == "none":
        continue
    ids_ = [x for x in o.split(";") if rt[x] != {"assumption"}]
    if not ids_:
        continue
    if min(tier[x] for x in ids_) <= 2:
        rl12 += 1
    else:
        rl3 += 1
print("cells with a row naming them:", len(out), "best tier 1:", cnt[1], "2:", cnt[2], "3:", cnt[3],
      "| tier 1 or 2:", cnt[1] + cnt[2], "of", len(arm))
print("reading-level (M078 definition): tier 1 or 2:", rl12, "tier 3 only:", rl3)
