import urllib.request, urllib.parse, json, time, re
UA={"User-Agent":"legend-research-client/1.0 (plain request; no browser identity)"}
def get(url,timeout=60):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.read()[:300]
    except Exception as e:
        return "ERR:"+str(e)[:60], b""
out=[]
for pm,pmc in [("20810895","PMC3070296"),("23141539","PMC3496186"),("24321005","PMC4102583"),("40994429","PMC12677382")]:
    s,b=get("https://www.ebi.ac.uk/europepmc/webservices/rest/%s/fullTextXML"%pmc)
    out.append((pm,pmc,"epmc_fullTextXML",s,len(b),re.sub(r"\s+"," ",b[:160].decode("utf8","replace"))))
    print(out[-1],flush=True); time.sleep(5)
s,b=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":"EXT_ID:40875931 AND SRC:MED","format":"json","resultType":"core"}))
doi=""
if s==200:
    res=json.loads(b).get("resultList",{}).get("result",[]); doi=res[0].get("doi","") if res else ""
print("40875931 doi",doi,flush=True); time.sleep(5)
if doi:
    s,b=get("https://doi.org/"+doi)
    print(("40875931",doi,"doi.org plain GET",s,len(b),re.sub(r"\s+"," ",b[:160].decode("utf8","replace"))),flush=True); time.sleep(5)
s,b=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":"EXT_ID:36601084 AND SRC:MED","format":"json","resultType":"core"}))
print("36601084 flag",s, (lambda d:(d[0].get("isOpenAccess"),d[0].get("pmcid"),d[0].get("hasSuppl")) if d else "none")(json.loads(b).get("resultList",{}).get("result",[])) if s==200 else "",flush=True); time.sleep(5)
print("done",flush=True)
