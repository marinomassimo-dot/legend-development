#!/usr/bin/env python3
"""Title-level screen through the Europe PMC REST search (lite records, one request per call, no key, no contact parameter). Usage: epmc_title_screen.py QUERY [N]. Used for the sourcing pass of the checklist test."""
import json,sys,time,urllib.request,urllib.parse
if len(sys.argv)<2 or sys.argv[1] in ("-h","--help"):
    print(__doc__); sys.exit(0 if len(sys.argv)>1 else 2)
q=sys.argv[1]; n=int(sys.argv[2]) if len(sys.argv)>2 else 40
url="https://www.ebi.ac.uk/europepmc/webservices/rest/search?"+urllib.parse.urlencode({"query":q,"resultType":"lite","pageSize":n,"format":"json","sort":"P_PDATE_D desc"})
r=urllib.request.urlopen(urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0 (compatible; reader)"}),timeout=30).read().decode()
if r.lstrip().startswith("<"): print("CHALLENGE"); sys.exit(1)
d=json.loads(r); print("hits",d.get("hitCount"))
for x in d["resultList"]["result"]:
    print(x.get("pmid") or x.get("id"),"|",x.get("firstPublicationDate"),"|",(x.get("title") or "")[:140])
