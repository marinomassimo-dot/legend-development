import re, html, sys, collections
V="disease-models/wwox/research/drug_repurposing/view/"
EN=set("the of and to in for with by from not no is are was were that this these those as at on or be has have had its their which when than into only data record time access fatty acids acid none radial glia".split())
OWN={"fr":set("le la les des du de un une et en pour avec par dans sur est sont pas ce cette ces au aux ou qui que dont non aucun donnée données".split()),
     "de":set("der die das den dem des ein eine und in für mit von nicht ist sind war zu auf oder wird bei aus nur keine kein daten".split()),
     "es":set("el la los las del de un una y en para con por no es son este esta estos al o que se sin datos solo".split())}
for lg in ("fr","de","es"):
    page=open(V+f"index.{lg}.html",encoding="utf-8").read()
    body=re.sub(r"<script\b.*?</script>|<style\b.*?</style>","",page,flags=re.S)
    body=re.sub(r"<(\w+)\b[^>]*(?:class=\"orig\"|lang=\"(?:it|en)\")[^>]*>.*?</\1>","",body,flags=re.S)
    nodes={re.sub(r"\s+"," ",html.unescape(t)).strip() for t in re.findall(r">([^<>]+)<",body)}
    hits=[]
    for n in nodes:
        w=re.findall(r"[a-zà-ü]+",n.lower())
        if len(n)<8 or len(w)<2: continue
        e=sum(x in EN for x in w); o=sum(x in OWN[lg] for x in w)
        if e>=2 and o==0 or (e>=1 and o==0 and len(w)<=4 and not re.search(r"[A-Z]{2,}|\d",n) and False): hits.append(n)
    print(lg,"nodes",len(nodes),"english-looking",len(hits)); 
    for h in sorted(hits)[:8]: print("   ",h[:110])
