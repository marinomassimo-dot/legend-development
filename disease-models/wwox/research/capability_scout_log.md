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
