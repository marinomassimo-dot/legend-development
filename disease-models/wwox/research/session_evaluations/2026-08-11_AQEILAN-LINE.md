# Session evaluation — Aqeilan line, PMIDs 27308416 / 25491415 / 26256646

## Scope and executable verdict

- **Batch/session:** three orchestrator-assigned, previously unread Aqeilan-line papers.
- **Receipts:** `FTR-20260811-27308416-01`, `FTR-20260811-25491415-01`,
  `FTR-20260811-26256646-01`.
- **Executable verdict:** `session_self_eval.py` initially failed on an orphan false positive for
  the existing `LIT-0333`/`CORPUS P333` landing. The shared record-ID predicate was corrected and
  two regressions added; the rerun passes. All three manifests pass STRICT with zero gaps under
  `main@d06a4a1`, against `<REPO_ROOT>/files/`. Receipt verification is
  `96 chained receipt(s)`, tail anchored. Structural LINT passes.
- **Declared global debt:** six unchanged `UNREAD PREMISE` records and legacy manifest gaps remain
  visible. They do not arise from this batch and were not hidden or widened.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| 1. Sequential full text, figures, tables, supplements | 27308416: whole commentary, 10 refs, 1/1 panel; 25491415: whole review, 48 refs, 2/2 panels; 26256646: every section, Table 1, 57 refs, 15/15 panels. `supplementaryFiles` was the first retrieval gesture for each; no supplement exists. | strong | The 26256646 JPEGs are only 700 px wide; all panel claims retain that ceiling. |
| 2. Read against disease-label grain | The batch is metabolism/oncology rather than CNS. The outcome is low transfer, not forced neurological relevance. | strong | No neurodevelopmental DATO was created. |
| 3. Hidden gold beyond gene keywords | The decisive findings do not depend on gene-name hits: unequal 3/5-week endpoints (Methods), exact `p=0.05` against `P<0.05` (Fig. 3/Methods), absent Figure 4 significance marks, and the review's reversed intervention direction. | strong | The paper cannot disclose an unrounded LM7 p-value. |
| 4-6. Group and evidence type | PubMed: Aqeilan 137 papers, 64 WWOX-title/abstract papers. Experimental primary gene group, not a primary WWOX-DEE disease group. Observation and interpretation were weighted separately; commentary/review create no independent data. | strong | Same-group continuity is not replication. No group-inexperience error was inferred; the observed errors are source-transmission/internal-direction defects. |
| 7. Field density | WWOX-HIF1A 4; WWOX-RUNX2 11; WWOX-osteosarcoma-metastasis 5 (PubMed ESearch, 2026-08-11). | strong | Sparse fields increase the cost of duplicating one primary through its review/commentary. |
| 8-10. Epistemics and cross-surface checks | 26256646's RUNX2 claim is `INFERENZA`; revival requires direct RUNX2 perturbation/occupancy/reporter. Text was separated from panel pixels, and the 254 PDF was screened `UNDECIDED` and refused rather than normalised. | strong | No claimed contradiction rests on a PDF text layer. |
| 11-15. Compounding | Three immutable receipts, three manifests, three dossiers and one candidate landed. All 115 references were enumerated; gene-direct PMIDs were deduplicated. Corpus links: `CORPUS-STUB-078/LIT-0101`, `CORPUS P333/LIT-0333`, `CORPUS-STUB-152/LIT-0169`, `FT-047`, CLAIM 009/028 context. | strong | Primary PMID 25012504 remains an explicit unread premise in meta metabolism and must be read before it bears more weight. |
| 20. Main message / original contribution / hidden gold | 27308416: author commentary on HIF1alpha glycolysis (opening body; Fig. 1). 25491415: synthesis plus explicit absence of authenticated SDR substrates (steroid section); hidden gold is the directional/transmission fault. 26256646: WWOX rescue reduces metastatic behaviour (Figs. 1-3); hidden gold is that RUNX2 was never directly tested and Fig. 4 does not support blanket transcript claims. | strong | Source parity governs promotion. |
| 21-23. Source parity, team class, skills | Commentary and review were treated as synthesis; the primary paper as new data. Recency was not used as a quality proxy. `legend`, deep-dive, self-eval, capability-scout and takeaways gates were used; `find-fulltext` was declined because complete structured sources existed. | strong | The PDF skill affected only the required font refusal. |
| 24-25. Durable and mechanically recoverable state | Each manifest names source, SHA-256, coverage, supplement state and exact locators; `reading_state.md`, `coverage_report.md` and `batch_queue.md` were regenerated from the 96-event ledger. | strong | Canonical scientific promotion is deliberately deferred to BATCH_COMMIT. |
| 26. Friction | Europe PMC refused a supplementary archive for PMC4935230; main figures were persisted from the structured HTML's CDN links. The first self-eval then exposed the incomplete record-ID population. Both failures occurred before final handoff. | strong | The non-OA refusal is recorded, not retried into ambiguity. |
| 27. Capability delta | `session_self_eval.py` now uses one record predicate that recognises `LIT-*`, `CORPUS P*` and `CORPUS-STUB-*` in the registries it already scans; two regressions prove those landings pass while incidental PMID prose still fails. | strong | Tooling change must be reviewed/merged separately from the scientific read. |

## Persistence diagnosis

- **Durable landing:** receipt ledger plus the three schema-v2 manifests and dossiers; promotion
  instructions are in `CC-20260811-AQEILAN-LINE-01`.
- **Queue/debt:** close only the 27308416 and 26256646 components of `FT-047` at BATCH_COMMIT;
  28123895 and 21444760 were not opened. PMID 25012504 remains a declared unread premise.
- **Future reconstruction:** the receipts distinguish complete full text from abstract, name the
  exact structured artifact fingerprints, section coverage, 1/1 + 2/2 + 15/15 image budgets and
  `supplementary: not_present`.

## Process and capability diagnosis

- **What caught failure:** the mandatory executable self-evaluation, not author judgement.
- **Micro-upgrade shipped:** registry-native identifiers now satisfy the landing gate through one
  disease-agnostic predicate; tests cover `LIT` and `CORPUS` independently.
- **Residual risk:** a structured source can place its ref-list inside evidentiary body text. This
  run avoided all bibliography-derived locators; the `_xml_surfaces` correction remains owned by
  Plan and was not touched.
- **Next decisive action:** operator/Plan applies the candidate through BATCH_COMMIT and reads primary
  PMID 25012504 before relying further on the secondary HIF1alpha papers.

Not medical advice.
