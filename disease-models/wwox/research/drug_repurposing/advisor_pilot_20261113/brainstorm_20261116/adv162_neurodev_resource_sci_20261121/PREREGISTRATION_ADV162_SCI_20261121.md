# ADV-162 pre-registration: what NeuRoDev holds and where it touches LEGEND decisions (SCI successor Y, 2026-11-21; hypothesis level; adjacent reference resource; no dose; no contact; no e-mail address to any service; reference genotype class only; not medical advice)

Fixed BEFORE any Wwox row of any NeuRoDev table was read. Read when this was written: the figshare record metadata and the four README files (file list with sizes), the GitHub README and licence field, the documentation pages (network, analysis, mapping-sc, mapping-bulk; tool inputs and outputs), the bioRxiv abstract, and, in the repository's own held copy of Steinberg et al., Brain 2026 (PMID 42397075, accepted manuscript and supplementary files), a case-sensitive search for the resource's name plus the organoid cluster-identification paragraph and its references. No Wwox value of any NeuRoDev object has been seen.

## What is already established (route and size facts, not results)
* Paper: Zonca, Bot, Davila-Velderrain, Cell Reports 2026 (PMID 42213786, DOI 10.1016/j.celrep.2026.117374; preprint bioRxiv 10.64898/2025.12.16.694589 v1, 17 Dec 2025). Cell Reports and ScienceDirect: bot-challenge pages (403); Europe PMC: not open access; bioRxiv v1 PDF served once and then HTTP 429 (a result; one polite retry only).
* Figshare 30885428 (CC BY 4.0, 7.1 GB in total): the single large file is `counts.mtx.gz` (6.2 GB; never fetched). Compact: four .xlsx tables of pseudobulk and preferential expression per stage and per subclass for three reference networks (6.5 to 11.0 MB each, about 35 MB together), small .rds gene lists, four README files; the network objects (.rda, 91 to 198 MB each) need R, which this host does not have, and no R is installed for this task.
* Resource: human only (corticogenesis, neurogenesis and gliogenesis reference networks of cluster profiles; 948,350 cells, 14,110 genes; clusters from named source studies with age, stage, subclass); eTrace plots a per-cluster gene or gene-set score ordered over the network; `mapNetwork` takes normalised bulk profiles or per-cluster single-cell profiles and returns the position in the network, the nearest reference clusters, a subclass score and a stage annotation with a mapping confidence.

## What counts as "touches a decision" (fixed per consumer)
**Consumer 1, the cell-class and developmental-window premise (RP-042, RP-019, INV-15; against ADV-147 and ADV-157 pooled detection).**
* YES, a better unit exists: the compact tables give Wwox expression by subclass AND stage jointly (or a cluster-level table with named study, age and subclass is reachable within the size cap), with the number of clusters and source studies per cell stated or recoverable; and the premise classes (an interneuron subclass against glutamatergic subclasses; OPC and oligodendrocyte stages) are present.
* PARTIAL: only marginals (by stage alone, or by subclass alone); these are pooled aggregates of the same kind as ADV-147 and are not a better unit. They can still ADD a stage ordering or a class ordering, labelled as a pooled marginal.
* NO: Wwox absent from the 14,110 genes, or the classes of the premise absent.
* In every case: the unit is a cluster pseudobulk pooled across source studies (not a donor or sample); a donor-level unit is NOT available from the compact tables; I state the aggregation and do not call it replication. Expression (log-normalised pseudobulk) and any detection measure are kept apart. No ranking change from abundance alone.
**Consumer 2, the RP-043 organoid benchmark.**
* YES: Brain 2026 states that it mapped organoid clusters with this resource and prints a panel or table with the mapped identities.
* PARTIAL: used, but printed only as a figure panel without a table, or without per-line identities.
* NO: not stated in the paper or in the supplement. The text search result above (zero hits for the name in the main text and five supplement files) is a result for the held versions only, not for the published version; the identification is by comparison with four published human fetal datasets (references 32 to 35), and I record what the paper prints about cluster identity (12 clusters at week 16; Fig. 2A-D; Supplementary Fig. 3A-E).
**Consumer 3, a mapping step on public data only.**
* YES: a public, human, WWOX-deficient or control sample set (single-cell or bulk) exists whose cluster profiles can be built from a small public table, AND the mapping tool can run within a stated footprint (R and package installation: not done here; reported for HE's assessment, ADV-163).
* PARTIAL: a public sample exists but only a mouse or non-comparable one (the resource is human only; an ortholog mapping adds a species caveat), or the tool cannot be run without a heavy install.
* NO: nothing public and human.

## Premise check (operator's premise: the group is a computational partner of the Aqeilan group)
Source for the premise: the paper (authors, affiliations, acknowledgements) and the Brain 2026 manuscript. Shared scientific provenance (laboratory and authorship) is counted conservatively, as in RP-045: a NeuRoDev-based identity call on the Brain 2026 organoids would share provenance with the benchmark and is not an independent confirmation.

## Limits
Public sources only, lawful routes; a challenge, 403 or 429 is a result; no multi-gigabyte download (cap about 500 MB; the plan stays near 40 MB); no installation; no contact with any author or group; no e-mail address to any service. Adult-to-fetal references and the VWM, T3 and organoid adjacent readings are comparisons, not transfers. WWOX-specific evidence is kept apart from the reusable method or reference. Hypothesis level; not medical advice.

## Rejecting observation (named in advance)
If the stage and subclass tables disagree with ADV-147 on the ordering of the neuronal and glial classes for Wwox, the pooled detection fractions of ADV-147 are the thing to revisit; if they agree, they add nothing to the unit and the verdict is PARTIAL by rule.

## Consumer
ADV (decision on a developmental-reference unit), IT (RP-043 dated line), HE (ADV-163, mapping tool and licence assessment).
