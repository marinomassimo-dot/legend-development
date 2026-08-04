# DisMech independent derivation — Rev. 12 comparison report

> **Non-canonical methodological result.** This report compares two derivations of CLAIM 016,
> 024 and 035. It does not modify a scientific registry, validate a DisMech export, approve a
> production deduplication rule or make a clinical claim.

**Date:** 2026-08-04  
**First derivation:** `data/dismech_sidecar_016_024_035.jsonl`  
**Independent authored SHA-256:** `ec117b0a3b7194ff283dc9e16dc081817cafbbe2a7949409403f8586a446e07b`  
**Independent reconciled SHA-256:** `33f2db6c7e933b6c147cde8e8461f8ddd8066b46eed2d287a86f1094acb6de23`  
**Machine comparison:** `data/dismech_independent_comparison_rev12.json`

## 1. Run validity

- The blind actor attested `CLEAN` from the sealed v1 bundle.
- The authored stage passed the allowlist and hash checks with no extra files.
- Two post-run targeted-extraction receipts were appended through the validated writer:
  `FTR-20260804-35716775-05` and `FTR-20260804-22193544-05`.
- Reconciliation changed only `locator_extraction_receipt_event`, `terminal_state` and
  `unreached_tests`; full receipt ancestry reaches the projected complete reads.
- The authored output remains byte-identical to its run attestation.

## 2. Measured surfaces

| Surface | First derivation | Independent derivation |
|---|---:|---:|
| Assertion candidates | 21 | 31 |
| Assertion occurrences | 19 | 27 |
| Representation items | 8 | 15 |
| `ELIGIBLE_FOR_EXPORT` | 14 | 23 |
| `SOURCE_SUPPORT_NOT_FOUND` | 3 | 1 |
| `ELIGIBILITY_DEBT` | 2 | 3 |
| Occurrences CLAIM 016 / 024 / 035 | 4 / 5 / 10 | 9 / 8 / 10 |

These are different derivations, not sampling noise around one authored decomposition.

## 3. Four-axis comparison

### Axis 1 — anchor selection

- Shared anchors: **7**
- Union: **23**
- Jaccard diagnostic: **0.3043**
- First-only anchors: **7**
- Second-only anchors: **9**

The two readers did not select the same registry sentence surface. The largest expansion is in
CLAIM 016 and CLAIM 024; CLAIM 035 has equal occurrence count but different anchor allocation.

### Axis 2 — atomisation and source attribution

All seven shared anchors differ in occurrence content or partition. Across the whole run the
independent reader produced eight more occurrences and seven more representation items. This is
direct evidence that the current generic atomisation rules do not determine a unique split.

### Axis 3 — proposition correspondence

- Exact semantic matches: **0**
- Canonical-candidate matches: **0**
- Ambiguous groups: **0**
- First unmatched occurrences within shared anchors: **8**
- Second unmatched occurrences within shared anchors: **13**

The zero is not agreement and not a matcher crash. The propositions attached to shared anchors
operate at different granularities or select different mechanisms from the same registry span.
Broadening canonicalisation to force matches would manufacture equivalence and is not justified.

### Axis 4 — deduplication

The declared comparison universe is unambiguous cross-run proposition matches. That universe is
empty, so production and canonical-candidate partition disagreements both report zero. This means
**not measurable**, not concordant.

## 4. Structural identity finding

Seven `occurrence_id` values appear in both runs. In all seven cases:

- `claim_id`, `registry_anchor` and local ordinal are identical;
- proposition and/or context are different;
- therefore the same structural ID names different semantic content.

This falsifies the strong interpretation that `claim + anchor + ordinal` is a stable assertion
identity under independent re-derivation. It remains usable as a within-run structural slot only.
`content_fingerprint` correctly exposes the drift, but does not repair identity.

## 5. Decisions

1. **Do not promote** occurrence IDs to cross-run or canonical assertion identity.
2. **Do not broaden** canonicalisation merely to increase the match count.
3. Treat Axis 4 as `NOT_MEASURABLE_EMPTY_CORRESPONDENCE`, never as zero disagreement.
4. Add an explicit comparator diagnostic for shared occurrence ID with different content.
5. Review candidate/span identity and explicit sub-assertion structure before writing a production
   exporter or modifying the claim registry.

## 6. Open review items

- Decide whether stable identity should bind to an exact raw registry span plus a semantic slot,
  or whether sub-assertions must become explicitly authored upstream.
- Manually adjudicate unmatched propositions before changing generic atomisation rules.
- Exercise the matcher on a future pair with at least one unambiguous semantic match before
  claiming that deduplication reproducibility has been measured.

**Verdict:** `REVIEW_REQUIRED`. The independent experiment succeeded as a measurement and found
that assertion selection and identity are under-specified. It did not validate the current
atomisation or deduplication design.
