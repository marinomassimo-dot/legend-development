# IT16 P0 — diagnosis of the effective capability (2026-11-01)

Question: along *WWOX knowledge -> question -> usable data -> method -> hypothesis -> comparison -> next verification -> queue*, what is declared, implemented, executed, measured as an advantage, and still lacking a validation? Size of the catalogue, number of hits, tools and tests do not measure predictive capability and are not used here as evidence of it.

Sources: `roadmap_current.md` (R1-R12), the README "Stage of the capability" table (historical snapshot, P7 gold set "not started"), the IT13-IT15 packages, the IT15 final report, and the baseline checked at the start of IT16 (`main` = `development/main` = `1cda3d2a`, CI success, one worktree, no active job, IT15 mandate COMPLETE). Cells say `not diagnosed` where this session did not look.

| Stage | Declared | Implemented | Executed | Advantage measured | Validation missing |
|---|---|---|---|---|---|
| Catalogue and identity | R2 | adapters (ChEMBL, GtoPdb, ...), name reconciliation | yes, IT7-IT15 | error counts only (7 false "not found" from name errors, IT15) | no rate of wrong identity per source; 35+22 failed REST attempts in IT15 not yet turned into a cache |
| Compound-target-action | R2/R5 | relations tables, action field | yes | none beyond coverage | action sign is source-declared; no independent check of direction |
| Quantitative pharmacology | R5 | graded same-document comparison (IT15), missing-condition rule (IT16 P1.1) | yes on 3 tables (40 / 1,037 / 60 groups) | changed interpretation of 4 real cases (IT15); P1.1 moved Q-A 492 INTERPRETABLE -> 0 | no accuracy against primary papers; descriptions rarely state voltage/agonist, so the grade mostly says LIMITED |
| Networks and models | R1/R3 | typed WWOX subnetwork, ToolUniverse optional | partly (IT13-14) | not diagnosed this session | no held-out contrast |
| Perturbations (LINCS etc.) | R3 | iLINCS adapter, signature census | yes (P6, GSE156243) | INCONCLUSIVE, confound named | no independent contrast |
| Phenotype-first | R4/R6 | cross-system analyses, needs | yes | not diagnosed this session | - |
| Contexts | R4 | context fields in needs/cards | partial | none | missing-vs-discordant not systematically separated |
| Hypothesis generation | R6 | target-first Q-A/Q-B (IT15), deepened cases | yes | WWOX contribution counted (IT15 P6): question, endpoint, premise limit, direction conflict | no outcome that the module did not itself produce |
| Evaluation | R3/R7 | nothing standing: no gold set exists and none was invented | no | none | **the principal bottleneck**: without outcomes independent of the module no step above can be called predictive |
| Scouting | R9 | scout_daily.py, capability log | yes (daily) | not measured | channels GitHub/Hugging Face/Nature not all explicit (IT16 P6) |
| Presentation | R10 | full view + shareable edition | yes (local) | none | site not online; shareable shows a count of the 10 cases |
| Continuity | R12 | mandate record, stop hook, mandate_watch, process_wait | yes | IT15 ran to COMPLETE | resumption from checkpoint and report-verify-next handoff not yet shown as a single trace |

Principal bottlenecks, by decision they block: (1) no independent outcome set, so predictive claims stay at "capability of the process"; (2) condition-poor assay text, so most pharmacology comparisons can only be LIMITED until a primary paper is opened; (3) source fragility (REST errors, truncation), so repeated work; (4) guidance that sits in the roadmap and in my private memory but is not linked from the role contracts, so an Orchestrator or Scientist has no guaranteed path to it.

What to remove or simplify is recorded in the iteration section of the module README at close (complexity ledger), not predicted here.
