import urllib.error,csv,json,re,sys,os,time,subprocess,urllib.request,urllib.parse
sys.path.insert(0,'framework/scripts')
import registry_records as R
from pathlib import Path
F='disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_map_negatives_residual_20261125'
M='disease-models/wwox/analysis/mechanism_intervention_map.md'
neg=list(csv.DictReader(open(F+'/negatives.tsv'),delimiter='\t'))
rec=[json.loads(l) for l in open('disease-models/wwox/registries/fulltext_read_receipts.jsonl') if l.strip()]
texts={}
for r in R.parse_records(Path('.'),'wwox','paper_registry_current'):
    if r.kind!='record': continue
    for p in set(re.findall(r'(?i)PMID[:\s*]+(\d{7,8})',r.identity_values())): texts.setdefault(p,[]).append(r.text)
def text_of(p):
    t='\n'.join(texts.get(p,[]))
    m=f'disease-models/wwox/research/deepdive_manifests/PMID{p}.json'
    if os.path.exists(m): t+='\n'+open(m,encoding='utf-8').read()
    return t
cache={}
def epmc(q):
    ids=set(); cur='*'; hit=0
    for _ in range(5):
        u='https://www.ebi.ac.uk/europepmc/webservices/rest/search?'+urllib.parse.urlencode({'query':q,'format':'json','pageSize':1000,'resultType':'idlist','cursorMark':cur})
        for a in range(4):
            try: j=json.load(urllib.request.urlopen(u,timeout=60)); break
            except urllib.error.HTTPError as e:
                if e.code not in (500,502,503,504) or a==3: raise
                time.sleep(20*(a+1))
            except (TimeoutError, urllib.error.URLError, OSError) as e:
                if a==3: raise
                time.sleep(20*(a+1))
        ids|={x.get('pmid') for x in j['resultList']['result'] if x.get('pmid')}; hit=j['hitCount']
        n=j.get('nextCursorMark')
        if not n or n==cur or not j['resultList']['result']: break
        cur=n; time.sleep(0.8)
    return ids,hit
txt=open(M).read().split('\n')
out=[]; dates=[]
for n in neg:
    i=n['id']
    log=subprocess.run(['git','log','-S',n['phrase'],'--format=%h%x09%aI%x09%s','--',M],capture_output=True,text=True).stdout.strip().split('\n')
    first=log[-1].split('\t') if log[-1] else ['?','?','?']
    d=first[1][:19]
    dates.append([i,d,first[0],first[2][:90]])
    rx=re.compile(n['object_terms'],re.I)
    before={};after={}
    for r in rec:
        p=str((r.get('study_id') or {}).get('pmid') or '')
        if not p.isdigit(): continue
        (after if r['event_at'][:19]>d else before).setdefault(p,[]).append(r['event_id'])
    def hits(S): return sorted(p for p in S if rx.search(cache.setdefault(p,text_of(p))))
    a_b=hits(before); a_a=hits(after)
    ids,hit=epmc(n['europepmc_query']); time.sleep(0.8)
    b_all=sorted(p for p in ids if p in before or p in after)
    b_before=[p for p in b_all if p in before]; b_after=[p for p in b_all if p in after]
    out.append([i,d[:10],len(a_b),len(a_a),len(b_before),len(b_after),hit,' '.join(a_b),' '.join(a_a),' '.join(b_before),' '.join(b_after)])
    print(i,d[:10],'A_before',len(a_b),'A_after',len(a_a),'B_before',len(b_before),'B_after',len(b_after),'epmc',hit,flush=True)
with open(F+'/dates.tsv','w',newline='') as fh:
    w=csv.writer(fh,delimiter='\t',lineterminator='\n'); w.writerow(['id','first_written','first_commit','commit_subject']); w.writerows(dates)
with open(F+'/receipts_routes.tsv','w',newline='') as fh:
    w=csv.writer(fh,delimiter='\t',lineterminator='\n'); w.writerow(['id','since','a_before_n','a_after_n','b_before_n','b_after_n','epmc_hitcount','a_before_pmids','a_after_pmids','b_before_pmids','b_after_pmids']); w.writerows(out)
