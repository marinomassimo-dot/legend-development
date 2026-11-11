"""SCI44 A4: one line per name from compound_identity.py (JSON): identity state, candidate records and, per expected gene, the evidence level reached.
  python3 identity_by_names.py "name1" "name2" ...   (expected genes fixed below)  -> identity_a4_tools.tsv"""
import csv, json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; ROOT = HERE.parents[5]
GENES = "LDHA,LDHB,PDK1,PDK2,PDK3,PDK4,PDHA1,PDP1"
def main(names):
    if not names or names[0] in ("-h", "--help"): print(__doc__); return 0
    rows = []
    for n in names:
        o = subprocess.run([sys.executable, "-I", str(ROOT / "framework/scripts/compound_identity.py"), n, "--genes", GENES], capture_output=True, text=True).stdout
        j = json.loads(o[o.index("{"):]) if "{" in o else {}
        idn = j.get("identity", {}); tg = j.get("target", {}).get("per_gene", {})
        reached = {g: v["level"] for g, v in tg.items() if v.get("level") not in ("EMPTY_RESULT", "NOT_READ")}
        rows.append([n, idn.get("identity_state", ""), ";".join(f'{c["catalogue_id"]}({c["origin"]})' for c in idn.get("candidates", [])), ";".join(f"{g}:{l}" for g, l in reached.items()) or "none"])
    with open(HERE / "identity_a4_tools.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["name", "identity_state", "candidate_records", "target_levels_reached"]); w.writerows(rows)
    return 0
if __name__ == "__main__": sys.exit(main(sys.argv[1:]))
