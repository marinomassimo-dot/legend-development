# Proposal handoff to Plan — panel/text relation, evidence-pair and artifact-workspace ratchet

This file is a proposal only. Codex does not land or merge the shared validator change.

## Adopted representation

The field is named `panel_text_relation`, not `evidence_relation`. The latter is already an
identity-bearing DisMech field with the orthogonal vocabulary `SUPPORT | PARTIAL | REFUTE`;
the two layers meet in `derive_dismech_sidecar.py` and must not collide.

For a `text_contradicted_by_panel` contradiction, both locator entries carry the same
`evidence_pair` key. Exactly two entries share that key: one textual surface and one `figure`
surface. A symmetric shared key is easier to verify than `id + paired_with` pointers.

The definitive `panel_text_relation` vocabulary has five values:

- `text_only`
- `text_and_panel_agree`
- `panel_only`
- `text_contradicted_by_panel`
- `unknown_legacy` — reserved for explicit backfill of locators that predate the field

`unknown_legacy` is a value, not an absent field. Absence must mean that a new locator forgot
the obligation; otherwise the ratchet cannot distinguish legacy debt from a regression.

Useful invariants from the withdrawn Codex implementation:

- `panel_only` requires `surface=figure`;
- `text_only` cannot use `surface=figure`;
- `text_contradicted_by_panel` requires `evidence_pair`;
- each `evidence_pair` identifies exactly two contradiction entries;
- the pair contains exactly one figure artifact and one textual artifact.

## Missing ratchet work owned by Plan

1. Require the field for every locator after the chosen schema/rule activation point; absence
   fails closed. Backfill every older locator explicitly as `unknown_legacy`.
2. Map pre-existing entries without a known relation to `unknown_legacy`, without inventing panel
   inspection or pair membership.
3. Add a growth anchor counting unresolved/unknown legacy entries; the count may only decrease.
4. Remap actor A's surface-inferred contradictions and actor B's `id + paired_with` records to the
   shared `evidence_pair` representation in one coordinated change.
5. Land validator, tests, schema/protocol text and remapping together, avoiding concurrent edits
   to shared framework files.

Reference implementation history is available in branch commit `ff6d2d6`; commit `56222fd`
withdraws those framework changes while retaining the manifest data that motivated them.

## Artifact-workspace adoption

Adopt the already demonstrated two-root validator interface in the same Plan-owned landing:

- `--workspace` resolves the versioned manifest and receipt ledger;
- `--artifact-workspace` resolves and containment-checks the persistent evidence tree;
- omitting it preserves the original single-root, fail-closed behaviour;
- symlinks escaping the selected evidence root remain invalid;
- receipt persistence receives the same explicit artifact root;
- tests cover default single-root operation, valid split-root operation, missing artifacts,
  hash mismatch and path escape.

This solves the recurring topology in which `files/` is gitignored and lives only in the shared
checkout while manifests travel on actor branches. The validation report must always name both
roots; a bare `PASS` is insufficient provenance.
