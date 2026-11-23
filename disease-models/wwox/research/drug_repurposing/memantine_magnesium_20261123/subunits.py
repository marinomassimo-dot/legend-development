"""Measure GluN2B/D RNA substrate, without imputing native receptor assembly."""
import argparse
import csv
import gzip
import hashlib
from itertools import combinations
from pathlib import Path
import sys
import numpy as np

ROOT = Path(__file__).parent
sys.path.insert(0,str(ROOT.parent/"ganaxolone_20261123"))
from analyze import assigned_nuclei, reference, load_target, tsv

MODELS = [
    ("neuronal_cortex","GSE158682","CRTX_S_Ctrl_","CRTX_S_KO_"),
    ("neuronal_hippocampus","GSE158681","S_Ctrl_","S_KO_"),
    ("neural_hippocampus","GSE158681","N_Ctrl_","N_KO_"),
    ("global_hippocampus","GSE158681","WT_","KO_"),
    ("human_organoid","GSE156243","cwt","cko")]
GENES=["Grin1","Grin2a","Grin2b","Grin2c","Grin2d"]

def probability_missing(total, molecules, draw):
    if molecules > total - draw:
        return 0.0
    return float(np.prod([(total-draw-i)/(total-i) for i in range(molecules)]))

def detection_after_thinning(total, counts, draw):
    result = 1.0
    for n in range(1,len(counts)+1):
        for subset in combinations(counts,n):
            result += (-1)**n * probability_missing(total,sum(subset),draw)
    assert -1e-8 <= result <= 1+1e-8
    return float(np.clip(result,0,1))

def adult_hippocampus(src):
    sys.path.insert(0,str(ROOT.parent/"perampanel_kainate_20261123"))
    from p47t_analysis import contrast
    assert hashlib.sha256(src.read_bytes()).hexdigest()=="d654f6bdd2a4ac5b3e24741f16962503a711575c72aa92a2c729a7a0cf04c18c"
    with gzip.open(src,"rt") as source:
        reader=csv.reader(source,delimiter="\t")
        labels=next(reader)[2:]
        cols=[i for i,n in enumerate(labels) if n.startswith("HPC_")]
        names=[labels[i] for i in cols]
        totals=np.zeros(len(cols))
        counts={g:np.zeros(len(cols)) for g in GENES}
        for _,gene,*values in reader:
            vals=np.array([int(values[i]) for i in cols])
            totals+=vals
            if gene in counts: counts[gene]+=vals
    groups=[(n.split("_")[1].split("/")[0],n.split("_")[2][0]) for n in names]
    assert len(set(names))==10
    logged={g:np.log2(1+v*1e6/totals) for g,v in counts.items()}
    logged["Grin2d_minus_Grin2b"]=logged["Grin2d"]-logged["Grin2b"]
    tsv(ROOT/"adult.tsv","measure sex_balanced_delta female_delta male_delta omit_min omit_max".split(),
        [(g,*contrast(v,groups)) for g,v in logged.items()])

def main(files):
    adult = files/"deepening_downloads/gse215425/GSE215425_processed_data.csv.gz"
    adult_hippocampus(adult)
    sources = {adult,next((files/"reference_ensembl_r92").glob("*.fa.gz"))}
    gene_map,_ = reference(files)
    bulk, libraries, nuclei, thinning = [],[],[],[]
    for name,acc,wt,ko in MODELS:
        human = name=="human_organoid"
        src = next((files/"geo"/acc).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz"))
        sources.add(src)
        wanted = {g.upper() if human else g:g for g in GENES}
        names,raw = load_target(src,wanted,None if human else gene_map)
        data = {wanted[g]:np.log2(1+v) for g,v in raw.items()}
        data["Grin2d_minus_Grin2b"] = data["Grin2d"]-data["Grin2b"]
        w = [i for i,n in enumerate(names) if n.startswith(wt)]
        k = [i for i,n in enumerate(names) if n.startswith(ko)]
        assert min(len(w),len(k))>=2
        for gene,y in data.items():
            def change(omit):
                return np.mean([y[i] for i in k if i!=omit])-np.mean([y[i] for i in w if i!=omit])
            omitted = [change(i) for i in w+k]
            bulk.append((name,gene,len(w),len(k),change(None),min(omitted),max(omitted)))
            libraries.extend((name,names[i],"WT" if i in w else "KO",gene,y[i]) for i in w+k)
    for arm,cell,depth,values in assigned_nuclei(files,[],[],GENES):
        g1,b,d=[values[g] for g in ("Grin1","Grin2b","Grin2d")]
        if cell in ("exc","inh"):
            for draw in (500,1000,3000):
                eligible = depth>=draw
                expected_d, expected_joint = [],[]
                for total, counts in zip(depth[eligible], zip(g1[eligible],b[eligible],d[eligible])):
                    counts = tuple(map(int,counts))
                    expected_d.append(detection_after_thinning(int(total),[counts[-1]],draw))
                    expected_joint.append(detection_after_thinning(int(total),counts,draw))
                thinning.append((arm,cell,draw,len(expected_d),np.mean(expected_d),np.mean(expected_joint)))
        # Common-depth bin is a diagnostic sensitivity, with no sample-level inference.
        for label, ix in [("all",depth>0),("1000_to_3000",(depth>=1000)&(depth<=3000))]:
            if not np.any(ix): continue
            g1p,bp,dp=(g[ix]>0 for g in (g1,b,d))
            nuclei.append((arm,cell,label,int(ix.sum()),int(depth[ix].sum()),int(b[ix].sum()),int(d[ix].sum()),
                          int(g1p.sum()),int(bp.sum()),int(dp.sum()),int((bp&dp).sum()),int((g1p&bp&dp).sum()),
                          int(dp.sum())/len(dp),int((g1p&bp&dp).sum())/len(dp)))
    for arm in ("ctrl","ko"):
        for suffix in ("matrix.mtx.gz","features.tsv.gz"):
            sources.add(files/"geo/GSE158684"/f"GSE158684_{arm}_filtered_{suffix}")
    tsv(ROOT/"bulk.tsv","model gene n_WT n_KO delta_log2 LOO_min LOO_max".split(),bulk)
    tsv(ROOT/"libraries.tsv","model sample group measure log2_value".split(),libraries)
    tsv(ROOT/"nuclei.tsv","pool class depth_range nuclei UMI Grin2b Grin2d Grin1_pos B_pos D_pos BD_pos N1BD_pos D_fraction N1BD_fraction".split(),nuclei)
    tsv(ROOT/"thinning.tsv","pool class reads_per_nucleus eligible_nuclei expected_D_detection_fraction expected_N1BD_detection_fraction".split(),thinning)
    tsv(ROOT/"inputs.tsv",["input","sha256"],[(src.name,hashlib.sha256(src.read_bytes()).hexdigest()) for src in sorted(sources)])

if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",type=Path)
    main(p.parse_args().files)
