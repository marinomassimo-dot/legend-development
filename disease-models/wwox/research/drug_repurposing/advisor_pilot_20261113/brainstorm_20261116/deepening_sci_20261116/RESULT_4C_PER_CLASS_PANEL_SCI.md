# Result [4c]: the panel once per cell class in the S-line single-nucleus set (SCI, 2026-11-17; non-canonical; hypothesis level; transcripts only; not medical advice)

**Unit and region:** hippocampus, S-line (Synapsin-Cre neuronal Wwox deletion) against S-Control at P17; unit = the nucleus, pooled per genotype; **n = 1 animal or pool per arm**; bootstrap intervals over nuclei are pseudo-replicated; no significance statement. GSE158684 (HELD, `files/deepening_downloads/gse158684/`).
Written for: ADV, HE, IT (scorer of L12 to L15). Registration: `c4c/PREREGISTRATION_4C_PER_CLASS_PANEL_SCI.md` sha256 56bbfcf1..., `c4c/LEDGER_LINES_L12_L15_SCI.md` e3c5af92..., `c4c/snuc_4c.py` 80a70124..., sent to ADV at 02:21Z; one run, start 02:21:32Z, end 02:21:44Z (`run_start_4c.txt`); the push carrying these files had not landed. Genes already read in [4b] are marked 'seen' and carry no prediction.

## Table: C = log2 KO over control; [pseudo-replicated interval]; nuclei expressing control/KO; the bulk reading it sits next to
| Gene, class | C [interval] | expressing | bulk reading (S-line unless said) | what it does to the bulk-based reading |
|---|---|---|---|---|
| Slc12a5 (KCC2), excitatory (seen) | +0.01 [-0.11, +0.14] | 815 / 663 | -0.55 | no neuronal KCC2 transcript fall |
| **Slc12a2 (NKCC1), excitatory (L13)** | **-0.40 [-0.61, -0.21]** | 444 / 305 | -1.15 (mixed with oligodendrocytes) | neuronal fall is a third of the bulk one; I6 chloride-loading index stays withdrawn; NKCC1 transcript down, KCC2 unchanged |
| Slc12a2, inhibitory / astrocyte | -0.46 [-0.98, +0.05] / -0.27 [-0.77, +0.26] | 49 / 48; 65 / 98 | | same direction, wide |
| **Scn1a, inhibitory (L12)** | **+0.18 [-0.02, +0.39]** | 154 / 194 | none in the panel; P47T PFC -0.47 | **no Nav1.1 transcript fall in interneuron nuclei** despite the 25.9% AP-amplitude fall: that fall is not a transcript-level Nav1.1 loss (protein and surface level unmeasured) |
| Scn2a, inhibitory | +0.24 [+0.06, +0.44] | 141 / 181 | | no fall |
| Kcnk2, excitatory (seen) / astrocyte | +0.24 [+0.07, +0.42] / -0.37 [-0.67, -0.07] | 720 / 635; 168 / 237 | -0.83 | the bulk K2P fall is not neuronal; astrocytic only |
| Kcnk3, Kcnq2, excitatory | +0.22 [-0.21, +0.62] (63 / 63); +0.38 [+0.29, +0.47] | 1055 / 1004 (Kcnq2) | Kcnq2 -0.45 | **no transcript fall of a K2P, Kv7 leak candidate in excitatory neurons**: the 'loss of resting K+ leak' reading of the intrinsic profile (I8) has no transcript support here |
| **Hcn1, excitatory (L15)** | **+0.15 [+0.03, +0.27]** (dentate subset +0.89 [+0.48, +1.34]) | 1031 / 1055 | flat | small rise overall; larger in dentate granule nuclei (not neocortex) |
| Kcnj10 (Kir4.1), astrocyte | -0.51 [-1.01, +0.01] | 70 / 77 | +0.22 (not readable) | astrocytic Kir4.1 transcript lower at the edge of the interval (I16) |
| Gabrd, excitatory (seen) | -1.40 [-1.86, -1.00] | 160 / 49 | -1.67 | agrees (per neuron); dentate -1.56 with 29 KO nuclei expressing: just below the 30 rule |
| Gabra5, excitatory (seen) | -0.29 [-0.42, -0.16] | 926 / 719 | -0.54 | small fall |
| Gabrg2, excitatory / inhibitory | +0.07 [-0.03, +0.16] / +0.15 [-0.11, +0.45] | 1111 / 953; 110 / 140 | -0.35 (not readable) | **no gamma-2 transcript fall**: the phasic deficit (sIPSC -52%) is not carried by the transcript of the synaptic gamma subunit; read with brief 13.7 |
| Slc6a1 (GAT-1), inhibitory (seen) | -0.32 [-0.56, -0.08] | 149 / 178 | -0.94 | small fall |
| **Slc6a11 (GAT-3), astrocyte** | **-0.85 [-1.17, -0.49]** | 156 / 144 | not in panel | **astrocytic GABA transporter transcript falls**: relevant to the GABA supply behind the tonic current (I13) |
| Cck, Lamp5, inhibitory | +0.11 [-0.48, +0.70]; -0.38 [-1.11, +0.28] | 50 / 57; 33 / 35 | | readable, uninformative (wide) |
| Npy, Sst, Pvalb, inhibitory (seen) | not readable (24 to 49 nuclei expressing; Pvalb 13 / 9) | | | **the reactive-state axis cannot be read in interneurons in this set** |
| Grin2b, Grin2a, excitatory | -0.12 [-0.17, -0.08] (seen); +0.02 [-0.04, +0.09] | 1594 / 1363; 1551 / 1343 | Grin2b **-1.81** | **no neuronal NMDAR-subunit fall: the bulk Grin2b fall is not seen in neurons** (I3 sustainer) |
| **Cacna1i (Cav3.3), excitatory (L14)** | **-0.30 [-0.54, -0.08]** | 340 / 244 | -1.11 | a quarter of the bulk fall; dentate -0.67 (25 KO nuclei expressing: not readable) |
| Cacna1h, excitatory (seen) | +0.30 [+0.14, +0.46] | 549 / 546 | -0.46 | opposite to bulk |
| Wwox (control) | excitatory -2.78 [-3.18, -2.44]; inhibitory -3.40; astrocyte -4.00 | 496 / 81 | -2.56 | deletion visible in neuronal nuclei (and in glia: Synapsin-Cre expressed outside neurons, or ambient RNA; not resolved) |

