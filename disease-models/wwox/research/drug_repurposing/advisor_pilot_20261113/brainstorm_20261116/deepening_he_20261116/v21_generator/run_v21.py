#!/usr/bin/env python3
"""Run the frozen v2 generator on (A) the filled v2 cells, (B) v2 plus SCI's V2.1 cells with ADV's mapped origin ids, (C) B with the S-line overlap collapsed; compare the top sets.

    python3 run_v21.py --repo <repo root> --out <dir>        (deterministic; the rule digest is checked by the generator)
    python3 run_v21.py --help

Inputs: matrix_v2_cells_sci_20261116/output/cells_v2_form.tsv, deepening_sci_20261116/V21_CELLS_SCI.tsv (blob sha256 84ee2332..., frozen in ADV's V21_MERGE_NOTE_ADV.md), rule_v2.json
(sha256 2cb4a908...). Origin mapping (ADV's note): O-BULK-S-LINES -> O-REPUDI21 for T26; for T23 and T27 (both datasets) the composite O-REPUDI21+O-P47T-GSE215425, one origin.
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
b = v2 + v21; c = [dict(r, origin_id="O-SLINE-S") if r["origin_id"] in SLINE else dict(r) for r in b]; ca = [dict(r, origin_id="O-SLINE-S") if r["origin_id"] in SLINE else dict(r) for r in v2]
for name, rows in (("A_v2", v2), ("B_v2_plus_V21", b), ("C_sline_collapsed", c), ("Ac_v2_sline_collapsed", ca)):
    write(out / f"cells_{name}.tsv", rows)
    r = subprocess.run([sys.executable, str(repo / "framework/scripts/aed_matrix.py"), "score", str(out / f"cells_{name}.tsv"), str(RULE), "--expect-rule-sha256", RULE_SHA, "--out", str(out / f"scores_{name}.tsv")], capture_output=True, text=True)
    if r.returncode: sys.exit(r.stderr)
ref = D / "matrix_v2_cells_sci_20261116/output/scores_v2.tsv"
same = (out / "scores_A_v2.tsv").read_bytes() == ref.read_bytes()
def top(name):
    t = {}
    for r in read(out / f"scores_{name}.tsv"):
        k = (r["endpoint"], r["window"])
        if r["rank"] == "1" or k not in t: pass
    # top set = every class whose rank-by-score_all equals the maximum score_all
    for r in read(out / f"scores_{name}.tsv"):
        k = (r["endpoint"], r["window"]); t.setdefault(k, []).append((float(r["score_all"]), r["class_id"], r.get("top_set_size", ""), r.get("tie_label", r.get("top_set_label", ""))))
    res = {}
    for k, v in t.items():
        mx = max(x[0] for x in v); res[k] = (mx, sorted(x[1] for x in v if x[0] == mx), v[0][2], v[0][3])
    return res
tops = {n: top(n) for n in ("A_v2", "B_v2_plus_V21", "C_sline_collapsed", "Ac_v2_sline_collapsed")}
with open(out / "top_sets_compared.tsv", "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["endpoint", "window", "run", "max_score_all", "top_set_size_by_score", "top_set", "generator_top_set_size", "generator_label"])
    for k in sorted(tops["A_v2"]):
        for n in tops:
            mx, ts, gsz, lab = tops[n].get(k, ("", [], "", ""))
            w.writerow([k[0], k[1], n, mx, len(ts), ",".join(ts), gsz, lab])
(out / "run_note.txt").write_text(f"A reproduces scores_v2.tsv byte for byte: {same}\nrule sha256 {RULE_SHA} (checked by the generator)\nV21_CELLS_SCI.tsv sha256 {V21_SHA} (checked here)\n")
print(open(out / "run_note.txt").read())
