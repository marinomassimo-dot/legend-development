#!/usr/bin/env python3
"""IT17 P3: freeze a prediction and score it later from the frozen copies only.

Offline, stdlib only. `--help` and import touch neither the network nor any file.

  freeze    --out DIR --task TEXT --pool F --selection F [--aux F ...] --rules F --pool-id-col C --top-n N
            Copies pool/selection/aux into DIR/frozen/, writes DIR/FREEZE.json with the real UTC instant,
            git commit SHA, sha256 of every input, the selection, the B1 baseline, method version and the
            design's own minimal-evidence rule. Refuses when an input differs from the committed copy.
  seal      --freeze DIR/FREEZE.json [--addendum DIR/ADDENDUM.json]
            Writes DIR/FREEZE.sha256 (sha256 of FREEZE.json and of the addendum). `freeze` seals automatically;
            `seal` exists for a freeze written before sealing (FREEZE.json is not rewritten).
  evaluate  --freeze DIR/FREEZE.json --outcomes TSV [--descriptive] [--repo PATH]
            Verifies the seal, the frozen copies, the scorer digest and (when the commit is available) the rules
            digest, re-derives pool/selection/baseline from the frozen copies (exit 3 on any mismatch), then scores
            typed outcome rows. Unknown unit ids or non-ISO dates are errors (exit 4).
            Only result == favourable AND objective_match == yes counts as a success; a tested compound with a
            null, contrary, undeterminable or off-objective result does not. One origin_group counts once per unit and
            once toward the minimal-evidence rule however many units it covers.
            Without --descriptive only rows dated after the freeze day count. Exit 2 when the design's minimal
            evidence (determinate origin groups) is not reached: counts are shown, no claim is made.

The real anchor is the git commit plus these digests; the clock value is the tool's own claim.
Outcome TSV columns: unit_id intervention system_context endpoint comparator result objective_match
origin_group pub_date provenance   (result in favourable|null|contrary|undeterminable; objective_match yes|no|unknown)
"""
import argparse
import csv
import datetime
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

METHOD_VERSION = "prospective_eval/1"
RESULTS = ("favourable", "null", "contrary", "undeterminable")
MATCH = ("yes", "no", "unknown")
MIN_DETERMINATE_ORIGINS = 3  # this design's own rule; not a LEGEND-wide threshold


def sha256(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def tsv(p):
    with open(p, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), *a], capture_output=True, text=True, check=True).stdout.strip()


def _num(x):
    try:
        return int(x)
    except (TypeError, ValueError):
        return 0


def b1_baseline(units, mem, id_col):
    """'List what is already tested first': order by WWOX-system assertions summed per unit, ties by id."""
    w = {}
    for m in mem:
        w[m["unit_id"]] = w.get(m["unit_id"], 0) + _num(m.get("wwox_assertions"))
    return sorted((u[id_col] for u in units), key=lambda u: (-w.get(u, 0), u))


def b1_top_units(units, mem, id_col, top_n):
    """Top of B1 without id-tie filler: only units with at least one WWOX-system assertion."""
    w = {}
    for m in mem:
        w[m["unit_id"]] = w.get(m["unit_id"], 0) + _num(m.get("wwox_assertions"))
    return [u for u in b1_baseline(units, mem, id_col)[:top_n] if w.get(u, 0) > 0]


