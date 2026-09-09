# CAPABILITY SCOUT LOG — LEGEND

> Non-canonical operational log. Append-only. It tracks capability gaps and contains no
> scientific claims or canonical promotions.

---

## 2026-08-11 — Structured-landing identity parity

### Session Learning Delta

- A complete review read was already attached to `LIT-0333` and `CORPUS P333`.
- The self-evaluation gate scanned both registry files but did not recognise either identifier
  family, producing `ORPHAN_COMPLETE_READ`.
- The failure was in the gate's population definition, not in the scientific landing.
- A single shared identifier predicate now covers every native record family used by the landing
  files, including `LIT-*`, `CORPUS P*` and `CORPUS-STUB-*`.

### Capability Gaps

| Gap | Why it matters for LEGEND | Priority |
|---|---|---:|
| The landing gate's file population and record-ID population could diverge | A valid registry record could be called orphan, encouraging redundant ledger entries or weakening the gate | 5 |
| Source-transmission direction is not mechanically compared with its cited primary | Reviews can invert an intervention or experimental arm while remaining fluent | 3 |

### Candidate Capabilities

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| Shared structured-landing ID predicate plus regressions | gate | Registry/record population parity | 3 | 3 | 2 | 3 | 3 | IMPORT |
| Review-to-primary actor/perturbation/direction audit | mini-procedure | Transmission error detection | 2 | 3 | 2 | 2 | 3 | MONITOR |

### Mandatory Micro-Upgrade

- **Type:** MINI-PROCEDURE / gate improvement.
- **What improved today:** `session_self_eval.py` recognises registry-native structured records and
  has independent regressions for `LIT` and `CORPUS` landings.
- **Why proportionate:** it repairs the exact false failure exposed by this batch without adding a
  new registry, dependency or disease-specific rule.

### Import/Audit Notes

- No external repository, API or plugin was needed; cost and privacy risk are zero.
- The scientific and tooling changes remain separable for merge review.

### Next Micro-Step

- On the next review/primary pair, trial a three-field transmission audit — actor, perturbation,
  direction — before deciding whether it deserves a reusable manifest field.

---

## 2026-08-11 — Wwox mouse-series reading

### Session Learning Delta

- A record-level deduplicator classified PMID 17360458 as integrated because another paper's prose cited it.
- The same false positive survived an exact-PMID score of 100: syntactic exactness did not imply semantic identity.
- A study record needs one explicit identity surface, distinct from citations, claim links and reading debt inside its prose.
- The four-paper read also confirmed that genotype labels in structured HTML must remain the reference when PDF fonts lack ToUnicode.

### Capability Gaps

| Gap | Why it matters | Priority |
|---|---|---:|
| Separate record identity from incidental citation identifiers | Otherwise unread studies can be declared integrated and skipped | 5 |
| Keep a regression with a primary PMID A and cited PMID B | Prevents the same false-negative reading debt from returning | 5 |

### Candidate Capabilities

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| Existing `study_dedup_triage.py` plus identity-field regression | internal skill | Record identity vs prose citation | 3 | 3 | 2 | 3 | 3 | IMPORT |
| External bibliographic entity resolver | service/API | More permissive identity inference | 1 | 1 | 2 | 2 | 1 | SKIP |

### Mandatory Micro-Upgrade

- **Type:** MINI-PROCEDURE / regression.
- **What improved today:** exact identifiers are indexed only from declared bibliographic identity fields; a PMID mentioned only in record prose now remains new/in-pipeline instead of becoming `KNOWN_INTEGRATED`.
- **Why proportionate:** it repairs the exact failure that almost suppressed an assigned first read, without adding a new dependency or changing scientific state.

### Import/Audit Notes

- Targeted test passes, and the real four-PMID triage now returns two corpus placeholders and two queue entries; PMID 17360458 resolves to FT-032 rather than PAPER 057.
- No external repository, API key or sensitive-data flow was introduced.

### Next Micro-Step

- When this tooling commit is merged, rerun the repository's record-convention test with the intake test so field vocabulary and identity semantics cannot drift separately.

---

## 2026-09-09 — `scientist-c`, `AQEILAN-FT-C-001` wave 1 (PMID 20530675, PMID 21731849)

### Session Learning Delta

- A **supplement** retrieved from a paper previously read as partial produced **four** findings, none
  visible from the main text: a table that reverses the direction of the paper's headline
  association, a figure legend that contradicts the paper's own penetrance number, clone/control
  dependence of the functional rescue, and an antibody the Methods never describe.
- Two of four confidence intervals in a printed table were computed on the **negative count** instead
  of the total — reproducible exactly by the paper's own stated method, and one of them lies entirely
  above its own point estimate.
- A **same-lab review** was read as a runnable **citation-fidelity test** because five of its
  load-bearing sources already carry complete-read receipts here. Result: mostly faithful, with four
  specific drifts — including one where abstract and body are correct and only the **Conclusions**
  conflate two assays.
- A **two-column PDF** extracted with `pdftotext -layout` interleaved its columns and put a page
  number **inside** the sentence carrying the headline claim.
