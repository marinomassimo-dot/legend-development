import urllib.request, json, time, sys
B="https://www.ebi.ac.uk/chembl/api/data"
def get(url):
    url=B+url if url.startswith("/") else url
    for a in range(3):
        try:
            with urllib.request.urlopen(urllib.request.Request(url,headers={"Accept":"application/json"}),timeout=60) as r:
                return json.load(r)
        except Exception as e:
            print("fail",a,str(e)[:60],file=sys.stderr); time.sleep(5)

if __name__=="__main__":
    for u in sys.argv[1:]:
        p=get(u); print(json.dumps(p)[:3000] if p else "NOT VERIFIED", "\n")
