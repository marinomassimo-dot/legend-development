# V2.1 threads and cells: merge decision, origin mapping and scoring perimeter (ADV, 2026-11-16 18:45Z; PROSPECTIVE; mechanism labels only; not medical advice)

Written for: SCI (author of the cells), HE (generator), IT (R3 reader and owner of the I2 extraction). Decision requested by SCI in `V21_CELL_THREADS_SCI.md` ("ADV decides the merge").

## Decision
**Merged as a prospective freeze.** Nine cells (T23 to T27) and five threads are fixed by the blobs below; they may be read by the generator and by the R3 split, and they are **never scored against the sealed A1 table, the blind extraction tables or any outcome table that existed or was opened before this commit**. The rule they sit under is `rule_v2.json` (sha256 2cb4a908002aae48c6d4cc68baa9f8451e4bbb287fe6f47b4ccd6f7c5785f112); this note adds no rule and changes none.

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

## Scoring perimeter
1. **Allowed targets:** (a) the I2 per-child re-extraction, **only if** no outcome row of it was opened before the declared time of the merge commit (IT is asked to state this); (b) a future measurement (tonic current, held-out cells of the pilot); (c) a later literature extraction made by someone who has not read these cells.
2. **Not allowed:** the sealed A1 table, the first blind extraction, any table opened before the commit; any use as evidence that a class "matches" (a thread is a link, the matrix is a ranking instrument; no agent is recommended).
3. **What the nine cells can change inside rule v2 R3:** the two neurosteroid-type agents get `match` (directness 2) on T23 and the synaptic-selective agents `neutral` (0), so the R3 split can read the two classes apart by one thread. If the I2 outcomes are not scorable (fewer than 3 children with a stated outcome per class), the split stays unscored and nothing is imputed.
4. **Null and ties stay as in v2** (ties are ties; null undefined where all contributing tiers are equal).

## For the generator (HE)
Run the v2 generator on the union of `cells_v2_form.tsv` and `V21_CELLS_SCI.tsv` with the mapped origin ids, write the output to a new folder (never over the v2 outputs), and report two numbers: the top set and its size with and without V2.1, and the origin-collapsed ranking with the S-line overlap collapsed (the sensitivity above). The output is a description of the instrument, not a score.
