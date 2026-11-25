import sys,re,os,json,csv
sys.path.insert(0,'framework/scripts')
import registry_records as R
from pathlib import Path
texts={}
for r in R.parse_records(Path('.'),'wwox','paper_registry_current'):
    if r.kind!='record': continue
    for p in set(re.findall(r'(?i)PMID[:\s*]+(\d{7,8})',r.identity_values())): texts.setdefault(p,[]).append(r.text)
def tx(p):
    t='\n'.join(texts.get(p,[]))
    m=f'disease-models/wwox/research/deepdive_manifests/PMID{p}.json'
    if os.path.exists(m): t+='\n'+open(m,encoding='utf-8').read()
    return t
rid=sys.argv[1]; col=sys.argv[2]; lim=int(sys.argv[3]) if len(sys.argv)>3 else 99
neg={r['id']:r for r in csv.DictReader(open('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_map_negatives_residual_20261125/negatives.tsv'),delimiter='\t')}
rt={r['id']:r for r in csv.DictReader(open('disease-models/wwox/research/drug_repurposing/advisor_pilot_20261113/brainstorm_20261116/it_map_negatives_residual_20261125/receipts_routes.tsv'),delimiter='\t')}
rx=re.compile(neg[rid]['object_terms'],re.I)
for p in rt[rid][col].split()[:lim]:
    t=re.sub(r'\s+',' ',tx(p)); m=rx.search(t)
    title=re.search(r'(?i)full title:\*?\*?\s*([^|\n]{0,110})',tx(p))
    print(p,(title.group(1).strip() if title else '')[:90],'||',(t[max(0,m.start()-120):m.start()+230] if m else 'NOHIT'))
    print()
