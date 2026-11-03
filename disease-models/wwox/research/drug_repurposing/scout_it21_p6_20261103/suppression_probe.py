#!/usr/bin/env python3
"""IT21 P6 light test: does the literature-curated human suppression table (Unlu et al., Genome Medicine 2023,
Data S2, a ~140 KB xlsx taken from the Europe PMC supplementary zip) name any gene of the WWOX-DEE question?

Stdlib only. Reads the xlsx given as argument, writes counts to stdout and a gene-level (no item text) TSV when
--out is given. Copies no paper text. Gene panel is public gene symbols, no individual data.

    python3 suppression_probe.py --help
    python3 suppression_probe.py DATA_S2.xlsx [--out probe_hits.tsv]
"""
import argparse
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
# WWOX itself, its documented interactors / module genes used elsewhere in this module, and a panel of DEE and
# channel/transporter genes whose drugs the module already compares (declared before the lookup).
PANEL = {
    "WWOX": "target", "ERBB4": "WWOX interactor", "TP73": "WWOX interactor", "RUNX2": "WWOX interactor",
    "HIF1A": "module axis", "SLC2A1": "module", "HK2": "module", "LDHA": "module", "LDHB": "module",
    "BNIP3": "module", "PDK1": "module", "MTOR": "axis", "NFE2L2": "axis", "ATF4": "axis",
    "GRIN2B": "DEE", "GRIN2A": "DEE", "KCNQ2": "DEE", "SCN1A": "DEE", "SCN2A": "DEE", "SCN8A": "DEE",
    "CACNA1G": "DEE", "STXBP1": "DEE", "CDKL5": "DEE", "SLC12A2": "pharm", "KCNJ6": "pharm",
}


def sheet_rows(path, sheet_no):
    z = zipfile.ZipFile(path)
    ss = []
    if "xl/sharedStrings.xml" in z.namelist():
        for si in ET.fromstring(z.read("xl/sharedStrings.xml")).iter(NS + "si"):
            ss.append("".join(t.text or "" for t in si.iter(NS + "t")))
    rows = []
    for _, el in ET.iterparse(z.open(f"xl/worksheets/sheet{sheet_no}.xml")):
        if el.tag == NS + "row":
            r = {}
            for c in el.iter(NS + "c"):
                col = re.match(r"[A-Z]+", c.get("r")).group()
                v = c.find(NS + "v")
                r[col] = (ss[int(v.text)] if c.get("t") == "s" else v.text) if v is not None else ""
            rows.append(r)
            el.clear()
    return rows


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("xlsx")
    ap.add_argument("--out")
    a = ap.parse_args()
    rows = sheet_rows(a.xlsx, 2)
    head = rows[0]
    col = {v: k for k, v in head.items()}
    data = rows[1:]
    print(f"rows {len(data)}; columns {list(head.values())}")
    cats = {}
    for r in data:
        cats[r.get(col["Category"])] = cats.get(r.get(col["Category"]), 0) + 1
    print("category counts", cats)
    neuro = [r for r in data if r.get(col["Tissue"], "").lower() in ("neuron", "brain", "cns")]
    print("rows with a neural tissue label", len(neuro))
    hits = []
    genes = set()
    for r in data:
        q, s = r.get(col["QueryGene"]), r.get(col["SuppressorGene"])
        genes.update([q, s])
        for g in (q, s):
            if g in PANEL:
                hits.append((g, PANEL[g], "query" if g == q else "suppressor", q, s, r.get(col["Category"]),
                             r.get(col["Tissue"]), r.get(col["SuppressorType"]), r.get(col["PubmedID"])))
    print("distinct genes in table", len(genes - {None, ""}))
    print("panel genes present", sorted({h[0] for h in hits}))
    print("panel genes absent", sorted(set(PANEL) - {h[0] for h in hits}))
    for h in hits:
        print("HIT", *h)
    if a.out:
        with open(a.out, "w") as f:
            f.write("panel_gene\tpanel_role\tposition\tquery_gene\tsuppressor_gene\tcategory\ttissue\tsuppressor_type\tpmid\n")
            for h in hits:
                f.write("\t".join(str(x) for x in h) + "\n")


if __name__ == "__main__":
    sys.exit(main())
