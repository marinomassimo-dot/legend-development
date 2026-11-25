"""ADV-261: list, by two routes, the sentences of the scoped claim records that give a numeric n or a counted number of
units, the PMIDs and PAPER records each claim cites, and a consumer count per claim.

Usage: python3 list_claim_n_adv261.py <repo root> <out folder>
"""
import sys

if len(sys.argv) != 3 or sys.argv[1] in ("-h", "--help"):
    print(__doc__)
    raise SystemExit(0)

import csv, glob, os, re

repo, out = sys.argv[1:3]
W = os.path.join(repo, "disease-models/wwox")
reg = open(os.path.join(W, "registries/claim_registry_current.md")).read()
SCOPE = "002 003 005 007 011 014 021 025 031 032 033 034 038 042 047".split()
FIRST = "002 005 007 014".split()
UNIT = (r"(?:mice|animals|patients|rats|libraries|organoids|clones|lines|samples|flies|families|subjects|embryos|individuals|"
        r"children|cases|pazienti|topi|ratti|famiglie|casi|linee|cloni|soggetti|slices|cells|fette|cellule)")
NUM = r"(?:\d+|one|two|three|four|five|six|seven|eight|nine|due|tre|quattro|cinque|sei)"
R1 = re.compile(r"(?<![A-Za-z])[nN] ?(?:=|of|≥|>=) ?\d+|\b%s (?:[\w-]+ )?%s\b" % (NUM, UNIT), re.I)
R2 = re.compile(r"(?<![A-Za-z])[nN] ?[=≥] ?\d|\bper (?:group|arm|condition|genotype)\b|\breplicat|\beach genotype\b|"
                r"\b%s [\w-]*\s?(?:clon|line|librar|slice|famil|linee|clone|replica)" % NUM, re.I)
claims = {m.group(1): u for u in re.split(r"(?m)^(?=## )", reg) for m in [re.match(r"## CLAIM (\d{3})", u)] if m}

surfaces = ([("card", f) for f in glob.glob(os.path.join(W, "research/drug_repurposing/cards*/*.card.json"))] +
            [("portfolio", os.path.join(W, "research/drug_repurposing/research_portfolio.tsv")),
             ("working_model", os.path.join(W, "registries/working_model_current.md")),
             ("model", os.path.join(W, "disease_model.md")),
             ("lead", os.path.join(W, "research/discovery_ledger_current.md")),
             ("hypothesis", os.path.join(W, "research/therapeutic_hypotheses_ledger_current.md"))] +
            [("analysis", f) for f in glob.glob(os.path.join(W, "analysis/*.md"))])
texts = [(k, f, open(f, errors="replace").read()) for k, f in surfaces]

rows, meta = [], []
for c in SCOPE:
    u = claims[c]
    consumers = [(k, os.path.basename(f)) for k, f, t in texts if re.search(r"CLAIM[ _#]*%s(?!\d)" % c, t)]
    pmids = sorted(set(re.findall(r"PMID\W{0,4}(\d{7,8})", u)))
    papers = sorted(set(re.findall(r"PAPER[ _#]*(\d{3})", u)))
    sentences = [s.strip() for line in u.split("\n") for s in re.split(r"(?<=[.;»])\s+(?=[\w\"«*`(🔴🔵⚠️])", line) if s.strip()]
    k = 0
    for s in sentences:
        a, b = R1.findall(s), R2.search(s)
        if a or b:
            k += 1
            rows.append(("%s-%02d" % (c, k), c, "both" if a and b else "route1" if a else "route2",
                         "; ".join(dict.fromkeys(x if isinstance(x, str) else " ".join(x) for x in a))[:120], s[:900]))
    meta.append((c, len(consumers), "yes" if any(x[0] == "working_model" for x in consumers) else "no", k,
                 ",".join(pmids), ",".join(papers), u.split("\n")[0].lstrip("# ")[:200]))
meta.sort(key=lambda r: (r[0] not in FIRST, -r[1] if r[0] not in FIRST else 0, r[0]))
os.makedirs(out, exist_ok=True)
for name, head, data in (("claim_n_sentences.tsv", "row claim route pattern_hits sentence", rows),
                         ("claim_order.tsv", "claim consumer_files in_working_model n_sentences pmids paper_records title", meta)):
    with open(os.path.join(out, name), "w") as o:
        w = csv.writer(o, delimiter="\t", lineterminator="\n")
        w.writerow(head.split())
        w.writerows([[x if str(x) != "" else "-" for x in r] for r in data])
for r in meta:
    print(r[0], "consumers", r[1], "wm", r[2], "sentences", r[3], "| pmids", r[4][:90], "| papers", r[5][:60])
print("total sentences", len(rows))
