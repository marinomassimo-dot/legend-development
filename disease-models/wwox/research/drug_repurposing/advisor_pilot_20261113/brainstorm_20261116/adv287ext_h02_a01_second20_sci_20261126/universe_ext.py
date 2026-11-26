"""ADV-287 extension: eligible statements = sentences of the frozen ADV-287 universe (universe_adv287.tsv) that are still
printed verbatim in the same card packet and were not audited before (ADV-287 step 1 sample, ADV-287 step 2 list).
Writes eligible_ext.tsv and counts_ext.tsv next to this file. Run: python3 -P -E universe_ext.py"""
import csv, glob, json, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
B = os.path.dirname(HERE)
CARDS = os.path.normpath(os.path.join(HERE, "../../../cards"))
csv.field_size_limit(10**7)
def rd(p): return list(csv.DictReader(open(p), delimiter="\t", quoting=csv.QUOTE_NONE))
uni = rd(os.path.join(B, "adv287_card_statements_sci_20261125/universe_adv287.tsv"))
s1 = [r for r in rd(os.path.join(B, "adv287_card_statements_sci_20261125/sample_adv287.tsv")) if r["role"].startswith("sample")]
s2 = rd(os.path.join(B, "adv287_step2_marked_statements_sci_20261125/list_adv287_step2.tsv"))
audited = {(r["card"], r["sentence"]) for r in s1}
audited |= {(r.get("card"), r.get("sentence")) for r in s2}
def strings(o):
    if isinstance(o, dict):
        for v in o.values(): yield from strings(v)
    elif isinstance(o, list):
        for v in o: yield from strings(v)
    elif isinstance(o, str): yield o
cur = {}
for f in glob.glob(os.path.join(CARDS, "*.packet.json")):
    cur[os.path.basename(f).split(".")[0]] = "\n".join(strings(json.load(open(f))))
rows, c = [], collections.Counter()
for r in uni:
    grp = "H02" if r["family"] == "H02" else "A01" if r["family"] == "A01" else "rest"
    if r["card_exclusion"] or r["obeid_flag"]: c[(grp, "excluded_card_or_obeid")] += 1; continue
    if (r["card"], r["sentence"]) in audited: c[(grp, "audited_before")] += 1; continue
    if r["sentence"] not in cur.get(r["card"], ""): c[(grp, "text_changed_since")] += 1; continue
    c[(grp, "eligible")] += 1
    rows.append((grp, r["card"], r["family"], r["route1"], r["field_paths"], r["sentence"]))
rows.sort(key=lambda x: (x[0], x[1], x[5]))
with open(os.path.join(HERE, "eligible_ext.tsv"), "w") as o:
    o.write("group\tcard\tfamily\troute1\tfield_paths\tsentence\n")
    for x in rows: o.write("\t".join(x) + "\n")
with open(os.path.join(HERE, "counts_ext.tsv"), "w") as o:
    o.write("group\tmeasure\tvalue\n")
    for (g, m), n in sorted(c.items()): o.write(f"{g}\t{m}\t{n}\n")
print(open(os.path.join(HERE, "counts_ext.tsv")).read())
print("s1", len(s1), "s2", len(s2), "audited matched in universe", sum((r["card"], r["sentence"]) in audited for r in uni))
