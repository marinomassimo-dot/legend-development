# ADV-099 blind recompute: report as delivered (legend-delegate, sonnet, effort high, blind, one round, no sub-delegation; delivered 2026-11-20; persisted verbatim by SCI from the subagent hand-back; the brief is `BLIND_RECOMPUTE_BRIEF_ADV099_SCI_20261120.md`). Delegate output; SCI has compared its pivotal numbers with the producer run (see `NEURON_DISCOVERY_RESULT_ADV099_SCI_20261120.md`, section "Blind recompute"). Hypothesis level only; not medical advice.

ADV-099 blind recompute (sonnet, effort high, one round). I read only the frozen pre-registration (sha256 starts 63faafa4) and the held GSE158684 and GSE156243 data. Code is in /home/desktop/.claude/jobs/2d2e7085/tmp/blind_adv099_20261120/ (load.py, an.py); numpy only, run with `-I`. Every number below was computed by me. Seed 20261120.

**Choices I made where the text is open**
- Marker score = mean of x over the panel genes. The glial panels were not named in the text, so I chose them. Astrocyte: Gfap, Aqp4, Slc1a2, Aldh1l1, Gja1. Microglia: Cx3cr1, P2ry12, Csf1r, Tmem119, C1qa. Oligodendrocyte lineage: Mbp, Plp1, Mog, Mobp, Pdgfra, Olig2, Cspg4.
- The 99th percentile is taken over all kept nuclei of both arms.
- The 35 duplicated mouse symbols in the features file were merged by summing their counts.
- Total counts = sum over all genes.
- Maturity covariate: leave-one-out for the 11 panel genes (each gene's own m, then z-scored in the class). The z-scoring does not change the arm coefficient.
- Half-splits: each arm is split in half at random (stratified by arm). The class-level m is kept, and the median is re-centred inside each half. A gene is stable if the sign agrees in at least 18 of 20 splits. The 0.25 threshold is applied only to the full-data c_N', not inside the halves.
- Organoid: CPM = count / library column sum x 1e6. Group agreement uses the raw (uncentred) log2(CPM+1) group-mean minus control-mean, with absolute value at least 0.25 in both groups and the sign of c_O. c_O in the |c_O| >= 0.5 rule is the centred value.
- Null: the O pass status of a gene (UP, DOWN or none, with agreement) is shuffled within deciles of the class mean x among the genes analysed in both systems. The N side stays fixed.
- Glial flag: mean CPM in a glial class greater than 4 times the neuron-class mean CPM in both arms, for any of the three glial classes.

**1. Nuclei and classes**
- All 6,102 nuclei have total counts of at least 500, so the filter dropped none (3,182 control, 2,920 knockout).
- 99th percentiles: excitatory 9.037, inhibitory 7.256, astrocyte 8.259, microglia 7.304, oligodendrocyte 7.470.
- Excitatory: 1,676 control, 1,401 knockout.
- Inhibitory: 268 control, 364 knockout.
- Other classes (control/knockout): astrocyte 393/509, microglia 174/218, oligodendrocyte 615/282. Unassigned: 56/146.

**2. Nuclei per class**

| | Excitatory | Inhibitory |
|---|---|---|
| Genes analysed | 7,738 | 7,622 |
| Median arm coefficient used for centring | -0.0903 | -0.1871 |
| UP (c_N' >= +0.25) before stability | 1,662 | 2,009 |
| DOWN (c_N' <= -0.25) before stability | 1,800 | 2,050 |
| UP after stability | 1,658 | 1,435 |
| DOWN after stability | 1,796 | 1,407 |

Genes stable overall (any sign): 4,838 of 7,738 excitatory, 2,878 of 7,622 inhibitory.

**3. Organoid**
- 14,367 of 35,337 genes have mean CPM at least 1.
- Median c_O used for centring: -0.0138.
- O rule passes: UP 732, DOWN 326.
- Centred c_O alone, without group agreement: UP 1,335, DOWN 1,136.

**4. Genes analysed in both systems (upper-case symbol match) and replicated counts (both rules, same sign)**

| | Excitatory | Inhibitory |
|---|---|---|
| Genes analysed in both | 6,778 | 6,690 |
| N-pass UP / DOWN (stable) among them | 1,451 / 1,528 | 1,279 / 1,166 |
| O-pass UP / DOWN among them | 354 / 110 | 345 / 116 |
| Replicated UP / DOWN | 72 / 25 | 71 / 18 |

Of the replicated genes, 3 UP and 1 DOWN in each class are glial-enriched by my flag.

**5. Permutation null (2,000 permutations, within-decile shuffle)**

| Class, direction | Observed | Null mean | Null 97.5th percentile | Null max | Fraction of null >= observed | Verdict |
|---|---|---|---|---|---|---|
| Excitatory UP | 72 | 79.27 | 94.0 | 107 | 0.845 | NOTHING_REPLICATES_BEYOND_CHANCE |
| Excitatory DOWN | 25 | 23.55 | 32.0 | 39 | 0.410 | NOTHING_REPLICATES_BEYOND_CHANCE |
| Inhibitory UP | 71 | 63.11 | 77.0 | 89 | 0.136 | NOTHING_REPLICATES_BEYOND_CHANCE |
| Inhibitory DOWN | 18 | 18.18 | 26.0 | 31 | 0.571 | NOTHING_REPLICATES_BEYOND_CHANCE |

No direction in either class exceeds its null, so under the registered rule the stop rule applies.

**6. Spearman correlation of c_N' with c_O, across genes analysed in both**
- Excitatory: -0.047 (n = 6,778).
- Inhibitory: -0.056 (n = 6,690).
- Both are essentially zero.

**Sensitivities (extra computations, not registered; none changes the verdict)**
- Group agreement computed on median-centred group differences instead of raw: replicated UP/DOWN becomes 73/25 (excitatory) and 74/18 (inhibitory).
- Without the N stability condition, excitatory replicated is 72/25 and inhibitory is 95/25. The observed counts there are higher, but I did not run a null for that variant, so I make no verdict claim for it.

**Differences from the registered text, and what I did not do**
- No nucleus was dropped by the 500-count filter.
- I did not run a null that excludes the glial-flagged genes. I only counted the flagged genes among the replicated ones (item 4).
- I did not map the replicated genes (section 4 of the pre-registration), because nothing exceeded its null. Reported by count only; I did not check the symbol-match loss (orthologues with different names) beyond the "analysed in both" figures.
- Stability depends on random splits. The seed is stated, but I did not rerun with other seeds.
- No repository file was edited, nothing committed, no receipt, no network use.
