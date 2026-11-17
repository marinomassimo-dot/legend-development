"""Build ideas_arm_table_v7 from v6: recompute origin_row on SCI's revised transfer table and carry three assumption signs.

Keeps every cell_id of v6. Stops (AssertionError) if cell_id is not unique or an origin_row id is missing from the
transfer table. Old values are kept in the note column. Run from the repository root.
"""
import csv, collections

B = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
rows = list(csv.reader(open(B + "ideas_arm_table_v6_20261117.tsv"), delimiter="\t"))
tq = list(csv.DictReader(open(B + "deepening_sci_20261116/TRANSFER_QUALIFICATION_SCI_20261117.tsv"), delimiter="\t"))
H = rows[0]
ix = {h: i for i, h in enumerate(H)}
tq_ids = {r["reading_id"] for r in tq}
k = collections.defaultdict(list)
for r in tq:
    for p in r["arm_row_affected"].split(";"):
        p = p.strip()
        if p and r["reading_id"] not in k[p]:
            k[p].append(r["reading_id"])
# the Cacna1g transfer row is now one string for both ideas
ASSUME = {
    ("GABA-A PAM", "I9"): ("qualifier", "qualifier 'only after maturation' is an ASSUMPTION; sign from R17a (simulation, tier 3)"),
    ("GABA-A PAM", "I10"): ("sign", "no held reading: the sign is an ASSUMPTION"),
    ("Remyelination mechanism", "I5"): ("sign", "R08c supports the premise only (tier 2); sign 'rate -' is an ASSUMPTION"),
}
out = [H]
for r in rows[1:]:
    r = r[:]
    arm, idea = r[ix["arm"]], r[ix["idea"]]
    key = arm + "|" + idea
    if arm.startswith("T-type blockade / Cacna1g") and idea == "I1/I10":
        key = "T-type blockade / Cacna1g deletion (transfer)|I1/I10"
    r[ix["origin_row"]] = ";".join(k.get(key, [])) or "none"
    a = ASSUME.get((arm, idea))
    if a:
        old = r[ix["value3"]]
        r[ix["note"]] += " | v7: old value3 '%s'; %s" % (old, a[1])
        if a[0] == "sign":
            r[ix["value3"]] = ". (assumed)"
        else:
            r[ix["status"]] += "; qualifier assumed"
    out.append(r)
ids = [r[0] for r in out[1:]]
assert len(ids) == len(set(ids)), "cell_id not unique"
for r in out[1:]:
    if r[ix["origin_row"]] != "none":
        for x in r[ix["origin_row"]].split(";"):
            assert x in tq_ids, "origin_row id %s not in the transfer table" % x
assert all(len(r) == len(H) for r in out)
with open(B + "ideas_arm_table_v7_20261117.tsv", "w", newline="") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
n = sum(1 for r in out[1:] if r[ix["origin_row"]] != "none")
sg = [(r[0], r[ix["arm"]][:30], r[ix["idea"]]) for r in out[1:] if r[ix["origin_row"]] == "none" and r[ix["value3"]].strip()[:1] in ("+", "-", "0")]
print("cells", len(out) - 1, "with origin", n, "none", len(out) - 1 - n, "signed-none by value3", len(sg), sg)
