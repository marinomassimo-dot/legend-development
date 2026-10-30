#!/usr/bin/env python3
"""IT9 P4b-c literature helper. Europe PMC REST (title/abstract search and PMID abstract fetch), polite retry, every attempt logged.

  lit_p4b_c.py --help
  lit_p4b_c.py search "<europepmc query>" [--label L] [--n 8]    append the hits to literature_search_log.tsv and literature_hits.jsonl
  lit_p4b_c.py fetch PMID [PMID ...]                              append the abstracts to literature_abstracts.jsonl (abstract-level reading only)

Nothing is sent but the query string; no key, no e-mail, no identity. A search count is a count, not a result."""
import argparse, json, sys, time, urllib.parse
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[4]))


def get(url):
    from framework.adapters import _http
    st, p = 0, ""
    for wait in (0, 2, 6, 15):
        if wait:
            time.sleep(wait)
        t0 = time.time()
        st, p = _http.get_json(url, timeout=40)
        with open(HERE / "literature_service_log.tsv", "a") as f:
            f.write(f"{time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\t{st}\t{round(time.time()-t0, 2)}\t{url[:200]}\n")
        if st == 200:
            break
    return st, p


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("search"); s.add_argument("query"); s.add_argument("--label", default=""); s.add_argument("--n", type=int, default=8)
    f = sub.add_parser("fetch"); f.add_argument("pmids", nargs="+")
    a = ap.parse_args()
    if a.cmd == "search":
        url = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({"query": a.query, "format": "json", "resultType": "lite", "pageSize": a.n})
        st, p = get(url)
        hits = (p.get("resultList") or {}).get("result", []) if st == 200 and isinstance(p, dict) else []
        total = p.get("hitCount") if st == 200 and isinstance(p, dict) else None
        with open(HERE / "literature_search_log.tsv", "a") as lg:
            lg.write(f"{time.strftime('%Y-%m-%d', time.gmtime())}\t{a.label}\t{a.query}\t{st}\t{total}\t{len(hits)}\n")
        with open(HERE / "literature_hits.jsonl", "a") as hf:
            for h in hits:
                hf.write(json.dumps({"label": a.label, "pmid": h.get("pmid"), "src": h.get("source"), "id": h.get("id"), "year": h.get("pubYear"), "title": h.get("title"), "journal": h.get("journalTitle")}) + "\n")
                print(h.get("pmid") or h.get("id"), h.get("pubYear"), (h.get("title") or "")[:110])
        print("hitCount", total, "status", st)
    elif a.cmd == "fetch":
        for pm in a.pmids:
            st, p = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({"query": f"EXT_ID:{pm} AND SRC:MED", "format": "json", "resultType": "core"}))
            r = ((p.get("resultList") or {}).get("result") or [None])[0] if st == 200 and isinstance(p, dict) else None
            rec = {"pmid": pm, "status": st, "title": r and r.get("title"), "journal": r and r.get("journalTitle"), "year": r and r.get("pubYear"), "doi": r and r.get("doi"), "abstract": r and r.get("abstractText")}
            with open(HERE / "literature_abstracts.jsonl", "a") as f_:
                f_.write(json.dumps(rec) + "\n")
            print(pm, st, rec["year"], (rec["title"] or "")[:100])
    else:
        ap.print_help()


if __name__ == "__main__":
    main()
