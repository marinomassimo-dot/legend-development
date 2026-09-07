---
record: SCIENTIST OPERATING PRACTICE DISCOVERY
id: SCIENTIST_OPERATING_PRACTICE_DISCOVERY_SCIB_v1
actor: scientist-b (NOT ACTIVATED — operator-directed analytical session; no TASK_ACK, no lease,
  roles/scientist.md deliberately not activated)
date: 2026-08-25
worktree: .claude/worktrees/lettore-b
branch: lettore-b
head: fb31c2a172c2c5dcb5f54ad5cd28ef12d78b6da9
status: NON-CANONICAL LEARNING ARTIFACT — analytical only. Modifies no register, no claim,
  no hypothesis, no governance file, no role contract, no validator, no routing.
independence: reconstructed without reading Scientist A's or Scientist C's output for this task.
---

# Scientist Operating Practice — independent reconstruction from repository evidence (B)

> **What this is.** An archaeology of how a LEGEND Scientist has actually learned to read a
> primary publication, reconstructed from artifacts the work left behind rather than from the
> documents that describe intended behaviour. Normative files were read late and deliberately —
> after the population measurements below were already taken — so that they could not decide
> what I expected to find.
>
> **What this is not.** Not a contract, not a workflow design, not a comparison with any peer
> reconstruction. Part 5 names subject areas only.

---

## 0 · Worktree, ref and population actually measured

Everything below is measured on one tree, named here so a reader can reproduce or refute it.

