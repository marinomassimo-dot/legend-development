"""Reproduce the perampanel premise tests from the LEGEND files cache."""
import argparse
import csv
import gzip
import re
from pathlib import Path

import numpy as np

PANELS = {
    "AMPA": "Gria1 Gria2 Gria3 Gria4",
    "AMPA234": "Gria2 Gria3 Gria4",
    "reactive": "Apoe Trem2 Cst7 Lpl",
    "stress": "Atf3 Ddit3 Hmox1",
    "activity": "Fos Arc Egr1 Npas4 Junb Nr4a1",
    "OPC": "Pdgfra Cspg4 Cspg5 Pcdh15",
    "COP": "Gpr17 Neu4 Bmp4 Vcan",
    "myelin": "Mbp Plp1 Mobp Cnp",
    "age": "Grin2a Slc12a5 Nrgn Camk2a Scn8a",
    "neuron": "Snap25 Rbfox3 Syt1 Stmn2 Tubb3 Map2",
}
TARGETS = PANELS["AMPA"].split()
PANELS.update({g: g for g in TARGETS})
# Post hoc markers aligned to the developmental AMPAR genetic experiment.
PANELS.update({g: g for g in ("Enpp6", "Pdgfra")})
WANTED = set(" ".join(PANELS.values()).split())
CLASSES = {
    "Exc": "Slc17a7 Camk2a Satb2", "Inh": "Gad1 Gad2 Slc32a1",
    "Ast": "Aqp4 Aldh1l1 Slc1a2", "Mic": "Cx3cr1 P2ry12 Csf1r",
    "OPC": PANELS["OPC"], "COP": PANELS["COP"],
    "NFOL": "Tcf7l2 Itpr2 Enpp6 Bcas1 Tmem2 Fyn Casr",
    "MFOL": "Mal Mog Opalin Serinc5 Mag", "MOL": "Klk6 Apod Pmp22 Slc5a11 Ermn Hapln2",
}


def mapping(files):
    result = {}
    with gzip.open(files / "reference_ensembl_r92/Mus_musculus.GRCm38.cdna.all.fa.gz", "rt") as f:
        for line in f:
            if line.startswith(">"):
                m = re.search(r"gene_symbol:(\S+)", line)
                if m and m[1] in WANTED:
                    result[line[1:].split()[0].split(".")[0]] = m[1]
    return result


def expression(path, transcripts=None):
    data = {}
    with gzip.open(path, "rt") as f:
        rows = csv.reader(f, delimiter="\t")
        offset = 1 if transcripts is None else 3
        samples = next(rows)[offset:]
        totals = np.zeros(len(samples))
        for row in rows:
            if transcripts is None:
                values = np.array(row[offset:], float)
                totals += values
                gene = row[0]
            else:
                gene = transcripts.get(row[0].split(".")[0])
            if gene in WANTED:
                data[gene] = data.get(gene, 0) + np.array(row[offset:], float)
        if transcripts is None:
            data = {g: v * 1e6 / totals for g, v in data.items()}
    if WANTED - data.keys():
        raise ValueError(f"Missing genes: {WANTED - data.keys()}")
    return samples, {k: np.mean([np.log2(1 + data[g]) for g in gs.split()], axis=0)
                     for k, gs in PANELS.items()}


def bulk(label, samples, scores, case, control, results, measurements, adjusted=False):
    indices = [i for i, s in enumerate(samples) if s.startswith((case, control))]
    group = np.array([int(samples[i].startswith(case)) for i in indices])
    stage = (scores["age"] - scores["neuron"])[indices]
    design = np.column_stack((np.ones(len(group)), group, stage))
    for k, values in scores.items():
        y = values[indices]
        for j, i in enumerate(indices):
            measurements.writerow([label, samples[i], group[j], k, f"{y[j]:.6f}"])
        effect = y[group == 1].mean() - y[group == 0].mean()
        estimates = []
        if adjusted:
            for omit in [-1, *range(len(y))]:
                mask = np.arange(len(y)) != omit
                assert np.linalg.matrix_rank(design[mask]) == 3
                estimates.append(np.linalg.lstsq(design[mask], y[mask], rcond=None)[0][1])
        results.writerow([label, k, sum(group), len(group)-sum(group), f"{effect:.4f}",
                          *([f"{v:.4f}" for v in (estimates[0], min(estimates[1:]), max(estimates[1:]))]
                            if estimates else ["NA", "NA", "NA"])])


