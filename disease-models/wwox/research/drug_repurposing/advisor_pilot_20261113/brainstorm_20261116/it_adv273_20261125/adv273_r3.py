import urllib.request,urllib.parse,json,time,datetime,sys
comp={'valproate':'(valproate[tiab] OR "valproic acid"[tiab] OR "sodium valproate"[tiab])','entinostat':'(entinostat[tiab] OR MS-275[tiab])','trichostatin':'("trichostatin A"[tiab] OR trichostatin[tiab])','panobinostat':'panobinostat[tiab]','vorinostat':'(vorinostat[tiab] OR SAHA[tiab] OR "suberoylanilide hydroxamic acid"[tiab])','belinostat':'belinostat[tiab]','butyrate':'(butyrate[tiab] OR "sodium butyrate"[tiab])','phenylbutyrate':'(phenylbutyrate[tiab] OR "4-phenylbutyric acid"[tiab] OR 4-PBA[tiab])','HDAC generic':'("histone deacetylase inhibitor"[tiab] OR "histone deacetylase inhibitors"[tiab] OR "HDAC inhibitor"[tiab] OR "HDAC inhibitors"[tiab] OR HDACi[tiab])'}
W='(WWOX[tiab] OR "WW domain-containing oxidoreductase"[tiab] OR FRA16D[tiab])'
today=datetime.date.today().isoformat(); out=[]
for k,q in comp.items():
    query=f'{W} AND {q}'
    u='https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&retmode=json&retmax=50&term='+urllib.parse.quote(query)
    for attempt in range(3):
        try: d=json.load(urllib.request.urlopen(u,timeout=60)); break
        except Exception as e: time.sleep(3); d=None
    ids=d['esearchresult']['idlist'] if d else None
    out.append((today,'R3 PubMed esearch',k,query,len(ids) if ids is not None else 'ERROR',' '.join(ids or [])))
    time.sleep(0.5)
with open(sys.argv[1],'w') as f:
    f.write('date\troute\tcompound\tquery\tcount\tpmids\n')
    for r in out: f.write('\t'.join(map(str,r))+'\n')
for r in out: print(r[2],r[4],r[5][:120])
