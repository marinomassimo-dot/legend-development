# WWOX | Epalrestat checkpoint diagnosis

context_policy: QUESTION_DRIVEN

**Scope.** SCI_CODEX evaluated epalrestat as one compound from shared base badb23405. The [dossier](../drug_repurposing/continuous_compounds/epalrestat/README.md) compares polyol engagement, glycan occupancy and neural function.

| Dimension | Evidence and residual |
| --- | --- |
| Original coverage | Inspected Radenkovic Figs. 2 and 4 and original Supplementary Fig. 4, targeted Methods and Results, and clinical Table 1. Inspected the original 2024 PMM2 organoid Fig. 7A, Results and targeted extraction Methods. Scoped Iyer, Cortese and Ligezka work to their recorded captions, results and assay context. |
| Original comparison | The bulk AKR1B1 contrast stays negative under single-library omissions. Hippocampal excitatory nuclear assignments show 118 versus 68 UMI with one pool per genotype. The assigned inhibitory and astrocyte contrasts are smaller or differ in direction. |
| Sensitivity | A protonated 727 s feature barely met the blank floor. The marked increase appeared in the Aβ42 background and persisted with TIC and adjacent windows. The sodium-adduct query failed QC. Identity and sensitivity to sorbitol remain unresolved. |
| Independent evidence | The PMM2-CDG drug response changed pools and relative glycopeptide abundance. The tracer study used knockdown and could not distinguish GDP-mannose from UDP-HexNAc isotopologues. PMM2 organoids reverse the basal sorbitol direction seen in fibroblasts. The SORD comparison validates sorbitol suppression in a different disease mechanism. |
| Feasibility | PMM2 pediatric phase III stopped for futility. Official API snapshots returned no arm results, while the FDAAA tracker marks reporting. Pediatric total plasma precedent comes from one case. Unbound CNS exposure and tolerability under epilepsy polytherapy remain undetermined. |
| Reopening | Verify a basal WWOX neural polyol and glycosylation deficit, then compare identified engagement, time-resolved labeled donor and occupancy with physiological recovery. |

**DEFAULTS_TAKEN.** Used common-month clinical denominators where follow-up varied. Kept the exact-mass screen independent of group labels until QC was chosen. Used fixed-binding conversions as explicit scenarios. **STOP_LOG.** Conditional mechanism probe only. A further review of RNA or the unassigned peak would not supply compound identification or neural target-site exposure. The controlled PMM2-CDG results can be reassessed when arm-level tables can be independently verified.
