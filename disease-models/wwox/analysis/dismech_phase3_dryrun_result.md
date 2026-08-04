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
occurrences 22 · eligible 17 · evidence assertions 16 · attachments 32
MONDO:0014533 (WOREE/DEE28):  16 pathophysiology nodes
MONDO:0013687 (SCAR12):       16 pathophysiology nodes
unassigned to any disease entry: 0
losses — Ledger A {SOURCE_SUPPORT_NOT_FOUND: 3, ELIGIBILITY_DEBT: 2} · Ledger B {SCHEMA_LOSS: 8}
```

### The first run emitted two nodes, and that was the finding

Before the disease attribution was made, fourteen of sixteen evidence assertions had no
target and the exporter reported them rather than placing them somewhere plausible. They are
statements like *"L404 is strictly required for the WWOX–GSK3β interaction"* — verified,
locator-backed, eligible, and not by themselves statements about the pathophysiology of
either disorder.

Nothing in the pipeline supplied that bridge. The sidecar decomposes claims about a **gene**;
a DisMech entry is about a **disease**. That judgement had never been asked of anyone — not
the derivation, not the independent run, not the two blind reviewers.

### The attribution, and where it comes from

WOREE and SCAR12 are one genotype-phenotype spectrum: severe toward null/null and total loss
of function, milder at SCAR12, which is still severe and differs by a few motor milestones
rather than by mechanism. This repository already asserts it:

| Claim | Status | |
|---|---|---|
| **CLAIM 008** | `consolidated baseline` · `DATO` | WOREE and SCAR12 form a genotype-phenotype spectrum |
| **CLAIM 017** | `consolidated baseline` · `DATO` | the disease spans severe WOREE/WWOX-DEE to milder SCAR12-like phenotypes |
| CLAIM 030 | `in observation` | severity tracks residual protein **function**, not abundance |

A finding about how WWOX works therefore describes the mechanism of both ends of one
spectrum. **The two entries differ in phenotype and severity, not in mechanism** — which is
exactly why the molecular nodes are shared and the clinical content is not. All sixteen
assertions now route to both entries: 32 attachments from 16 assertions.

### 🔴 The claim that licenses the routing cannot itself be exported

Neither CLAIM 008 nor CLAIM 017 has a source with a complete-read receipt. Both terminate in
`ELIGIBILITY_DEBT`. **The reason we may place a node on both entries is a claim we cannot yet
put in either.**

The routing is therefore recorded in the loss report as a curation judgement with its basis
named and its basis's ineligibility declared, rather than emitted as an asserted node. A
regression asserts that the report says so.

This also settles a question left open in the specification. §10 recommended entry-local
nodes over a shared module *"because no proposition meets all three conditions"*. Condition
(ii) — holds for both disorders without weakening — is now met on this evidence. Condition
(i) — supported by an assertion passing §5 — is not, and will not be until CLAIM 008 or 017
is read to receipt. **The shared module has a rationale and still lacks its evidence.**

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

## Phase 4, offline: validated against the pinned schema

The field mapping was written by reading `dismech.yaml`, and reading is not checking.
[`validate_dismech_yaml.py`](./scripts/validate_dismech_yaml.py) compares the emitted entries
against what the schema declares — slot names per class, permissible enum values, required
slots — with the pin verified by recomputing the git blob id rather than trusting a label.

**First run: 130 problems, all of one shape.** Every schema-legal part passed — `Disease`
slots, `Pathophysiology` slots, `EvidenceItem` slots, and all three enums
(`mechanism_confidence`, `supports`, `evidence_source`). What failed were four keys of my own
invention: `_provenance`, `_confidence_criteria`, `_evidence_assertion_id`,
`_originating_claim_ids`.

That is the failure mode worth catching. A key the schema does not declare is not rejected by
a permissive reader — it is **silently ignored**. The entries would have looked complete and
arrived carrying nothing of the receipt lineage.

**The fix is not to drop the provenance.** Losing it to satisfy the schema would discard the
one thing this pipeline exists to carry. It moves to companion files beside the entry:

| File | Holds |
|---|---|
| `MONDO_*.yaml` | schema-clean entries; `notes` names the LEGEND assertion id and its claims |
| `provenance.json` | 17 records: occurrence, claim, PMID, **both** receipt IDs, source anchor, link basis |
| `confidence_criteria.json` | 16 records: the six-criterion justification behind each `mechanism_confidence` |
| `loss_report.json` | the two ledgers and the routing justification |

**Second run: 0 schema problems**, on both entries. A regression asserts that no key
beginning with `_` survives inside an entry and that the provenance is non-empty — so the
next person cannot quietly trade one for the other.

What this still does not do is what `just qc` does upstream: resolve ontology terms and match
snippets against cached references. Both need the DisMech repository and the network.

## What is not established

- **That these two nodes should be submitted.** They are one proposition — the WWOX 388–407
  requirement — reached from two claims, at `PROVISIONAL` confidence from a single source.
- **That the fourteen unassigned assertions belong anywhere.** They may belong on a WWOX
  gene page, on a shared mechanism module, on both disorder entries, or nowhere in DisMech.
  That is the next question and it is a scientific one.
- **That the schema pin still holds.** The run was executed with `--schema-sha` asserted from
  the specification, not fetched. A live check needs the network and is a separate step.

## Next

1. **Read CLAIM 008 or CLAIM 017 to receipt.** It is the shortest path to two things at once:
   the spectrum becomes exportable, and §10's shared module gains the evidence it lacks. One
   paper, already in the registry, and the reading debt is the only thing in the way.
2. Only three claims of thirty-five are represented. A submittable entry needs the rest of
   the model through the same gates — and the locator requirement now in the deep-dive
   contract means new readings will arrive export-ready rather than needing retrofit.
3. Phase 4 — running DisMech's own validators against the emitted YAML — is now possible and
   would test the field mapping against the real schema rather than against our reading of
   it. Sixteen nodes per entry is enough material for that test to mean something.

## Related

[`dismech_export_spec.md`](dismech_export_spec.md) §13 · [`dismech_axis4_result.md`](dismech_axis4_result.md) · [`dismech_axis3_review_result_round2.md`](dismech_axis3_review_result_round2.md)
