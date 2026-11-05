#!/usr/bin/env python3
"""Check the challenges carried by the steps of a mandate record: the trigger of an inverse research batch and the proof that its result returned.

    python3 framework/scripts/challenge_batch.py check --task <TASK_ID> [--ledger PATH]
    python3 framework/scripts/challenge_batch.py --help

A challenge is NOT a new registry: it is an optional `challenge` object on a step of the record `mandate_continuity.py` already reads (`ledger/tasks/<actor>/<TASK_ID>.json`).
Required text fields: id, origin (record paths), decision_at_stake, available_knowledge, decisive_uncertainty, discriminating_outcomes, prior_work, resources, reevaluate_when,
nature (identity_or_measure -> targeted_reading | shared_premise -> thematic_batch | need_without_interpretation -> exploratory_batch). Optional: sources (study ids),
reopen_reason, returned (paths of consumers that must carry the challenge id).
`check` prints, per challenge: the routing by nature; for each source its standing depth in the receipt ledger; DUPLICATE_NO_NEW_INFORMATION when every source was already read at
partial or full depth and no `reopen_reason` is given (a motivated re-evaluation stays possible); and for each `returned` path whether it exists and names the challenge id.
NAMES_ID / LACKS_ID is a TRACEABILITY check (the file mentions the id). It does not show that the result was read or that anything changed: for that, show the persisted result, the consumer input that reads it, the command that regenerates the output and the diff
(see disease-models/wwox/research/drug_repurposing/consumption_it29_p9_20261105/ for the pattern). A fixture carrying only the id is not a demonstration of consumption.
It reads shared origins from the ledger by study id only: no detected dependency does not certify independence. Offline, standard library only. Exit 1 on a malformed challenge."""
import sys
if __name__ == "__main__" and (len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help")):
    print(__doc__); raise SystemExit(0)
import argparse, json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REQUIRED = ("id", "origin", "decision_at_stake", "available_knowledge", "decisive_uncertainty", "discriminating_outcomes", "prior_work", "resources", "reevaluate_when", "nature")
ROUTES = {"identity_or_measure": "targeted_reading", "shared_premise": "thematic_batch", "need_without_interpretation": "exploratory_batch"}
DEPTH_RANK = {"abstract_only": 1, "partial_fulltext_read": 2, "complete_fulltext_read": 3}


def challenges(record):
    for key, block in record.items():
        if key.startswith("AUTHORISED_QUEUE") and isinstance(block, dict):
            for obj, body in block.items():
                if isinstance(body, dict):
                    for i, st in enumerate(body.get("steps") or []):
                        if isinstance(st, dict) and isinstance(st.get("challenge"), dict):
                            yield f"{obj}[{i}]", st["challenge"]


def depth_by_study(ledger):
    best = {}
    if ledger.exists():
        for line in ledger.read_text(encoding="utf-8").splitlines():
            try:
                d = json.loads(line)
            except ValueError:
                continue
            sid = d.get("study_id")
            keys = [str(v).replace("PMID", "") for v in sid.values() if v] if isinstance(sid, dict) else [str(sid).replace("PMID", "")]     # study_id is {doi, pmid}; either names the study
            r = DEPTH_RANK.get(d.get("evidence_depth"), 0)
            for k in keys:
                best[k] = max(best.get(k, 0), r)
    return best


def assess(ch, depth, root=ROOT):
    problems = [f for f in REQUIRED if not str(ch.get(f) or "").strip() and not (f == "origin" and ch.get(f))]
    if ch.get("nature") not in ROUTES:
        problems.append("nature:" + str(ch.get("nature")))
    srcs = [str(s) for s in ch.get("sources") or []]
    standing = {s: depth.get(s, 0) for s in srcs}
    dup = bool(srcs) and all(v >= 2 for v in standing.values()) and not str(ch.get("reopen_reason") or "").strip()
    ret = {p: ((root / p).exists() and ch.get("id", "") in (root / p).read_text(encoding="utf-8", errors="replace")) for p in ch.get("returned") or []}
    return dict(id=ch.get("id"), problems=problems, route=ROUTES.get(ch.get("nature")), standing=standing, duplicate=dup, returned=ret)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("cmd", choices=["check"])
    ap.add_argument("--task", required=True)
    ap.add_argument("--ledger", default=str(ROOT / "disease-models/wwox/registries/fulltext_read_receipts.jsonl"))
    a = ap.parse_args()
    rec = json.loads(next(ROOT.glob(f"ledger/tasks/*/{a.task}.json")).read_text(encoding="utf-8"))
    depth = depth_by_study(Path(a.ledger))
    bad = 0
    for where, ch in challenges(rec):
        r = assess(ch, depth)
        bad += bool(r["problems"])
        print(f"{where} {r['id']}: route={r['route']} problems={r['problems'] or 'none'} duplicate={'DUPLICATE_NO_NEW_INFORMATION' if r['duplicate'] else 'no'}")
        print("  sources (0 unread, 1 abstract, 2 partial, 3 full):", r["standing"])
        for p, ok in r["returned"].items():
            print("  returned:", "NAMES_ID " if ok else "LACKS_ID ", p)
    raise SystemExit(1 if bad else 0)


if __name__ == "__main__":
    main()
