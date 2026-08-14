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
