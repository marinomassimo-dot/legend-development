#!/usr/bin/env python3
"""IT23 P3: reproduce the sign-conversion defect in NORDic's drug-target aggregator (retrieve_drug_targets),
and show the explicit-only converter that LEGEND would use instead.

Runs the REAL NORDic function (installed from the cloned repo at commit 9db480d) on 5 synthetic cached
source tables; no network access, no credentials. Needs the venv with NORDic installed.
  usage: python -I defect_repro.py [--help]
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
import os, re, tempfile, inspect, json
import pandas as pd
import NORDic.NORDic_DS.get_drug_targets as gdt

src = inspect.getsource(gdt)
# --- locate the lines responsible, verbatim from the installed source
lines = src.splitlines()
def find(s):
    return [(i + 1, l.strip()) for i, l in enumerate(lines) if s in l]
resp = {
    "unsigned_to_inhibition": find('targets_df[(targets_df!="0")&(targets_df!="-1")&(targets_df!="1")] = "-1"'),
    "minus_beats_plus": find('is_inhibitor = np.vectorize(lambda x : "-" in x)'),
    "ttd_unlisted_moa_to_plus": find('drug_targets["MOA"] = [("-" if (m in decrease_expr_MOA) else "+") for m in drug_targets["MOA"]]'),
}
assert all(len(v) == 1 for v in resp.values()), resp
decrease = re.search(r"decrease_expr_MOA = (\[.*?\])", src).group(1)
decrease = eval(decrease)

def ttd_sign(moa):  # exactly the expression of get_targets_TTD
    return "-" if (moa in decrease) else "+"

rows = [  # (drug, gene, TTD MOA or None, DrugCentral present, injected signed 2nd source)
    ("D1", "G1", "inhibitor", False, None),
    ("D2", "G2", "?", False, None),
    ("D3", "G3", "binding", False, None),
    ("D4", "G4", None, True, None),
    ("D5", "G5", "agonist", False, "-"),
]
drugs = [r[0] for r in rows]; genes = [r[1] for r in rows]
def table(fn):
    t = pd.DataFrame("", index=genes, columns=drugs)
    for d, g, moa, dc, inj in rows:
        v = fn(moa, dc, inj)
        if v is not None:
            t.loc[g, d] = v
    return t
tmp = tempfile.mkdtemp(prefix="nordic_defect_")
folder = tmp + "/"
table(lambda moa, dc, inj: None if moa is None else ttd_sign(moa)).to_csv(folder + "drug_targets_TTD.csv")
table(lambda moa, dc, inj: "*" if dc else None).to_csv(folder + "drug_targets_DrugCentral.csv")
table(lambda moa, dc, inj: inj).to_csv(folder + "drug_targets_DrugBank.csv")  # a signed 2nd source, injected for the contrast case
out = gdt.retrieve_drug_targets(folder, drugs, TARGET_args={"DrugBank": {"path_to_drugbank": "x", "target_fname": "y", "drug_fname": "z"}},
                                sources=["TTD", "DrugCentral", "DrugBank"], quiet=True)
truth = {"D1": "inhibitor (explicit)", "D2": "unknown ('?')", "D3": "unknown ('binding': no direction)", "D4": "unknown (presence only)", "D5": "contrasting (+ and -)"}
print("responsible source lines (installed NORDic, get_drug_targets.py):")
for k, v in resp.items():
    print(f"  {k}: line {v[0][0]}: {v[0][1]}")
print("\nTTD decrease list:", decrease)
print("\nrow  input                                   NORDic output (gene x drug)   what it should be")
res = []
for d, g, moa, dc, inj in rows:
    desc = f"TTD MOA={moa!r}" if moa else "DrugCentral presence only"
    if inj: desc += f" + 2nd source '{inj}'"
    val = int(out.loc[g, d])
    res.append(dict(row=d, gene=g, input=desc, nordic_value=val, correct=truth[d]))
    print(f"{d}/{g}  {desc:40s} {val:+d}                         {truth[d]}")

# --- explicit-only converter (what LEGEND would use)
EXPLICIT_DOWN = set(decrease)
EXPLICIT_UP = {"agonist", "activator", "positive modulator", "stimulator", "inducer", "opener"}
def explicit_sign(strings):
    s = {("-1" if x in EXPLICIT_DOWN else "+1" if x in EXPLICIT_UP else "unknown") for x in strings}
    if s == {"-1"}: return -1
    if s == {"+1"}: return 1
    if "unknown" in s and len(s) == 1: return None            # unknown stays unknown: no edge
    if "unknown" in s: return explicit_sign([x for x in strings if x in EXPLICIT_DOWN | EXPLICIT_UP])  # unknown annotations are ignored, never counted
    return "CONFLICT"                                          # contrasting explicit signs are reported, never resolved
fixed = {
    "D1": explicit_sign(["inhibitor"]), "D2": explicit_sign(["?"]), "D3": explicit_sign(["binding"]),
    "D4": explicit_sign([]), "D5": explicit_sign(["agonist", "inhibitor"]),
}
fixed["D4"] = None
print("\nexplicit-only converter (None = no edge, CONFLICT = listed, not resolved):", fixed)
json.dump(dict(responsible_lines=resp, nordic_output=res, explicit_only=fixed, ttd_decrease_list=decrease), open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "results", "defect_repro.json"), "w"), indent=1)
