# Perampanel premise tested at the GRIA2 Q/R editing site

**Decision, 23 November 2026.** The six public human WWOX organoid RNA-seq libraries do not resolve whether WWOX knockout changes the fraction of unedited mature GluA2 RNA. We checked 252,931,601 reads. Only **30** qualified at the site, and **14** also crossed the downstream splice junction. All 14 splice-supported reads contained the edited base. This does not distinguish an ordinary high editing rate from a modest genotype difference. No perampanel was administered in these libraries. [WWOX organoid experiment](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE156243) · [Frozen decision](prediction.md)

## Why this test is different from gene expression

Edited and unedited GluA2 protein can confer different calcium permeability to AMPA receptors even when total GRIA2 RNA is unchanged. The primary hypothesis was a rise in mature unedited GRIA2 in the knockout. An alternative is altered abundance of receptors that lack GluA2 entirely. Perampanel can affect AMPA-mediated transmission through either population. A further rival explanation is recent network activity. In a separate study, TTX plus APV in ordinary cultured neurons increased the fraction of unedited RNA within half an hour, with recovery by 24 hours. An editing difference in WWOX tissue could therefore reflect the activity history, even if it were detected. [Q/R editing during neural differentiation](https://pmc.ncbi.nlm.nih.gov/articles/PMC4350408/) · [Activity deprivation experiment](https://pubmed.ncbi.nlm.nih.gov/40359260/)

## All six libraries

A is the unedited genomic base in transcript orientation, G the edited base. Splice-supported reads also match eight bases of the following exon.

| Library | Genotype | Primary A / (A+G) | Splice-supported A / (A+G) |
|---|---|---:|---:|
| SRR12453540 | WT | 1/4 | 0/1 |
| SRR12453541 | WT | 0/4 | 0/2 |
| SRR12453542 | KO | 0/5 | 0/2 |
| SRR12453543 | KO | 0/9 | 0/3 |
| SRR12453544 | KO | 0/4 | 0/4 |
| SRR12453545 | KO | 0/4 | 0/2 |

The only unedited call comes from a control library. It did not meet the splice-junction criterion, so its maturation status is unknown. The unweighted primary difference was −12.5 percentage points, driven by that single read; omitting its library gives zero. The primary count was 4–9 per library against a predeclared minimum of 30. The splice-aware minimum of ten per library also failed. No C/T/N calls passed primary filters. The 18-base flanks retained the only A; the read-interior check also retained it. The secondary filters cannot compensate for sparse biological sampling. [Library counts and counting-only Wilson intervals](results/per_library.tsv) · [Differences and omission checks](results/group_difference.tsv)

For scale, if the true unedited fraction were 5% and every informative read independent, the chance of observing even one A would be only 18.5% at four reads and 37.0% at nine. Even 30 reads give 78.5% under this idealization. A zero of four gives a counting-only upper 95% Wilson limit of roughly 49%. Neither the intervals nor pooled reads quantify variation among organoids. Exact matching may exclude molecules with other differences in the flanks, individual cells are unresolved, and non-UMI reads with different or shared offsets cannot establish molecule independence. The deposited series did not sample at defined times relative to an electrical event.

## Coordinate and technical controls

The codon and the annotated editing feature independently identify NM_000826.6 nt 2135 (c.1820A; Q607). The historical text note mentioning 2279 points to a different codon in this accession version. Allowing any central base and requiring the 12 or 18 flanking bases on each side found just one position in the downloaded hg38 genome, chr4:157336723 on the plus strand; all transcriptome hits belonged to GRIA2 (22 transcripts per width, Ensembl release 112). The eight genomic intronic bases immediately following this exon differ from the eight spliced transcript bases at six positions. An eight-read known-answer fixture tests edited/unedited alleles, both orientations, intron retention, a third base, end proximity and central/flank quality rejection. [RefSeq](https://www.ncbi.nlm.nih.gov/nuccore/NM_000826.6) · [Genome matches](results/genome_matches.tsv) · [Transcript matches](results/transcript_matches.tsv)

The independent mouse cortex and hippocampus projects PRJNA666184 and PRJNA666183 exposed no public FASTQ entries in the ENA run reports checked on 23 November. NCBI returned “not public” for their first linked SRA experiments, SRX9206265 and SRX9206251. Transcript-abundance tables alone cannot remeasure this base. These series provide no independent editing estimate here. [Mouse cortex](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682) · [Mouse hippocampus](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681)

**What would change the decision.** A replicated genotype difference in mature site-specific RNA with adequate coverage, accompanied by altered calcium-permeable AMPA currents at matched developmental stage and activity history, would support moving this mechanism up the list. An independent measurement of receptors lacking GluA2 would distinguish a change of subunit composition. A drug-specific benefit would still require an actual perampanel comparison. The present analysis leaves these possibilities open. [Earlier perampanel dossier](../perampanel_20261122/README.md)

## Reproduction

The verified ENA manifest records run accessions, file locations, bytes, MD5 values and expected record counts. The six compressed reads total 12,391,912,328 bytes. The counter verifies all three integrity measures and processes one run at a time. Use Python 3.11 or later. Store the fixed RefSeq GenBank record in INPUTS, copy results/ena_runs.tsv to INPUTS/runs.tsv, and place the genomic and transcriptomic references there for the uniqueness check. Reference hashes are provided. No raw third-party sequencing reads or paper figures are redistributed. Only selected source sections and public data were used for this analysis.

```bash
python3 verify_counter.py "$INPUTS/NM_000826.6.gb"
python3 editing.py reference "$INPUTS/NM_000826.6.gb" "$INPUTS/hg38.fa.gz" results/genome_matches.tsv
python3 editing.py reference "$INPUTS/NM_000826.6.gb" "$INPUTS/Homo_sapiens.GRCh38.cdna.all.fa.gz" results/transcript_matches.tsv
python3 run_series.py "$INPUTS" results/runs
python3 summarize.py results/runs results
```

[ENA manifest](results/ena_runs.tsv) · [Genome FASTA](https://hgdownload.soe.ucsc.edu/goldenPath/hg38/bigZips/hg38.fa.gz) · [Ensembl cDNA](https://ftp.ensembl.org/pub/release-112/fasta/homo_sapiens/cdna/Homo_sapiens.GRCh38.cdna.all.fa.gz) · [Reference hashes](results/references.sha256)
