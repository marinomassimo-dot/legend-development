"""ADV-256: build the catalogued PMID list by two routes, ask Europe PMC for notices, compare with the held Retraction
Watch snapshot and with the repository's own flags. Rules: PREREG_ADV256_SCI_20261125.md.

Usage: python3 sweep_catalogue_adv256.py <repo root> <retraction watch csv> <out folder>
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, json, os, re, time

repo, rw_path, out = sys.argv[1:4]
sys.path.insert(0, os.path.join(repo, "framework/scripts"))
import epmc_notice_sweep as sweep_tool  # get() stops on any challenge, 429 or non-JSON reply

W = os.path.join(repo, "disease-models/wwox/registries")
rd = lambda p: open(os.path.join(W, p), errors="replace").read()
PM = re.compile(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,8})")
id_lines = lambda t: {p for line in t.split("\n") if "Identifier" in line for p in PM.findall(line)}

seed = list(csv.DictReader(open(os.path.join(W, "corpus_seed_pubmed_20260806.tsv")), delimiter="\t"))
a_seed = {r["pmid"] for r in seed if r["pmid"]}
a_reg = id_lines(rd("paper_registry_current.md"))
b_queue = set(re.findall(r"(?m)^\| \[(\d{6,8})\]\(", rd("batch_queue.md")))
b_log = id_lines(rd("literature_tracking_log_current.md"))
route_a, route_b = a_seed | a_reg, b_queue | b_log
pmids = sorted(route_a | route_b, key=int)
counts = {"seed": len(a_seed), "paper_registry": len(a_reg), "route_a": len(route_a), "batch_queue": len(b_queue),
          "tracking_log": len(b_log), "route_b": len(route_b), "union": len(pmids),
          "only_route_a": len(route_a - route_b), "only_route_b": len(route_b - route_a)}
print(counts)

core = {}
for i in range(0, len(pmids), 40):
    for rec in sweep_tool.get("SRC:MED AND EXT_ID:(" + " OR ".join(pmids[i:i + 40]) + ")"):
        core[rec["id"]] = rec
    time.sleep(2.0)
not_indexed = [p for p in pmids if p not in core]


def kind(link_type):
    t = link_type.lower()
    if t in ("retraction in", "partial retraction in"):
        return "retraction"
    if t == "expression of concern in":
        return "concern"
    if t in ("erratum in", "corrected and republished in", "retracted and republished in") or ("correct" in t and t.endswith(" in")):
        return "correction"
    return ""


hits = []
for p, rec in core.items():
    types = (rec.get("pubTypeList") or {}).get("pubType", [])
    found = False
    for c in (rec.get("commentCorrectionList") or {}).get("commentCorrection", []):
        k = kind(c.get("type", ""))
        if k:
            hits.append([p, k, c["type"], c.get("id", ""), c.get("reference", "")])
            found = found or k == "retraction"
    if "Retracted Publication" in types and not found:
        hits.append([p, "retraction", "pubType Retracted Publication", "", ""])
notice_self = sorted(p for p, r in core.items()
                     if set((r.get("pubTypeList") or {}).get("pubType", [])) & {"Retraction of Publication", "Published Erratum", "Expression of Concern"})
types_seen = sorted({c.get("type", "") for r in core.values() for c in (r.get("commentCorrectionList") or {}).get("commentCorrection", [])})

nids = sorted({h[3] for h in hits if h[3]})
notices = {}
for i in range(0, len(nids), 40):
    for rec in sweep_tool.get("SRC:MED AND EXT_ID:(" + " OR ".join(nids[i:i + 40]) + ")"):
        notices[rec["id"]] = rec
    time.sleep(2.0)

rw_pmid, rw_doi = {}, {}
with open(rw_path, errors="replace", newline="") as f:
    for r in csv.DictReader(f):
        nature = (r.get("RetractionNature") or "").strip()
        p = (r.get("OriginalPaperPubMedID") or "").strip()
        d = (r.get("OriginalPaperDOI") or "").strip().lower()
        if p and p != "0":
            rw_pmid.setdefault(p, set()).add(nature)
        if d:
            rw_doi.setdefault(d, set()).add(nature)

queue_lines = rd("batch_queue.md").split("\n")
registry_units = [u for fn in ("paper_registry_current.md", "literature_tracking_log_current.md")
                  for u in re.split(r"(?m)^(?=## )", rd(fn))]
FLAG = {"retraction": re.compile(r"retract|ritrat|ritirat", re.I), "concern": re.compile(r"concern", re.I),
        "correction": re.compile(r"erratum|corrig|correct|corrett|correzione", re.I)}


def repo_note(pmid, k):
    notes = []
    if any(pmid in line and FLAG[k].search(line) for line in queue_lines):
        notes.append("batch_queue")
    if any(re.search(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)%s\b" % pmid, u) and FLAG[k].search(u) for u in registry_units):
        notes.append("registry_or_log")
    return ",".join(notes) or "none"


rows = []
for p, k, link, nid, ref in hits:
    rec, note = core[p], notices.get(nid, {})
    doi = (rec.get("doi") or "").lower()
    listed = sorted((rw_pmid.get(p, set()) | rw_doi.get(doi, set())) - {""})
    rows.append([p, k, link, nid or "-", note.get("firstPublicationDate") or sweep_tool.reference_date(ref) or "-",
                 note.get("doi") or "-", "|".join(listed) or "not listed", repo_note(p, k),
                 "wwox_title" if re.search(r"wwox|WW domain.containing oxidoreductase|WOX1", rec.get("title", ""), re.I) else "-",
                 "route_a" if p in route_a else "route_b_only", (rec.get("title") or "")[:110]])
order = {"retraction": 0, "concern": 1, "correction": 2}
rows.sort(key=lambda r: (r[0] != "19357348", order[r[1]], r[7] != "none", r[0]))
rw_only = sorted(p for p in pmids if any("Retraction" == n for n in rw_pmid.get(p, set()) | rw_doi.get((core.get(p, {}).get("doi") or "x").lower(), set()))
                 and not any(h[0] == p and h[1] == "retraction" for h in hits))
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "notice_hits.tsv"), "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("pmid kind link_type notice_pmid notice_date notice_doi snapshot_nature repository_note title_flag source_route title".split())
    w.writerows(rows)
with open(os.path.join(out, "pmid_list.tsv"), "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("pmid route_a route_b indexed".split())
    for p in pmids:
        w.writerow([p, int(p in route_a), int(p in route_b), int(p in core)])
summary = {"counts": counts, "indexed": len(core), "not_indexed": not_indexed, "link_types_seen": types_seen,
           "records_that_are_notices": notice_self, "snapshot_retraction_not_marked_by_europepmc": rw_only,
           "hits_by_kind": {k: len({r[0] for r in rows if r[1] == k}) for k in order},
           "unflagged_by_kind": {k: sorted({r[0] for r in rows if r[1] == k and r[7] == "none"}) for k in order}}
json.dump(summary, open(os.path.join(out, "summary.json"), "w"), indent=1)
print(json.dumps(summary, indent=1))