def freeze(a):
    repo = Path(a.repo).resolve()
    out = Path(a.out)
    if (out / "FREEZE.json").exists():
        sys.exit("refused: %s already holds a freeze (a freeze is written once)" % out)
    inputs = {"pool": Path(a.pool), "selection": Path(a.selection), "rules": Path(a.rules)}
    for i, p in enumerate(a.aux or []):
        inputs["aux%d" % i] = Path(p)
    commit = git(repo, "rev-parse", "HEAD")
    for name, p in inputs.items():
        rel = str(p.resolve().relative_to(repo))
        committed = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (commit, rel)], capture_output=True).stdout
        if hashlib.sha256(committed).hexdigest() != sha256(p):
            sys.exit("refused: %s differs from the copy committed at %s (commit first)" % (rel, commit[:12]))
    (out / "frozen").mkdir(parents=True)
    rec_inputs = {}
    for name, p in inputs.items():
        dest = out / "frozen" / p.name
        if name == "rules":  # rules are referenced by digest and commit, not copied (large)
            rec_inputs[name] = {"path": str(p.resolve().relative_to(repo)), "sha256": sha256(p), "copied": False}
            continue
        shutil.copyfile(p, dest)
        rec_inputs[name] = {"path": str(p.resolve().relative_to(repo)), "frozen_copy": "frozen/" + p.name,
                            "sha256": sha256(dest), "copied": True}
    pool = tsv(inputs["pool"])
    sel = [r for r in tsv(inputs["selection"]) if r.get("view", "general") == a.view]
    sel.sort(key=lambda r: int(r["position_in_list"]))
    top = [r[a.pool_id_col] for r in sel][: a.top_n]
    aux = [tsv(p) for n, p in inputs.items() if n.startswith("aux")]
    rec = {
        "method_version": METHOD_VERSION,
        "scorer_sha256": sha256(__file__),
        "frozen_at_utc": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "git_commit": commit,
        "task": a.task,
        "pool_size": len(pool),
        "pool_ids": [r[a.pool_id_col] for r in pool],
        "selection_view": a.view,
        "selection": top,
        "selection_objective": {r[a.pool_id_col]: r.get("objective", "") for r in sel[: a.top_n]},
        "baseline_B1_order": b1_baseline(pool, aux[0], a.pool_id_col) if aux else None,
        "baseline_B1_top": (b1_top_units(pool, aux[0], a.pool_id_col, a.top_n) if aux else None),
        "top_n": a.top_n,
        "pool_id_col": a.pool_id_col,
        "rules_version_note": a.rules_note,
        "inputs": rec_inputs,
        "minimal_evidence_rule": {"determinate_origin_groups_at_least": MIN_DETERMINATE_ORIGINS,
                                  "scope": "this design only; not a LEGEND-wide threshold"},
        "success_definition": "result == favourable AND objective_match == yes, one origin_group counted once per unit, "
                              "published after the freeze day; null, contrary, undeterminable and off-objective results are never successes",
    }
    (out / "FREEZE.json").write_text(json.dumps(rec, indent=1, sort_keys=True, ensure_ascii=False) + "\n", encoding="utf-8")
    seal(out / "FREEZE.json", None)
    print(json.dumps({k: rec[k] for k in ("frozen_at_utc", "git_commit", "selection", "pool_size")}, indent=1))
    return 0


def seal(freeze_path, addendum):
    fp = Path(freeze_path)
    side = fp.parent / "FREEZE.sha256"
    if side.exists():
        sys.exit("refused: %s already exists" % side)
    ad = Path(addendum) if addendum else fp.parent / "ADDENDUM.json"
    lines = ["%s  FREEZE.json" % sha256(fp)]
    if ad.exists():
        lines.append("%s  ADDENDUM.json" % sha256(ad))
    side.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return 0


