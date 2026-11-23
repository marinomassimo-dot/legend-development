"""Reanalyse mouse Grik1 splice-cassette TPMs and kainate partner availability."""
import argparse
import csv
import gzip
import hashlib
import itertools
from pathlib import Path
import sys

import numpy as np
sys.path.insert(0,str(Path(__file__).resolve().parents[1] / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference, tsv

GENES = ["Grik1","Grik2","Grik4","Grik5","Neto1","Neto2"]
MODELS = [
    ("neuronal_cortex","GSE158682","CRTX_S_Ctrl_","CRTX_S_KO_"),
    ("neuronal_hippocampus","GSE158681","S_Ctrl_","S_KO_"),
    ("neural_hippocampus","GSE158681","N_Ctrl_","N_KO_"),
    ("global_hippocampus","GSE158681","WT_","KO_"),
    ("human_organoid","GSE156243","cwt","cko"),
]
CODE = dict(zip(itertools.product("TCAG", repeat=3),
                "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"))
LEFT = "KSRKNNDIEQ"
CASSETTE = "KGKSSRLRFYFRNKVRFHGSKTESLGVEK"
RIGHT = "CLSFNAIMEELG"


def isoforms(fasta):
    with gzip.open(fasta, "rt") as source:
        for is_header, lines in itertools.groupby(source, lambda line: line.startswith(">")):
            if is_header:
                header = next(lines)
            elif "gene_symbol:Grik1 " in header:
                seq = "".join(line.strip() for line in lines)
                frames = ["".join(CODE.get(tuple(seq[i:i+3]), "X")
                                  for i in range(f,len(seq)-2,3)) for f in range(3)]
                labels = [typ for typ, motif in (("insert", LEFT+CASSETTE+RIGHT),
                                                 ("skip", LEFT+RIGHT))
                          if any(motif in protein for protein in frames)]
                assert len(labels) <= 1
                yield header[1:].split()[0], labels[0] if labels else "other"


def main(files, out):
    out.mkdir(exist_ok=True, parents=True)
    ref = next((files/"reference_ensembl_r92").glob("*.fa.gz"))
    forms = dict(isoforms(ref))
    tsv(out/"cassette_map.tsv",["transcript","cassette"],forms.items())
    genes_for_tx,_ = reference(files)
    bulk,iso,single = [],[],[]
    sources = {ref}
    for model,accession,ctrl,ko in MODELS:
        human = accession == "GSE156243"
        src = next((files/"geo"/accession).glob("*count_table.txt.gz" if human else "*TPM_Table.txt.gz"))
        sources.add(src)
        wanted = {g.upper() if human else g:g for g in GENES}
        names,raw = load_target(src,wanted,None if human else genes_for_tx)
        data = {wanted[g]:np.log2(1+v) for g,v in raw.items()}
        for partner,core in (("Grik5","Grik2"),("Neto1","Grik1"),("Grik4","Grik1")):
            data[f"{partner}_minus_{core}"] = data[partner]-data[core]
        w = [i for i,n in enumerate(names) if n.startswith(ctrl)]
        k = [i for i,n in enumerate(names) if n.startswith(ko)]
        assert min(len(w),len(k)) >= 2
        for gene,y in data.items():
            def delta(skip):
                return np.mean([y[i] for i in k if i!=skip])-np.mean([y[i] for i in w if i!=skip])
            loo = [delta(i) for i in w+k]
            bulk.append((model,gene,len(w),len(k),delta(None),min(loo),max(loo)))
        if not human:
            accum = {typ: np.zeros(len(names)) for typ in ("insert","skip","other")}
            with gzip.open(src,"rt") as stream:
                rows = csv.reader(stream,delimiter="\t")
                assert next(rows)[3:] == names
                for tx,_,_,*values in rows:
                    if tx in forms:
                        accum[forms[tx]] += np.array(values,float)
            for i in w+k:
                a,b,c = (accum[t][i] for t in ("insert","skip","other"))
                assert np.isclose(a+b+c, np.exp2(data["Grik1"][i])-1)
                iso.append((model,names[i],"KO" if i in k else "control",a,b,c,a/(a+b),
                            a/(a+b+c),(a+c)/(a+b+c)))
    class_counts = {"ctrl": {}, "ko": {}}
    for arm,cell,depth,values in assigned_nuclei(files,[],[],GENES):
        class_counts[arm][cell] = int(values["Grik1"].sum())
        if cell in ("exc","inh"):
            for a,b in (("Grik5","Grik2"),("Neto1","Grik1"),("Grik4","Grik1")):
                va,vb = values[a],values[b]
                single.append((arm,cell,len(depth),a,b,int((va>0).sum()),int((vb>0).sum()),
                               int(((va>0)&(vb>0)).sum()),
                               np.log2(1+1e6*va.sum()/depth.sum())-np.log2(1+1e6*vb.sum()/depth.sum())))
    fractions = {}
    weights = []
    for arm in ("ctrl","ko"):
        prefix = files/"geo/GSE158684"/f"GSE158684_{arm}_filtered_"
        with gzip.open(str(prefix)+"features.tsv.gz","rt") as source:
            ids = {str(i) for i,line in enumerate(source,1) if line.split("\t")[1]=="Grik1"}
        assert ids
        with gzip.open(str(prefix)+"matrix.mtx.gz","rt") as source:
            next(line for line in source if not line.startswith("%"))
            total = sum(int(parts[2]) for line in source if (parts:=line.split())[0] in ids)
        class_counts[arm]["unassigned_or_low_depth"] = total-sum(class_counts[arm].values())
        fractions[arm] = {cell:n/total for cell,n in class_counts[arm].items()}
        weights.extend((arm,cell,n,total,fractions[arm][cell]) for cell,n in class_counts[arm].items())
        for suffix in ("matrix.mtx.gz","features.tsv.gz"):
            sources.add(files/"geo/GSE158684"/f"GSE158684_{arm}_filtered_{suffix}")
    tv = sum(abs(fractions["ko"][c]-w) for c,w in fractions["ctrl"].items())/2
    tsv(out/"class_weights.tsv", ["pool","class","Grik1_molecules","total","fraction"],weights)
    tsv(out/"class_mixture_bound.tsv",["model","maximum_absolute_fraction_shift"],
        [("class-constant splice fractions, pooled nuclear molecule weights",tv)])
    tsv(out/"bulk.tsv","model gene_or_ratio n_control n_KO delta_log2 LOO_min LOO_max".split(),bulk)
    tsv(out/"isoforms.tsv","model library arm insert_TPM skip_TPM other_TPM fraction_among_classified lower_all upper_all".split(),iso)
    tsv(out/"nuclei.tsv","pool assigned_class nuclei partner core partner_positive core_positive double_positive log_partner_minus_core".split(),single)
    tsv(out/"inputs.tsv",["input","sha256"],[(f.name,hashlib.sha256(f.read_bytes()).hexdigest()) for f in sorted(sources)])


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files",type=Path)
    args = parser.parse_args()
    main(args.files,Path(__file__).parent/"results")
