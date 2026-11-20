# ADV-095 supply search: is a cortical cell-type-resolved Wwox-deficient deposit public? (SCI successor, 2026-11-20; ADV assignment; zero spend; plain clients; hypothesis level; not medical advice)

**Question (ADV).** Public single-nucleus or spatial data from cerebral cortex of any Wwox-deficient model; failing that, a Wwox neuron-targeted or conditional deletion with cortical cell-type data. It is the condition that would reopen the activity-dependent branch stopped in unit A3 (`ACTIVITY_BRANCH_RESULT_UNIT_A3_ADV095_SCI_20261119.md`: hippocampal nuclei show no activity-panel deficit in excitatory neurons, the deficit is a cortex bulk finding of -1.28, and no cortical nuclei deposit was held).

**Answer in one line.** None found by the routes below. What is public and cell-type resolved for a Wwox-deficient mouse is the hippocampal single-nucleus deposit GSE158684, which is held; every public cortical Wwox-mouse deposit is bulk RNA-seq. The only other cell-type-resolved Wwox-deficient data are human iPSC organoids (not cortex tissue; deposit not located). This becomes a supply need only if ADV wants the cortical nuclei: it would have to come from the authors of the Wwox neuronal-deletion mouse work (the deposit would be the cortex counterpart of GSE158684).

## Routes (dated 2026-11-20; plain HTTP clients with a generic client name, no contact parameter, no browser-header spoofing)
1. **GEO (NCBI E-utilities, db=gds, entry type GSE).** Terms: `Wwox` or `WWOX` alone (301 records, of which 39 are series; all 39 listed), `WOREE`, `SCAR12`, `WW domain-containing oxidoreductase`, each combined with single nucleus, single cell, snRNA, scRNA, spatial, Visium, nuclei, 10x, Cre, cortex, oligodendrocyte, hypomyelination; separate organism filters for rat and zebrafish (0 series each). The search is a text search over GEO metadata: a deposit whose metadata never names the gene (for example a knockout labelled by a line name) would be missed.
2. **ArrayExpress / BioStudies** (collection `arrayexpress`, query Wwox): 16 studies.
3. **PRIDE** (search by keyword Wwox and WWOX): 0 projects. **Zenodo** (Wwox with single-nucleus, snRNA, single-cell or spatial): 3 records, all glioblastoma cell lines.
4. **CELLxGENE curation API** (all 407 collections searched as text for wwox): 0 collections. **Broad Single Cell Portal** public search (Wwox, studies): 0 studies.
5. **Europe PMC** (title, abstract, full text index: Wwox or WWOX with single-nucleus, single-cell, snRNA-seq, scRNA-seq, spatial transcriptomics or Visium, with brain, cortex, neuron, hippocampus or cerebellum): 240 records read by title; the brain-relevant ones are in the table.

## What exists (every Wwox-related GEO series that involves brain, neural cells or neurons; the other 28 series are cancer, cell-line, SNP or unrelated)
| Accession | Species, model | What it is | Cortex? | Cell-type resolved? | Held in the repository? |
|---|---|---|---|---|---|
| GSE158684 | mouse, neuronal deletion (S-KO against S-Control), P17 | hippocampal nuclei, single-nucleus (3182 control, 2920 knockout nuclei, one pool per arm) | no, hippocampus | yes | **held** (`files/geo/GSE158684`, used in unit A2 and A3) |
| GSE158682 | mouse, neuronal deletion, P17 | cortex bulk RNA-seq, 3 knockout against 4 control | yes | no, bulk | **held** |
| GSE158681 | mouse, null and neuronal deletions, P17 | whole hippocampus bulk, 14 samples in three contrasts | no | no | **held** |
| GSE158685 | mouse | SuperSeries joining GSE158681, GSE158682, GSE158684 | | | its three subseries are held |
| GSE215425 | mouse, knock-in Wwox P47T/P47T against wild type (5 against 5) | bulk RNA-seq of prefrontal cortex, parietal cortex, hippocampus and cerebellum, 37 samples, processed table only | yes | no, bulk | **held** (`files/deepening_downloads/gse215425/`: processed table and series matrix); it is the object of the proteostasis screen (checkpoint I, section 4.4) |
| GSE156243 | human iPSC brain organoids | bulk, 6 samples | not tissue | no | **held** |
| GSE126075 | human neural stem cells, WWOX shRNA, before and after neuronal differentiation | CAGE, 4 samples | not tissue | no | **held** (`files/geo/GSE126075`) |
| E-MTAB-14948, E-MTAB-14949 | Drosophila heads, neuronal Wwox knockdown or overexpression with Abeta42 | bulk RNA-seq | not mouse cortex | no | not relevant to this question |

Not in a public repository by these routes: **PMID 42397075** (Brain 2026, "Disrupted WWOX-MYC interplay impairs neurogenesis in human brain organoids"; preprint DOI 10.1101/2024.12.22.630016, versions of 2024-12-25 and 2025-09-25). It reports single-cell transcriptomics of human iPSC-derived neural organoids (isogenic WWOX knockouts and patient lines) with radial glia affected and MYC raised. The data availability statement was **not reached**: bioRxiv returned HTTP 429 (error 1015) to plain GET on the page and on the JATS file, the journal article is not open access, and Europe PMC full text for the preprint returned HTTP 500. No GEO series of that title or with WWOX in its metadata carries single-cell data, so the deposit is either under a name without the gene, not yet public, or not deposited. This is a human organoid, not cortex tissue, and does not bear on the cortical question; it is recorded because it is the only cell-type-resolved Wwox-deficient data found beyond GSE158684.

## What is not available (by these routes)
- Single-nucleus, single-cell or spatial data from the cortex of any Wwox-deficient mouse or rat: none.
- Any conditional or neuron-targeted Wwox deletion with cortical cell-type data: none (the only neuron-targeted deletion deposits are the held GSE158681, GSE158682 and GSE158684).
- Rat (the Wwox-deficient rat with hypomyelination reported in the literature) and zebrafish: no GEO series.
- Wwox proteomics in PRIDE: none.

## What follows (for ADV; nothing here is a request to the operator)
1. The activity-dependent branch (A3) stays closed; the registered reopening condition (a cortical cell-type-resolved deposit) is not met by anything public.
2. If ADV wants the cortical nuclei, the supply need is: the cortex counterpart of GSE158684 from the authors of the neuronal-deletion mouse work, or a new single-nucleus run on cortex; this note names the need and decides nothing.
3. The held cell-type evidence for the oligodendrocyte lineage remains the one-pool-per-arm hippocampal nuclei with the ambient-RNA caveat (unit A2); the cell-level experiment named as the priority experiment of unit C is therefore not answerable from public data.
4. Next cheap check, if wanted: the data availability statement of PMID 42397075 by a route that is not rate limited (for example the journal supplementary page by plain GET once the rate limit clears).
