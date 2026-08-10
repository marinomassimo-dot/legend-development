# Proposal handoff to Plan — evidence-pair ratchet

This file is a proposal only. Codex does not land or merge the shared validator change.

## Adopted representation

For a `text_contradicted_by_panel` contradiction, both locator entries carry the same
`evidence_pair` key. Exactly two entries share that key: one textual surface and one `figure`
surface. A symmetric shared key is easier to verify than `id + paired_with` pointers.

The locator vocabulary is:

- `text_only`
- `text_and_panel_agree`
- `panel_only`
- `text_contradicted_by_panel`

Useful invariants from the withdrawn Codex implementation:

- `panel_only` requires `surface=figure`;
- `text_only` cannot use `surface=figure`;
- `text_contradicted_by_panel` requires `evidence_pair`;
- each `evidence_pair` identifies exactly two contradiction entries;
- the pair contains exactly one figure artifact and one textual artifact.

## Missing ratchet work owned by Plan

1. Keep fields optional for legacy manifests, but fail closed for locators created after the
   chosen schema/rule activation point.
2. Map pre-existing entries without a known relation to `unknown_legacy`, without inventing panel
   inspection or pair membership.
3. Add a growth anchor counting unresolved/unknown legacy entries; the count may only decrease.
4. Remap actor A's surface-inferred contradictions and actor B's `id + paired_with` records to the
   shared `evidence_pair` representation in one coordinated change.
5. Land validator, tests, schema/protocol text and remapping together, avoiding concurrent edits
   to shared framework files.

Reference implementation history is available in branch commit `ff6d2d6`; commit `56222fd`
withdraws those framework changes while retaining the manifest data that motivated them.
