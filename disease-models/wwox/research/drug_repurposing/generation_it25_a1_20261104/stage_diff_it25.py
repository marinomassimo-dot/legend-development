#!/usr/bin/env python3
"""IT25 A1: what changed between the IT23 stage tables (results_s5) and the IT25 ones (results_s6), and why.

  python3 stage_diff_it25.py [--out DIR]

Offline; reads the two committed stage folders. Writes stage_diff.tsv (one row per proposal whose z, eligibility, blocker, phase or presence changed) and
stage_diff_summary.json. The causes are three and only three: (1) twelve listing-tier pairs withheld at the action refresh (source_exclusions_it24.tsv), which
removes proposals and moves z for the families that lose a target; (2) F1, the record's own concept-id ligand in the attribution screen (attribution_* columns,
not read here); (3) F2, a blank phase read from the sibling family (max_phase, max_phase_source). Nothing here is a finding.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import csv, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
OLD = DR / "generation_it23_p2_20261103" / "results_s5"
NEW = HERE / "results_s6"


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def key(r):
    return (r["question"], r["seed_set"], r["hypothesis"], r["compound"])


def diff():
    A = {key(r): r for r in rd(OLD / "proposals_it21.tsv")}
    B = {key(r): r for r in rd(NEW / "proposals_it21.tsv")}
    ha = {r["proposal_id"] for r in rd(OLD / "handoff_it21.tsv")}
    hb = {r["proposal_id"] for r in rd(NEW / "handoff_it21.tsv")}
    rows = []
    for k, a in A.items():
        b = B.get(k)
        if b is None:
            rows.append((a["proposal_id"], k[0], k[3], a["family_id"], "LEFT_THE_TABLE", a["z_total"], "", a["z_reach"], "", a["handoff_eligible"], "", a["handoff_blocker"], "", "yes" if a["proposal_id"] in ha else "", ""))
            continue
        moved = any(a[c] != b[c] for c in ("z_total", "z_reach", "handoff_eligible", "handoff_blocker"))
        if moved:
            rows.append((a["proposal_id"], k[0], k[3], a["family_id"], "MOVED", a["z_total"], b["z_total"], a["z_reach"], b["z_reach"], a["handoff_eligible"], b["handoff_eligible"],
                         a["handoff_blocker"], b["handoff_blocker"], "yes" if a["proposal_id"] in ha else "", "yes" if b["proposal_id"] in hb else ""))
    return A, B, ha, hb, rows


def main():
    out = HERE
    if "--out" in sys.argv:
        out = Path(sys.argv[sys.argv.index("--out") + 1])
    A, B, ha, hb, rows = diff()
    cols = ("proposal_id", "question", "compound", "family_id", "change", "z_total_old", "z_total_new", "z_reach_old", "z_reach_new", "eligible_old", "eligible_new", "blocker_old", "blocker_new", "handed_over_old", "handed_over_new")
    with open(out / "stage_diff.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(cols)
        w.writerows(rows)
    own = sum(1 for r in B.values() if r.get("max_phase_source") == "own")
    sib = sum(1 for r in B.values() if r.get("max_phase_source") == "sibling_family")
    s = {"proposals_old": len(A), "proposals_new": len(B), "left": sorted(r[2] for r in rows if r[4] == "LEFT_THE_TABLE"), "moved": sorted(r[2] for r in rows if r[4] == "MOVED"),
         "handoff_old": len(ha), "handoff_new": len(hb), "handoff_left": sorted(ha - hb), "handoff_gained": sorted(hb - ha), "phase_from_own_record": own, "phase_from_sibling_family": sib}
    (out / "stage_diff_summary.json").write_text(json.dumps(s, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(s, indent=1))


if __name__ == "__main__":
    main()
