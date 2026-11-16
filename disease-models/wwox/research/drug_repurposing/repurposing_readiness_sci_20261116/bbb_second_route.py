#!/usr/bin/env python3
"""Second route for the 'blood-brain barrier not stated at abstract level' absence claims of the readiness sheets.

    python3 bbb_second_route.py --help
    python3 bbb_second_route.py run <out_tsv>

For each agent, NCBI esearch ("<agent>"[Title/Abstract] AND "blood-brain barrier"[Title/Abstract], 8 most relevant) then efetch of those abstracts;
writes every sentence that contains 'blood-brain' or 'blood brain' with its PMID. Descriptive retrieval only (no contact parameter sent); a sentence is
a candidate for the sheet only after a person reads it. Not medical advice.
"""
import sys
if len(sys.argv) != 3 or sys.argv[1] != "run":
    print(__doc__); raise SystemExit(0)
import csv, re, time, urllib.parse, urllib.request
import xml.etree.ElementTree as ET
AG = ["esketamine", "zolpidem", "eszopiclone", "clobazam", "clonazepam", "ethosuximide", "zonisamide", "carbamazepine", "lamotrigine", "phenytoin"]
def get(u):
    time.sleep(0.5); return urllib.request.urlopen(u, timeout=60).read()
rows = []
for a in AG:
    q = urllib.parse.quote(f'"{a}"[Title/Abstract] AND "blood-brain barrier"[Title/Abstract]')
    ids = re.findall(r"<Id>(\d+)</Id>", get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term={q}&retmax=8&sort=relevance").decode())
    if not ids:
        rows.append((a, "", "no hit for the query", "")); continue
    root = ET.fromstring(get(f"https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id={','.join(ids)}&retmode=xml"))
    for art in root.findall(".//PubmedArticle"):
        pmid = art.findtext(".//PMID"); title = "".join(art.find(".//ArticleTitle").itertext())
        text = " ".join("".join(x.itertext()) for x in art.findall(".//AbstractText"))
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z])", text):
            if re.search(r"blood[- ]brain", s, re.I) and re.search(a, s, re.I):
                rows.append((a, pmid, s.strip(), title[:90]))
with open(sys.argv[2], "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["agent", "pmid", "sentence_naming_agent_and_barrier", "article_title"]); w.writerows(rows)
import collections; print(collections.Counter(r[0] for r in rows if r[1]))
print([a for a in AG if not any(r[0] == a and r[1] for r in rows)])
