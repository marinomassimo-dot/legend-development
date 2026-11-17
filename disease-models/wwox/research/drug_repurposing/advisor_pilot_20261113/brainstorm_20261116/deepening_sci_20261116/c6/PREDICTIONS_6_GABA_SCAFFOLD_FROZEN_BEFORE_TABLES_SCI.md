# Predictions: per-class GABAergic and inhibitory-scaffold transcripts in the held single-nucleus tables (ADV-024; SCI, 2026-11-17; written and hashed BEFORE the per-class values are computed; hypothesis level; transcripts only, not function; not medical advice)

**Unit and sets (first line):** n = 1 per arm, pseudo-replicated. (a) GSE158684: S-line hippocampus, P17, one pool per genotype, the unit is the nucleus, intervals over nuclei are pseudo-replicated. (b) GSE334405: PV-Cre Scn1a F/+ against +/+ neocortex, 6 months, per-animal pseudobulk 3 against 3, STATE CONTROL: its genotype is Scn1a, never read as a Wwox statement, no Wwox information in it. A transcript is not function. Reference genotype class only.

**Question (ADV-024):** per class, log2 KO over control of Gad1, Gad2, Slc32a1, Slc17a7, Gabrb2, Gabrb3, Gabra1, Gabra2, Gabra3 and the postsynaptic inhibitory scaffold genes Gphn, Nlgn2, Arhgef9 (the LIVE1-H1 lever). Does the human organoid direction (GAD1 up, GABRB2 and GABRB3 down; Steinberg 2021, CLAIM 002) appear per class in the neuron-specific mouse deletion, and do the scaffold transcripts fall?

## What was and was not seen before this file (stated, not hidden)
The two matrices were opened by this session on earlier days for other genes (panels [4b], [4c], [4d], [5]); the per-class values of the twelve genes here were never computed or read. The class-marker genes Gad1, Gad2, Slc32a1 and Slc17a7 entered the earlier classification, and class shares were seen; none of their per-class KO over control values was. Both matrices' byte digests were taken for the record (below); that reads no values.

## Rules (as [4c] and [5], fixed here)
- Classes: marker-set argmax (excitatory Slc17a7, Slc17a6, Camk2a; inhibitory Gad1, Gad2, Slc32a1; astrocyte Aqp4, Gja1, Slc1a2, Aldh1l1; oligodendrocyte Mbp, Plp1, Mog, Mobp; microglia Cx3cr1, P2ry12, Csf1r). Classes read: excitatory, inhibitory, astrocyte (astrocyte reported, not scored).
- READABLE in a class: at least 30 nuclei expressing the gene in each arm (in (b), summed over animals per group). A non-readable row is reported as non-readable, never as a value.
- C = log2 of KO (or mutant) CPM over control CPM per class (pooled counts in (a); mean of per-animal values in (b), pooled value beside it). Bins: C below -0.4 LOW, -0.4 to +0.4 inclusive MIDDLE (edge goes to MIDDLE), above +0.4 HIGH.
- **Circularity control, stated before the run.** Gad1, Gad2, Slc32a1 define the inhibitory class and Slc17a7 is a marker of the excitatory class, so the per-class value of a marker in its own class is attenuated by selection (a nucleus that lost the marker moves class). The four marker genes are therefore read by the LEAVE-ONE-OUT classification (the tested gene removed from its marker set; variant LOO) and that value is the scored one; the default-classification value is reported beside it. Marker genes in the other classes are ambient RNA and are reported, not scored.
- Premise note: the two held sources differ in level (human organoids RNA, GAD1 up; mouse systemic knockout hippocampus protein, GAD65/67 lower; Hussain 2019). A per-nucleus transcript cannot adjudicate a protein finding; the result is read as the RNA arm of the question only.
- Genes: none added, none dropped. Gabra3 and Slc32a1 may be non-readable in the small inhibitory class of (a) (about 190 control and 260 KO nuclei in the earlier composition); this is predicted below, not a reason to change the list.
- Scripts: copies of `c5/snuc_5_sline.py` and `c5/snuc_5_neocortex.py` with only the gene list replaced, the LOO variant added for the four marker genes, and (a) the dentate block removed; digests below. No engine run, no retrieval, no download.

