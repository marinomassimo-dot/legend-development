"""Measure α7 fate perturbations, human disease expression and conditional drug block."""
import argparse
import csv
import gzip
import hashlib
from pathlib import Path
import numpy as np
import openpyxl


def write(path, fields, rows):
    with path.open("w") as stream:
        writer=csv.writer(stream,delimiter="\t",lineterminator="\n")
        writer.writerow(fields.split())
        writer.writerows(rows)


def fate(book, out):
    w=openpyxl.load_workbook(book,read_only=True,data_only=True)
    knock=list(w["Tab4-Fig 5"].values)
    assert knock[0][3:5]==("Sox2+RFP+/RFP+","%NEUN+RFP+/RFP")
    blocks={"shControl":((2,10),(12,14)),"shCHRNA7":((16,24),(26,28)),"shCHRFAM7A":((30,37),(39,41))}
    stats={}
    for condition,bounds in blocks.items():
        for age,(first,last) in zip((21,15),bounds,strict=True):
            for col,marker in ((3,"SOX2"),(4,"NEUN")):
                v=[r[col] for r in knock[first-1:last] if isinstance(r[col],(int,float))]
                stats[condition,age,marker]=np.array(v)
    data=[]
    for (condition,age,marker),v in stats.items():
        wt=stats["shControl",age,marker]
        data.append([condition,age,marker,len(v),len(wt),v.mean(),wt.mean(),v.mean()-wt.mean()])
    write(out/"knockdown.tsv","condition gestational_week endpoint sections control_sections mean_pct control_pct delta_pp",data)
    summary=[]
    for condition in blocks:
        for marker in ("SOX2","NEUN"):
            for weighted in (True,False):
                def metric(group):
                    obs=[stats[group,g,marker] for g in (15,21)]
                    return np.mean([v.mean() for v in obs]) if weighted else np.concatenate(obs).mean()
                q,ctrl=metric(condition),metric("shControl")
                summary.append([condition,marker,"equal_week" if weighted else "equal_section",q,ctrl,q-ctrl])
    write(out/"knockdown_summary.tsv","condition endpoint weight mean_pct control_pct delta_pp",summary)

    organoid=list(w["Tab2- Fig 4"].values)
    assert organoid[0][11:13]==("%SOX2","%NEUN")
    assert organoid[1][9]=="DMSO" and organoid[24][9]=="PNU-282987"
    data=[]
    for k,g in ((11,"SOX2"),(12,"NEUN")):
        values=[]
        for rows in (organoid[1:24],organoid[24:]):
            values.append(np.array([r[k] for r in rows if isinstance(r[k],(int,float))]))
        ctrl,pnu=values
        data.append([g,len(ctrl),len(pnu),ctrl.mean(),pnu.mean(),pnu.mean()-ctrl.mean()])
    write(out/"agonist.tsv","marker control_rows PNU_rows control_pct PNU_pct delta_pp",data)

    # Exploratory human-slice contrast from the six separate Figure 7 groups.
    sheet=list(w["Tab5-Fig 7"].values)
    assert sheet[1][0]=="Quants: %HOPX/Total Dapi"
    assert tuple(sheet[0][1:])==("Untreated","Acetylcholine","Nicotine","TAT","Acetylcholine + TAT","Nicotine + TAT")
    arms={name:[r[i] for r in sheet[1:] if isinstance(r[i],(int,float))]
          for i,name in enumerate(sheet[0]) if i}
    groups=[[name,len(x),np.mean(x)] for name,x in arms.items()]
    write(out/"YAP_groups.tsv","condition rows mean_HOPX_pct",groups)
    effects=[]
    for name in ("Acetylcholine","Nicotine"):
        without=np.mean(arms[name])-np.mean(arms["Untreated"])
        with_inhibitor=np.mean(arms[name+" + TAT"])-np.mean(arms["TAT"])
        effects.append([name,without,with_inhibitor,with_inhibitor-without])
    write(out/"YAP_interaction.tsv","agonist delta_pp_without_inhibitor delta_pp_with_inhibitor difference_of_differences_pp",effects)



def organoids(counts, out):
    radial=["SOX2","PAX6","VIM","HOPX"]
    neurons=["RBFOX3","SNAP25","MAP2","TUBB3"]
    targets=["CHRNA7","CHRFAM7A"]
    keep=set(radial+neurons+targets)
    with gzip.open(counts,"rt") as source:
        rd=csv.reader(source,delimiter="\t")
        label=next(rd)[1:]
        total=np.zeros(len(label))
        raw={}
        for row in rd:
            v=np.array(row[1:],float)
            total+=v
            if row[0] in keep:
                assert row[0] not in raw
                raw[row[0]]=v
    wt=[i for i,n in enumerate(label) if n.startswith("cwt")]
    ko=[i for i,n in enumerate(label) if n.startswith("cko")]
    assert len(wt)==2 and len(ko)==4
    cpm={k:v*1e6/total for k,v in raw.items()}
    if all(g in raw for g in targets):
        cpm["both_genes"]=sum(cpm[g] for g in targets)
    y={k:np.log2(1+v) for k,v in cpm.items()}
    checks=[]
    for panel,genes in (("radial",radial),("neuronal",neurons)):
        ok=[g for g in genes if g in cpm and np.all(cpm[g][wt]>=1)]
        for g in targets:
            if len(ok)>=2 and g in y: y[g+"_minus_"+panel]=y[g]-np.mean([y[h] for h in ok],axis=0)
        checks.append([panel,",".join(genes),",".join(ok)])
    write(out/"panel_coverage.tsv","panel prespecified meets_floor",checks)
    samples=[[g,label[i],raw[g][i],cpm[g][i]] for g in sorted(raw) for i in wt+ko]
    write(out/"human_counts.tsv","gene library Salmon_estimated_count CPM",samples)
    summary=[]
    for g,v in y.items():
        def delta(omit=None):
            return v[[i for i in ko if i!=omit]].mean()-v[[i for i in wt if i!=omit]].mean()
        omits=[delta(i) for i in wt+ko]
        summary.append([g,delta(),min(omits),max(omits),np.all(cpm[g][wt]>=1) if g in cpm else "NA"])
    for g in sorted(keep-set(raw)):summary.append([g,"NA","NA","NA","unmapped"])
    write(out/"human_contrasts.tsv","measure log2_delta omit_low omit_high both_controls_ge1_CPM",summary)


def exposure(out):
    rows=[]
    for c in (.01,.36,.7,1,5,10):
        for context,ic,slopes in [("human_alpha7_central",5,(.5,1,1.5)),("human_alpha7_low_bound",2,(.5,1,1.5)),
                                  ("human_alpha7_high_bound",13,(.5,1,1.5)),("rat_neuronal_alpha7",.34,(.25,.5,.75,1)),
                                  ("rat_neuronal_NMDA",5.1,(1,))]:
            for slope in slopes:
                rows.append([c,context,ic,slope,100/(1+(ic/c)**slope)])
    write(out/"exposure.tsv","free_assay_uM context IC50_uM assumed_Hill block_pct",rows)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    for key in ("workbook","counts","out"):p.add_argument(key,type=Path)
    a=p.parse_args()
    a.out.mkdir(exist_ok=True,parents=True)
    fate(a.workbook,a.out)
    organoids(a.counts,a.out)
    exposure(a.out)
    write(a.out/"sources.tsv","file sha256",[(p.name,hashlib.sha256(p.read_bytes()).hexdigest()) for p in (a.workbook,a.counts)])
