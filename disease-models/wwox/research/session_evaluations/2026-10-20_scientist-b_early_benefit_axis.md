# Session self-evaluation — `scientist-b`, `REPURP-P3-EARLYBENEFIT-B-20261020`

> Written 2026-10-21 at the close of the early-benefit axis, **before** the capability scout and
> before the report, which is the order the protocol fixes for a reason: takeaways written first
> describe a session that went well. One completed reading (resume), one parked paper, one analysis
> note, one dossier, one commit candidate. Public, disease-level. Not medical advice.

## Part 1 — the executable gate

| Command | Verdict |
|---|---|
| `deepdive_manifest.py --pmid 36537114 --verify-artifacts --require-current-schema` | **PASS**, 0 gaps (one RATCHET: `acquisition_recipe` absent on 1 of 2 artefacts, with a stated `no_recipe` reason) |
| `paper_packet.py check --pmid 36537114` | manifest validator `ok`; erratum scope `ok`; undeclared locator revision `ok`; **flag drift `INSUFFICIENT_DATA` — established nothing, and it is not a pass** |
| `staged_receipt_check.py --check-doi` | **OK** (after one refusal, below) |
| `fulltext_receipts.py record --dry-run` | **DRY RUN OK**, nothing written |
| `fulltext_receipts.py verify` | **OK**, 680 chained receipts, tail anchored |
| `session_self_eval.py` | **PASS** — every complete read landed, every declared output resolves |
| `legend_lint.py .` | **WARN**, no BLOCK (every warning pre-existing, none from my files) |
| `public_release_gate.py` | **PASS**, 0 BLOCKS |

## Part 2 — the written judgement

**What the session was asked and whether it answered.** The question was which WOREE endpoints are
measurable and what the repository holds on each. It answered, and the answer is mostly a set of
negatives — which is the shape the contract predicted and the shape I should be most suspicious of,
because a negative is the finding this repository pays for later if it is wrong. So the three
load-bearing negatives were each given a dated, reproducible instrument: two PubMed probes for
developmental/motor instruments and for imaging/electrophysiological modalities (both zero), and one
record-level registry query for `GMFM`, `Bayley`, `Vineland`, `wearable` (zero across all surfaces).
Each is stated as what it is — an **indexing** absence — and § 2(c) of the note explains why that
qualifier is not cosmetic.

**The one thing I would have got wrong without the reading, and it is the session's best moment.** I
had written the instrument negative and was ready to carry it. The reading of the case series then
produced, from the **body and the table**, a **visual evoked potential** performed in a WOREE patient
and a **sleep study** that found apnoea with hypopnoea — against probes that return zero for VEP, ERG
and actigraphy. Had the note shipped with the unbounded sentence *«these instruments have never been
used in WOREE»*, it would have been **false**, discoverable in one full text, and it would have sat in
the record discouraging exactly the sweep that would disprove it. The repair was `self`, by reading a
primary instead of trusting a query — which is the catcher class the attribution census says to watch.

**Where I nearly overclaimed in the other direction.** My first instinct on the diet series was to
treat *«three of five responded»* as a response rate. The surface does not state how many patients
were placed on the diet; `CLAIM 042` already said so, and the reading confirmed it on the delivered
chunks. More importantly, the paper declares that **two of its five patients were previously
published and does not say which two** — so even the count of *observations* is not three. I caught
that in the summary paragraph of the last delivered chunk, on a second pass made specifically to look
for a provenance sentence. Had I stopped at the table, the commit candidate would have asserted three
independent observations.

**Coverage honesty, deliberately conservative.** Four Discussion chunks were delivered and read end
to end, and I still declared `discussion: not_read`, because chunk indices 3–17 and 19–21 are absent
and a section is not read when most of it is missing. Every quotation names its chunk index instead.
The same reasoning gave `results: not_read` with Table 1 declared `tables: read`, and
`references: not_present`, which is what made the dependency screen `UNSCREENABLE_NO_REFERENCE_LIST`
rather than a screen over a hand-reconstructed citation list — a verdict over a surrogate would have
been a verdict about a different object.

**Group assessment, observation weighted apart from interpretation.** Classified
`descriptive_clinical`: a multi-centre clinical-genetics consortium with no experimental arm, and the
senior author's single WWOX paper (234 publications, 1 on the gene; measured, with the caveat that
initials-level author strings pool homonyms). Right provenance for a phenotype and endpoint question,
wrong provenance for a mechanism — so the reading takes twelve phenotype and endpoint propositions
from it and **no mechanistic proposition at all**, including declining the gene-therapy proof-of-
concept sentence it prints.

