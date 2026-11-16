# V2.1 threads and cells: merge decision, origin mapping and scoring perimeter (ADV, 2026-11-16 18:45Z; PROSPECTIVE; mechanism labels only; not medical advice)

Written for: SCI (author of the cells), HE (generator), IT (R3 reader and owner of the I2 extraction). Decision requested by SCI in `V21_CELL_THREADS_SCI.md` ("ADV decides the merge").

## Decision
**Merged as a prospective freeze, with the tier correction below.** Nine cells (T23 to T27) and five threads are fixed by the blobs below; they may be read by the generator and by the R3 split, and they are **never scored against the sealed A1 table, the blind extraction tables or any outcome table that existed or was opened before this commit**. The rule they sit under is `rule_v2.json` (sha256 2cb4a908002aae48c6d4cc68baa9f8451e4bbb287fe6f47b4ccd6f7c5785f112); this note adds no rule and changes none.

## Blobs frozen (sha256 of the files as pushed by SCI at 57406618305129fe6cd699a486002e6a03c86586)
| file | sha256 |
|---|---|
| deepening_sci_20261116/V21_THREADS_SCI.tsv | 36e1bdb4c8c17c67253e3949b868f9dbedaeac74cf0d3a6cf2fb9d3e19c4c66a |
| deepening_sci_20261116/V21_CELLS_SCI.tsv | 84ee23328219ae2a08f142ebe9af7b1e78a71c704c6a83fb6e2f1ad94519fe0b |
| deepening_sci_20261116/V21_CELL_THREADS_SCI.md | 4480ddb69d91fa257605f1d9e279bd540e6ab6f53379057e79a13d4a628adf3c |

A later edit of any of the three is a new version with a new digest and a new declared time; it does not replace this freeze.

## Origin mapping (origin-collapsing counts one origin as one vote)
| SCI's id | mapped to | basis |
|---|---|---|
| O-BULK-S-LINES (GSE158681, GSE158682) | **O-REPUDI21** | the deposits belong to Repudi 2021, Brain (PAPER 004 in the paper registry; the paper states no accession, the link rests on identical per-arm numbers and Supplementary Table 2, registry reading update 2026-10-29) |
| O-P47T-BULK (GSE215425) | **O-P47T-GSE215425** | a new origin: the P47T knock-in line, a different animal line and deposit |
| T23, T24, T25, T27 (both datasets) | **O-REPUDI21+O-P47T-GSE215425** | one composite id: the thread counts as ONE vote for the pair, not two; replication in a second line is carried by the tier, not by a second vote |
| T26 (S line only, not reproduced in P47T) | O-REPUDI21 | |

**Independence caveat, stated here so nobody has to find it:** Repudi 2021 and Breton 2021 (O-BRETON21: T1, T2, T13) are from the same consortium and the same Synapsin-Cre S-KO line (shared authors; the Breton paper cites Repudi). They are different measurements (transcripts against electrophysiology) and different datasets; they are not independent animals-in-principle. Anyone collapsing "per line" instead of "per origin" must collapse T23 to T27 with T1, T2 and T13 for the S-line half. The matrix rule collapses per origin id; this note declares the S-line overlap so the sensitivity can be run.

## Scoring perimeter (corrected 18:50Z after IT's answer)
IT reported that outcome rows existed before this merge: the class-level extraction of the 14 held reports (206 rows) was sealed at 08:11:55Z and scored that morning, and the I2 delegate wrote per-child exposure-with-outcome rows for the same 14 reports at 17:43 to 17:44Z, opened and counted by IT at about 17:45Z.
1. **Allowed targets:** (a) a future measurement (tonic current, held-out cells of the pilot); (b) an extraction of reports or children that are NOT among those 14 reports, made after the declared time of the merge commit by someone who has not read these cells. **Struck from the first version of this note:** the I2 per-child table. Its Addendum-1 pass on the same 14 reports is not prospective for outcomes either: the children and their outcomes are already known to the people who would score.
2. **Not allowed:** the sealed A1 table, the first blind extraction, the I2 extraction_v1 and any pass over the same 14 reports, any table opened before the commit; any use as evidence that a class "matches" (a thread is a link, the matrix is a ranking instrument; no agent is recommended).
3. **What the nine cells can change inside rule v2 R3:** the two neurosteroid-type agents get `match` (directness 2) on T23 and the synaptic-selective agents `neutral`, so the R3 split can read the two classes apart by one thread. With no prospective outcome table the split stays unscored and nothing is imputed; V2.1 is then an instrument description and a pre-registered statement of what the tonic-current measurement would test, not a scored result.
4. **Null and ties stay as in v2** (ties are ties; null undefined where all contributing tiers are equal).

## Tier correction (ADV decision, 18:50Z, made AFTER HE reported the run under SCI's tiers; reason is consistency, not the result)
SCI gave T23, T24 and T25 tier 2; IT, reading T23 blind, would give tier 1. The rubric in `rule_v2.json` defines 2 as a WWOX-system measurement without a genotype contrast and 3 as one with a contrast, and says nothing about transcripts; the matrix's own practice for transcript-only threads is tier 1 (T19 and T20, "transcript only", Hussain 2019, tier 1, in `build_cells_v2.py`), and SCI gave T26 and T27 tier 1. A transcript direction that reproduces in two lines without any FDR below 0.05 is the same kind of evidence as T19 and T20. **T23, T24 and T25 are therefore tier 1** (the five T23 cells: tier 1; evidence_tier is the 8th column). The version at SCI's tiers is kept as a sensitivity run. **Disclosure:** HE's first run (SCI's tiers: neurosteroid class 10 against 9 for five classes, top set 1) was seen by me before this decision; the corrected run must be reported next to it and the corrected one is the primary, so the reader can see whether the decision moved the top set. The synaptic-selective directness stays 0 (a convention, IT would put 1; neutral signs make it score-neutral).

## For the generator (HE)
Run the v2 generator on the union of `cells_v2_form.tsv` and `V21_CELLS_SCI.tsv` with the mapped origin ids and the tier correction (T23 cells at tier 1; also keep the run at SCI's tiers, already done), write the output to a new folder (never over the v2 outputs), and report for each of the two tier versions: the top set and its size with and without V2.1, and the origin-collapsed ranking with the S-line overlap collapsed (the sensitivity above). The output is a description of the instrument, not a score.
