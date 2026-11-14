#!/usr/bin/env python3
"""check_keys.py (PRESIDIO-002): compares the two keys that tie a source hypothesis or lever to an ADV-006 row.

For each of the seven SCI42 explanations: (a) tokens = rows of measurement_reconciliation_adv006_20261114/output/measurements.tsv
whose `requests_merged` holds sci42_chloride#explanations:<id>; (b) crosswalk = the rows named by `measurement_id` of the
explanation's crosswalk row; (c) source_names = rows whose `source_names` cite a SCI42 id that the explanation's
`needs_new_measurement` names. Each row in (c) but not in (a) is classified with a reason, checked against the cell text.
For each SCI47 lever L1-L6: tokens (levers:<id>), O-id tokens named in the lever's own cells, and rows that mention the
lever id in name, source_names, lever_or_comparison_gated or interpretable_after. Writes keys.tsv next to this file.
Idempotent; reads three tables; takes no arguments.   Usage: python3 check_keys.py   |   check_keys.py --help
"""
import csv
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = next(p for p in HERE.parents if (p / "framework").is_dir() and (p / "disease-models").is_dir())
RD = ROOT / "disease-models/wwox/research/drug_repurposing"

REASON = {  # (row, sci42 id): (phrase that must be in the row's source_names, classification and reason)
    ("M07", "M03"): ("SCI42 M03 (Ra, noise)", "component: the covariates (access resistance, noise) that SCI42 M03 asks to be reported per genotype; M01 is the sIPSC re-record itself"),
    ("M07", "M05"): ("M05 (Rin, cell size)", "component: the covariates (input resistance, cell size) read with SCI42 M05; M04 is the agonist response itself"),
    ("M26", "M02"): ("SCI42 M02 ('protein across ages')", "component: SCI42 M02 is a programme that contains 'protein across ages'; M08 is its age series, M26 its KCC2/NKCC1 protein part"),
    ("M22", "M01"): ("not SCI42 chloride M01", "false hit: the cell says it is the GluN2B package's M01 (pH), not SCI42 chloride M01"),
}


def table(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def sci42_ids(sn):
    out = set()
    for seg in sn.split(";"):
        if "SCI42" in seg:
            out |= set(re.findall(r"\bM\d{2}\b", seg.split("SCI42", 1)[1]))
    return out


def main():
    if len(sys.argv) > 1:
        print(__doc__)
        return 0
    A = RD / "measurement_reconciliation_adv006_20261114/output"
    ms = table(A / "measurements.tsv")
    cw = {r["req_id"]: r for r in table(A / "crosswalk.tsv")}
    ex = table(RD / "chloride_gradient_sci42_20261110/output/explanations.tsv")
    lev = table(RD / "inhibitory_defect_sci47_20261112/output/levers.tsv")
    out = []
    for e in ex:
        eid = e["expl_id"]
        need = set(re.findall(r"\bM\d{2}\b", e["needs_new_measurement"]))
        tok = [m["m_id"] for m in ms if re.search(r"sci42_chloride#explanations:%s(?![\w-])" % re.escape(eid), m["requests_merged"])]
        cwm = [x for x in cw["sci42_chloride#explanations:" + eid]["measurement_id"].split(";") if x]
        sn = [m["m_id"] for m in ms if sci42_ids(m["source_names"]) & need]
        extras = []
        for m in ms:
            if m["m_id"] in sn and m["m_id"] not in tok:
                for i in sorted(sci42_ids(m["source_names"]) & need):
                    phrase, why = REASON[(m["m_id"], i)]
                    assert phrase in m["source_names"], (m["m_id"], i)
                    extras.append("%s via SCI42 %s: %s" % (m["m_id"], i, why))
        out.append(["explanation", eid, ",".join(sorted(need)), ",".join(sorted(tok)), ",".join(sorted(cwm)), ",".join(sorted(sn)),
                    "tokens == crosswalk: %s; tokens subset of source_names: %s" % (sorted(tok) == sorted(cwm), set(tok) <= set(sn)), " || ".join(extras)])
    for L in lev:
        lid = L["lever_id"]
        tok = [m["m_id"] for m in ms if re.search(r"sci47_inhibitory#levers:%s\b" % lid, m["requests_merged"])]
        oids = sorted(set(re.findall(r"\bO\d{2}\b", " ".join(v for k, v in L.items() if k != "lever_id"))))
        otok = sorted({m["m_id"] for m in ms for o in oids if re.search(r"sci47_inhibitory#matrix:%s\b" % o, m["requests_merged"])})
        ment = sorted({m["m_id"] for m in ms for c in ("name", "source_names", "lever_or_comparison_gated", "interpretable_after") if re.search(r"\b%s\b" % lid, m[c])})
        out.append(["lever", lid, ",".join(oids), ",".join(sorted(tok)), "", ",".join(sorted(set(otok) | set(tok))), "prose mentions: " + ",".join(ment),
                    "rows mentioning the lever but neither a levers token nor a row reached by an O-id of the lever's own cells: " + ",".join(sorted(set(ment) - set(tok) - set(otok)))])
    with open(HERE / "keys.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["kind", "id", "needs_or_O_ids", "requests_merged_tokens", "crosswalk_measurement_id", "source_names_or_O_declared_rows", "comparison", "extras_and_reason"])
        w.writerows(out)
    print("rows", len(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
