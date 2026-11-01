#!/usr/bin/env python3
"""IT18 P3 route B: ToolUniverse DrugCentral_get_targets on a fixed sample, compared with route A (direct file).

  sample  --catalog F --needs F --out F               write the 20-compound sample (rule in README; offline)
  run     --sample F --out F                          call ToolUniverse (must run in an isolated venv holding tooluniverse)
  compare --sample F --tu F --dc F --unichem F --catalog F --out F [--inchikeys F]
                                                      same compounds, route A rows vs route B rows (offline)
--help and import read and write nothing and never import tooluniverse.
"""
import argparse
import hashlib
import json
import sys
import time
from pathlib import Path

DISCORDANT_PARENTS = ["CHEMBL1420", "CHEMBL1614652", "CHEMBL493", "CHEMBL709"]


def _h(x):
    return hashlib.sha256(x.encode()).hexdigest()


def cmd_sample(a):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import dc_direction as dcd
    module = dcd.dt.load_module(a.catalog)
    uni, _ = dcd.module_universe(a.catalog, a.needs)
    upar = sorted({p for p, _ in uni} - set(DISCORDANT_PARENTS), key=_h)[:8]
    rest = sorted({p for p, _ in module} - set(upar) - set(DISCORDANT_PARENTS) - {p for p, _ in uni}, key=_h)[:8]
    ids = DISCORDANT_PARENTS + upar + rest
    Path(a.out).write_text("\n".join(ids) + "\n", encoding="utf-8")
    print(len(ids), "compounds")


def cmd_run(a):
    from tooluniverse import ToolUniverse  # only here: the isolated venv provides it
    ids = Path(a.sample).read_text().split()
    t0 = time.time()
    tu = ToolUniverse()
    tu.load_tools()
    load_s = time.time() - t0
    out = {"load_tools_seconds": round(load_s, 2), "calls": []}
    for cid in ids:
        t = time.time()
        try:
            r = tu.run({"name": "DrugCentral_get_targets", "arguments": {"chem_id": cid}})
            err = None
        except Exception as exc:  # recorded, not hidden
            r, err = None, f"{type(exc).__name__}: {exc}"
        out["calls"].append({"chembl": cid, "seconds": round(time.time() - t, 2), "error": err, "result": r})
    Path(a.out).write_text(json.dumps(out, indent=1, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({"load_tools_seconds": out["load_tools_seconds"], "n": len(ids),
                      "errors": sum(1 for c in out["calls"] if c["error"])}))


def cmd_compare(a):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    import csv
    import gzip
    import dc_direction as dcd
    ids = Path(a.sample).read_text().split()
    tu = json.loads(Path(a.tu).read_text())
    uc = dcd.load_unichem(a.unichem)
    if a.inchikeys:
        uc, _ = dcd.augment_with_inchikey(uc, a.inchikeys, a.catalog)
    pmap = dcd.dt.parent_map(a.catalog)
    direct = {c: set() for c in ids}
    with gzip.open(a.dc, "rt", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            if row["ORGANISM"] != "Homo sapiens" or not row["ACTION_TYPE"].strip():
                continue
            for c in uc.get(row["STRUCT_ID"].strip(), ()):
                p = pmap.get(c, c)
                if p in direct:
                    for u in dcd.dt._split_ids(row["ACCESSION"]):
                        direct[p].add((u, row["ACTION_TYPE"].strip().upper(), dcd.origin_of(row)))
    rows = []
    for call in tu["calls"]:
        c = call["chembl"]
        res = call["result"] if isinstance(call["result"], dict) else {}
        tg = (res.get("data") or {}).get("targets") or []
        b = set()
        has_moa_source = any("moa_source" in t for t in tg)
        for t in tg:
            if t.get("organism") == "Homo sapiens" and (t.get("action_type") or "").strip():
                for u in t.get("uniprot_ids") or []:
                    b.add((u, t["action_type"].strip().upper()))
        a_pairs = {(u, act) for u, act, _ in direct[c]}
        rows.append({"chembl": c, "seconds": call["seconds"], "status": res.get("status") or ("exception" if call["error"] else "none"),
                     "error": (call["error"] or res.get("error") or "")[:160],
                     "route_a_action_pairs": len(a_pairs), "route_b_action_pairs": len(b),
                     "both": len(a_pairs & b), "only_a": len(a_pairs - b), "only_b": len(b - a_pairs),
                     "route_b_origin_field": "act_source only" if tg and not has_moa_source else ("moa_source" if has_moa_source else "n/a"),
                     "route_a_independent_origin_pairs": len({(u, act) for u, act, o in direct[c] if dcd.origin_class(o) == "INDEPENDENT"}),
                     "route_b_total_targets_reported": (res.get("metadata") or {}).get("total_targets", "")})
    with open(a.out, "w", encoding="utf-8") as f:
        f.write("\t".join(rows[0]) + "\n")
        for r in rows:
            f.write("\t".join(str(r[k]) for k in rows[0]) + "\n")
    tot = {k: sum(r[k] for r in rows) for k in ("route_a_action_pairs", "route_b_action_pairs", "both", "only_a", "only_b")}
    tot["seconds"] = round(sum(r["seconds"] for r in rows), 2)
    tot["errors"] = sum(1 for r in rows if r["error"])
    print(json.dumps(tot))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("sample")
    for k in ("catalog", "needs", "out"):
        s.add_argument("--" + k, required=True)
    r = sub.add_parser("run")
    for k in ("sample", "out"):
        r.add_argument("--" + k, required=True)
    c = sub.add_parser("compare")
    for k in ("sample", "tu", "dc", "unichem", "catalog", "out"):
        c.add_argument("--" + k, required=True)
    c.add_argument("--inchikeys", help="amendment: add the exact InChIKey join (dc_inchikeys.py output)")
    a = ap.parse_args(argv)
    if not a.cmd:
        ap.print_help()
        return 0
    {"sample": cmd_sample, "run": cmd_run, "compare": cmd_compare}[a.cmd](a)
    return 0


if __name__ == "__main__":
    sys.exit(main())
