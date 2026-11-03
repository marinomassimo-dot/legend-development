#!/usr/bin/env python3
"""IT22 P3: build the amended generator inputs from the committed IT9 P1 seed table, the IT10 question roles and the reviewed additions in p3_A_redox/.

  build_inputs_it22.py --out DIR [--arm hnpc_excluded]

Writes DIR/{seeds.tsv, questions.tsv, question_roles.tsv, process_ids.tsv, hgnc_check.tsv} and DIR/seeds_p1/ (the existing p1_adapter.py applied to them).
Nothing in the IT9 P1 folder is edited; every added or changed row carries change_ref `it22-<tag>`, so the difference from the IT21 inputs is one diff.

 - Q8 (NRF2 tone, role unknown): one usable gene seed, NFE2L2 transcript lower in the human KO organoid (p3_A_redox N22-A001), carrying guard NRF2_TONE_UNRESOLVED; the other
   redox rows are demoted or states without gene members and are NOT placed (they are in the trace, not in the engine).
 - arm hnpc_excluded (sensitivity, not a correction of the table): rows whose second system is the shWWOX hNPC library of GSE126075 (S017-S025, S040-S044) set usable=no,
   because that library did not show WWOX lower (gate 1 failed, hnpc_gse126075_it5_20261029/RESULTS.md section 1).
"""
import sys
if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)
import argparse, csv, shutil, subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
DR = HERE.parent
P1 = DR / "generation_it9_p1_20261030"
HNPC_ROWS = ["S017", "S018", "S019", "S020", "S021", "S022", "S023", "S024", "S025", "S040", "S041", "S042", "S043", "S044"]


def rd(p):
    with open(p, encoding="utf-8", newline="") as fh:
        return list(csv.DictReader(fh, delimiter="\t"))


def wr(p, rows, cols):
    with open(p, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=cols, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--arm", default="", choices=["", "hnpc_excluded"])
    a = ap.parse_args()
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    seeds = rd(P1 / "seeds.tsv")
    cols = list(seeds[0])
    nxt = max(int(r["seed_id"][1:]) for r in seeds) + 1
    add = [r for r in rd(HERE / "p3_A_redox" / "proposed_seed_rows.tsv") if r["seed_id"] == "N22-A001"]
    for r in add:
        r = dict(r, seed_id=f"S{nxt}", question_id="Q8", guard_tag="NRF2_TONE_UNRESOLVED", change_ref="it22-A001")
        nxt += 1
        seeds.append(r)
    by = {r["seed_id"]: r for r in seeds}
    tag = lambda r, t: r.__setitem__("guard_tag", ";".join(sorted({x for x in (r["guard_tag"] + ";" + t).split(";") if x})))
    for sid in HNPC_ROWS:                                   # D01: carried to every proposal these rows generate, as an annotation (check_seeds.py allows one machine guard per row, and the existing one stays)
        by[sid]["change_ref"] = (by[sid]["change_ref"] + ";" if by[sid]["change_ref"] else "") + "it22-D01"
    wr(out / "seed_annotations.tsv", [dict(seed_id=sid, annotation="SECOND_SYSTEM_GATE_FAILED", source="hnpc_gse126075_it5_20261029/RESULTS.md section 1") for sid in HNPC_ROWS], ["seed_id", "annotation", "source"])
    tag(by["S116"], "NPY_SIGN_CONTESTED"); by["S116"]["change_ref"] = (by["S116"]["change_ref"] + ";" if by["S116"]["change_ref"] else "") + "it22-B"
    r79 = by["S079"]                                        # latent hazard: a cell-type marker set must never become a gene seed if the ortholog table is completed later
    r79.update(usable_for_generation="no", reason_class="UNUSABLE_MATURITY_OR_COMPOSITION", change_ref="it22-B")
    tag(r79, "COMPOSITION_NOT_REGULATION")
    if a.arm == "hnpc_excluded":
        for r in seeds:
            if r["seed_id"] in HNPC_ROWS:
                r["usable_for_generation"], r["reason_class"], r["change_ref"] = "no", "UNUSABLE_NOT_EVALUABLE", (r["change_ref"] + ";" if r["change_ref"] else "") + "it22-D01-arm"
    wr(out / "seeds.tsv", seeds, cols)
    q = rd(P1 / "questions.tsv")
    qa = rd(HERE / "p3_A_redox" / "proposed_question_Q8.tsv")[0]
    qa["question_id"] = "Q8"
    q.append(qa)
    wr(out / "questions.tsv", q, list(rd(P1 / "questions.tsv")[0]))
    roles = rd(DR / "generation_it10_p1_20261031" / "question_roles.tsv")
    roles.append(rd(HERE / "p3_A_redox" / "proposed_question_roles_Q8.tsv")[0])
    wr(out / "question_roles.tsv", roles, list(roles[0]))
    shutil.copy(P1 / "process_ids.tsv", out / "process_ids.tsv")
    g = rd(P1 / "guards.tsv")
    g += rd(HERE / "p3_A_redox" / "proposed_guard.tsv") + rd(HERE / "p3_B_cellpop" / "proposed_guard_rows.tsv")
    wr(out / "guards.tsv", g, list(g[0]))
    hg = rd(P1 / "hgnc_check.tsv")
    if "NFE2L2" not in {r["symbol"] for r in hg}:
        hg.append(dict(symbol="NFE2L2", hgnc_id="HGNC:7782", approved_symbol="NFE2L2", approved_name="NFE2 like bZIP transcription factor 2", status="Approved", matched_via="symbol",
                       mgd_id_ortholog_link="", rgd_id_ortholog_link=""))
    wr(out / "hgnc_check.tsv", hg, list(hg[0]))
    subprocess.run([sys.executable, str(DR / "generation_it9_p2_20261030" / "p1_adapter.py"), "--p1", str(out), "--out", str(out / "seeds_p1")], check=True, capture_output=True)
    import tempfile                                                             # the IT9 seed-set folder also holds the Q1 sets (tiers A,B,C); carry them so the seed index is complete
    with tempfile.TemporaryDirectory() as t:
        subprocess.run([sys.executable, str(DR / "generation_it9_p2_20261030" / "p1_adapter.py"), "--p1", str(out), "--out", t, "--tiers", "A,B,C"], check=True, capture_output=True)
        for f in Path(t).glob("Q1_*.tsv"):
            shutil.copy(f, out / "seeds_p1" / f.name)
    print("inputs written to", out)


if __name__ == "__main__":
    main()
