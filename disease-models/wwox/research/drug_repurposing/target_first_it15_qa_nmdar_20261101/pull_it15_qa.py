"""IT15 Q-A target-first pull. Uses framework/adapters/chembl.py (uniprot -> targets; target -> activities per standard_type).
Retry policy: at most 2 retries (pause 6 s) on HTTP 5xx / transport failure; every failed request is logged, never looped.
--help is safe. Stage A (default): accession -> targets. --activities: per target and type. --molecules IDS: molecule-first pull.
Raw adapter outputs go to raw/ as json."""
import argparse, json, os, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.abspath(os.path.join(HERE, "../../../../..")))
from framework.adapters import chembl, _http
ACC = {"GRIN1": "Q05586", "GRIN2A": "Q12879", "GRIN2B": "Q13224", "GRIN2C": "Q14957", "GRIN2D": "O15399"}
FAILS = []
def fetch(url, params=None, body=None, timeout=60):
    for k in range(3):
        st, p = _http.get_json(url, params, body, timeout)
        if st == 200 or (st and st < 500):
            return st, p
        FAILS.append({"url": url, "http": st, "attempt": k + 1, "text": str(p)[:120]})
        if k < 2: time.sleep(6)
    return st, p
def save(name, obj):
    os.makedirs(os.path.join(HERE, "raw"), exist_ok=True)
    json.dump(obj, open(os.path.join(HERE, "raw", name), "w"))
def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--stage", choices=["targets", "activities", "molecules"], default="targets")
    ap.add_argument("--targets", default="", help="comma list of ChEMBL target ids (activities stage); default = all found from accession queries")
    ap.add_argument("--molecules", default="")
    a = ap.parse_args()
    if a.stage == "targets":
        for g, acc in ACC.items():
            o = chembl.query({"uniprot": acc}, fetch=fetch); save(f"targets_{g}.json", o)
            print(g, acc, o["status"], len(o["hits"]), o.get("error", ""))
    elif a.stage == "activities":
        tids = {}
        for t in [x for x in a.targets.split(",") if x]: tids[t] = {"target_type": "?", "organism": "?"}
        for g in ([] if a.targets else ACC):
            for h in json.load(open(os.path.join(HERE, "raw", f"targets_{g}.json")))["hits"]:
                tids.setdefault(h["target_chembl_id"], h)
        for t, h in sorted(tids.items()):
            for ty in ("IC50", "Ki", "Kd", "EC50"):
                fn = f"act_{t}_{ty}.json"
                if os.path.exists(os.path.join(HERE, "raw", fn)): continue
                o = chembl.query({"target": t, "types": [ty], "max_rows": 2000}, fetch=fetch); save(fn, o)
                print(t, h["target_type"], h["organism"], ty, o["status"], o.get("retrieved"), o.get("total_count"), "TRUNC" if o.get("truncated") else "", o.get("error", ""), flush=True)
    else:
        for m in a.molecules.split(","):
            fn = f"mol_{m}.json"
            o = chembl.query({"molecule": m, "max_rows": 2000}, fetch=fetch); save(fn, o)
            print(m, o["status"], o.get("retrieved"), o.get("total_count"), "TRUNC" if o.get("truncated") else "", o.get("error", ""), flush=True)
    json.dump(FAILS, open(os.path.join(HERE, "raw", f"failures_{a.stage}_{int(time.time())}.json"), "w"), indent=0)
    print("failed requests logged:", len(FAILS))
if __name__ == "__main__": main()
