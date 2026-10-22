# Batch self-evaluation — repurposing group R4 third lot (R4d), scientist-d

> Written after the analytical work and before capability growth and takeaways. Not medical advice.

## Scope and executable verdict

- **Task:** `REPURP-R4D-D-20261022`, branch `task/R4d-D-20261022`: the P5 comparison's exposure wording re-sourced to the audited D01 card; seven completing receipts for partial R4 readings; two limits paragraphs for cards drawing on the zinc pilot and the antisense consensus.
- **Receipts (staged, not in the ledger):** seven `FTR-20261022-<PMID>-02`, all passing `staged_receipt_check.py`; each names its prior receipt with `reread_reason: inadequate_prior_coverage`.
- **Manifests:** `deepdive_manifest.py` strict with `--artifact-workspace` on the shared checkout: PASS, zero gaps, for all seven.
- **P5:** `p5_check.py` 203 cells, 0 problems; verdict unchanged.
- **Blind audit:** 87 triples by two separate agents: 30 SUPPORTED, 57 NARROW, none unsupported; all narrowed; one figure value read differently by the auditor and corrected.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Full text, figures, tables, supplements | Five figures of 39439575 obtained from the image CDN named in the saved page and opened; two long protocols read (39625912 to page 47 plus scanned approvals as images; Data S2 of 41999155 after stripping reference-manager payloads); 39762914's protocol read in selected sections only | strong for four, partial for 39762914 and 35499850 | 39762914 sections 5.2-5.4, 5.6, 6, 8, 10, 11, 13+; eTable 1 of 39439575 unavailable |
| Main message and contribution | Per paper in the note; protocols differ internally (endpoint definitions, analysis-set names, durations) | strong | none |
| Hidden gold beyond keywords | The CGI-I endpoint defined three ways; alpha printed as 0.5; a figure p value differing from the text; the missing statistical analysis plan | strong | none |
| Source parity | Protocols, a consensus text and a pilot are labelled as such; the zinc and antisense limits paragraphs say what a card must not infer | strong | none |
| DATO / INFERENZA / IPOTESI | Three leads `IPOTESI` with falsifiers; the salt-base reading and the alpha slip are flagged inference; my own counts are marked unaudited | strong | recount of the 82, 21/75 and 37 row counts |
| Existing claims touched | None | strong | none |
| Multi-hop | Not extended; reference lists not read | partial | not read |

## Persistence diagnosis

Durable ids: seven manifests, seven staged receipts, note, candidate `CC-20261022-SCIENTISTD-R4D-01`, the audit file, this file, the task JSON with `DEFAULTS_TAKEN`, the selection file's HELD-partial rows updated. A future run can tell full text from abstract by coverage per section and fingerprints.

## Process and capability diagnosis

- **Used:** `build_p5.py`, `p5_check.py`, `deepdive_manifest.py` strict, `staged_receipt_check.py`, `pdftotext`, `pdftoppm`, `docx_to_text.py`, `xlsx_to_text.py`, ImageMagick, blind locator audit by two agents.
- **Declined:** `legend-hypothesis-forge`, `legend-safety-triage` (no compound proposed), `legend-paperqa` (external spend), `legend-discovery` (leads staged in the candidate).
- **Micro-upgrade:** none (CHANGE = NONE); the resume-manifest helper and the figure-fetch step are scratch code, named in the scout log.
- **Residual risk and next decisive act:** the audit's strict reading made 57 of 87 propositions narrower; a Scientist drafting future propositions should write them from the quote, not from the section. The remaining unread protocol sections of 39762914 and the unavailable eTable 1.

## Attribution census

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest validator refusals: form-feed bytes, quotes under 30 characters, an ellipsis-stitched quote, a wrong user-agent policy word, a quote broken by a page-break line | machine | no |
| B | Propositions that said more than their quote: about eight fixed in my own pass before the audit; 57 more found by the blind audit under the strict rule (borrowed subjects and predicates, counts, stronger figure wording) | self (eight), blind auditor (57) | would have |
| C | Wrong paper identifications in the first draft of the note (a fenfluramine trial named as cannabidiol, a systematic review named as a cohort) | self (re-read the article titles) | would have |
| D | A coverage claim `complete` for a protocol whose scanned pages were unread, corrected by opening the pages | self | would have |
| E | Duplicate locator entries on a rerun of the resume builder, found by the count check | self | no |

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 1   blind_auditor: 1   peer: 0   self: 3
severity_high: 1   of which self: 1
undetected_known: 0
```

**Reading of the census.** The blind audit's strict reading again found a large group of overreaches (57 of 87) that were mostly borrowed context rather than errors of fact; one figure value was actually misread by me. The pass of my own is not a substitute for the audit. The one high-severity item (a wrong paper identity in the first note draft) was caught only because I re-read the article titles.
