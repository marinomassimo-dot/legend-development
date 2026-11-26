"""ADV-287 extension: list the H02 and A01 full pass and draw the second random 20 from the other families with the
ADV-287 rule (strata route1 / route2-only, proportional by largest remainder, random.Random(287) over rows sorted by
(card, sentence), 6 reserves per stratum). Obeid rule: a row whose enclosing record names only the Obeid article as its
source is removed before the draw, from the record's own source field, without opening anything.
Run: python3 -P -E sample_ext.py"""
import csv, glob, json, os, random, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.normpath(os.path.join(HERE, "../../../cards"))
rows = list(csv.DictReader(open(os.path.join(HERE, "eligible_ext.tsv")), delimiter="\t", quoting=csv.QUOTE_NONE))
packets = {os.path.basename(f).split(".")[0]: json.load(open(f)) for f in glob.glob(os.path.join(CARDS, "*.packet.json"))}
def records(o, parent=None):
    if isinstance(o, dict):
        for v in o.values(): yield from records(v, o)
    elif isinstance(o, list):
        for v in o: yield from records(v, parent)
    elif isinstance(o, str): yield o, parent
def info(card, sent):
    ids, srcs = [], []
    for s, rec in records(packets[card]):
        if sent in s and isinstance(rec, dict):
            ids.append(str(rec.get("id") or rec.get("assertion_id") or ""))
            srcs.append(str(rec.get("source") or ""))
    return ";".join(dict.fromkeys(i for i in ids if i)), " || ".join(dict.fromkeys(x for x in srcs if x))
for r in rows:
    r["record_ids"], r["record_source"] = info(r["card"], r["sentence"])
    src = r["record_source"]
    pm = set(re.findall(r"\b[34]\d{7}\b", src))
    r["obeid_only"] = "1" if (("42422765" in src or "Obeid" in src) and pm <= {"42422765"}) else ""
cols = ["group", "role", "n", "card", "route1", "field_paths", "record_ids", "record_source", "sentence"]
out = []
for g in ("H02", "A01"):
    for i, r in enumerate([r for r in rows if r["group"] == g and not r["obeid_only"]], 1):
        out.append(dict(r, role="full_pass", n=f"{g}-{i:02d}"))
rest = [r for r in rows if r["group"] == "rest" and not r["obeid_only"]]
strata = {"route1": [r for r in rest if r["route1"] == "1"], "route2_only": [r for r in rest if r["route1"] == "0"]}
for k in strata: strata[k].sort(key=lambda r: (r["card"], r["sentence"]))
N = 20; tot = len(rest)
raw = {k: N * len(v) / tot for k, v in strata.items()}
alloc = {k: int(x) for k, x in raw.items()}
for k in sorted(raw, key=lambda k: raw[k] - alloc[k], reverse=True):
    if sum(alloc.values()) < N: alloc[k] += 1
rng = random.Random(287); n = 0
for k in sorted(strata):
    order = list(strata[k]); rng.shuffle(order)
    for i, r in enumerate(order[: alloc[k] + (30 if k == "route2_only" else 6)]):
        n += 1
        out.append(dict(r, role=f"sample_{k}" if i < alloc[k] else f"reserve_{k}", n=f"R-{n:02d}"))
with open(os.path.join(HERE, "list_ext.tsv"), "w") as o:
    o.write("\t".join(cols) + "\n")
    for r in out: o.write("\t".join(str(r[c]).replace("\t", " ").replace("\n", " ") for c in cols) + "\n")
print("removed_obeid_only", [(r["card"], r["group"]) for r in rows if r["obeid_only"]])
print("rest", tot, {k: len(v) for k, v in strata.items()}, "alloc", alloc)
print("families in sample", len({r["card"].split("_")[0] for r in out if r["role"].startswith("sample")}))
