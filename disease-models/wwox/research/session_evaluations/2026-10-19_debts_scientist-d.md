# Batch self-evaluation — reading debts, WWOX-direct primaries, scientist-d (2026-10-19)

> Written after the analytical work and before capability growth and takeaways. Not medical advice.

## Scope and executable verdict

- **Task:** `DEBT-WWOX-DIRECT-D-20261019`, branch `task/DEBT-WWOX-DIRECT-D-20261019`. Eight papers read (four complete, four partial), fifteen parked with the cascade run.
- **Staged receipts:** `FTR-20261019-<PMID>-01` for the eight PMIDs of `debts_wave_20261019_scientist-d.md`, each validated in isolation (`validate_receipt` and `validate_new_receipt`: OK); none appended.
- **Manifests:** `deepdive_manifest.py --verify-artifacts --require-current-schema --artifact-workspace <shared root>` PASS, zero gaps, for all eight; `paper_packet.py check --artifact-workspace` ok on the validator, erratum scope and undeclared-revision checks, and "flag drift" established nothing (not a pass, said so).
- **Locator revision check:** `locator_contradiction_audit.py --working-tree --fail-on-undeclared` clean after one declared self-correction.
- **Global gates** (`session_self_eval.py`, `fulltext_receipts.py verify`, `legend_lint.py`) are run at landing; results in the task JSON note if they differ.

## Content diagnosis

| Dimension | Answer | Grade |
|---|---|---|
| Full text section by section, figures as images | Whole body of all eight; every figure of every paper opened as an image (page renders or blob JPEGs); tables read as text and compared with renders (Chen 2018, Lee 2017). Four archived-PMC readings leave supplements `not_read`, declared. | strong, supplements open |
| Against the disease label | The papers are cancer, leukaemia and cell-line biology; the question asked of each was what it measures about mitochondria, metabolism and loss of function. Two Zfra and TGF-beta papers read for what they cannot show (no Wwox-null cell). | strong |
| Found that a gene keyword search would not return | The Hong 2007 mitochondrial pointer ends at a "submitted" paper; Lin 2011 knockdown significance contrast; Huang 2016 fractionation without a marker row; Lee 2017 GTEx class sizes implying a different allele; Huang 2018 "conditional" misnaming. | strong |
| Group and evidence type | Chang laboratory (primary for WWOX stress signalling, not for loss of function) and Richards laboratory (reviews of its own Drosophila work); two clinical-genetic HCC cohorts; weighted observation over interpretation per manifest. | strong |
| Field density | PubMed `rettype=count`, dated, per manifest. | adequate |
| DATO/INFERENZA/IPOTESI separation | Leads L1-L4 are `IPOTESI` with falsifiers; the Lee 2021 "treatable via compensation" is labelled `IPOTESI`; no hypothesis promoted. | strong |
| Existing claims touched | `CLAIM 009` annotation, MINOR, dry-run clean; `CLAIM 026` not moved. | strong |
| Multi-hop | Reference lists enumerated from the artefact or the Europe PMC references endpoint; gene-direct items resolved to receipts or queued; the debt chain followed to primaries (Lin 2011, Huang 2016) behind two review sentences. | strong |

## Persistence

Manifests, staged receipts, analysis note, commit candidate (op list, registry placeholders, wishlist, queue proposals, leads), this file, task JSON with `DEFAULTS_TAKEN` and `STOP_LOG`, scout-log entry, regression test. The discovery ledger is not appended (single writer).

## Process and capability

