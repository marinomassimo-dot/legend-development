import urllib.error,csv,json,re,sys,glob,os,time,urllib.request,urllib.parse
sys.path.insert(0,'framework/scripts')
import registry_records as R
from pathlib import Path
F='disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_adv266_20261125'
root=Path('.')
neg=list(csv.DictReader(open(F+'/negatives.tsv'),delimiter='\t'))
dates={r['id']:r for r in csv.DictReader(open(F+'/dates.tsv'),delimiter='\t')}
rec=[json.loads(l) for l in open('disease-models/wwox/registries/fulltext_read_receipts.jsonl') if l.strip()]
texts={}
for stem in ('paper_registry_current','literature_tracking_log_current'):
    for r in R.parse_records(root,'wwox',stem):
        if r.kind!='record': continue
        for p in set(re.findall(r'(?i)PMID[:\s*]+(\d{7,8})',r.identity_values())):
            texts.setdefault(p,[]).append(r.text)
def text_of(p):
    t='\n'.join(texts.get(p,[]))
    m=f'disease-models/wwox/research/deepdive_manifests/PMID{p}.json'
    if os.path.exists(m): t+='\n'+open(m,encoding='utf-8').read()
    return t
def epmc(q):
    ids=set(); cur='*'
    for _ in range(5):
        u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','pageSize':1000,'resultType':'idlist','cursorMark':cur})
        for attempt in range(4):
            try:
                j=json.load(urllib.request.urlopen(u,timeout=60)); break
            except urllib.error.HTTPError as e:
                if e.code not in (500,502,503,504) or attempt==3: raise
                time.sleep(20*(attempt+1))
        ids|={x.get('pmid') for x in j['resultList']['result'] if x.get('pmid')}
        n=j.get('nextCursorMark'); 
        if not n or n==cur or not j['resultList']['result']: break
        cur=n; time.sleep(0.8)
    return ids,j['hitCount']
Q={'G01':'("GABA reversal" OR "E_GABA" OR "intracellular chloride" OR NKCC1 OR KCC2)','G02':'EXT_ID:36621327','G03':'(senolytic OR navitoclax OR dasatinib)','G04':'calpain','G05':'("conditional knockout" OR "Synapsin-Cre" OR "Nestin-Cre")','G06':'(CC1 AND PDGFR AND myelin)','G07':'(hypomorph OR hypomorphic)','G08':'("tamoxifen" OR CreERT OR "inducible knockout")','G09':'("gene therapy" AND ("after onset" OR "post-onset" OR symptomatic))','G10':'(NMDA OR NMDAR OR GluN OR GRIN)','G11':'(carbenoxolone OR connexin OR "gap junction")','G12':'memantine','G13':'(NMDA OR NMDAR OR GluN OR GRIN)','G14':'("pyruvate dehydrogenase" OR PDHA1)','G15':'(Seahorse OR "extracellular acidification" OR "oxygen consumption rate" OR fluxomics OR "13C")','G16':'"1057-2"','G17':'("clinical trial" AND AAV)','G18':'(cognition OR cognitive OR cerebellum OR cerebellar)','G19':'(tankyrase OR XAV939)','G20':'(GSK3B OR "GSK3 beta" OR "glycogen synthase kinase")'}
cache={}; out=[]
for n in neg:
    i=n['id']; d=dates[i]['first_written']
    later={}
    for r in rec:
        p=str((r.get('study_id') or {}).get('pmid') or '')
        if p.isdigit() and r['event_at'][:19]>d: later.setdefault(p,[]).append(r['event_id'])
    if i=='G02':
        a=sorted(p for p in later if p=='36621327'); b=a; hit=0
    else:
        rx=re.compile(n['object_terms'],0 if i in('G06','G17') else re.I)
        a=sorted(p for p in later if rx.search(cache.setdefault(p,text_of(p))))
        ids,hit=epmc(f'WWOX AND {Q[i]}'); time.sleep(0.8)
        b=sorted(p for p in later if p in ids)
    both=sorted(set(a)&set(b))
    out.append([i,d[:10],len(later),len(a),len(b),len(both),hit,Q[i],' '.join(a),' '.join(b)])
    print(i,d[:10],'later_pmids',len(later),'routeA',len(a),'routeB',len(b),'both',len(both),'epmc_hits',hit,flush=True)
with open(F+'/later_receipts.tsv','w',newline='') as fh:
    w=csv.writer(fh,delimiter='\t',lineterminator='\n'); w.writerow(['id','since','later_receipted_pmids','route_a_n','route_b_n','both_n','epmc_hitcount','epmc_query','route_a_pmids','route_b_pmids']); w.writerows(out)
