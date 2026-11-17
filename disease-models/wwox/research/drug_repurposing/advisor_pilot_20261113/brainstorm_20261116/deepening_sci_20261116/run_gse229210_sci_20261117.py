import gzip, math, random, json, sys
path = sys.argv[1]
ids = {'AXIN2':'ENSG00000168646','LEF1':'ENSG00000138795','NKD1':'ENSG00000140807','APCDD1':'ENSG00000154856',
       'TCF7L2':'ENSG00000148737','WNT5A':'ENSG00000114251','CTNNB1':'ENSG00000168036','WWOX':'ENSG00000186153'}
R4 = ['AXIN2','LEF1','NKD1','APCDD1']; R7 = R4+['TCF7L2','WNT5A','CTNNB1']
rows = {}
with gzip.open(path,'rt') as f:
    hdr = f.readline().rstrip('\n').split('\t')[1:]
    for l in f:
        p = l.rstrip('\n').split('\t'); rows[p[0].split('.')[0]] = [float(x) for x in p[1:]]
lines = ['DBTRG-05MG','T98G','U87MG','U251MG']
idx = {ln: ([i for i,h in enumerate(hdr) if h.startswith(ln+'_vec')], [i for i,h in enumerate(hdr) if h.startswith(ln+'_WWOX')]) for ln in lines}
assert all(len(v[0])==3 and len(v[1])==3 for v in idx.values())
def cell(g, ln):
    v = rows.get(g)
    if v is None: return None
    vec = sum(v[i] for i in idx[ln][0])/3; oe = sum(v[i] for i in idx[ln][1])/3
    if max(vec, oe) < 1: return ('unmeasured', vec, oe, None)
    return ('ok', vec, oe, math.log2(oe+1)-math.log2(vec+1))
out = {'cells':{}}
for sym in list(ids):
    out['cells'][sym] = {ln: cell(ids[sym], ln) for ln in lines}
def stat(genes_ids):
    n=d=0; big=0
    for g in genes_ids:
        for ln in lines:
            c = cell(g, ln)
            if c and c[0]=='ok':
                n+=1; d += (c[3]<0); big += (abs(c[3])>=0.5)
    return n, d, big
for name, S in (('R4',R4),('R7',R7)):
    n,d,big = stat([ids[s] for s in S])
    out[name] = {'expressed_cells':n,'down':d,'S':(d/n if n else None),'abs>=0.5':big}
# class
n,d = out['R4']['expressed_cells'], out['R4']['down']
if n<8: cls='U'
else:
    s=d/n; cls = 'P' if s>=0.75 else ('O' if s<=0.25 else 'M')
out['class']=cls
# matched null: decile of overall mean CPM
allm = {g: sum(v)/len(v) for g,v in rows.items()}
srt = sorted(allm, key=allm.get); dec = {g: min(9, int(10*i/len(srt))) for i,g in enumerate(srt)}
bydec = {}
for g in srt: bydec.setdefault(dec[g], []).append(g)
random.seed(229210)
sims=[]
for _ in range(1000):
    gs = [random.choice(bydec[dec[ids[s]]]) for s in R4]
    n2,d2,_b = stat(gs)
    if n2: sims.append(d2/n2)
out['null'] = {'n_sims_with_cells':len(sims),'mean_S':sum(sims)/len(sims),
  'frac_null_S_ge_obs': sum(1 for s in sims if out['R4']['S'] is not None and s>=out['R4']['S'])/len(sims),
  'frac_null_S_le_obs': sum(1 for s in sims if out['R4']['S'] is not None and s<=out['R4']['S'])/len(sims)}
out['deciles'] = {s: dec[ids[s]] for s in ids}
# WWOX check
out['wwox_overexpression_check'] = {ln: out['cells']['WWOX'][ln] for ln in lines}
print(json.dumps(out, indent=1))
