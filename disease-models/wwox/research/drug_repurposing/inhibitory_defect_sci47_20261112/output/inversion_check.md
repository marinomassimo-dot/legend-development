# Inversion check: which of sIPSC amplitude and frequency falls more (PMID 34634460)

Non-canonical research material. Not medical advice. Reference genotype class only. Source read: PMC full text incl. legends, Methods, Table 1, Supplement text and figures (depth in `receipts/`). Paths below relative to `disease-models/wwox/research/drug_repurposing/`.

## What the source says (measured or declared)
* Results 2.5 (printed means and SD, 140 mM KCl pipette, -70 mV, no antagonist named): sIPSC amplitude S-CTL 57.3 +/- 31.0 pA, S-KO 27.5 +/- 19.4 pA; frequency S-CTL 10.3 +/- 11.5 Hz, S-KO 8.4 +/- 10.0 Hz. n: S-CTL 14 cells from 7 animals, S-KO 9 cells from 5 animals (Fig 4 legend).
* My arithmetic (labelled): amplitude -52.0% (KO is 0.48 of control); frequency -18.4% (KO is 0.82 of control). The frequency falls BY about a fifth, not TO a fifth.
* The authors' sentences: "the sIPSCs were reduced in both amplitude and frequency"; "primarily through an impairment in the amplitude of the inhibitory currents". Amplitude is the larger fall, in the authors' own words and in the figure (Fig 4H h1 curves separated widely; h2 curves close; the mean waveform in Fig 4G about -45 pA control against about -20 pA KO, inferred_from_figure).
* Is the frequency change significant, and how shown? Only as a Kolmogorov-Smirnov test on the cumulative distribution (Fig 4H h2): pooled p = 9.42e-8, S-WT vs S-KO 6.16e-8, S-HT vs S-KO 4.56e-5. No test of per-cell or per-animal mean frequency is printed; the unit of the KS test is not declared (the smallest KS p one value per cell can give is above 1e-6, so event or interval units are implied; IT36 audit). The SD exceed the mean in both groups, which points to a distribution of per-interval values, not of cell means (inference). If the SD were across cells (not stated), a two-sample t on the printed values would be about 0.4 for frequency and about 2.8 for amplitude (own arithmetic, assumption stated).

## Where the repository states the relation (file:line; meaning against the source)
| Place | Statement | Meaning matches the source? |
|---|---|---|
| `inhibitory_defect_sci47_20261112/inputs_it46/it46_README.md:26` (copy of IT46) | "amplitude about half, frequency about a fifth" | Wording ambiguous ("a fifth" of the fall, or of the value); read as a fall by 18% it matches. Read as "to a fifth" it would be false (KO frequency is 82% of control). Needs rewording. |
| same file `:27` | "the amplitude falling more than the frequency" | Matches the source (52% against 18%). The inference drawn from it is not supported as stated (see below). |
| `inputs_it46/s5_result_it46.md:6` and `:30` | "52% fall ... 18% fall, SDs as large as the means"; deficit "larger in amplitude than in frequency" | Matches in magnitude and direction. |
| `function_pharm_it14_p3_20261101/README.md:13`; `disease-models/wwox/analysis/therapeutic_canonical_repair_package.md:443`; `canonical_impact_and_negative_audit.md:39` | amplitude -52% only | Match; none states a frequency size. |
| `decisive_rechecks_it36_20261108/verify/items.md` E15 | frequency difference 1.9 Hz small against its spread | Matches, and is the only place that treats the frequency change as not firm. |
| `next_batch_it42_20261110/BRIEF.md:19`; `locator_audits/2026-10-28_it3_needs_second_verification.md:21` | "frequency reduced"; "IPSC frequency also reduced" | Match. |
No place found states that frequency fell more than amplitude, or by half or to a fifth. Search perimeter: `git grep` over the worktree with the strings fifth, 18%, 20 percent, "more than", sIPSC with frequency; the two large registries not grepped; IT46 originals are not on main (copies only).

## Result
The suspected inversion is a wording hazard, not a reversal of meaning: direction and order of the two falls are the same in the source and in every held statement. What the source does not support is the step built on the order: "amplitude falls more than frequency, so receptor response or GABA content per event". The source cannot carry that step because (i) the frequency change has only a pooled-distribution KS test, (ii) amplitude and detected frequency are not independent (a 4 x SD detection threshold removes small events), (iii) a loss of a high-amplitude input class lowers mean amplitude with an unchanged per-synapse amplitude, (iv) event identity (GABA-A against glutamatergic events, with no antagonist at -70 mV in KCl) is not shown. Fix the wording to "falls by about 18%" wherever "about a fifth" is used.
