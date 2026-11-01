"""IT15 Q-B step 1: target-first ChEMBL retrieval for GSK3B/GSK3A (human and rodent single-protein targets).
Uses framework/adapters/_http.get_json (the adapter's own door). Retries: at most 2 per request, 8 s pause; every request is logged to perimeter_log.tsv.
Raw bodies go to the scratchpad given by --raw (CC BY-SA 3.0 copies are not committed). Usage: retrieve_qb.py --raw DIR --stage targets|acts"""
import sys, os, json, time, argparse, hashlib
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), *([".."] * 5)))
sys.path.insert(0, REPO)
from framework.adapters import _http, chembl
H = os.path.dirname(os.path.abspath(__file__))
BASE = chembl.BASE
LOG = os.path.join(H, "perimeter_log.tsv")

def log(*f):
    new = not os.path.exists(LOG)
    with open(LOG, "a") as fh:
        if new: fh.write("utc\tstage\trequest\tattempt\thttp_status\tresult\n")
        fh.write("\t".join(str(x) for x in (_http.now_utc(),) + f) + "\n")

def get(url, stage):
    for attempt in (1, 2, 3):          # first try + at most two retries
        st, p = _http.get_json(url, timeout=60)
        ok = st == 200 and isinstance(p, dict)
        log(stage, url, attempt, st, "ok" if ok else "NOT RETRIEVED (" + str(p)[:80].replace("\t", " ").replace("\n", " ") + ")")
        if ok or st in (400, 404): return st, p
        if attempt < 3: time.sleep(8)
    return st, p

if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--raw", required=True); ap.add_argument("--stage", required=True)
    a = ap.parse_args(); os.makedirs(a.raw, exist_ok=True)
    if a.stage == "targets":
        out = {}
        for gene, acc in (("GSK3B human", "P49841"), ("GSK3A human", "P49840"), ("Gsk3b rat", "P18266"), ("Gsk3b mouse", "Q9WV60"), ("Gsk3a rat", "P18265"), ("Gsk3a mouse", "Q2NL51")):
            st, p = get(f"{BASE}/target.json?target_components__accession={acc}&limit=50", "targets")
            out[acc] = {"label": gene, "http": st, "targets": [(t["target_chembl_id"], t["pref_name"], t["organism"], t["target_type"]) for t in (p.get("targets") or [])] if isinstance(p, dict) else None}
        json.dump(out, open(os.path.join(a.raw, "targets.json"), "w"), indent=1)
        print(json.dumps(out, indent=1))
    elif a.stage == "acts":
        # full census of single-protein targets, paged 1000 at a time, types IC50/Ki/Kd (EC50 excluded by pre-registration)
        import urllib.parse
        for tid in ("CHEMBL262", "CHEMBL2850", "CHEMBL3669", "CHEMBL1075321", "CHEMBL1075224", "CHEMBL2176843"):
            rows, off, total = [], 0, None
            while True:
                url = f"{BASE}/activity.json?target_chembl_id={tid}&standard_type__in=IC50,Ki,Kd&limit=1000&offset={off}"
                st, p = get(url, "acts:" + tid)
                if not isinstance(p, dict) or st != 200:
                    print(tid, "STOP at offset", off, "not retrieved"); break
                total = p["page_meta"]["total_count"]; pg = p.get("activities") or []
                rows += pg; off += len(pg)
                if not pg or not p["page_meta"].get("next"): break
            json.dump({"target": tid, "total_count": total, "retrieved": len(rows), "rows": rows}, open(os.path.join(a.raw, f"acts_{tid}.json"), "w"))
            log("summary", tid, "-", "-", f"total_count={total} retrieved={len(rows)} truncated={total is not None and len(rows) < total}")
            print(tid, total, len(rows))

# stage "acts_small": the limit=1000 page failed (HTTP 500) for these; a different request form (limit=200 pages) is tried once per page with the same retry rule.
if __name__ == "__main__" and a.stage == "acts_small":
    for tid, start in (("CHEMBL262", 7000), ("CHEMBL2850", 0), ("CHEMBL3669", 0), ("CHEMBL1075321", 0)):
        rows, off, total = [], start, None
        while True:
            url = f"{BASE}/activity.json?target_chembl_id={tid}&standard_type__in=IC50,Ki,Kd&limit=200&offset={off}"
            st, p = get(url, "acts_small:" + tid)
            if not isinstance(p, dict) or st != 200:
                print(tid, "STOP at offset", off); break
            total = p["page_meta"]["total_count"]; pg = p.get("activities") or []
            rows += pg; off += len(pg)
            if not pg or not p["page_meta"].get("next"): break
        json.dump({"target": tid, "start_offset": start, "total_count": total, "retrieved": len(rows), "rows": rows}, open(os.path.join(a.raw, f"actsS_{tid}.json"), "w"))
        log("summary_small", tid, "-", "-", f"start={start} total_count={total} retrieved={len(rows)} complete={total is not None and start + len(rows) >= total}")
        print(tid, total, len(rows))
