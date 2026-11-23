"""Score the fixed myelin signature on non-myelin phagocytosis in GSE221080."""
import csv
import gzip
import io
import sys
import tarfile
from pathlib import Path

import numpy as np

from analyze import reference, score, tsv


def main():
    files, inputs, signature, out = map(Path, sys.argv[1:])
    out.mkdir(exist_ok=True, parents=True)
    tx, _ = reference(files)
    with signature.open() as f:
        genes = list(csv.DictReader(f, delimiter="\t"))
    up, down = [[r["gene"] for r in genes if r["direction"] == direction] for direction in ("up", "down")]
    wanted = set(up + down)
    with gzip.open(inputs/"GSE221080_series_matrix.txt.gz","rt") as f:
        meta = list(csv.reader(f, delimiter="\t"))
    def field(name, prefix=""):
        row, = [r for r in meta if r and r[0]==name and r[1].startswith(prefix)]
        return [s.removeprefix(prefix) for s in row[1:]]
    labels = dict(zip(field("!Sample_geo_accession"), zip(field("!Sample_characteristics_ch1","genotype: "),field("!Sample_characteristics_ch1","treatment: "))))
    samples = []
    with tarfile.open(inputs/"GSE221080_RAW.tar") as tar:
        for member in tar.getmembers():
            accession = Path(member.name).name.split("_")[0]
            genotype, treatment = labels[accession]
            with tarfile.open(fileobj=io.BytesIO(tar.extractfile(member).read()),mode="r:gz") as inner:
                quant, = [m for m in inner if m.name.endswith("/quant.sf")]
                with io.TextIOWrapper(inner.extractfile(quant)) as f:
                    data = {}
                    for row in csv.DictReader(f,delimiter="\t"):
                        gene = tx.get(row["Name"].split(".")[0])
                        if gene in wanted:
                            data[gene] = data.get(gene,0) + float(row["TPM"])
            value,sizes = score({g:np.log2(1+v) for g,v in data.items()},up,down)
            assert min(sizes)>=10
            samples.append([accession,genotype,treatment,*sizes,value])
    assert len(samples)==len(labels) and len({s[0] for s in samples})==len(labels)
    tsv(out/"alternative_samples.tsv","accession genotype sort up_mapped down_mapped score".split(),samples)
    results = []
    for genotype in sorted({s[1] for s in samples}):
        rows = [r for r in samples if r[1]==genotype]
        def contrast(omit):
            means = [np.mean([s[-1] for i,s in enumerate(rows) if i!=omit and s[2]==kind]) for kind in ("Phag","Non_Phag")]
            return means[0]-means[1]
        loo = [contrast(i) for i in range(len(rows))]
        results.append([genotype, sum(r[2]=="Phag" for r in rows), sum(r[2]=="Non_Phag" for r in rows), contrast(-1), min(loo), max(loo)])
    tsv(out/"alternative_contrasts.tsv","genotype phag nonphag delta loo_min loo_max".split(),results)


if __name__ == "__main__":
    main()
