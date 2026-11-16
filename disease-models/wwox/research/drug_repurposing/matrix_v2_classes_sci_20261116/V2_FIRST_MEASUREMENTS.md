# Matrix V2: the first measurement that would give each column a thread (SCI, 2026-11-16; pre-registered before any v2 cell exists)

Non-canonical working note; mechanism matching only; no dose, no recommendation to use any agent; classes are labels. One line per V2 column (19), from `V2_FIRST_MEASUREMENTS.tsv`. Written BEFORE the v2 cells and before HE's rule v2 hash exists; it states what would turn a column from a class expectation into a held WWOX thread, and does not score anything.

| column | first measurement (one line) | where |
|---|---|---|
| sodium-channel blockers | burst-rate change (direction) under a sodium-channel blocker in KO neocortex against vehicle, two exposure levels | brief arm (sodium, AH1) |
| T-type calcium blockers | rebound-spike probability after hyperpolarising steps, with and without a T-type blocker, KO against wild type, plus burst rate under the blocker | brief arm (T-type); same cells as the sag measurement |
| SV2A ligands | paired-pulse ratio and evoked-EPSC amplitude before and after an SV2A ligand in KO against wild-type L2/3 cells (release-probability thread) | not in the brief; one added measurement |
| AMPA antagonists (competitive and noncompetitive) | isolated AMPA current removed and burst rate against it, with one competitive and one noncompetitive tool, in the same KO slices | brief arm (AMPA pair) |
| NMDAR pore blockers | burst probability against measured fractional NMDAR current removed by titration, KO and provoked wild type (HSCI-3 threshold shape) | brief arm (pore blocker) plus WO-10 |
| GluN2B NAMs | NAM-sensitive fraction of the isolated NMDAR current, KO against wild type at P13-P17, both regions (WO-10; F6 predicts >= 40%) | WO-10, first measurement of the brief |
| GABA-A PAM, synaptic-selective | sign of the burst-rate change under a synaptic-selective GABA-A PAM in KO neocortex (HSCI-2 predicts a RISE) and E_GABA at burst onset and end | brief arm (GABA-A PAM) |
| GABA-A neurosteroid / extrasynaptic | gabazine-sensitive tonic GABA-A current in KO against wild-type L2/3 cells and its response to a neurosteroid-type PAM | one added readout in the GABA-A arm |
| benzodiazepines | burst-rate sign under a benzodiazepine arm next to the non-benzodiazepine PAM, same slices | brief arm (benzodiazepine) |
| GABA-AT/GAT inhibitors | tonic current and extracellular GABA response to a GAT-1/GAT-3 blocker in KO against wild type (astrocytic transporters, HE H2) | one added arm in the GABA-A readout |
| Kv7 openers | XE991-sensitive current and the effect of a Kv7 opener on resting potential and burst rate in KO against wild-type L2/3 cells | one added arm; same cells |
| carbonic-anhydrase / multi-target | burst rate under a change of bath bicarbonate/CO2 (extracellular pH) against a carbonic-anhydrase inhibitor, KO against wild type | one added arm |
| valproate-type (breadth control) | H-HE-3 module transcripts (HK2, LDHA, SLC2A1) under a valproate-type label in wild-type against KO neurons | held-table replication plus one two-genotype transcript measurement |
| steroid / ACTH | glucocorticoid-receptor target-gene response to a corticosteroid label in KO against wild-type slice culture (Nr3c1 target genes) | not in the brief; slice-culture measurement |
| ketogenic diet | genotype-by-substrate interaction on burst rate (lowered glucose, added ketone body) in KO against wild type (H-ADV-2) | pilot extra arm, four animals per genotype |
| cannabidiol | burst rate under a cannabidiol arm at two exposure levels in KO against wild-type provoked | one added arm |
| fenfluramine-type (serotonergic / sigma-1) | effect of a sigma-1-modulating label on the isolated NMDAR current, KO against wild type (WO-10 extension) | WO-10 extension |
| HCN (Ih) blockers | HCN-blocker-sensitive current (Ih) amplitude and sag ratio, KO against wild-type L2/3, then burst rate under the blocker | same cells as T13 |
| neuroinflammation / IL-1 modulators | IL-1 pathway readout (Il1b, Il1r1 protein or transcript) in KO against wild-type tissue and slice supernatant at P13-P17; held tables do not detect Il1b, Il1a, Il6, Tnf or Ccl2 | held-table lookup done (below); then one measurement |

## Held-table lookup for the neuroinflammation sign (done now; no new data)
Reactive-glia markers are up in both laboratories' data: Gfap up in three neuron-deletion contrasts (e.g. hippocampus S 252.38 to 1096.26 TPM); Aif1 up (null 6.35 to 8.70 TPM; P47T CTX +0.65 log2, FDR 0.036; PFC +0.66, FDR 0.012); Cd68 up (hippocampus N 13.39 to 26.16 TPM; P47T PFC +0.46); Serpina3n up (cortex S 9.24 to 24.76 TPM; P47T CTX +0.81, FDR 0.047); Stat3 up. Homeostatic microglial markers are DOWN in the neuron-deletion tables (Tmem119 16.93 to 5.72 TPM in hippocampus N, 12.97 to 6.33 in S; P2ry12 16.34 to 5.89 in N) and unchanged in P47T. **Il1b, Il1a, Il6, Tnf and Ccl2 are not among the held rows or the P47T tested genes** (not detected at the depth of those tables, or filtered): the IL-1 axis specifically is NOT supported by held data; the general reactive-glia signature is, in two laboratories. INFERENZA: the column as proposed ('IL-1 modulators') rests on a generic gliosis signature, not on IL-1; the first measurement is therefore an IL-1 pathway readout. Cause against consequence remains open.

Cost of the whole list: no new data; one table lookup run now.
