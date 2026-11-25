"""ADV-254: for every discovery-ledger lead with no PubMed identifier, count consumers by two routes and list the
identifiers the lead does name. Rules: PREREG_ADV254_SCI_20261125.md.

Usage: python3 scan_unsourced_leads_adv254.py <repo root> <out.tsv>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import collections, csv, glob, os, re, subprocess

repo, out = sys.argv[1:3]
W = os.path.join(repo, "disease-models/wwox")
rd = lambda p: open(os.path.join(W, p), errors="replace").read()
DL = re.compile(r"\bDL-[A-Z]+-\d+\b")
PMID_ANY = re.compile(r"PMID\W{0,6}\d{7,8}|pubmed\.ncbi\.nlm\.nih\.gov/\d{7,8}", re.I)

leads = collections.OrderedDict()
for part in re.split(r"(?m)^(?=#{2,4} )", rd("research/discovery_ledger_current.md")):
    m = DL.search(part.split("\n")[0])
    if part.startswith("##") and m:
        leads.setdefault(m.group(0), []).append(part)
nopm = [l for l, ps in leads.items() if not PMID_ANY.search("\n".join(ps))]

# route 2: one unit per record, row or file
SURFACES = [
    ("card", "research/drug_repurposing/cards*/*.json", "file"),
    ("claim", "registries/claim_registry_current.md", "md"),
    ("model", "registries/working_model_current.md", "md"),
    ("model", "disease_model.md", "md"),
    ("portfolio", "research/drug_repurposing/research_portfolio.tsv", "tsv"),
    ("ranking", "research/drug_repurposing/ranking*/investigations*.tsv", "tsv"),
    ("ranking", "research/drug_repurposing/ranking*/triggers*.tsv", "tsv"),
    ("hypothesis", "research/therapeutic_hypotheses_ledger_current.md", "md"),
    ("map", "analysis/mechanism_intervention_map.md", "md"),
    ("analysis", "analysis/*.md", "md"),
    ("meta", "meta/*.md", "md"),
]
c2 = collections.defaultdict(set)
for kind, pat, how in SURFACES:
    for f in sorted(glob.glob(os.path.join(W, pat))):
        t = open(f, errors="replace").read()
        rel = os.path.relpath(f, W)
        if kind == "analysis" and rel.endswith("mechanism_intervention_map.md"):
            continue
        if how == "file":
            units = [(os.path.basename(f).split("_")[0], t)]
        elif how == "tsv":
            units = [(line.split("\t")[0], line) for line in t.split("\n")[1:] if line]
        else:
            units = [(p.split("\n")[0].lstrip("# ")[:50] or "preamble", p) for p in re.split(r"(?m)^(?=#{2,4} )", t)]
        for name, body in units:
            for d in DL.findall(body):
                c2[d].add("%s:%s:%s" % (kind, rel.split("/")[-1], name))

# route 1: line search per lead id
EXCL = re.compile(r"discovery_ledger|corpus_seed|receipts|reading_state|batch_queue|coverage_report|locator_audits|"
                  r"session_evaluations|assignments|checkpoint|wm_history|working_model_history|/join/|ranking\.json|"
                  r"advisor_pilot|commit_candidates|debts_wave|gold_wave|held_wave|deepdive_manifests|learning/")
grep = subprocess.run(["git", "-C", repo, "grep", "-n", "-I", "-o", "-E", r"\bDL-[A-Z]+-[0-9]+\b", "--", "disease-models/wwox"],
                      capture_output=True, text=True, check=True).stdout
c1 = collections.defaultdict(set)
for line in grep.split("\n"):
    if line:
        path, _, lead = line.split(":", 2)
        if not EXCL.search(path):
            c1[lead].add(path.replace("disease-models/wwox/", ""))

# files that route 1 may find outside the route-2 surfaces are listed in the output, not silently counted
IDS = {"paper": re.compile(r"PAPER[ _#]*(\d{1,4})\b"), "claim": re.compile(r"CLAIM[ _]*(\d{1,4})\b"),
       "doi": re.compile(r"\b10\.\d{4,9}/[^\s\])>,;*]+"), "accession": re.compile(r"\b(?:PMC\d{6,}|GSE\d{3,}|NCT\d{8}|PXD\d{4,}|E-MTAB-\d+)\b"),
       "author_year": re.compile(r"\b([A-ZÅŁ][\w’'-]{2,}(?:[- ][A-ZÅŁ][\w’'-]+)?)(?: et al\.?)?,? \(?((?:19|20)\d\d)\b")}
rows = []
for lead in nopm:
    body = "\n".join(leads[lead])
    found = {k: sorted(set(m if isinstance(m, str) else " ".join(m) for m in rx.findall(body))) for k, rx in IDS.items()}
    cons = c2[lead]
    extra = sorted(p for p in c1[lead] if not any(p.split("/")[-1] == c.split(":")[1] or (c.startswith("card:") and p.endswith(".json")) for c in cons))
    rows.append((lead, len(cons), len(c1[lead]), "; ".join(sorted(cons)), "; ".join(extra), ",".join(found["paper"]),
                 ",".join(found["claim"]), ",".join(found["doi"]), ",".join(found["accession"]), "; ".join(found["author_year"]),
                 leads[lead][0].split("\n")[0].lstrip("# ")[:160]))
rows.sort(key=lambda r: (-r[1], -r[2], r[0]))
with open(out, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("lead n_units_route2 n_files_route1 consumers_route2 route1_only_files papers claims dois accessions author_year heading".split())
    for r in rows:
        w.writerow([c if str(c) != "" else "-" for c in r])
cls = collections.Counter()
for r in rows:
    cls["registry id" if (r[5] or r[6]) else "doi or accession" if (r[7] or r[8]) else "author-year only" if r[9] else "nothing"] += 1
print("leads", len(leads), "| no PMID", len(nopm), "| with consumer route2", sum(r[1] > 0 for r in rows),
      "| route1", sum(r[2] > 0 for r in rows), "| classes", dict(cls))
