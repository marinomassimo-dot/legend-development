# WWOX | Carbamazepine checkpoint diagnosis

context_policy: QUESTION_DRIVEN

**Scope and verdict.** SCI_CODEX, sole compound carbamazepine, from shared base 460b22617. The [dossier](../drug_repurposing/continuous_compounds/carbamazepine/README.md) contains the decision and raw-data replay. The session self-evaluation returned PASS with historical declared gaps in PMIDs 30361190, 32000863, 34214506 and 35716775. Receipt verification returned 3604 anchored entries. Structural LINT gave warnings in existing science records. These procedures did not modify the four canonical science files. New receipts have targeted or selected-passage coverage, so there is no new complete deep-dive manifest.

| Dimension | Answer and evidence | Grade |
| --- | --- | --- |
| Original coverage | Fig. 3–4 of Schiebler, Fig. 7–8 of Lin and Table I–II of Riva resolve the selected comparisons. Abstract-only pediatric CSF data are kept as a lead and sensitivity scenario. | Partial |
| Contribution | The dossier separates an early reporter signal from loss of native cargo and tests an inositol-dependent branch alongside acute channel suppression. | Strong |
| Observations beyond the abstract | Lin Fig. 8 puts the absence of p62 reduction at 10 µM and 16 h. Riva Table I gives separate pediatric parent and epoxide. | Strong |
| Parity | All arms use primary tissue or cell context, concentration, time and reported replication. The studies span different tissues and eras and cannot support pooled estimates. | Partial |
| Sample units and interpretation | The macrophage block panel comprises three experiments from one donor. Bulk libraries and single-nucleus pools have separate units in the dossier. | Strong |
| Evidence levels | The positive control, contrary observation, in silico identifiability example and WWOX inference have distinct sections. | Strong |
| Claims and reopening | This research-layer disposition does not promote a claim. Reopening requires native lysosome-dependent cargo degradation and preserved PIP2/Kv7 and evoked inhibition at measured exposure. | Strong |
| Cross-query | Dataset reanalysis challenged a transporter bypass. Opposing HMIT primary results made compartment and state explicit controls. The old pediatric CSF dataset has a full-text acquisition gap. | Partial |

**Persistence.** FTR events dated 2026-11-27 with suffix 26 cover PMIDs 14749729, 19607714, 22216497, 24008736, 25535254, 35398096, 35984507, 36779245, 39507621 and 4064451. Two JATS copies are fingerprinted in the shared evidence directory. Individual clinical rows and source figures were kept out of the dossier. The durable output contains only published aggregate comparisons and derived data.

**Process.** The first Europe PMC acquisition of the Lin JATS timed out and NIH open data supplied the same publication. Other older pediatric papers remained abstract-depth leads. A self-check caught an author attribution error before the draft was staged and replaced the author with the first author on the paper. The weakest analytical answer was whether more reporter puncta meant more degradation. The persistent correction is the [two-compartment counterexample](../drug_repurposing/continuous_compounds/carbamazepine/replay_flux_identifiability.py) with an add-back-alone experimental arm and post-washout function. The independent-review criterion is the availability of paired native turnover and exposure with a contested denominator or assay sign. The study is bounded by the absence of those data. CHANGE = NONE for the harness itself.

```
ATTRIBUTION_CENSUS
incidents: 2
machine: 1   blind_auditor: 0   peer: 0   self: 1
severity_high: 0   of which self: 0
undetected_known: 0
```

**DEFAULTS_TAKEN.** Continued with licensed full-text sources and abstract-depth leads whose applicability is limited. No active peer duplication was identified. **STOP_LOG.** No operator-only stop. This compound checkpoint is closed with a reopening condition. The standing programme continues to the next eligible compound.
