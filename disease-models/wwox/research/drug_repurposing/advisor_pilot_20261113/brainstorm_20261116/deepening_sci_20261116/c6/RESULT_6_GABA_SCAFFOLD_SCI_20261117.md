# Result ADV-024: per-class GABAergic and inhibitory-scaffold transcripts in the held single-nucleus tables (SCI, 2026-11-17)

**n = 1 per arm, pseudo-replicated, a transcript is not function.** (a) is GSE158684, S-line hippocampus P17, one pool per genotype, nucleus unit. (b) is GSE334405, PV-Cre Scn1a neocortex, 3 against 3, a STATE CONTROL: its genotype is Scn1a, never a Wwox statement. Not medical advice. Reference genotype class only. Predictions frozen and hashed first: `c6/PREDICTIONS_6_GABA_SCAFFOLD_FROZEN_BEFORE_TABLES_SCI.md`, sha256 `77b63749990349b0f7df425ab47ee8899f1530cb10948118f53596f8ebac0be7`, commit `fe3a7c58a`, 20:29Z; run started 20:29:18Z. Held tables only; no retrieval, no download, no engine run.

## Answer first
1. **The organoid direction (GAD1 up, GABRB2 and GABRB3 down) does not appear per class in the S-line deletion** at this resolution. Gad1 inhibitory +0.09 and excitatory +0.09; Gabrb2 inhibitory -0.19, excitatory +0.02; Gabrb3 inhibitory +0.13, excitatory +0.07; every one is in the MIDDLE bin (frozen joint statement J1 false).
2. **The scaffold transcripts do not fall.** Gphn is up (inhibitory +0.37 [+0.21, +0.53], excitatory +0.21), Nlgn2 MIDDLE and slightly negative (-0.11, -0.18, intervals include 0), Arhgef9 slightly up (+0.11, +0.20). None is LOW; J2 false. This does not refute H1: its lever is protein and clustering, and a transcript can stay flat while the protein or the cluster falls.
3. **No GABA-A subunit is LOW in a neuronal class.** One is HIGH by the frozen edge: Gabra1 excitatory +0.42 [+0.27, +0.57]. Slc32a1 in the inhibitory class is HIGH +0.55 with an interval touching zero [+0.03, +1.12] on 34 and 56 expressing nuclei, the lowest-count readable row of the panel.
4. **Gad1 and Gad2 do not point in opposite directions** (+0.09, -0.05, both MIDDLE; J4 false). The panel says nothing about the protein-level mouse result (GAD65/67 lower, Hussain 2019); it reads the RNA arm only.
5. **The state control is flat.** In (b) every one of the 20 scored rows is MIDDLE (largest |C| = 0.35, Gad2 inhibitory), J3 false. So no state pattern was there for J1 to be confused with; and the panel has no organoid-like pattern in either set.
6. **Premise: kept, one correction.** The two held sources differ in level (organoid RNA, mouse knockout protein), so "opposite ways" is not a contradiction a transcript table can adjudicate. I added nothing and dropped nothing from the gene list.

## Rows scored and not scored
All 40 scored rows (20 per dataset) were readable (at least 30 expressing nuclei in each arm), including those I had given 0.35 to 0.55; see the score. Marker genes are read by the leave-one-out classification (LOO), default beside it; markers in a class they do not mark are shown for transparency and not scored.

### (a) S-line hippocampus P17, C = log2 KO over control (pooled nuclei; interval = nuclei bootstrap, pseudo-replicated)
| Gene | Excitatory C [95%] (expr. nuclei ctrl, KO) | Inhibitory C [95%] (expr. nuclei ctrl, KO) | Bin (exc / inh) |
|---|---|---|---|
| Gad1 (LOO) | not scored (+0.09 [-0.21, +0.37]; 222, 216) | +0.09 [-0.15, +0.30]; 129, 146 | / MID |
| Gad2 (LOO) | not scored (-0.15 [-0.63, +0.32]; 101, 93) | -0.05 [-0.30, +0.19]; 129, 148 | / MID |
| Slc32a1 (LOO) | not readable (25, 19) | +0.55 [+0.03, +1.12]; 34, 56 | / **HIGH** |
| Slc17a7 (LOO) | -0.33 [-0.43, -0.24]; 1099, 799 | not readable (18, 27) | MID (near edge) / |
| Gabrb2 | +0.02 [-0.08, +0.11]; 1384, 1136 | -0.19 [-0.45, +0.06]; 151, 178 | MID / MID |
| Gabrb3 | +0.07 [+0.02, +0.11]; 1591, 1395 | +0.13 [-0.08, +0.34]; 174, 229 | MID / MID |
| Gabra1 | +0.42 [+0.27, +0.57]; 670, 653 | +0.02 [-0.40, +0.45]; 95, 113 | **HIGH** / MID |
| Gabra2 | -0.27 [-0.35, -0.20]; 1456, 1234 | -0.01 [-0.38, +0.37]; 110, 167 | MID / MID |
| Gabra3 | +0.25 [+0.01, +0.48]; 272, 279 | -0.12 [-0.53, +0.34]; 60, 79 | MID / MID |
| Gphn | +0.21 [+0.16, +0.26]; 1584, 1403 | +0.37 [+0.21, +0.53]; 180, 239 | MID / MID |
| Nlgn2 | -0.18 [-0.39, +0.04]; 341, 265 | -0.11 [-0.58, +0.40]; 46, 52 | MID / MID |
| Arhgef9 | +0.20 [+0.13, +0.28]; 1229, 1114 | +0.11 [-0.16, +0.38]; 115, 145 | MID / MID |
Astrocyte rows (reported, not scored): Gabrb2 +0.56 [+0.13, +1.00] and Gabrb3 +0.61 [+0.34, +0.91] (83 and 155; 151 and 321 expressing nuclei), Gphn -0.13, Nlgn2 -0.20.

