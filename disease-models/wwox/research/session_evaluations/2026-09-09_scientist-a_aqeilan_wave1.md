# Batch self-evaluation — `scientist-a`, `AQEILAN-FT-A-001` wave 1, 2026-09-09

## Scope and executable verdict

- **Batch/session:** Aqeilan free-full-text sweep, wave 1 of a lot of 8. Two PMIDs dispatched: `34268881`, `33914858`. Reading mode `PRIMARY_EVIDENCE_READ`.
- **Studies and receipt IDs:** `34268881` → `FTR-20260909-34268881-04` (`partial_fulltext_read`, `new_question_outside_prior_coverage`). `33914858` → **no receipt, and none was due**: never acquired.
- **`session_self_eval.py`:** `PASS` — receipts 134, complete_fulltext_events 66, active_complete_reads 55, unread_premises 4/4 (at baseline, no regression).
- **Per-study manifest:** `PMID34268881.json` → `PASS`, 0 gaps, schema v2, 18 locators, artifacts + SHA-256 + exact text locators verified. No manifest for `33914858` — correctly, there is no artifact to fingerprint.
- **Receipt verification:** `OK: 134 chained receipt(s), tail anchored`.
- **Structural LINT:** `PASS` — **after I fixed a defect of my own that it caught**; see Process below.
- **Local verdict:** wave objectives met on paper 1; paper 2 parked with cause.
- **Workspace/global and concurrent conditions:** three actors share this checkout. Peer files (`PMID29724996`, `PMID20530675`) were dirty throughout and were **never touched**; all commits were path-scoped through the `flock` wrapper. Peer receipts transiently held `BLOCK_BATCH_COMMIT` (`UNRESOLVED_OUTPUT_FILE`) twice during the session; both cleared when the peers landed their candidates. Not my defect and not mine to fix.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | `34268881`: abstract, introduction, all Results subsections, Discussion, Limitations and Methods read from the fingerprinted PMC XML; Appendix `s004.docx` read in full; Figure 4 inspected at native resolution and panel H re-rendered at 400 dpi from the fingerprinted PDF. **Only Figure 4's pixels were inspected**, so `coverage.figures` is `captions_only`, not `read`. | `partial` | Deliberate. Ten figures uninspected **in this event**; the 2026-08-14 receipt covers all 69 panels and its coverage is **not inherited**. |
| Main message and original contribution | Stated in the dossier addendum §4–6: brain organoids model WOREE; the AAVS1 rescue is **marker-selective**, normalising TBR1/SATB2 and overshooting CTIP2. | `strong` | — |
| Hidden gold beyond keywords/abstract | Two finds neither the abstract nor any prior locator carried: the Figure 4H WT-vs-rescue bracket, and the fact that **`Appendix Table S1` is distributed while Appendix Figs S1–S6 are not**, recovering exact P-values for four of six missing figures. | `strong` | — |
| Source parity: context, type and recency | Both papers are Aqeilan-lab CNS primaries, 2021. Field density measured with dates: `WWOX` 707, `WWOX AND epilepsy` 66, **`WWOX AND myelin` 8**, **`WWOX AND oligodendrocyte` 4**, `Aqeilan RI[au]` 137 (PubMed, 2026-09-09). | `strong` | — |
| Team type, field density, observation vs interpretation | Aqeilan is **primary for the gene, not for the WOREE clinical phenotype** — weighted accordingly. The seam was kept explicit: the authors' *"recovered"* is reported as theirs; the overshoot is the panel's. | `strong` | — |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Dossier §6 types each carried statement. The non-monotonic dose idea is `IPOTESI` with `PREMISE: DEFAULT_FROM_TEXTBOOK` and a `REVIVAL_TRIGGER`, **not** a claim. | `strong` | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 002` (*consolidated baseline*) narrowed on the layering endpoint only → `CC-20260909-34268881-01`, change class MINOR. `CLAIM 032` composes with it as the opposite bound (lower threshold vs upper). `CLAIM 003`'s primary source (`33914858`) **remains unread**. | `partial` | `FT-044` open and now ALTA. |
| Multi-hop and corpus cross-query | **Weak.** The 91-item reference list was counted, not enumerated, in this event; `references: not_read`. Corpus cross-query was targeted (claim registry for rescue/organoid claims) rather than systematic. | `partial` | Declared in the receipt rather than glossed. |

## Persistence diagnosis

- **Durable IDs / wikilinks:** `FTR-20260909-34268881-04` · `CC-20260909-34268881-01` · `DL-THER-105` · manifest `entries[12..17]` · `FT-044` update · task contract `WAVE_1_RESULT`.
- **Reading queue / debt:** `FT-044` updated with the 19-tier cascade, the human-actionable routes, and the instruction that **any fresh copy must have its text layer re-tested, not assumed clean**. Appendix S1–S6 debt declared on `34268881`.
- **Dossier and commit candidate:** both written and committed (`da08cb9`, `6ce4128`).
- **Receipt fingerprint, coverage, supplements:** `source_fingerprint` = the XML's SHA-256, re-derived byte-identical. `supplementary: not_read` chosen **conservatively** — the Appendix was read in full, five of eight files were not, and the coarse enum has no honest middle; the precise account is in `evidence_basis` and in two supplement-surface locators.
- **Can a future run distinguish full text from abstract only?** Yes, three ways: the receipt's `evidence_depth` and coverage map; the manifest's fingerprinted `source_artifacts` with per-locator `surface`; and — new today — `evidence_presence.py`, which says whether the bytes behind those fingerprints are even present.

## Process and capability diagnosis

- **Skills / gates used:** duplicate-work gate per paper (`fulltext_receipts.py status`); `deepdive_manifest.py` strict; `legend-locator-audit` (R4, mandatory here); `legend-session-self-eval`; `find-fulltext` cascade (delegated); `legend_lint.py`; `session_self_eval.py`; `growth_anchors.py`.
- **Skills deliberately declined, with reasons:** `legend-deepdive` — the paper already had a complete-coverage reading; running the full pipeline again is the duplicate work the gate forbids. `legend-paperqa` — **external spend, reserved**. `legend-hypothesis-forge` and `legend-safety-triage` — no molecule and no therapeutic candidate matured here; an overshoot on a patterning marker is not a lever. `legend-discovery` — its product, a discovery-capital entry, was produced directly as `DL-THER-105`; invoking the wrapper would have added ceremony, not capital. `legend-proband-priority-matrix` — the wave was two named PMIDs, not a batch to rank.
- **Failures, retries, mismatches, concurrency:** (1) strict validator returned 22 BLOCKs on arrival — the checkout held no evidence; (2) receipt writer rejected `analysis_at` later than `event_at` — my clock error, corrected; (3) a locator snippet fell below the 30-character minimum — corrected; (4) **LINT caught `DUPLICATE_QUEUE_ID` on my own `FT-044` heading**, which would have made every existing reference to `FT-044` ambiguous — corrected by removing the `FT-` prefix from the update heading, with the reason written into the file; (5) the commit wrapper had a `-m`-after-`--` defect, fixed by the coordinator before I first used it; (6) peer `BLOCK_BATCH_COMMIT` twice, transient.
- 🔴 **What caught each failure before an overclaim — the attribution matters more than the count.** Item 1: the strict validator, not me. Items 2–3: the validated writers, not me. Item 4: **`legend_lint.py`, not me** — I had already committed the duplicate heading. Item 5: the coordinator. And the most consequential: **the blind locator auditor caught an `OVERSHOOT` in my own wording** — I wrote that the WT-versus-rescue comparison was *"untested"* for TBR1 and SATB2, when the legend's all-pairwise Tukey test means *tested and not significant*. I did not catch that; a reader with no knowledge of my conclusions did, in minutes. **Every one of the six was caught by a machine or another agent. Not one was caught by my own re-reading**, which is the single most useful line in this diagnosis and the argument for keeping all of these gates expensive.
- **Disease-agnostic micro-upgrade shipped:** `framework/scripts/evidence_presence.py` + `test_evidence_presence.py` (commit `2482071`). Reports, per manifest, whether each fingerprinted artifact is `PRESENT` / `DIGEST_MISMATCH` / `ABSENT`, and refuses to merge the last two. First measurement over this checkout: **65 manifests, 464 artifacts, 36 present, 428 absent, 0 digest mismatches.**
- **Regression / evidence making it persistent:** 7 unittest cases, repo convention. **Mutation-tested**: collapsing `DIGEST_MISMATCH` into `ABSENT` turns 2 tests red, so the suite fails on exactly the conflation it forbids. Release regressions: 10 suites FAIL and **all 10 were already red before the change**, verified by removing both new files and re-running four to identical exit 1; they are live-corpus tests asserting on the empty `files/` tree.
- **Residual risk and next decisive action:** the highest risk is that **`CLAIM 003` is a consolidated baseline whose primary source this repository cannot currently open**, in a field with 8 PubMed records. Next decisive action is not analytical but mechanical: open `https://academic.oup.com/brain/article/144/10/3061/6259140` in a real browser, save the PDF, re-test its text layer for the `SUSPECT` signature, and only then read it.

## Grade separation — process versus outcome

**Outcome: good.** One paper's evidence chain restored and re-verified byte-identical, one genuine
panel finding that qualifies a consolidated baseline, two adjacent negatives anchored, a capability
shipped with tests.

**Process: adequate, not good.** Every defect in this session was caught by a gate or another
agent and none by my own review, including one wording overshoot that had already reached a draft
locator and one duplicate identifier that had already reached a commit. The gates worked; my
self-checking did not add to them.

*Disease-level, derived from public literature. Not medical advice.*