def verify(freeze_path, repo=None):
    """-> (record with derived fields, problems). Problems are strings; empty means every check passed."""
    fp = Path(freeze_path)
    bad = []
    side = fp.parent / "FREEZE.sha256"
    seals = {}
    if side.exists():
        for ln in side.read_text(encoding="utf-8").split("\n"):
            if ln.strip():
                h, n = ln.split()
                seals[n] = h
    else:
        bad.append("no FREEZE.sha256 seal")
    if seals.get("FREEZE.json") != sha256(fp):
        bad.append("FREEZE.json differs from its seal")
    rec = json.loads(fp.read_text(encoding="utf-8"))
    ad_path = fp.parent / "ADDENDUM.json"
    ad = {}
    if ad_path.exists():
        if seals.get("ADDENDUM.json") != sha256(ad_path):
            bad.append("ADDENDUM.json differs from its seal")
        ad = json.loads(ad_path.read_text(encoding="utf-8"))
    for name, i in rec["inputs"].items():
        if not i["copied"]:
            continue
        p = fp.parent / i["frozen_copy"]
        if not p.exists() or sha256(p) != i["sha256"]:
            bad.append("frozen input " + name)
    allowed = {rec["scorer_sha256"]} | {v["sha256"] for v in ad.get("scorer_versions", [])}
    if sha256(__file__) not in allowed:
        bad.append("running scorer sha256 is not the frozen one nor a sealed addendum version")
    if repo is not None:
        r = rec["inputs"]["rules"]
        out = subprocess.run(["git", "-C", str(repo), "show", "%s:%s" % (rec["git_commit"], r["path"])], capture_output=True)
        if out.returncode == 0 and hashlib.sha256(out.stdout).hexdigest() != r["sha256"]:
            bad.append("rules file at the frozen commit differs from the recorded digest")
        rec["_rules_checked"] = out.returncode == 0
    if not bad:  # re-derive from the digest-checked copies and compare with the record
        top_n = rec.get("top_n") or ad.get("top_n") or len(rec["selection"])
        col = rec.get("pool_id_col") or ad.get("pool_id_col") or "unit_id"
        d = fp.parent
        pool = tsv(d / rec["inputs"]["pool"]["frozen_copy"])
        sel = [r for r in tsv(d / rec["inputs"]["selection"]["frozen_copy"]) if r.get("view", "general") == rec["selection_view"]]
        sel.sort(key=lambda r: int(r["position_in_list"]))
        rec["selection"], derived_sel = [r[col] for r in sel][:top_n], rec["selection"]
        rec["pool_ids"], derived_pool = [r[col] for r in pool], rec["pool_ids"]
        if rec["selection"] != derived_sel or rec["pool_ids"] != derived_pool:
            bad.append("selection or pool in FREEZE.json differs from the frozen copies")
        if "aux0" in rec["inputs"]:
            mem = tsv(d / rec["inputs"]["aux0"]["frozen_copy"])
            if b1_baseline(pool, mem, col) != rec["baseline_B1_order"]:
                bad.append("baseline order differs from the frozen copies")
            rec["baseline_B1_top"] = b1_top_units(pool, mem, col, top_n)
    return rec, bad


def valid_date(x):
    try:
        return len(x) == 10 and datetime.date.fromisoformat(x).isoformat() == x
    except (TypeError, ValueError):
        return False