## Digests stated before the run (sha256)
| File | sha256 |
|---|---|
| c5/snuc_5_sline.py (original) | 9e93a25f8705cddc94033c60ee970cffaeedef25e507518a5cb72d312b90b903 |
| c5/snuc_5_neocortex.py (original) | 2921da8ca80b1eba77df6ad313882c84bf1806eb340a6aaa2db11f6817a2ba6f |
| c6/snuc_6_sline.py (run) | ac114cb99b33704fcc309645d91a3fbcd5d703100affefc883b43a31c1b73a0e |
| c6/snuc_6_neocortex.py (run) | 56db0d6c77172369d151d82b9dc5c7bc22ffa552cf3fb1a4e74ed70f14c2183f |
| GSE158684_ctrl_filtered_matrix.mtx.gz | 1b5e2de95eef52a45dd1bc5794c8bf5c8df04c793b2d6610704ad020929bd8c3 |
| GSE158684_ko_filtered_matrix.mtx.gz | aa422129d7ba922aa1e11b125b192256bacef455066461ac2ccaa266cdc428a7 |

## Naive prior (stated)
For every scored row: P(readable) = 0.75; given readable, LOW / MIDDLE / HIGH = 0.10 / 0.80 / 0.10 (the share of MIDDLE in my earlier S-line panel [4c] was 18 of 22 readable excitatory and 12 of 14 readable inhibitory rows, 9 of 12 in the neocortex panel [5]; those rows were other genes in the same tables).

## Scoring
Per scored row two terms, in nats: the natural log of the probability given to the observed readable or non-readable state, plus, if readable, the natural log of the probability given to the observed bin. The same two terms with the naive prior. Sum over scored rows; report my total, the naive total and the difference, separately for (a) and (b) and separately from every other line of this session. Rows not scored: astrocyte, oligodendrocyte, microglia, and a marker gene in a class it does not mark.

## Predictions, mine (IPOTESI)
Rows give P(readable) then LOW / MIDDLE / HIGH given readable. Where a row has no hypothesis-driven reason, the generic bins are 0.10 / 0.80 / 0.10 in (a) and 0.08 / 0.72 / 0.20 in (b) (the neocortex panel [5] gave 3 HIGH of 12; one genotype pair of three animals each).

### (a) S-line hippocampus P17 (n = 1 per arm, nucleus unit)
| Gene | Excitatory | Inhibitory |
|---|---|---|
| Gad1 (LOO) | not scored | 0.97 / 0.15 / 0.65 / 0.20 |
| Gad2 (LOO) | not scored | 0.97 / 0.20 / 0.65 / 0.15 |
| Slc32a1 (LOO) | not scored | 0.85 / 0.10 / 0.80 / 0.10 |
| Slc17a7 (LOO) | 0.97 / 0.10 / 0.80 / 0.10 | not scored |
| Gabrb2 | 0.90 / 0.20 / 0.65 / 0.15 | 0.55 / 0.20 / 0.60 / 0.20 |
| Gabrb3 | 0.95 / 0.20 / 0.65 / 0.15 | 0.70 / 0.20 / 0.60 / 0.20 |
| Gabra1 | 0.70 / 0.10 / 0.80 / 0.10 | 0.80 / 0.10 / 0.80 / 0.10 |
| Gabra2 | 0.80 / 0.10 / 0.80 / 0.10 | 0.40 / 0.10 / 0.80 / 0.10 |
| Gabra3 | 0.40 / 0.10 / 0.80 / 0.10 | 0.35 / 0.10 / 0.80 / 0.10 |
| Gphn | 0.97 / 0.18 / 0.70 / 0.12 | 0.90 / 0.18 / 0.70 / 0.12 |
| Nlgn2 | 0.85 / 0.20 / 0.66 / 0.14 | 0.55 / 0.20 / 0.66 / 0.14 |
| Arhgef9 | 0.80 / 0.18 / 0.68 / 0.14 | 0.60 / 0.18 / 0.68 / 0.14 |

