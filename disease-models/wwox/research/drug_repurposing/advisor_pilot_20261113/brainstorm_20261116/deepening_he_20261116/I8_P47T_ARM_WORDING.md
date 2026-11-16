# I8 · the P47T arm, wording for the pilot brief (Addendum 6) (HE, 2026-11-16; non-canonical; mechanism level; not medical advice)

Written for: SCI (owner of the brief). Adds one genotype group to the pilot's existing slice recordings; no new assay, no new animals beyond the P47T group. No agent, dose or concentration appears here.

**Groups.** Wwox P47T/P47T knock-in (the line of the held GSE215425 tables), the null or neuron-deletion genotype as already in the pilot, and wild-type littermates. Same preparation and ages as the pilot (neocortex, layer II/III; P13 to P17 where the P47T line allows it; the age at which P47T animals can be recorded is not stated in any held table and is to be confirmed by SCI).

**Measure (already part of the pilot's whole-cell recordings).** Per recorded layer II/III pyramidal neuron, five features in this fixed order: (1) resting membrane potential; (2) input resistance; (3) sag at the pilot's fixed hyperpolarising step; (4) post-inhibitory rebound amplitude after that step; (5) action-potential amplitude of the first spike at rheobase. Per recorded fast-spiking interneuron (identified by firing, as the pilot does): (6) action-potential amplitude. The unit of analysis is the animal where the pilot's design allows, otherwise the cell with the animal as a stated cluster.

**Reading, fixed before recording (digest of this file pushed before the first P47T cell).** For each feature let D(null,WT) be the null-to-wild-type difference. The feature is **copied** if |P47T − null| < 0.5 × |D(null,WT)| and |P47T − WT| ≥ 0.5 × |D(null,WT)|; **not copied** if |P47T − WT| < 0.5 × |D(null,WT)| and |P47T − null| ≥ 0.5 × |D(null,WT)|; **intermediate** otherwise. A feature whose D(null,WT) does not exceed the pilot's own between-animal variability is declared **unreadable** and is not counted. The margin 0.5 is fixed here, before any P47T value exists.

**What the result decides (both directions).**
* A feature that P47T copies is reachable by the WW1 ligand-binding route (ASSUMED: P47 lies inside WW1, residues 16 to 49, and the mutation weakens PPxY binding; mRNA of Wwox is unchanged in the line). A feature P47T does not copy needs the protein itself or another route.
* The pattern of copied features separates the candidates: sag and rebound copied, AP amplitude not copied supports HCN1 (adaptor) and not Nav1.1 (shield); AP amplitude (pyramidal and interneuron), resting potential and input resistance copied supports the shield reading for sodium and potassium channels; all five copied supports a WW1 route for the whole null profile; none copied removes the WW1-PY route from the sag and rebound and from the amplitude.
* Consequence for the sodium-channel class and for AH1: see `I8_V2_ADDENDUM.md`, section AH1.

**Optional, no extra animals.** Where the P47T group is sacrificed for slices, the contralateral cortex can be used for cell-surface protein of HCN1, Nav1.1, Nav1.2 (Nav1.6 as the LPxY negative control) and Kv7.2 (no motif, negative control).

**Limits.** P47T is a missense line; loss of ligand binding is assumed, not shown. The pilot's variability sets what "copied" can mean; with few animals the classification will often read "intermediate" or "unreadable", and that is a valid result.
