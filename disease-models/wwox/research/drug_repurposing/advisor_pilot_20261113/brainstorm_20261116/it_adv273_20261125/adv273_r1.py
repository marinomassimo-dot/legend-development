import re,glob,os,json,sys
root='disease-models/wwox'
terms=r'valpro|entinostat|MS-275|trichostatin|panobinostat|vorinostat|\bSAHA\b|belinostat|butyrate|phenylbutyr|histone deacetylase inhibit|HDAC ?inhibit|HDACi|\bHDACIs?\b'
tre=re.compile(terms,re.I); wre=re.compile(r'WWOX|WW domain.containing oxidoreductase',re.I)
def split_md(text,pat):
    parts=re.split(pat,text); return parts
files={'discovery_ledger':('registries/../research/discovery_ledger_current.md',r'(?m)^(?=### )'),
 'paper_registry':('registries/paper_registry_current.md',r'(?m)^(?=## )'),
 'literature_log':('registries/literature_tracking_log_current.md',r'(?m)^(?=## )'),
 'claim_registry':('registries/claim_registry_current.md',r'(?m)^(?=## )'),
 'batch_queue':('registries/batch_queue.md',r'(?m)^(?=\| \[)')}
out=[]
for k,(p,pat) in files.items():
    path=os.path.join(root,p)
    if not os.path.exists(path): print('missing',path); continue
    t=open(path,encoding='utf-8',errors='replace').read()
    recs=re.split(pat,t); n=0
    for r in recs:
        if tre.search(r) and wre.search(r):
            n+=1; head=r.strip().split('\n')[0][:120]; out.append((k,head,sorted(set(m.group(0).lower() for m in tre.finditer(r)))))
    print(k,'records',len(recs),'with compound+WWOX',n)
for p in glob.glob(root+'/registries/corpus_seed_pubmed_*.tsv')+glob.glob(root+'/registries/corpus_seed_pubmed_*.jsonl')+[root+'/registries/fulltext_read_receipts.jsonl']:
    n=0
    for l in open(p,encoding='utf-8',errors='replace'):
        if tre.search(l) and wre.search(l):
            n+=1; out.append((os.path.basename(p),l[:110].strip(),sorted(set(m.group(0).lower() for m in tre.finditer(l)))))
    print(os.path.basename(p),'lines with compound+WWOX',n)
json.dump(out,open(sys.argv[1],'w'),indent=0)
