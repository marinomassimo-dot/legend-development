#!/usr/bin/env python3
"""ADV-287 step 0: count fold/ratio/range/percent/versus statements in the cards by two routes.
Run from anywhere: python3 -P -E universe_adv287.py  -> universe_adv287.tsv, route_counts_adv287.tsv"""
import json, glob, os, re, collections
HERE = os.path.dirname(os.path.abspath(__file__))
CARDS = os.path.normpath(os.path.join(HERE, "../../../cards"))
EXCLUDED = {"D02", "F02", "E03", "I01", "H01"}
NUM = r"\d+(?:\.\d+)?"
PATS = [
    re.compile(NUM + r"\s*[- ]?(?:fold|x|times)\b", re.I),
    re.compile(r"\bratio\b", re.I),
    re.compile(NUM + r"\s*(?:to|-|–)\s*" + NUM + r"\s*(?:%|percent|per cent|ms|mM|uM|mg|fold|x\b|years?|months?|weeks?|days?|hours?|h\b|nM|kDa|kb)", re.I),
    re.compile(r"\brange\b", re.I),
    re.compile(NUM + r"\s*(?:%|percent)", re.I),
    re.compile(NUM + r"[^.;]{0,60}\b(?:versus|vs\.?|v\.|against)\b[^.;]{0,60}" + NUM, re.I),
]
R1_FIELDS = re.compile(r"(drug_assertions|disease_assertions)\[\]/(measured_result_note|endpoint|note|locator)$|p4_card/(evidence_for_and_against/[a-z_]+|clinical_census|pharmacology|next_measurement)$|/(evidence_against|not_known)$")
SPLIT = re.compile(r"(?<=[.;])\s+|\n+")
def sentences(s):
    return [x.strip() for x in SPLIT.split(s) if x and x.strip()]
def has_quant(x): return any(p.search(x) for p in PATS)
def walk(o, p):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, p + "/" + k)
    elif isinstance(o, list):
        for v in o: yield from walk(v, p + "[]")
    elif isinstance(o, str):
        yield p, o
rows = []; counts = collections.Counter()
for f in sorted(glob.glob(os.path.join(CARDS, "*.packet.json"))):
    cid = os.path.basename(f).split(".")[0]; fam = cid.split("_")[0]
    d = json.load(open(f)); seen = {}
    for path, s in walk(d, ""):
        if re.search(r"(sha256|input_sha|receipt|id)$", path.split("/")[-1], re.I) and len(s) < 80: continue
        for sent in sentences(s):
            if not has_quant(sent): continue
            key = sent
            r1 = bool(R1_FIELDS.search(path)) and bool(re.search(r"\d", sent))
            if key in seen:
                seen[key]["r1"] = seen[key]["r1"] or r1; seen[key]["paths"].add(re.sub(r"\[\]", "", path)); continue
            seen[key] = {"r1": r1, "paths": {re.sub(r"\[\]", "", path)}}
    for sent, v in seen.items():
        obeid = bool(re.search(r"Obeid|42422765", sent))
        rows.append((cid, fam, "1" if v["r1"] else "0", "1", ";".join(sorted(v["paths"]))[:160], "excluded_card" if fam in EXCLUDED else "", "obeid_mention" if obeid else "", sent.replace("\t", " ")))
with open(os.path.join(HERE, "universe_adv287.tsv"), "w") as o:
    o.write("card\tfamily\troute1\troute2\tfield_paths\tcard_exclusion\tobeid_flag\tsentence\n")
    for r in rows: o.write("\t".join(r) + "\n")
fam_c = collections.Counter(); 
for r in rows: fam_c[(r[1], r[5] != "")] += 1
with open(os.path.join(HERE, "route_counts_adv287.tsv"), "w") as o:
    o.write("measure\tvalue\n")
    o.write(f"cards_scanned\t{len(glob.glob(os.path.join(CARDS,'*.packet.json')))}\n")
    o.write(f"union_statements\t{len(rows)}\n")
    o.write(f"route1\t{sum(r[2]=='1' for r in rows)}\n")
    o.write(f"route2_only\t{sum(r[2]=='0' for r in rows)}\n")
    o.write(f"in_excluded_cards\t{sum(r[5]!='' for r in rows)}\n")
    o.write(f"obeid_mention\t{sum(r[6]!='' for r in rows)}\n")
    o.write(f"universe_after_exclusions\t{sum(r[5]=='' and r[6]=='' for r in rows)}\n")
    for (fam, ex), n in sorted(fam_c.items()): o.write(f"family_{fam}{'_excluded' if ex else ''}\t{n}\n")
print(open(os.path.join(HERE, "route_counts_adv287.tsv")).read())
