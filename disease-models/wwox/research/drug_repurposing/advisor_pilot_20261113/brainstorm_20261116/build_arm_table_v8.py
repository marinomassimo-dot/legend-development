"""Build ideas_arm_table_v8 from v7: recompute origin_row on SCI's revised transfer table and carry three assumption signs.

Keeps every cell_id of v6. Stops (AssertionError) if cell_id is not unique or an origin_row id is missing from the
transfer table. Old values are kept in the note column. Run from the repository root.
"""
import csv, collections

B = "disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/"
rows = list(csv.reader(open(B + "ideas_arm_table_v7_20261117.tsv"), delimiter="\t"))
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
    a = None
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
with open(B + "ideas_arm_table_v8_20261117.tsv", "w", newline="") as f:
    csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
n = sum(1 for r in out[1:] if r[ix["origin_row"]] != "none")
sg = [(r[0], r[ix["arm"]][:30], r[ix["idea"]]) for r in out[1:] if r[ix["origin_row"]] == "none" and r[ix["value3"]].strip()[:1] in ("+", "-", "0")]
print("cells", len(out) - 1, "with origin", n, "none", len(out) - 1 - n, "signed-none by value3", len(sg), sg)

# origin coverage, computed here and not by hand: by reading, including assumption rows, and by best tier
rt, tier = {}, {}
for r in tq:
    rt.setdefault(r["reading_id"], set()).add(r["row_type"])
    tier[r["reading_id"]] = min(int(tier.get(r["reading_id"], 9)), int(r["tier_cap"]))
body = out[1:]
with_origin = [r for r in body if r[ix["origin_row"]] != "none"]
by_reading = [r for r in with_origin
              if any(t != "assumption" for x in r[ix["origin_row"]].split(";") for t in rt[x])]
best12 = [r for r in by_reading if min(tier[x] for x in r[ix["origin_row"]].split(";") if rt[x] != {"assumption"}) <= 2]
tier3 = [r for r in by_reading if r not in best12]
rows_cov = [("cells", len(body)), ("origin_by_reading", len(by_reading)), ("origin_including_assumption_rows", len(with_origin)),
            ("best_tier_1_or_2", len(best12)), ("tier_3_only", len(tier3)), ("no_origin", len(body) - len(with_origin))]
with open(B + "ORIGIN_COVERAGE_V8_IT_20261117.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["measure", "cells"]); w.writerows(rows_cov)
print(rows_cov)
