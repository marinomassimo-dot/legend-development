# Session self-evaluation: IT22 (orchestrator, 2026-11-03)

## Scope and executable verdict
- Batch/session: ORCH-ROADMAP-IT22-20261103; analytical packages with 59 new receipts (11 TR agonists, 5 EZH2/glia, 5 stability probes, 17 batch1, 21 batch2).
- Receipt IDs: `FTR-20261103-*-01/-02/-03` (record order by event id; ledger 968 -> 1,027 chained).
- `session_self_eval.py --workspace . --disease wwox`: VERDICT PASS (declared gaps listed there belong to older PMIDs).
- Receipt verification: `fulltext_receipts.py verify` OK, 1,027 chained, tail anchored. Structural LINT: WARN (no BLOCK). `growth_anchors.py check`: PASS. `public_release_gate.py`: PASS, 0 blocks.
- Local verdict: PASS. Concurrent conditions: four background producers wrote only to their own folders; one battery on the frozen candidate (clone) ran while later work stayed out of that candidate.

## Content diagnosis
| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | No complete read anywhere: 59 receipts = partial text or abstract; figures and supplements not opened; the TR, EZH2 and stability dossiers say so per paper | partial | complete reads of the 3-4 decisive papers (Triac Trial I, Wang 2020, PMID 29132376, P252A) |
| Main message and original contribution | Corrections change selection, not the 980 generated rows; only the new Q8 input generated (20 rows); no hypothesis qualified | strong (stated) | none |
| Hidden gold beyond keywords/abstract | the hNPC gate failure sat in a results file and in no seed row; PMID 29132376 used DZNep/siEZH2, not GSK343 (found by reading) | strong | |
| Source parity | typed measures only; GtoPdb v ChEMBL pracinostat 47 v 5,113 nM unresolved (ChEMBL activities not in the local cache) | partial | reconcile the two sources |
| Team type, field density, observation v interpretation | seeds distinguish measured, inferred, hypothesised; cell composition never a gene seed | strong | |
| DATO / INFERENZA / IPOTESI / ESPANSIONE | every dossier tags the TR-alpha isoform and OPC-sign arguments as agent reasoning; engine-executed steps listed apart (generation_it22 README section 3) | strong | |
| Claims touched; revival triggers | IT21 P4a GSK343 counter-evidence reworded by correction note; BTK exclusion kept as `premise_contradicted` with a reopening condition | strong | Btk/Npy detection in the snRNA deposit never run |
| Multi-hop and corpus cross-query | blind-first reverse test over 6 cases by a separate actor; 5 general fixes, 3 did not hold | partial | |

## Persistence diagnosis
- Durable IDs: scope table, inputs builder, measures json, selection table, correction note, task record with evidence per objective.
- Reading debt: coverage_report and reading_state regenerated after the receipts (checks OK).
- Receipts: drafted by producers, validated with `--dry-run`, recorded by the integrator in event-id order; 11 TR receipts were rewritten after the validator refused their format.
- A future run distinguishes full text from abstract through each receipt's `source_kind` and `evidence_depth`.

## Process and capability diagnosis
- Skills/gates used: legend-start chain, mandate binding, independent verification (blind-first), reverse-test snapshot committed before analysis, release gate, freshness check, battery on a frozen clone.
- Declined: legend-locator-audit (no baseline claim narrowed); legend-discovery-method (not needed).
- Failures: `--no-v1` byte-identical regression after adding columns (caught by the machine test only when the cache env was set); malformed producer receipts; shareable audit refused two wordings (AhR agonist, EZH2 inhibitor as ChEMBL names); check_seeds refused a second guard tag; a mistaken assumption that a `<` on the other target is not comparable (verifier).
- Caught by: machine tests and validators for 5; the independent verifier for 8 (premise scope across clusters, work-done leak, BTK label, censored value, empty type, favourable type hiding a deficit, NRF2 novelty, '146 rows').
- Micro-upgrade shipped: dossier audit normalises each surface once (10m03s -> 25 s, identical report, cap unchanged) with regression; incremental engine runs (`--seeds-dir`, `--only`, `--reach-sets`); decision scope and typed attribution as code with tests.
- Residual risk and next decisive action: a measurement in a WWOX-deficient neural system (NRF2 protein/NQO1 activity; seizure-free neuron+OPC co-culture; KO-controlled WWOX blot) moves more than any further generation.

## Attribution census
```
ATTRIBUTION_CENSUS
incidents: 13
machine: 5   blind_auditor: 0   peer: 8   self: 0
severity_high: 1   of which self: 1
undetected_known: 0
```
(`severity_high`: a curated sentence on the failed-control count, "146 rows", would have reached the published dashboard; it was mine and the verifier caught it. `undetected_known` stays 0 because this wave has not yet had a later reader.)

## Capability scout
CHANGE = NONE for the registry. Gap observed and not shipped: producers must emit receipts in the ledger format and two attempts failed before the validator was consulted; reopen if it repeats (a producer-side template command would be the proportional fix).

## §21c output
`DEFAULTS_TAKEN` [] and `STOP_LOG` are in the task record ORCH-ROADMAP-IT22-20261103.
