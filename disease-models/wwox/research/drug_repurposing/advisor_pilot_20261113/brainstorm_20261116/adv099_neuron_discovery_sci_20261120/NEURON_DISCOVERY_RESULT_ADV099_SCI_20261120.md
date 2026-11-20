# ADV-099 unbiased neuron-internal discovery: result (SCI successor, 2026-11-20; hypothesis level; evidence, not a gate; no dose, no recommendation; not medical advice)

Registered text: `PREREGISTRATION_ADV099_NEURON_DISCOVERY_FROZEN_BEFORE_ANY_VALUE_SCI_20261120.md` (sha256 63faafa4912961209b040e7a0029382898d3d997544587b35229087bf312dde2), committed first (5d8f0536c764), then the script (5b615998331f; a 3,000-gene self-test was run first and its values were not read), then one registered run (about 36 seconds; `out/`). Held data: hippocampal nuclei `GSE158684` (neuronal deletion, P17, one pool per arm; excitatory 1,596 control and 1,262 knockout nuclei, inhibitory 246 and 293 by the unit A3 class rule) and human organoid bulk `GSE156243` (2 control, 4 knockout libraries, two groups of knockout libraries, clonal identity not stated); 12,209 genes matched by upper-cased symbol and analysed in both. **A blind recompute from the pre-registration text alone reproduced the verdict (section "Blind recompute" below).**

## Registered verdict
**NOTHING_REPLICATES_BEYOND_CHANCE in all four cells.** The stop rule written by ADV applies: nothing replicates, so the mapping steps (Hallmark enrichment, druggability, agent classes, endpoint placement) were **not run** and no new candidate class is named.

| Neuron class, direction | nuclei pass (centred 0.25, stable) | organoid pass (0.5, group agreement), among analysed in both | observed replicated | null mean | null 97.5th percentile |
|---|---|---|---|---|---|
| excitatory UP | 1,503 | 353 | 79 | 85.3 | 101 |
| excitatory DOWN | 1,532 | 109 | 25 | 24.1 | 33 |
| inhibitory UP | 1,177 | 352 | 63 | 63.0 | 77 |
| inhibitory DOWN | 1,072 | 114 | 15 | 17.2 | 25 |
In every cell the observed count equals the count expected when the organoid values are shuffled among genes of similar expression. The 182 gene rows in `replicated_genes.tsv` (79 + 25 + 63 + 15; 15 flagged "glial-enriched in nuclei") are therefore what chance gives at these thresholds, not a discovery; they are kept as the registered output and are not candidates.

## Post hoc descriptive checks (labelled; not registered; no claim)
- Across all genes analysed in both systems the centred nuclei coefficient and the centred organoid coefficient have Spearman correlation -0.028 (excitatory, 6,776 genes) and -0.025 (inhibitory, 6,719 genes) against a permutation spread of about 0.011 to 0.012; sign agreement is 48.3 and 48.7 percent. There is no positive shared signal at gene level; a very small negative one is present and is not interpreted.
- Bulk corroboration of the chance-level lists is inconsistent and not independent: for the nuclei-UP excitatory genes the hippocampal bulk contrast (the same neuronal-deletion line as the nuclei, so not an independent system) has the same sign in 56 of 79, the cortical bulk contrast in 22 of 79; for the DOWN genes 7 of 25 hippocampal and 17 of 25 cortical. The two bulk deposits disagree with each other.
- Genes present in the lists of both neuron classes in the same direction (33 UP, 8 DOWN: for example Epha4, Dlgap4, Nfasc, Prrc2b among UP; Agfg2, Cpne4, Dnajb4, Esco1, Ndufaf2, Pibf1, Snx2, Swt1 among DOWN) come from the same pool of one arm, so the agreement of the two classes is not an independent replication. Listing is for the record only.

