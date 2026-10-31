# cards_early_it13_p22 — why `cards_early/check_cards.py` fails, and the minimal repair (IT13, P2.2)

## Decision

* **Seven cards fail, not eight** (nine packets; `EB-KD-01` and `EB-ETX-01` already pass). Failing:
  `EB-CBD-AX-01`, `EB-DEV-AX-01`, `EB-GROWTH-AX-01`, `EB-HORM-AX-01`, `EB-MTOR-AX-01`, `EB-PDANCHOR-AX-01`,
  `EB-VGB-01`. The only failing check is #1 (stored card == what the bridge builds now); every other check
  (P4 fields, forbidden keys, quotes, labels, candidate/abstention rules) passes. Reason: the bridge now emits
  `endpoint_outcomes`; six cards predate it (missing key, value `[]`), and `EB-VGB-01` additionally has a
  **stale `input_sha256`** (see below).
* **Classification: all seven are ACTIVE and DERIVED, none HISTORICAL.** Each card is exactly
  `bridge.build_card(packet)` plus the missing field, and each is consumed (evidence below).
* **Action: regenerate those seven through the unmodified bridge** (done into `regenerated/`; one proposed
  patch). No pre-baked field added, no manual information lost: the semantic diff shows only
  `endpoint_outcomes` added (and the VGB digest corrected). With the patch applied the checker prints `PASS`
  (verified on a scratch copy, which was removed).
* **The checker is not wrong.** Check #1 does its job and caught a real defect (the VGB digest). Two
  improvements, proposed but not applied (no silent weakening): (a) on mismatch print the differing top-level
  keys, so version skew (key added by the bridge) reads differently from a hand edit; (b) it is not wired into
  any battery (no suite calls it), which is why it drifted silently since the bridge change.

## Diagnosis

`python3 cards_early/check_cards.py` (before): `packets checked: 9`, FAIL on the seven above, one message each:
"stored card differs from what the bridge builds from the packet now". Per-card differing top-level keys
(`semantic_diff_it13_p22.py`):

| Card | kind | differs in | after regeneration |
|---|---|---|---|
| EB-CBD-AX-01, EB-DEV-AX-01, EB-GROWTH-AX-01, EB-HORM-AX-01, EB-MTOR-AX-01, EB-PDANCHOR-AX-01 | abstention | `endpoint_outcomes` absent | `[]` (no drug assertion, so no endpoint question) |
| EB-VGB-01 | candidate | `endpoint_outcomes` absent **and** `input_sha256` stale | 1 question, see below |

**EB-VGB-01 digest.** Commit `d1538c97` (VABAM wording) edited one sentence in the packet and the same sentence in
the card's embedded `input`, by hand, without rebuilding: the card's `input` equals the packet's content but its
`input_sha256` is the digest of the pre-edit packet. So the stored provenance hash did not describe the stored
input. Regeneration fixes that and nothing else (test `test_vgb_stored_sha_was_stale...`).

## Classification evidence (ACTIVE)

* `catalog/card_links.json` links all seven (`cards_early/<id>.card.json` + `.packet.json`); `catalog/catalog_build.py:1773`
  globs `cards_early/*.json`.
* `framework/scripts`: `repurposing_join.py` (CURATED_CARDS_EARLY), `repurposing_view.py` (80, 1038, 1828),
  `repurposing_coverage.py` (94, 486: the `cards_and_packets` input digest hashes every file in `cards_early/`),
  `repurposing_shareable_audit.py` (336); `p5/build_p5.py:134` reads the `.card.json`; `coverage_it11_p21_20261031/phenotype_first_it11.py:83` reads the packets.
* `needs/needs.json` (17 hits) and `needs/check_needs.py:79` require `cards_early/<id>.card.json` to exist.
* `ranking_it8_p9_20261029`: `EB-VGB-01` is a member of unit U20 (`unit_map.tsv`, `unit_members.tsv`, `ranking.json`, reason classes P3/C2);
  the abstention axes are linked through needs/README Q-N rows.
