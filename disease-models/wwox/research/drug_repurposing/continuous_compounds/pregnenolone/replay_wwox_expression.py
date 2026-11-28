"""Screen steroid routing transcripts in held WWOX models as descriptive context."""
import argparse
import csv
import gzip
from math import log2
from pathlib import Path
from statistics import mean
import sys

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("worktree", type=Path)
parser.add_argument("files", type=Path)
args = parser.parse_args()

compounds = args.worktree / "disease-models/wwox/research/drug_repurposing/continuous_compounds"
sys.path.insert(0, str(compounds / "ribitol"))
import replay_matriglycan_screen as common

# Mouse and human AKR entries are routed separately. No one-to-one mapping is assumed.
common.GENES = {
    "upstream_context": ("Star", "Cyp11a1", "Hsd3b1", "Hsd3b2"),
    "five_alpha_reduction": ("Srd5a1", "Srd5a2"),
    "mouse_product_routing": ("Akr1c14",),
    "human_product_routing": ("Akr1c1", "Akr1c2", "Akr1c3"),
    "sulfate_handling": ("Sult2b1", "Sts", "Papss1", "Papss2"),
}
common.ALIASES = {}
common.verified_expression(args.files)
output_dir = Path(__file__).resolve().parent
common.tsv(output_dir / "initial_bulk_transcripts.tsv",
    "model accession category gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
    common.bulk_rows(args.files))
common.tsv(output_dir / "initial_cage_transcripts.tsv",
    "stage category gene mapped_symbol ctrl_n ko_n ctrl_TPM depletion_TPM log2_delta mapping".split(),
    common.cage_rows(args.files))

# Analyze the other P17 hippocampal genotypes against their own controls.
# The same underlying series is used for all arms. These are descriptive contrasts.
import coagonist_screen

hippocampal_models = (
    ("hippocampus_neuronal_deletion", "GSE158681", "S_Ctrl_", "S_KO_"),
    ("hippocampus_progenitor_deletion", "GSE158681", "N_Ctrl_", "N_KO_"),
    ("hippocampus_constitutive_null", "GSE158681", "WT_", "KO_"),
)
original_models = coagonist_screen.MODELS
coagonist_screen.MODELS = hippocampal_models
try:
    common.tsv(
        output_dir / "p17_hippocampal_genotypes.tsv",
        "model accession category gene mapped_symbol ctrl_n ko_n ctrl_positive ko_positive ctrl_mean ko_mean log2_delta omit_min omit_max mapping".split(),
        common.bulk_rows(args.files),
    )
finally:
    coagonist_screen.MODELS = original_models


def sult2b1_biotype_rows(files):
    reference, = (files / "reference_ensembl_r92").glob("*.fa.gz")
    with gzip.open(reference, "rt", encoding="utf-8") as stream:
        biotypes = {}
        for line in stream:
            if line.startswith(">") and " gene_symbol:Sult2b1 " in line:
                transcript = line.split()[0][1:]
                biotypes[transcript] = line.split(" transcript_biotype:")[1].split()[0]

    source, = (files / "geo" / "GSE158681").glob("*TPM_Table.txt.gz")
    with gzip.open(source, "rt", encoding="utf-8") as stream:
        reader = csv.DictReader(stream, delimiter="\t")
        libraries = reader.fieldnames[3:]
        grouped = {kind: [] for kind in sorted(set(biotypes.values()))}
        for row in reader:
            transcript = row["Name"]
            if transcript in biotypes:
                grouped[biotypes[transcript]].append(row)
    assert sum(map(len, grouped.values())) == len(biotypes)

    for model, _, control_tag, knockout_tag in hippocampal_models:
        control = [library for library in libraries if library.startswith(control_tag)]
        knockout = [library for library in libraries if library.startswith(knockout_tag)]
        for biotype, rows in grouped.items():
            def values(group):
                return [sum(float(row[library]) for row in rows) for library in group]

            ctrl, ko = values(control), values(knockout)
            delta = mean(log2(1 + x) for x in ko) - mean(log2(1 + x) for x in ctrl)
            yield model, biotype, len(rows), len(ctrl), len(ko), mean(ctrl), mean(ko), delta


common.tsv(
    output_dir / "sult2b1_transcript_biotypes.tsv",
    "model transcript_biotype transcript_count ctrl_n ko_n ctrl_TPM ko_TPM log2_delta".split(),
    sult2b1_biotype_rows(args.files),
)
