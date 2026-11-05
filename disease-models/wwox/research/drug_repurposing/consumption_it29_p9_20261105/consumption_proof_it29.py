#!/usr/bin/env python3
"""IT29 P9: show that two persisted IT28 challenge results are READ by the generator, and what they change.

For each persisted result (a row of generation_it22_p1_20261103/decision_scope_it22.tsv whose reason starts with 'IT28') the script
  1. runs the committed `propose` step twice into a scratch directory: with the table as committed, and with the IT28 rows removed;
  2. compares the two proposal tables cell by cell and reports which columns moved on which proposals;
  3. checks the 'as committed' run against the committed stage tables, so the claim 'regenerates' is itself tested.
The decision-scope table is restored byte for byte afterwards. Usage: consumption_proof_it29.py run --engine-dir DIR --out DIR2 [--p1-inputs DIR]
"""
from __future__ import annotations

import argparse
import csv
import subprocess
import sys
from pathlib import Path

DR = Path(__file__).resolve().parent.parent
SCOPE = DR / "generation_it22_p1_20261103" / "decision_scope_it22.tsv"
GEN = DR / "generation_it21_p2_20261103" / "run_generation_it21.py"
STAGE = DR / "generation_it28_p6_20261105" / "results_s9"


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def propose(out: Path, engine: Path, p1: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, str(GEN), "propose", "--engine-dir", str(engine), "--out-dir", str(out)]
    if p1:
        cmd += ["--p1-inputs", p1]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)


def diff(a: Path, b: Path):
    A = {r["proposal_id"]: r for r in rd(a / "proposals_it21.tsv")}
    B = {r["proposal_id"]: r for r in rd(b / "proposals_it21.tsv")}
    moved, cols = {}, {}
    for pid in A:
        for k in A[pid]:
            if A[pid][k] != B[pid].get(k):
                moved.setdefault(pid, []).append(k)
                cols[k] = cols.get(k, 0) + 1
    return A, moved, cols


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("cmd", choices=["run"])
    ap.add_argument("--engine-dir", required=True, type=Path)
    ap.add_argument("--out", required=True, type=Path)
    ap.add_argument("--p1-inputs", default="")
    a = ap.parse_args(argv)
    original = SCOPE.read_bytes()
    lines = original.decode("utf-8").splitlines(keepends=True)
    header, rows = lines[0], lines[1:]
    kept = [r for r in rows if not r.split("\t")[4:5] or not r.split("\t")[4].startswith("IT28")]
    removed = len(rows) - len(kept)
    try:
        propose(a.out / "as_committed", a.engine_dir, a.p1_inputs)
        SCOPE.write_bytes((header + "".join(kept)).encode("utf-8"))
        propose(a.out / "without_it28_rows", a.engine_dir, a.p1_inputs)
    finally:
        SCOPE.write_bytes(original)
    committed = {r["proposal_id"]: r for r in rd(STAGE / "proposals_it21.tsv")}
    mine, _, _ = diff(a.out / "as_committed", STAGE)
    regenerates = all(mine[p] == committed[p] for p in committed) and set(mine) == set(committed)
    _, moved, cols = diff(a.out / "as_committed", a.out / "without_it28_rows")
    print(f"scope rows removed for the control: {removed}")
    print(f"as-committed run reproduces the committed stage table cell for cell: {regenerates}")
    print(f"proposals whose cells differ with v without the IT28 rows: {len(moved)}; columns: {cols}")
    A = {r["proposal_id"]: r for r in rd(a.out / "as_committed" / "proposals_it21.tsv")}
    elig = sum(r["handoff_eligible"] == "yes" for r in A.values())
    B = {r["proposal_id"]: r for r in rd(a.out / "without_it28_rows" / "proposals_it21.tsv")}
    print(f"eligible with/without: {elig}/{sum(r['handoff_eligible'] == 'yes' for r in B.values())}")
    with open(a.out / "consumption_diff.tsv", "w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(["proposal_id", "compound", "columns_that_moved"])
        for pid, ks in sorted(moved.items()):
            w.writerow([pid, A[pid]["compound"], ",".join(ks)])
    return 0 if regenerates else 1


if __name__ == "__main__":
    raise SystemExit(main())
