# Batch self-evaluation — wave 4, group W2 second half, scientist-d

> Written after the analytical work and before capability growth and takeaways. Not medical advice.

## Scope and executable verdict

- **Task:** `W4-W2B-D-20261019`, branch `task/W4-W2B-D-20261019`; 8 papers read in full, none parked.
- **Receipts (staged, not in the ledger):** `FTR-20261019-<PMID>-01` for the eight PMIDs in `wave4_scientist-d.md`; all `complete_fulltext_read`; each validated in isolation.
- **Manifests:** `deepdive_manifest.py` strict with `--artifact-workspace` on the shared checkout returned PASS, zero gaps, for all eight.
- **`session_self_eval.py --workspace . --disease wwox`:** `VERDICT: PASS`, `unread_premises: 0/0`; the `[DECLARED GAP]` lines belong to other PMIDs.
- **`fulltext_receipts.py verify`:** OK, 624 chained receipts. **`legend_lint.py`:** no BLOCK; pre-existing `UNLINKED_SUPPORT` warnings only.
- **Blind audit:** 30 triples, separate agent: 24 SUPPORTED, 2 SUPPORTED with note, 4 OVERSHOOT (3 minor); all narrowed before commit.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Full text, figures, tables, supplements | Every figure of every paper opened as an image (publisher numbering mismatches found in three); all tables read; one supplement DOCX and one PDF page read | strong | none |
| Main message and contribution | Stated per paper; the group message is negative (no WWOX evidence on seven axes) plus one positive: three WWOX case rows in Agarwala 2023 | strong | none |
| Hidden gold beyond abstract | Agarwala's WWOX rows (selection file said substitute, no record); CTX and ketogenic-bone reviews' internal numeric inconsistencies; the folate pair's opposite statements on folic acid | strong | none |
| Source parity | Reviews, one trial, case reports and one prospective cohort labelled as such; group assessment declares weighting per manifest | strong | none |
| DATO / INFERENZA / IPOTESI separation | Four leads labelled `IPOTESI`; the exome-missed deletion is flagged an inference | strong | none |
| Existing claims touched | None; no registry claim op | strong | none |
| Multi-hop | Gene-direct references of Agarwala resolved or queued; other reference lists counted, not read | partial | reference lists of the seven substitutes not read |

## Persistence diagnosis

Durable ids: eight manifests, eight staged receipts, note, candidate `CC-20261019-SCIENTISTD-W4B-01`, this file, task JSON with `DEFAULTS_TAKEN` and `STOP_LOG`. A future run can tell full text from abstract: fingerprinted artefacts, coverage per section, locators verified on the body surface.

## Process and capability diagnosis

- **Used:** `pubmed_identity_check.py`, `deepdive_manifest.py` strict, `dependency_integrity.py screen`, `registry_records.py`, blind locator audit, `session_self_eval.py`.
- **Declined:** `legend-deepdive` (inline), `legend-discovery`, `legend-safety-triage` (no compound proposed), `legend-paperqa` (external spend).
- **Micro-upgrade shipped:** `scientist_operating_practice_v1.md` Phase 5 gained the figure-numbering trap and the 2026-deposit routes; logged in `capability_scout_log.md`. Evidence: three of eight papers had publisher files whose numbering or attached image did not match the legend.
- **Residual risk and next decisive act:** the manifests' propositions about Agarwala's WWOX rows rest on a published table; the primary reports (Piard 2019 manifest exists; Surana 2020 queued) are the next read.

## Attribution census

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest validator refusals: `user_agent_policy` value outside the closed list, quote only in the abstract, quote broken by italic markup, quote under 30 characters, unresolved gene-direct references, a mistyped quote (6 instances over 4 papers) | machine | no |
| B | Selection file labelled Agarwala 2023 a substitute with no record; the XML has eight WWOX mentions and three WWOX case rows | self (counting WWOX in the text surface) | would have |
| C | Publisher figure numbering or caption-image pairing wrong in three deposits | self (opening every image) | would have |
| D | My text converter returned zero characters for a JATS with untitled sections | self (noticing the empty output) | no |
| E | Four propositions said more than their quote (a "no annotations" and "continuous EEG" figure reading; a review label for a citation; "did not change"; a wider inference from one normal screen) | blind auditor | would have |

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 1   blind_auditor: 1   peer: 0   self: 3
severity_high: 2   of which self: 2
undetected_known: 0
```

**Reading of the census.** The two high-severity incidents were caught by my own cross-measurement, not by a validator: the validator checks that a quote exists, not what the paper contains elsewhere or which legend an image belongs to. The blind auditor again found overshoots in propositions I had re-read myself, so the audit stays worth running on figure readings in particular.
