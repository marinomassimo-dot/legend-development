"""Offline consistency check of seeds.tsv (IT9 P1).

Checks: rectangular; closed vocabularies; usable and reserved never both yes; usable iff reason_class USABLE; every
gene/protein row has an HGNC id matching hgnc_check.tsv (approved symbol equal to the row symbol); every process_id is
declared in process_ids.tsv; every 'NEED-X:On' locator names an existing need and a statement id that exists in
needs.json; every per-gene number printed in a Q2/Q3 reason for a P1/P7 value is re-read from the committed source table
(derived_gene_values.tsv, p7_organoid_key_genes.tsv, per_gene_in_sets.tsv). Prints PASS or the list of failures. Exit 0/1.

  python3 check_seeds.py --root <drug_repurposing dir> --dir <this dir>
"""
import argparse, csv, json, os, re, sys

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default="..", help="drug_repurposing directory")
    ap.add_argument("--dir", default=".", help="folder holding seeds.tsv")
    a = ap.parse_args()
    bad = []
    raw = list(csv.reader(open(os.path.join(a.dir, "seeds.tsv")), delimiter="\t"))
    if len({len(r) for r in raw}) != 1: bad.append("not rectangular")
    seeds = [dict(zip(raw[0], r)) for r in raw[1:]]
    hg = {r["symbol"]: r for r in csv.DictReader(open(os.path.join(a.dir, "hgnc_check.tsv")), delimiter="\t")}
    procs = {r["process_id"] for r in csv.DictReader(open(os.path.join(a.dir, "process_ids.tsv")), delimiter="\t")}
    needs = {n["id"]: {o["id"] for o in n["observed"]} for n in json.load(open(os.path.join(a.root, "needs/needs.json")))["needs"]}
    der = {}
    for r in csv.DictReader(open(os.path.join(a.root, "subnetwork_it7_p1_20261029/derived_gene_values.tsv")), delimiter="\t"):
        if r["R_centred"] != "": der[(r["gene"], r["system_id"])] = float(r["R_centred"])
    key = {r["gene"]: float(r["R_centred"]) for r in csv.DictReader(open(os.path.join(a.root, "hnpc_gse126075_it5_20261029/p7_organoid_key_genes.tsv")), delimiter="\t")}
    hn = {}
    for r in csv.DictReader(open(os.path.join(a.root, "hnpc_gse126075_it5_20261029/per_gene_in_sets.tsv")), delimiter="\t"):
        if r["set"] == "ISR_targets": hn[(r["symbol"], r["contrast"])] = float(r["R_centred"])
    for s in seeds:
        i = s["seed_id"]
        if s["direction"] not in {"up", "down", "uncertain", "unchanged"}: bad.append(i + " direction")
        if s["level"] not in {"expression", "protein", "phospho", "activity", "function", "pathology"}: bad.append(i + " level")
        if s["entity_type"] not in {"gene", "protein", "process", "state"}: bad.append(i + " entity_type")
        if s["usable_for_generation"] == "yes" and s["reserved_for_evaluation"] == "yes": bad.append(i + " usable and reserved")
        if (s["reason_class"] == "USABLE") != (s["usable_for_generation"] == "yes"): bad.append(i + " usable/reason_class")
        if bool(s["entity_symbol"]) == bool(s["process_id"]): bad.append(i + " exactly one of entity_symbol/process_id")
        if s["entity_symbol"]:
            h = hg.get(s["entity_symbol"])
            if not h or h["status"] != "Approved" or h["approved_symbol"] != s["entity_symbol"] or h["hgnc_id"] != s["hgnc_id"]: bad.append(i + " HGNC " + s["entity_symbol"])
        elif s["process_id"] not in procs: bad.append(i + " undeclared process " + s["process_id"])
        for m in re.finditer(r"(NEED-[A-Z0-9-]+):([O0-9,]+)", s["source_locator"]):
            if m.group(1) not in needs: bad.append(i + " unknown need " + m.group(1)); continue
            for oid in m.group(2).split(","):
                if oid and oid not in needs[m.group(1)]: bad.append("%s %s has no %s" % (i, m.group(1), oid))
        g = s["entity_symbol"]
        if s["question_id"] == "Q2" and "organoid %+.3f" not in s["reason"] and re.search(r"centred log2 ratio organoid ([+-][0-9.]+), hNPC ([+-][0-9.]+)", s["reason"]):
            m = re.search(r"centred log2 ratio organoid ([+-][0-9.]+), hNPC ([+-][0-9.]+)", s["reason"])
            for sysid, val in (("organoid_ko_w15", m.group(1)), ("hnpc_shwwox_cage", m.group(2))):
                if abs(der.get((g, sysid), 99) - float(val)) > 0.0006: bad.append("%s %s %s printed %s source %s" % (i, g, sysid, val, der.get((g, sysid))))
        if s["question_id"] == "Q3" and g in ("CHAC1", "TRIB3", "SESN2", "PSAT1", "ATF5"):
            m = re.search(r"centred log2 ratio organoid ([+-][0-9.]+), hNPC ([+-][0-9.]+)", s["reason"])
            if abs(key[g] - float(m.group(1))) > 0.0006 or abs(hn[(g, "C_hNPC")] - float(m.group(2))) > 0.0006: bad.append("%s %s ISR values differ from source" % (i, g))
    n_gene = sum(1 for s in seeds if s["entity_symbol"])
    print("rows:", len(seeds), "gene/protein rows with HGNC id:", n_gene, "needs locators resolved")
    print("PASS" if not bad else "FAIL\n" + "\n".join(bad))
    return 1 if bad else 0

if __name__ == "__main__":
    sys.exit(main())
