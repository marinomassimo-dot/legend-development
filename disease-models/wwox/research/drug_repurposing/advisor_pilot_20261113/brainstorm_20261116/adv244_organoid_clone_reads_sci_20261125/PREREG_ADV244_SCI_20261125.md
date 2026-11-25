# ADV-244 pre-registration: assigning the four knockout organoid libraries to clones from raw reads (SCI; hypothesis level; not medical advice)

Written before any raw read was fetched in this task. Effort high, no delegate, no spend, no contact. Feasibility probe: 20-minute exit from the acceptance of the step (2026-11-25T02:20:29Z).

## What is known before looking
* PMID 34268881: clones 1B (KO1) and A2 (KO2) were selected for organoids; editing at WWOX exon 1 (Fig EV1C, appendix PDF page 2).
* My reading of Fig EV1C rendered at 1200 dpi (an image reading, not a deposited sequence): the single T after ...CTGCGC and before ACGCGG... is expanded. KO1 shows runs of 5 T and 2 T; KO2 shows runs of 3 T and 2 T. So T5 would mark KO1, T3 would mark KO2, T2 is shared, T1 is wild type.
* Runs: SRX8947985..88 = SRR12453542..45 = GSM4727527..30 = cko1..cko4; single-end, mean about 86 nt; 39 to 47 million reads each. GEO numbers the samples 1 to 4, which says nothing about clones.

## Data taken
The first 20 million reads of each of the four knockout runs, streamed from the ENA fastq route and not stored; only reads that match the pattern below are written. The same from one wild-type run (SRX8947983 or SRX8947984, cwt) as a detection control, which the brief does not ask for. No full run.

## Tool
Exact pattern match, both orientations: GCTGCGC(T+)ACGCGG and its reverse complement. No aligner, no error tolerance in the anchors. Each read counted once.

## Calling rule per library
* **KO1**: at least 3 reads with T5, and T3 reads fewer than one fifth of T5 reads.
* **KO2**: at least 3 reads with T3, and T5 reads fewer than one fifth of T3 reads.
* **mixed**: at least 3 of each.
* **unassigned**: anything else, including any run length I did not predict, however frequent.
* Detection control: the wild-type run must show T1 reads (at least 3) and neither T3 nor T5. If it does not, no call is made.
* Wild-type (T1) reads in a knockout library are reported as they are.

## What follows
* Two libraries KO1 and two KO2: redo the ADV-239 organoid removals at clone level (log2(CPM+1), same sets and genes; clone-dependent if a clone alone has the opposite sign or less than half the effect). This can weaken a reading; it cannot make it robust against the control side (2 wild types).
* All four one clone: say so; "two clones" does not hold for the sequenced libraries.
* Any unassigned library at the exit: write the limit and the read counts; no clone-level removal on a partial map unless at least one library of each clone is assigned and the rest are reported as unknown.

## Predictions
* P1: the probe reaches 3 distinguishing reads in all four libraries (0.6).
* P2: the split is two and two (0.5, given P1).
