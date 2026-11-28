#!/usr/bin/env bash
set -euo pipefail

if [[ $# != 4 ]]; then
    echo "Usage: bash replay.sh SRR12453541.fastq.gz GRCh38_genome.fa.gz Ensembl_GRCh38_cdna.fa.gz OUT_DIR" >&2
    exit 2
fi

study_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
reused_counter="$study_dir/../../../perampanel_ampa_splicing_20261123/junction_counter.cpp"
raw_reads="$1"
genome="$2"
transcripts="$3"
output="$4"

test "$(stat -c %s -- "$raw_reads")" = "1703840713"
printf 'fa9e17761ef92bf2d5998b308fa4472e  %s\n' "$raw_reads" | md5sum --check --status
printf 'c1dd87068c254eb53d944f71e51d1311964fce8de24d6fc0effc9c61c01527d4  %s\n' "$genome" |
    sha256sum --check --status
printf '0bb3012f45e2474b8ce79911c47de0fc216bd574c60f1ddc8a8d911cd8a32b4d  %s\n' "$transcripts" |
    sha256sum --check --status

mkdir -p "$output"
scratch="$(mktemp -d)"
trap 'rm -rf -- "$scratch"' EXIT
# The original matcher takes the same two class labels. Only the Ensembl target gene changes.
sed 's/gene_symbol:GRIA2 /gene_symbol:SCN1A /' "$reused_counter" > "$scratch/counter.cpp"
g++ -O3 -std=c++17 "$scratch/counter.cpp" -lz -o "$scratch/counter"
"$scratch/counter" audit "$study_dir/candidates.tsv" "$genome" > "$scratch/genome_audit.tsv"
"$scratch/counter" audit "$study_dir/candidates.tsv" "$transcripts" > "$scratch/transcript_audit.tsv"
"$scratch/counter" count "$study_dir/candidates.tsv" "$raw_reads" > "$scratch/SRR12453541_counts.tsv"

for result in genome_audit.tsv transcript_audit.tsv SRR12453541_counts.tsv; do
    diff -u "$study_dir/$result" "$scratch/$result"
    cp "$scratch/$result" "$output/"
done
