#!/usr/bin/env python3
"""ADV-285 stage 1: fetch abstracts (efetch, public GET) for the union PMIDs and apply the frozen keyword filter.
Usage (python3 -I -P -E): screen_adv285.py <union_pmids.tsv> <outdir>. Writes abstracts_adv285.tsv (pmid, year, journal, title, abstract, flags) and stage1_adv285.tsv."""
import csv, sys, os, re, time, urllib.request, urllib.parse, xml.etree.ElementTree as ET
src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
ids = [r["pmid"] for r in csv.DictReader(open(src), delimiter="\t")]
strs = {r["pmid"]: r["strings_and_routes"] for r in csv.DictReader(open(src), delimiter="\t")}
FN = re.compile(r"conduction velocit|compound action potential|evoked potential|visual evoked|auditory brainstem|nerve conduction|\bVEPs?\b|\bABR\b|\bCAPs?\b|\bCNAP|latenc|propagation|action potential", re.I)
TX = re.compile(r"treat|administ|inject|rescue|\bdrug|compound|\bdiet|mg/kg|gavage|clemastine|miconazole|benztropine|clobetasol|quetiapine|guanabenz|sephin|ISRIB|ibudilast|thyroid hormone|lactate|ketogenic", re.I)
rows = []
for i in range(0, len(ids), 150):
    chunk = ids[i:i + 150]
    data = urllib.parse.urlencode({"db": "pubmed", "retmode": "xml", "id": ",".join(chunk)}).encode()
    r = urllib.request.Request("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi", data=data, headers={"User-Agent": "legend-census/1.0"})
    with urllib.request.urlopen(r, timeout=120) as h:
        root = ET.fromstring(h.read())
    for a in root.iter("PubmedArticle"):
        pmid = a.findtext(".//PMID")
        t = "".join(a.find(".//ArticleTitle").itertext()) if a.find(".//ArticleTitle") is not None else ""
        ab = " ".join("".join(x.itertext()) for x in a.findall(".//AbstractText"))
        y = a.findtext(".//JournalIssue/PubDate/Year") or (a.findtext(".//JournalIssue/PubDate/MedlineDate") or "")[:4]
        jn = a.findtext(".//Journal/ISOAbbreviation") or ""
        rows.append([pmid, y, jn, " ".join(t.split()), " ".join(ab.split())])
    time.sleep(0.5)
got = {r[0] for r in rows}
with open(f"{out}/abstracts_adv285.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["pmid", "year", "journal", "title", "abstract", "strings_and_routes"])
    for r in rows: w.writerow(r + [strs.get(r[0], "")])
n_keep = 0
with open(f"{out}/stage1_adv285.tsv", "w", newline="") as h:
    w = csv.writer(h, delimiter="\t"); w.writerow(["pmid", "year", "title", "functional_term", "treatment_term", "has_abstract", "stage1", "strings_and_routes"])
    for r in rows:
        txt = r[3] + " " + r[4]
        f = bool(FN.search(txt)); t = bool(TX.search(txt))
        s = strs.get(r[0], "")
        wwox = s.startswith(("S1", "S2", "S3")) or any(x[:2] in ("S1", "S2", "S3") for x in s.split(";"))
        keep = (f and t) or wwox
        n_keep += keep
        w.writerow([r[0], r[1], r[3][:160], f, t, bool(r[4]), "KEEP" if keep else "DROP", s])
print("ids", len(ids), "fetched", len(got), "missing", len(set(ids) - got), "stage1 KEEP", n_keep)
