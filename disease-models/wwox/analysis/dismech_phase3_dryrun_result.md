# Phase 3 — exporter dry run

> **Non-canonical, and not a submission.** Output goes to `staging/` only. No pull request,
> no canonical file touched, nothing sent anywhere.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Date:** 2026-08-04 · **Tool:** [`export_dismech_dryrun.py`](./scripts/export_dismech_dryrun.py) · 15 regressions
**Schema pin:** `dismech.yaml` blob `e1a5bde3…`, commit `c43343af…`

---

## What came out

```
occurrences 22 · eligible 17 · evidence assertions 16 · attachments 2
MONDO:0014533 (WOREE/DEE28):  2 pathophysiology nodes
MONDO:0013687 (SCAR12):       0 pathophysiology nodes
unassigned to any disease entry: 14
losses — Ledger A {SOURCE_SUPPORT_NOT_FOUND: 3, ELIGIBILITY_DEBT: 2} · Ledger B {SCHEMA_LOSS: 8}
```

Seventeen occurrences pass every gate. **Two nodes are emitted.** The gap between those two
numbers is the finding.

## The finding: a claim about a gene is not a claim about a disease

Fourteen of the sixteen evidence assertions were not assigned to either disorder, and the
exporter reports them rather than placing them somewhere plausible.

They are statements like *"L404 is strictly required for the WWOX–GSK3β interaction"* and
*"WW2 engages a second PPxY motif when the topology is compatible"*. Every one is verified,
locator-backed, and eligible. None of them is, by itself, a statement about the
pathophysiology of WOREE or of SCAR12.

**Nothing in the pipeline supplies that bridge.** The sidecar decomposes claims about WWOX;
a DisMech entry is about a disease. Deciding that a molecular finding belongs in a disorder's
pathophysiology is a curation judgement, and no one has made it — not the derivation, not
the independent run, not the two blind reviewers, none of whom were ever asked.

So the honest state is: **the export machinery works and the content is not yet
disease-attributed.** That is a better outcome than two well-formed entries would have been,
because well-formed entries would have hidden the same gap behind plausible YAML.

**SCAR12 receives nothing**, and the file is emitted empty rather than omitted, so the gap is
visible in the output instead of inferable from its absence.

## What the exporter refuses to do, verified

| Rule | Refusal | Checked |
|---|---|---|
| write outside `staging/` | exit 1 | ✅ |
| schema pin mismatch | exit 1 | ✅ |
| pin not asserted | run marked `DRY_RUN_SCHEMA_UNVERIFIED`, never silently "verified" | ✅ |
| F1 — export an `INFERENZA` as `SUPPORT` | `REFUSED (Rule F1)` | ✅ |
| eligible occurrence without a snippet | refused | ✅ |
| E2 — omit `mechanism_confidence` | never omitted; the pinned schema reads absence as `ESTABLISHED` | ✅ |
| E1 — `ESTABLISHED` from a single source | never | ✅ |
| unassessed confidence criteria | recorded as `null`, never read as satisfied | ✅ |
| C2 — invent a `modifier` | none emitted; no occurrence records a signed direction | ✅ |
| M1 — `conforms_to` an `UNASSESSED` module | none emitted | ✅ |
| identity A | exported + classified = enumerated, asserted at run time | ✅ |
| determinism | two runs, byte-identical | ✅ |

Every exported evidence item carries **both** receipt IDs, the verbatim snippet, the source
anchor, and the link basis in both directions.

## What is not established

- **That these two nodes should be submitted.** They are one proposition — the WWOX 388–407
  requirement — reached from two claims, at `PROVISIONAL` confidence from a single source.
- **That the fourteen unassigned assertions belong anywhere.** They may belong on a WWOX
  gene page, on a shared mechanism module, on both disorder entries, or nowhere in DisMech.
  That is the next question and it is a scientific one.
- **That the schema pin still holds.** The run was executed with `--schema-sha` asserted from
  the specification, not fetched. A live check needs the network and is a separate step.

## Next

1. **Decide the disease attribution.** For each of the fourteen, does it belong in the
   pathophysiology of WOREE, of SCAR12, of both, or of neither? This is the judgement the
   whole pipeline has been deferring, and it cannot be automated.
2. Only two claims of thirty-five are represented here. The PoC scope was always three
   claims; a submittable entry needs the rest of the model to clear the same gates.
3. Phase 4 — running DisMech's own validators against the emitted YAML — is now possible for
   the first time, and would test the field mapping against the real schema rather than
   against our reading of it.

## Related

[`dismech_export_spec.md`](dismech_export_spec.md) §13 · [`dismech_axis4_result.md`](dismech_axis4_result.md) · [`dismech_axis3_review_result_round2.md`](dismech_axis3_review_result_round2.md)
