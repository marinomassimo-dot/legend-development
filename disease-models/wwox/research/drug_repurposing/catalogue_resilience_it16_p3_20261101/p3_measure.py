#!/usr/bin/env python3
"""IT16 P3 measurements through framework/adapters/chembl.py with the caching, bounded-retry fetch (_http.make_fetch).
Stages (each explicit; with no stage nothing runs; --help touches neither network nor files):
  identity   re-test the 8 IT15 queue names, short names and declared-id (salt -> parent) lookups -> identity_retest.tsv
  context    assay context for the molecules of --relations (default: scout_it14_p6 relations.tsv) whose assays are missing from --context
             -> assay_context_recovered.tsv (assay_context.tsv format)
  truncation re-run one IT15 truncated query (CHEMBL1904 IC50) with max_rows above the old 2000 cap -> truncation_check.tsv
  resume     run the same query twice and report network requests of the second run (cache effect) -> resume_check.tsv
The cache lives under --cache (use the gitignored files/ tree); outputs go to --out. Third-party raw responses stay in the cache, not in git."""
import argparse, csv, json, os, sys, time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "../../../../.."))
MOLS = {"Ro 25-6981": "CHEMBL305195", "ethosuximide": "CHEMBL696"}
QUEUE = ["acamprosate", "AV-101", "AZD8108", "delucemine", "indantadol", "neramexane", "ralfinamide", "felbamate"]
SHORT = ["AP5", "d-AP5", "MK-801", "dizocilpine", "TCN-201", "Ro 25-6981", "NPS 1506", "CP-101,606", "traxoprodil"]
DECLARED = {"delucemine HCl (salt id)": "CHEMBL2106165", "neramexane mesylate (salt id)": "CHEMBL2106798", "Ro 25-6981": "CHEMBL305195", "MK-801 maleate (salt id)": "CHEMBL344151"}


def tsv(path, header, rows):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(header); w.writerows(rows)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--stage", action="append", choices=["identity", "context", "truncation", "resume"], default=[])
    ap.add_argument("--cache", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--relations", default=os.path.join(HERE, "../scout_it14_p6_20261101/relations.tsv"))
    ap.add_argument("--context", default=os.path.join(HERE, "../scout_it14_p6_20261101/assay_context.tsv"))
    ap.add_argument("--pause", type=float, default=6.0)
    a = ap.parse_args()
    sys.path.insert(0, ROOT)
    from framework.adapters import chembl, _http
    fetch = _http.make_fetch(a.cache, retries=2, pause=a.pause)
    os.makedirs(a.out, exist_ok=True)
    if "identity" in a.stage:
        rows = []
        for n in QUEUE + SHORT:
            o = chembl.query({"drug": n}, fetch=fetch)
            h = (o["hits"] or [{}])[0]
            near = ";".join(f'{x["molecule_chembl_id"]}({x["pref_name"]},parent {x["parent_molecule_chembl_id"]})' for x in o.get("nearest", []))
            rows.append(["by_name", n, o["status"], h.get("molecule_chembl_id", ""), h.get("parent_molecule_chembl_id", ""), h.get("mechanism_found_via", ""), len(o["hits"]), near, o["error"][:80]])
        for n, mid in DECLARED.items():
            o = chembl.query({"drug": n, "molecule_id": mid}, fetch=fetch)
            h = (o["hits"] or [{}])[0]
            rows.append(["declared_id", n, o["status"], h.get("molecule_chembl_id", mid), h.get("parent_molecule_chembl_id", ""), h.get("mechanism_found_via", ""), len(o["hits"]),
                         ";".join(sorted({x.get("mechanism_of_action", "") for x in o["hits"]})), o["error"][:80]])
        tsv(os.path.join(a.out, "identity_retest.tsv"), ["route", "name_or_label", "status", "molecule", "parent", "mechanism_found_via", "n_hits", "nearest_or_mechanisms", "error"], rows)
    if "context" in a.stage:
        have = {r["assay_id"] for r in csv.DictReader(open(a.context, encoding="utf-8"), delimiter="\t")}
        need = set()
        for r in csv.DictReader(open(a.relations, encoding="utf-8"), delimiter="\t"):
            if r["compound"] in MOLS and r["source"] == "chembl_activity":
                parts = r["ref"].split(";")
                if len(parts) >= 3 and parts[2] not in have: need.add(parts[2])
        out, log = {}, []
        for name, mid in MOLS.items():
            o = chembl.query({"molecule": mid, "max_rows": 3000, "types": ["IC50", "Ki", "Kd", "EC50"]}, fetch=fetch)
            log.append([name, mid, o["status"], o.get("coverage", ""), o.get("retrieved", ""), o.get("total_count", ""), o.get("assay_batches_failed", ""), o["error"][:80], o.get("note", "")[:120]])
            for h in o["hits"]:
                c = h.get("assay_context")
                if h["assay_chembl_id"] in need and c:
                    out[h["assay_chembl_id"]] = [h["assay_chembl_id"], h["document_chembl_id"], c.get("assay_type") or "", c.get("assay_cell_type") or "", c.get("assay_organism") or "",
                                                 c.get("confidence_score") or "", c.get("relationship_type") or "", h.get("data_validity_comment") or "", h.get("potential_duplicate") if h.get("potential_duplicate") is not None else "",
                                                 (c.get("description") or "").replace("\t", " "), f"framework/adapters/chembl.py molecule={mid} (IT16 P3)"]
        tsv(os.path.join(a.out, "assay_context_recovered.tsv"), ["assay_id", "document_id", "assay_type", "assay_cell_type", "assay_organism", "confidence_score", "relationship_type", "data_validity_comment", "potential_duplicate", "description", "fetched_from"], sorted(out.values()))
        tsv(os.path.join(a.out, "context_pull_log.tsv"), ["compound", "molecule", "status", "coverage", "retrieved", "total_count", "assay_batches_failed", "error", "note"], log)
        print("assays needed", len(need), "recovered", len(out), "still missing", sorted(need - set(out))[:10])
    if "truncation" in a.stage:
        o = chembl.query({"target": "CHEMBL1904", "types": ["IC50"], "max_rows": 3000}, fetch=fetch)
        tsv(os.path.join(a.out, "truncation_check.tsv"), ["target", "type", "max_rows", "status", "coverage", "retrieved", "total_count", "truncated", "transport", "error"],
            [["CHEMBL1904", "IC50", 3000, o["status"], o.get("coverage", ""), o.get("retrieved", ""), o.get("total_count", ""), o.get("truncated", ""), json.dumps(o.get("transport")), o["error"][:80]]])
    if "resume" in a.stage:
        rows = []
        for k in (1, 2):
            f2 = _http.make_fetch(a.cache, retries=2, pause=a.pause)
            t = time.time(); o = chembl.query({"target": "CHEMBL1904", "types": ["Kd"], "max_rows": 400}, fetch=f2)
            rows.append([k, o["status"], o.get("coverage", ""), o.get("retrieved", ""), json.dumps(o.get("transport")), round(time.time() - t, 2)])
        tsv(os.path.join(a.out, "resume_check.tsv"), ["run", "status", "coverage", "retrieved", "transport", "seconds"], rows)
    print("fetch stats", fetch.stats, "failures", len(fetch.failures))
    json.dump(fetch.failures, open(os.path.join(a.out, "failures_log.json"), "w"), indent=0)


if __name__ == "__main__":
    main()
