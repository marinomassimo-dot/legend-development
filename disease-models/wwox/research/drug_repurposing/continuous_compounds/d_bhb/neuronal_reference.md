# Does lower SLC16A7 survive a neuronal RNA reference?
Post hoc sensitivity check of the bulk result. The reference panel SNAP25, RBFOX3 and MAP2 samples neuronal synapses, nuclear identity and dendritic differentiation. For every biological library calculate log2(1 + SLC16A7) minus the mean log2(1 + reference gene expression); compare genotype means and omit one library at a time. This tests normalization sensitivity. The three markers are themselves potentially altered by WWOX and maturity, and a ratio cannot recover neuron counts or expression in matched individual human neurons.

| KO minus control, log2 scale | Unadjusted | Adjusted to three markers | Omit-one range, adjusted |
|---|---:|---:|---:|
| Mouse cortex | −0.96 | −0.95 | −1.36 to −0.56 |
| Mouse hippocampus | −0.93 | −1.16 | −1.55 to −0.77 |
| Human cerebral organoid | −0.40 | −0.06 | −0.25 to +0.14 |

In human organoids the adjusted estimates using SNAP25, RBFOX3 and MAP2 separately were +0.03, −0.43 and +0.23. The apparent human convergence is sensitive to the denominator. The stronger evidence is a mouse tissue and hippocampal-nucleus signal, with human transport capacity unresolved. The data also fit altered neuronal composition or maturation. The first discriminating human measurement is initial D-BHB uptake per viable maturity-matched neuron alongside surface MCT2, matched extracellular substrate and direct oxidation. A normal uptake would substantially weaken the proposed transporter bottleneck even if tissue-level SLC16A7 remains lower.

Run neuronal_reference.py from the worktree root with the archived files directory as its only argument. Output is neuronal_reference.tsv. It reuses the same transcript mapping and library selection as model_screen.py. [Bulk inputs and alternative mechanisms](exposure_transport.md)

**Human dataset access.** The BioStudies public API for E-MTAB-14792 returned HTTP 403 (study inaccessible) on 24 November 2026. A comparison within the relevant human cell state using the deposited raw data remains open. Check the author-released supplemental tables for usable per-state counts and donor replication; missing genes in a thresholded supplement would not be a negative expression result. The existing [access request draft](../../ebi_access_request_E-MTAB-14792_draft.md) is available to the operator. [Study](https://pubmed.ncbi.nlm.nih.gov/42397075/)
