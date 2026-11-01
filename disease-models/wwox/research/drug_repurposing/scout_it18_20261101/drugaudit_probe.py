"""IT18 scout probe: can DrugAudit items score the module's pharmacology answers?

Reads the DrugAudit evidence.xlsx (stdlib only), the module's matching answers
and card identities, and the catalogue names. Prints counts only (no item text
is written anywhere), so nothing from an unlicensed repository is copied.
Usage: python3 -I drugaudit_probe.py <evidence.xlsx> <repo_drug_repurposing_dir>
"""
import collections
import csv
import gzip
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = {"m": "http://schemas.openxmlformats.org/spreadsheetml/2006/main"}
ACTION = re.compile(r"\b(agonist|antagonist|inhibit\w*|activat\w*|blocker|modulator|"
                    r"mechanism of action|action type|opener|positive allosteric|negative allosteric)\b", re.I)


def read_xlsx(path):
    z = zipfile.ZipFile(path)
    shared = []
    root = ET.fromstring(z.read("xl/sharedStrings.xml"))
    for si in root.findall("m:si", NS):
        shared.append("".join(t.text or "" for t in si.iter("{%s}t" % NS["m"])))
    sheet = ET.fromstring(z.read("xl/worksheets/sheet1.xml"))
    rows = []
    for r in sheet.iter("{%s}row" % NS["m"]):
        row = {}
        for c in r.findall("m:c", NS):
            col = re.match(r"[A-Z]+", c.get("r")).group(0)
            v = c.find("m:v", NS)
            if v is None:
                isv = c.find("m:is", NS)
                val = "".join(t.text or "" for t in isv.iter("{%s}t" % NS["m"])) if isv is not None else ""
            elif c.get("t") == "s":
                val = shared[int(v.text)]
            else:
                val = v.text or ""
            row[col] = val
        rows.append(row)
    header = rows[0]
    return [header[k] for k in sorted(header)], [{header.get(k, k): v for k, v in r.items()} for r in rows[1:]]


def main():
    if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 0 if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help") else 2
    xlsx, d = sys.argv[1], sys.argv[2]
    cols, items = read_xlsx(xlsx)
    print("columns:", cols)
    print("items:", len(items))
    src_col = next(c for c in cols if "source" in c.lower())
    q_col = next(c for c in cols if c.lower().startswith("question"))
    a_col = next(c for c in cols if "answer" in c.lower())
    print("by source:", dict(collections.Counter(i.get(src_col, "") for i in items).most_common()))

    ids = set()
    with open(f"{d}/matching_it18_p4_20261101/answers.tsv") as f:
        match_ids = {r["parent_chembl_id"] for r in csv.DictReader(f, delimiter="\t")}
    with open(f"{d}/catalog/card_identity_declarations.tsv") as f:
        card_ids = {r["chembl_id"] for r in csv.DictReader(f, delimiter="\t")}
    ids = match_ids | card_ids
    names = {}
    with gzip.open(f"{d}/catalog/catalog.jsonl.gz", "rt") as f:
        for line in f:
            rec = json.loads(line)
            cid = rec.get("ids", {}).get("chembl")
            if cid in ids and rec.get("name"):
                names[cid] = rec["name"].lower()
    print("module compounds: matching", len(match_ids), "cards", len(card_ids), "named", len(names))

    def hits(idset):
        pats = {cid: re.compile(r"\b" + re.escape(names[cid]) + r"\b", re.I) for cid in idset if cid in names and len(names[cid]) > 3}
        per_item = []
        for it in items:
            text = it.get(q_col, "") + " " + it.get(a_col, "")
            found = [cid for cid, p in pats.items() if p.search(text)]
            if found:
                per_item.append((it, found))
        return per_item

    for label, idset in (("matching", match_ids), ("cards", card_ids)):
        ph = hits(idset)
        comp = {c for _, f in ph for c in f}
        act = [(it, f) for it, f in ph if ACTION.search(it.get(q_col, "") + " " + it.get(a_col, ""))]
        print(f"[{label}] items naming a module compound: {len(ph)}; distinct compounds: {len(comp)}; "
              f"of which with action/mechanism wording: {len(act)}; by source: "
              f"{dict(collections.Counter(it.get(src_col, '') for it, _ in act))}")
        print(f"[{label}] compounds named:", sorted(names[c] for c in comp))
    chembl_items = [i for i in items if "chembl" in i.get(src_col, "").lower()]
    print("ChEMBL-source items with action wording:",
          sum(1 for i in chembl_items if ACTION.search(i.get(q_col, "") + " " + i.get(a_col, ""))), "of", len(chembl_items))


if __name__ == "__main__":
    sys.exit(main())
