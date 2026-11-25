"""ADV-249: list discovery-ledger leads, their primary PMIDs, whether each was ever read (receipt ledger), what is
held under files/, and how many consumers cite the lead. Query and ranking: PREREG_ADV249_SCI_20261125.md.

Usage: python3 list_leads_adv249.py <repo root> <held-files root> <out.tsv>
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, glob, json, os, re

repo, held_root, out = sys.argv[1:4]
W = os.path.join(repo, "disease-models/wwox")
rd = lambda p: open(os.path.join(W, p), errors="replace").read()
DL = re.compile(r"\bDL-[A-Z]+-\d+\b")
PM = re.compile(r"(?:PMID[:\s]*|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{7,8})")

leads = collections.OrderedDict()
for part in re.split(r"(?m)^(?=#{2,4} )", rd("research/discovery_ledger_current.md")):
    head = part.split("\n")[0]
    m = DL.search(head)
    if head.startswith("##") and m:
        leads.setdefault(m.group(0), []).append(part)

def primaries(body):
    lines = body.split("\n")
    src = [x for x in lines if re.search(r"\*\*(Fonte|Source)\b|^\s*[-*]*\s*(Fonte|Source)\s*:", x, re.I)]
    ids, how = [p for x in src for p in PM.findall(x)], "source line"
    if not ids:
        ids, how = PM.findall(lines[0]), "heading"
    if not ids:
        ids, how = PM.findall(body)[:1], "first mentioned"
    return list(dict.fromkeys(ids)), how

BODY = ("introduction", "methods", "results", "discussion", "figures")
recs = [json.loads(l) for l in open(os.path.join(W, "registries/fulltext_read_receipts.jsonl"))]
dead = {r.get("invalidates_receipt") for r in recs} - {None}
read, anyrec = collections.defaultdict(set), collections.Counter()
for r in recs:
    p = str((r.get("study_id") or {}).get("pmid") or "")
    if not p or r.get("event_id") in dead or r.get("invalidates_receipt"):
        continue
    anyrec[p] += 1
    read[p] |= {k for k in BODY if (r.get("coverage") or {}).get(k) == "read"}

held = collections.defaultdict(list)
for dp, dn, fn in os.walk(held_root):
    for f in fn:
        for p in re.findall(r"PMID_?(\d{7,8})", f):
            if f.lower().endswith((".xml", ".pdf", ".txt", ".html")):
                held[p].append(os.path.relpath(os.path.join(dp, f), held_root))

consumers = collections.defaultdict(set)
pm_consumers = collections.defaultdict(set)
def feed(key, text):
    for d in DL.findall(text):
        consumers[d].add(key)
    for p in PM.findall(text):
        pm_consumers[p].add(key)

for f in glob.glob(os.path.join(W, "research/drug_repurposing/cards/*.card.json")):
    feed("card " + os.path.basename(f).split("_")[0], open(f).read())
for rel, tag in (("research/drug_repurposing/research_portfolio.tsv", "portfolio"),
                 ("research/drug_repurposing/ranking_it8_p9_20261029/investigations.tsv", "investigation"),
                 ("research/drug_repurposing/ranking_it8_p9_20261029/triggers.tsv", "trigger")):
    for line in rd(rel).split("\n")[1:]:
        if line:
            feed(tag + " " + line.split("\t")[0], line)
for rel, tag in (("registries/claim_registry_current.md", "claim"), ("registries/working_model_current.md", "model")):
    for part in re.split(r"(?m)^(?=#{2,4} )", rd(rel)):
        feed(tag + " " + part.split("\n")[0].lstrip("# ")[:40], part)
hyp = collections.defaultdict(set)
for part in re.split(r"(?m)^(?=#{2,4} )", rd("research/therapeutic_hypotheses_ledger_current.md")):
    for d in DL.findall(part):
        hyp[d].add(part.split("\n")[0][:30])

rows = []
for lead, parts in leads.items():
    body = "\n".join(parts)
    ids, how = primaries(body)
    for p in ids:
        if not read[p]:
            rows.append((len(consumers[lead]), len(pm_consumers[p]), len(hyp[lead]), int(lead.split("-")[-1]), lead, p, how))
rows.sort(key=lambda r: (-r[0], -r[1], -r[2], r[3], r[4]))
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("lead pmid primary_from n_consumers n_pmid_consumers n_hypothesis_records receipts held_files consumers heading".split())
    for n, npm, nh, _, lead, p, how in rows:
        w.writerow([lead, p, how, n, npm, nh, anyrec[p], ";".join(held[p][:3]), "; ".join(sorted(consumers[lead]))[:300],
                    leads[lead][0].split("\n")[0].lstrip("# ")[:200]])
allp = {p for l, ps in leads.items() for p in primaries("\n".join(ps))[0]}
print("leads", len(leads), "| leads with a primary PMID", sum(bool(primaries("\n".join(v))[0]) for v in leads.values()),
      "| primary PMIDs", len(allp), "| never read", len({r[5] for r in rows}), "| never-read lead-primary pairs", len(rows),
      "| pairs with >=1 consumer", sum(r[0] > 0 for r in rows))
