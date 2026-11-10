"""IT42 P2: evaluation of retrieval and qualification, protocol in eval_protocol_it42.md (fixed before execution). Paths A0 (previous source), A1 (two sources), B (guided on the same two sources).
Errors E1-E5 are checked here from the source fields of each row with their own small tests (not by reading B's verdict). Output: eval_results.tsv, eval_summary.md. Not a prediction accuracy."""
import csv, re, sys, time
from collections import defaultdict
from pathlib import Path
HERE = Path(__file__).resolve().parent; DR = HERE.parent; IT41 = DR / "generation_it41_20261109"
sys.path.insert(0, str(IT41))
t0 = time.time()
import action_search as A  # noqa: E402
def tsv(p): return list(csv.DictReader(open(p, encoding="utf-8"), delimiter="\t"))
rel = {r["relation_id"]: r for r in tsv(IT41 / "relations_it41.tsv")}
ident = A.load_identity(DR)
REF = {"S1": {"radiprodil", "traxoprodil", "rislenemdaz", "evt-101", "ifenprodil", "ro 25-6981"}}   # fixed in the protocol: primary readings of earlier packages
QS = {"Q1": "S1", "Q2": "S3", "Q3": "S5", "Q4": "S6", "Q5": "S7"}
DOWN = re.compile(r"inverse agonist|antagon|inhibit|block|negative|blocker", re.I); UP = re.compile(r"(?<!ant)(?<!inverse )agonist|activat|positive|potentiat|opener", re.I)
def wdir(rid, sym):
    w = rel[rid]["wanted_direction"]
    if ":" in w: return dict(x.split(":") for x in w.split(";")).get(sym.upper(), "")
    return w
def errors(rid, r):
    """E1-E3, E5 for one source row, from its own fields."""
    e = set(); parts = (r["action"] or "").split("/"); act = parts[-1] if parts[-1].strip().lower() not in ("none", "") else parts[0]; w = wdir(rid, r["target_symbol"].split("|")[0].strip() if r["source"].startswith("GtoPdb") else r["target_symbol"])
    if w == "down" and UP.search(act) and not DOWN.search(act): e.add("E1")
    if w == "up" and DOWN.search(act) and not UP.search(act): e.add("E1")
    if rel[rid]["site_policy"] == "allosteric_subunit" and (r["site_or_granularity"] in ("glutamate site", "glycine site", "family_record_subunit_unresolved") or (r["action"] or "").startswith("Channel blocker")): e.add("E2")
    if rel[rid]["subunit_out"] and re.search(rel[rid]["subunit_out"], r["assay_or_note"] or "", re.I): e.add("E3")
    for nm in (r["name"] or "").lower().split(" | "):
        if any(x.get("label_conflict") == "yes" for x in ident.get(nm, [])): e.add("E5")
    return e
rows_all = tsv(IT41 / "search_rows.tsv"); out = []; md = []
for q, rid in QS.items():
    R = [r for r in rows_all if r["relation_id"] == rid]
    paths = {"A0": [r for r in R if r["source"].startswith("ChEMBL")], "A1": R, "B": [r for r in R if r["qualification"] == "CANDIDATE"]}
    for p, rows in paths.items():
        parents = defaultdict(list)
        for r in rows: parents[r["molecule"] if not r["labelled_form"] == "yes" else r["molecule"] + "#labelled"].append(r)
        dup = len(rows) - len(parents)
        errs = defaultdict(int); unflagged = 0; clean = 0
        for par, rs in parents.items():
            es = set.intersection(*[errors(rid, r) for r in rs])   # an error of the unit = shared by all its returned rows
            for k in es: errs[k] += 1
            if not es: clean += 1
            elif p != "B": unflagged += 1
            elif any(r["qualification"] != "CANDIDATE" for r in rs): pass
            else: unflagged += 1
        names = {n.lower() for r in rows for n in (r["name"] or "").split(" | ")}
        refs = REF.get(rid, set()); ref_found = sorted(x for x in refs if any(x in n for n in names))
        unk = [r for r in R if r["qualification"] == "UNKNOWN"] if p == "B" else []
        unk_cf = len({r["molecule"] for r in unk}) if p == "B" else 0
        excl = len({r["molecule"] for r in R if r["qualification"] == "EXCLUDED"}) if p == "B" else 0
        out.append([q, rid, p, len(rows), len(parents), dup, clean, errs["E1"], errs["E2"], errs["E3"], errs["E5"], unflagged, ";".join(ref_found) if refs else "n/a", unk_cf, excl])
H = ["question", "relation", "path", "rows_returned", "distinct_units", "E4_duplicates", "clean_units", "E1_direction", "E2_site_class", "E3_subunit_transfer", "E5_identity", "units_with_unflagged_error", "reference_positives_returned", "unknown_units_kept_with_reason", "excluded_units_with_reason"]
with open(HERE / "eval_results.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(H); w.writerows(out)
elapsed = time.time() - t0
print("\t".join(H))
for o in out: print("\t".join(str(x) for x in o))
print("wall seconds for the whole evaluation (import + scoring from stored rows):", round(elapsed, 2))

# lost candidates: units that are clean under E1-E5 in A1 but absent from B's shortlist (protocol measure 4)
lost = []
for q, rid in QS.items():
    R = [r for r in rows_all if r["relation_id"] == rid and r["labelled_form"] != "yes"]
    parents = defaultdict(list)
    for r in R: parents[r["molecule"]].append(r)
    for par, rs in parents.items():
        clean = not set.intersection(*[errors(rid, r) for r in rs])
        in_b = any(r["qualification"] == "CANDIDATE" for r in rs)
        if clean and not in_b:
            lost.append([q, par, rs[0]["name"], ";".join(sorted({r["qualification"] + ":" + r["reason"] for r in rs})), ";".join(sorted({r["action"] for r in rs}))[:60]])
with open(HERE / "eval_lost_candidates.tsv", "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["question", "unit", "name", "B_verdicts", "actions"]); w.writerows(lost)
print("clean in A1 but not in B's shortlist:", len(lost))
for l in lost: print(*l, sep=" | ")
