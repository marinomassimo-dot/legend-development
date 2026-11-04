"""Verifier stage 4: diagnostics. Usage: python3 -I v_diag.py <out_dir> <npz_dir> <supp_tables.xlsx>
(a) mapping validation against metabolites with strong published effects (public Supplementary Table 4 of the paper, used ONLY as
    an external check of the letter->group map, never to tune integration),
(b) itaconate-vs-2-HG fragment test, (c) blanks/carryover, (d) TIC and reference-panel by group, (e) leave-one-out of the 2-HG
interaction, (f) lactate window sensitivity (reported in full; the 0.7 gate is not changed), (g) pooled-QC CV."""
import sys,os,csv,json,collections
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vstats as V, xlsx_dump, v_integrate as I
out,npz,xl=sys.argv[1:4]
rows=list(csv.DictReader(open(os.path.join(out,'v_areas_long.tsv')),delimiter='\t'))
CELL={('RNAi Control','LacZ'):(0,0),('Wwox RNAi','LacZ'):(1,0),('RNAi Control','AB42'):(0,1),('Wwox RNAi','AB42'):(1,1)}
files={r['file']:CELL[(r['group_wwox'],r['group_amyloid'])] for r in rows if r['assay_name'].endswith('_KDExp')}
tic={r['file']:float(r['tic']) for r in rows}
def A(t,ppm=5): return {r['file']:float(r['area']) for r in rows if r['target']==t and r['ppm']==str(ppm)}
fl=sorted(files);tm=np.median([tic[f] for f in fl])
def cells_of(a,norm=True):
    return {k:np.log2([a[f]/tic[f]*tm if norm else a[f] for f in fl if files[f]==k]) for k in set(files.values())}
res={}
# (a) mapping validation
wb=xlsx_dump.load(xl)['Supplementary Table 4']
pub={}
for r in wb[4:]:
    v=list(r.values())
    if len(v)>18 and v[4] in('L-Lysine','L-Lysine (negative)','2-Hydroxyglutarate','L-Lactate','Itaconate'):
        pub[(v[4],round(float(v[1]),3))]=dict(KD_main=float(v[9]),Ab_main=float(v[13]),inter_p=float(v[15]),KD_in_Ab=float(v[17]),KD_in_LacZ=float(v[18]))
for r in wb[4:]:
    v=list(r.values())
    if len(v)>5 and v[3] and v[1] in('193.0354','193.03539999999999') : pass
mp={}
for t,key in [('lysine',('L-Lysine (negative)','145.0983')),('hydroxyglutarate',('2-Hydroxyglutarate','147.0299')),('lactate',('L-Lactate','89.0245')),('itaconate',('Itaconate','129.0194'))]:
    tw=V.twoway(cells_of(A(t)))
    p=[v for k,v in pub.items() if k[0]==key[0] and k[1]==round(float(key[1]),3)]
    mp[t]=dict(own={k:round(tw[k]['est'],3) for k in('KD_main','Abeta_main','KD_in_Abeta','KD_in_LacZ','interaction')},own_p={k:tw[k]['p'] for k in('KD_main','Abeta_main','interaction')},published=p[0] if p else None)
res['mapping_validation_vs_published_Table4']=mp
# (b) itaconate vs 2-HG
ita=A('itaconate');hg=A('hydroxyglutarate')
ratio={f:ita[f]/hg[f] for f in fl}
byg=collections.defaultdict(list)
for f in fl: byg[files[f]].append(ratio[f])
res['itaconate750_over_2HG']={str(k):[float(np.mean(v)),float(np.std(v,ddof=1))] for k,v in byg.items()}
res['itaconate750_vs_2HG_log_pearson']=float(np.corrcoef(np.log([ita[f] for f in fl]),np.log([hg[f] for f in fl]))[0,1])
allf=[f for f in ita if f.startswith(('pooled',))]
res['pooled_ratio_ita750_over_2HG']=[float(np.mean([ita[f]/hg[f] for f in allf])),float(np.std([ita[f]/hg[f] for f in allf],ddof=1))]
# integrate the deposit-anchor (771 s) region directly: +/-6 s around 771 s with linear baseline from 764/778, relative to 2-HG area
a771={}
for f in ita:
    d=np.load(os.path.join(npz,f+'.npz'));rt=d['rt'];y=d['itaconate_5']
    a771[f]=I.area(rt,y,771.0,6.0,6.0)
res['itaconate_771s_region']={'note':'window 765-777 s, linear baseline; this is a tail/plateau, not a resolved peak',
   'ratio_to_2HG_by_group':{str(k):float(np.mean([a771[f]/hg[f] for f in fl if files[f]==k])) for k in set(files.values())},
   'pooled_mean_area':float(np.mean([a771[f] for f in a771 if f.startswith('pooled')])),'blank_mean_area':float(np.mean([a771[f] for f in a771 if f.startswith('matrix')]))}
