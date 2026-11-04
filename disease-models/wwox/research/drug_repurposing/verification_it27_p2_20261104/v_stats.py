"""Verifier stage 3: group statistics. Usage: python3 -I v_stats.py <out_dir>   (reads v_areas_long.tsv, v_qc_gate.json)
Units of replication = pools of 10 heads (n=5 per cell). Cells: C=(ctrl RNAi,LacZ) D=(Wwox RNAi,LacZ) G=(ctrl RNAi,Abeta42) H=(Wwox RNAi,Abeta42);
the letter->group map is read from the ISA sample sheet s_MTBLS12344.txt (via the assay MS Assay Name), not assumed.
Normalisations: raw area; TIC (area / file MS1 TIC * median TIC); reference-panel (median ratio of 6 amino acids, fixed before looking).
Primary pre-declared family: 2-HG and citrate x {KD in LacZ, KD in Abeta, interaction}; all others diagnostic."""
import sys,os,csv,json,math
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vstats as V
out=sys.argv[1]
rows=list(csv.DictReader(open(os.path.join(out,'v_areas_long.tsv')),delimiter='\t'))
qc=json.load(open(os.path.join(out,'v_qc_gate.json')))
CELL={('RNAi Control','LacZ'):(0,0),('Wwox RNAi','LacZ'):(1,0),('RNAi Control','AB42'):(0,1),('Wwox RNAi','AB42'):(1,1)}
files={};tic={}
for r in rows:
    if r['assay_name'].endswith('_KDExp'):
        files[r['file']]=CELL[(r['group_wwox'],r['group_amyloid'])];tic[r['file']]=float(r['tic'])
def A(t,ppm=5):
    return {r['file']:float(r['area']) for r in rows if r['target']==t and r['ppm']==str(ppm) and r['file'] in files}
fl=sorted(files)
ref=[A(t) for t in ['leucine','methionine','aspartate','glutamate','phenylalanine','tryptophan']]
med=[np.nanmedian([d[f] for f in fl]) for d in ref]
panel={f:float(np.nanmedian([d[f]/m for d,m in zip(ref,med)])) for f in fl}
tm=np.median([tic[f] for f in fl])
def norm(a,how):
    if how=='raw':return a
    if how=='TIC':return {f:a[f]/tic[f]*tm for f in a}
    if how=='panel':return {f:a[f]/panel[f] for f in a}
res=[];n=0
for t in ['hydroxyglutarate','citrate','lactate','itaconate','lysine']:
    for how in ['raw','TIC','panel']:
        a=norm(A(t),how)
        cells={k:np.log2([a[f] for f in fl if files[f]==k]) for k in set(files.values())}
        tw=V.twoway(cells)
        wz={'D_vs_C(KD in LacZ)':V.welch(cells[(0,0)],cells[(1,0)]),'H_vs_G(KD in Abeta)':V.welch(cells[(0,1)],cells[(1,1)]),
            'G_vs_C(Abeta in ctrl)':V.welch(cells[(0,0)],cells[(0,1)])}
        for name,w in wz.items():
            res.append(dict(metabolite=t,norm=how,test='Welch '+name,log2fc=w['diff'],p=w['p'],qc_pass=qc[t]['assay_sheet_mapping']['gate_pass'] if t in qc else None))
        for k in ['KD_in_LacZ','KD_in_Abeta','KD_main','Abeta_main','interaction']:
            c=tw[k];res.append(dict(metabolite=t,norm=how,test='two-way '+k,log2fc=c['est'],p=c['p'],ci_lo=c['ci95'][0],ci_hi=c['ci95'][1],
               qc_pass=qc[t]['assay_sheet_mapping']['gate_pass'] if t in qc else None,df=tw['_df']))
        res[-1]['cell_means_log2']={f'{k}':float(np.mean(v)) for k,v in cells.items()}
ps=[r['p'] for r in res]
for r,q,h in zip(res,V.bh(ps),V.holm(ps)):r['BH_all']=q;r['Holm_all']=h
# primary family
prim=[r for r in res if r['metabolite'] in('hydroxyglutarate','citrate') and r['norm']=='TIC' and r['test'] in('two-way KD_in_LacZ','two-way KD_in_Abeta','two-way interaction')]
for r,h in zip(prim,V.holm([x['p'] for x in prim])):r['Holm_primary_TIC_family6']=h
json.dump(res,open(os.path.join(out,'v_stats_full.json'),'w'),indent=1,default=float)
with open(os.path.join(out,'v_stats.tsv'),'w') as fh:
    fh.write('metabolite\tnorm\ttest\tlog2FC_or_effect\tp\tCI95_lo\tCI95_hi\tBH_over_all\tHolm_over_all\tHolm_primary6\tQC_gate_pass\n')
    for r in res:
        fh.write(f"{r['metabolite']}\t{r['norm']}\t{r['test']}\t{r['log2fc']:.3f}\t{r['p']:.4g}\t{r.get('ci_lo',float('nan')):.3f}\t{r.get('ci_hi',float('nan')):.3f}\t{r['BH_all']:.4g}\t{r['Holm_all']:.4g}\t{r.get('Holm_primary_TIC_family6','')}\t{r['qc_pass']}\n")
print('n tests',len(res));
json.dump(dict(panel=panel),open(os.path.join(out,'v_panel_factors.json'),'w'),indent=1)
