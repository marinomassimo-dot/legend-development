# Public recovery handoff

This file records release-blocking content residuals found by the independent
tooling lane. It contains no private source excerpts and does not authorize
publication.

## Current verdict

- Public release gate after the Italian parent-of-origin adversarial upgrade:
  `PASS`, zero blocks.
- Independent privacy scan: zero blocking findings.
- Release regressions: the complete ordered inventory passes, including strict
  Obsidian heading-link integrity and the fresh-clone reader journey.
- Structural parity: canonical counts and working-model architecture pass.
- The earlier temporary-clone verdict was invalidated when the stricter link
  contract was added. A new hostile clone must be made from the final
  authorised candidate commit after every release change is complete.
- Publication remains blocked until the ownership/sponsorship wording is
  externally confirmed and the same review succeeds on the authorised,
  immutable candidate commit.

## Completed adversarial privacy repair

The following command is now green:

```bash
python3 scripts/public_release_gate.py \
  --root . --mode staging --skip-clean-clone
```

The post-first-green detector upgrade had exposed twenty-five overlapping
findings across fifteen locations: Italian parent-of-origin terms, abbreviated
compound-genotype language and reassembly of the two worked examples. The
content owner decoupled them; the upgraded 22-test detector remains in place.

The following content checks are now green:

```bash
python3 scripts/test_scientific_consistency.py
python3 scripts/test_public_prose_quality.py
```

They confirm that the later canonical Q230P mechanism correction is propagated
and that the known malformed Italian/English substitution scars are gone.

The analysis-package losslessness/readme check is now green:

```bash
python3 scripts/test_analysis_package_contract.py
```

All five compressed Claude Science narrative classes retain their decisive
method anchors and substantive public replacements. The README correctly
discloses that four large structure inputs are reconstructed/downloaded on
demand, and its example commands now match the shipped CLI.

The public-claim consistency target is now green:

```bash
python3 scripts/test_public_claims_contract.py
```

`CAPABILITIES.md` now describes the restored runtime and qualifies its
preservation claim against the manifest's named unresolved status rows.

Deep-link integrity is now independently enforced:

```bash
python3 scripts/test_link_targets.py
```

It verifies standard Markdown fragment anchors, stable LEGEND record IDs in
the correct registry, exact Obsidian heading text and stable block anchors for
non-heading records. The audit repaired a claim link that targeted the paper
registry, two claim links that targeted the working model, and the previously
referenced-but-absent `RL-BIOM-001` research line. The subsequent migration
closed all **234** historical shorthand/title mismatches; the five canonical
claim-registry edits were propagated by `BATCH_COMMIT`, without scientific
changes.

Content fixes must preserve registry cardinalities and must not weaken either
privacy scanner. After a content-owner correction, rerun:

```bash
python3 scripts/run_release_regressions.py
python3 scripts/public_release_gate.py \
  --root . --mode staging --skip-clean-clone
python3 scripts/independent_privacy_scan.py .
```

## Losslessness classification of private-only roots

The following are intentional exclusions, not public capability loss:

- live operational logs, inboxes, staging, caches, backups and full texts;
- personal/case overlays and source reports;
- vendored third-party repositories, environments, model weights and local
  plugin settings;
- implementation-history diffs and superseded snapshots.

Their reusable public-safe capability is represented by protocols, skills,
agents, tests, the learned-gates registry, the external workshop manifest and
provenance/licensing documentation. No private-only source tree should be
copied wholesale to close a manifest row.

## Clean-clone hold

The staging directory is not yet a Git repository. Do not initialise it merely
to satisfy the hostile-review procedure. A disposable candidate created under
`/tmp` passed the earlier regression inventory, LINT, both privacy scanners
and the gate, but predates the completed link migration and fresh-clone reader
contract. Its SHA is audit evidence only and will not equal the eventual
authorised candidate. Repeat the runbook after the owner authorises creation
of the private candidate repository.
