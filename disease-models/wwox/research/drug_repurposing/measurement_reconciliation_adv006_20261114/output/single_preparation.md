# Which single preparation would close the most rows of `closes.tsv` (ADV-006, producer P)

Non-canonical. Not medical advice. Described, never commissioned: no wet work is requested, authorised or urgent. "Closes" is read from `closes.tsv` (13 rows: IT42-Q01..Q03, IT40-Q03, WO-14, WO-15, WO-16, WO-17, IT46-Q01, IT46-Q04, IT46-Q10, IT47-Q04, IT53-Q01).

## The preparation
**Mouse, Synapsin-Cre neuron-deleted neocortical acute slices, layer II/III pyramidal cells, P13-P17, Cre-positive wild-type, heterozygote and knockout littermates analysed separately with the animal as the unit, as the two nested cohorts SCI47 Phase 0 states** (a perforated-patch cohort: E_GABA, native-chloride sIPSC, mIPSC, evoked IPSC, puffed agonist; a whole-cell cohort: high-chloride sIPSC with antagonist-defined identity, Rs, Cm, Rin). Measurements M01, M02, M03, M04, M05, M07 of `measurements.tsv`. It is the preparation of the only published inhibitory datum (34634460; SCI42 and SCI47 both state it) and the one CLAIM002 section 6 already specifies for E_GABA.

## What it closes (Phase 0 only, no drug)
| Rows | Closed fully | Closed partly |
|---|---|---|
| IT42-Q02 (E_GABA, M05) | yes | |
| IT42-Q03 (sIPSC re-record, M01) | yes | |
| WO-14 (heterozygote versus wild type, M01 with arms separated) | yes | |
| IT46-Q01 (E_GABA against rest, threshold, input conductance, M05 + M07) | yes | |
| WO-15 (NP3P2: receptor- or release-limited, M02 + M04) | | partly: the same-cell triad of NP3P2 (isolated NMDAR current, sIPSC charge) is in no inhibitory-thread table |
| IT46-Q10 (sIPSC, evoked IPSC, reversal "in the same cells") | | partly: the same-cell wording conflicts with the two-cohort structure (CF05b) |
| WO-17 (resting potential, M-current, NMDAR current, sIPSC in the same slices) | | partly: the two currents are outside Phase 0 |

**Four rows fully and three partly, of thirteen.** If the pH of the same slices were added as a separate (non-patch) measurement (M22), IT42-Q01 would be a fifth fully closed row; the sources give it as a measurement in the burst preparation, with its own instrument.

## What it would not decide
* **The subtype question (L2 wording, WO-16, IT53-Q01):** a heterologous matched-beta series (M21), a different preparation entirely; no slice recording answers it. The ADV-004 wording constraint for L2 stays as it is (pointer: `gabaa_subtype_adv004_20261114/README.md` answer 6).
* **IT42-Q01 (pH):** a bath and tissue pH measurement (M22) in the GluN2B thread; the patch recordings do not measure it.
* **IT46-Q04 and IT40-Q03 (the drug arms):** Phase 1 and the glutamate-current half of IT40-Q03 are conditional on Phase 0 and outside it.
* **IT47-Q04 (OPC contribution):** needs identified NG2-cell recordings; none of the cohorts.
* **Anything needing another cohort:** ages other than P13-P17 (M08, with the survivor-selection control); the global knockout or P47T and CA3 (M14, the August candidate's preparation); hippocampus (M13); human neurons (M28); tonic current (M06) and interneuron counts (M09), which SCI42 lists and SCI47 does not; correctability.
* **Within the cohort:** whether E_GABA is primary or secondary to bursting (needs M11 or the burst-status stratification, which cannot be recorded with a glutamate-receptor block at the same time: CF03); the native-chloride sIPSC and the low-chloride sIPSC are different configurations (CF01); the same-cell structure of CF05a.

## Competing explanations
1. **Consolidation is possible at the recording level.** SCI42 M01, M03, M04, M05, M06 and SCI47 Phase 0 (i)-(v) are the same six recordings under different names (crosswalk), and one cohort pair holds them.
2. **Fragmentation is partly correct.** The arms test different biology (supply, postsynaptic response, chloride handling, network state, a heterologous receptor series, tissue pH) and some cannot share a preparation: the heterologous series and pH are different instruments; the drug arms are conditional on Phase 0 (D7); the burst-state arms and the glutamate-block artefact control exclude each other in one slice (CF03).
3. **The two ways of grouping do not disagree on the core**, they disagree on conditions (conflicts CF01, CF04, CF05a/b) that no package can adjudicate because none holds a recording; the choice between native-chloride (perforated) and pipette-set chloride sIPSC changes how an amplitude fall is read.
4. **Pre-existing specification:** the E_GABA recording is already specified twice in August (CLAIM002 section 6 for this preparation; CC-EGABA-EXPERIMENT/ANALYSIS-PLAN/CLOSURE for the global-allele preparation). Neither SCI42 nor SCI47 cites them (grep of the two package folders outside `inputs_it46/`).
