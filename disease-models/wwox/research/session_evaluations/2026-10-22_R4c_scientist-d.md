# Batch self-evaluation — repurposing group R4 follow-up lot (R4c), scientist-d

> Written after the analytical work and before capability growth and takeaways. Not medical advice.

## Scope and executable verdict

- **Task:** `REPURP-R4C-D-20261022`, branch `task/R4-D-20261022`: card D01 rewritten from the audited recomputation; six completing receipts for partial R4 readings; three new precedent readings (one partial, one complete, one partial).
- **Receipts (staged, not in the ledger):** nine, all passing `staged_receipt_check.py` and `validate_receipt`; the three new ones are `FTR-20261022-<PMID>-01`, the six completions `-02` naming their prior receipt.
- **Manifests:** `deepdive_manifest.py` strict with `--artifact-workspace` on the shared checkout: PASS, zero gaps, for the three new and the six resumed.
- **Card:** `repurposing_bridge.py` rebuild equals the stored card; `check_cards.py` 12 packets 0 problems; `cards_early/check_cards.py` PASS; `test_repurposing_bridge.py` OK.
- **Blind audit:** 49 triples by a separate agent: 45 SUPPORTED, 4 not (1 NOT_IN_SOURCE, 3 OVERSHOOT), all narrowed; `contradicts_locator` on the three already-committed entries.
- **Held row:** the one HELD-partial row in the selection file (Chong 2023) is not closable lawfully; retry recorded.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Full text, figures, tables, supplements | Every figure of the three new papers opened as an image; appendix of the zinc pilot read in full, its protocol and the review's poster only in part (declared `captions_only`, depth partial); six resumed supplements read, their images opened (EMF images decoded by script) | strong for the six, partial for two of the three new | long protocols and four supplements still owed, named |
| Main message and contribution | Per paper in the note; for the lot: no design in R4 separates symptomatic effect from change of course | strong | none |
| Hidden gold beyond keywords | Headline versus paired change in the zinc pilot; n = 8 versus 10 in its comparator; appendix figure against text on zinc and ferritin categories; swapped figure pairing in the outcome review; supplementary cons the review omits | strong | none |
| Source parity | A consensus text and an expert-opinion review are labelled as opinion; the review's industry interests are noted | strong | none |
| DATO / INFERENZA / IPOTESI | Three leads labelled `IPOTESI` with falsifiers; the decision-tree denominator and the nanorare fit are flagged inference | strong | none |
| Existing claims touched | None; the D01 card is non-canonical | strong | none |
| Multi-hop | Registry query per PMID before reading (no record); reference lists counted not read | partial | not read |

## Persistence diagnosis

Durable ids: nine manifests, nine staged receipts, note, candidate `CC-20261022-SCIENTISTD-R4C-01`, the audit file, this file, the task JSON with `DEFAULTS_TAKEN`, the selection file's HELD-partial table updated. A future run can tell full text from abstract by the coverage per section and the fingerprints.

## Process and capability diagnosis

- **Used:** `repurposing_bridge.py`, `check_cards.py`, `deepdive_manifest.py` strict, `staged_receipt_check.py`, `docx_to_text.py`, `pdftotext`, `pdftoppm`, blind locator audit.
- **Declined:** `legend-hypothesis-forge`, `legend-safety-triage` (no compound proposed), `legend-paperqa` (external spend), `legend-discovery` (leads staged in the candidate).
- **Micro-upgrade shipped:** `framework/scripts/docx_media_extract.py` with a 4-test suite, README routing and release-battery enrolment: unchanged media from a Word supplement plus a standard-library decoder for the uncompressed EMF+ bitmap that no viewer on the host could render. Evidence: three owed Figure S1 images for a day. Logged in `capability_scout_log.md`.
- **Residual risk and next decisive act:** the owed long protocols and four supplements; the one-off PNGs of the 42446932 manifest were produced by a scratch decoder, not the shipped script (digests differ).

## Attribution census

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest validator refusals: form-feed bytes in a supplement text layer, an ellipsis-stitched quote, and a quote under 30 characters (about seven instances over four papers) | machine | no |
| B | Propositions that said more than their quote in the new manifests (a clause in a table row, an unbacked "all", a count of 67 individuals not in the image, an employer description, a tree-leaf denominator, a curve-step count): the first group fixed in my own word-level pass before commit (about twelve), four reached the blind audit | self (twelve), blind auditor (four) | would have |
| C | Peer or earlier-commit overlap: none found this lot | n/a | n/a |
| D | Card text first drafted with dose-like figures; the card checker refuses digit-plus-unit tokens | machine | no |
| E | The supplement wording first claimed `supplementary: read` for a protocol read only in part; corrected to `captions_only` before building | self | would have |

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 2   blind_auditor: 1   peer: 0   self: 2
severity_high: 1   of which self: 1
undetected_known: 0
```

**Reading of the census.** The blind audit again found overshoots in propositions that had passed my own pass, all of them in figure readings or in clauses whose quote covered only part of the sentence; the pass is worth keeping but is not a substitute for the audit. The one high-severity item (a coverage claim larger than the reading) was caught by re-reading the coverage line against what had been opened.
