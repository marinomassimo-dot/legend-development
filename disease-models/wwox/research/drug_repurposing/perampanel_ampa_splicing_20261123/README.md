# Perampanel and GRIA2 flip/flop splicing in WWOX loss

**Mouse decision, 23 November 2026.** The classifications do not support enrichment of the slower-desensitizing flip isoform across the two P17 neuronal-Wwox-deletion regions. Cortex passed coverage and shifted slightly in the opposite direction. Hippocampus failed coverage because a large fraction of Gria2 RNA belonged to transcripts without a diagnostic cassette. These are tissue-level transcript estimates. No WWOX preparation was treated with perampanel. [Locked mouse hypothesis](prediction.md) · [Results and bounds](results/contrasts.tsv)

## Why this could matter beyond burst suppression

Independent patch recordings of recombinant unedited GluA2 found faster desensitization of the flop than flip form during sustained glutamate application. The two forms differ in a short alternatively spliced cassette. Auxiliary proteins can change the consequence of that cassette. Perampanel binds an allosteric site near the channel and can stabilize its closed state. We asked if WWOX loss biases the population toward a slower-desensitizing receptor, creating a particular substrate for modulation during sustained input. This prediction is distinct from a change in calcium permeability via Q/R editing. It neither assumes isoform-selective perampanel binding nor estimates net benefit in a developing brain. [Koike et al., primary electrophysiology](https://pubmed.ncbi.nlm.nih.gov/10704491/) · [Cassette–auxiliary protein interaction](https://pmc.ncbi.nlm.nih.gov/articles/PMC10124957/) · [Perampanel structural study](https://pubmed.ncbi.nlm.nih.gov/27618672/) · [Previous Q/R result](../perampanel_gria2_editing_20261123/README.md)

## Quantitative test in mouse

We used two complete multi-residue motifs to identify flip and flop sequences in Ensembl release 92 mouse Gria2 transcripts. Independently, curated NCBI RefSeq proteins identified the same exact motif for two flip and two flop transcripts. One shorter curated protein had neither motif. The two full-length Ensembl coding forms classified unambiguously, each matched the precise transcript version in both GEO tables. Five retained-intron and one nonsense-mediated-decay transcripts remained unclassified. Estimates below are means of animal-level fractions; raw reads covering splice junctions were unavailable for these two series. [Mouse RefSeq comparison](results/refseq.tsv) · [Transcript classification and abundance](results/annotations.tsv) · [Individual libraries](results/libraries.tsv)

| P17 tissue and genotype | Controls / KO | Flip share, control → KO | Change in percentage points | Lowest classifiable fraction of total Gria2 |
|---|---:|---:|---:|---:|
| Cortex, neuronal deletion | 4 / 3 | 87.2% → 85.6% | −1.60 | 85.4% |
| Hippocampus, neuronal deletion | 2 / 3 | 66.6% → 62.7% | −3.87 | 39.4% |
| Hippocampus, global null | 3 / 2 | 63.2% → 66.0% | +2.84 | 54.8% |
| Hippocampus, progenitor deletion | 2 / 2 | 70.4% → 69.6% | −0.82 | 40.3% |

In cortex, the effect among classified transcripts ranged from −2.20 to −0.85 percentage points on animal omission. Even assigning all unclassified KO abundance to flip and all unclassified control abundance to flop gave at most +4.53 points, below the prespecified +5-point prioritization floor. This is a fixed-data allocation bound, not a population confidence limit. The alternative assignment permitted a decrease of up to 8.47 points. The sensitivity limited to predicted ORFs of at least 800 residues with a stop codon returned the same two coding forms. The hippocampal allocation bounds span both directions widely. Changes in cell mix or developmental maturation remain possible. Neither area measures subunit assembly, current kinetics or drug responses. [Primary hippocampal deposit](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158681) · [Primary cortical deposit](https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE158682)

## How large could the kinetic consequence be in a simple receptor mixture?

As an exploratory forward calculation, take the classified cortical RNA shares as if they were fractions of functional receptor populations. Normalize each mixed response to its own peak and integrate the exponential desensitization plus the measured residual current over a 100-ms glutamate step. Using Koike et al.’s GluA2Q values and equal peak contribution per receptor gives a **1.46% smaller** charge for the knockout share. The independently reported Q/R co-expression condition gives a 1.48% decrease. Allowing a fixed 0.25–4 ratio of peak current per flip versus per flop receptor yields decreases between 0.42% and 3.86% across the two configurations. The calculation applies to the plateau and decay following an instantaneous peak. It omits receptor abundance, activation, deactivation between pulses, auxiliary proteins, drug occupancy and firing. A large increase in native sustained current would therefore need a mechanism beyond this simple projection from the measured cortical shares. [Primary kinetic estimates](https://pubmed.ncbi.nlm.nih.gov/10704491/) · [Pulse and peak-weight sensitivity](results/kinetic_projection.tsv)

## Reproduction

The mouse program takes Ensembl release 92 GRCm38 cDNA, a GenBank file with the six [mouse Gria2 RefSeq mRNAs](https://www.ncbi.nlm.nih.gov/gene/?term=Gria2%5BGene%5D+AND+Mus+musculus%5BOrgn%5D), the two deposited transcript TPM tables, and an output directory. The accession versions and checksums identify the inputs. Targeted review used published functional results, primary data tables and sequence annotations. Only original code and derived summaries are included. [Input hashes](results/sources.tsv)

```bash
python3 analyze.py Mus_musculus.GRCm38.cdna.all.fa.gz mouse_refseq.gb hippocampus_TPM.txt.gz cortex_TPM.txt.gz results
```

Reproduce the conditional pulse calculation with `python3 kinetic_projection.py` after the mouse analysis.
