---
record: SESSION LEARNING REVIEW / batch self-evaluation
id: SLR-scientist-b-0002
actor: scientist-b — task AQEILAN-FT-B-001 (wave 1), TASK_ACK and durable TASK_CLAIM committed d5e1191
date: 2026-09-09
tree: 41eef22 -> (this session)
outputs: deepdive_manifests/PMID29724996.json (38 locators) · deepdive_manifests/PMID30470736.json (5 locators) ·
  fulltext_dossiers/PMID29724996.md · fulltext_dossiers/PMID30470736.md ·
  commit_candidates/CC-20260909-29724996-01.md · discovery_ledger_current.md#DL-BIOM-014 ·
  framework/scripts/erratum_scope_check.py
receipts: FTR-20260909-29724996-01 · FTR-20260909-30470736-01
template: framework/protocols/batch_self_evaluation_template.md
---

# Batch self-evaluation — `scientist-b`, `AQEILAN-FT-B-001` wave 1, 2026-09-09

> Written **before** the capability micro-upgrade was finished and **before** the closing report,
> per `session_self_evaluation.md`. Takeaways written first describe a session that went well.

## Scope and executable verdict

- **Batch/session:** `AQEILAN-FT-B-001` wave 1 — PMID **29724996** (resume of a declared partial),
  PMID **30470736** (its Author Correction, first contact). The remaining six PMIDs of the lot were
  **not opened**, per the wave dispatch.
- **Studies and complete-read receipt IDs:** `FTR-20260909-29724996-01` (`complete_fulltext_read`,
  `inadequate_prior_coverage`, `prior_receipt: FTR-20260810-29724996-01`) ·
  `FTR-20260909-30470736-01` (`complete_fulltext_read`, `first_read`).
- **`session_self_eval.py`:** **PASS** — receipts 134, complete_fulltext_events 66,
  active_complete_reads **55**, unread_premises **4/4** (at baseline: this batch added none).
- **Per-study manifest(s):** `PMID29724996.json` **PASS, 0 gaps**, 38 locators (13 new);
  `PMID30470736.json` **PASS, 0 gaps**, 5 locators. Both `--verify-artifacts
  --require-current-schema`, run from the shared root checkout.
- **Receipt verification:** `fulltext_receipts.py verify` → **OK, 134 chained, tail anchored**.
- **Structural LINT:** **PASS** (one pre-existing INFO on CLAIM 010, untouched by this batch).
- **Local verdict:** **PASS**.
- **Workspace/global verdict and concurrent conditions:** three actors on one checkout. Peers
  appended to the receipt ledger **between** my two receipts (133 → 134) and the writer's exclusive
  lock handled it with no rechain event, which is the case it was built for. `scientist-a` landed
  `evidence_presence.py` mid-session; I checked it **before** choosing a micro-upgrade specifically
  to avoid duplicating it, and did not.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | The uncovered section of the prior receipt (supplementary) read in full: 4 supplemental figures as 300 dpi page images, 2 supplemental tables. All 7 main figures re-opened; 5 re-verified at 400 dpi by rasterising the publisher PDF's vector charts. Main article has 0 `table-wrap`, verified by element count. | **strong** | none |
| Main message and original contribution | The paper's own central result was **bounded** rather than restated: the ChIP battery is closed at five promoters and excludes PDK1/LDHA1. | **strong** | — |
| Hidden gold beyond keywords/abstract | Four supplement-only findings the running text does not carry: the closed ChIP roster; PKM2 absent from the HFD response; superimposed HFD weight curves (a negative doing positive work); CTGF running opposite in time to the glycolytic programme. | **strong** | — |
| Source parity: context, type and recency | An oncology/hepatic paper and a one-page erratum, both read at full depth. The erratum was read **as a source**, not treated as metadata — which is what let its scope be checked against the locator set. | **strong** | — |
| Team type, field density, observation vs interpretation | Field density re-measured 2026-09-09 (137/65), not carried over. Group weighting stated honestly for an erratum: an Author Correction's value comes from the journal of record publishing it, **not** from the laboratory's standing. | **strong** | — |
| DATO / INFERENZA / IPOTESI / ESPANSIONE separation | Transfer verdict **ESPANSIONE** with the neural assumption tagged `PREMISE: DEFAULT_FROM_TEXTBOOK` and a `REVIVAL_TRIGGER`. The tag is not decorative: the paper's own supplement falsifies gene-set stability across two contexts of one tissue. | **strong** | — |
| Existing claims touched; conflicts/revival triggers | `CLAIM 025` corroborated in direction and narrowed in scope; `Status` unchanged. Review floor **checked against the registry** and correctly not triggered — the three consolidated baselines are human clinical claims this hepatic paper does not reach. | **strong** | — |
| Multi-hop and corpus cross-query | 74 references enumerated (prior). Cross-query answered a real question and returned a real answer (0 locators on a corrected panel), not a formality. | **partial** | The PDK1 bridge to `PMID 30755385` is flagged for qualification in the candidate but that paper's own record was not edited — correctly, it is not my task. |