| Fact | Value | How established |
|---|---|---|
| Worktree | `<REPO_ROOT>/.claude/worktrees/lettore-b` | `pwd` |
| Branch / HEAD | `lettore-b` / `fb31c2a` | `git rev-parse` |
| Working tree | CLEAN — 0 modified, 0 untracked (`-uall`) | `git status --porcelain -uall` |
| Tracked files at HEAD | **583** | `git ls-tree -r --name-only HEAD \| wc -l` |
| Staleness vs authoritative remote | **0 behind** `development/main` (`788c357`) | HEAD is a *descendant* of every remote-tracking ref present: `origin/main`, `origin/HEAD`, `origin/harden-release-scan-scoping`, `development/main`, `development/HEAD`, `local/main` |
| Own commits ahead | **3** (`c6061b8`, `cbcd364`, `fb31c2a` — this actor's prior evidence-review assignment) | `git log main..HEAD` |

**No fast-forward was needed and none was performed.** The previous session on this branch
derived findings from a tree 203 commits behind; that failure is recorded in
[`learning/scientist-b/SLR-scientist-b-0001.md`](../../learning/scientist-b/SLR-scientist-b-0001.md).
Here the ancestry check was run *first*, and it is a positive result, not an absence: HEAD
contains every commit on every remote ref in this repository.

**Two divergent lanes exist and were deliberately not merged.**
`legend-operating-convention-v1` (`30cb4f3`, the branch checked out in the shared checkout) is
`main` + 3 Orchestrator commits; `mirror` (`2767333`) forked at `908197b` and carries 83 commits
absent from HEAD. Neither is on the authoritative line — `development/main` is, and HEAD contains
it — so measuring against HEAD measures a tree that exists. Findings here do not describe those
two lanes and do not claim to.

**Independence.** Branches `lettore` (scientist-a) and `lettore-c` (scientist-c) both measure
`0` commits ahead of HEAD — they are strict ancestors and carry nothing unique. `reviews/` holds
only `plan/` and `scientist-b/`; `learning/` holds only `orchestrator/`, `plan/` and
`scientist-b/`. **No Scientist A or Scientist C output for this task exists in the measured
tree**, so none was encountered and none was inspected.

### Population used for this analysis

Run in this worktree, at this HEAD:

```
python3 framework/scripts/legend_lint.py .        → VERDICT: PASS (1 INFO: CLAIM 010 wikilink not required)
python3 framework/scripts/growth_anchors.py check → VERDICT: PASS
   structural: claims=39 · papers=70 · corpus=356 · literature=390 | registry_only=15 | unread_premises=4
```

| Evidence surface | Count | Denominator note |
|---|---:|---|
| Deep-dive manifests (`deepdive_manifests/*.json`) | **64** | the machine-validated reading record |
| Verbatim locator entries inside them | **1002** | across 63 manifests; 1 manifest (`PMID 34214506`) has zero |
| `source_artifacts` entries (fingerprinted) | **448** | in the 60 manifests carrying the key |
| Full-text read receipts (`fulltext_read_receipts.jsonl`) | **128** | hash-chained; **82 distinct PMIDs** (89 distinct `study_id` *objects* — the object pairs PMID with DOI and seven PMIDs appear under two DOI spellings, so the PMID count is the paper count and matches `reading_state.md`) |
| Prose dossiers (`fulltext_dossiers/`) | **33** | free-form Markdown, no schema |
| Commit candidates (`CC-`) | **16** | + 1 standing proposal = 17 files |
| Session self-evaluations | **22** | |
| Full-text queue entries (`FT-`) | **72** | |
| Discovery-ledger lead IDs (`DL-`) | **145** | |
| Therapeutic hypothesis IDs (`HYP-`) | **20** | |
| Dismissal-ledger entries (`DIS-`) | **12** | plus the `DEFAULTS THAT BIT US` table (16 rows) |
| Learned-gate rows (`learned_gates_registry.md`) | **79** | |
| Named reasoning-failure gates (`failure_taxonomy.md`) | **12** | |
| Page-adjudication record sets | **3 PMIDs / 5 files** | |
| Observation-freeze record sets | **1 PMID / 2 files** | |

**A denominator caveat I hit myself, and it is on-topic.** Counting corpus records with
`grep -cE '^## CORPUS[ -]'` returns **358**; `growth_anchors.py` returns **356**. The two extra
are prose section headings (`## CORPUS COVERAGE …`) — and this is the exact defect already
documented in the header of `framework/scripts/unread_gold.py`, which once reported 358 for the
same reason. I reproduced a known bug by writing my own predicate instead of using the canonical
one. Where a tool defines the population, its number is used above.

---

## PART 1 — Reconstructed Scientist workflow

Derived from what the artifacts show was *done*, in the order the records were produced. Nothing
in the evidence supports the idea that a reading begins by opening the PDF: in the 64 manifests,
five obligatory sections all concern work that precedes interpretation, and three of them precede
the paper being opened at all.

### Phase 0 — Before the paper is selected

**0.1 · Establish which tree you are measuring.** `reading_state.md` opens by refusing to be read
as global truth: *"This page is true of ONE checkout — the one that generated it… If a paper
looks unread, check whether the reading is merged before concluding it does not exist."*
`caption_census.py` records that a census was wrong "because a shell had inherited a worktree's
cwd", and that `files/` being gitignored means a relative path measures whichever tree you happen
to be standing in. Worktree identity is a *reading* precondition here, not an infrastructure
detail.

**0.2 · Check the reading debt you already owe before opening anything new.** `unread_gold.py`
exists to surface "CORPUS items with Tier A **and** Relevance HIGH/VERY HIGH never deep-dived",
and states the rule plainly: *"These must be read BEFORE opening any new batch of studies."* Its
origin is failure FM-011 (2026-07-09), where LEGEND reconstructed in silico a functional result
that was already sitting unread in its own corpus. `growth_anchors.py check` reports
`unread_premises=4` as a ratchet — a debt counter that must not increase.

### Phase 1 — Selection and duplication control

**1.1 · Resolve identity before anything else.** Every queue entry must open with a resolvable
identifier; LINT enforces it (`QUEUE_ENTRY_WITHOUT_IDENTIFIER`,
`QUEUE_ENTRY_IDENTIFIER_NOT_LEADING`). The queue header records why: on 2026-08-10, **21 of 45
entries named their paper only by a dead internal number, an inbox id or an author-year**, and
`FT-004` and `FT-029` had been the same paper for months — *"duplicato che nessun dedup poteva
vedere."*

**1.2 · Check the receipt ledger, not memory.** Rule 7 of `gold_is_in_the_details.md`: *"Check
prior receipts first; a repeated complete read needs an explicit `reread_reason`."* This is
practiced at scale — of 128 receipts, **46 name a `prior_receipt`** and the reason vocabulary is
populated rather than nominal: `first_read` 82, `inadequate_prior_coverage` 20,
`receipt_correction` 14, `explicit_operator_request` 5, `new_version_or_supplement` 3,
`adversarial_reanalysis` 2, `receipt_invalidation` 1, `new_question_outside_prior_coverage` 1.

**1.3 · A re-read for a different purpose is a first-class event, not a duplicate.** 23 of 89
studies carry more than one receipt; four studies carry four. `reading_state.md` states the
non-obvious half: *"Two actors can read one paper in parallel and both be right; the later
receipt is not a correction of the earlier one"* — so the state of a paper is the **union** of
its receipts, computed and *asserted by no receipt*.

**1.4 · Cross-query the shared corpus for artifacts another actor already fetched.**
`corpus_crossquery` is required in all 64 manifests and returns >0 hits in **51**. Its sharpest
instance is a self-indictment (`PMID 42422765`): *"mmc1.pdf and mmc2.pdf were in
files/fulltext/… at 12:13, fetched by another actor. I declared the supplementary unavailable at
13:26 after five failed routes of my own… Two retractions rested on that false premise and both
have been reopened."*

### Phase 2 — Importance, and what importance is *not*

**2.1 · Recency is not the ranking.** Of the 60 deeply-read papers whose year is recoverable from
their fingerprinted artifact filenames: **2000–2009 → 10 (16.7 %), 2010–2019 → 29 (48.3 %),
2020–2026 → 21 (35.0 %)**. Two-thirds of the deep-read corpus predates 2020. The oldest read to
schema-v2 depth is a 2004 PNAS paper (`PMID 15070730`), read on 2026-08-14 with a declared
40-panel budget.

**2.2 · Oncology and pre-pediatric WWOX biology are treated as first-class, and the hierarchy is
explicitly inverted.** `gold_is_in_the_details.md` is declared *"a superordinate principle: it
overrides every gate, score, tier, and matrix"* and states that oncology studies are *"often
decades ahead on the molecular biology"* while syndrome-specific case reports are *"largely
descriptive… Consistency ≠ usefulness."* The worked example is the 2026-07-12 thyroid-cancer
paper, filed Tier C and shelved, that carried the degradation biology of a WWOX SDR missense
allele (P252A: normal mRNA, accelerated turnover, no MG-132 rescue, lysosomal rescue, HSC70
co-IP, LAMP1 colocalization). The same entry records the correction that followed: transferring
that route to Q230P was itself over-transfer and was reversed on audit.

**2.3 · Three axes are kept apart in practice.** Disease proximity is recorded separately from
mechanistic weight: `is_primary_group_for_disease` is **False in 43 of 60** manifests carrying
the flag, while `research_type` is `experimental_lab` in **42 of 60**. The corpus is dominated by
mechanistically strong, disease-distant work — deliberately.

**2.4 · No tier authorizes not reading.** Binding rules 1 and 2: *"`background`,
`discard_low_signal`, `out_of_scope_likely`, `Tier C` mean only 'later in the queue' — never
'never'"* and *"If a ranking ends up discarding a study, the ranking is broken — fix the ranking,
don't lose the study."* Gate `READING_DEBT_FALSE_NEGATIVE` names the same failure.

### Phase 3 — Group, laboratory and field context

**3.1 · Measured, not impressionistic.** `group_assessment` is required in all 64 manifests and
carries numeric counts in **60**, each with the query that produced them — e.g. *"PubMed esearch
2026-08-10: 'Aqeilan RI[au]' 137, 'Aqeilan RI[au] AND WWOX' 65."* `research_type` is a closed
vocabulary of six read *off the Methods rather than the journal*, because "a descriptive series
and a wet-lab mechanism are not interchangeable support for the same claim."

**3.2 · Context adjusts weight; it never substitutes for evidence.** The clearest instance
(`PMID 42082822`, a review) measures self-citation: *"34 % of the citation base shares an author
with the review and 20 % names a Chang, against four references to Aqeilan and one to Croce… A
synthesis assembled almost entirely from one group's own output is a strong description of that
group's model and a weak description of the field."* The operational consequence is stated as a
rule, not a mood: *"TREAT ITS PRIMARY-SOURCE POINTERS AS THE PRODUCT AND ITS SYNTHESIS AS A
HYPOTHESIS."* The same manifest still records three places where the review's prose diverges from
its own panels.

**3.3 · Declared funding reweights interpretation.** `PMID 42422765`'s `weighting` field notes the
study is supported by a therapeutics company and treats that as a declared change in
interpretive weight, sourced to the Methods and the declaration of interests.

**3.4 · `retraction_check` is a required, dated, routed step.** Present in 64/64, performed in 35
with route and result recorded (`SOURCE_INTEGRITY` gate).

### Phase 4 — Surface preflight and acquisition

**4.1 · Choose the surface before opening the paper.** Rule 5d: *"prefer XML/HTML PMC over the
PDF, always, and record the absence."* The reason is measured, not stylistic: *"`PMID 33914858`
extracts as `P 5 0.05` where the page prints `P < 0.05`, and three independent extractors agree
on the wrong character… **cross-checking extractors detects nothing.** 33 of 51 local PDFs carry
the defect… `Wwox\x01/\x01` is `Wwox⁻/⁻` while `Wwox\x02/\x01` is `Wwox⁺/⁻`… Roughly 80 % of the
damage is printable, so no control-character check can see it."*

**4.2 · The corpus-wide surface state is a standing, generated page.** `surface_census.md`
(census 2026-08-15, listing digest `825fc4a9d8415b0e`): **116 papers → structured 67, pdf_only
20, absent 29**; sentinel over the 87 papers with a local surface → **SUSPECT 15, clean 72,
not_screened 0**. Two files with `.html` suffixes are reclassified as PDF-only because their body
sits inside a `<pre>` block: *"a suffix is not a surface."* And the honest limit is printed on the
page: *"A photograph, not an invariant… `clean` — no known signature found — **this is not a
verification**."*

**4.3 · A suspect surface is refused, never normalised.** *"cleaning it launders the defect into
every quote drawn from it… never hand-correct a corrupted surface — re-derive it, or anchor the
affected locators to the rendered page and say so."*

**4.4 · One route failing is a fact about the route, not about the paper.** The practice is
visible in the manifests as an explicit route ledger. `PMID 42128308`: *"Route that worked: the
Europe PMC REST endpoint `/{PMCID}/supplementaryFiles`, which returns a ZIP containing ALL ELEVEN
figure JPEGs plus three supplementary Data Sheets — 13.4 MB, HTTP 200. Two routes that did NOT
work and are recorded so nobody re-pays for them: `ncbi.nlm.nih.gov/pmc/articles/{PMCID}/bin/…`
returns 404 (the path moved), and `europepmc.org/articles/{PMCID}/bin/…` 301s to HTML."* The same
entry names the specification gap it exposed: the preflight asked for PMCID, structured surface,
licence and class **but not for a figure surface**, so four "structured" papers were readable and
blind to their panels.

**4.5 · A retrieval failure is characterised, and its artifacts destroyed.** `PMID 15070730`:
PMC's proof-of-work interstitial returned HTTP 200 with 1.8 kB of HTML per requested JPEG;
*"The three files were deleted rather than kept; an interstitial saved under a .jpg name is a
future false artifact."* Elsewhere, seven byte-identical "figures" were caught by comparing
digests — an HTML error page saved eleven times.

**4.6 · Abstract-only is honest and clears nothing.** Rule 8: *"A local abstract corpus is a map,
never the territory… an `abstract_only` event is honest but clears no reading debt. **Un abstract
non è una lettura.**"* Enforced at the append primitive and mutation-tested. In the ledger,
`abstract_only` appears in **2 of 128** receipts.

### Phase 5 — Declare the reading budget before reading

**5.1 · The denominator is measured from the paper, not chosen after the fact.**
`reading_budget.declared_before_reading: true`, with `figures_present`, `panels_present`,
`panels_inspected`, `panel_coverage` and a `method` string that says how the count was obtained.
`PMID 15070730`: *"MEASURED, NOT INTENDED. Counted by reading the captions, not by counting
`<fig>` — the HTML deposit carries ZERO `<fig>` elements, so that count is meaningless here and
was not used."* `PMID 32581702`: *"fixed BEFORE reading so the budget could not be chosen to
match what was found."*

**5.2 · The denominator is where the tooling lies most often, and the practice is to distrust
it.** Four silent miscounts in one session, four different scripts, all recorded:
`PMID 32581702` — 22 panels produced by a silent `or 1` fallback on an unlettered figure;
`PMID 34268881` — counter reported 17 where there are **69**; `PMID 24550385` — reported 7, count
"still not reliably obtainable"; `PMID 18487609` — automatic census returned **27 against an
actual 32**, because a caption wrote "higher magnifications in D" without the punctuation the
panel regex required. That last entry names the class: *"a small plausible integer where an error
belonged"*, and the shape it shares with *"the four silent-zero failures the counter was built to
end."*

**5.3 · Coverage that cannot be achieved is declared as a gap with its consequence, not padded.**
`PMID 15070730`: `panels_present_supplementary` = *"UNKNOWN AND DECLARED AS UNKNOWN RATHER THAN
PADDED — panels cannot be counted in figures that could not be opened."* And the gap is argued as
load-bearing: *"This is the finding, not the apology. All three are cited in the running text as
the support for a specific step… Fig 5 carries the DOSE-DEPENDENCE of p73 relocalisation — the
strongest form of the routing evidence."*

**5.4 · The denominator's own reference class is checked.** `PMID 32581702` records a correction
to the orchestrator's coverage rule: *"The rule as first issued was `figures per paper` compared
across readers; that ratio has the reader's denominator, not the paper's."*

### Phase 6 — Neutral first pass, then interpretation

**6.1 · The strongest instance is a hashed observation freeze.** `PMID 34831305`: twelve numbered
observations recorded, reading order declared (*"XML body sequentially, Table 1, disclosures, 224
references, Figure 1 pixels, Figure 2 pixels"*), *"Pattern prompt deliberately withheld until
after this record"*, frozen at `2026-08-10T07:43:00Z`, SHA-256
`ee6e4988…`, and the named pattern adjudicated 19 minutes later against the frozen text.

**6.2 · The verdict was negative, which is why it counts.** *"No valid third occurrence… In a
narrative review this is visual compression, not an undrawn primary experimental comparison."*
A freeze whose only recorded use *refuses* to confirm the hypothesis it was testing is
behavioural evidence that the mechanism works, not decoration.

**6.3 · And its limit is stated.** *"Prior conversational knowledge could not be erased and
remains a residual contamination risk."*

**6.4 · This is a population of one.** `observation freeze` appears in exactly **2 files for 1
PMID** out of 64 manifests. It is the most rigorous anti-confirmation-bias artifact in the
repository and it has been executed once.

### Phase 7 — Experiment-by-experiment interrogation

**7.1 · Reading is sequential and vertical, not keyword-driven.** Rule 4 is a prohibition:
*"`grep` / keyword is forbidden as a method of analysis — only for technical file search, dedup,
or post-reading audit. Never to decide what a paper says."* Reading order is recorded
(*"XML read in document order across every section; nine PDF pages reconciled"*).

**7.2 · The unit of interrogation is the experiment, and its direction.** Session evaluation
`2026-08-14_Salah2013`: *"Results/Figure 3: WWOX competes with ITCH for ΔNp63α, reduces ΔNp63α
ubiquitination/degradation and lengthens ΔNp63α half-life. Figures 4–5: increased abundance
coexists with cytoplasmic retention and reduced transcriptional function."* The micro-upgrade
shipped from that read requires **enzyme/process, substrate, sign/effect and edge-modulator** for
any ubiquitination/degradation/stabilization statement.

**7.3 · The hidden gold is looked for explicitly and named as a dimension.** The self-evaluation
template scores *"Hidden gold beyond keywords/abstract"* per read. On Salah 2013: *"Figures 4–5
expose abundance/function decoupling; Figure 6d exposes doxycycline-induced death and cisplatin
potentiation in controls. Neither is captured by a gene-keyword extraction of the headline
mechanism."*

**7.4 · Hidden assumptions are surfaced as method notes.** `PMID 18487609`: *"Table 1 (qRT-PCR
primer sequences)… is the source of the note that the Wwox primer pair spans the region deleted
in this knockout, which is why Fig 5A and 6C show a Wwox bar at zero rather than a missing bar."*
An artifact of primer design, recovered from a methods table, that would otherwise read as data.

**7.5 · Multi-hop starts at the reference list and is bounded honestly.** `multihop` is required
in 64/64 and resolves ≥1 reference in **47**. `PMID 42422765` enumerated 73 reference PMIDs,
deduplicated all 73 against three registries (*"38 known, 35 unknown"*), and then declared:
*"Enumerated and queued, not pursued."* — with the reason that gene-directedness classification
*"is triage work and is deliberately deferred."* The `references` coverage key exists because on
2026-07-26 a `complete_fulltext_read` was declared without enumerating the reference list, losing
the neuron-specific GSK3B isoform (PMID 20067585) *"that qualified its own inferences."*

### Phase 8 — Figures as a separate primary surface

**8.1 · Figures are pixels, and they are the second-largest evidence surface in the corpus.**
Of 448 fingerprinted `source_artifacts`, **333 are `kind: figure`** — more than article text
(58), article binaries (44), tables (9) and supplement text (4) combined. Of 1002 locators,
**338 (33.7 %) declare `surface: figure`.**

**8.2 · Panel-level, at native resolution, with crops where adjudication is needed.**
`PMID 15070730`: *"Every one inspected as an image at native resolution, with 6x-7x LANCZOS crops
on Fig 1G, 4A, 4B and 4E where band-level adjudication was needed."* `figure_ppi_preflight.py`
inventories the raster ceiling before rendering; `PMID 18487609` records *"All eight sit at 150
effective ppi"*, and `PMID 34831305` records that the CDN returned 757×434 JPEGs against
XML-declared 4542×2601 originals — and says so rather than claiming the originals were read.

**8.3 · Text-versus-panel disagreement is a typed, machine-checked field.** `panel_text_relation`
carries six values, and the two that assert disagreement (`text_contradicted_by_panel`,
`panel_qualifies_text`) are **coupled**: each must name the text locator it bears on
(`contradicts` / `qualifies`) and quote a fragment of it (`contradicts_needle` /
`qualifies_needle`), *"Without the pointer the claim is unfalsifiable prose sitting in a JSON
field."*

**8.4 · The measured disagreement rate.** Across all 1002 locators:

| `panel_text_relation` | n | % of 1002 |
|---|---:|---:|
| `text_only` | 417 | 41.6 % |
| *(absent — pre-dates the field)* | 230 | 23.0 % |
| `panel_only` | 148 | 14.8 % |
| `text_confirmed_by_panel` | 128 | 12.8 % |
| **`text_contradicted_by_panel`** | **47** | **4.7 %** |
| **`panel_qualifies_text`** | **32** | **3.2 %** |

**79 locators — 7.9 % of the corpus — record a panel that contradicts or qualifies the running
text.** That is the empirical answer to "why inspect figures": in roughly one locator in
thirteen, the panel and the prose do not say the same thing.

**8.5 · Adjudication favours the image, and the rule is stated at its strongest.** `DEFAULTS THAT
BIT US` D-14, on Wang 2012 (`PMID 22193544`): both the published supplementary legend **and** the
main text describe a co-IP proving *"WWOX does not associate with Tau"*, stating *"anti-Tau was
used to detect endogenous Tau"* — *"The image contains **no Tau blot at all**: its two panels are
labelled **WWOX** and **GSK3β**, and the lower one shows a faint *positive* band in the HA-IP
lane. **A caption is authored prose; a blot is data.**"* The recorded rule: *"a negative asserted
by a figure must be verified in the figure IMAGE, never on caption authority — and this is
strictly stronger than reading the text, because here text and caption agreed with each other and
both were wrong."* Cost avoided: a false conflict registered against a live mechanism.

**8.6 · Figures have corrected conclusions repeatedly, with dates.** `deepdive_manifest.py`
records three in its own source: *"on 2026-08-04 a figure panel reversed a conclusion the running
text did not contain, on 2026-08-06 an unmarked asterisk was the difference between 'not
significant' and 'not tested', and on 2026-08-10 Figure 3B of PMID 42422765 turned a
'dose-dependent' continuum into a threshold."*

**8.7 · The vocabulary itself was corrected by evidence.** `panel_qualifies_text` was added on
2026-08-10 *"on SIX independent instances across five papers, found by three actors who had not
spoken"* — including two pairs on `PMID 38182577` that **B downgraded from contradiction** after
checking the panel was not the one the sentence cites. The recorded reasoning is the strongest
methodological sentence in the repository: *"When no admitted value is true, the defect is the
enum. Forcing one would write a known falsehood into canonical state… 'Incomplete is not false'
is the shortest statement of the relation."*

**8.8 · Captions are a surface an extractor can silently hide.** `caption_census.py`, measured
2026-08-10: **7 of 34 parseable XML surfaces place every `<fig>` outside `<body>`**, 2 more place
some there. *"An agent reading through a body-scoped extractor sees no caption at all… and the
manifest still passes, because a validator checks what you QUOTED, not what you were able to
SEE."* One of the seven, `PMID 24308844`, carries seven figure entries and not one caption
locator — *"an absence that looked like a budget choice and was a surface nobody had seen."*

### Phase 9 — Tables and supplementary material

**9.1 · This is the weakest surface in the entire practice, and it is measured.** Of 1002
locators, exactly **1 (0.1 %) declares `surface: supplement`**; 13 (1.3 %) declare `table`.
Across 128 receipts, `supplementary` is `read` in **23**, `not_read` in 27, `unavailable` in 20,
`not_present` in 35, `unknown_legacy` in 23 — i.e. of the 93 receipts where a supplement exists
or might, **23 read it**.

**9.2 · Failure to recover it is recorded as a limitation with its blast radius named.**
`PMID 18487609` `coverage_gaps.supplementary`: *"UNAVAILABLE, AND ONE LOAD-BEARING NUMBER DEPENDS
ON IT… that path is behind the service operator's proof-of-work anti-automation challenge
(cloudpmc-viewer-pow), which this session does not defeat. Consequence: entry 21's '50 % lower
calcium and 20 % increased phosphate' — the number on which the whole metabolic-bone-disease
reading rests — is recorded as an unverified citation to a table that was not seen."*

**9.3 · And the most valuable single finding in the corpus came from a supplement.** The
`captions_only` coverage state exists because *"On 2026-07-26 the single most valuable finding of
a deep dive — a supplementary figure whose panels contradict its own caption — was invisible at
caption level and visible only in the raster image."*

### Phase 10 — Locators and verbatim capture

**10.1 · Captured while the document is open, never reconstructed.** Rule 5b, and the failure that
produced it: *"On 2026-08-04 an export found that no verbatim locator existed anywhere in the
canonical state, across every complete read in the ledger; fourteen had to be recovered by
reopening papers already read. Capturing costs seconds, recovering costs the reading twice."*

**10.2 · A locator declares five independent facts.** Proposition; verbatim snippet (≥30
characters — *"A quote shorter than this is not a locator, it is a gesture at one"*); `surface`
(`body|figure|table|supplement|abstract`); the fingerprinted `source_artifact` it came from; and
`panel_text_relation`. `surface` and artifact are separate on purpose: *"an agent could read the
abstract, write a plausible dossier, declare the XML, and pass."*

**10.3 · Receipt ≠ anchoring, and the repository says so in three places.** Rule 5b: *"A receipt
attests that a document was read; it does not attest which sentence supports which statement."*
`locator_audit.py` exists to close half of that gap, and reports the debt it found: audited
2026-08-10, **`PMID 32000863` had 5 locators out of 22 that did not occur in its own XML** — all
*"transcribed as the page reads rather than extracted as the artifact contains… None changed
meaning; two lost information — which figure a result points at, and which references support
which clause."*

**10.4 · And the mechanical half is explicitly not the judgement half.** `locator_audit.py`:
*"It is the mechanical half of `legend-locator-audit` and never a substitute for it. This asks
only whether the sentence EXISTS in the source. Whether the sentence SUPPORTS the proposition
written above it — overshoot, undershoot — is a judgement… and no amount of string matching
approaches it."* The blind auditor receives only `(proposition, quote, anchor)` triples, never
the dossier and never the reader's name.

**10.5 · Prose dossiers are the unguarded remainder.** `dossier_quote_audit.py`: *"a dossier is
prose, so a quotation in one carries no artifact, no surface and no fingerprint… Until [promoted]
it is load-bearing and unexamined."* Deliberately non-blocking, because typographic quotes are
used both to quote and to coin.

**10.6 · Where the text layer cannot be trusted, the rendered page is adjudicated — as a
recipe.** Rule 5e: state records source-PDF digest, page, crop rectangle in PDF points, dpi and
image SHA-256; `regenerate_adjudications.py` reproduces identical bytes from a reader's own copy.
*"Publish the derivation, not the derived."* Two conditions are machine-checked, including
`crop_contains_span` — because *"an adjudication artifact must contain the entire span it
adjudicates"* or a locator would be "verified" against pixels that do not exist. Standing policy,
because *"33 of 51 local PDFs will eventually need adjudicating."* Executed so far on **3 PMIDs**.

### Phase 11 — Observation / author interpretation / LEGEND interpretation

**11.1 · The separation exists and is typed.** Claim `Type` is a composite of DATO / INFERENZA /
IPOTESI / ESPANSIONE, and the composites are the norm: of 39 claims, 16 are bare `DATO` and the
rest are annotated compounds naming which half is which — e.g. *"DATO (le misure) + IPOTESI
(entrambe le spiegazioni)"*, *"DATO (statistica di coorte) + IPOTESI (l'assunzione 'missense =
ipomorfo')"*, *"DATO (osservazione clinica) + INFERENZA (degli autori)"*. That last one types the
**authors'** inference as a distinct object from the datum.

**11.2 · The most explicit machine-readable instance is `three_arcs_kept_separate`
(`PMID 16061658`)** — one manifest key holding three separated provenances: arc 1, this article's
DATO (*"The authors state it as 'may compete'; this manifest states it as they did"*); arc 2, a
different source's DATO, *"NOT retro-attributable here"*; arc 3, the combination, typed
`INFERENZA` and *"supported by neither on its own."* Plus a negative clause naming what the
adjudication does **not** license. Its stated rationale: *"a single sentence in a later paper
compresses two provenances, and compression is how a hedged result becomes a fact."*

**11.3 · LEGEND narrows author interpretation, and records the narrowing.** `PMID 20530675`
receipt: *"THE PAPER PRINTS ITS OWN REFUTATION OF ONE OF ITS FIGURE TITLES… Figure 5 is titled
'Inverse association of WWOX and RUNX2 expression in osteosarcoma'… The Results, two paragraphs
later: 'this was not evident when paired comparisons were performed on the 56 available cases'.
The numbers that follow run the OTHER WAY."* The same entry classifies the failure mode against
two prior ones: *"On PMID 27308504 and PMID 31075076 what travelled beyond the evidence was
MODALITY — hedges present in the text and absent from the figure. Here the modality is INTACT."*

**11.4 · LEGEND records when its own mechanism failed to predict.** `CLAIM 001`: *"il razionale
meccanicistico 'GABA depolarizzante nei neuroni immaturi → i farmaci GABAergici rendono poco'…
**non predice questi esiti clinici**: il vigabatrin ha risolto gli spasmi in un WWOX-null. Il
meccanismo resta valido come meccanismo; **non è un predittore di risposta clinica.**"* The status
`conflicting evidence` is kept and re-justified rather than resolved.

### Phase 12 — Negatives, tension and contradiction

**12.1 · Negatives are claims, and the asymmetry is the stated reason.** *"A false positive gets
tested and dies. A false negative is silent, permanent, and self-reinforcing… a false positive is
a cost; a false negative is a compounding loss. And tiers, gates, filters, `refuted`, 'do not
assume that…' are all machinery that produces negatives."*

**12.2 · Three binding obligations, one of them LINT-enforced.** `PREMISE_TAG`
(`DATO` / `INFERENZA` / `DEFAULT_FROM_TEXTBOOK`); `REVIVAL_TRIGGER` on every rejection; and the
re-audit rule — *"Every time a new mechanistic DATO arrives, re-scan the dismissal ledger…
Without this step you have self-correction, not self-improvement."* `legend_lint.py` fires
`DISMISSAL_WITHOUT_PREMISE` and `DEFAULT_PREMISE_NO_TRIGGER`, both at `WARN_BUT_PROCEED`,
matched bilingually (`PREMESSA|PREMISE`).

**12.2b · The re-audit rule has demonstrably fired, and the dismissal ledger is where it is
visible.** Of the **12** `DIS-` entries, exactly **one** is recorded as *"a rejection that
holds"*. The other eleven: 2 `REOPENED`, 1 `FALSE, REVERSED`, 2 `WITHDRAWN`, 1 `DOES NOT HOLD`,
2 `NON STABILITA`, 3 `RIGETTATA` — every one of them re-adjudicated after the fact, none deleted.
`DIS-006` names the mechanism in its own heading: *"REOPENED — **by the re-audit rule**"*, and
records that *"`REVIVAL_TRIGGER` already fired"*. Its lesson is the sharpest statement of the
practice in the repository: *"'not resolvable in silico' is not a property of the world: it is a
property of the question you are asking… This rejection was correct for the old question, and
wrong for the new one."*

**12.2c · The parity-of-sources principle is itself a reversed negative.** `DIS-002`, *«Oncology
papers are background for this disease»* → **FALSE, REVERSED**. Load-bearing premise tagged
`PREMISE: DEFAULT_FROM_TEXTBOOK` — *"that relevance follows the disease phenotype."* Verdict:
*"WWOX was born a tumor suppressor: folding, stability, degradation routes, partners were
characterized by cancer research. Of the papers that produced key commit candidates in this
domain, **none was on WOREE** (thyroid, prostate, leukemia)."* Outcome: the parity-of-sources
principle and the `DOMAIN_PARITY` rule. The superordinate reading principle of §2.2 did not arrive
as a design decision — **it is a false negative that was caught and inverted.**

**12.3 · `DEFAULTS THAT BIT US` is a live, consulted table.** 16 rows spanning domain biology
(D-01 K48 vs K63; D-02 ERAD vs CMA compartment; D-03 *"HSC70 does not rescue: it delivers to the
lysosome"* — an HSP70 co-inducer could **accelerate** destruction; D-04 *"stability is bought with
occlusion, and occlusion is anti-function"*), reading (D-14, D-15), and engineering meta-defaults
(D-05 through D-13). Instruction: *"Consult it BEFORE discarding anything."*

**12.4 · Counter-evidence is a required field in the discovery ledger.** Every `DL-` lead carries
`Evidenza: supporta= / refuta= / neutrale=`, a `Belief` level, and an `Esperimento proposto` that
would falsify it. `DL-BIO-010` is the model instance: from Figure 8 read as an image, *"l'onda-a
— la componente generata dai fotorecettori — è invariata. Solo l'onda-b, post-fotorecettoriale, si
muove. La tesi del lavoro è una patologia guidata dai fotorecettori; la sua elettrofisiologia
colloca il deficit a valle."* Belief: *"medio sull'osservazione; nullo su qualunque validità in un
contesto WWOX, mai testata."* Process reflection: *"adottarlo senza leggere la Figura 8 avrebbe
importato l'errore."*

**12.5 · Secondary-source attribution is treated as unreliable by default.** D-15: a review cited
`[75, 76]` for a compound statement; the different-sites clause was attributed to ref 76 (Saeki
2011), which *"measures one site only, Ser396, and never addresses site selectivity."* Rule:
*"when a secondary source cites `[a, b]` for a compound statement, you do not know which clause
belongs to which reference — resolve the primary before propagating any clause of it."* Recorded
as *"caught… but one cycle late: the misattribution had already been written to a ledger."*

### Phase 13 — Mechanistic reasoning and causal licence

**13.1 · The existing vocabulary is DATO / INFERENZA / IPOTESI / ESPANSIONE**, plus claim status
(`consolidated baseline` 18, `in observation` 17, `flagged for review` 2, `conflicting evidence`
1, `background only` 1 — of 39) and transferability tiers `T1`–`T4`, which in practice are
qualified in prose rather than left bare (*"T1 nominale, **T3 di fatto** (vedi riserva 3)"*;
*"T3 — non trasferisce un fenotipo, trasferisce un avvertimento metodologico"*).

**13.2 · Co-occurrence is explicitly not causation, and the gates say how.**
`DEGRADATION_DIRECTION_GATE`: *"Name the direction; do not infer causality from co-occurrence."*
`MECHANISM_DIRECTNESS_GATE`: *"A surrogate is not the mechanism; the intermediate must be
measured."* `TARGET_ATTRIBUTION_GATE`: *"A pharmacological rescue does not identify the target
automatically."* `KG_EDGE_HAS_NO_SIGN`: *"A KG edge is a relevance hypothesis, never a direction;
read the sign in a loss-of-function model, not a tumor line under chemotherapy."*

**13.3 · A causal edge transferred across systems degrades to a hypothesis, by rule.**
`MECHANISM_TRANSFER_FIREWALL`: *"Attach `variant/model`, `experimental system` and `epistemic
level` to every edge. A transferred edge remains a bridge hypothesis until measured in the target
system."* `MECHANISTIC_OVERTRANSFER`: *"a route measured on variant X is a hypothesis for variant
Y, not a datum."*

**13.4 · The discovery ledger already writes typed causal statements** — `Q230P
—predicted_destabilizes→ WWOX_SDR_fold`, `SDR_destabilization —decreases→
WWOX_oxidoreductase_activity` — each with a `Belief` and each separated into an `A → B → C` map.
Recorded here as observed practice only; no proposal is made about it.

### Phase 14 — Brainstorming, separated by construction

**14.1 · Creativity is not suppressed; it is relocated.** Three non-canonical ledgers exist
downstream of reading — `discovery_ledger_current.md` (145 leads),
`therapeutic_hypotheses_ledger_current.md` (20 `HYP-`), `dismissal_ledger_current.md` — each
headed *"READ-ONLY verso i 4 current"* and *"Nulla entra nei current se non via INGEST →
DEEP_DIVE → COMMIT CANDIDATE → BATCH_COMMIT."*

**14.2 · The safeguards are four, and they are stacked.** *(i)* file separation — hypotheses
physically cannot be in a canonical register; *(ii)* epistemic typing — *"qui vivono IPOTESI ed
ESPANSIONE, mai DATI"*; *(iii)* a required falsification experiment and a scored ranking
(actionability / evidence / safety / time-to-benefit / partial-value); *(iv)* a BLOCK-1 safety
verdict on every entry.

**14.3 · Append-only on leads, status never deletion.** *"leads are never deleted, only
re-statused"* — `open · maturing · promoted-to-CC · parked · refuted`. The reason is the false-
negative asymmetry again: a deleted lead is an unrevivable rejection.

**14.4 · Promotion is a separate, gated artifact.** 16 commit candidates, 14 of which carry the
heading *"Proposed canonical effect at the next lawful BATCH_COMMIT"* — proposals, not edits.

### Phase 15 — Landing, receipt, self-evaluation

**15.1 · The manifest gates the strongest claim.** A `complete_fulltext_read` receipt is refused
unless a valid manifest exists — *"The strongest claim the system can make about a paper becomes
unavailable until the work behind it exists."*

**15.2 · The ledger is append-only and anchored twice.** Every event carries `ledger_prev_hash`;
the tail (count + head digest) is anchored in the state manifest *"because a hash chain alone
cannot detect truncation."* The residual limit is printed: *"an editor who rewrites the ledger
and the manifest anchor in the same breath is not caught by arithmetic… the integrity claim
degrades to 'visible in review', never to 'invisible'."*

**15.3 · A read must land somewhere findable.** `session_self_eval.py` compares declared outputs
against six landing files. Its origin: *"On 2026-07-26 a receipt was persisted, hash-chained and
tail-anchored declaring discovery ledger entries DISC-2026-07-26-A/B/C… None existed, and the ID
scheme was not even the one this repository uses. The receipt was immutable and wrong, inside the
one subsystem whose whole purpose is to be trustworthy."*

**15.4 · A wrong receipt is invalidated forward, never deleted.** One `receipt_invalidation`
exists in 128 events: `FTR-20260806-23446842-02` invalidates `FTR-20260726-23446842-01` because
the legacy reconstruction pointed at a paper record whose own identifier was a **different PMID**
— *"the event is retained in history but removed from active depth indexes."*

**15.5 · Every read is diagnosed against a fixed dimension set,** and the tool refuses to grade
the science: *"It deliberately does not try to score analytical quality: the judgement questions
live in `session_self_evaluation.md` and stay human."* The written diagnosis names failures
explicitly (*"all six XML figures lie outside `<body>`; the automatic sweep ranked the paper P2
despite an existing high-priority load-bearing queue entry; inherited shorthand omitted the
stabilized substrate"*) and must ship a **micro-upgrade**, with persistence evidence.

---

## PART 2 — Implicit operating rules

Twenty-four rules recovered from behaviour. Standing is assigned from what the tree shows, not
from what a document asserts.

| # | Rule | Observed evidence | Why it matters | Standing | Mechanizability |
|---|---|---|---|---|---|
| R-01 | Verify which tree you are measuring before producing any number | `reading_state.md` header; `caption_census.py` (*"a shell had inherited a worktree's cwd"*); `SLR-scientist-b-0001` §1 (203 commits behind) | Every downstream count describes a tree nobody holds | PRACTICED (after failure) | MECHANIZABLE |
| R-02 | Retire existing reading debt before opening new work | `unread_gold.py` (FM-011, 2026-07-09); `growth_anchors` `unread_premises=4` ratchet | The corpus already contained the experimental proof LEGEND re-derived in silico | EXECUTABLY_ENFORCED (ratchet) | MECHANIZABLE |
| R-03 | Every queue entry opens with a resolvable identifier | LINT `QUEUE_ENTRY_WITHOUT_IDENTIFIER`; 21/45 entries were unresolvable on 2026-08-10; `FT-004`≡`FT-029` | Dedup cannot see a duplicate whose identity is a dead internal number | EXECUTABLY_ENFORCED | MECHANIZABLE |
| R-04 | Consult the receipt ledger before reading; a re-read declares its reason | Rule 7; 46/128 receipts name a `prior_receipt`; 8-value `REREAD_REASONS` enum | Distinguishes a duplicate from a purposeful second reading | EXECUTABLY_ENFORCED | MECHANIZABLE |
| R-05 | Parallel readings do not supersede each other; paper state is the union | `reading_state.md` (*"asserted by no receipt"*); 1 parallel pair measured | Reading the latest receipt as state erases the other reader's coverage | PRACTICED + generated view | MECHANIZABLE |
| R-06 | Cross-query the shared corpus before declaring anything unavailable | `corpus_crossquery` required 64/64, >0 hits in 51; `PMID 42422765` (*"Two retractions rested on that false premise"*) | Unavailability is a property of your routes, not of the artifact | EXECUTABLY_ENFORCED (slot) / PRACTICED (quality) | HYBRID |
| R-07 | No tier, score or category authorizes not reading | Binding rules 1–2; `READING_DEBT_FALSE_NEGATIVE` gate; D-05 (a script silently refused to download the lowest class) | A ranking that discards a study is a broken ranking | DOCUMENTED, partially enforced | HYBRID |
| R-08 | Recency is not priority; oncology and pre-2010 biology carry mechanistic weight | 65 % of the 60 dated deep-reads predate 2020; 16.7 % predate 2010; the Tier-C thyroid paper; **`DIS-002` records the opposite belief as a reversed false negative** | The lever for a tumour-suppressor allele is usually in the older, disease-distant literature | PRACTICED + DOCUMENTED | SCIENTIFIC_JUDGMENT |
| R-09 | Disease proximity, mechanistic relevance and foundational weight are three axes | `is_primary_group_for_disease` False in 43/60 while `research_type=experimental_lab` in 42/60 | Collapsing them re-imports the inverted hierarchy | PRACTICED | HYBRID |
| R-10 | Group assessment is measured with its query, not asserted | 60/64 numeric counts, each with the esearch string; 6-value `RESEARCH_TYPES` read off Methods | "Important lab" is unfalsifiable; "137 publications, 65 on the gene, esearch 2026-08-10" is not | EXECUTABLY_ENFORCED | MECHANIZABLE (counts) / SCIENTIFIC_JUDGMENT (weighting) |
| R-11 | Field density and self-citation adjust interpretive weight, never evidential weight | `PMID 42082822` (*"34 % … shares an author"*, *"pointers as the product, synthesis as a hypothesis"*) | A group's synthesis of its own output is not independent replication | PRACTICED (few instances) | SCIENTIFIC_JUDGMENT |
| R-12 | Prefer the structured surface; a suffix is not a surface; a suspect surface is refused, never cleaned | Rule 5c/5d; census 87 papers → 15 SUSPECT; two `.html` files reclassified as PDF-only | Cleaning launders the defect into every quote drawn from it | EXECUTABLY_ENFORCED (`_refuse_suspect_surface`) | MECHANIZABLE |
| R-13 | One route failing is a fact about the route; record which routes were tried and which worked | `PMID 42128308` route ledger; `PMID 15070730` PoW interstitial deleted; seven byte-identical "figures" caught by digest | Prevents re-paying for dead paths and prevents saving an error page as evidence | PRACTICED (heterogeneous) | HYBRID |
| R-14 | Abstract-only is honest and clears no reading debt | Rule 8; 2/128 receipts; enforced at the append primitive and mutation-tested | Hundreds of local greppable abstracts make answering from them *feel* like working | EXECUTABLY_ENFORCED | MECHANIZABLE |
| R-15 | Declare the reading denominator before reading, measured from the paper | `reading_budget.declared_before_reading`; `PMID 32581702` (*"fixed BEFORE reading so the budget could not be chosen to match what was found"*) | Coverage claimed against a post-hoc denominator is unfalsifiable | PRACTICED — **12/64 manifests**; not required | MECHANIZABLE (the slot) / SCIENTIFIC_JUDGMENT (the count) |
| R-16 | Distrust automatic counters; a small plausible integer is the failure mode | 27-vs-32, 17-vs-69, 22-via-`or 1`, 7-unreliable — four scripts, one session | A counter that cannot report "I found nothing" fails silently | PRACTICED (after failure) | HYBRID |
| R-17 | An unreachable surface is declared UNKNOWN with its consequence, never padded | `PMID 15070730` (*"declared as unknown rather than padded"*, *"This is the finding, not the apology"*); `PMID 18487609` (*"ONE LOAD-BEARING NUMBER DEPENDS ON IT"*) | Distinguishes what was inspected from what was intended | PRACTICED (best instances) | HYBRID |
| R-18 | Separate a neutral observation pass from interpretation, and freeze it | `PMID 34831305` freeze, SHA-256 `ee6e4988…`, pattern withheld 19 min; verdict **negative** | The only mechanism here that can prove a pattern was not manufactured | PRACTICED — **1 PMID of 64** | HYBRID |
| R-19 | `grep` is forbidden as a method of analysis | Binding rule 4; reading order recorded per manifest | Keyword reading finds the headline and misses the gold | DOCUMENTED; not enforceable by construction | SCIENTIFIC_JUDGMENT |
| R-20 | Figures are a separate primary surface, inspected as images at native resolution | 333/448 artifacts are figures; 338/1002 locators are `surface: figure`; PPI preflight; LANCZOS crops | Text extraction cannot represent a panel | EXECUTABLY_ENFORCED (surface + artifact) / PRACTICED (resolution) | HYBRID |
| R-21 | Record how the panel stands to the text, per locator, and couple every disagreement to what it disagrees with | `PANEL_TEXT_RELATIONS`, `COUPLED_RELATIONS` pointer + needle; **79/1002 disagreements** | Without the pointer the assertion is unfalsifiable prose | EXECUTABLY_ENFORCED | MECHANIZABLE (structure) / SCIENTIFIC_JUDGMENT (the value) |
| R-22 | A negative asserted by a figure is verified in the image, never on caption authority | D-14, Wang 2012: caption *and* text both describe a blot that does not exist | Strictly stronger than reading the text — here both agreed and both were wrong | DOCUMENTED + `captions_only` state | SCIENTIFIC_JUDGMENT |
| R-23 | Capture the verbatim locator while the document is open | Rule 5b; 2026-08-04: zero locators existed corpus-wide, 14 recovered by reopening papers | Capturing costs seconds; recovering costs the reading twice | EXECUTABLY_ENFORCED (slot + waiver) | MECHANIZABLE |
| R-24 | A receipt proves a document was read; it never proves a sentence supports a statement | Rule 5b; `locator_audit.py` (5/22 quotes absent in `PMID 32000863`); blind `(proposition, quote, anchor)` audit | The two are routinely conflated and only one is checked | EXECUTABLY_ENFORCED (existence) / PROPOSED (support) | HYBRID |

**Standing counts across R-01…R-24:** EXECUTABLY_ENFORCED (in whole or in a named part) **12**;
PRACTICED without enforcement **8**; DOCUMENTED without enforcement **3**; PROPOSED-only
component **1**.

---

## PART 3 — Failure-derived practices

Every one of these exists because something went wrong on a dated occasion. The repository does
not merely admit this — it records the date *"because a rule whose origin is forgotten is a rule
that gets relaxed."*

| Date | What failed | How it was detected | Practice that emerged |
|---|---|---|---|
| 2026-07-09 | Johannsen 2018 sat unread in the corpus, correctly triaged Tier A / HIGH, while LEGEND re-derived the same functional result in silico | Operator noticed the duplication of effort | `unread_gold.py`; reading debt becomes a counted ratchet (FM-011) |
| 2026-07-12 | Three rejections of the form `P → C` where P was never checked because it was "obvious" (`polyUb → proteasome`) | Domain re-audit | The entire premise/negative discipline: `PREMISE_TAG`, `REVIVAL_TRIGGER`, the re-audit rule, `DEFAULTS THAT BIT US` |
| 2026-07-12 | A Tier-C thyroid paper, shelved as low-signal, held the degradation biology of a WWOX SDR missense allele | Read anyway | `gold_is_in_the_details.md` as a **superordinate** principle over every gate and tier |
| (with it) | The standing belief *«oncology papers are background for this disease»* — premise: *"relevance follows the disease phenotype"* | Counted which papers had produced key commit candidates: **none was on WOREE** | `DIS-002` reversed; parity of sources and the `DOMAIN_PARITY` rule are the *output of a corrected negative*, not a design choice |
| (later) | *«Whether a folded and active state for Q230P is reachable is not resolvable in silico»* — premise: that "in silico" means ΔΔG + static structure, tagged `DEFAULT_FROM_TEXTBOOK` | A new mechanism changed the question from thermodynamics to dynamics | `DIS-006` reopened **by the re-audit rule**; *"'not resolvable in silico' is not a property of the world: it is a property of the question you are asking"* |
| 2026-07-12 (same case) | That route was then over-transferred to a different allele | Audit | `MECHANISTIC_OVERTRANSFER`; separate synthesis / solubility / turnover / route / function |
| 2026-07-26 | Group never assessed, field density never measured, multi-hop never attempted, corpus never cross-queried — **every check passed and the session graded itself green** | Operator asked | `deepdive_manifest.py`: *"An obligation that produces no artifact cannot be enforced"* — five required slots, waivable only with ≥40 characters of argument |
| 2026-07-26 | A hash-chained receipt declared four ledger entries that did not exist, in an ID scheme the repository does not use | Later inspection | `session_self_eval.py`: declared outputs must resolve in one of six landing files |
| 2026-07-26 | A `complete_fulltext_read` declared without ever enumerating the reference list; lost PMID 20067585, which qualified its own inferences | Later multi-hop | `references` added as an optional coverage key + a ratchet (history not rewritten) |
| 2026-07-26 | The single most valuable finding of a deep dive — a supplementary figure whose panels contradict its own caption — was invisible at caption level | Raster inspection | `captions_only` as a coverage state distinct from `read` |
| 2026-08-04 | **No verbatim locator existed anywhere in canonical state**, across every complete read in the ledger | An export tried to use them | Rule 5b; 14 locators recovered by reopening papers already read |
| 2026-08-04 | A figure panel reversed a conclusion the running text did not contain | Panel inspection | Figures declared a separate surface, never read through text conversion |
| 2026-08-05 | A locator whose anchor named `files/corpus/*.jsonl` passed `validate()` with zero errors — the only check was a test nobody must run | Review | The refusal moved into the gate; then into a shared `corpus_firewall` |
| 2026-08-06 | An unmarked asterisk was the difference between *"not significant"* and *"not tested"* | Panel inspection | Statistical marks read from the image; absence of testing recorded as a fact |
| 2026-08-06 | By-name corpus recognition survives no rename; a copy out of `files/corpus/` defeats it | Review | `corpus_firewall.looks_like_corpus` asks what the file **is** |
| 2026-08-06 | A legacy receipt attested reading depth for a PMID its own paper record contradicted | Ledger audit | `receipt_invalidation` — forward-only, history retained, active index corrected |
| 2026-08-10 | `PMID 32000863`: 5 of 22 locators did not occur in its own XML — transcribed as the page reads, not extracted as the artifact contains | `locator_audit.py`, written for exactly this | Legacy manifests get a mechanical quote-existence audit |
| 2026-08-10 | Four automatic panel counters produced four wrong small plausible integers in one session (27/32, 17/69, 22-via-fallback, 7-unreliable) | Printed letters visible in the caption | Counters must refuse; *"a lettering gap is not among"* the refusals — named as a missing fourth refusal |
| 2026-08-10 | 21 of 45 queue entries had no resolvable identifier; two entries were one paper for months | Identity sweep | LINT identifier gates |
| 2026-08-10 | 7 of 34 XML surfaces place every `<fig>` outside `<body>`; a body-scoped extractor shows no caption, raises no error, and the manifest still validates | `caption_census.py` | `SURFACE_CONTAINMENT_PRECHECK_GATE`; count by tag name, never by regex (`<fig\b` matches `<fig-count>`) |
| 2026-08-10 | Figure 3B of `PMID 42422765` turned a "dose-dependent" continuum into a threshold | Panel inspection | Third dated instance behind `panel_text_relation` |
| 2026-08-10 | A supplementary declared unavailable had been fetched by another actor 73 minutes earlier; **two retractions rested on that false premise** | Corpus cross-query | *"having tested whether I could retrieve it and recorded the answer as a property of the artifact"* — the shared tree is checked first |
| 2026-08-10 | Six locators across five papers, found by three actors independently, where **no admitted enum value was true** | Convergence | `panel_qualifies_text` added; *"When no admitted value is true, the defect is the enum"* |
| 2026-08-11 | A file-level ToUnicode screen passed a PDF whose map is missing *exactly* where α, β, × are set | Per-font screen | *"the predicate 'the file has a glyph-to-Unicode map somewhere' is not the predicate that protects a quote"* |
| 2026-08-14 | `PMID 20530675`: a figure title generalises to "in osteosarcoma" what the paper's own Results paragraph withdraws | Sequential read | Third failure class isolated: modality intact, **scope** overreached |
| 2026-08-14 | An inherited commit candidate had the substrate of a degradation statement reversed | Horizontal corpus audit | Skill now requires enzyme/process, substrate, sign, edge-modulator |
| 2026-08-15 | A census of the same class by three actors produced three different numbers; none had written down what it counted, and one measured the wrong tree | Comparison | *"The predicate is printed, not implied… The root is a required argument and is echoed back"* |
| (undated, D-16) | An unquoted shell heredoc executed `` `references` `` as a command and silently deleted the word from a hash-chained receipt — **the JSON stayed well-formed, so no check could see it** | Reading the stored record | *"never construct append-only-ledger content through an unquoted heredoc"*; **validity is not fidelity** |

**The pattern across all of them.** Not one was caught by the check that was supposed to catch
it. They were caught by an operator's question, a later export needing something that was not
there, a printed letter visible in a caption, a digest comparison, or a second actor arriving at
the same locator independently. The repository draws the conclusion itself, in
`deepdive_manifest.py`: *"A gate can only see what was written."*

---

## PART 4 — Formalization gaps

Labels are local to this analysis.

### ALREADY ADEQUATELY FORMALIZED
- Manifest section obligations (5 sections + locators + skills-considered), with argued waivers.
- Locator structure: proposition, ≥30-char verbatim snippet, `surface`, fingerprinted artifact,
  `panel_text_relation`, coupled pointer + needle for disagreements.
- Receipt schema: depth ladder, 9+1 coverage keys, 6-state coverage vocabulary, 9-value re-read
  reason enum, hash chain + tail anchor, forward-only invalidation.
- Text-surface integrity: sentinel refusal, `article_binary` vs `article_text` separation,
  suspect-refusal-not-normalisation, page adjudication as recipe with `crop_contains_span`.
- Queue identity, and the four-current/BATCH_COMMIT promotion boundary.

### FORMALIZED BUT NOT ENFORCED
- **Rule 4 (no `grep` as analysis)** — binding prose, unobservable by construction.
- **`PREMISE_TAG` / `REVIVAL_TRIGGER`** — LINT checks them only inside the dismissal ledger, and
  only at `WARN_BUT_PROCEED`. The obligation as written covers *"every rejection **and every
  non-trivial conclusion**"*; nothing checks the second half anywhere.
- **The re-audit rule** — *"every time a new mechanistic DATO arrives, re-scan the dismissal
  ledger"*. It demonstrably runs: `DIS-006` is headed *"REOPENED — by the re-audit rule"*, and
  11 of 12 `DIS-` entries have been re-adjudicated. What is missing is not the practice but the
  **trigger side**: nothing records, for a given incoming DATO, that a re-scan was performed and
  found nothing. A re-audit that fires is visible; a re-audit that was skipped is silent — which
  is the same asymmetry the rule exists to defeat.
- **Rule 5's coverage-map obligation** — `coverage_status` appears in **2 of 64** manifests,
  though receipts carry the section map for all 128.

### PRACTICED BUT NOT FORMALIZED
- **Reading budget / denominator declared before reading** — the sharpest quality discriminator I
  measured, present in **12 of 64** manifests, absent from the required key set, concentrated on
  2026-08-10/11 and after. It has never been retro-applied.
- **Surface preflight as a recorded artifact** — **9 of 64**, always co-occurring with a reading
  budget. Sentinel result, glyph census, per-font ToUnicode screen, and the explicit refusal to
  run a screen that would be *"theatre"* on a surface no locator draws from.
- **Retrieval-route ledger** — which routes were tried, which returned what, which artifacts were
  destroyed as false. Recorded in prose, in varying places, with no slot.
- **Self-citation / field-density measurement of a synthesis** — one strong instance.
- **Explicit provenance separation of arcs** (`three_arcs_kept_separate`) — **1 of 64**.
- **Named-consequence gap declaration** (`coverage_gaps` with the load-bearing number identified)
  — 2 of 64.
- **Distrust of automatic counters** — four documented miscounts; the fourth refusal identified as
  missing is still identified as missing.

### PARTIALLY CAPTURED
- **`panel_text_relation`** — enforced where present, but **230 of 1002 locators (23 %)** predate
  the field and carry no value; `unknown_legacy` is defined as *"owed a re-read, not a guess"* and
  that debt is not counted by any ratchet I found.
- **Supplementary material** — the vocabulary distinguishes `read` / `not_read` / `unavailable`
  / `not_present` precisely, and the practice barely reaches it: **1 of 1002 locators**, 23 of
  128 receipts.
- **Figure surface acquisition** — the preflight spec asks for PMCID, structured surface, licence
  and class but **not** for a figure surface, which is why four "structured" papers were blind to
  their own panels.
- **Dossier quotations** — audited by a deliberately non-blocking tool; the `elsewhere` and
  `stitched` buckets are known hazards with no owner.

### OBSERVED ONLY LOCALLY
- **The observation freeze** — 1 PMID, 2 files. The single strongest anti-confirmation-bias
  artifact here, executed once, by one actor, in one session.
- **Blind adversarial locator audit** — the skill and the `(proposition, quote, anchor)` triple
  contract exist; the manifests that most need it record it as **OWED**, including the one
  carrying two text-versus-panel contradictions and two withdrawn-then-reinstated claims.
- **Divergent lanes.** The 2026-08-11 manifests split cleanly: 8 of 20 carry reading budget +
  surface preflight; the other 12 (a separate acquisition lane) carry neither. Practice is not
  uniform across actors, and nothing measures the divergence.

### UNCLEAR
- Whether `reading_budget` was omitted from the required key set by decision or by not having
  been proposed yet. I found no design record either way.
- Whether `T1`–`T4` transferability tiers have a definition anywhere, or exist only as usage —
  the registry qualifies them in prose so often (*"T1 nominale, T3 di fatto"*) that the bare tier
  may not be load-bearing.
- Whether the four `unread_premises` counted by `growth_anchors` are the same class as
  `UNREAD_PREMISE` in the queue prose. The identifiers coincide; the predicates were not
  reconciled in the time available.

### The single largest gap
`roles/scientist.md` is **122 lines**, its `status:` is **`PROPOSED — binding once Mirror hostile
review passes and the operator approves`**, and it compresses this entire reconstruction into one
sentence:

> *"Parity of sources, the ban on grep as a method of analysis, verbatim locators captured while
> the document is open, structured surfaces preferred over PDFs, figures inspected at original
> resolution, the full-text read receipt — all of it continues to bind."*

Six clauses. Of the twenty-four rules in Part 2, that sentence names five. The reading modes
protocol that would extend it is likewise `PROPOSED` and says of itself: *"Until then it binds
nobody."*

---

## PART 5 — Candidate areas for a future Scientist Contract

Subject areas only. No normative language, no causal-graph contract, no ordering implied beyond
grouping.

**Highest-value, because measured practice exceeds any written obligation:**

1. **Reading budget and denominator** — establishing, measuring and declaring the scope of a
   reading before interpreting it, including how a denominator that cannot be obtained is
   declared.
2. **Surface preflight** — choosing and screening the evidentiary surface before the paper is
   opened, and recording the screen's own limits.
3. **Figure surface acquisition** — the gap that made four structured papers blind to their
   panels; currently in no specification.
4. **Text-versus-panel adjudication as a judgement obligation** — the structure is enforced; what
   is not required is that the question be *asked* of a paper at all. 7.9 % of locators say it
   matters.
5. **Supplementary material** — the weakest measured surface (1 locator in 1002) against a
   vocabulary that already handles it precisely.

**Second tier, because the practice exists but has been executed once or twice:**

6. **Neutral first pass and its freeze** — separation of observation from interpretation, and
   what evidence demonstrates the separation occurred.
7. **Provenance arc separation** — keeping this paper's datum, another paper's datum and the
   combination apart, including what an adjudication does *not* license.
8. **Blind adversarial locator audit** — when a reading may touch a consolidated baseline, and
   what the auditor may and may not see.
9. **Retrieval-route ledger** — which routes were tried, what each returned, and the destruction
   of false artifacts.
10. **Group, field-density and funding weighting** — measured counts, and the boundary at which
    context stops adjusting attention and would start substituting for evidence.

**Third tier, because the rule is written and unreachable by any current check:**

11. **The re-audit loop** — the step named as the difference between self-correction and
    self-improvement, with no artifact proving it ever ran.
12. **Premise tagging beyond rejections** — the written obligation covers non-trivial conclusions;
    only rejections are checked, and only with a warning.
13. **Legacy re-read debt** — the 23 % of locators owed a `panel_text_relation` re-read, and the
    absence of a ratchet counting them.
14. **Uniformity across actors** — whether two readers on the same corpus in the same week are
    permitted to work to visibly different depths, and what measures the difference.

---

## 6 · The central question, measured

> *Which parts of high-quality Scientist work are protected by executable machinery, and which
> depend on the Scientist remembering how to think?*

**The repository has already answered this about itself, numerically.** In
`framework/eval/learned_gates_registry.md`, over **79 gate rows**:

| Status | n | % of 79 |
|---|---:|---:|
| `ACTIVE_METHOD` — a documented reasoning constraint | **55** | 69.6 % |
| `ACTIVE_EXECUTABLE` — enforced by public code and regression tests | **19** | 24.1 % |
| `PENDING_EXECUTABLE` | 2 | 2.5 % |
| `PROPOSED` | 2 | 2.5 % |
| `SUPERSEDED` | 1 | 1.3 % |

**Roughly one gate in four is machinery. Three in four are memory.** The same ratio appears in
the manifests from the other direction. `deepdive_manifest.validate` requires **ten** keys —
`pmid`, `receipt`, `landing`, `skills_considered` and the six `SECTIONS` — and all ten are present
in 64/64; `doi` is the eleventh key present in every manifest without being required. Meanwhile
the four keys carrying the most discriminating work — `reading_budget` (12), `surface_preflight`
(9), `figure_extractions` (6), `coverage_status` (2) — are optional, and appear in a minority.
**What is required is universal; what is optional is where the quality lives.**

### What is genuinely MECHANIZABLE, and largely already is
Identifier resolvability · receipt existence, chain and tail anchor · declared-output resolution ·
locator slot, minimum length and existence-in-artifact · surface declaration and sentinel refusal ·
artifact fingerprinting and kind · coupled-relation pointer and needle resolution · adjudication
`crop_contains_span` and digest regeneration · corpus-artifact refusal · population ratchets ·
waiver length. **Plus three that are not yet and could be:** a required `reading_budget` slot;
a required figure-surface field in the preflight; a ratchet counting `unknown_legacy` locators.

### What is irreducibly SCIENTIFIC JUDGMENT
Whether Figure 7 supports the author's causal reading · whether an apparent rescue is
genotype-specific · whether an alternative explanation remains viable · whether a caption
describes the blot beneath it · whether a hedge in the Results was carried into the figure title ·
whether a transferred mechanism is a datum or a bridge hypothesis · whether the decisive detail is
in a paper the tier says is background · whether an absent statistical mark means "not
significant" or "not tested". **A contract can require that each question be asked, and require
the answer to be recorded in a slot — it cannot supply the answer, and nothing here suggests it
should try.**

### The HYBRID class, which is where the real leverage is
Every rule where the *structure* is checkable and the *content* is not: `panel_text_relation` (the
enum is enforced; which value is true is a reading), the reading budget (the slot is trivial; the
count is a judgement that four scripts got wrong in one session), waivers (length is enforced;
whether the argument is good is not), `corpus_crossquery` (the slot is required; whether you
actually looked is attested). This is precisely the design the manifest already articulates about
itself:

> *"a manifest can be filled with hollow but well-formed content. This design does not make that
> impossible — it makes it **reviewable** instead of invisible, and it makes the honest path
> cheaper than the dishonest one."*

That sentence is, as far as I can tell from the evidence, the operating theory of the entire
system: **not automation of judgement, but the conversion of silence into an artifact somebody
can disagree with.**

---

## 7 · Limits of this reconstruction

1. **One tree, one moment.** Everything is measured at `fb31c2a`. The `mirror` lane (83 commits
   not in HEAD) and `legend-operating-convention-v1` (3 commits) were not measured, and practice
   recorded there is not represented here.
2. **`files/` is gitignored and nearly empty in this worktree** (55 files, 3 PDFs). I could not
   re-run `locator_audit.py` or `dossier_quote_audit.py` against a real corpus, so every claim
   about quote-existence is taken from the tools' own recorded findings, not re-derived. That is a
   weaker standing than the counts, and it is marked as such where it appears.
3. **Population-derived figures decay.** *"33 of 51 local PDFs"*, *"7 of 34 XML surfaces"*, the
   surface census's 87 papers and its `825fc4a9d8415b0e` digest are all quoted from records dated
   2026-08-10 to 2026-08-15 and were not re-measured. Object-derived counts (64 manifests, 1002
   locators, 128 receipts, 79 gate rows) were measured here, today, at this HEAD.
4. **Six of the twelve `failure_taxonomy` gates and much of `learned_gates_registry` describe
   engineering rather than reading.** I have not treated engineering meta-defaults (D-05 to D-13)
   as reading practice, though the repository files them together.
5. **The Italian/English split is real and I did not normalise it.** Several claims, ledger
   entries and queue statuses are in Italian; quoting them translated would have made them
   unfindable.
6. **No peer synthesis was performed and none is implied.** Convergence with Scientist A and
   Scientist C is a separate stage.

---

## 8 · Checks run after writing this file

| Check | Result |
|---|---|
| `python3 framework/scripts/legend_lint.py .` | **PASS** — 1 INFO (`CLAIM 010`, pre-existing) |
| `python3 scripts/public_release_gate.py` | **PASS**, BLOCKS 0 — 4 `[REVIEW]` items, all pre-existing in manifests and the queue, none in this file |
| `git status --porcelain -uall` before analysis | clean; this file is the only addition |

Two counts in the first draft of this document were wrong and were corrected before it was
finished: commit candidates (17 → **16**, the seventeenth file being the standing proposal) and
dismissal-ledger entries (4 → **12**, because `grep -cE '^## '` had counted prose section
headings rather than `### DIS-` records). The second error also changed a conclusion — Part 4 had
stated that no artifact records the re-audit rule ever running, and `DIS-006` records exactly
that. Both were caught by re-deriving from the raw records instead of from my own summary, which
is the same discipline Part 1 § 5.2 attributes to the readings.

---

*Non-canonical learning artifact. No canonical register, claim, hypothesis, governance file, role
contract, validator or routing rule was modified. `roles/scientist.md` was read as evidence and
was not activated. `reviews/` is a declared `CONTROL_PLANE_ROOT` under
`governance/plan_defined_parameters.md` § P5.1, and the candidate content hash is a function of
`(base, tip)` over a domain that excludes that root — so this file moves no candidate hash. It is
**uncommitted** on branch `lettore-b`: an untracked artifact is a surface no gate inspects, so it
is committed or discarded at the operator's direction, not left in place.*