- Used: `pubmed_identity_check.py`, `paper_packet.py`, `deepdive_manifest.py`, `dependency_integrity.py --manifest-block` (run from the shared checkout against the task worktree's manifest directory, because the snapshot lives in the shared `files/`), `registry_records.py`, `record_scoped_edit.py` dry run, `locator_contradiction_audit.py`, a blind auditor agent.
- Declined: `legend-discovery`, `legend-hypothesis-forge`, `legend-safety-triage` (no lever matured), `legend-paperqa` (external spend).
- **Micro-upgrade:** `pubmed_identity_check.py` read a cited paper's DOI as the article's own (false TITLE_MISMATCH on a clean record); fixed with a regression test. Disease-agnostic.
- Friction: Europe PMC XML HTTP 500 for author-manuscript PMC deposits (archived page route used); publisher bot challenges on ScienceDirect, AACR, JBC, MDPI and BioMed Central counter URLs; Internet Archive and Semantic Scholar HTTP 429 (backed off); a subagent-free browser route was not available.

## Attribution census

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest validator refusals: `research_type` outside the closed list; `resolved_url` with an `@` in a recipe; flagged-dependency `citing_relation` placeholder; locator quote found only in the abstract (Huang 2018 Impact statement) or with a changed wording ("10 minutes" against "10 min") — one instance class each, nine instances | machine | no |
| B | `pubmed_identity_check.py` false TITLE_MISMATCH on a clean record | self (I opened the PubMed XML and saw the correct DOI before believing the verdict), then fixed | no |
| C | Receipt validator: `event_at` missing in isolation | machine | no |
| D | Wrong first author written for PMID 25411445 ("Piard", it is Mignot) in the commit candidate; and a "cited by four read papers" count not backed by a command | self (re-checked author names with esummary before landing) | would have |
| E | Hsu 2009 DOI/figure URLs in recipes; a figure artefact path name guessed (`Aldaz2021` for a Lee 2021 file) | self (esummary first-author check; renamed before use) | would have |
| F | Overshoot in a committed locator proposition: Lee 2021 "region, not the gene; neither a metabolic disease" | blind auditor | would have |
| G | Reference type of four Huang 2018 references stated without a printed type | blind auditor | would have |

```
ATTRIBUTION_CENSUS
incidents: 7
machine: 2   blind_auditor: 2   peer: 0   self: 3
severity_high: 4   of which self: 2
undetected_known: 0
```

**Reading of the census.** Two of the four incidents that could have reached the record were caught by the blind auditor and two by my own re-check; none by a validator. The validators caught only malformed declarations. The two auditor catches are the ones that matter: both were propositions that said slightly more than their source, written by me and passed by every gate. `undetected_known: 0` cannot be trusted; absence claims ("the paper contains no X") are the class most likely to hide an error and were audited for only five of the papers.

---

# Wave 2 addendum (2026-10-20): the open unread gene-direct items of my own queue list

## Scope and executable verdict

- Nine readings under `DEBT-WWOX-DIRECT-D-20261019` wave 2: six new (Tabarki 2015, Hsu 2016, Lee 2015, Zhang 2012, Cheng 2016, Ekizoglu 2015) and three resumes of partial receipts (Li 2009, O'Keefe 2015, Tsai 2013). Staged receipts `FTR-20261019-<PMID>-01` for the six and `-02`, `-02`, `-03` for the resumes; all validated in isolation; none appended.
- All nine manifests `PASS` against the shared evidence tree; `locator_contradiction_audit.py --working-tree --fail-on-undeclared` clean. Global gates are run at landing, which the coordinator has deferred (branch kept committed, not landed).

## Content diagnosis (differences from wave 1 only)

| Dimension | Answer | Grade |
|---|---|---|
| Figures as images | Every figure of every new paper opened (page renders or blob JPEGs); resumes opened the supplementary figures, using PyMuPDF where ImageMagick crashes on the TIFFs. | strong |
| Supplements | Two new papers leave supplements not read (declared); a deposit defect (another article's supplement under one PMID) was repaired by finding the article's own supplement on the publisher's page, which supersedes an earlier "not retrievable". | strong |
| Duplicate-work gate | Two entries on my own queue list were wrong (a paper already resumed by a peer; one already complete). Caught by checking worktrees and the ledger before reading. | adequate |
| Existing claims touched | None annotated; one queue-record status op (`FT-090`), dry-run clean. | strong |
| Multi-hop | Reference lists enumerated; gene-direct items resolved to receipts or queued or parked; two un-triaged. | adequate |

## Attribution census, wave 2

| # | Incident | Caught by | Reached the record? |
|---|---|---|---|
| A | Manifest validator: unfilled `citing_relation` placeholder for a flagged dependency (one class, one instance) | machine | no |
| B | My queue list named Hong 2009 as unread and Park 2004 as unreceipted; the first had been resumed by a peer, the second was complete | self (status check and worktree search before reading) | would have (duplicate reading) |
| C | A first draft of the candidate carried counts "cited by five/seven read papers" and "worked eleven times" that no command supported | self (re-read the candidate against what I had run) | would have |
| D | Proposition in the Cheng manifest said a promoter reporter "reports transcriptional output" as fact | blind auditor | would have |
| E | Proposition in the Tabarki manifest said "the only reference to metabolism" while the abstract has an uncited metabolic phrase | blind auditor | would have |
| F | Hsu 2016 proposition called a family study a case report | blind auditor | would have |
| G | Italian text in a draft registry op (the queue file is Italian; my instruction is English files) | self (re-read the op before applying) | would have |

```
ATTRIBUTION_CENSUS
incidents: 7
machine: 1   blind_auditor: 3   peer: 0   self: 3
severity_high: 6   of which self: 3
undetected_known: 0
```

**Reading of the census.** Half of the incidents that could have reached the record were caught by the blind auditor, and all three auditor catches are propositions that went a clause beyond their source: a mechanism inferred, an absence stated as "only", a type mislabelled. That is the same class as wave 1. The practice that worked was running the auditor on eight triples before committing, which let the narrowings be made without a declared contradiction.

## Micro-upgrade of the wave

Not a code change this time: the capability scout log gains the proven route for author-manuscript PMC deposits and the TIFF-render workaround (see `capability_scout_log.md`).
