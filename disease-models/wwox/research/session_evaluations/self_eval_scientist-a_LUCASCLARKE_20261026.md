# Self-evaluation — scientist-a — published Lucas-Clarke 2026 (PMID 42909904) — 2026-10-26

## Scope and executable verdict

- Batch/session: one-paper full reading, MODE A, `SOURCE_FIRST` then `QUESTION_DRIVEN` comparison, branch `task/sci-a-lucasclarke2026`.
- Studies and receipt IDs: PMID 42909904, `FTR-20261026-42909904-01` (staged, `complete_fulltext_read`, supplementary `read`, limitations `not_present`).
- `session_self_eval.py`: PASS (every complete read has landed, every declared output resolves).
- Per-study manifest: `deepdive_manifest.py --verify-artifacts --require-current-schema --artifact-workspace <shared root>` PASS, 0 gaps, 104 locators; `paper_packet.py check` ok on the manifest, "flag drift" established nothing (not a pass).
- Receipt verification: `staged_receipt_check.py --check-doi` verdict OK; nothing was recorded (parallel-wave rule).
- Structural LINT: WARN, no BLOCK (the pre-existing UNLINKED_SUPPORT warnings are not mine).
- Local verdict: green for this paper. Workspace verdict: not claimed.

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full text, figures, tables, supplements | 19-page PDF read in order; 8 main figures rendered at 300 dpi (vector-flagged pages); supplementary docx figures 1-8 viewed, tables 1A, 1B, 2-7 read through the flattened workbook | strong | MetaboLights MTBLS12344 and ArrayExpress not retrieved; Supp Table 2 (sleep matrix) read for presence only |
| Main message and original contribution | chain Wwox-Atf4-Ldh-lactate is measured at two nodes and inferred at the Atf4-Ldh arrow; one causal experiment (Ldh double RNAi) | strong | |
| Hidden gold beyond keywords | lactate is conditional (-0.43 log2 without amyloid, +1.30 with); glycolytic transcripts fall with Wwox OE; Aβ42 cohort in OE experiment has no lactate rise; sima reporter described three ways; KK RNAi line dropped; text-versus-table Ldh 1.19 versus 1.1097 | strong | |
| Source parity | preprint read in full for the comparison only after the first-pass observations were fixed | strong | |
| Team type, field density | experimental AD/fly laboratory, first Wwox encounter; PubMed counts measured | strong | |
| Tag separation | each locator carries the NOT-WWOX-DEE label; reader findings typed INFERENZA in the dossier | partial | quote-less absence findings (no Pdk/Pdha/Pdhb in lists; no pyruvate row) live in the dossier, not in locators |
| Existing claims touched | PAPER 158 two statements, DL-MECH-020 chain, CLAIM 025 wording, DL-BIO-008 | partial | narrowing items are OWED a blind audit by someone else; none run |
| Multi-hop and corpus cross-query | 71 refs enumerated; ref 43 (Atf4-dependent Ldh in flies) named, not read | partial | hop to that paper not made |

## Persistence diagnosis

- Durable IDs: dossier `fulltext_dossiers/PMID42909904.md`, manifest, candidate `CC-20261026-SCIENTIST-A-LUCASCLARKE-01`, two staged leads under `lead_staging/scientist-a/`, staged receipt.
- Reading debt: blind audit of narrowing items; MetaboLights retrieval.
- Receipt fingerprint: PDF sha256 abab045e2403c2781a25ca7f2146de056fab081e4158e86a337066cfac8c4e1a; the XML, the supplementary zip, docx, xlsx and derived text are fingerprinted in the manifest.
- Full text versus abstract only: `evidence_depth: complete_fulltext_read` with a 64-hex fingerprint and body locators on the structured XML.

## Process and capability diagnosis

- Skills/gates used: `paper_packet.py packet/claim/rank/check`, `deepdive_manifest.py`, `locator_audit.py --strength-scan`, `xlsx_to_text.py`, `dependency_integrity.py`, `staged_receipt_check.py`, `registry_records.py` (selective, `--json`).
- Declined: `legend-locator-audit` (no existing locator contradicted; the owed audit is for the narrowing proposals), `legend-deepdive`.
- Failures: (1) first manifest passed the validator while 51 of 86 propositions carried numerals absent from their quotes — the validator proves a quote exists, not that its numerals cover the proposition; caught by my own scan, not by a machine gate; (2) the validator refused a quote whose text came from a normalised plain-text window (UNVERIFIABLE_PUNCTUATION) and had to be re-captured; (3) the operator's premise that the published version "adds metabolomics and Ldh work" was false, found only by reading the preprint text itself.
- Disease-agnostic micro-upgrade shipped: none; the gap is recorded with evidence rather than patched — a standalone numeral-in-quote scan does not exist in `framework/scripts/` (the docstring of `locator_audit.py` says one stands); the one used here is a 12-line script kept in the session scratchpad.
- Residual risk and next decisive action: blind audit of the narrowing proposals; fetch MTBLS12344 to settle pyruvate.

## Attribution census — required, fixed, parseable

```
ATTRIBUTION_CENSUS
incidents: 3
machine: 1   blind_auditor: 0   peer: 0   self: 2
severity_high: 0   of which self: 0
undetected_known: 0
```

## §21c output

`DEFAULTS_TAKEN`: took the published PDF as the evidentiary surface and the Europe PMC XML for quote matching; classified the work ORDINARY; staged but did not record the receipt; staged two leads rather than writing the ledger. `STOP_LOG`: none; no stop condition arose. (No task contract JSON was dispatched for this one-paper task, so these are recorded here.)
