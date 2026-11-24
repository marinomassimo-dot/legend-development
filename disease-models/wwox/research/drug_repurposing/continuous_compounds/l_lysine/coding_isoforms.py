"""Cross-check archived Kars transcript estimates against exact mouse RefSeq coding sequences."""
import argparse
import csv
import gzip
from math import log2
from pathlib import Path
import re
from statistics import mean
from xml.etree import ElementTree as ET


def kars_cdna(path):
    transcripts = {}
    with gzip.open(path, "rt") as source:
        for line in source:
            if line.startswith(">"):
                current = None
                if " gene_symbol:Kars " in line:
                    current = line[1:].split()[0]
                    biotype = re.search(r"transcript_biotype:(\S+)", line)[1]
                    transcripts[current] = [biotype, []]
            elif current:
                transcripts[current][1].append(line.strip().upper())
    return {name: (typ, "".join(parts)) for name, (typ, parts) in transcripts.items()}


def reference_cds(path):
    sequences = {}
    for entry in ET.parse(path).findall("GBSeq"):
        for feature in entry.findall(".//GBFeature"):
            if feature.findtext("GBFeature_key") != "CDS":
                continue
            start, end = map(int, feature.findtext("GBFeature_location").split(".."))
            coding = entry.findtext("GBSeq_sequence")[start-1:end].upper()
            qualifiers = {q.findtext("GBQualifier_name"): q.findtext("GBQualifier_value")
                          for q in feature.findall(".//GBQualifier")}
            sequences[coding] = qualifiers["product"]
    if len(set(sequences.values())) != 2:
        raise ValueError("Expected the two mouse reference products")
    return sequences


def empirical_bounds(samples, ctrl, ko):
    totals = [log2(1 + sum(values)) for values in zip(*samples)]
    def delta(skip):
        return mean(totals[i] for i in ko if i != skip) - mean(totals[i] for i in ctrl if i != skip)
    excluded = [delta(i) for i in ctrl + ko]
    return (delta(None), min(excluded), max(excluded))


parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("files", type=Path)
parser.add_argument("refseq_xml", type=Path)
parser.add_argument("output", type=Path)
args = parser.parse_args()
transcripts = kars_cdna(next((args.files/"reference_ensembl_r92").glob("*.fa.gz")))
cds = reference_cds(args.refseq_xml)
classes = {}
for tid, (biotype, seq) in transcripts.items():
    hits = {name for coding, name in cds.items() if coding in seq}
    classes[tid] = (next(iter(hits)) if len(hits) == 1 else "unresolved") if biotype == "protein_coding" else biotype
with (args.output/"coding_identity.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("transcript", "archived_biotype", "complete_refseq_CDS_class", "cDNA_nt",
                     "unique_start_fraction_50nt", "unique_start_fraction_75nt", "unique_start_fraction_100nt",
                     "product_specific_start_fraction_75nt"))
    for tid, (biotype, seq) in sorted(transcripts.items()):
        fractions = []
        for k in (50,75,100):
            others = {s[j:j+k] for key, (_, s) in transcripts.items() if key != tid for j in range(len(s)-k+1)}
            fraction = mean(seq[i:i+k] not in others for i in range(len(seq)-k+1))
            fractions.append(f"{fraction:.4f}")
        other_products = {s[j:j+75] for key, (_, s) in transcripts.items() if classes[key] != classes[tid]
                          for j in range(len(s)-74)}
        group_fraction = mean(seq[i:i+75] not in other_products for i in range(len(seq)-74))
        writer.writerow((tid, biotype, classes[tid], len(seq), *fractions, f"{group_fraction:.4f}"))
with (args.output/"isoform_bounds.tsv").open("w") as stream:
    writer = csv.writer(stream, delimiter="\t", lineterminator="\n")
    writer.writerow(("dataset","deletion","set","transcript_count","wt_libraries","ko_libraries","delta","omit_min","omit_max"))
    contrasts = (("GSE158681","neuronal","S_Ctrl_","S_KO_"),
                 ("GSE158681","neural_progenitor","N_Ctrl_","N_KO_"),
                 ("GSE158681","constitutive","WT_","KO_"),
                 ("GSE158682","neuronal","CRTX_S_Ctrl_","CRTX_S_KO_"))
    for acc, deletion, wt, ko in contrasts:
        with gzip.open(next((args.files/"geo"/acc).glob("*TPM_Table.txt.gz")), "rt") as data:
            rows = csv.reader(data, delimiter="\t")
            names = next(rows)[3:]
            selected = {r[0]: list(map(float,r[3:])) for r in rows if r[0] in transcripts}
        if set(selected) != set(transcripts):
            raise ValueError("Archive transcript versions disagree")
        ctrl = [i for i,n in enumerate(names) if n.startswith(wt)]
        knockout = [i for i,n in enumerate(names) if n.startswith(ko)]
        groups = {"all": list(selected), "protein_coding": [t for t in selected if transcripts[t][0] == "protein_coding"]}
        for cls in sorted(set(classes.values())):
            groups[cls] = [t for t in selected if classes[t] == cls]
        for cls, ids in groups.items():
            bounds = empirical_bounds([selected[t] for t in ids],ctrl,knockout)
            writer.writerow((acc,deletion,cls,len(ids),len(ctrl),len(knockout),*(f"{v:.4f}" for v in bounds)))
