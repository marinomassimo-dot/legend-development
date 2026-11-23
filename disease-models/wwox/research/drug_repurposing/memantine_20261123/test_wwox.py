"""Apply the frozen mouse NMDA-minus-silencing contrast to untreated brain tissue."""
import argparse
from collections import defaultdict
import csv
import gzip
import json
from pathlib import Path
import re

import numpy as np

from learn_signature import write


def references(fasta, hgnc, gene_info, wanted):
    transcripts, symbols, mgi = {}, defaultdict(set), defaultdict(set)
    with gzip.open(fasta, "rt") as f:
        for header in f:
            if not header.startswith(">"):
                continue
            gid = re.search(r" gene:(\w+)",header)[1]
            sym = re.search(r" gene_symbol:(\S+)",header)
            if sym:
                symbols[sym[1]].add(gid)
            if gid in wanted:
                tx = header[1:].split(".",1)[0]
                transcripts[tx] = gid
                mouse = re.search(r"Acc:(MGI:\d+)",header)
                if mouse:
                    mgi[gid].add(mouse[1])
    # Sequence descriptions often give a protein accession. Resolve missing mouse
    # identifiers from NCBI Gene dbXrefs using the same Ensembl gene ID.
    with gzip.open(gene_info, "rt") as source:
        for row in csv.DictReader(source, delimiter="\t"):
            xrefs = row["dbXrefs"].split("|")
            ensembl_ids = {x.removeprefix("Ensembl:") for x in xrefs if x.startswith("Ensembl:")}
            for gene in ensembl_ids & wanted:
                mgi[gene].update(x.removeprefix("MGI:") for x in xrefs if x.startswith("MGI:MGI:"))
    approved = json.loads(hgnc.read_text())["response"]["docs"]
    from_mgi = defaultdict(set)
    for record in approved:
        for mid in record.get("mgd_id",[]):
            from_mgi[mid].add(record["symbol"])
    mouse, human = {}, {}
    for symbol, gids in symbols.items():
        if len(gids)==1 and gids <= wanted:
            gid, = gids
            mouse[gid] = symbol
    for gid, ids in mgi.items():
        matched = set().union(*(from_mgi[mid] for mid in ids))
        if len(ids)==1 and len(matched)==1:
            human[gid], = matched
    # Exclude two targets that would receive the same human symbol.
    human = {gid:s for gid,s in human.items() if list(human.values()).count(s)==1}
    return transcripts, mouse, human


def load(path, lookup, transcript=False):
    with gzip.open(path,"rt") as f:
        rows = csv.reader(f, delimiter="\t")
        offset = 3 if transcript else 1
        samples = next(rows)[offset:]
        totals = np.zeros(len(samples))
        accum = {}
        for row in rows:
            key = row[0].split(".",1)[0] if transcript else row[0]
            if not transcript or key in lookup:
                v = np.asarray(row[offset:],float)
                if not transcript:
                    totals += v
                if key in lookup:
                    g = lookup[key]
                    accum[g] = accum.get(g,0)+v
    if not transcript:
        accum={g: x*1e6/totals for g,x in accum.items()}
    return samples,{g:np.log2(1+x) for g,x in accum.items()}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for key in ["files","gene_info","pairs","out"]:
        parser.add_argument(key,type=Path)
    args=parser.parse_args()
    args.out.mkdir(exist_ok=True,parents=True)
    with args.pairs.open() as f:
        by_pair=defaultdict(dict)
        for r in csv.DictReader(f, delimiter="\t"):
            by_pair[r["pair"]][r["arm"]]=r["ensembl"]
    markers = {"Inhba":"ENSMUSG00000041324", "Bdnf":"ENSMUSG00000048482", "Homer1":"ENSMUSG00000007617"}
    marker_rows = []
    wanted={x for p in by_pair.values() for x in p.values()} | set(markers.values())
    tx,mouse,human=references(args.files/"reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz",
                              args.files/"geo/GSE156243/hgnc_complete_set_20261022.json",args.gene_info,wanted)
    geo=args.files/"geo"
    systems=[
        ("hippocampus", next((geo/"GSE158681").glob("*TPM_Table.txt.gz")),tx,True,"S_KO_","S_Ctrl_"),
        ("cortex", next((geo/"GSE158682").glob("*TPM_Table.txt.gz")),tx,True,"CRTX_S_KO_","CRTX_S_Ctrl_"),
        ("kainate_day14", args.files/"deepening_downloads/gse319769/counts_fixed.tsv.gz",
         {s:g for g,s in mouse.items()},False,"iaka14_","iasl14_"),
        ("human_organoid", next((geo/"GSE156243").glob("*count_table.txt.gz")),
         {s:g for g,s in human.items()},False,"cko","cwt"),
    ]
    outputs, pairs, libraries = [],[],[]
    for name,path,lookup,is_tx,case,ctrl in systems:
        samples,expression=load(path,lookup,is_tx)
        cases=[i for i,s in enumerate(samples) if s.startswith(case)]
        controls=[i for i,s in enumerate(samples) if s.startswith(ctrl)]
        def effect(v,omit=None):
            return v[[i for i in cases if i!=omit]].mean()-v[[i for i in controls if i!=omit]].mean()
        for symbol,gene in markers.items():
            if gene in expression:
                v = expression[gene]
                marker_rows.append([name,symbol,effect(v),min(effect(v,i) for i in cases+controls),max(effect(v,i) for i in cases+controls)])
            else:
                marker_rows.append([name,symbol,"NA","NA","NA"])
        hs,cs=[],[]
        for num,p in by_pair.items():
            h,c = p["hit"],p["control"]
            ok=h in expression and c in expression
            info=[name,num,h,mouse.get(h,"NA"),human.get(h,"NA"),c,mouse.get(c,"NA"),human.get(c,"NA")]
            if ok:
                hv,cv=expression[h],expression[c]
                hs.append(hv)
                cs.append(cv)
                pairs.append([*info,"included",effect(hv),effect(cv),effect(hv-cv)])
            else:
                pairs.append([*info,"missing_"+("_".join(k for k,v in p.items() if v not in expression)), "NA","NA","NA"])
        h,c=np.mean(hs,axis=0),np.mean(cs,axis=0)
        s=h-c
        loo=[effect(s,i) for i in cases+controls]
        pair_effect=np.array([effect(a-b) for a,b in zip(hs,cs)])
        assert np.isclose(effect(s),pair_effect.mean())
        jack=(pair_effect.sum()-pair_effect)/(len(pair_effect)-1)
        outputs.append([name,len(cases),len(controls),len(hs),effect(h),effect(c),effect(s),
                        min(loo),max(loo),jack.min(),jack.max(),int(np.sum(pair_effect<0))])
        for i in cases+controls:
            libraries.append([name,samples[i],"case" if i in cases else "control",h[i],c[i],s[i]])
    write(args.out/"named_markers.tsv","model gene delta loo_min loo_max",marker_rows)
    write(args.out/"tissue.tsv","model case_n control_n valid_pairs hit_delta control_delta difference loo_library_min loo_library_max loo_pair_min loo_pair_max negative_pairs",outputs)
    write(args.out/"tissue_pairs.tsv","model pair hit_ensembl hit_mouse hit_human ctrl_ensembl ctrl_mouse ctrl_human coverage hit_delta ctrl_delta difference",pairs)
    write(args.out/"tissue_libraries.tsv","model library group hit control difference",libraries)


if __name__=="__main__":
    main()