## Ledger lines (scored by IT from `c4c/snuc_4c_genes.tsv`; values unrounded in brackets)
L12 Scn1a inhibitory +0.18 (+0.1803): middle bin (my 0.40; naive 0.8). L13 Slc12a2 excitatory -0.40 (-0.3988, 0.0012 above the edge, which belongs to the less extreme bin): middle bin (my 0.60; naive, the bulk reading carried over, 0.1 on this bin). L14 Cacna1i excitatory -0.30 (-0.3006): middle bin (my 0.40; naive 0.1). L15 Hcn1 excitatory +0.15 (+0.1460): middle bin (my 0.55; naive 0.8). Sum of log scores for me -2.94, for the naive rule -5.05; I lose to the naive rule on L12 and L15 (where its central bin was the right guess) and beat it on L13 and L14 (where it carried a bulk value over). **L13 sits 0.0012 from the edge:** its bin is decided by the registered edge rule, not by a measured difference.

## Reading, one paragraph
Of the bulk-based readings that decide open dossiers, the single-nucleus set reproduces the bulk value for one gene (Gabrd, per neuron) and **not for most others**: bulk Grin2b -1.81 against neuronal -0.12, bulk Kcnk2 -0.83 against +0.24, bulk Cacna1h -0.46 against +0.30, bulk Slc12a2 -1.15 against -0.40. The excitatory share of nuclei is unchanged (51.9% and 50.9%), so composition of excitatory neurons does not explain these gaps; the candidates are a different cohort and animals (bulk 2 to 3 against 2 to 4 animals per arm, this set n = 1 per arm: animal-to-animal variance is not estimable here), nuclear versus whole-tissue RNA, and non-neuronal expression of some genes. **The consequence for the dossiers is limited to what a per-neuron number says:** I3 (NMDAR sustainer), I8 (K+ leak, Nav1.1 transcript) and I6 (chloride index) lose their bulk transcript support in neurons at P17 in this set; I13 gains a supported neuronal Gabrd and Gabra5 fall and a new astrocytic GAT-3 fall; the reactive-state axis in interneurons is unreadable; the intrinsic profile still has no transcript explanation (post-translational, size or non-transcript causes are what remains, brief 13.2).

## Limits
n = 1 animal or pool per arm; the nucleus is the unit; marker-set classification; sparse counts (low-expression genes unreadable); transcripts only; P17 hippocampus (not neocortex, where bursts occur); many rows were read in several classes and no multiplicity correction is made; 'seen' rows were read before registration, so the comparisons in the reading paragraph that use seen genes (Grin2b, Kcnk2, Cacna1h, Gabrd) are not predictions.
