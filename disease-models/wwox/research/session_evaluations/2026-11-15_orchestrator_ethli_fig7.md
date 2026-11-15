# Session self-evaluation: Fig 7 quantification of PMID 32000863 (orchestrator as SCI, 2026-11-15)

Non-canonical. Process diagnosis. Not medical advice.

## Executable verdict
`session_self_eval.py --workspace . --disease wwox`: see the record `ledger/tasks/orchestrator/ORCH-ETHLI-FIG7-20261115.json` (battery evidence is recorded there at landing).

## Content diagnosis
| Dimension | Answer | Grade | Debt |
|---|---|---|---|
| Prior work checked first | IT6 and the cards read Fig 7b by eye; IT15 verified Fig 7c only; the 2026-09-07 pilot holds the panel map. The peer's pointer to the pilot arrived mid-task and changed nothing in the extraction but supplied the contradiction check. | sound | none |
| Vector before pixels | The lithium panels were found to be vector only after the page was inspected with PyMuPDF; ethosuximide is raster only. The lattice test (all 726 vector means on k/N) validated the calibration without any outside reference. | sound | none |
| Raster accuracy | Null panels: two files agree to 0.004-0.025 stage, controls read 0.00 to -0.02, lattice 0.06-0.10 step. The 7d raster run against the vector truth is biased low by up to 0.15 stage under heavy marker overlap; the +/+ and +/- 7b series have no equivalent protection. | bounded, stated | an unquantified error on the wild-type 7b series |
| Inference | "Between-animal differences persist across minutes, so the upper-limit standard error is closer" is mine, not measured; the answer to question (1) is therefore given as bounds. | weak, labelled INFERENZA | a per-animal table would settle it |
| Verification | no blind verifier | weak | an independent re-extraction by another actor |
| Consumption | `consumer_delta.md` (six rows); the pilot's "genotype-specific ethosuximide" wording is the first candidate for correction | pending | benefit unproven until IT consumes it |

## Process diagnosis
* My first raster run failed three times for configuration reasons (x labels, legend window, panel row range) before producing numbers; each failure was visible, none produced silent wrong values. The bias of the 7d raster run was found only because the vector truth was available; without it the same bias would have been carried into 7b unseen.
* Nobody outside this session has checked the extraction yet.

## Micro-upgrades (the answers)
Extraction, validation and analysis scripts with `--help`, input digests and a lattice check that works as a calibration test on any integer-score time course.

## Residual debt
A generic figure-series tool (consumer_delta row 6, not built); an independent re-extraction; the authors' per-animal table, which would replace this extraction.