* DERIVED: `bridge.build_card(packet) == regenerated card` for all seven (test `test_equals_bridge_output`).

## Semantic before/after (regeneration)

| Dimension | Change |
|---|---|
| Evidence (`comparisons`, `directional_summary`) | none; summary `UNRESOLVED` before and after on all seven |
| Endpoints | `endpoint_outcomes` added. Abstentions: `[]`. VGB: one question (`epileptic_spasms` / clinical cessation of epileptic spasms / WWOX-DEE with West syndrome or infantile spasms / WWOX-null class / human / whole organism / infancy; no discriminators) with `statuses=[OPPOSES_DISEASE_CHANGE]`, `assertion_ids=[A-VGB-1, A-VGB-3]`, `discriminators_declared=false`. Nine other VGB rows stay `UNRESOLVED`; nothing promoted. `A-VGB-1` is not additionally counted with `A-VGB-2` (one reporting origin, two patients; unchanged README wording) |
| Contexts (`input`, `p4_fields`, `translation`, `label_lookup`) | identical |
| Nulls (`NO_CHANGE` rows A-VGB-5/6, `limits` text, `NOT_ATTEMPTED` label lookup) | identical; the two reported nulls remain `UNRESOLVED` (non-comparable cell), not erased and not turned into `NO_EFFECT_REPORTED` |
| Provenance | `input_sha256` identical on six; VGB corrected to the digest of the current packet |

Reading of the new VGB field: it records that the single comparable question has one sign from case reports
with undeclared timepoint/level; it is a sign comparison, **not efficacy** (README `cards_early` "How to read a
bridge result"; CLAIM 031 unchanged).

## Files

* `regenerated/*.card.json` — the seven cards, built by `framework/scripts/repurposing_bridge.py <packet>`; originals untouched.
* `proposed_cards_early_regeneration.patch` — `git apply --check` clean against `dbc8e7c3`; replaces the seven cards.
* `semantic_diff_it13_p22.py` — read-only diff and assertion that only `endpoint_outcomes`/`input_sha256` differ.
* `test_cards_early_it13_p22.py` — 8 targeted tests (bridge equality, key-set diff, empty outcomes on abstentions, VGB question, stale digest, no pre-baked field, KD/ETX unchanged). Passing.
* `test_structured_data_integrity.py` run read-only on this tree: `Ran 4 tests ... OK`.

## Edits this implies (for the Orchestrator; not done here)

1. `git apply` the patch to `cards_early/` (seven files). Add the line "regenerated 2026-10-31 through the bridge; `endpoint_outcomes` added" to `cards_early/README.md` if wanted (not required).
2. Derived surfaces become stale by construction: `repurposing_coverage.inputs_digest["cards_and_packets"]` changes (it hashes `cards_early/*.json`), so coverage/priorities, `join/cards.json` (if it embeds the cards) and the view/shareable package need the usual regeneration after landing. No consumer reads `endpoint_outcomes` from these cards except `wwox_marginal_value_it8_p4_20261029/classify_inputs.py:162`, which tolerates absent/empty (`or []`); the ranking snapshot's card-derived counts are not expected to change, to be confirmed by the integrator's regeneration.
3. Optional harness note: add `check_cards.py` to a regression suite and print differing keys on mismatch; record that any later hand edit of a packet requires a bridge rebuild (the VGB digest drifted this way).

## What a verifier needs

The decisive datum: rerun `python3 cards_early/check_cards.py` after `git apply` of the patch and see `PASS`; and `python3 semantic_diff_it13_p22.py` showing the differing keys are only `endpoint_outcomes` (+`input_sha256` for VGB). Not verified here: that downstream regenerated surfaces (view, coverage, ranking) stay semantically unchanged; no source was re-read, no quote re-checked beyond the checker's own check #5 (which passes).