**Friction, named rather than smoothed.** Five incidents. (1) The manifest validator rejected my
first draft on nine distinct grounds — null `resolved_url` on a pre-existing artefact, an invented
`research_type`, a derived artefact without `derived_from`/`extractor`, an unscreenable-class key I
made up, and arithmetic that did not close. The repair that mattered was recognising that the honest
answer for the gateway bytes is the schema's own `no_recipe` escape, not a reconstructed URL: I do not
know the route that session used, and inventing a plausible one would have been the worst available
outcome. (2) All twelve locators failed byte-verification against the JSON escape form; the fix was a
**declared derived text artefact with a versioned extractor**, not a loosened snippet. (3)
`staged_receipt_check` refused on `analysis_at` later than `event_at` — a real inversion in my draft.
(4) `find-fulltext`, run inline for two papers, found no lawful surface for either. (5) The parked
paper's only OA deposit answers every route with an anti-bot proof-of-work; I did not solve it,
because solving one is getting around an access control on my own authority.

**What I did not do, and should be read as a limit.** No blind locator audit. Two of my propositions
bear on `CLAIM 042`, already propagated, and one locator carries a declared surface defect — absent
minus signs on the growth SD scores — which is precisely the class `legend-locator-audit` exists for.
It is declared OWED in the commit candidate rather than quietly skipped, but an owed audit is a debt
and not a discharge. `flag drift` also established nothing.

**Where each output landed.** Manifest `deepdive_manifests/PMID36537114.json`; staged receipt
`receipt_staging/scientist-b/FTR-20261020-36537114-01.json`; dossier
`fulltext_dossiers/PMID36537114_earlybenefit_20261020.md`; candidate
`commit_candidates/CC-20261020-SCIENTIST-B-KETO-ENDPOINT-01.md` (target `CLAIM 042`,
`target_wm_version` `WM_v7.27`, **MINOR**); note
`research/repurposing_early_benefit_20261020_scientist-b.md`; this diagnosis. Three commits on
`task/REPURP-P3-EARLYBENEFIT-B-20261020`.

**Can the next run answer mechanically?** Yes: `owed_sections.py` already prints
`36537114 owed: figures=captions_only, supplementary=not_read latest=FTR-20261020-36537114-01
staged_by=scientist-b`, and the manifest fingerprints both artefacts.

**Skills considered and declined, with reasons.** `find-fulltext` run inline and exhausted (two
papers, both without a lawful surface). `legend-deepdive`, `legend-study-intake-triage`,
`legend-hypothesis-forge` declined with reasons recorded in the manifest. `legend-locator-audit`
**declined and declared OWED** — the only decline that costs something. `legend-discovery-method`
declined: it is optional and nothing here needed a primitive beyond reading the records; had I
invoked one it would have been `adversarial re-retrieval`, which is in substance what the probe
bounding in § 2(c) did. `legend-commit` not applicable — no actor of this class runs `BATCH_COMMIT`.

**Capability delta that transfers off this gene.** Two, and both are stated as the capability scout's
input rather than as achievements: the pattern *«a title-and-abstract probe returns zero, the
instrument is in a case-series body»* is gene-independent and belongs wherever this repository writes
an instrument or modality negative; and the schema's `no_recipe` escape is the right answer for every
pre-existing artefact whose route was never recorded, of which `session_self_eval` counts **96**.

## Part 3 — the attribution census

```
ATTRIBUTION_CENSUS
incidents: 5
machine: 3   blind_auditor: 0   peer: 0   self: 2
severity_high: 2   of which self: 2
undetected_known: 0
```

**Counting note.** The nine manifest-validator rejections are **one** incident (one class: a schema I
had not read closely enough), caught by `machine`. The locator byte-verification failure and the
`analysis_at`/`event_at` inversion are the other two machine catches. The two `severity_high`
incidents are the ones that would have **reached the record**: the unbounded instrument negative
(*«never used in WOREE»*, false) and the three-independent-observations count — **both caught by
`self`**, by reading a primary rather than trusting a query, and by making a second pass specifically
for a provenance sentence. `blind_auditor: 0` is the honest weakness of this session and the reason
the audit is declared owed: **2 of 2 high-severity catches being self is a good ratio only until an
auditor tests it**, and no auditor has.