def score(rec, rows, descriptive):
    fday = rec["frozen_at_utc"][:10]
    sel = set(rec["selection"])
    b1 = set(rec["baseline_B1_top"] or [])
    pool = set(rec["pool_ids"])
    elig, excluded = [], []
    for r in rows:
        if r.get("unit_id") not in pool:
            raise ValueError("unit id not in the frozen pool: %r" % r.get("unit_id"))
        if not valid_date(r.get("pub_date")):
            raise ValueError("pub_date is not ISO YYYY-MM-DD: %r" % r.get("pub_date"))
        if r["result"] not in RESULTS or r["objective_match"] not in MATCH:
            excluded.append((r.get("unit_id"), "invalid result/objective_match"))
        elif not descriptive and not r["pub_date"] > fday:
            excluded.append((r["unit_id"], "not after freeze day"))
        else:
            elig.append(r)
    per = {}  # (unit, origin_group) -> set of (result, match)
    for r in elig:
        per.setdefault((r["unit_id"], r["origin_group"]), set()).add((r["result"], r["objective_match"]))
    cell = {}
    for (u, g), s in per.items():
        if len(s) > 1:
            cell[(u, g)] = "undeterminable"  # conflicting rows of one origin: unresolved, not netted out
            continue
        (res, m), = s
        if res == "undeterminable" or m == "unknown":
            cell[(u, g)] = "undeterminable"  # unknown stays unknown
        elif m == "no":
            cell[(u, g)] = "off_objective"  # a result on another endpoint (e.g. safety) is kept visible, never netted
        else:
            cell[(u, g)] = {"favourable": "success", "null": "null", "contrary": "contrary"}[res]
    kinds = ("success", "null", "contrary", "off_objective", "undeterminable")
    units = {}
    for (u, g), k in cell.items():
        units.setdefault(u, {x: 0 for x in kinds})[k] += 1
    det_groups = {g for (u, g), k in cell.items() if k in ("success", "null", "contrary")}  # shared origin counts once across units
    determinate = len(det_groups)
    arm = {}
    for name, S in (("selection", sel), ("B1_top", b1)):
        arm[name] = {"units_with_outcome": sorted(u for u in units if u in S),
                     "units_with_success": sorted(u for u in units if u in S and units[u]["success"]),
                     "units_with_contrary": sorted(u for u in units if u in S and units[u]["contrary"]),
                     "units_with_null": sorted(u for u in units if u in S and units[u]["null"]),
                     "units_only_off_objective_or_undeterminable": sorted(u for u in units if u in S and not any(units[u][x] for x in ("success", "null", "contrary")))}
    ok = determinate >= rec["minimal_evidence_rule"]["determinate_origin_groups_at_least"]
    return {"descriptive": descriptive, "rows_used": len(elig), "rows_excluded": excluded,
            "origin_cells": len(cell), "determinate_origin_groups": determinate, "per_unit": units, "arms": arm,
            "claim": ("scored; compare against B1 first, not against chance" if ok and not descriptive else
                      ("descriptive only (no claim)" if descriptive else
                       "none: fewer than %d determinate origin groups after the freeze" % rec["minimal_evidence_rule"]["determinate_origin_groups_at_least"]))}, (ok and not descriptive)


def evaluate(a):
    rec, bad = verify(a.freeze, a.repo)
    if bad:
        print("REFUSED: %s" % "; ".join(bad), file=sys.stderr)
        return 3
    try:
        res, ok = score(rec, tsv(a.outcomes), a.descriptive)
    except ValueError as e:
        print("ERROR: %s" % e, file=sys.stderr)
        return 4
    res["rules_digest_checked_against_git"] = rec.get("_rules_checked", False)
    res["frozen_at_utc"] = rec["frozen_at_utc"]
    res["git_commit"] = rec["git_commit"]
    print(json.dumps(res, indent=1, sort_keys=True, ensure_ascii=False))
    return 0 if ok or a.descriptive else 2


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    f = sub.add_parser("freeze")
    f.add_argument("--out", required=True)
    f.add_argument("--repo", default=".")
    f.add_argument("--task", required=True)
    f.add_argument("--pool", required=True)
    f.add_argument("--selection", required=True)
    f.add_argument("--aux", action="append")
    f.add_argument("--rules", required=True)
    f.add_argument("--rules-note", default="")
    f.add_argument("--pool-id-col", default="unit_id")
    f.add_argument("--view", default="general")
    f.add_argument("--top-n", type=int, default=8)
    e = sub.add_parser("evaluate")
    e.add_argument("--freeze", required=True)
    e.add_argument("--outcomes", required=True)
    e.add_argument("--descriptive", action="store_true")
    e.add_argument("--repo", default=None, help="git checkout holding the frozen commit, to verify the rules digest")
    sl = sub.add_parser("seal")
    sl.add_argument("--freeze", required=True)
    sl.add_argument("--addendum")
    a = ap.parse_args(argv)
    if a.cmd == "freeze":
        return freeze(a)
    if a.cmd == "evaluate":
        return evaluate(a)
    if a.cmd == "seal":
        return seal(a.freeze, a.addendum)
    ap.print_help()
    return 0


if __name__ == "__main__":
    sys.exit(main())
