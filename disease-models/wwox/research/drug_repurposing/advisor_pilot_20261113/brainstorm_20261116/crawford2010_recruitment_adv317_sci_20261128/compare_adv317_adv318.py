import re,sys
he=open('/home/desktop/legend-development/.claude/worktrees/sci_bc_20261128/disease-models/wwox/research/drug_repurposing/brainstorm_20261116/adv318_blind_crawford_he_20261128/BLIND_READING.md').read()
def tab(header_start):
    i=he.index(header_start); rows=[]
    for l in he[i:].splitlines()[2:]:
        if not l.startswith('|'): break
        rows.append([c.strip() for c in l.strip('|').split('|')])
    return rows
def num(s):
    m=re.match(r'~?([0-9.]+)',s); return float(m.group(1)) if m else None
f8={r[0]:r[1:] for r in tab('| mA | N1 normal')}
cols=['N1 normal','N1 vehicle','N1 ligand D20','N1 ligand D36','N2 normal','N2 vehicle','N2 ligand D20','N2 ligand D36']
# delegate Fig 8 (SCI side): mA 1,2,3,4 ; rows
sci8={'N1 normal':[.31,.66,.97,1.07],'N1 ligand D36':[.24,.61,.80,.90],'N1 ligand D20':[.17,.47,.68,.80],'N1 vehicle D20':[.17,.41,.54,.59],'N1 vehicle D36':[.17,.38,.52,.55],
'N2 normal':[.08,.39,.67,.84],'N2 ligand D36':[.07,.29,.50,.60],'N2 ligand D20':[.07,.28,.42,.45],'N2 vehicle D20':[.07,.21,.31,.35],'N2 vehicle D36':[.07,.20,.30,.33]}
print('FIG 8 (mV): group, mA, SCI-delegate, HE, diff')
mx=0;bad=[]
for g,vals in sci8.items():
    key=g.replace(' D20','').replace(' D36','') if 'vehicle' in g else g
    key=key.replace('N1 ligand','N1 ligand').strip()
    if 'vehicle' in g: key=g.split(' D')[0]
    for mA,v in zip(['1.0','2.0','3.0','4.0'],vals):
        h=num(f8[mA][cols.index(key)])
        d=round(v-h,2); mx=max(mx,abs(d))
        if abs(d)>=0.03: bad.append((g,mA,v,h,d))
        print(g,mA,v,h,d)
print('max abs diff',mx,'cells >=0.03:',bad)

print('\nFIG 9B (percent C2/C1)')
f9={r[0]:r[1:] for r in tab('| ms | N1 normal')}
c9=['N1 normal','N1 vehicle','N1 ligand','N2 normal','N2 vehicle','N2 ligand']
sci9={'N1':{'ms':[2,2.5,3,3.5,4,5,6,8],'normal':[43,57,61,71,76,82,88,90],'ligand':[22,31,46,56,66,78,88,90],'vehicle':[12,17,28,40,48,66,82,90]},
      'N2':{'ms':[2,3,4,5,6,8],'normal':[25,39,52,55,64,73],'ligand':[18,39,56,62,72,78],'vehicle':[11,29,50,62,72,78]}}
n=0;mx=0;big=[]
for comp,d in sci9.items():
    for grp in ('normal','ligand','vehicle'):
        for ms,v in zip(d['ms'],d[grp]):
            key=f'{comp} {grp}'
            k=('%.1f'%ms)
            h=f9[k][c9.index(key)]
            hv=num(h)
            if hv is None: print('HE NR',key,ms,'SCI',v); continue
            diff=v-hv; n+=1; mx=max(mx,abs(diff))
            if abs(diff)>2: big.append((key,ms,v,hv,diff))
print('cells compared',n,'max abs diff',mx,'cells with |diff|>2:',big)
# exploratory ratios (HE table)
print('\nN1/N2 vehicle/normal ratio per mA (HE table, computed now)')
for comp in ('N1','N2'):
    print(comp,[ (mA, round(num(f8[mA][cols.index(comp+' vehicle')])/num(f8[mA][cols.index(comp+' normal')]),2)) for mA in f8])
