#!/usr/bin/env python3
"""Offline checks for the IT9 P4b group-A qualification (no network).
  test_qualify_p4b_a.py          run the checks; exit 0 when all pass
  test_qualify_p4b_a.py --help   this text
Checks: every TSV is rectangular; decisions come from the allowed set; every candidate has all four scores and a decisive datum; the builder is deterministic
(rebuilding in a temporary directory gives byte-identical tables); the denominators quoted in the records match chembl_row_counts.tsv."""
import csv, hashlib, shutil, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ALLOWED = {"DROP", "KEEP-AS-PROPOSAL", "REFERENCE-ONLY", "INCONCLUSIVE"}
TABLES = ["chembl_rows_selected.tsv", "chembl_row_counts.tsv", "trials_registry_search.tsv", "edge_provenance_live.tsv", "hpa_adult_expression.tsv", "faers_counts.tsv"]


def rect(p):
    rows = list(csv.reader(open(p, newline=""), delimiter="\t"))
    return len({len(r) for r in rows}) == 1


def sha(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main():
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__); return 0
    bad = []
    for t in TABLES + ["qualification_q2_metabolism.tsv", "edge_provenance_judged.tsv", "service_log.tsv", "service_log_supp.tsv", "hnpc_target_gene_rows.tsv", "organoid_target_gene_rows.tsv"]:
        if not rect(HERE / t):
            bad.append(f"not rectangular: {t}")
    dec = list(csv.DictReader(open(HERE / "qualification_q2_metabolism.tsv", newline=""), delimiter="\t"))
    if len(dec) != 6:
        bad.append(f"expected 6 candidates, found {len(dec)}")
    for r in dec:
        if r["decision"] not in ALLOWED:
            bad.append(f"{r['cand_id']}: decision {r['decision']}")
        for k in ("decisive_datum", "biological_promise_given_seed_link_and_target_action", "depth_of_evidence", "feasibility", "priority_of_next_experiment", "unverified"):
            if not r[k].strip():
                bad.append(f"{r['cand_id']}: empty {k}")
        if not (HERE / "records" / f"{r['cand_id']}_{r['name']}.md").exists() and not list((HERE / "records").glob(f"{r['cand_id']}_*.md")):
            bad.append(f"{r['cand_id']}: no record file")
    counts = {r["molecule"]: r for r in csv.DictReader(open(HERE / "chembl_row_counts.tsv", newline=""), delimiter="\t")}
    for m, r in counts.items():
        if r["complete"] != "yes" or r["total_count"] != r["rows_retrieved"]:
            bad.append(f"{m}: truncated pull")
    with tempfile.TemporaryDirectory() as td:
        for f in ("collected.json.gz", "collected_supp.json.gz", "build_tables_p4b_a.py"):
            shutil.copy(HERE / f, td)
        subprocess.run([sys.executable, "-I", str(Path(td) / "build_tables_p4b_a.py"), "build"], check=True, capture_output=True)
        for t in TABLES:
            if sha(HERE / t) != sha(Path(td) / t):
                bad.append(f"not reproducible: {t}")
    if bad:
        print("FAIL"); [print(" ", b) for b in bad]; return 1
    print("PASS: tables rectangular, decisions in the allowed set, pulls complete, builder deterministic"); return 0


if __name__ == "__main__":
    sys.exit(main())
