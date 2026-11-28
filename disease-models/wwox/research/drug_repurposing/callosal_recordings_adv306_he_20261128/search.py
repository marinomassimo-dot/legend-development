"""ADV-306: dated plain GET/POST searches of public data repositories. Output: queries.tsv, hits.tsv."""
import json, sys, time, urllib.parse, urllib.request, urllib.error
from pathlib import Path

OUT = Path(sys.argv[1] if len(sys.argv) > 1 else ".")
UA = "legend-research-client/1.0"
Q = {
    "Q1": '"compound action potential" "corpus callosum"',
    "Q2": "callosal conduction velocity myelin mouse",
    "Q3": '"optic nerve" "compound action potential" mouse',
    "Q4": "hypomyelination electrophysiology conduction",
    "Q5": "shiverer conduction",
    "Q6": "Wwox electrophysiology",
    "Q7": '4-aminopyridine "compound action potential"',
    "Q8": "clemastine conduction",
}


def get(url, data=None):
    req = urllib.request.Request(url, data=data, headers={"User-Agent": UA, "Accept": "application/json",
                                                          "Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=40) as r:
        return json.loads(r.read(8_000_000))


def plain(q):
    return q.replace('"', "")


def datacite(q):
    words = [w for w in __import__("shlex").split(q)]
    query = " AND ".join(f'"{w}"' if " " in w else w for w in words)
    j = get("https://api.datacite.org/dois?page[size]=25&resource-type-id=dataset&query=" + urllib.parse.quote(query))
    return j["meta"]["total"], [(d["id"], d["attributes"]["titles"][0]["title"]) for d in j["data"]]


def zenodo(q):
    j = get("https://zenodo.org/api/records?size=25&q=" + urllib.parse.quote(q if '"' in q else " AND ".join(q.split())))
    h = j["hits"]
    return h["total"], [(x.get("doi", str(x["id"])), x["metadata"]["title"] + " [" + x["metadata"]["resource_type"]["type"] + "]") for x in h["hits"]]


def figshare(q):
    j = get("https://api.figshare.com/v2/articles/search", json.dumps({"search_for": q, "page_size": 25}).encode())
    return len(j), [(x.get("doi") or str(x["id"]), x["title"] + " [type " + str(x.get("defined_type_name")) + "]") for x in j]


def dryad(q):
    j = get("https://datadryad.org/api/v2/search?per_page=25&q=" + urllib.parse.quote(plain(q)))
    return j.get("total", 0), [(x["identifier"], x["title"]) for x in j.get("_embedded", {}).get("stash:datasets", [])]


def dandi(q):
    j = get("https://api.dandiarchive.org/api/dandisets/?page_size=25&draft=true&empty=false&search=" + urllib.parse.quote(plain(q)))
    return j["count"], [("DANDI:" + x["identifier"], (x.get("draft_version") or {}).get("name", "")) for x in j["results"]]


def gin(q):
    j = get("https://gin.g-node.org/api/v1/repos/search?limit=25&q=" + urllib.parse.quote(plain(q)))
    d = j.get("data", [])
    return len(d), [("gin:" + x["full_name"], x.get("description", "")) for x in d]


def osf(q):
    j = get("https://api.osf.io/v2/nodes/?page[size]=25&filter[title]=" + urllib.parse.quote(plain(q)))
    return j["links"]["meta"]["total"], [("osf:" + x["id"], x["attributes"]["title"]) for x in j["data"]]


REPOS = {"datacite": datacite, "zenodo": zenodo, "figshare": figshare, "dryad": dryad, "dandi": dandi, "gin": gin, "osf": osf}


def main():
    only = sys.argv[2:] 
    with (OUT / "queries.tsv").open("a") as qf, (OUT / "hits.tsv").open("a") as hf:
        for repo, fn in REPOS.items():
            if only and repo not in only:
                continue
            for key, q in Q.items():
                stamp = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
                try:
                    total, hits = fn(q)
                    qf.write(f"{stamp}\t{repo}\t{key}\t{q}\tok\t{total}\t{len(hits)}\n")
                    for ident, title in hits:
                        hf.write(f"{repo}\t{key}\t{ident}\t{' '.join(str(title).split())[:220]}\n")
                except urllib.error.HTTPError as e:
                    qf.write(f"{stamp}\t{repo}\t{key}\t{q}\tHTTP {e.code}\t-\t0\n")
                    if e.code in (401, 403, 429):
                        break
                except Exception as e:  # recorded, not retried
                    qf.write(f"{stamp}\t{repo}\t{key}\t{q}\terror {type(e).__name__}\t-\t0\n")
                time.sleep(1.0)


if __name__ == "__main__":
    main()
