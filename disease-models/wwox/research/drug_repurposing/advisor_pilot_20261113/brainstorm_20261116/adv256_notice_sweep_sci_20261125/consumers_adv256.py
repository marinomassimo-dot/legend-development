"""ADV-256: for each hit PMID, find the claims, cards, ledger leads, hypotheses, model, portfolio, ranking and analysis
units that name it by PMID, DOI or its registry ids (PAPER, CORPUS, LIT). Route 1 is a git grep over lines; route 2 a
record-aware split. Retractions and concerns use every surface; corrections only claims, cards, leads, hypotheses and
the model.

Usage: python3 consumers_adv256.py <repo root> <notice_hits.tsv> <out.tsv>
"""
import sys

if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, glob, os, re, subprocess

repo, hits_path, out = sys.argv[1:4]
W = os.path.join(repo, "disease-models/wwox")
rd = lambda p: open(os.path.join(W, p), errors="replace").read()
hits = list(csv.DictReader(open(hits_path), delimiter="\t"))
seed = {r["pmid"]: r for r in csv.DictReader(open(os.path.join(W, "registries/corpus_seed_pubmed_20260806.tsv")), delimiter="\t")}

ids = collections.defaultdict(set)
for fn in ("registries/paper_registry_current.md", "registries/literature_tracking_log_current.md"):
    for unit in re.split(r"(?m)^(?=## )", rd(fn)):
        head = re.match(r"## ((?:PAPER \d+|CORPUS(?:-STUB-\d+| P\d+)|LIT-\d+))", unit)
        if not head:
            continue
        own = set()
        for line in unit.split("\n"):
            if "Identifier" in line:
                own |= set(re.findall(r"(?:PMID\W{0,4}|pubmed\.ncbi\.nlm\.nih\.gov/)(\d{6,8})", line))
        for p in own:
            ids[p].add(head.group(1))


def pattern(pmid, doi):
    alts = [r"(?<![\d.])%s(?!\d)" % pmid]
    if doi:
        alts.append(re.escape(doi))
    for i in ids[pmid]:
        alts.append(re.escape(i).replace(r"\ ", r"[ _#]?") + r"(?!\d)")
    return re.compile("|".join(alts), re.I)


SURF = [("claim", "registries/claim_registry_current.md"), ("model", "registries/working_model_current.md"),
        ("model", "disease_model.md"), ("lead", "research/discovery_ledger_current.md"),
        ("hypothesis", "research/therapeutic_hypotheses_ledger_current.md"),
        ("card", "research/drug_repurposing/cards*/*.json"),
        ("portfolio", "research/drug_repurposing/research_portfolio.tsv"),
        ("ranking", "research/drug_repurposing/ranking*/investigations*.tsv"),
        ("analysis", "analysis/*.md"), ("meta", "meta/*.md")]
CORE = {"claim", "model", "lead", "hypothesis", "card"}
units = []
for kind, pat in SURF:
    for f in sorted(glob.glob(os.path.join(W, pat))):
        t = open(f, errors="replace").read()
        rel = os.path.relpath(f, W)
        if f.endswith(".json"):
            units.append((kind, rel, os.path.basename(f).split("_")[0], t))
        elif f.endswith(".tsv"):
            units += [(kind, rel, line.split("\t")[0], line) for line in t.split("\n")[1:] if line]
        else:
            units += [(kind, rel, p.split("\n")[0].lstrip("# ")[:60] or "preamble", p) for p in re.split(r"(?m)^(?=#{2,4} )", t)]

rows = []
for h in hits:
    p, k = h["pmid"], h["kind"]
    doi = seed.get(p, {}).get("doi", "")
    rx = pattern(p, doi)
    want = CORE if k == "correction" else {s for s, _ in SURF}
    r2 = sorted({"%s:%s:%s" % (kind, rel.split("/")[-1], name) for kind, rel, name, body in units if kind in want and rx.search(body)})
    terms = [p] + ([doi] if doi else []) + sorted(ids[p])
    cmd = ["git", "-C", repo, "grep", "-n", "-I", "-i", "-w", "-F"] + sum([["-e", t] for t in terms], []) + ["--"] + \
          sorted({"disease-models/wwox/" + pat for kind, pat in SURF if kind in want})
    res = subprocess.run(cmd, capture_output=True, text=True)
    r1 = sorted({l.split(":", 1)[0].split("/")[-1] for l in res.stdout.split("\n") if l})
    rows.append((p, k, h["repository_note"], ",".join(sorted(ids[p])) or "-", len(r2), "; ".join(r2) or "-", "; ".join(r1) or "-"))
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("pmid kind repository_note registry_ids n_units_route2 units_route2 files_route1".split())
    w.writerows(rows)
for r in rows:
    print(r[0], r[1], r[2], r[3], "| n2=%d" % r[4], "|", r[5][:300], "| r1:", r[6][:150])
