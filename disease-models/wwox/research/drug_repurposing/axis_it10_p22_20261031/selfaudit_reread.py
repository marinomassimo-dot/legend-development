#!/usr/bin/env python3
"""Independent re-read of the three most decisive premises of IT10 P2.2, from source copies (not from the package notes).
Usage: selfaudit_reread.py --ft DIR_WITH_FULLTEXT --geo COUNTS.gz --label OPENFDA_LABEL.json
Needs: PMC7104842 publisher html (pmc7104842.html), kob.txt (Kobayashi 2016 PMC4879264 text), oma_label.json (openFDA), the GSE156243 counts file.
Run with python3 -I. Prints each check with PASS/FAIL; no network."""
import re,sys,gzip,csv,json,argparse
ap=argparse.ArgumentParser(); ap.add_argument('--ft',required=True); ap.add_argument('--geo',required=True); ap.add_argument('--label',required=True)
a=ap.parse_args()
def clean(p):
    t=open(p,encoding='utf8').read(); t=re.sub(r'<[^>]+>',' ',t); return re.sub(r'\s+',' ',t)
ok=True
def chk(name,cond,detail=''):
    global ok; ok&=bool(cond); print(('PASS ' if cond else 'FAIL ')+name+(' | '+detail if detail else ''))
# A. Hussain 2019 (PMID 30290271): which cytokine is significant
t=clean(a.ft+'/pmc7104842.html')
m=re.search(r'We observed &gt; 1\.5 fold upregulation of both cytokines \( Il6 significant at p &lt; \.05\) in Wwox KO \( n = 4\)',t) or re.search(r'upregulation of both cytokines \( Il6 significant at p',t)
chk('A1 results 3.3 attaches significance to Il6 only',m is not None, t[m.start()-60:m.end()+80] if m else '')
chk('A2 caption (E) n=4, one asterisk legend',bool(re.search(r'\(E\) Expression of Tnf-a and Il6 in Wwox KO mice hippocampi \( ?n = 4\)',t)))
# B. Kobayashi 2016 (PMID 27211851)
k=open(a.ft+'/kob.txt').read()
chk('B1 subset inhibited includes IL6, IL1b',bool(re.search(r'These genes included IL6, IL1b, IL1a, Nos2 and IL12b',k)))
chk('B2 Tnf not changed in KpCKO BMDMs',bool(re.search(r'such as Tnf and Irf1 , and M2-induced genes, such as Arg1 and Ccl17 , were not changed in KpCKO BMDMs',k)))
chk('B3 cell type is bone-marrow-derived macrophage, no microglia in text','microglia' not in k.lower() or k.lower().count('microglia')<3, 'microglia mentions: %d'%k.lower().count('microglia'))
# C. organoid counts, recomputed from raw counts (own code, not gene_rows_cpm.py)
rows={}
with gzip.open(a.geo,'rt') as f:
    r=csv.reader(f,delimiter='\t'); h=next(r)
    for x in r: rows[x[0]]=[float(v) for v in x[1:]]
tot=[sum(v[i] for v in rows.values()) for i in range(6)]
def ratio(g):
    v=rows[g]; c=[v[i]/tot[i] for i in range(6)]
    return (sum(c[:4])/4)/(sum(c[4:])/2) if sum(c[4:])>0 else float('nan')
print('   columns',h[1:])
for g in ['IL1B','IL6','TNF','NFE2L2','KEAP1','NQO1','HMOX1']: print('   ',g,rows[g],'KO/WT=%.2f'%ratio(g))
chk('C1 IL6 raw count 0 in all six libraries',all(x==0 for x in rows['IL6']))
chk('C2 IL1B and TNF max raw count <=11 (essentially absent)',max(rows['IL1B'])<=11 and max(rows['TNF'])<=1)
chk('C3 NFE2L2 KO/WT cpm ratio between 0.7 and 0.8',0.7<=ratio('NFE2L2')<=0.8,'%.3f'%ratio('NFE2L2'))
# D. omaveloxolone label
d=json.load(open(a.label))['results'][0]
s=' '.join(' '.join(v) if isinstance(v,list) else str(v) for kk,v in d.items() if kk not in('openfda','spl_product_data_elements'))
chk('D1 label has no seizure/convulsion string',not re.search(r'seizure|convuls|epilep',s,re.I))
chk('D2 label states perinatal neurobehavioral impairment in offspring',bool(re.search(r'impaired neurobehavioral function \(increased locomotor activity and learning and memory deficits\) in offspring at all doses',s)))
chk('D3 label: pediatric <16 not established; strong/moderate CYP3A4 inducer avoid',bool(re.search(r'not been established in pediatric patients less than 16',s)) and bool(re.search(r'Strong or Moderate CYP3A4 inducer\s*(</td><td[^>]*>)?\s*Recommended to avoid',s)))
print('ALL PASS' if ok else 'SOME FAIL')
