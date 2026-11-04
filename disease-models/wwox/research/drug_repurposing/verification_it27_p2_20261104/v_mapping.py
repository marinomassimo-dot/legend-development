"""Verifier: adjudicate the two competing file->sample links in the assay sheet (negative-mode assay '-1').
 Link A: MS Assay Name column (e.g. C1_KDExp for raw C1.raw)  -> sample sheet s_ -> factor values.
 Link B: Sample Name column of the SAME assay row (alphabetically sorted list, offset against the raw file) -> sample sheet.
Test: which link reproduces the published effects (Supplementary Table 4: L-lysine strongly down with Wwox RNAi; L-lactate interaction; 2-HG up with Abeta42)?
Usage: python3 -I v_mapping.py <out_dir> <isa_dir>"""
import sys,os,csv,json
import numpy as np
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import vstats as V
out,isa=sys.argv[1:3]
a=list(csv.reader(open(os.path.join(isa,'a_MTBLS12344_LC-MS_alternating_hilic_metabolite_profiling-1.txt')),delimiter='\t'));h=a[0]
iS,iA,iD=h.index('Sample Name'),h.index('MS Assay Name'),h.index('Derived Spectral Data File')
s=list(csv.reader(open(os.path.join(isa,'s_MTBLS12344.txt')),delimiter='\t'));sh=s[0]
g={r[sh.index('Sample Name')]:(r[sh.index('Factor Value[Wwox manipulation]')],r[sh.index('Factor Value[Amyloid]')]) for r in s[1:]}
CELL={('RNAi Control','LacZ'):(0,0),('Wwox RNAi','LacZ'):(1,0),('RNAi Control','AB42'):(0,1),('Wwox RNAi','AB42'):(1,1)}
rows=[]
for r in a[1:]:
    f=os.path.basename(r[iD]).replace('.mzXML','')
    rows.append((f,r[iA],r[iS]))

print('rows',len(rows),'MS Assay Name letter code == raw file name in',sum(1 for f,an,sn in rows if an.split('_')[0]==f or an==f),'rows; Sample Name == MS Assay Name in',sum(1 for f,an,sn in rows if an==sn),'rows')
ar=list(csv.DictReader(open(os.path.join(out,'v_areas_long.tsv')),delimiter='\t'))
tic={r['file']:float(r['tic']) for r in ar};tm=np.median(list(tic.values()))
def A(t):return {r['file']:float(r['area']) for r in ar if r['target']==t and r['ppm']=='5'}
res={}
for link,idx in (('A_MS_Assay_Name',1),('B_Sample_Name_column',2)):
    f2g={}
    for f,an,sn in rows:
        key=(an,sn)[idx-1]
        if key in g and key.endswith('_KDExp'): f2g[f]=CELL[g[key]]
    out_t={}
    for t in('lysine','hydroxyglutarate','lactate','glucuronate','orotate'):
        a_=A(t);cells={}
        for f,c in f2g.items():
            if f not in a_: continue
            cells.setdefault(c,[]).append(np.log2(a_[f]/tic[f]*tm))
        cells={k:np.array(v) for k,v in cells.items()}
        if any(len(v)<2 for v in cells.values()) or len(cells)<4:out_t[t]='cells incomplete: '+str({str(k):len(v) for k,v in cells.items()});continue
        tw=V.twoway(cells);out_t[t]={k:(round(tw[k]['est'],3),float('%.3g'%tw[k]['p'])) for k in('KD_main','Abeta_main','interaction')}
        out_t[t]['n_per_cell']={str(k):len(v) for k,v in cells.items()}
    res[link]=out_t
json.dump(res,open(os.path.join(out,'v_mapping_adjudication.json'),'w'),indent=1)
print(json.dumps(res,indent=1))
