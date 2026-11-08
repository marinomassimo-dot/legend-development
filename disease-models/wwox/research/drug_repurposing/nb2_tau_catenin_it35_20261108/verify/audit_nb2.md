# Blind audit NB2 (Tau + beta-catenin under GSK3 inhibitors of different class)

Source: PubMed abstracts via the PubMed tools (according to PubMed). Depth for every row: abstract only; no full text opened. Inputs read: evidence.tsv, queries.tsv only.

## Row verdicts

| Row | PMID | Verdict | Verbatim locator (abstract) | Note |
|---|---|---|---|---|
| R1 | 16014628 | SUPPORTED (system, inhibitors, readouts, "undetermined" split) | "induced the nuclear translocation of beta-catenin in Chinese hamster ovary cells and rat cultured neurons, in which a decrease in tau phosphorylation was observed" | SB415286: "induced the nuclear translocation of beta-catenin and slightly decreased Abeta production"; tau not stated, as producer says. Producer quote is 31 words (over the 25 cap). Inhibitor class labels (Mg-competitive, ATP-competitive maleimide) are not in the abstract (background knowledge). Ambiguity: "in which" most plausibly refers to the neurons but could include CHO. |
| R2 | 14511119 | SUPPORTED for the quote; cell type is ASTROCYTES (inferred, strong) | "compound SB216763 inhibited Tau phosphorylation at Ser396 and stabilized cytosolic beta-catenin" | The sentence sits inside the astrocyte passage ("In asynchronously proliferating rat cortical astrocytes ..."); the neuron passage starts only afterwards ("In cerebellar granule neurons ..."); MeSH carries Astrocytes. The abstract never states "in astrocytes" next to the SB216763 sentence, so inference, but I judge it astrocytic. Not a neuronal system: exclude. Lithium: no tau/catenin statement; divergence is MEK/ERK (producer correct). |
| R3 | 39798400 | SUPPORTED (readouts, quote, SH-SY5Y); two sub-claims NOT_IN_SOURCE | "41 up-regulated beta-catenin and neurogenesis-related markers (GAP43 and MAP-2)"; "decreasing the p-tau-Ser396 abundance" | "Western per earlier module document search" and "ATP-competitive-type" are not in the abstract. Single compound, single series: producer's "no" correct. |
| R4 | 33621689 | SUPPORTED | "GSK3 inhibitors, BIO, SB216763, and lithium, reversed the Tau 1 reduction by sodium arsenite" | beta-catenin: "a reduction of beta-catenin" in the membrane fraction after arsenite only; nothing about catenin under the inhibitors. Producer wording accurate. Inhibitor class labels not in abstract. Differentiated SH-SY5Y confirmed. |
| R5 | 26819000 | NOT_IN_SOURCE for system; otherwise SUPPORTED | "increased levels of beta-catenin, and decrease the DKK1-induced Tau phosphorylation at serine 396" | Abstract/MeSH give HEK293, not SH-SY5Y (the SH-SY5Y claim may come from ChEMBL, unseen). Not a GSK3 inhibitor paper (DKK1/LRP6): correctly excluded from the null. |
| R6 | 37235865 | UNVERIFIABLE / NOT_IN_SOURCE for system | "lowered levels of phosphorylated tau in a triple-transgenic mouse Alzheimer's disease model" | Abstract has no U2OS, beta-catenin-GFP, 4R1N, or high-content imaging; those come from a ChEMBL assay description I did not see. Single medchem series; no catenin in abstract. Not neuronal either way. |

## Absence claim: independent search

Strings (PubMed tool; the tool ANDs every term and maps "tau" oddly to a journal, so long strings collapsed to 0):
1. `tideglusib tau phosphorylation neurons` -> 6 hits (42320199 not opened; 38160617 review; 36868127 thiadiazolidinedione med-chem, p-Tau, no catenin; 33139110 review; 32955735 SH-SY5Y GSK3b/tau + tideglusib CSF, no catenin; 19523516 NP12 in vivo p-tau, no catenin). None meets the criterion.
2. `lithium SB216763 tau phosphorylation beta-catenin neurons` -> 33621689, 14511119 only (both already in the table).
3. `lithium Wnt reporter neurons tau phosphorylation glycogen synthase kinase` -> 16919965 (see below).
4. `(GSK-3 inhibitors) AND (phospho-tau OR tau hyperphosphorylation) AND (Wnt signaling) AND (cortical neurons OR hippocampal neurons OR neuroblastoma) AND (lithium OR CHIR99021 OR SB216763 OR AR-A014418)` -> 16919965 only.
5. `tideglusib OR TDZD-8 OR L803-mts tau beta-catenin neurons` -> 333 hits (the OR made it broad); first 15 are 2026 PMIDs, not screened by abstract (not read).
6. Zero-hit strings: `GSK-3 inhibitor tau phosphorylation Wnt TOPflash neurons`; `tideglusib[Title/Abstract] AND "tau" AND catenin`; `... kenpaullone indirubin ...`; `thiadiazolidinone ... TCF`.

Result: I found NO primary neuronal/neuron-like source showing a phospho-Tau readout AND a beta-catenin/Wnt-reporter readout under two or more GSK3 inhibitors of different class, at abstract level. Nearest misses:
- 16014628 (R1): LiCl and SB415286 both give nuclear beta-catenin in rat neurons/CHO; tau only for LiCl in the abstract. Full text unread; the null cannot be closed on it.
- 33621689 (R4): three inhibitors (two classes) on Tau 1; catenin only as the arsenite readout. Full text unread.
- OMITTED by the producer: 16919965 (Scali 2006, Neurobiol Dis). Cultured neurons: DKK1 lowers TCF reporter and beta-catenin and raises TAU hyperphosphorylation; lithium rescues in vivo. One GSK3 inhibitor (lithium), Wnt antagonist rather than a GSK3 inhibitor as the perturbation, so it does not break the null, but it is the only Wnt-reporter + tau + lithium neuronal paper I saw and belongs in the table.

Limits: abstracts only, PubMed only (no Europe PMC full-text, no Google Scholar, no ChEMBL); old papers (late 1990s-2000s GSK3 tau papers) often report catenin or tau only in the full text, so an abstract-level null is weak against them.

## Should the null be narrowed?
Yes. Say: "No abstract-level PubMed record in a neuronal/neuron-like system reports both readouts under two or more GSK3 inhibitor classes; two papers (16014628, 33621689) are unresolved at abstract level and need full text." Do not state it as absence of evidence in the primary literature. Also drop 14511119 from neuronal rows (astrocytes) and fix the unseen-source attributions in R5/R6.