# (c) blanks
bl={}
for t in['lactate','hydroxyglutarate','citrate','itaconate']:
    a=A(t);bl[t]={'blank_areas_in_run_order_1_to_6':[a[f'matrix_blank_{i}'] for i in range(1,7)],'median_sample_area_KD':float(np.median([a[f] for f in fl])),
      'blank_mean_over_median_sample':float(np.mean([a[f'matrix_blank_{i}'] for i in range(1,7)])/np.median([a[f] for f in fl])),
      'min_sample_over_max_blank':float(min(a[f] for f in fl)/max(a[f'matrix_blank_{i}'] for i in range(1,7)))}
res['blanks']=bl
# (d) TIC and panel by group
pf=json.load(open(os.path.join(out,'v_panel_factors.json')))['panel']
res['TIC_by_group_rel_median']={str(k):float(np.mean([tic[f]/tm for f in fl if files[f]==k])) for k in set(files.values())}
res['panel_factor_by_group']={str(k):float(np.mean([pf[f] for f in fl if files[f]==k])) for k in set(files.values())}
res['TIC_pooled_batch1_mean_over_median_sample']=float(np.mean([tic[f] for f in tic if f in('pooled_7','pooled_8','pooled_9','pooled_10','pooled_11','pooled_12')])/tm)
res['TIC_pooled_batch2_mean_over_median_sample']=float(np.mean([tic[f] for f in tic if f.startswith('pooled_2_')])/tm)
# (e) LOO of 2-HG interaction (TIC-normalised and raw)
loo={}
for nm,norm in(('TIC',True),('raw',False)):
    a=A('hydroxyglutarate');out_l=[]
    for drop in fl:
        c={}
        for k in set(files.values()):
            c[k]=np.log2([a[f]/tic[f]*tm if norm else a[f] for f in fl if files[f]==k and f!=drop])
        tw=V.twoway(c);out_l.append((drop,tw['interaction']['est'],tw['interaction']['p']))
    loo[nm]={'est_range':[min(x[1] for x in out_l),max(x[1] for x in out_l)],'p_range':[min(x[2] for x in out_l),max(x[2] for x in out_l)],'worst_p_dropped':max(out_l,key=lambda x:x[2])[0],'n_p_lt_0.05':sum(x[2]<0.05 for x in out_l),'n':len(out_l)}
res['LOO_2HG_interaction']=loo
# (f) gate sensitivity to integration window, all four features (every variant is reported; the 0.7 gate is not changed)
file2assay,grp,dep=I.load_isa(sys.argv[4])
order=['Pool1_1','Pool1_2','Pool1_3','Pool1_4','Pool1_5','Pool1_6','Pool2_1','Pool2_2','Pool2_3','Pool2_4','Pool2_5','Pool2_6']
inv={v:k for k,v in file2assay.items()}
sens={}
for t,(nm,mz,apex0) in {'lactate':('L-Lactate','89.0245',563.0),'hydroxyglutarate':('2-Hydroxyglutarate','147.0299',750.0),'citrate':('Citrate','191.0199',841.0),'itaconate':('Itaconate','129.0194',750.0)}.items():
    dv=dep[(nm,mz)];vs=[]
    for ppm in(5,10):
        for halfw in(8,12,15,20,30):
            for recentre in(True,False):
                own=[]
                for p in order:
                    d=np.load(os.path.join(npz,inv[p]+'.npz'));rt=d['rt'];y=d[f'{t}_{ppm}']
                    apex=apex0
                    if recentre:
                        m=(rt>=apex-8)&(rt<=apex+8);apex=float(rt[m][np.argmax(I.smooth(y)[m])])
                    own.append(I.area(rt,y,apex,halfw,halfw))
                vs.append(dict(ppm=ppm,half_width_s=halfw,recentre=recentre,rho12=V.spearman(own,[dv[p] for p in order])))
    sens[t]=dict(variants=vs,n=len(vs),n_pass=sum(v['rho12']>=0.7 for v in vs),min=min(v['rho12'] for v in vs),max=max(v['rho12'] for v in vs),
        fixed_window_15s_no_recentre_5ppm=[v['rho12'] for v in vs if v['ppm']==5 and v['half_width_s']==15 and not v['recentre']][0])
res['gate_window_sensitivity']=sens
# (g) pooled CV within batch
cv={}
b1=['pooled_7','pooled_8','pooled_9','pooled_10','pooled_11','pooled_12'];b2=[f'pooled_2_0{i}' for i in range(4,10)]
for t in['lactate','hydroxyglutarate','citrate','itaconate','lysine']:
    a=A(t);cv[t]={'batch1_CV%':float(100*np.std([a[f] for f in b1],ddof=1)/np.mean([a[f] for f in b1])),'batch2_CV%':float(100*np.std([a[f] for f in b2],ddof=1)/np.mean([a[f] for f in b2])),
       'batch2_over_batch1':float(np.mean([a[f] for f in b2])/np.mean([a[f] for f in b1]))}
res['pooled_QC_CV']=cv
json.dump(res,open(os.path.join(out,'v_diagnostics.json'),'w'),indent=1,default=float)
print(json.dumps(res,indent=1,default=float))
