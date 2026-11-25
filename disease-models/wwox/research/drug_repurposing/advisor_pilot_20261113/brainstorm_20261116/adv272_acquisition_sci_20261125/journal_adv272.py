import urllib.request, urllib.parse, json, time, re
UA={"User-Agent":"legend-research-client/1.0 (plain request; no browser identity)"}
def get(url,timeout=60):
    try:
        with urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=timeout) as r:
            return r.status, r.headers.get("Content-Type",""), r.read(), r.geturl()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type","") if e.headers else "", e.read()[:300], url
    except Exception as e:
        return "ERR:"+str(e)[:60], "", b"", url
for pm in ["16818616","25720522","18460020"]:
    s,ct,b,u=get("https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":"EXT_ID:%s AND SRC:MED"%pm,"format":"json","resultType":"core"}))
    time.sleep(3)
    if s!=200: print(pm,"epmc search",s,flush=True); continue
    res=json.loads(b).get("resultList",{}).get("result",[])
    x=res[0]; doi=x.get("doi",""); urls=[(u.get("availabilityCode"),u.get("documentStyle"),u.get("site"),u.get("url")) for u in x.get("fullTextUrlList",{}).get("fullTextUrl",[])]
    print(pm,"doi",doi,"journal",x.get("journalInfo",{}).get("journal",{}).get("title"),"year",x.get("pubYear"),"urls",urls,flush=True)
    tried=set()
    for av,style,site,url in urls:
        if av in ("F","OA") and url not in tried:
            tried.add(url); s,ct,b,u2=get(url); print("  GET",site,av,url[:90],"->",s,ct[:30],len(b),re.sub(r"\s+"," ",b[:80].decode("utf8","replace")),flush=True); time.sleep(5)
    if doi:
        s,ct,b,u2=get("https://doi.org/"+doi); print("  doi.org",doi,"->",s,ct[:30],u2[:90],len(b),re.sub(r"\s+"," ",b[:80].decode("utf8","replace")),flush=True); time.sleep(5)
print("done",flush=True)
