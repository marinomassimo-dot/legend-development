"""Measure OPC GABA-A transcription and relative fast-spiking markers in Wwox models."""
import argparse
import gzip
import hashlib
from pathlib import Path
import sys
import numpy as np
import xlrd
from geometry import write

sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"ganaxolone_20261123"))
from analyze import assigned_nuclei, reference, load_target

ALPHA=[f"Gabra{i}" for i in range(1,7)]
BETA=[f"Gabrb{i}" for i in range(1,4)]
PARTNERS=["Gabrg2","Gabrd"]
OPC=["Pdgfra","Cspg4","Cspg5","Pcdh15"]
NEURON=["Slc17a7","Gad1","Gad2","Snap25","Rbfox3"]
FAST=["Pvalb","Kcnc1","Kcnc2"]
COMPARATORS=["Gad1","Gad2","Lhx6"]


def nuclei(files,out):
    summaries,subunits=[],[]
    wanted=set(ALPHA+BETA+PARTNERS+OPC+NEURON)
    for pool,cell,depth,genes in assigned_nuclei(files,[],[],wanted):
        if cell not in ("OPC","COP","inh","exc"):continue
        zeros=np.zeros(len(depth),dtype=int)
        def x(g):return genes.get(g,zeros)
        def number_detected(panel):return sum((x(g)>0).astype(int) for g in panel)
        rules={"assigned":np.ones(len(depth),dtype=bool)}
        if cell=="OPC":
            rules["OPC_markers_ge2"]=(number_detected(OPC)>=2)
            rules["OPC_markers_ge2_neuronal_undetected"]=(number_detected(OPC)>=2)&(number_detected(NEURON)==0)
        alpha=number_detected(ALPHA)>0
        beta=number_detected(BETA)>0
        for rule,sel in rules.items():
            n=int(sel.sum())
            for g in ALPHA+BETA+PARTNERS:
                y=x(g)[sel]
                subunits.append([pool,cell,rule,g,g in genes,n,int(y.sum()),int((y>0).sum()),
                                 1e6*y.sum()/depth[sel].sum() if n else "NA"])
            for p in PARTNERS:
                val=x(p)
                summaries.append([pool,cell,rule,p,n,int(depth[sel].sum()),int(val[sel].sum()),
                                  int(((val>0)&sel).sum()),int((alpha&beta&(val>0)&sel).sum()),
                                  int((alpha&beta&(val>0)&sel&(number_detected(NEURON)>0)).sum())])
    write(out/"lineage.tsv","pool lineage filter partner nuclei UMIs partner_UMIs partner_detected alpha_beta_partner_detected triple_with_neuronal_marker",summaries)
    write(out/"subunits.tsv","pool lineage filter gene mapped nuclei gene_UMIs n_detected CPM",subunits)


def purified(folder,out):
    records=[]
    for group in ["OPC","NFO","MO","Neuron"]:
        files=sorted(folder.glob(f"*_{group}[12].xls.gz"))
        assert len(files)==2
        for p in files:
            table=xlrd.open_workbook(file_contents=gzip.open(p).read()).sheet_by_index(0)
            assert table.cell_value(0,0)=="gene.symbol"
            key=table.cell_value(0,1)
            for gene in ALPHA+BETA+PARTNERS:
                vals=[float(table.cell_value(i,1)) for i in range(1,table.nrows) if table.cell_value(i,0)==gene]
                records.append([group,p.name,gene,key,vals[0] if len(vals)==1 else "NA"])
    write(out/"purified.tsv","cell source gene column expression",records)


def bulk(files,out):
    tx,_=reference(files)
    stats=[]
    genes=FAST+COMPARATORS
    for name,acc,case,ctrl in [("cortex","GSE158682","CRTX_S_KO_","CRTX_S_Ctrl_"),
                              ("hippocampus","GSE158681","S_KO_","S_Ctrl_")]:
        path,=(files/"geo"/acc).glob("*TPM_Table.txt.gz")
        samples,values=load_target(path,set(genes),tx)
        assert all(g in values for g in genes)
        y={g:np.log2(1+values[g]) for g in genes}
        y["fast_minus_comparators"]=np.mean([y[g] for g in FAST],axis=0)-np.mean([y[g] for g in COMPARATORS],axis=0)
        ko=[i for i,t in enumerate(samples) if t.startswith(case)]
        wt=[i for i,t in enumerate(samples) if t.startswith(ctrl)]
        for g,v in y.items():
            def effect(j=None):
                return v[[i for i in ko if i!=j]].mean()-v[[i for i in wt if i!=j]].mean()
            loo=[effect(i) for i in wt+ko]
            stats.append([name,g,len(ko),len(wt),values[g][wt].mean() if g in values else "NA",
                          values[g][ko].mean() if g in values else "NA",effect(),min(loo),max(loo)])
    write(out/"fast_spiking.tsv","model gene KO_n control_n control_mean_TPM KO_mean_TPM delta omit_min omit_max",stats)


def main(files,geometry,out):
    nuclei(files,out)
    purified(files/"geo/GSE52564_raw",out)
    bulk(files,out)
    inputs=[geometry,*sorted((files/"geo/GSE158684").glob("*features*")),*sorted((files/"geo/GSE158684").glob("*matrix*")),
            *sorted((files/"reference_ensembl_r92").glob("*.fa.gz"))]
    for acc in ("GSE158681","GSE158682"):inputs.extend((files/"geo"/acc).glob("*TPM_Table.txt.gz"))
    for name in ("OPC","NFO","MO","Neuron"):inputs.extend(sorted((files/"geo/GSE52564_raw").glob(f"*_{name}[12].xls.gz")))
    inputs.extend([files/"geo/E-MTAB-6798_mouse_timecourse/Mouse.RPKM.txt",
                   files/"deepening_downloads/gse319769/counts_fixed.tsv.gz"])
    write(out/"inputs.tsv","input sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in inputs])


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("files","geometry","out"):p.add_argument(key,type=Path)
    a=p.parse_args()
    main(a.files,a.geometry,a.out)
