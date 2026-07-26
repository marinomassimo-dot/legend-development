# Exact-wikilink migration completion record

## Release status

**Migration completed on 2026-07-25.** The strict link target is green:

```bash
python3 scripts/test_link_targets.py
```

The migration repaired **234** Obsidian fragments that identified an existing
record but did not reproduce the target heading exactly. Obsidian heading
links use the full heading text after `#`; non-heading failure-mode records now
use stable block anchors.

Breakdown:

| Source | Migrated links | Mutation discipline used |
|---|---:|---|
| `research/discovery_ledger_current.md` | 185 | invariant-safe link-only migration; historical records preserved |
| `research/therapeutic_hypotheses_ledger_current.md` | 41 | invariant-safe link-only migration; historical records preserved |
| `registries/claim_registry_current.md` | 5 | migrated through `BATCH_COMMIT` |
| `analysis/md_q230p_protocol.md` | 1 | ordinary content correction |
| `research/research_candidates_current.md` | 1 | ordinary content correction |
| `framework/protocols/wikilink_schema.md` | 1 | ordinary documentation correction |

## Preserved migration contract

1. Keep `scripts/test_link_targets.py` unchanged.
2. Resolve every reported basename to the unique shipped Markdown target.
3. Replace the fragment with the target's complete current heading, preserving
   any existing display alias: `[[file#Exact full heading|display text]]`.
4. Do not create duplicate/fake headings merely to satisfy the test.
5. Do not turn a record line into a heading without an explicit schema
   migration. If a stable block identifier is preferred, update the protocol,
   migration and test together and document the compatibility decision.
6. Treat the five `claim_registry_current.md` edits as one canonical
   `BATCH_COMMIT`; do not edit that current directly.
7. For the two append-only ledgers, use the repository's approved
   history-preserving migration path. Do not delete or rewrite scientific
   assertions while repairing links.
8. Require all three link tests and the complete release regression inventory
   to remain green after every heading or record-link change.

## Verification

```bash
python3 scripts/test_link_targets.py
python3 scripts/run_release_regressions.py
python3 framework/scripts/legend_lint.py .
python3 scripts/public_release_gate.py \
  --root . --mode staging --skip-clean-clone
python3 scripts/independent_privacy_scan.py .
```

These commands are green in staging. A clean-clone hostile review must still
be tied to the exact candidate commit; any later commit invalidates that
sign-off.
