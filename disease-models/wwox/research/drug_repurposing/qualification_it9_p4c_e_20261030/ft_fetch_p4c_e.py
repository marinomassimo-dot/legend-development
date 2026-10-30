#!/usr/bin/env python3
"""IT9 P4c-e: Europe PMC full-text fetch for papers behind decisive edges. For each PMID: core record (PMCID, open-access flags); if a PMCID exists and the
full text is served, fetch fullTextXML, render to plain text (section headings kept), save under <artifact-root>/files/fulltext/ and append to ft_fetch_log.tsv
(pmid, pmcid, state, words, sha256 of the saved file). States: FULLTEXT_SAVED / NO_PMCID_ABSTRACT_ONLY / FULLTEXT_NOT_SERVED / SERVICE_ERROR.
  ft_fetch_p4c_e.py --help | fetch PMID [PMID ...] [--root DIR]
Nothing is sent but identifiers; no key, no e-mail."""
import argparse, hashlib, json, re, sys, time, urllib.parse, urllib.request
from pathlib import Path
HERE = Path(__file__).resolve().parent
def get(url, binary=False):
    last = None
    for wait in (0, 2, 6, 15):
        if wait: time.sleep(wait)
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": "legend-research/1.0"}), timeout=60) as r:
                b = r.read(); return 200, (b if binary else b.decode("utf-8", "replace"))
        except urllib.error.HTTPError as e:
            last = e.code
            if e.code == 404: return 404, ""
        except Exception as e:
            last = str(e)[:80]
    return last, ""
def render(xml):
    xml = re.sub(r"<(xref|ext-link)[^>]*>(.*?)</\1>", r"\2", xml, flags=re.S)
    xml = re.sub(r"<title>(.*?)</title>", lambda m: "\n\n## " + m.group(1) + "\n", xml, flags=re.S)
    xml = re.sub(r"</(p|sec|caption|abstract|table-wrap|fig)>", "\n", xml)
    t = re.sub(r"<[^>]+>", "", xml)
    import html
    return re.sub(r"\n{3,}", "\n\n", html.unescape(t))
def main():
    ap = argparse.ArgumentParser(description=__doc__); ap.add_argument("cmd", nargs="?", choices=["fetch"]); ap.add_argument("pmids", nargs="*"); ap.add_argument("--root", default=str(HERE.parents[4]))
    a = ap.parse_args()
    if not a.cmd: ap.print_help(); return
    out = Path(a.root) / "files" / "fulltext"; out.mkdir(parents=True, exist_ok=True)
    log = HERE / "ft_fetch_log.tsv"
    if not log.exists(): log.write_text("date\tpmid\tpmcid\tstate\twords\tsha256\tfile\tcore_title\n")
    for pm in a.pmids:
        st, b = get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?" + urllib.parse.urlencode({"query": f"EXT_ID:{pm} AND SRC:MED", "format": "json", "resultType": "core"}))
        try: r = json.loads(b)["resultList"]["result"][0]
        except Exception: r = None
        row = [time.strftime("%Y-%m-%d", time.gmtime()), pm, "", "", "", "", "", ""]
        if not r: row[3] = "SERVICE_ERROR" if st != 200 else "NO_RECORD"
        else:
            row[7] = (r.get("title") or "")[:90]; pmc = r.get("pmcid") or ""; row[2] = pmc
            if not pmc: row[3] = "NO_PMCID_ABSTRACT_ONLY"
            else:
                st2, x = get(f"https://www.ebi.ac.uk/europepmc/webservices/rest/{pmc}/fullTextXML")
                if st2 != 200 or len(x) < 2000:
                    st3, h = get(f"https://pmc.ncbi.nlm.nih.gov/articles/{pmc}/")   # fallback: the PMC article page (HTML); Europe PMC answers 500 for non-OA-licensed PMC articles
                    if st3 == 200 and len(h) > 20000:
                        h = re.sub(r"<(script|style|nav|header|footer)[^>]*>.*?</\1>", "", h, flags=re.S)
                        m = re.search(r"<section[^>]*(article-body|main-article-body|body)[^>]*>(.*)</section>", h, flags=re.S)
                        h = re.sub(r"<h([1-6])[^>]*>(.*?)</h\1>", lambda mm: "\n\n## " + re.sub(r"<[^>]+>", "", mm.group(2)) + "\n", m.group(2) if m else h, flags=re.S)
                        h = re.sub(r"</(p|li|tr|div|section|figcaption)>", "\n", h)
                        import html as _h
                        txt = re.sub(r"\n{3,}", "\n\n", _h.unescape(re.sub(r"<[^>]+>", "", h)))
                        f = out / f"{pmc}_PMID{pm}_pmc_html_fulltext_{row[0]}.txt"; f.write_text(txt)
                        row[3] = "FULLTEXT_SAVED_PMC_HTML"; row[4] = str(len(txt.split())); row[5] = hashlib.sha256(f.read_bytes()).hexdigest(); row[6] = str(f.relative_to(a.root))
                    else: row[3] = "FULLTEXT_NOT_SERVED" if st2 in (404, 200, 500) else "SERVICE_ERROR"
                if row[3] == "":
                    txt = render(x); f = out / f"{pmc}_PMID{pm}_europepmc_fulltext_{row[0]}.txt"; f.write_text(txt)
                    row[3] = "FULLTEXT_SAVED"; row[4] = str(len(txt.split())); row[5] = hashlib.sha256(f.read_bytes()).hexdigest(); row[6] = str(f.relative_to(a.root))
        with log.open("a") as fh: fh.write("\t".join(row) + "\n")
        print("\t".join(row[1:5] + [row[7]]))
if __name__ == "__main__": main()
