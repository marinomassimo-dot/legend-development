# ADV-244 result: all four knockout organoid libraries carry clone 1B's edit (SCI, 2026-11-25)

Actor `orchestrator` (SCI). Hypothesis level; reference genotype class; nothing here is medical advice. Free ENA reads, no spend, no contact, no delegate, nothing installed. Pre-registration: `PREREG_ADV244_SCI_20261125.md` (frozen before any read was fetched).

## 1. Answer

1. **cko1, cko2, cko3 and cko4 all call KO1 (clone 1B).** Each has reads with the 5 T run of KO1's allele and with the 2 T run that both clones carry; none has the 3 T run that marks KO2. The wild-type control shows only the unedited single T.
2. **The organoid transcriptome (GSE156243) therefore compares one CRISPR clone with its parental line**: four organoids of clone 1B against two of WiBR3. "Two clones" does not hold for the sequenced libraries.
3. **What that changes.** A difference in this deposit cannot be separated from anything particular to clone 1B (off-target edits, drift during cloning). The four libraries are replicate organoids, not independent genetic units. At the level of genetic units the contrast is one clone against one line.
4. **What it does not change.** No value moves, and ADV-239's disposition stays "not testable". The study's other assays use both clones (Fig EV1B, EV1I); this finding is about the RNA sequencing only. No clone-level removal is possible with one clone.
5. **A reading of mine to update.** The two library groups recorded in ADV-069 (cko1+cko2, cko3+cko4) are within one clone, so what separates them is not clonal identity.

## 2. Counts

First 20,000,000 reads of each run (of 39 to 47 million), streamed and not stored. Pattern `GCTGCGC(T+)ACGCGG`, both orientations. "WWOX flanks" is a post hoc filter that keeps only reads whose neighbouring bases continue as WWOX exon 1 (the 13-base anchor also occurs elsewhere).

| Library (run) | T1 | T2 | T3 | T5 | Call |
|---|---|---|---|---|---|
| cko1 (SRR12453542) | 0 | 3 | 0 | 7 (6 with flanks) | KO1 |
| cko2 (SRR12453543) | 0 | 4 | 0 | 3 | KO1 |
| cko3 (SRR12453544) | 1 (0 with flanks) | 3 | 0 | 6 | KO1 |
| cko4 (SRR12453545) | 0 | 3 | 0 | 3 | KO1 |
| cwt1 (SRR12453540, control) | 15 (10 with flanks) | 0 | 0 | 0 | control passes |

The call is the same with and without the flank filter. `out_counts_adv244.tsv` holds both.

## 3. Where the alleles come from

Fig EV1C of PMID 34268881 (appendix PDF page 2, rendered at 1200 dpi and read by eye, no deposited sequence): after `...CTGCGC`, KO1 shows alleles with 5 T and 2 T, KO2 with 3 T and 2 T. The reads reproduce KO1's pair exactly in all four libraries.

* That all four libraries are **one** clone rests on the reads alone: they share the same pair of alleles.
* That this clone is the one the paper calls **KO1** rests on my reading of the figure. No KO2 library was observed, so KO2's pattern is not checked against any data.

## 4. Predictions

| | Prediction | Outcome |
|---|---|---|
| P1 | at least 3 distinguishing reads in all four libraries (0.6) | Met (3 to 7) |
| P2 | the split is two and two (0.5) | Not met: four of one clone |

## 5. Limits

* Counts are small (3 to 7 distinguishing reads); the minimum was fixed at 3 beforehand.
* One cko1 T5 read lacks matching flanks; one cko1 read sequence appears twice (possible PCR duplicate). Neither moves a call.
* First reads of each file, not a random sample.
* Not checked: whether clone 1B differs from its parental line elsewhere in the genome.
* No independent re-run by a second reader.

## 6. Proposed wording (replaces ADV-242 section 6)

For the organoid rows (K01, D01, D02, M01, E02, I01, INV-16, RP-008, CLAIM 002; claim text only through a candidate): "four knockout organoids of **one** CRISPR clone (1B) against two organoids of the parental line, apparently one batch; one further wild type was excluded for not clustering. A difference here is not shown to be independent of the clone."

## 7. Files and disk

`stream_count_adv244.py`, `summarise_adv244.py`, `out_counts_adv244.tsv`, `stream_log_adv244.txt`. The matching reads (24 KB, third-party data, not in git; digests in `matched_reads_sha256.txt`) are kept at the root checkout under `files/geo/adv244_matched_reads_20261125/` so the call can be re-checked; the 20-million-read subsamples were never written to disk. Free space on the volume was 16.99 GB before; this probe's own files are 24 KB there and 3.2 MB of figure renders in the job scratch folder.

## 8. DREAM

Not yet consumed: the wording of section 6. A method that costs minutes and no disk (streaming reads for an edit-spanning pattern) can assign clone identity in any CRISPR-model deposit whose clones' edits are published; no other deposit has been checked.
