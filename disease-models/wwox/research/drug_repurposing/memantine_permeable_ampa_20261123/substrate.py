"""Contrast relative AMPAR transcripts and TARP availability in existing WWOX datasets."""
import argparse
import hashlib
from pathlib import Path
import sys
import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"ganaxolone_20261123"))
from analyze import assigned_nuclei,load_target,reference,tsv

GENES=["Gria1","Gria2","Gria3","Gria4","Cacng2","Cacng8"]


def measurements(data):
    y={g:np.log2(1+data[g]) for g in GENES}
    y["GluA1_minus_GluA2"]=y["Gria1"]-y["Gria2"]
    y["other_pore_subunits_minus_GluA2"]=np.mean([y[g] for g in ("Gria1","Gria3","Gria4")],axis=0)-y["Gria2"]
    return y


def main(files,out):
    out.mkdir(exist_ok=True,parents=True)
    geo=files/"geo"
    hip,=(geo/"GSE158681").glob("*TPM_Table.txt.gz")
    cortex,=(geo/"GSE158682").glob("*TPM_Table.txt.gz")
    organoid,=(geo/"GSE156243").glob("*count_table.txt.gz")
    tx,_=reference(files)
    models=[("neuronal_cortex",cortex,"CRTX_S_Ctrl_","CRTX_S_KO_"),
            ("neuronal_hippocampus",hip,"S_Ctrl_","S_KO_"),
            ("global_hippocampus",hip,"WT_","KO_"),
            ("human_organoid",organoid,"cwt","cko")]
    obs,stats=[],[]
    for name,p,wt_prefix,ko_prefix in models:
        human=p==organoid
        genes={g.upper() if human else g:g for g in GENES}
        labels,raw=load_target(p,genes,None if human else tx)
        data={genes[g]:v for g,v in raw.items()}
        assert len(data)==len(GENES)
        wt=[i for i,n in enumerate(labels) if n.startswith(wt_prefix)]
        ko=[i for i,n in enumerate(labels) if n.startswith(ko_prefix)]
        assert min(len(wt),len(ko))>=2
        for g,v in data.items():
            obs.extend([[name,labels[i],"KO" if i in ko else "control",g,"CPM" if human else "TPM",v[i]] for i in wt+ko])
        for g,v in measurements(data).items():
            def delta(omit=None):
                return v[[i for i in ko if i!=omit]].mean()-v[[i for i in wt if i!=omit]].mean()
            omit=[delta(i) for i in wt+ko]
            stats.append([name,g,len(wt),len(ko),delta(),min(omit),max(omit),min(data[g][wt+ko]) if g in data else "NA"])
    tsv(out/"bulk.tsv","model gene_or_index n_control n_mutant log_delta omit_min omit_max min_abundance_all_libraries".split(),stats)
    tsv(out/"observations.tsv","model sample group gene linear_units abundance".split(),obs)
    rows=[]
    for arm,cell,depth,values in assigned_nuclei(files,[],[],GENES):
        if cell not in ("exc","inh"): continue
        data={g:1e6*values[g].sum()/depth.sum() for g in GENES}
        y=measurements(data)
        for g,v in y.items():
            rows.append([arm,cell,len(depth),g,int(values[g].sum()) if g in data else "NA",data.get(g,"NA"),v])
    tsv(out/"nuclei.tsv","pool assigned_class nuclei measure gene_molecules pooled_CPM log_value".split(),rows)
    paths=[hip,cortex,organoid,*sorted((files/"reference_ensembl_r92").glob("*.fa.gz")),
           *sorted((geo/"GSE158684").glob("*features*")),*sorted((geo/"GSE158684").glob("*matrix*"))]
    tsv(out/"inputs.tsv",["input","sha256"],[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in paths])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.files,a.out)
