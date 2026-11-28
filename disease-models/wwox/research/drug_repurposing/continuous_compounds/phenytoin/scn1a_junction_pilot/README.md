# SCN1A exon 5 | Coverage in a public WWOX organoid control library

context_policy: QUESTION_DRIVEN

**Unit and preparation.** One single-end RNA-seq library, SRR12453541, from homogenized untreated human cerebral organoids in GSE156243. Read counts are informative sequences within this library. The library is the smallest by compressed size in the six-run held manifest and was selected in the [pretest](PRETEST.md). [Series](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Prior manifest of six runs](../../../perampanel_ampa_splicing_20261123/results/human_run_qc.tsv)

## Method and outcome

For each alternative exon, match the junction from the common coding exon 4 to the alternative exon 5. GRCh38 chr2 coordinates are 1-based and inclusive on the minus strand. Exon 4 spans 166054638–166054766. Exon 5A spans 166052852–166052943 (ENST00000637988.2). Exon 5N spans 166053039–166053130 (ENST00000640036.2). A 31-mer must span the junction with at least 10 bases on each side. The primary rule uses 15 upstream and 16 downstream bases, all Q20 or higher. Sensitivities include all prespecified offsets and minimum Q30. Search either strand and count each read once per rule. Reads supporting both alternatives have a separate conflict count. The reused counter's output labels `flip` and `flop` correspond to 5A and 5N. [Probe sequences](candidates.tsv) · [Liang et al., Fig. 1B, p. 3](https://link.springer.com/article/10.1186/s13073-021-00949-0)

All 24 strand-aware exact probes had zero matches in the GRCh38 genomic reference and zero matches to Ensembl cDNA annotated to another gene. At each offset, 5A had 17 matching SCN1A transcript records and 5N had one. These are counts of annotated sequences. [Genome audit](genome_audit.tsv) · [Transcript audit](transcript_audit.tsv)

The verified compressed file was 1,703,840,713 bytes with ENA MD5 `fa9e17761ef92bf2d5998b308fa4472e`. Of **34,397,207** intact FASTQ reads, **zero** matched the 5A junction, **zero** matched the 5N junction and zero conflicted under the primary rule and all three sensitivity rules. The denominator for an isoform fraction is therefore zero. The prespecified coverage requirement was at least 20 informative reads. The largest remaining run has about 1.37 times as many reads as the pilot. Depth alone offers little reason to expect a usable contrast under this rule. Other libraries could differ in transcript abundance, cell composition or capture. [Archived reads](https://ftp.sra.ebi.ac.uk/vol1/fastq/SRR124/041/SRR12453541/SRR12453541.fastq.gz) · [Counts](SRR12453541_counts.tsv)

## Decision

Defer bulk-organoid 5A/5N inference for this analysis. This zero result applies to the exact junction assay in a single control library. It leaves transcript expression and a WWOX genotype contrast unresolved. Liang et al. report that the mouse lineage lacks a functional equivalent of the human SCN1A 5N alternative. Keep the mouse experiment on sodium availability and inhibitory recruitment. If a native genotype difference remains after waveform matching in a human preparation, prioritize direct exon-specific measurements by developmental stage and cell class. A targeted junction assay needs to demonstrate coverage of both alternatives within biological replicates. [Liang et al., Fig. 4A and Results, p. 8](https://link.springer.com/article/10.1186/s13073-021-00949-0)

## Replay

Run `bash replay.sh SRR12453541.fastq.gz hg38.fa.gz Homo_sapiens.GRCh38.cdna.all.fa.gz OUT_DIR`. The script checks the archive size and digest, verifies both pinned reference digests, compiles the existing matcher with its Ensembl target changed to SCN1A and compares every audit and counting row. It requires a C++17 compiler with zlib. The input is downloaded from ENA. Use the same GRCh38 assets as the held [human junction analysis](../../../perampanel_ampa_splicing_20261123/README.md).
