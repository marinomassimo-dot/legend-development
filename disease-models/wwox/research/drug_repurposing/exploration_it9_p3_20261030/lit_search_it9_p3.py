#!/usr/bin/env python3
"""IT9 P3: dated PubMed and Europe PMC count searches for selected compounds (compound x WWOX, compound x epilepsy/DEE, compound x question phenotype terms).
Only compound names and phenotype words are sent (no operator identity, no e-mail address, no API key). Usage: lit_search_it9_p3.py --selected selected.tsv --out search_log.tsv --hits wwox_hits.tsv"""
import argparse, csv, datetime, json, sys, time, urllib.parse, urllib.request
ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("--selected", required=True); ap.add_argument("--out", required=True); ap.add_argument("--hits", required=True); a = ap.parse_args()
TODAY = datetime.date.today().isoformat()
PHEN = {"Q2": '(glycolysis OR lactate OR "pyruvate dehydrogenase")', "Q4": '(interneuron OR "excitation inhibition" OR GABAergic)', "Q5": '(myelin* OR oligodendrocyte* OR microglia* OR astrocyte*)', "Q6": '("radial glia" OR "neural progenitor" OR MYC)', "Q3": '("integrated stress response" OR "unfolded protein response" OR ATF4)'}
EPI = '(epilep* OR seizure* OR "developmental and epileptic encephalopathy")'
def get(url):
    for t in range(4):
        try:
            with urllib.request.urlopen(url, timeout=40) as r: return json.load(r)
        except Exception as e: time.sleep(1.5 * (t + 1)); err = str(e)
    return {"_error": err}
def pm(term, ret=0):
    d = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=%d&term=%s" % (ret, urllib.parse.quote(term))); time.sleep(0.4)
    if "_error" in d or "esearchresult" not in d or "count" not in d["esearchresult"]: return None, [], d.get("_error", "no count")
    return int(d["esearchresult"]["count"]), d["esearchresult"].get("idlist", []), ""
def epmc(term):
    d = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&pageSize=1&resultType=lite&query=" + urllib.parse.quote(term)); time.sleep(0.3)
    if "_error" in d or "hitCount" not in d: return None, d.get("_error", "no hitCount")
    return int(d["hitCount"]), ""
sel = list(csv.DictReader(open(a.selected), delimiter="\t"))
log = []; hits = []
def run(parent, name, qid, label, pq, eq, ph, want_ids=False):
    n, ids, err = pm(pq, 15 if want_ids else 0); e, err2 = epmc(eq)
    log.append([parent, name, qid, label, "PubMed [Title/Abstract]", pq, TODAY, "ERROR:" + err if n is None else n, "Europe PMC title+abstract (all sources, incl. preprints)", eq, "ERROR:" + err2 if e is None else e])
    return n, ids
run("CONTROL", "WWOX", "-", "positive control (the search tools return counts)", "WWOX[Title/Abstract]", 'TITLE:"WWOX" OR ABSTRACT:"WWOX"', "")
for s in sel:
    nm = s["name"].strip()
    alt = [x.strip() for x in (s.get("chembl_name") or "").split("|") if x.strip() and x.strip().upper() != nm.upper()]
    def p(n): return '"%s"[Title/Abstract]' % n
    def e(n): return '(TITLE:"%s" OR ABSTRACT:"%s")' % (n, n)
    pn = "(" + " OR ".join(p(x) for x in [nm] + alt) + ")"; en = "(" + " OR ".join(e(x) for x in [nm] + alt) + ")"
    q = s["question_for_phenotype"]
    n, ids = run(s["parent"], nm, q, "A compound x WWOX/WOREE", pn + " AND (WWOX[Title/Abstract] OR WOREE[Title/Abstract])", en + " AND (TITLE:WWOX OR ABSTRACT:WWOX OR TITLE:WOREE OR ABSTRACT:WOREE)", "", True)
    for i in ids: hits.append([s["parent"], nm, i])
    run(s["parent"], nm, q, "B compound x epilepsy/DEE", pn + " AND " + EPI.replace("(", "(").replace('epilep*', 'epilep*') .replace("seizure*", "seizure*"), en + " AND (" + 'epilep* OR seizure* OR "developmental and epileptic encephalopathy"' + ")", "")
    ph = PHEN.get(q, "")
    if ph: run(s["parent"], nm, q, "C compound x %s phenotype terms" % q, pn + " AND " + ph.replace("*", "*"), en + " AND " + ph, ph)
with open(a.out, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["parent", "name_searched", "question", "search", "pubmed_perimeter", "pubmed_query", "date", "pubmed_hits", "europepmc_perimeter", "europepmc_query", "europepmc_hits"]); w.writerows(log)
# titles of WWOX-query PubMed hits
ids = sorted({h[2] for h in hits})
titles = {}
for i in range(0, len(ids), 40):
    d = get("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id=" + ",".join(ids[i:i + 40])); time.sleep(0.4)
    for k, v in d.get("result", {}).items():
        if k != "uids": titles[k] = (v.get("title", ""), v.get("pubdate", ""), v.get("source", ""))
with open(a.hits, "w", newline="") as fh:
    w = csv.writer(fh, delimiter="\t", lineterminator="\n"); w.writerow(["parent", "name_searched", "pmid", "year_source", "title", "opened_at_title_abstract_level", "concerns_compound_in_WWOX_context"])
    for h in hits: t = titles.get(h[2], ("", "", "")); w.writerow(h + [t[1] + " " + t[2], t[0].replace("\t", " "), "NOT_YET", "NOT_YET"])
print(len(log), "searches;", len(hits), "WWOX-query hits listed", file=sys.stderr)