## Persistence diagnosis

- **Durable ledger/registry IDs and wikilinks:** `FTR-20260909-29724996-01`,
  `FTR-20260909-30470736-01`; `CC-20260909-29724996-01` (proposes `CORPUS-STUB-073` → `PAPER 081`,
  `LIT-0096` completion); `DL-BIOM-014` in the discovery ledger.
- **Reading queue/debt:** the 2026-08-10 supplementary debt is **closed**. Six PMIDs of the lot
  remain unopened by design (wave dispatch), not as silent debt.
- **Dossier and commit candidate:** both papers have dossiers; one commit candidate covers both,
  deliberately — an erratum does not merit its own `PAPER` record, and a second candidate would
  create two places to keep aligned.
- **Receipt source fingerprint, coverage and supplement state:** fingerprints are of the artifacts
  **actually on disk and actually inspected**. `supplementary: read` — earned; it is the whole point
  of the resume.
- **Can a future run distinguish full text from abstract only? How:** yes. Both receipts are
  `fulltext_local` with a SHA-256 over a local structured surface, every locator names a
  fingerprinted artifact, and `abstract` is not an evidentiary surface on any entry.

## Process and capability diagnosis

- **Skills/gates/patterns used:** M0 duplicate-work gate re-run **per paper** (a peer had appended
  since the orchestrator's sweep); strict manifest validator; receipt writer; LINT;
  `session_self_eval.py`; `evidence_presence.py` (peer's, run over my PMIDs: 17/17 present and
  matching).
- **Plausible skills deliberately declined, with reasons:** `legend-locator-audit` — floor tested
  against the registry and not met, written into `skills_considered`; `legend-discovery` — leads
  recorded as locators and a ledger entry, restating them would add no source;
  `legend-safety-triage` — no molecule promoted, and this reading *narrows* digoxin's evidence.
- **Failures, retries, extraction mismatches or concurrency events:**
  1. **Evidence bytes absent.** `files/` was empty; every artifact re-acquired. Supplement digest
     reproduced exactly; XML and all 7 figures **did not** (Europe PMC re-serialises and re-encodes).
  2. **Validator refused my first supplement text surface** (`U+000C` at offset 1500). Re-derived
     with `pdftotext -raw -nopgbrk`, **not** stripped.
  3. **Receipt writer rejected `analysis_at` twice** as later than `event_at` — I had stamped a
     round future time instead of reading the clock.
  4. **Commit message lost a clause to shell backtick expansion.** Not amended: history rewrite is
     reserved (§21d). Remaining messages avoided backticks.
- **What caught each failure before an overclaim — the honest one first:**
  🔴 **I was about to file a false correction against a correct locator.** Reading Fig 6A at the
  667 px PMC rendering I made the counts ~14 vs ~1 of ~15 and began drafting a correction to
  `entries[21]`, which asserts 11/12 vs 4/18. At 400 dpi the bars resolve as stacked **by genotype
  within each outcome category** and the existing locator is **exactly right**. What caught it was
  the rule that a figure is inspected at original resolution — applied *before* contradicting an
  existing locator, not after. **Grade for my own first pass here: `failed`.** The near-miss is the
  most important thing in this batch, because the wrong edit would have been confident,
  well-argued, and would have passed every gate this repository owns.
  The other three were caught by machines: the SUSPECT screen, the writer's timestamp check, and
  the strict validator's digest comparison.
- **Disease-agnostic micro-upgrade shipped:** `framework/scripts/erratum_scope_check.py` — answers
  *"does any locator stand on a panel its own erratum corrected?"*, the check this repository has
  now recorded as missing **twice** (2026-08-10 and again today) and implemented zero times.
- **Regression/evidence that makes the upgrade persistent:** a `--self-test` of **12 cases, 12
  passing**, every one of which was a **live false positive before it was a test** — including the
  one that matters most, that a main-figure erratum scope must **not** match a *Supplemental*
  Figure 3A anchor, which the first version got wrong against my own new locators. Corpus run:
  58 manifests mention an erratum, **52 are negated mentions** (counted, not silently dropped),
  **2 CLEAR**, **4 SCOPE_UNDECLARED**. The `CLEAR` on 29724996 was **mutation-tested**: an injected
  `Figure 3, panel A` anchor fires, the real `panel F` anchor does not — so the clean verdict is
  earned rather than vacuous.
- **Residual risk and next decisive action:**
  1. **4 manifests record a real erratum and declare no scope** (`30290271`, `36779245`, `37519886`,
     `38182577`). I did **not** edit them — they are not my task and may be a peer's. Reported to the
     orchestrator as a measured, newly visible debt; declaring `corrected_items` on each is minutes
     of work by their authors.
  2. **The tool reports; it does not gate.** `--fail-on-review` exists but is not wired into LINT.
     Wiring it is a governed change and belongs to Harness Engineering, not to a reading session.
  3. **Anchor-dependence is a real blind spot**, reported as `ANCHOR_UNPARSEABLE` rather than scored
     clean: a figure locator whose anchor says "the histology" cannot be checked by any string match.
