# IT17 session evaluation (orchestrator, 2026-11-01)

Executable part: see the close-out in the task record; `legend_lint.py` WARN without BLOCK, `fulltext_receipts.py verify` OK (no new receipt this iteration).

1. **Who caught what.** Fresh-context verifiers found: the cache read hole was real and the IT16 write-only guard insufficient (verified), obfuscated addresses and overwritten discards (P1); five failures of the sealed-freeze design (unhashed FREEZE.json, vacuous B1, rule counted outside the pool, non-ISO dates, vigabatrin coding) (P3); smoke overclaim and a missing push step in the single-act request (P4); non-UTF8 crash, silent empty surfaces, zero live WATCH questions and noisy queries (P2). The orchestrator's own pre-battery oversight of IT16 (landing without the freshness check) was caught by the battery, not by the orchestrator.
2. **Verifier independence.** Each verifier declared what it knew; two had seen a fragment of the producer's files (declared). Fixes after verification were rerun by the producer, not re-verified by a third actor.
3. **Autonomy.** Report to verification to next package happened and a checkpoint resume from the record was exercised (RECONCILIATION.md). Not shown: behaviour across sessions or days; the router row was not retested with a third actor.
4. **Capability.** Computational/process only. The one measured task (direction field) measures imported curation, and the radar's query quality is mixed. No predictive or therapeutic capability is claimed.
5. **Owed.** WATCH-with-reopen questions on the live repository (0), prose reopen conditions in READMEs; prospective scoring needs outcomes after 2026-11-01T16:54:06Z.
