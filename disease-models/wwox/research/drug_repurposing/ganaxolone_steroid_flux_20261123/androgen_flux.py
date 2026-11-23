"""Summarize measured substrate alternatives and conditional steroid-conversion contrasts."""
import argparse
import hashlib
from pathlib import Path
import sys
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ganaxolone_20261123"))
from analyze import assigned_nuclei, load_target, reference, tsv


def main(files, out):
    out.mkdir(exist_ok=True, parents=True)
    wt_gene = "Wwox"
    alternative = "Hsd17b12"
    genes = {wt_gene, alternative}
    tx, _ = reference(files)
    geo = files / "geo"
    hip, = (geo / "GSE158681").glob("*TPM_Table.txt.gz")
    cortex, = (geo / "GSE158682").glob("*TPM_Table.txt.gz")
    organoid, = (geo / "GSE156243").glob("*count_table.txt.gz")
    samples, summary = [], []
    studies = [
        ("neuronal_cortex", cortex, "CRTX_S_Ctrl_", "CRTX_S_KO_"),
        ("neuronal_hippocampus", hip, "S_Ctrl_", "S_KO_"),
        ("global_hippocampus", hip, "WT_", "KO_"),
        ("human_organoid", organoid, "cwt", "cko"),
    ]
    for model, path, control, mutant in studies:
        human = path == organoid
        expected = {g.upper() for g in genes} if human else genes
        labels, data = load_target(path, expected, None if human else tx)
        assert set(data) == expected
        wt = [i for i, label in enumerate(labels) if label.startswith(control)]
        ko = [i for i, label in enumerate(labels) if label.startswith(mutant)]
        assert min(len(wt),len(ko)) >= 2
        for gene, x in sorted(data.items()):
            units = "CPM" if human else "TPM"
            for i in wt + ko:
                samples.append([model, labels[i], "KO" if i in ko else "control", gene, units, x[i]])
            log = np.log2(1 + x)
            def effect(omit=None):
                return log[[i for i in ko if i!=omit]].mean() - log[[i for i in wt if i!=omit]].mean()
            omission = [effect(i) for i in wt+ko]
            summary.append([model,gene,units,len(wt),len(ko),x[wt].mean(),x[ko].mean(),
                            min(x[ko]),effect(),min(omission),max(omission)])
    tsv(out/"samples.tsv", "model sample genotype gene units abundance".split(), samples)
    tsv(out/"summary.tsv", "model gene units controls mutants control_mean mutant_mean mutant_min log_delta omit_min omit_max".split(), summary)
    cellular=[]
    for arm, name, depth, data in assigned_nuclei(files, [], [], genes):
        ww, alt = data[wt_gene],data[alternative]
        cellular.append([arm,name,len(depth),int(depth.sum()),int(ww.sum()),int(alt.sum()),
                         sum(ww>0),sum(alt>0),sum((ww>0)&(alt>0))])
    tsv(out/"nuclei.tsv", "pool assigned_class nuclei all_UMIs Wwox_UMIs Hsd17b12_UMIs n_Wwox n_Hsd17b12 n_both".split(),cellular)
    inputs=[hip,cortex,organoid,*sorted((files/"reference_ensembl_r92").glob("*.fa.gz")),
            *sorted((geo/"GSE158684").glob("*features*")),*sorted((geo/"GSE158684").glob("*matrix*"))]
    tsv(out/"inputs.tsv", ["filename","sha256"], [[p.name,hashlib.sha256(p.read_bytes()).hexdigest()] for p in inputs])
    # Keller (2006), table 2.10. Apparent velocities in micromoles/minute for the cell assay.
    # Treat substrates in separate assays, equal concentration in each, and a common preparation.
    kinetics=[]
    for concentration in (.01,.1,1,10,100):
        v_androstenedione = 5.3e-8 * concentration / (.7 + concentration)
        v_androsterone = 6.6e-7 * concentration / (2.2 + concentration)
        kinetics.append([concentration,v_androstenedione,v_androsterone,v_androsterone/v_androstenedione])
    tsv(out/"apparent_rates.tsv", "equal_substrate_uM androstenedione_umol_per_min androsterone_umol_per_min androsterone_over_androstenedione".split(),kinetics)


if __name__=="__main__":
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument("files",type=Path)
    p.add_argument("out",type=Path)
    a=p.parse_args()
    main(a.files,a.out)
