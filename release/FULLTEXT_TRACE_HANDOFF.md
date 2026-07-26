# Full-text trace handoff

## Integration status

The full-text trace seam is closed for the public WWOX fixture. Future reads have one
authoritative append-only sink, and both operational views consume it fail-closed.

## What is now available

- Universal contract: `framework/protocols/fulltext_read_receipt.md`
- Machine schema: `framework/schemas/fulltext_read_receipt.schema.json`
- Append/query validator: `framework/scripts/fulltext_receipts.py`
- Authoritative WWOX event ledger:
  `disease-models/wwox/registries/fulltext_read_receipts.jsonl`
- Exhaustive route classification: `framework/config/fulltext_route_registry.json`
- Cross-skill contract test: `scripts/test_fulltext_trace_contract.py`
- Utility tests: `framework/scripts/test_fulltext_receipts.py`

## Integration rule for the reconstructed classifier

1. Future reads should be driven by contemporaneous append-only receipts, not inferred from
   prose markers.
2. Historical evidence may be represented as `legacy_reconstruction`; it must name the
   surviving `evidence_basis` and must not invent `analysis_at` or complete coverage.
3. A downloaded file or retrieval manifest is `retrieved_not_read`.
4. The derived coverage report and batch queue consume the receipt history, but they are
   views, not the event history. Missing or invalid ledger state blocks their generation.
5. The preflight order is PMID/DOI resolution → receipt lookup → reuse/resume/reread decision
   → only then full-text acquisition and analysis.
6. Do not synthesize historical receipts merely to make counts green. Unresolved history
   remains reading debt.

## Historical boundary

The ledger contains 22 conservative reconstructions for public registry records whose
surviving prose explicitly declared full or partial full-text review. They use
`partial_fulltext_read`, `analysis_at: null` and section state `unknown_legacy`: none is
presented as contemporaneous proof or a complete receipt. No event was invented for work
that is not evidenced in this public repository. Those unresolved historical reads remain
separate from receipt-backed completion and visible as audit debt.

## Enforcement

- Append validation rejects empty or contradictory “complete” receipts, invalid timestamps,
  broken reread lineage and identifier conflicts.
- Append uses an exclusive POSIX lock, linear per-study lineage, flush/`fsync` and an
  atomic state-anchor update before success is reported. If the anchor update fails, the
  uncommitted ledger append is rolled back.
- LINT validates a unique authoritative ledger path, unique anchor fields and the exact
  identities of grandfathered registry declarations. A one-for-one substitution cannot
  bypass the historical ratchet merely by leaving its count unchanged.
- Every current and future `.claude/skills/*/SKILL.md` and `.claude/agents/*.md` route must
  be classified; the regression fails when a route is added without an explicit policy.
- Retrieval, RAG/query and sampled reading have non-complete states and cannot clear debt.
