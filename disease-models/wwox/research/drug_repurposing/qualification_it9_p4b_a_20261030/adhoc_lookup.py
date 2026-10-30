#!/usr/bin/env python3
"""Logged ad hoc lookups used while reading primary papers (Europe PMC search / abstract / full text). Every call appends one row to adhoc_log.tsv.
  adhoc_lookup.py --help
  adhoc_lookup.py search "<europepmc query>" [--n 10]     list title, year, journal, PMID, PMCID
  adhoc_lookup.py abstract PMID [PMID ...]               print abstract (first 1500 characters)
  adhoc_lookup.py fulltext PMCID OUTFILE                 save the Europe PMC full-text XML (OA subset) to OUTFILE
Standard library only; no identifying header, no e-mail address."""
import json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent
LOG = HERE / "adhoc_log.tsv"
UA = "legend-public-research/1.0 (non-commercial literature and database qualification)"
BASE = "https://www.ebi.ac.uk/europepmc/webservices/rest"


def get(url, raw=False):
    status, body = 0, ""
    for wait in (0, 2, 6, 15):
        time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=60) as r:
                status, body = r.status, r.read().decode("utf-8", "replace")
            break
        except Exception as e:
            status, body = getattr(e, "code", 0), str(e)[:100]
    new = not LOG.exists()
    with open(LOG, "a") as f:
        if new:
            f.write("date\tstatus\tbytes\turl\n")
        f.write(f"2026-10-30\t{status}\t{len(body)}\t{url[:230]}\n")
    return status, body


def main():
    a = sys.argv[1:]
    if not a or a[0] in ("-h", "--help"):
        print(__doc__); return
    if a[0] == "search":
        n = int(a[a.index("--n") + 1]) if "--n" in a else 10
        s, b = get(f"{BASE}/search?query={urllib.parse.quote(a[1])}&resultType=lite&format=json&pageSize={n}&sort=CITED%20desc")
        d = json.loads(b) if s == 200 else {}
        print("hitCount", d.get("hitCount"))
        for r in d.get("resultList", {}).get("result", []):
            print(r.get("pmid"), r.get("pmcid"), r.get("pubYear"), r.get("journalTitle"), "|", (r.get("title") or "")[:140])
    elif a[0] == "abstract":
        for p in a[1:]:
            s, b = get(f"{BASE}/search?query=EXT_ID:{p}%20AND%20SRC:MED&resultType=core&format=json")
            r = (json.loads(b).get("resultList", {}).get("result") or [{}])[0] if s == 200 else {}
            print("##", p, r.get("pubYear"), r.get("journalTitle"), "OA", r.get("isOpenAccess"), r.get("pmcid"), r.get("doi")); print(r.get("title"))
            print(re.sub(r"<[^>]+>", "", r.get("abstractText") or "")[:1500]); print()
    elif a[0] == "fulltext":
        s, b = get(f"{BASE}/{a[1]}/fullTextXML")
        if s == 200:
            Path(a[2]).write_text(b)
        print(s, len(b))


if __name__ == "__main__":
    main()
