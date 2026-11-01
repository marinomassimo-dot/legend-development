#!/usr/bin/env python3
"""IT18 P1.2: old vs new query construction on the SAME declared questions, same live channels, same day.

Usage: query_compare.py OLD_SCOUT_PY OUT_DIR [--run]
Without --run it only prints the declared question set and the two query strings per question (no network).
Selection rule (declared before any hit was seen): all reopen: and work_order: questions of the plan at HEAD, sorted by
id, every third one starting at the first, at most 10.
"""
import importlib.util, json, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
sys.path.insert(0, str(ROOT / "framework" / "scripts"))
import scout_daily as new  # noqa: E402


def load(path):
    spec = importlib.util.spec_from_file_location("scout_old", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main():
    old = load(sys.argv[1])
    out = Path(sys.argv[2]); out.mkdir(parents=True, exist_ok=True)
    sha = subprocess.check_output(["git", "rev-parse", "HEAD"], text=True, cwd=ROOT).strip()
    plan, extracts = new.resolve_plan(None, None, {"main_sha": sha})
    items = [dict(it, path=p, blob=e["blob"], sha=sha) for p, e in extracts.items() for it in e["items"]]
    q_new = {q["id"]: q for q in new.build_questions(items)[0]}
    q_old = {q["id"]: q for q in old.build_questions(items)[0]}
    ids = sorted(i for i in q_new if i.startswith(("reopen:", "work_order:")) and i in q_old)[::3][:10]
    rows = []
    for i in ids:
        rows.append({"id": i, "need": q_new[i]["gap"], "old_kw": q_old[i]["kw"], "new_kw": q_new[i]["kw"],
                     "old_gh": q_old[i]["gh"], "new_gh": q_new[i]["gh"], "old_epmc": q_old[i]["epmc"], "new_epmc": q_new[i]["epmc"]})
    (out / "declared_questions.json").write_text(json.dumps({"sha": sha, "rule": __doc__.split("Selection rule")[1].strip(), "rows": rows}, indent=1))
    for r in rows:
        print(r["id"][-40:], "| OLD:", r["old_kw"], "| NEW:", r["new_kw"])
    if "--run" not in sys.argv:
        return
    import datetime as dt
    now = dt.datetime.now(dt.timezone.utc)
    results = []
    for r in rows:
        for arm, mod, q in (("old", old, q_old[r["id"]]), ("new", new, q_new[r["id"]])):
            calls = []
            def opener(url, *a, **k):
                calls.append(url)
                return mod.http(url, *a, **k)
            res = mod.discover_theme(q, {}, opener=opener, now=now, budget={"n": 0})
            results.append({"id": r["id"], "arm": arm, "calls": len(calls),
                            "channels": {c: {"calls": v["calls"], "errors": v["errors"]} for c, v in res["channels"].items()} if "channels" in res else None,
                            "items": [{k: it.get(k) for k in ("channel", "kind", "title", "url", "when", "desc")} for it in res.get("items", [])]})
            print(r["id"][-30:], arm, "calls", len(calls), "items", len(res.get("items", [])), flush=True)
    (out / "raw_results.json").write_text(json.dumps(results, indent=1))


if __name__ == "__main__":
    if len(sys.argv) < 3 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        sys.exit(0)
    main()