## Blind recompute (fresh delegate, sonnet asked and read back at effort high on 8 turns, 14,004 output tokens; report as delivered in `BLIND_RECOMPUTE_REPORT_AS_DELIVERED_ADV099_20261120.md`)
The delegate read only the frozen pre-registration and the held data and implemented the rule in its own code. **Same registered verdict in all four cells (NOTHING_REPLICATES_BEYOND_CHANCE) and the same stop rule.** The counts differ because the pre-registration leaves choices open (glial marker panels, the 99th-percentile pool, merging of 35 duplicated mouse symbols, the split-half details, the unassigned nuclei); none changed the verdict.
| Quantity | Producer run | Blind recompute |
|---|---|---|
| excitatory nuclei, control and knockout | 1,596 and 1,262 | 1,676 and 1,401 |
| inhibitory nuclei, control and knockout | 246 and 293 | 268 and 364 |
| organoid pass UP / DOWN among genes analysed in both (excitatory table) | 353 / 109 | 354 / 110 |
| replicated UP / DOWN, excitatory | 79 / 25 | 72 / 25 |
| replicated UP / DOWN, inhibitory | 63 / 15 | 71 / 18 |
| null mean (97.5th percentile), excitatory UP / DOWN | 85.3 (101) / 24.1 (33) | 79.3 (94) / 23.6 (32) |
| null mean (97.5th percentile), inhibitory UP / DOWN | 63.0 (77) / 17.2 (25) | 63.1 (77) / 18.2 (26) |
| Spearman, centred nuclei against centred organoid effect, excitatory / inhibitory | -0.028 / -0.025 | -0.047 / -0.056 |
Delegate sensitivities (not registered, no verdict claimed): group agreement on median-centred differences gives 73/25 and 74/18; without the stability condition the replicated count is 72/25 (excitatory) and 95/25 (inhibitory), with no null run for that variant. The delegate did not run a null excluding the glial-flagged genes, did not rerun with other seeds, and did not map the replicated genes (nothing exceeded the null). The class assignment differences (unit A3 classes against its own glial panels) bear on the nuclei counts, not on the organoid side, which agrees to one gene.

## What cannot replicate here (power and design, stated plainly)
The nuclei have no biological replication (one pool per arm; genotype confounded with pool and library; the ambient-RNA depth shift was removed by centring, not by modelling). The organoid is bulk at 15 weeks with a maturity lag, 2 control and 4 knockout libraries, human, a cultured line. The thresholds (0.25 in log2 CPM units for sparse nuclei data, 0.5 in the organoid) were fixed before the data. A neuron-internal change that is cell-type-specific, protein-level (a WW-domain protein acts through interactions, not necessarily through transcripts), small in effect, or present in one system only cannot be detected by this design. "Nothing replicates beyond chance" is the absence of evidence in these two systems, not evidence that no neuron-internal lesion exists.

## Data that would show it (named, as the stop rule asks)
1. A **neuron-resolved organoid deposit** (the single-cell data behind PMID 42397075, Brain 2026; not located in a public repository by the routes of the supply note; the preprint page was rate limited): with it the replication could be run cell-type to cell-type.
2. A **cortical or hippocampal single-nucleus deposit with animals as units** (at least three animals per arm), so that neuron-class effects have biological replication.
3. **Protein-level or phospho-level data** from the neuronal-deletion brain (a published tandem-affinity interactome of the WWOX protein, PMC6300487, listed by title in a repository search; it is not held in files/fulltext (checked by name); an interaction-level lesion would not appear in these transcripts).
4. A second independent neuron-containing transcriptome of a Wwox-deficient human system (a second parental line, or clonal knockouts).

## What this does to the programme
It removes no candidate and adds none. The broad objective stays as unit C left it (no convincingly preferable candidate; oligodendrocyte-lineage support as the testable class; neuronal re-expression rescuing downstream consequences together argues the lesion is neuron-internal, and this screen finds no replicated transcript lesion in the held neuron-containing systems). The next available analysis that could change the choice and needs no new data is **protein-interaction-level**: crossing a WWOX interactome (the published tandem-affinity list and any held interaction record) with druggable targets and the HE sheets; it is a proposal, not started.
