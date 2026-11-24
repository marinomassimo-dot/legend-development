# Reproduce the human GRIN1 junction counts

The six archived single-read libraries are listed in runs.tsv. The dataset contains two untreated libraries and four WWOX-knockout libraries from the WiBR3 background. The analysis unit is a deposited library; the six observations do not represent six donors. For the primary estimate use centered Q20 reads with one unambiguous junction class. Report a genotype direction only when every library supplies at least 20 informative primary reads. This criterion failed in the first control.

Build and validate the counter in this directory. The supplied synthetic controls contain both junction classes and a conflict.

```sh
g++ -std=c++17 -O3 grin1_count.cpp -lz -o grin1_count
python3 counter_controls.py ./grin1_count | cmp - counter_controls.tsv
python3 ../organoid_summary.py . > /tmp/legend-grin1-per-library.tsv
cmp /tmp/legend-grin1-per-library.tsv per_library_counts.tsv
python3 library_precision.py /tmp/legend-grin1-per-library.tsv | cmp - per_library_precision.tsv
```

For an independent replay from raw FASTQs, use an empty output directory: the wrapper reuses existing verified TSVs. From this directory run:

```sh
replay_dir=$(mktemp -d)
python3 ../../../perampanel_ampa_splicing_20261123/human_count.py runs.tsv "$PWD/grin1_count" junction_probes.tsv "$replay_dir"
diff -r organoid_counts "$replay_dir"
```
 Allow up to one complete compressed library in temporary storage. The wrapper validates each file against the original compressed MD5, byte count and full FASTQ read count. Intermediate downloads are temporary.

The 24 reference windows span one inclusion or one skipping junction ending in the same downstream exon. The 15-base upstream anchor is primary and additional offsets assess positional sensitivity. Regenerate windows from human RefSeq records NM_007327.4, NM_000832.7, NM_001185090.2 and NM_001185091.2 in NCBI GenBank XML saved as human_grin1.gb.xml. Run human_junctions.py from this directory. The two audit tables record the exact-match screen on hg38 and human Ensembl cDNAs. No diagnostic window had a genomic or off-gene transcript hit in the screened references.
