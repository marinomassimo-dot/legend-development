#!/usr/bin/env python3
"""Run the frozen v2 generator on (A) the filled v2 cells, (B) v2 plus SCI's V2.1 cells with ADV's mapped origin ids, (C) B with the S-line overlap collapsed; compare the top sets.

    python3 run_v21.py --repo <repo root> --out <dir>        (deterministic; the rule digest is checked by the generator)
    python3 run_v21.py --help

Inputs: matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv, deepening_sci_20261116/V21_CELLS_SCI.tsv (blob sha256 84ee2332..., frozen in ADV's V21_MERGE_NOTE_ADV.md), rule_v2.json
(sha256 2cb4a908...). Origin mapping (ADV's note): O-BULK-S-LINES -> O-REPUDI21 for T26; for T23 and T27 (both datasets) the composite O-REPUDI21+O-P47T-GSE215425, one origin.
TIER (ADV, after the first run): ADV corrected the evidence tier of the T23 cells from 2 to 1 (matrix precedent: transcript-only threads are tier 1). The PRIMARY runs set the T23 cells' evidence_tier to 1; the runs at SCI's tier 2 (the frozen blob as it is) are kept as SENSITIVITY and reported side by side. The first report at tier 2 was written before that decision.
C: every origin that shares the S-line (O-BRETON21, O-REPUDI21 and the composite) becomes one id, O-SLINE-S, in the v2 and V2.1 cells alike (ADV's sensitivity). The output describes the instrument; it scores no agent and recommends none. Not medical advice.
"""
import argparse, csv, hashlib, subprocess, sys
from pathlib import Path

ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter); ap.add_argument("--repo"); ap.add_argument("--out"); a = ap.parse_args()
if not (a.repo and a.out):
    ap.print_help(); sys.exit(0)
repo, out = Path(a.repo), Path(a.out); out.mkdir(parents=True, exist_ok=True)
D = repo / "disease-models/wwox/research/drug_repurposing"; B = D / "advisor_pilot_20261113/brainstorm_20261116"
RULE = B / "rule_v2.json"; RULE_SHA = "2cb4a908002aae48c6d4cc68baa9f8451e4bbb287fe6f47b4ccd6f7c5785f112"
V2 = D / "matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv"; V21 = B / "deepening_sci_20261116/V21_CELLS_SCI.tsv"
V21_SHA = "84ee23328219ae2a08f142ebe9af7b1e78a71c704c6a83fb6e2f1ad94519fe0b"
sha = lambda p: hashlib.sha256(Path(p).read_bytes()).hexdigest()
if sha(V21) != V21_SHA: sys.exit(f"REFUSED: V21_CELLS_SCI.tsv is not the frozen blob ({sha(V21)})")
COMPOSITE = "O-REPUDI21+O-P47T-GSE215425"
def read(p): return list(csv.DictReader(open(p, newline=""), delimiter="\t"))
v2, v21 = read(V2), read(V21); cols = list(v2[0])
for r in v21:
    r["origin_id"] = "O-REPUDI21" if r["thread_id"] == "T26" else COMPOSITE if r["thread_id"] in ("T23", "T24", "T25", "T27") else r["origin_id"]
def write(p, rows):
    with open(p, "w", newline="") as fh:
        w = csv.DictWriter(fh, cols, delimiter="\t", lineterminator="\n"); w.writeheader(); w.writerows(rows)
SLINE = {"O-BRETON21", "O-REPUDI21", COMPOSITE}
def with_tier(rows, tier):
    return [dict(r, evidence_tier=str(tier)) if r["thread_id"] == "T23" else dict(r) for r in rows]
SLINE = {"O-BRETON21", "O-REPUDI21", COMPOSITE}
collapse = lambda rows: [dict(r, origin_id="O-SLINE-S") if r["origin_id"] in SLINE else dict(r) for r in rows]
RUNS = {"A_v2": v2, "B_tier1_primary": v2 + with_tier(v21, 1), "C_tier1_sline_collapsed": collapse(v2 + with_tier(v21, 1)), "B_tier2_sensitivity": v2 + v21, "C_tier2_sline_collapsed": collapse(v2 + v21)}
for name, rows in RUNS.items():
    write(out / f"cells_{name}.tsv", rows)
    r = subprocess.run([sys.executable, str(repo / "framework/scripts/aed_matrix.py"), "score", str(out / f"cells_{name}.tsv"), str(RULE), "--expect-rule-sha256", RULE_SHA, "--out", str(out / f"scores_{name}.tsv")], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)
ref = D / "matrix_v2_cells_sci_20261116/output/scores_v2.tsv"
same = (out / "scores_A_v2.tsv").read_bytes() == ref.read_bytes()
def num(x):
    try: return int(x)
    except ValueError: return 99
with open(out / "top_sets_compared.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["endpoint", "window", "run", "max_score_all", "top_set_size", "top_set", "label", "neurosteroid_score_all", "neurosteroid_origin_collapsed", "neurosteroid_rank_origin_collapsed", "origin_collapsed_top3"])
    for name in RUNS:
        rows = read(out / f"scores_{name}.tsv")
        for ep, win in sorted({(r["endpoint"], r["window"]) for r in rows}):
            rr = [r for r in rows if r["endpoint"] == ep and r["window"] == win]; mx = max(float(x["score_all"]) for x in rr); ts = sorted(x["class_id"] for x in rr if float(x["score_all"]) == mx)
            n = [x for x in rr if x["class_id"] == "gabaa_neurosteroid_extrasynaptic"][0]; oc = sorted(rr, key=lambda x: num(x["rank_origin_collapsed"]))[:3]
            w.writerow([ep, win, name, f"{mx:g}", len(ts), ",".join(ts), rr[0]["top_set_label"], n["score_all"], n["score_origin_collapsed"], n["rank_origin_collapsed"], "; ".join(f"{x['class_id']}={x['score_origin_collapsed']}" for x in oc)])
(out / "run_note.txt").write_text(f"PERIMETER: V2.1 has NO allowed outcome table yet (the sealed A1 table and the I2 rows existed before the merge commit); this is an instrument description, not a score.\nA reproduces scores_v2.tsv byte for byte: {same}\nrule sha256 {RULE_SHA} (checked by the generator)\nV21_CELLS_SCI.tsv sha256 {V21_SHA} (checked here)\n")
print(open(out / "run_note.txt").read())
