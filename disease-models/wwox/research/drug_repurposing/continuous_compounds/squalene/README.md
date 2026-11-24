# Squalene · substrate supply during developmental myelination

The question is whether adding squalene can bypass inadequate synthesis by FDFT1 while leaving sufficient downstream capacity to form sterols and a first myelin sheath. A shortage of SQLE activity would instead limit use of added substrate.

## Untreated WWOX comparison

For each original library, subtract log2(FDFT1 expression + 1) from log2(SQLE expression + 1), then compare the genotype means. [Code](entry_balance.py) takes the repository root, local files directory and output TSV path as arguments. [Results with single-library omissions](entry_balance.tsv). Mouse cortex (4 controls/3 knockouts) gave −0.641 log2 units, mouse hippocampus (2/3) −0.047 and human organoids (2/4) +0.128. The hippocampal sign changed after omitting one library. The opposing cortex and organoid signs persisted. These descriptive contrasts neither localize a cell type nor measure catalytic reserve, metabolite transport or flux. Cross-species expression scales, cell composition and developmental stage preclude pooling. No common directional signature supports a single entry bottleneck.

## Discriminating prediction and decision

At matched intracellular tracer availability in WWOX-deficient and corrected cultures, a substrate shortage predicts that labelled squalene contributes to newly synthesized downstream sterols and increases first ensheathment of previously bare, viable axons. Measure absolute newly formed sterol alongside fractional labelling, comparable axonal firing and surviving lineage cells, and evoked conduction. Include vehicle with identical carrier. Intracellular tracer accumulation without increased downstream product suggests a conversion bottleneck. More labelled sterol without improved ensheathment argues against the developmental rescue hypothesis. A response confined to microglia after addition of myelin debris would support a separate repair mechanism.

Active for preclinical appraisal. A developmental PLP1 mouse comparator was identified (supplementary Fig. 4, DOI 10.1038/s41593-026-02489-5). The [supplementary figure check](plp1.md) distinguishes early changes in sheath pathology from first ensheathment. The EAE/macrophage experiment addresses repair after inflammatory injury (PMID 33349711). These are retrieval leads. No pediatric central exposure or WWOX treatment response established in this checkpoint.