### (b) PV-Scn1a neocortex, per-animal mean of mutant minus control log2 (3 against 3; STATE CONTROL)
All 20 scored rows MIDDLE; C by gene, excitatory then inhibitory: Gad1 (LOO) not scored, -0.02; Gad2 not scored, +0.35; Slc32a1 not scored, -0.04; Slc17a7 +0.13, not scored; Gabrb2 0.00, +0.19; Gabrb3 +0.06, +0.01; Gabra1 +0.03, +0.06; Gabra2 +0.17, +0.23; Gabra3 +0.15, -0.02; Gphn +0.02, 0.00; Nlgn2 -0.08, -0.20; Arhgef9 -0.01, +0.07. Full tables: `snuc6_a_genes.tsv`, `snuc6_b_genes.tsv`.

## Score (nats, scored separately from every other line of this session)
Naive prior (frozen): readable 0.75, bins 0.10 / 0.80 / 0.10. Scorer: `score_6.py`, output `score6_output.txt`, `score6.json`.
| Set | Rows | Mine | Naive | Mine minus naive | of which readability | of which bins |
|---|---|---|---|---|---|---|
| (a) S-line | 20 | -17.685 | -14.375 | **-3.310** | -0.93 | -2.38 |
| (b) PV-Scn1a | 20 | -8.728 | -10.217 | **+1.489** | +3.80 | -2.31 |
Reading: in (a) my prediction was worse than the naive one. Two causes: I gave 0.35 to 0.55 to seven rows that all turned out readable (the thin inhibitory class of 190 to 260 nuclei still held at least 30 expressing nuclei for every gene except the marker Slc32a1 in the excitatory class, which was not scored), and I put 0.15 to 0.20 on LOW and HIGH for hypothesis-driven rows where the observed C was MIDDLE (non-MIDDLE rows were only 2 of 20, against my expected 4 to 5). In (b) the gain is only readability (high probabilities where naive said 0.75); the bin term was also worse than naive for the same reason (too much weight on HIGH). The panel therefore does not support the idea that this deletion's GABAergic RNA moves per class at P17 beyond a mild shift, and my 0.15 to 0.20 weights on LOW for the hypothesis rows were too high.

## What the result does not say
- One pool per arm: a pool-to-pool difference (age, litter, dissociation, capture) is not separable from genotype, and every interval is over nuclei.
- Composition differs between the two pools: oligodendrocyte share 22.5% to 7.8%, astrocyte 13.7% to 21.7%, inhibitory 6.0% to 9.0%, unassigned 0.9% to 3.9% (control to KO). Class membership is a marker argmax, so a class mean can move with composition; the astrocyte Gabrb2 and Gabrb3 rise (+0.56, +0.61) sits on a class that grew by half and is not scored, not interpreted.
- Slc17a7 excitatory -0.33 and Gabra1 excitatory +0.42 have narrow intervals but narrow intervals over pseudo-replicated nuclei are not evidence of a genotype effect; the same excitatory class shows Gabra2 -0.27, Gphn +0.21, Arhgef9 +0.20 with equally narrow intervals, a pattern more consistent with a pool-level offset than with gene-specific changes. I do not read it.
- A transcript is not a protein, not a cluster, not a current. LIVE1-H1 (a postsynaptic lever) is not tested by this panel.
- (b) is Scn1a: it is a state control, used here only to show that these twelve genes sit flat in an epileptic neocortex of a different genotype.

## For the transfer table (origin rows)
Where a tier-2 transcript row exists for one of these genes in the transfer table, the origin line is: GSE158684, S-line hippocampus P17, one pool per genotype, per-class C as above, MIDDLE except Gabra1 excitatory (HIGH) and Slc32a1 inhibitory (HIGH, interval touching zero), pseudo-replicated, RNA. For the organoid direction the line is: not reproduced per class in the neuron-specific mouse deletion at this resolution (Gad1 +0.09, Gabrb2 -0.19 inhibitory, Gabrb3 +0.13 inhibitory). No row should be marked "reproduced" or "refuted".

## Files and digests (sha256)
Scripts run: `c6/snuc_6_sline.py` `ac114cb99b33704fcc309645d91a3fbcd5d703100affefc883b43a31c1b73a0e`, `c6/snuc_6_neocortex.py` `56db0d6c77172369d151d82b9dc5c7bc22ffa552cf3fb1a4e74ed70f14c2183f` (as frozen). Outputs: `snuc6_a_genes.tsv` `5b7803ced1245b23741a4d20e78e3287835808663a7db8d99c7fcaa3e0fc1aea`, `snuc6_b_genes.tsv` `7b2a6fb3a324ae9ef9dc6211b7969833168e063580eb33b439f72b2ceefd3514`. Inputs: held files under `files/geo/GSE158684` and `files/deepening_downloads/gse334405_ctx` (digests in the frozen file).
