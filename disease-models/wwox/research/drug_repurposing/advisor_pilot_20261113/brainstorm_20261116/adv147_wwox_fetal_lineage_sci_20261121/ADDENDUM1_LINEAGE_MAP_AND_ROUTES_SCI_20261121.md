# ADV-147 addendum 1 (written after the route probes and before any WWOX or control value was read): lineage map and route results (SCI window X, 2026-11-21; hypothesis level; not medical advice)

The pre-registration is not edited; this addendum is dated after the route probes and before any gene value was extracted.

## Route results so far (UTC, plain HTTP client, no bypass)
* Route 1, CZ CELLxGENE Discover, 2026-11-21 about 15:20 to 15:30Z: the portal index and the gene-by-cell-type summary endpoint (WMG v2) are reachable (200). The unfiltered query returns pooled values across all ages and tissues. **Every query that filters on a development stage (fetal weeks, 'fetal stage', or an adult stage) returned HTTP 500 (Internal Server Error), five different filters tried**, so fetal data cannot be isolated through this route; the per-dataset route needs h5ad downloads of hundreds of megabytes to gigabytes and no h5py or scipy is installed. Dated route result, not a claim about the data. The portal index lists human fetal brain datasets (for example a second-trimester brain regions and cortical areas set, a mid-gestational neocortex set, a subpallial germinal zone and entorhinal cortex set), none used.
* Route 2, UCSC Cell Browser, same window: reachable (200). The dataset `cortex-dev` (Nowakowski 2017; 4,261 cells, 48 labelled clusters, gestational weeks about 5.85 to 37 in the metadata) was downloaded as its processed expression matrix (about 79 MB, TPM-scale values; sha256 prefix recorded in the job scratch) and its cell metadata. The Polioudakis 2019 atlas was not found as a UCSC dataset by name (a 'cortex-midgestation' listing exists; not opened).

## Lineage map (fixed now, from the cluster labels and counts only)
* Excitatory neurons: EN-PFC1, EN-PFC2, EN-PFC3, EN-V1-1, EN-V1-2, EN-V1-3, nEN-early1, nEN-early2, nEN-late.
* Inhibitory neurons (MGE, CGE and striatal lineage): IN-CTX-CGE1, IN-CTX-CGE2, IN-CTX-MGE1, IN-CTX-MGE2, IN-STR, nIN1, nIN2, nIN3, nIN4, nIN5.
* Inhibitory progenitors: MGE-RG1, MGE-RG2, MGE-IPC1, MGE-IPC2, MGE-IPC3, MGE-div.
* Cortical radial glia: vRG, oRG, tRG, RG-early, RG-div1, RG-div2, Glyc.
* Cortical intermediate progenitors: IPC-div1, IPC-div2, IPC-nEN1, IPC-nEN2, IPC-nEN3.
* Glia and other: Astrocyte, OPC, Microglia, Mural, Endothelial, Choroid.
* Excluded as unassigned: the blank label and U1 to U4.

## Measure (fixed now)
Detection fraction = share of cells in the group with a value above 0 in the processed matrix (TPM scale, so a zero is a non-detection, not a measured absence). Comparison: WWOX detection fraction per group divided by the median detection fraction of its matched controls (pool members within plus or minus 25 percent, relative, of WWOX's dataset-wide detection over the 4,261 assigned cells). Verdict row V2: ratio in inhibitory neurons divided by ratio in excitatory neurons; V3: ratio in radial glia and in inhibitory progenitors against excitatory neurons. Cluster-level fractions are also tabulated for the readers. 95 percent intervals: Wilson interval on each group fraction (a normal-approximation interval for the ratio is not used; ratios are reported with the Wilson bounds of numerator and denominator).
