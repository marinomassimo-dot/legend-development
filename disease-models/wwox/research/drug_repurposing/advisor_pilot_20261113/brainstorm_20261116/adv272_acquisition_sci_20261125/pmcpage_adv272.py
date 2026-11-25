import urllib.request,re,time
UA={"User-Agent":"legend-research-client/1.0 (plain request; no browser identity)"}
for pm,pmc in [("20810895","PMC3070296"),("23141539","PMC3496186"),("24321005","PMC4102583"),("40994429","PMC12677382")]:
    url="https://pmc.ncbi.nlm.nih.gov/articles/%s/"%pmc
    try:
        r=urllib.request.urlopen(urllib.request.Request(url,headers=UA),timeout=60); b=r.read(); s=r.status; u=r.geturl()
    except urllib.error.HTTPError as e:
        s=e.code; b=e.read()[:400]; u=url
    except Exception as e:
        s="ERR:"+str(e)[:50]; b=b""; u=url
    t=re.sub(r"\s+"," ",re.sub(r"<[^>]+>"," ",b.decode("utf8","replace")))
    print(pm,pmc,s,len(b),("recaptcha" if re.search("recaptcha|captcha|Just a moment",b.decode("utf8","replace"),re.I) else "no-captcha-marker"),("has Methods" if "Materials and Methods" in t or "Methods" in t[:100000] else ""),t[:120],flush=True)
    if s==200 and len(b)>50000: open("pmcpage_%s.html"%pm,"wb").write(b)
    time.sleep(10)
print("done",flush=True)
