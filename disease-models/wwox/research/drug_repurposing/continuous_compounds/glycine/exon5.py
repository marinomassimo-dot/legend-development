"""Estimate the Grin1 N1 cassette share from exact versioned mouse transcript TPMs."""
import csv
import gzip
from pathlib import Path
import re
from statistics import mean
import sys

here = Path(__file__).resolve().parent
sys.path.insert(0, str(here.parents[1] / "perampanel_ampa_splicing_20261123"))
from analyze import CODE

files, out = map(Path, sys.argv[1:3])
records = {}
with gzip.open(next((files/"reference_ensembl_r92").glob("*.fa.gz")), "rt") as infile:
    for line in infile:
        if line.startswith(">"):
            name = None
            if " gene_symbol:Grin1 " in line:
                name = line[1:].split()[0]
                records[name] = (re.search(r"transcript_biotype:(\S+)", line)[1], [])
        elif name:
            records[name][1].append(line.strip().upper())

groups = {}
left, cassette, right = "ETLLEERESK", "SKKRNYENLDQLSYDNKRGPK", "AEKVLQFDP"
motifs = {"included": left+cassette+right, "skipped": left+right}
with (out/"cassette_identity.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("transcript", "biotype", "supported_junction", "eligible"))
    for name, (biotype, parts) in sorted(records.items()):
        seq = "".join(parts)
        peptides = ["".join(CODE.get(seq[i:i+3], "X") for i in range(frame, len(seq)-2, 3))
                    for frame in range(3)]
        hits = [label for label, motif in motifs.items() for peptide in peptides if motif in peptide]
        observed, = hits if len(hits) == 1 else ["unknown"]
        groups[name] = observed if biotype == "protein_coding" else "other"
        writer.writerow((name, biotype, observed, groups[name] in motifs))

arms = {"GSE158681": (("neuronal", "S_Ctrl_", "S_KO_"), ("progenitor", "N_Ctrl_", "N_KO_"),
                      ("constitutive", "WT_", "KO_")),
        "GSE158682": (("neuronal", "CRTX_S_Ctrl_", "CRTX_S_KO_"),)}
with (out/"cassette_fractions.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("dataset", "contrast", "n_WT", "n_KO", "WT_included_fraction", "KO_included_fraction",
                     "difference_pp", "omit_min_pp", "omit_max_pp", "min_classified_share_all_TPM"))
    for acc, contrasts in arms.items():
        path, = (files/"geo"/acc).glob("*TPM_Table.txt.gz")
        with gzip.open(path, "rt") as source:
            rows = csv.reader(source, delimiter="\t")
            names = next(rows)[3:]
            counts = {label: [0.0]*len(names) for label in ("included", "skipped", "other", "unknown")}
            seen = set()
            for row in rows:
                if row[0] in groups:
                    target = counts[groups[row[0]]]
                    seen.add(row[0])
                    for i, tpm in enumerate(row[3:]):
                        target[i] += float(tpm)
        assert seen == groups.keys(), (acc, groups.keys() - seen)
        both = [a+b for a,b in zip(counts["included"], counts["skipped"])]
        share = [a/b for a,b in zip(counts["included"], both)]
        coverage = [b/(b+u+o) for b,u,o in zip(both,counts["unknown"],counts["other"])]
        for label, wt_prefix, ko_prefix in contrasts:
            wt = [i for i,n in enumerate(names) if n.startswith(wt_prefix)]
            ko = [i for i,n in enumerate(names) if n.startswith(ko_prefix)]
            def avg(ids, omit=None):
                return mean(share[i] for i in ids if i != omit)
            def delta(omit=None):
                return 100*(avg(ko, omit)-avg(wt, omit))
            omissions = [delta(i) for i in wt+ko]
            writer.writerow((acc, label, len(wt),len(ko), f"{avg(wt):.4f}", f"{avg(ko):.4f}",
                             f"{delta():.3f}", f"{min(omissions):.3f}", f"{max(omissions):.3f}",
                             f"{min(coverage[i] for i in wt+ko):.4f}"))
