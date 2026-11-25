"""ADV-272 step 2: acquire open-access full text XML from Europe PMC (fullTextXML), one request at a time, 3 s apart, declared generic client, no e-mail,
stop on two consecutive route failures. Usage: acquire_adv272.py FLAGS_TSV OUT_DIR LOG_TSV"""
import sys, csv, time, hashlib, re, urllib.request
import xml.etree.ElementTree as ET
if len(sys.argv) != 4 or sys.argv[1] in ("-h", "--help"):
    print(__doc__); raise SystemExit(0)
flags, out, log = sys.argv[1:4]
rows = [r for r in csv.DictReader(open(flags), delimiter="\t") if r["isOpenAccess"] == "Y" and r["pmcid"]]
fails = 0
res = []
import os, glob
for r in rows:
    pm, pmc = r["study_key"], r["pmcid"]
    if glob.glob("%s/PMID%s_ADV272_*" % (out, pm)):
        continue
    url = "https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML" % pmc
    req = urllib.request.Request(url, headers={"User-Agent": "legend-research-client/1.0 (plain request; no browser identity)"})
    status = "ok"; sha = ""; nsec = nfig = ntab = 0; title_ok = ""; pmid_ok = ""; path = ""
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
        fails = 0
        head = data[:400].decode("utf8", "replace")
        if b"<article" not in data[:3000] and b"<pmc-articleset" not in data[:3000]:
            status = "not_xml_article:" + re.sub(r"\s+", " ", head)[:80]
        else:
            root = ET.fromstring(data)
            ids = {(e.get("pub-id-type"), (e.text or "").strip()) for e in root.iter("article-id")}
            pmid_ok = "Y" if ("pmid", pm) in ids else "N"
            ttl = re.sub(r"\s+", " ", "".join(root.find(".//article-title").itertext())).lower() if root.find(".//article-title") is not None else ""
            want = re.sub(r"<[^>]+>|&lt;[^&]*&gt;|\s+", " ", r["title"]).lower().strip()[:40]
            have = re.sub(r"\s+", " ", ttl)[:200]
            title_ok = "Y" if want and want.split()[0] in have and (want[:25] in have or want[:25].replace("-", " ") in have.replace("-", " ")) else "check"
            nsec = len(list(root.iter("sec"))); nfig = len(list(root.iter("fig"))); ntab = len(list(root.iter("table-wrap")))
            sha = hashlib.sha256(data).hexdigest()
            path = "%s/PMID%s_ADV272_%s_epmc_20261125.xml" % (out, pm, pmc)
            open(path, "wb").write(data)
    except Exception as e:
        status = "route_result:" + str(e)[:70]; fails += 1
    res.append((r["rank"], pm, pmc, status, pmid_ok, title_ok, nsec, nfig, ntab, sha, path))
    print(res[-1], flush=True)
    if fails >= 2:
        print("two consecutive route failures: stopping, no retry", flush=True); break
    time.sleep(4)
with open(log, "w") as o:
    w = csv.writer(o, delimiter="\t", lineterminator="\n")
    w.writerow("rank pmid pmcid status pmid_in_xml title_agrees sec fig table_wrap sha256 path".split()); w.writerows(res)
print("done", flush=True)