def nucleus(files, table):
    names = list(CLASSES)
    wanted = set(" ".join(CLASSES.values()).split()) | set(TARGETS)
    by_arm = {}
    for arm in ["ctrl", "ko"]:
        prefix = str(files / f"geo/GSE158684/GSE158684_{arm}_filtered_")
        with gzip.open(prefix + "features.tsv.gz", "rt") as f:
            indices = {i: row.split("\t")[1] for i, row in enumerate(f, 1)
                       if row.split("\t")[1] in wanted}
        assert set(indices.values()) == wanted
        with gzip.open(prefix + "matrix.mtx.gz", "rt") as f:
            dims = next(row for row in f if not row.startswith("%"))
            _, n, entries = map(int, dims.split())
            matrix = np.fromstring(f.read(), dtype=np.int64, sep=" ").reshape(-1, 3)
        assert len(matrix) == entries
        totals = np.bincount(matrix[:, 1]-1, weights=matrix[:, 2], minlength=n)
        keep = totals >= 500
        genes = {}
        for i, g in indices.items():
            subset = matrix[matrix[:, 0] == i]
            counts = np.bincount(subset[:, 1]-1, weights=subset[:, 2], minlength=n)[keep]
            genes[g] = np.log2(1 + 1e6 * counts / totals[keep])
        scores = np.column_stack([np.mean([genes[g] for g in CLASSES[c].split()], axis=0) for c in names])
        by_arm[arm] = genes, scores
    scale = np.percentile(np.concatenate([s for _, s in by_arm.values()]), 99, axis=0)
    for arm, (genes, scores) in by_arm.items():
        norm = scores / scale
        for i, name in enumerate(names):
            mask = (norm.argmax(axis=1) == i) & (norm.max(axis=1) >= .2)
            for g in TARGETS:
                table.writerow([arm, name, int(mask.sum()), g, f"{np.mean(genes[g][mask] > 0):.4f}"])


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("files", type=Path)
    parser.add_argument("out", type=Path)
    args = parser.parse_args()
    args.out.mkdir(exist_ok=True, parents=True)
    transcripts = mapping(args.files)
    with (args.out/"panels.tsv").open("w") as a, (args.out/"sample_scores.tsv").open("w") as b:
        result, samples = [csv.writer(f, delimiter="\t", lineterminator="\n") for f in (a, b)]
        result.writerow("contrast panel cases controls raw stage_adjusted loo_min loo_max".split())
        samples.writerow("contrast sample case panel mean_log_expression".split())
        for dataset, case, ctrl, label in [
            ("GSE158682", "CRTX_S_KO_", "CRTX_S_Ctrl_", "cortex_Wwox"),
            ("GSE158681", "S_KO_", "S_Ctrl_", "hippo_Wwox"),
        ]:
            path, = (args.files/"geo"/dataset).glob("*TPM_Table.txt.gz")
            bulk(label, *expression(path, transcripts), case, ctrl, result, samples, dataset == "GSE158682")
        path = args.files/"deepening_downloads/gse319769/counts_fixed.tsv.gz"
        bulk("hippo_kainate_d14", *expression(path), "iaka14_", "iasl14_", result, samples)
    with (args.out/"nuclei.tsv").open("w") as f:
        table = csv.writer(f, delimiter="\t", lineterminator="\n")
        table.writerow("pool class nuclei gene fraction_detected".split())
        nucleus(args.files, table)


if __name__ == "__main__":
    main()