### (b) PV-Scn1a neocortex, 6 months, 3 against 3 (STATE CONTROL; not a Wwox statement)
| Gene | Excitatory | Inhibitory |
|---|---|---|
| Gad1 (LOO) | not scored | 0.99 / 0.15 / 0.65 / 0.20 |
| Gad2 (LOO) | not scored | 0.99 / 0.15 / 0.65 / 0.20 |
| Slc32a1 (LOO) | not scored | 0.97 / 0.08 / 0.72 / 0.20 |
| Slc17a7 (LOO) | 0.99 / 0.08 / 0.72 / 0.20 | not scored |
| Gabrb2 | 0.98 / 0.08 / 0.72 / 0.20 | 0.95 / 0.08 / 0.72 / 0.20 |
| Gabrb3 | 0.98 / 0.08 / 0.72 / 0.20 | 0.95 / 0.08 / 0.72 / 0.20 |
| Gabra1 | 0.95 / 0.08 / 0.72 / 0.20 | 0.97 / 0.08 / 0.72 / 0.20 |
| Gabra2 | 0.95 / 0.08 / 0.72 / 0.20 | 0.80 / 0.08 / 0.72 / 0.20 |
| Gabra3 | 0.50 / 0.08 / 0.72 / 0.20 | 0.70 / 0.08 / 0.72 / 0.20 |
| Gphn | 0.99 / 0.08 / 0.72 / 0.20 | 0.98 / 0.08 / 0.72 / 0.20 |
| Nlgn2 | 0.95 / 0.08 / 0.72 / 0.20 | 0.90 / 0.08 / 0.72 / 0.20 |
| Arhgef9 | 0.95 / 0.08 / 0.72 / 0.20 | 0.90 / 0.08 / 0.72 / 0.20 |

### Joint statements (not scored in the nat total; stated so they cannot be moved afterwards)
- J1: in (a), in either neuronal class, with all three rows readable: Gad1 HIGH and Gabrb2 LOW and Gabrb3 LOW together (the organoid direction per class). P = 0.02.
- J2: in (a), at least two of Gphn, Nlgn2, Arhgef9 LOW in the same neuronal class, readable. P = 0.12 for inhibitory, 0.12 for excitatory.
- J3: the J1 pattern in (b). P = 0.03. If J3 holds, J1 loses its specificity (a state pattern, not a Wwox one).
- J4: in (a), Gad1 and Gad2 in the inhibitory class point in opposite directions (one LOW, one HIGH). P = 0.04.

## What each outcome would change
- J1 holds in (a) and not in (b): the first per-neuron transcript hint that the organoid GABAergic direction survives in a neuron-specific deletion; still one pool per arm, still RNA, no function.
- J2 holds: transcript-level support for a lowered postsynaptic scaffold, the H1 reading of the LIVE1 lever, still not a protein or puncta statement; its absence does not refute H1 (the lever is at protein and clustering level).
- Both absent in (a): the organoid direction does not transfer at the RNA level to this deletion at P17; it does not decide the protein-level mouse result.
- Readable-state results also tell the brief which classes can be read at all in these tables.
- No outcome changes a need, a card, a direction or a ranking by itself.

## Limits that travel with any result
One pool per arm in (a): every interval over nuclei is pseudo-replicated and a sample-to-sample batch difference is not separable from genotype. A class is a marker argmax, so a composition change moves nuclei between classes. Counts of lowly expressed receptor genes in a class of a few hundred nuclei are noisy. (b) is Scn1a, never a Wwox row.

## Result
Run 2026-11-17 20:29Z; see `RESULT_6_GABA_SCAFFOLD_SCI_20261117.md` (frozen text above unchanged; frozen at commit fe3a7c58a, sha256 77b63749990349b0f7df425ab47ee8899f1530cb10948118f53596f8ebac0be7). Score: (a) -3.310 nats against naive, (b) +1.489.
