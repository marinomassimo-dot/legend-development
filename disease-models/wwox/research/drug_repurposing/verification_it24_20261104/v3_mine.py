import csv,gzip,collections,sys
G='generation_it22_p1_20261103/'
P=list(csv.DictReader(open(G+'results_p4/proposals_it21.tsv'),delimiter='\t'))
cache={}
def load(sn):
    if sn not in cache:
        d=collections.defaultdict(list)
        for r in csv.DictReader(gzip.open(G+f'eng_merged/contributions_p1_{sn}.tsv.gz','rt'),delimiter='\t'): d[r['family_id']].append(r)
        cache[sn]=d
    return cache[sn]
def classify(rows,orient,thr):
    net=collections.defaultdict(float); both=0
    for r in rows:
        c0,ck=float(r['contrib_hop0']),float(r['contrib_hops1to3'])
        t=r['main_target_hops1to3'] or r['main_target_hop0']
        net[t]+=orient*(c0+ck)
    if not net: return 'NONE',net
    mx=max(abs(v) for v in net.values())
    keep={t:v for t,v in net.items() if abs(v)>=thr*mx and abs(v)>0}
    pos=[t for t,v in keep.items() if v>0]; neg=[t for t,v in keep.items() if v<0]
    if len(keep)<=1: return 'SINGLE_TARGET',net
    if neg: return 'CONFLICT_BETWEEN_TARGETS',net
    return 'MULTI_POSITIVE',net
out=[]
for thr in (0.0,0.1):
    C=collections.Counter(); res={}
    for p in P:
        o=1 if p['hypothesis']=='H_HARM' else -1
        cl,net=classify(load(p['seed_set']).get(p['family_id'],[]),o,thr)
        C[cl]+=1; res[p['proposal_id']]=(cl,net,p)
    print('thr',thr,dict(C))
    if thr==0.0: R0=res
    else: R1=res
H=[r['proposal_id'] for r in csv.DictReader(open(G+'results_p4/handoff_it21.tsv'),delimiter='\t')]
for name,R in (('thr0',R0),('thr0.1',R1)):
    print(name,'handovers',[(h,R[h][0],R[h][2]['compound'][:12]) for h in H if R[h][0]!='SINGLE_TARGET'])
w=csv.writer(open('verification_it24_20261104/v3_mine_rows.tsv','w'),delimiter='\t'); w.writerow(['proposal_id','compound','hyp','class_thr0','class_thr0.1','nets'])
for h,(cl,net,p) in R0.items(): w.writerow([h,p['compound'],p['hypothesis'],cl,R1[h][0],';'.join(f'{t}:{v*(1 if p["hypothesis"]=="H_HARM" else -1):.3g}' for t,v in sorted(net.items(),key=lambda x:-abs(x[1]))[:6])])
# do main_target of proposal exist among nets
miss=[h for h,(cl,net,p) in R0.items() if p['main_target'] not in net]
print('proposal main_target not a row main target',len(miss))