- `files/fulltext/` and `files/figures/` were **empty** in the shared checkout, so no prior manifest
  could be verified from bytes.

### Capability Gap

1. To quote safely from a PDF-only, multi-column paper we lacked **any mechanical detector for page
   furniture landing inside a sentence** — the one hazard that produces a locator which *passes*
   verification while matching a sentence nobody wrote.
2. To trust a printed confidence interval we lack **a recomputation check against its own stated
   numerator and denominator**. Two real defects here were found only because the reading did the
   arithmetic by hand.
3. To know whether a checkout can verify its own manifests we lacked a presence check — **closed in
   this same session by `scientist-a`'s `evidence_presence.py`**, found independently from the other
   direction. Recorded as convergence, not as a new gap.
4. To repair a persisted receipt whose **`study_id` is wrong** there is no lawful route at all; the
   ledger now refuses the *correct* DOI because an incorrect one was written first. This is a
   **schema** gap and is the operator's, not an actor's.

### Search Plan and Scoring

**No external search was run and no resource was imported.** The session's constraint was explicit —
no external spend, no API-keyed service — and gap 1 was answerable from inside the repository, which
is the cheaper and more auditable answer. Recorded so the absence is a decision, not an omission.

| Resource | Type | Gap covered | Case fit | LEGEND fit | Novel | Maturity | Cost/privacy | Action |
|---|---|---|---:|---:|---:|---:|---:|---|
| `framework/scripts/text_surface_intrusion_check.py` (built here) | internal script + 7 regressions | Gap 1 | 3 | 3 | 3 | 2 | 3 | **IMPORT** |
| `scientist-a`'s `evidence_presence.py` | internal, peer-shipped | Gap 3 | 3 | 3 | 2 | 2 | 3 | **AUDIT** — landed by a peer today; not re-verified by me |
| A CI recomputation check (Clopper–Pearson vs stated n/N) | proposed internal | Gap 2 | 2 | 3 | 3 | 1 | 3 | **MONITOR** — specified below, deliberately not built |
| `record_kind: identity_correction` for receipts | schema change | Gap 4 | 2 | 3 | 3 | 0 | 3 | **SKIP** — reserved; referred to the operator |
| PyMuPDF / `fitz`, external OCR or layout ML | external dependency | Gap 1, richer | 1 | 1 | 2 | 3 | 2 | **SKIP** — `fitz` is already absent in this environment and a red suite proves it; an ML layout model would also violate rule 5c if its output were ever declared as an artifact |

### Mandatory Micro-Upgrade

- **Type:** NEW INTERNAL CHECK + regressions.
- **What improved today:** `framework/scripts/text_surface_intrusion_check.py` with
  `test_text_surface_intrusion_check.py` (**7/7 PASS**). It reports every span in an extracted text
  surface where page furniture sits inside a continuing sentence — i.e. every span a verbatim quote
  must not cross. Fully **disease-agnostic**: it names no gene, disease or model.
- **Why proportionate:** it mechanises the exact judgement that saved this session's most load-bearing
  quote, and which was otherwise performed by eye against a rendered page.
- 🔴 **It was strengthened by its own first production run, which is the part worth keeping.** Run
  against the PMID 20530675 supplement it reported **chart axis ticks** as page numbers and
  **repeated table rows** as running headers. Both were turned into regressions and the heuristics
  narrowed — a bare integer counts only inside a consecutive numbering chain; a repeated line is
  excluded when it carries table-column gaps. **False positives on that document: 12 → 1.** The check
  was then turned on my own work: of 15 text locators in the `PMID21731849` manifest, **0** span an
  intrusion.

### Import/Audit Notes

- **No external repository, API key, paid service or sensitive-data flow was introduced.**
- Release regressions after the change: the one suite this change reddened —
  `test_scientific_consistency` — was **green again after fixing the science rather than the check**
  (a dossier had collapsed *normal mRNA + low protein* into a turnover mechanism; it now states that
  the pattern locates the loss post-transcriptionally and identifies no route, leaving turnover,
  impaired translation, insolubility and a technical epitope floor all open). The remaining six
  failures are environmental and pre-existing: `numpy` and `fitz` absent, a `master`/`main` fixture
  assumption, and `test_surface_census` failing because `files/` holds no bytes.

### Next Micro-Step

1. **Wire `text_surface_intrusion_check` into `deepdive_manifest.py`** for any locator whose declared
   `artifact` is a PDF-derived text surface, so a quote spanning an intrusion is refused rather than
   merely reportable. **Deliberately not done in the same change that introduced the checker** — a
   detector and the gate that enforces it should not land together, because the first production run
   is what tells you the thresholds are wrong, and it did.
2. **Build the CI recomputation check (gap 2).** Specified concretely so it is not a wish: given a
   table row carrying a count, a total and a printed exact-binomial interval, recompute
   Clopper–Pearson and flag disagreement, plus the cheap invariant that **an interval must contain its
   own point estimate** — which alone would have caught the Total OS row here.
3. **Re-derive the group publication counts** (137/64, carried forward from 2026-08-11) at the next
   wave rather than carrying them a third time.
