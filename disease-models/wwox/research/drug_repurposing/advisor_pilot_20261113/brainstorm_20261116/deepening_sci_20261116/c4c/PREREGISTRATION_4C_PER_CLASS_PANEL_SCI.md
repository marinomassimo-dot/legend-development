# Candidate [4c]: the panel once per cell class in the S-line single-nucleus set (GSE158684): panel and reasons, readability rule, predictions, ledger lines L12 to L15, written and hashed BEFORE any gene row of the new panel was read (SCI, 2026-11-17; non-canonical; hypothesis level; mechanism level; not medical advice)

**Unit and region (first line, as adopted):** hippocampus, S-line (Synapsin-Cre neuronal Wwox deletion) against S-Control at P17; the unit is the NUCLEUS, pooled per genotype; n = 1 animal or pool per arm (the paper's legend); intervals are bootstrap over nuclei and are pseudo-replicated; no significance statement is made on any row.
Written for: ADV (assigned it), HE, IT (scorer of L12 to L15). Same classification, same code path as [4b] (marker-set argmax, log2 of pseudobulk counts per million over nuclei of a class, classes excitatory, inhibitory, astrocyte, oligodendrocyte, microglia; dentate subset = excitatory nuclei with Prox1 above 0). The script is `snuc_4c.py` (the [4b] script with this panel; tested on synthetic matrices only).

## What I had already read (disclosed; no prediction is registered for these)
From the [4b] output (`snuc_S_line_GSE158684_genes.tsv`), I had printed the excitatory and inhibitory rows of: Gabrd, Gabra5, Gabra1, Slc6a1, Npy, Sst, Pvalb, Gad1, Grin2b, Kcnk2, Cacna1h, Slc12a5, Wwox, and all classes of Gfap and Gja1. Their values (excitatory, inhibitory, log2 KO over control): Gabrd -1.40, -0.52; Gabra5 -0.29, +0.16; Slc6a1 -0.02, -0.32; Npy +0.49, -0.04; Sst +0.65, +0.73; Pvalb -0.29, -1.20; Grin2b -0.12, -0.16; Kcnk2 +0.24, +0.18; Cacna1h +0.30, +1.17; Slc12a5 +0.01, +0.18; Wwox -2.78, -3.40. These rows appear in the [4c] table as already seen and are not scored as predictions. Every other row of the panel below is unread.

## Panel and why each gene decides a reading (class where it is read)
* **Chloride loading per neuron (I6):** Slc12a5 (KCC2; seen), Slc12a2 (NKCC1) in excitatory and inhibitory nuclei. Bulk NKCC1 reads oligodendrocytes (HE), so the bulk value of -1.15 is not a neuronal one.
* **Interneuron sodium channel (I8, AH1):** Scn1a, Scn2a in inhibitory nuclei (the interneuron AP amplitude falls 25.9% with unchanged rest, Breton Table 1).
* **Leak versus HCN reading of the intrinsic profile (I8):** Kcnk2 (seen), Kcnk3, Kcnq2, Hcn1 in excitatory nuclei; Kcnj10 (Kir4.1) in astrocyte nuclei (I16).
* **Tonic versus phasic components and GABA supply (I13):** Gabra5, Gabrd (seen), Gabrg2 in excitatory and inhibitory nuclei; Slc6a1 (seen) in inhibitory; Slc6a11 (GAT-3) in astrocyte nuclei.
* **Reactive-state axis (I13, DREAM-1b):** Npy, Sst, Pvalb (seen), Cck, Lamp5 in inhibitory nuclei.
* **Sustainer (I3, I7):** Grin2b (seen), Grin2a in excitatory nuclei. **T-type (I1):** Cacna1i (Cav3.3), Cacna1h (seen) in excitatory nuclei.
Wwox is reported as the genotype control, not scored.

## Readability rule (as in [4b])
A row is **readable** if at least 30 nuclei of the class express the gene (any count) in each genotype; otherwise 'not readable (detection)'. A change is called **meaningful in size** at |C| of at least 0.4 log2 (the bins below), with the pseudo-replicated interval shown beside it and no significance claimed.

## Predictions (bins on C = log2 KO over control: at or below -0.4 / between / at or above +0.4; probabilities sum to 1)
Excitatory nuclei: Slc12a2 0.25 / 0.60 / 0.15; Cacna1i 0.40 / 0.40 / 0.20; Kcnq2 0.25 / 0.60 / 0.15; Kcnk3 0.20 / 0.60 / 0.20; Hcn1 0.25 / 0.55 / 0.20; Gabrg2 0.25 / 0.60 / 0.15; Grin2a 0.25 / 0.55 / 0.20. Inhibitory nuclei: Scn1a 0.45 / 0.40 / 0.15; Scn2a 0.25 / 0.55 / 0.20; Cck 0.25 / 0.45 / 0.30; Lamp5 0.40 / 0.40 / 0.20. Astrocyte nuclei: Kcnj10 0.35 / 0.45 / 0.20; Slc6a11 0.30 / 0.50 / 0.20. Reasons are the held bulk readings (S-line bulk: Slc12a2 -1.15, Cacna1i -1.11, Kcnq2 -0.45; P47T bulk: Cacna1i -0.71, Scn1a -0.47 in PFC) discounted for composition, which [4b] showed to be large (oligodendrocyte share 22.5% to 7.8%).
**Ledger lines (to be scored by IT from the locator `snuc_4c_genes.tsv`, row gene and class, column C_log2_KO_over_ctrl; scored only if readable):**
* **L12** Scn1a, inhibitory nuclei: bins 0.45 / 0.40 / 0.15; naive baseline (no held bulk value for this gene in the panel table): the middle bin 0.8, 0.1 each elsewhere.
* **L13** Slc12a2, excitatory nuclei: 0.25 / 0.60 / 0.15; naive = the bulk reading carried over (-1.15): the lowest bin 0.8, 0.1 each elsewhere.
* **L14** Cacna1i, excitatory nuclei: 0.40 / 0.40 / 0.20; naive = the bulk reading carried over (-1.11): lowest bin 0.8, 0.1 elsewhere.
* **L15** Hcn1, excitatory nuclei: 0.25 / 0.55 / 0.20; naive = the middle bin 0.8, 0.1 elsewhere.
Bin edges: a value at an edge belongs to the less extreme bin.

## What each outcome changes (hypothesis level)
A per-neuron number is put next to each bulk-based reading: where the neuronal value is near zero while the bulk value is large (the L13 and L14 naive reading), the bulk reading is composition and the dossier statement is withdrawn for that gene; where it matches, the reading gains one dataset of n = 1 per arm. Scn1a in inhibitory nuclei at or below -0.4 would support the interneuron Nav1.1 reading of the AP-amplitude fall at the transcript level only (no protein). Nothing here moves a pilot arm by itself.
## Limits
n = 1 animal or pool per arm; the nucleus is the unit; marker-set classification; sparse 10x counts (low-expression genes will be 'not readable'); transcripts only; P17 hippocampus only (not neocortex); several genes are read in more than one class, so 'meaningful in size' rows are numerous by chance alone: no multiplicity correction is made and none is claimed.
