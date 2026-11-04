#!/usr/bin/env python3
"""IT26 A1: what changed between the IT25 stage tables (results_s6) and the IT26 ones (results_s7), and why.

  python3 stage_diff_it26.py [--out DIR]

Offline; reads the two committed stage folders. Writes stage_diff.tsv (one row per proposal that appeared, disappeared or changed eligibility, blocker, identity
or z_reach) and stage_diff_summary.json. Two causes and only two: (1) nine listing-tier pairs withheld at the action refresh (rabeprazole x6, fexagratinib AKT1-3; an
alias collision and an alias artefact), which removes or re-targets proposals; (2) route R4 (G-SRS name -> UNII -> structure, confirmed by a second actor), which gives
19 DGIdb-only families an identity (has_chembl, modality) and so moves their eligibility blocker. Nothing here is a finding.
"""
import sys
if len(sys.argv) > 1 and sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import argparse, csv, json
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
OLD = DR / "generation_it25_a1_20261104" / "results_s6"
NEW = HERE / "results_s7"
COLS = ["z_reach", "handoff_eligible", "handoff_blocker", "has_chembl", "modality", "identity_via"]


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def key(r):
    return (r["question"], r["hypothesis"], r["family_id"], r["main_target"])


def compare(old, new):
    O = {key(r): r for r in old}
    N = {key(r): r for r in new}
    rows = []
    for k in sorted(set(O) | set(N)):
        if k not in N:
            rows.append(dict(change="removed", question=k[0], hypothesis=k[1], family_id=k[2], main_target=k[3], compound=O[k]["compound"], detail=""))
        elif k not in O:
            rows.append(dict(change="added", question=k[0], hypothesis=k[1], family_id=k[2], main_target=k[3], compound=N[k]["compound"], detail=""))
        else:
            d = [f"{c}: {O[k].get(c, '')} -> {N[k].get(c, '')}" for c in COLS if O[k].get(c, "") != N[k].get(c, "")]
            if d:
                rows.append(dict(change="changed", question=k[0], hypothesis=k[1], family_id=k[2], main_target=k[3], compound=N[k]["compound"], detail="; ".join(d)))
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE))
    a = ap.parse_args()
    old, new = rd(OLD / "proposals_it21.tsv"), rd(NEW / "proposals_it21.tsv")
    rows = compare(old, new)
    with open(Path(a.out) / "stage_diff.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["change", "question", "hypothesis", "family_id", "main_target", "compound", "detail"], delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(rows)
    eligible = lambda t: sum(r["handoff_eligible"] == "yes" for r in t)
    newly = [r for r in rows if r["change"] == "changed" and "handoff_eligible: no -> yes" in r["detail"]]
    s = dict(proposals_s6=len(old), proposals_s7=len(new), eligible_s6=eligible(old), eligible_s7=eligible(new), newly_eligible=sorted({r["compound"] for r in newly}),
             removed=[r["compound"] + " " + r["main_target"] for r in rows if r["change"] == "removed"], added=[r["compound"] + " " + r["main_target"] for r in rows if r["change"] == "added"],
             handoff_s6=len(rd(OLD / "handoff_it21.tsv")), handoff_s7=len(rd(NEW / "handoff_it21.tsv")), rows_changed=len(rows))
    json.dump(s, open(Path(a.out) / "stage_diff_summary.json", "w"), indent=1, sort_keys=True)
    print(json.dumps(s, indent=1, sort_keys=True))


if __name__ == "__main__":
    main()
