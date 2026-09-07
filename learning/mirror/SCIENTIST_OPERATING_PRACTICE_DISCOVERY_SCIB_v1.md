# SCIENTIST OPERATING PRACTICE — DISCOVERY (SCIB, v1)

**Independent reconstruction of the implicit LEGEND Scientist methodology, from repository evidence.**

> **Non-canonical learning artifact.** Analytical only. It modifies no register, claim, hypothesis,
> governance file, role contract, validator or routing. It does not activate `roles/scientist.md`,
> and it is not a Scientist Contract. Labels used in PART 4 are local to this analysis and are not
> repository governance vocabulary.

---

## 0 · State safety, measured population, and what this analysis could not verify

### 0.1 Actor and worktree identity

| | |
|---|---|
| Worktree | `<REPO_ROOT>/.claude/worktrees/mirror` |
| Branch | `mirror` |
| HEAD at task start | `2767333` · 2026-08-23 20:02 · *"The fix for the quotation defect went onto one pattern of two…"* |
| Authoritative ref | `main` = `development/main` = `788c357` · 2026-08-22 18:01 (verified equal after `git fetch development`) |

`origin/main` is `8ab8e4b` (2026-08-01) — the public release remote, far behind, and **not** the
authoritative development state. `legend-operating-convention-v1` (`30cb4f3`, 3 commits ahead of
`main`) is an unmerged feature branch, not an authority.

### 0.2 Staleness found, and how it was resolved

At task start this worktree was **65 commits behind `main`** and 83 ahead, diverged at `908197b`
(2026-08-16). The staleness was **material to this task specifically**:

- `roles/scientist.md` — **modified on `main`**, not present in that form here;
- `framework/protocols/scientist_reading_modes.md` — **added on `main`**, absent here;
- `framework/eval/benchmarks/BENCH-AB-001/` (12 files), `governance/candidates/CAND-20260818-SCIENTIST-AB-SPEC.md`,
  `framework/scripts/lease_state.py`, `governance/decisions/DEC-20260822-ROLE-CONTRACT-ACTIVATION-STATE.md` — all added on `main`.

Had I analysed without resolving this, I would have concluded that no Scientist role contract and
no reading-modes protocol existed — the exact error class the task names.

Counter-check that bounded the risk: the scientific evidence corpus was **not** stale. The
`disease-models/` tree object is byte-identical across merge-base, `main` and `mirror`
(`9ef1a09a7204bcfb3cb765cf041ff79039e6fdf5` in all three). The divergence was entirely in
`framework/`, `governance/`, `roles/`, `ledger/`, `learning/`, `reviews/`, `runtime/`.

Resolution: `git merge --no-edit main` — dry-run showed **zero conflict markers**; merged as
`c7e8d6e`. Now **0 behind `main`**, 84 ahead. No local work overwritten: all 7 untracked
`learning/mirror/` and `reviews/mirror/` files survive the merge unchanged. Tracked files
618 → **683**.

### 0.3 Measured population

Enumerated before measurement, never inferred from a tool's own output.

| Surface | Count | Path |
|---|---:|---|
| Deep-dive manifests (JSON, machine-readable) | **64** | `disease-models/wwox/research/deepdive_manifests/` |
| Verbatim locator entries inside them | **1 002** | `verbatim_locators.entries[]` |
| Full-text dossiers (prose) | **33** | `research/fulltext_dossiers/` |
| Full-text read receipts (hash-chained) | **128**, over **82** distinct PMIDs | `registries/fulltext_read_receipts.jsonl` |
| Commit candidates | **16** CC + **1** PROPOSAL | `research/commit_candidates/` |
| Session self-evaluations | **22** | `research/session_evaluations/` |
| Page-adjudicated articles | **3** PMIDs / 5 files | `research/page_adjudications/` |
| Observation-freeze / pattern audits | **2** | `research/pattern_audits/` |
| Full-text queue entries | **72** | `research/full_text_queue_current.md` |
| Canonical claims | **39** | `registries/claim_registry_current.md` |
| Registry records | **70** `PAPER` · **356** `CORPUS` · **390** literature | `registries/` |
| Learned reasoning gates | **79** | `framework/eval/learned_gates_registry.md` |
| Executable machinery | **51** files in `framework/scripts/`, **24** of them test modules | |

Executable gates re-run in this tree, after the merge:

```
legend_lint.py .                → VERDICT: PASS  (1 INFO: CLAIM 010 wikilink not required)
growth_anchors.py check         → PASS · claims=39 papers=70 corpus=356 literature=390
                                         registry_only=15 unread_premises=4
fulltext_receipts.py verify     → OK: 128 chained receipt(s), tail anchored
deepdive_manifest.py × 64       → 64/64 PASS
```

### 0.4 🔴 The limit of the last line, stated with its denominator

The 64/64 pass is **STRUCTURE ONLY**. The validator prints its own scope, and I am quoting it
rather than paraphrasing it:

> `VERDICT: PASS — manifest for PMID 34831305 is complete (0 gap(s)); verification scope: STRUCTURE ONLY: local artifact existence, SHA-256 and exact text locators NOT VERIFIED`

`files/` is gitignored and exists **only in the shared checkout**. Run here with
`--verify-artifacts --require-current-schema`, the same manifest emits `[BLOCK]` on every one of
its 13 locators — not because the quotes are wrong, but because the artifact is absent from this
tree. **So this analysis verified the shape of 1 002 locators and the content of none of them.**
Every statement below about quote fidelity is a statement about *what the machinery checks
elsewhere*, not about a check I ran.

That the tool discloses its own scope is itself a finding — see RULE-29.

### 0.5 Independence record

Per §0 of the task, I searched every ref by **filename only** for peer outputs and did not open
them.

- **No** file named `SCIENTIST_OPERATING_PRACTICE_DISCOVERY_*` exists on any branch or remote ref.
- Branch `lettore-b` (2026-08-25 00:20) carries `learning/scientist-b/SLR-scientist-b-0001.md`,
  `reviews/scientist-b/REV-EVIDENCE-SCIB-001.md`, `reviews/scientist-b/SCIENTIST-REVIEW-STANDARD-v1.md`.
  **Existence recorded; content not inspected.** These post-date the previous evidence-review
  assignment and their authorship relative to this seat is unresolved, so the conservative rule
  applied.
- Branches `lettore` and `lettore-c` were compared to `main` at **path level only**, to establish
  they carry no output for this task. They do not.
- No synthesis document was read.

### 0.6 🔴 A seat/identity mismatch this analysis must declare rather than absorb

`framework/protocols/scientist_reading_modes.md` §1.1 fixes `scientist-b` to worktree `lettore-b`,
branch `lettore-b`. **This session is on worktree `mirror`, branch `mirror`.** The task names the
output `…_SCIB_v1.md`. I have used the mandated filename and written it to this worktree's
established non-canonical learning path, and I am recording the mismatch rather than asserting an
ACTOR_ID I cannot demonstrate. The protocol that would bind it is itself `status: PROPOSED —
binding on canonical execution of CAND-20260818-SCIENTIST-AB-SPEC… Until then it binds nobody.`

---

## PART 1 — The reconstructed end-to-end Scientist workflow

Derived from what the artifacts *record having done*, in the order the records show it happening.
**The workflow does not begin with opening the PDF.** Five of its twelve stages precede that.

### Stage 0 · Establish which tree you are measuring

Not a preamble — a load-bearing step, and the one most visibly paid for. `reading_state.md`, a
generated file, opens with the warning in its own header:

> 🔴 **This page is true of ONE checkout — the one that generated it.** … Work sitting on an
> unmerged branch is not here, and a count over unmerged state is a count of work that is not in
> the model.

The receipt for PMID 20530675 records the same discipline applied to the *validator itself*:

> "main@d06a4a1's deepdive_manifest.py is 1,559 lines against this worktree's 1,359 — a 200-line
> per-font encoding-verdict subsystem that did not exist when this branch was aligned. Validating
> with the branch copy would have been validating against a validator older than the rule.
> Extracted with `git show d06a4a1:` and used for every quote match and the verdict."

`caption_census.py` states the same thing as a rule with its cause: *"That census was wrong because
a shell had inherited a worktree's cwd. `files/` is gitignored, so it exists in exactly one
checkout, and a relative path measures whatever tree you happen to be standing in."*

### Stage 1 · Duplication and prior-reading control

Before a paper is opened, the Scientist asks whether it has already been read, and *how deeply*.
The check is against four surfaces, not one: `paper_registry_current.md` (70 `PAPER` + 356 `CORPUS`
records), `literature_tracking_log_current.md` (390), the receipt ledger (128 receipts / 82 PMIDs),
and `full_text_queue_current.md` (72 entries).

Duplication control is **identifier-first**, and it became so by failure. The queue header records
it: on 2026-08-10, *"21 voci su 45 nominavano il proprio paper solo con un numero interno morto, un
id d'inbox o un autore-anno; `FT-004` e `FT-029` erano lo stesso paper da mesi, duplicato che nessun
dedup poteva vedere."* `FT-004` is preserved rather than deleted — *"cancellarla toglierebbe la
traccia del duplicato invece della sua causa."*

### Stage 2 · Decide whether an already-read paper needs a *new* reading

This is a first-class decision with its own controlled vocabulary. **46 of 128 receipts (36%) are
not first reads.** `reread_reason` across the ledger:

| `reread_reason` | n |
|---|---:|
| `first_read` | 82 |
| `inadequate_prior_coverage` | 20 |
| `receipt_correction` | 14 |
| `explicit_operator_request` | 5 |
| `new_version_or_supplement` | 3 |
| `adversarial_reanalysis` | 2 |
| `receipt_invalidation` | 1 |
| `new_question_outside_prior_coverage` | 1 |

Parallel reading is explicitly *not* a correction: `reading_state.py` computes a **union** across
receipts and refuses to let the latest one speak for the paper — *"Two actors can read one paper in
parallel and both be right; the later receipt is not a correction of the earlier one."* One paper
(PMID 42422765) is currently in that state.

### Stage 3 · Establish why *this* paper is worth deep analysis

Two orthogonal mechanisms, and they pull against each other on purpose.

**Ranking orders reading. It never authorises not reading.** `gold_is_in_the_details.md` rules 1–3
are absolute, and `coverage_report.md` is built to keep the cost visible: **338 of 426 records
(79%) are "catalogued only — the debt"**, and the page says *"It is supposed to look incomplete:
the denominator is the whole known corpus, not the part already processed."*

**Disease proximity is not the priority axis.** Rule 3: *"Disease context is never a reason to
downgrade."* The worked example is a **thyroid-cancer** paper filed `Tier C` that carried the
degradation biology of an SDR missense variant. `DIS-002` in the dismissal ledger is the rejection
«Oncology papers are background for this disease» → **❌ FALSE, REVERSED**. The intuitive hierarchy
is documented as *exactly inverted*: oncology often decades ahead on folding/stability/turnover;
adult neurology fully relevant; syndrome case reports the most phenotype-consistent and the most
descriptive — *"Consistency ≠ usefulness."*

**Unread premises are the sharpest priority signal.** `unread_gold.py` exists because of failure
mode FM-011: a paper correctly triaged `Tier A / HIGH` and never read, while LEGEND *"reconstructed
the same conclusion in-silico from scratch while the experimental proof was already in the
corpus."* `growth_anchors.py check` currently reports `unread_premises=4` as a ratchet. The queue
uses the class name directly — FT-002: *"era esatta, ed è la classe `UNREAD_PREMISE` — una fonte su
cui il modello si appoggiava senza averla letta."*

### Stage 4 · Group, field density, and retraction — measured, not assumed

Every manifest carries `group_assessment`; **60/64** carry its full structure (4 predate schema v2).
Fields: `total_publications`, `publications_on_gene`, `research_type`, `is_primary_group_for_disease`,
`weighting`.

- `research_type`: `experimental_lab` 42 · `mixed` 10 · `primary_disease_group` 4 · `descriptive_clinical` 3 · `adjacent_method_expert` 1 · absent 4.
- `is_primary_group_for_disease`: **True 17 · False 43 · absent 4.**

The counts are **measured and sourced**, not asserted — PMID 34831305: *"Europe PMC author counts
measured 2026-08-10: Aqeilan RI 149 total and 79 with WWOX; Steinberg DJ 13 total and 7 with WWOX."*

And the conclusion drawn from provenance is a **weighting on independence, never on truth**, in the
same field: *"That raises confidence in model coverage and technical context, but the present
article is a narrative review from the same group that produced several load-bearing primaries. Its
observations and interpretations are weighted separately: it is authoritative synthesis, not
independent replication."*

`field_density` records **155 measured PubMed queries** across the population (4 manifests carry
zero). A failed query is recorded as failed, not guessed: *"A fourth sequential ESearch request for
a metabolic intersection returned HTTP 429 and was not substituted with a guessed count."*

`retraction_check` is present in **64/64** manifests; `checked: true` in **25/64**, the remainder
carrying the key with a null/other value.

### Stage 5 · Surface preflight and acquisition cascade

The acquisition step is where the largest measured methodological investment sits, and it is
governed by rules 5c–5d.

**Preference order:** structured PMC/Europe PMC XML or HTML **over** the PDF, always. Across the 72
queue entries the derived `Surface:` line classifies **38 `structured` · 28 `absent` · 13
`pdf_only`**. Rule 5d's reason is measured, not stylistic: *"33 of 51 local PDFs carry the defect …
`Wwox\x01/\x01` is `Wwox⁻/⁻` while `Wwox\x02/\x01` is `Wwox⁺/⁻` … Roughly 80% of the damage is
printable, so no control-character check can see it."*

**A surface is screened before a locator is drawn from it.** `_refuse_suspect_surface()` refuses a
declared text surface carrying C0 controls or `PRINTABLE_SUBSTITUTIONS`, and refuses on
*suspicion by absence* — zero `< > ≤ ≥ ± × − µ α β Δ` in a paper that says "significan" three or
more times (`MIN_STATISTICAL_MENTIONS = 3`). **A `SUSPECT` surface is refused, never cleaned**,
because cleaning launders the defect into every quote drawn from it.

**"Not found on one surface" is never "no full text".** The cascade is documented as *routes*, and
the disagreements between them are recorded:

- PMID 42422765 S8: *"Five ordinary routes had returned PMC interstitial, 404, 500 or FTP denial.
  The PMC interstitial itself exposed a public SHA-256 proof-of-work protocol. Completing that
  protocol returned both original PDFs without credentials."* — the route is now
  `framework/scripts/pmc_pow_fetch.py`, which *"fails closed on an unrecognised page or a
  non-PDF retry."*
- PMID 30158849 / 39952983 / 42082822: figures acquired via the **Europe PMC REST
  `/{PMCID}/supplementaryFiles`** endpoint. On 42082822 the probe answered a *negative*: *"the
  deposit declares one `<fig>` and the package contains one figure, so one figure is all that
  exists. That is the reason the first gesture is a probe and not an assumption — it confirms an
  absence as well as a presence."*
- PMID 22634283: figures first waived because the article is not open access; **the operator refused
  the reasoning** — *"NON-OPEN-ACCESS IS A CONSTRAINT ON REDISTRIBUTION, NOT A DISPENSATION FROM
  VISUAL INSPECTION."* All nine figures were then retrieved, fingerprinted and inspected. *"The
  waiver was a category error and it cost two panel findings that the text does not contain."*
- PMID 15070730: three supplementary figures **could not** be retrieved. Recorded as `figure_gap`,
  with `panels_present_supplementary` explicitly *"UNKNOWN AND DECLARED AS UNKNOWN RATHER THAN
  PADDED."*

Where no structured deposit and no trustworthy text layer exist, the article enters **page
adjudication** (rule 5e): locators anchored to the *rendered page*, published as a regeneration
recipe rather than as images. Currently **3 articles**.

**Abstract-only is honest and clears nothing.** Rule 8: *"A local abstract corpus is a map, never
the territory… an `abstract_only` event is honest but clears no reading debt."* The receipt ledger
holds exactly **2** `abstract_only` and **5** `queried_not_full_read` events out of 128, and the
validator carries an `abstract_anchoring_waived` flag (present in 36/64 manifests).

### Stage 6 · Declare the reading budget — the denominator — before reading

Present in **12 of 64 manifests**. Where present, the field is `declared_before_reading: true` and
carries `figures_present`, `panels_present`, `tables_present`, `supplementary_elements_present`,
`panels_inspected`, `panel_coverage`, and — decisively — a `method` string stating **how the
denominator was derived**.

The recurring formula is *"MEASURED, NOT INTENDED"*, and the counting method is **reading the
captions**, explicitly *not* running a parser (RULE-14, PART 3).

Coverage is reported as a fraction against the measured denominator, and shortfalls are named
rather than absorbed: 40/40, 32/32, 39/39, 24/24, 22/22, 29/29, 17/17, 7/7, 6/6 — but also
**17/23** (PMID 31543760, corrected downward), **5/17** (PMID 16061658, a deliberately bounded
adjudication), and **0/26** (PMID 30356099, no figure image on disk plus a named privacy waiver on
patient photographs).

### Stage 7 · Neutral first pass, frozen before interpretation

`research/pattern_audits/PMID34831305_observation_freeze.md` is the executed instance:

> - Frozen at: 2026-08-10T07:43:00Z
> - Reading order: XML body sequentially, Table 1, disclosures, 224 references, Figure 1 pixels, Figure 2 pixels.
> - **Pattern prompt deliberately withheld until after this record.**

Twelve numbered observations, then — separately — *"Figure acquisition facts recorded before
inspection"* with the resolution discrepancy between XML-declared originals (4542×2601) and what the
CDN actually served (757×434). The paired `PMID34831305_pattern_assessment.json` is the interpretive
pass that the freeze was withheld from.

The same separation appears inside manifests as `found_or_sought` — **229 entries across 14 PMIDs** —
distinguishing evidence met by reading in sequence (*"found — read in sequence"*) from evidence
deliberately hunted (*"sought — the rescue is what separates competition from co-occurrence"*).

### Stage 8 · Experiment-by-experiment interrogation

The dossier form carries the reconstruction. Heading vocabulary across the 33 dossiers is **not
uniform** (see PART 4) but the recurring spine is: *Verdict* (25/33) → *Coverage map* (12/33) →
figure/panel audit → **DATO → INFERENZA → IPOTESI / ESPANSIONE** (5–6/33 as explicit headings) →
*Horizontal impact* (7/33) → *Limits* → *Commit impact* (5/33) → *Process report* (9/33).

What the interrogation actually reaches, evidenced in the locator sets: the biological question, the
system (species / cell type / stage), the intervention, the **directionality**, the controls, the
statistical marks, the dependency between experiments, and the authors' own hedging. Examples of the
last, which is where "gold in the details" repeatedly lands:

- PMID 16061658: *"AND THE CONCLUSION IS HEDGED IN THE ORIGINAL. The authors write 'may compete'.
  Every downstream restatement…"*
- PMID 32581702: *"il test proteico della claim centrale è stato fatto, è risultato **non
  significativo**, e la Discussione non lo ripete."*
- PMID 20530675: the paper prints its own refutation of a figure title — *"this was not evident when
  paired comparisons were performed on the 56 available cases"* — and a tenth blot lane (`ROS`) that
  the caption and the Results between them never mention, *"and it carries the darkest RUNX2 band in
  the row."*

### Stage 9 · Figures as primary evidence, adjudicated against the text

**This is the single most developed practice in the corpus, and the one with the highest yield.**

Of 1 002 locator entries, **338 declare `surface: figure`** (body 617, table 13, supplement 1, absent
33). **57 of 64 manifests carry at least one figure-surface locator.**

Every locator also declares `panel_text_relation` — a closed enum the validator enforces:

| `panel_text_relation` | n | meaning |
|---|---:|---|
| `text_only` | 417 | no panel bears on the statement |
| `panel_only` | 148 | read from the image; the text carries no equivalent |
| `text_confirmed_by_panel` | 128 | both looked at, they agree |
| **`text_contradicted_by_panel`** | **47** | both looked at, they do not |
| **`panel_qualifies_text`** | **32** | the panel bears on it and neither confirms nor contradicts |
| *(absent — legacy)* | 230 | |

**79 of 772 typed relations (10.2%) record the visual surface disagreeing with or qualifying the
authored one.** They are spread across **31 of 64 papers** (21 with a contradiction, 16 with a
qualification).

The relation is **coupled**: `text_contradicted_by_panel` must carry `contradicts` (a resolvable
`entries[n]` pointer) and `contradicts_needle`; `panel_qualifies_text` must carry `qualifies` /
`qualifies_needle`. Present in exactly 47/47 and 32/32 entries. The validator's own comment states
why: *"Without the pointer the claim is unfalsifiable prose sitting in a JSON field."*

Adjudication is settled **on the pixels**, and the record says so with the resolution it was settled
at. Representative confirmed cases:

- **PMID 18487609** — *"PANEL 5A MEASURES THE IN VIVO DIRECTION AND IT IS UP, NOT DOWN"*; and
  separately, *"THE MAGNITUDE IN THE RESULTS IS UNDERSTATED BY ROUGHLY HALF."*
- **PMID 38499540** — four pairs; the strongest: *"The experiment is OVEREXPRESSION, not loss. The
  panels are labelled EV against WWOX OE, the caption's own body says so two lines below."*
- **PMID 42422765** — *"The text asserts no significant difference in locomotor velocity or distance;
  panels 4D and 4E each carry…"*; and the epilepsy claim, where panel 7C *prints* `0.2000` above the
  bracket.
- **PMID 34634460** — *"THE PANNEXIN BLOCKER RAISED BURST FREQUENCY TWO AND A HALF FOLD, AND BOTH THE
  RESULTS AND THE DISCUSSION DESCRIBE THAT AS AN ABSENCE OF EFFECT."*
- **PMID 39507621** — the figure contradicts *its own caption*: caption 100 mV/mm, calibration bar
  100 µV.
- **PMID 32300104** — *"Figure 1's caption swaps the plotted WWOX and WFPA colour identities."*
- **PMID 42128308** — and the case where the **text is right and the panel is wrong**: a figure
  *"declared as prepared by a generative model loses a category and reassigns a gene"*.
- **PMID 38182577** — the contradiction is in a **Supplementary** figure: *"MCM7 is NOT higher in the
  panel the sentence cites."*

Resolution is **measured before rendering**, never assumed. `figure_ppi_preflight.py` computes native
pixels ÷ placed size to yield an effective-PPI ceiling per image. The anchors then quote it:
*"inspected at the returned native 757×434 pixels after 600-effective-PPI preflight"*; *"read at 400×646 px,
150 dpi — the resolution PMC serves"*; *"cropped at native resolution and upscaled 6× LANCZOS"*;
*"extracted at smask=0 from the publisher PDF (150 effective ppi)"*. Page 7 of PMID 16061658 *"carries
zero images. Figure 6 is entirely vector, so 400 dpi there is resolution, not upsampling — and that
was measured, not assumed from the fact that it looks like a diagram."*

And there is a guard against over-calling a contradiction: **`cited_panel_check`** (22 entries) asks
whether the panel that falsifies is the panel the sentence actually *names*. `DL-METH-082` states it:
*"Una coppia è una contraddizione solo se il pannello che falsifica è quello che la frase cita."* Two
pairs on PMID 38182577 were **downgraded** from contradiction to qualification by this check.

### Stage 10 · Tables and supplementary material — and declaring the gap

Supplementary material is where the refutation repeatedly lives, and where coverage is weakest. Across
128 receipts the `supplementary` axis reads: **`not_present` 35 · `not_read` 27 · `read` 23 ·
`unavailable` 20 · `unknown_legacy` 23.**

The gap is recorded as a *limitation with a route*, not as silence:

- PMID 20530675: *"THE SUPPLEMENT HOLDS THE REFUTATION AND WAS NOT RETRIEVED… SUPPLEMENTAL TABLE 8 is
  where the paired WWOX/RUNX2 comparison fails… A supplement that holds the refutation of a main-figure
  title is not an appendix, and it is why this reading is partial."*
- PMID 32581702: *"`Supplementary Figure S3` **è** l'immunoistochimica di TUBA1A, cioè il negativo
  proteico, e non è stata ispezionata. Chi la ottiene riapra `entries[13]` per primo."*
- PMID 39952983: the `.docx` supplement *"holds Supplementary Tables 1-2 and Supplementary Figures 1-2,
  which are where the Bonferroni-corrected p-values, the QQ plot and the genomic inflation figure live
  — i.e. the statistical support for the paper's central claim. Fingerprinted and declared
  `supplementary: not_read`, with the route open."*
- PMID 30158849: the `.xlsx` is refused as a text surface **by the schema**, and the manifest says so:
  *"`deepdive_manifest._artifact_text` accepts only .xml, .html, .txt and .docx as text surfaces, so
  .xlsx is refused the way a PDF is."*

The counter-example that closes the loop: PMID 42422765 Supplementary Figure S8 was recovered by the
proof-of-work route **and overturned the prior reading** — *"The earlier shorthand 'P0–P5 fully
rescues' therefore exceeded the panel."*

### Stage 11 · Evidence capture — locator, not receipt

The Scientist writes, **while the document is open**, one entry per statement the reading will carry:
`proposition · snippet · surface · artifact · anchor · panel_text_relation`.

Field presence across 1 002 entries: `proposition` **1002/1002**, `snippet` **1002/1002**, `anchor`
**1002/1002**, `surface` 969, `artifact` 969, `panel_text_relation` 772. Artifacts are fingerprinted
(`source_artifacts[].sha256`, present in 60/64 manifests), typed by `ARTIFACT_KINDS`
(`article_binary | article_text | supplement_text | figure | table`), and the *extraction method* is
declared — because rule 5c refuses an ML-converted surface as the artifact behind a locator: *"A quote
checked against that output can pass while matching the reconstruction and not the paper."*

**Capture is contemporaneous, and the one manifest that proves it was not is the one that says so.**
PMID 34214506 is the sole manifest with **zero** locator entries, and its `waived` field carries the
reason:

> *"locators were not captured at reading time: this reading predates the requirement, introduced
> 2026-08-04 after an external export found that no verbatim locator existed anywhere in the canonical
> state. Extraction from the retained artefact is queued and does not require re-reading; the debt is
> declared here rather than left silent."*

**The receipt and the locator answer different questions, and the corpus separates them by tooling.**
`fulltext_receipts.py verify` proves the ledger chain (128 chained, tail-anchored). `locator_audit.py`
asks whether the quote *exists* in the artifact. `legend-locator-audit` — a **blind** auditor receiving
only `(proposition, quote, anchor)` triples plus the source, never the dossier, never the reader's name
— asks whether the quote *supports* the proposition and whether the source says **more or less** than
the proposition claims. The tool's docstring states the boundary itself: *"This asks only whether the
sentence EXISTS in the source. Whether the sentence SUPPORTS the proposition written above it —
overshoot, undershoot — is a judgement… and no amount of string matching approaches it."*

### Stage 12 · Typing, negatives, mechanism, and the promotion gate

**Three-way separation.** `OBSERVATION` / `AUTHOR INTERPRETATION` / `LEGEND INTERPRETATION` exists in
practice with vocabulary: `DATO` (what happened) · `INFERENZA` (derived, declared) · `IPOTESI` ·
`ESPANSIONE`. The distinctive practice is that the type is **decomposed per component of a claim, not
applied to the claim as a whole**. Of 39 canonical claims, **19 carry a bare single-token type** (16
`DATO`, 2 `INFERENZA`, 1 `IPOTESI`) and **20 carry a composite or qualified type** — 14 of those joined
by an explicit `+`. Examples:

> `DATO (statistica di coorte) + IPOTESI (l'assunzione "missense = ipomorfo")`
> `DATO (le misure) + INFERENZA (la portata come confondente)`
> `DATO (biochimica, cinque saggi ortogonali, una mutazione puntiforme) + INFERENZA (trasferimento al neurone umano e a WWOX-DEE)`

Claim `Status` is a separate axis: `consolidated baseline` 18 · `in observation` 17 · `flagged for
review` 2 · `conflicting evidence` 1 · `background only` 1.

**Negatives are claims.** The dismissal ledger opens by naming the asymmetry it exists for — a false
positive *"gets tested → dies"*; a false negative is *"silent, permanent, self-reinforcing"*. Two
obligations follow, and both are visible in the file: **`PREMISE_TAG`** (16 tagged premises: 10
`DEFAULT_FROM_TEXTBOOK`, 4 `INFERENZA`, 2 `DATO`) and **`REVIVAL_TRIGGER`** (11 declared). Of the 12
active rejections, **3 have already reopened or been reversed** (`DIS-001` REOPENED, `DIS-002` FALSE/
REVERSED, `DIS-006` REOPENED by the re-audit rule) and 3 more were withdrawn.

**Mechanism moves under named gates.** `framework/eval/failure_taxonomy.md` and
`learned_gates_registry.md` (79 gates) carry the vocabulary. The gates that govern the move from
*"A and B occurred"* to *"A contributes causally to B"* are explicit:
`MECHANISM_DIRECTNESS_GATE` (*"A surrogate is not the mechanism; the intermediate must be measured"*),
`TARGET_ATTRIBUTION_GATE` (*"A pharmacological rescue does not identify the target automatically"* —
requires binding/engagement, an inactive chemical control, genetic epistasis, a resistant rescue),
`DEGRADATION_DIRECTION_GATE` (*"do not infer causality from co-occurrence"*), `CAUSAL_AXIS_GATE`
(*"Conclude only on the directly measured axis and include INCONCLUSIVE in the outcome matrix"*),
`MECHANISM_TRANSFER_FIREWALL` (*"a route measured on variant X is a hypothesis for variant Y, not a
datum"*), `KG_EDGE_HAS_NO_SIGN`.

**Brainstorming is permitted and quarantined by file, not by tone.** The discovery ledger (3 320
lines; 368 `DL-MECH` references, 98 `DL-BIO`, 79 `DL-MOL`, 42 `DL-METH`, 16 `DL-META`, 10 `DL-REPO`,
9 `DL-THER`) is explicitly *"Research-layer working file. Append-only sui lead; status, mai
cancellazione. Tag epistemici: DATO / INFERENZA / IPOTESI / ESPANSIONE. **Promozione a canonico SOLO
via COMMIT CANDIDATE.**"* Lead status: `open · maturing · promoted-to-CC · parked · refuted`. Each lead
carries a mandatory falsification field (`Esperimento proposto`), a `Belief` level, an
`Evidenza: supporta / refuta / neutrale` split, a `Statement causale`, and `Interconnessioni`.

**Nothing reaches canon inside a reading.** All 16 commit candidates propose; none edits. CC-20260810-34831305-01
is characteristic: *"do not create a new DATO or count the review as independent replication of its
cited primaries"*, *"Preserve the review-to-primary tension"*, **"Batch gate: intentionally untouched."**

### Stage 13 · Self-evaluation, before takeaways

`session_self_eval.py` runs the mechanical half — it compares what a receipt *declared* it produced
against what exists, because *"On 2026-07-26 a receipt was persisted, hash-chained and tail-anchored
declaring discovery ledger entries DISC-2026-07-26-A/B/C and dismissal ledger entry DISM-2026-07-26-A.
None existed… The receipt was immutable and wrong, inside the one subsystem whose whole purpose is to
be trustworthy."* It *"deliberately does not try to score analytical quality."*

The judgement half lands in `research/session_evaluations/` — **22 files**, structured as *Scope and
verdict* → **Content diagnosis** → **Process diagnosis** → **Residual debt**. `CLAUDE.md` orders it
before takeaways, on the stated ground that *"takeaways written first will describe a session that went
well."*

---

## PART 2 — Implicit operating rules

Standing labels: **PRACTICED** (visible repeatedly in real work) · **DOCUMENTED** (written as a rule,
limited observable execution) · **EXECUTABLY_ENFORCED** (a validator/gate refuses non-compliance) ·
**PROPOSED** (non-binding proposal). Where a rule holds two, both are given.
Mechanizability: **MECHANIZABLE** · **SCIENTIFIC_JUDGMENT** · **HYBRID**.

---

**RULE-01 · Measure which tree you are standing in before any count.**
*Evidence:* `reading_state.md` header; `caption_census.py` docstring (*"a shell had inherited a
worktree's cwd"*, *"The root is a required argument and is echoed back"*); receipt FTR-20260814-20530675-01
validating against `main@d06a4a1` rather than the branch copy; this analysis, which began 65 commits
behind and would have concluded that no Scientist contract existed.
*Why it matters:* Every number below is a number about a tree. A coherent measurement of the wrong tree
is indistinguishable from a correct one.
*Standing:* PRACTICED · partially EXECUTABLY_ENFORCED (`caption_census.py` requires and echoes the root)
*Mechanizability:* **MECHANIZABLE**

**RULE-02 · Check receipts, registries and queue before opening anything.**
*Evidence:* 128 receipts / 82 PMIDs; 4 dedup surfaces; `study_dedup_triage.py`; rule 7 (*"Check prior
receipts first"*).
*Why:* The corpus reconstructs conclusions it already owns when it does not.
*Standing:* PRACTICED · DOCUMENTED (rule 7) · EXECUTABLY_ENFORCED at the receipt-writer
*Mechanizability:* **MECHANIZABLE**

**RULE-03 · A queue or registry entry must name a resolvable identifier, leading.**
*Evidence:* LINT codes `QUEUE_ENTRY_WITHOUT_IDENTIFIER`, `QUEUE_ENTRY_IDENTIFIER_NOT_LEADING`; the
2026-08-10 measurement of 21/45 unresolvable entries; `FT-004`/`FT-029` duplicated for months.
*Why:* *"Un riferimento che non si risolve non è un riferimento"* — and a duplicate no dedup can see.
*Standing:* **EXECUTABLY_ENFORCED**
*Mechanizability:* **MECHANIZABLE**

**RULE-04 · A re-read is a first-class act and declares its reason from a closed vocabulary.**
*Evidence:* 46/128 receipts non-first-read across 8 `reread_reason` values; rule 7 (*"a repeated
complete read needs an explicit `reread_reason`"*).
*Why:* Distinguishes deepening, correction and adversarial re-analysis from redundant work.
*Standing:* PRACTICED · **EXECUTABLY_ENFORCED** (validated field)
*Mechanizability:* **HYBRID** — the enum is mechanical; choosing the right member is judgement.

**RULE-05 · Parallel readings union; the later receipt does not supersede the earlier.**
*Evidence:* `reading_state.py` docstring; PMID 42422765 with two siblings on one parent.
*Why:* Last-writer-wins silently erases whatever the other reader covered.
*Standing:* **EXECUTABLY_ENFORCED** (the union is computed, not asserted)
*Mechanizability:* **MECHANIZABLE**

**RULE-06 · No tier, score or category authorises not reading.**
*Evidence:* `gold_is_in_the_details.md` rules 1–2; `READING_DEBT_FALSE_NEGATIVE` gate; `unread_gold.py`
(FM-011); `coverage_report.md` publishing 338 of 426 (79%) as debt; `D-05` — *"The docs said 'ranking
decides only reading order'. The script **refused to download the full text** of the lowest class.
Implementation wins, silently."*
*Why:* A ranking that discards a study is a broken ranking, not a decision.
*Standing:* DOCUMENTED · PRACTICED · **EXECUTABLY_ENFORCED** in part (debt ratchets in `growth_anchors.py`)
*Mechanizability:* **HYBRID**

**RULE-07 · Disease proximity, mechanistic relevance and foundational importance are three axes, not one.**
*Evidence:* rule 3 and the inverted-hierarchy section; the thyroid-cancer worked example; `DIS-002`
reversed; the WWOX oncology line read in depth (PMIDs 15070730, 16061658, 18487609, 20530675, 23435430,
24550385, 25331887, 29724996, 38182577, 38499540 all carry panel-level locators).
*Why:* For a tumour-suppressor gene, the biology needed to interrogate an allele predates the paediatric
disease literature and lives in oncology.
*Standing:* DOCUMENTED · PRACTICED (measurably — the oncology reads are among the densest in the corpus)
*Mechanizability:* **SCIENTIFIC_JUDGMENT**

**RULE-08 · An unread source the model already leans on outranks any new paper.**
*Evidence:* `unread_gold.py` / FM-011; `UNREAD_PREMISE` class in FT-002; `growth_anchors check →
unread_premises=4`; `IMPORTED_PREMISE_ATTRIBUTION_GATE`.
*Why:* *"LEGEND reconstructed the same conclusion in-silico from scratch while the experimental proof was
already in the corpus."*
*Standing:* **EXECUTABLY_ENFORCED** (ratchet) · PRACTICED
*Mechanizability:* **MECHANIZABLE** (detection) + **SCIENTIFIC_JUDGMENT** (what counts as leaning)

**RULE-09 · Group provenance is measured, and it weights independence — never truth.**
*Evidence:* `group_assessment` in 64/64 (full structure 60/64); Europe PMC counts quoted with the date
measured; *"authoritative synthesis, not independent replication"*; `EVIDENCE_REUSE_GATE` — *"Reuse
improves traceability, not replication count."*
*Why:* Same-group confirmation inflates apparent replication in a small field.
*Standing:* **EXECUTABLY_ENFORCED** (section required; `MIN_WAIVER_CHARS = 40`) · PRACTICED
*Mechanizability:* **HYBRID** — presence and counts mechanical; the weighting sentence is judgement.

**RULE-10 · Field density around a finding is measured with real queries; a failed query is recorded as failed.**
*Evidence:* `field_density.queries` required (*"at least one measured query is required"*); 155 queries
across the population; the HTTP 429 *"not substituted with a guessed count."*
*Why:* A sparse intersection changes what a single paper can carry.
*Standing:* **EXECUTABLY_ENFORCED**
*Mechanizability:* **MECHANIZABLE**

**RULE-11 · Prefer the structured surface; record the absence when there is none.**
*Evidence:* rule 5d; `structured_surface_preferred` in `surface_preflight`; queue surface census
38 structured / 28 absent / 13 pdf_only; the 33-of-51 PDF defect measurement.
*Why:* Three extractors agree on the same wrong character, so cross-checking extractors detects nothing.
*Standing:* DOCUMENTED (binding rule) · PRACTICED · **partially EXECUTABLY_ENFORCED** — `_artifact_text`
refuses `.pdf` as a text kind by suffix, but `surface_preflight` itself appears in **9/64** manifests and
the validator does not know the key.
*Mechanizability:* **HYBRID**

**RULE-12 · A SUSPECT surface is refused, never cleaned; never hand-corrected.**
*Evidence:* `_refuse_suspect_surface()`; suspicion-by-absence with `MIN_STATISTICAL_MENTIONS = 3`;
PMID 16061658 — *"Twenty-five corruptions, twenty-three printable (92%). A control-character scan finds
two of twenty-five and reports the surface clean"*; `font_encoding_verdict()` reading the ToUnicode
declaration in one second without extracting.
*Why:* Cleaning launders the defect into every quote drawn from the surface; a hand fix across sixteen
points *"is indistinguishable from a rewrite and verifiable by nothing."*
*Standing:* **EXECUTABLY_ENFORCED**
*Mechanizability:* **MECHANIZABLE**

**RULE-13 · "Not found on one surface" is never "no full text"; cascade failures are recorded as routes.**
*Evidence:* the PMC proof-of-work route (`pmc_pow_fetch.py`, five prior routes failed); Europe PMC
`supplementaryFiles`; PMID 22634283 (non-OA is a redistribution constraint, not a dispensation); PMID
15070730's named `figure_gap` after exhausting `/bin/` and the OA package.
*Why:* Each abandoned route silently converts an available surface into a permanent coverage hole.
*Standing:* PRACTICED · **partially EXECUTABLY_ENFORCED** (the PoW route is scripted and fails closed)
*Mechanizability:* **HYBRID**

**RULE-14 · Declare the reading denominator before reading, and derive it by reading the captions — not from a parser.**
*Evidence:* `reading_budget.declared_before_reading` (12/64); *"MEASURED, NOT INTENDED"*; and four
parser failures in one session, each returning a plausible small integer instead of an error —
27 vs 32 (PMID 18487609, a lettering gap the regex could not see), 7→9→6 (PMID 24550385), a silent
`or 1` fallback (PMID 32581702), and 17 where there are 69 (PMID 34268881).
*Why:* A denominator produced by a fallback that cannot report "I found nothing" is
indistinguishable from a measured one, and coverage is a fraction of it.
*Standing:* **PRACTICED (12/64)** · **NOT** executably enforced — `deepdive_manifest.py` does not know
the key `reading_budget` exists.
*Mechanizability:* **HYBRID** — "a declared denominator with a stated derivation method exists" is
mechanical; "the caption-derived count is correct" is judgement.

**RULE-15 · Report panels *inspected*, never panels *intended*.**
*Evidence:* PMID 31543760 — *"I DECLARED 23/23 BEFORE INSPECTING 23 PANELS. At the moment of writing I
had opened three figures… it is the one I filled in from intention instead of measurement"*, corrected
to 17/23 with four figures waived **by name**; PMID 42082822 an hour later — *"MEASURED, NOT INTENDED —
the correction earned an hour ago on PMID 31543760."*
*Why:* This is the exact defect the corpus documents in other people's abstracts, pointed at itself.
*Standing:* PRACTICED · DOCUMENTED only inside the manifests that carry it
*Mechanizability:* **SCIENTIFIC_JUDGMENT** (no tool can see what an agent looked at) — but the
*declaration* is MECHANIZABLE.

**RULE-16 · A partial reading is bounded on purpose and says so with the fraction.**
*Evidence:* 5/17 (PMID 16061658, *"a bounded authorisation produces a bounded reading, and the residual
debt is declared rather than absorbed"*); 0/26 (PMID 30356099, no image on disk + a privacy waiver on
patient photographs); PMID 20530675 *"Target was one locator per main figure and was NOT met; written as
a shortfall"*; receipts split 63 `complete_fulltext_read` / 56 `partial_fulltext_read`.
*Why:* An undeclared partial read produces a receipt that overstates itself.
*Standing:* PRACTICED · **EXECUTABLY_ENFORCED** at the receipt (`complete` requires no `not_read`)
*Mechanizability:* **MECHANIZABLE**

**RULE-17 · Freeze the neutral observation pass before the interpretive prompt is seen.**
*Evidence:* `PMID34831305_observation_freeze.md` — timestamped, reading order recorded, *"Pattern prompt
deliberately withheld until after this record"*, twelve numbered observations, figure-acquisition facts
recorded before inspection; paired separately with `pattern_assessment.json`.
*Why:* Reduces confirmation bias by making the pattern unable to select the observations.
*Standing:* **PRACTICED, but n = 1 of 64.** No rule requires it.
*Mechanizability:* **HYBRID** — that a timestamped freeze precedes the assessment file is checkable;
that the reading was genuinely neutral is not.

**RULE-18 · Distinguish evidence met in sequence from evidence deliberately hunted.**
*Evidence:* `found_or_sought` — 229 entries across 14/64 PMIDs; *"found — read in sequence"* vs
*"sought — the rescue is what separates competition from co-occurrence."*
*Why:* Separates the completeness of the vertical pass from the aim of the horizontal one.
*Standing:* PRACTICED (14/64) · not documented, not enforced
*Mechanizability:* **MECHANIZABLE** (as a declared field)

**RULE-19 · Figures are a separate evidentiary surface, inspected as images at measured resolution — never through text extraction, never on caption authority.**
*Evidence:* rule 5c; 338 figure-surface locators over 57/64 papers; `figure_ppi_preflight.py`; anchors
quoting native pixels, effective PPI, LANCZOS factor, `smask=0`, crop rectangles; PMID 34634460 —
*"At full-figure scale I first misread which bar of panel 3D was which and nearly recorded that CBX
increased burst frequency, which is the opposite of the finding. Six panels were re-cropped at native
resolution and upscaled 6×–10× before any call was made."*
*Why:* `D-14` — *"A caption is authored prose; a blot is data."*
*Standing:* DOCUMENTED (rule 5c) · PRACTICED heavily · **partially EXECUTABLY_ENFORCED** (a `figure`
surface is an attestation the validator accepts but cannot verify; the PPI preflight is a tool, not a gate)
*Mechanizability:* **HYBRID**

**RULE-20 · Every locator declares whether anyone looked at the other surface.**
*Evidence:* `PANEL_TEXT_RELATIONS`, a closed six-value enum; 772/1002 entries typed. The validator's own
comment dates the three failures that made it a field rather than a convention (2026-08-04 panel reversal,
2026-08-06 unmarked asterisk, 2026-08-10 dose-dependence turned threshold) and adds: *"In all three the
text was accurate and incomplete, which is the failure mode a text-only pipeline cannot see."*
*Why:* `surface` records where a quote came *from*; nothing else records whether the other surface was
opened.
*Standing:* **EXECUTABLY_ENFORCED** (introduced 2026-08-10, commit `da052c7`)
*Mechanizability:* **MECHANIZABLE** (the declaration) + **SCIENTIFIC_JUDGMENT** (the value)

**RULE-21 · A contradiction or qualification must point at the locator it overturns, and carry a needle.**
*Evidence:* `COUPLED_RELATIONS`; `contradicts` + `contradicts_needle` on 47/47; `qualifies` +
`qualifies_needle` on 32/32; `POINTER_RE = ^entries\[(\d+)\]$`.
*Why:* *"Without the pointer the claim is unfalsifiable prose sitting in a JSON field."*
*Standing:* **EXECUTABLY_ENFORCED**
*Mechanizability:* **MECHANIZABLE**

**RULE-22 · A panel contradicts a sentence only if it is the panel the sentence cites.**
*Evidence:* `cited_panel_check` (22 entries); `DL-METH-082`; two pairs on PMID 38182577 downgraded from
contradiction to qualification.
*Why:* Without it, every unrelated panel disagreement inflates into a contradiction against the paper.
*Standing:* PRACTICED · DOCUMENTED as a `DL-METH` lesson · **not enforced** (an optional field)
*Mechanizability:* **HYBRID**

**RULE-23 · "Incomplete is not false" — when no enum value is true, the defect is the enum.**
*Evidence:* the validator comment adding `panel_qualifies_text` on 2026-08-10, *"on SIX independent
instances across five papers, found by three actors who had not spoken"*, concluding: *"When no admitted
value is true, the defect is the enum. Forcing one would write a known falsehood into canonical state,
which outlasts any ordering of contracts."*
*Why:* Under a closed vocabulary, the pressure is always to pick the nearest wrong value.
*Standing:* PRACTICED · **EXECUTABLY_ENFORCED** as a consequence (the value now exists)
*Mechanizability:* **SCIENTIFIC_JUDGMENT**

**RULE-24 · Failure to recover supplementary material is recorded as a limitation with a named route and a named cost.**
*Evidence:* supplementary coverage 23 read / 27 not_read / 20 unavailable / 35 not_present across 128
receipts; PMID 20530675 (*Supplemental Table 8 holds the refutation*); PMID 32581702 (*"Chi la ottiene
riapra `entries[13]` per primo"*); PMID 39952983 (*the statistical support for the paper's central claim*);
and the closing case, PMID 42422765 S8 recovered and overturning the prior conclusion.
*Why:* A supplement holding the refutation of a main-figure title is not an appendix.
*Standing:* PRACTICED · **EXECUTABLY_ENFORCED** in part (`supplementary` is a required coverage axis with
a closed vocabulary)
*Mechanizability:* **HYBRID**

**RULE-25 · Capture the verbatim locator while the source is open; a waiver is an argument, silence is not.**
*Evidence:* rule 5b — *"On 2026-08-04 an export found that no verbatim locator existed anywhere in the
canonical state, across every complete read in the ledger; fourteen had to be recovered by reopening
papers already read. Capturing costs seconds, recovering costs the reading twice"*; `MIN_SNIPPET_CHARS = 30`;
`MIN_WAIVER_CHARS = 40` (*"A waiver must be an argument, not a shrug. Short strings like 'n/a' or 'not
relevant' are how a checklist dies"*); PMID 34214506, the sole zero-entry manifest, declaring the debt.
*Why:* Reconstructed locators are the reading paid for twice, at lower fidelity.
*Standing:* **EXECUTABLY_ENFORCED**
*Mechanizability:* **MECHANIZABLE** (existence, length, waiver substance) — contemporaneity itself is not.

**RULE-26 · A receipt proves a document was read. It does not prove which sentence supports which statement.**
*Evidence:* rule 5b's opening 🔴; three distinct tools for three distinct questions —
`fulltext_receipts.py verify` (chain), `locator_audit.py` (does the quote exist), `legend-locator-audit`
(does the quote support the proposition, blind); the 2026-08-10 audit of PMID 32000863 finding **5 of 22
locators absent from their own XML**, *"transcribed as the page reads rather than extracted as the artifact
contains."*
*Why:* These are three separate failure surfaces and only the first was ever instrumented.
*Standing:* DOCUMENTED · **EXECUTABLY_ENFORCED** for the first two · the third is a blind human/agent
judgement by design
*Mechanizability:* **HYBRID**

**RULE-27 · A page adjudication is published as a recipe, never as the image.**
*Evidence:* rule 5e; 3 adjudicated articles; `regenerate_adjudications.py write|verify`; PMID 16061658's
*"9 artifacts regenerate to their declared digest, 10 locators resolve to a span inside the crop that
shows them"*; two machine-checked conditions (`crop_contains_span`, digest regeneration) and two defects
they caught — a crop missing its own span by 1.2 points, and four needles that were not unique because
they wrapped across a line.
*Why:* The property that makes a crop evidence is the property that makes it someone else's to
redistribute. *"33 of 51 local PDFs will eventually need adjudicating, so this is a standing policy."*
*Standing:* DOCUMENTED · **EXECUTABLY_ENFORCED** · PRACTICED at n = 3
*Mechanizability:* **MECHANIZABLE**

**RULE-28 · A needle is drawn from characters that are identical in both surfaces.**
*Evidence:* PMID 16061658 — *"A needle containing `µ` would simply fail to resolve — but a needle taken
from the corrupted rendering would resolve successfully, to a string the author never wrote."*
*Why:* The silent false positive that wears the badge of having been checked.
*Standing:* PRACTICED at n = 1 · DOCUMENTED locally in that README
*Mechanizability:* **HYBRID**

**RULE-29 · A tool states the scope of its own verdict, so a PASS cannot be over-read.**
*Evidence:* `VERDICT: PASS … verification scope: STRUCTURE ONLY: local artifact existence, SHA-256 and
exact text locators NOT VERIFIED`; `VERIFICATION_SCOPE_DISCLOSURE_GATE` in the registry;
`caption_census.py`'s *"The predicate is printed, not implied. Two counts that do not name their
definition are not in disagreement — they are not yet comparable."*
*Why:* This analysis relied on it in §0.4 to avoid reporting 64/64 as more than it is.
*Standing:* **EXECUTABLY_ENFORCED** (the string is emitted) · PRACTICED
*Mechanizability:* **MECHANIZABLE**

**RULE-30 · Epistemic type is decomposed per component of a claim, not applied to the claim.**
*Evidence:* 20 of 39 canonical claims carry a composite or qualified `Type`; `epistemic_discipline.md` §1 vocabulary
`DATO | INFERENZA | IPOTESI | ESPANSIONE`; `Status` as a separate axis.
*Why:* A claim that is a measurement plus a transfer is not one epistemic object, and tagging it as one
launders the transfer.
*Standing:* PRACTICED · DOCUMENTED (the vocabulary) · **not enforced** at the composite level
*Mechanizability:* **HYBRID**

**RULE-31 · Every rejection names its load-bearing premise, tags it, and declares what would revive it.**
*Evidence:* `PREMISE: DATO | INFERENZA | DEFAULT_FROM_TEXTBOOK` (16 tagged: 10 of them
`DEFAULT_FROM_TEXTBOOK`); 11 `REVIVAL_TRIGGER`s; 3 of 12 active rejections already reopened or reversed;
*"The most dangerous premises are the ones too obvious to write down."*
*Why:* *"the false positive is a cost; the false negative is a compounding loss."*
*Standing:* PRACTICED · DOCUMENTED · **not enforced**
*Mechanizability:* **HYBRID** — presence of the two fields is mechanical; recognising an unstated premise is not.

**RULE-32 · The move from co-occurrence to causation passes a named gate.**
*Evidence:* `MECHANISM_DIRECTNESS_GATE`, `TARGET_ATTRIBUTION_GATE`, `DEGRADATION_DIRECTION_GATE`,
`CAUSAL_AXIS_GATE`, `MECHANISM_TRANSFER_FIREWALL`, `PROTEIN_STATE_IDENTITY_GATE`,
`REPORTER_IDENTITY_GATE`, `ASSAY_SEMANTICS_GATE`, `CONTROL_SPECIFICITY_RULE`, `STIMULUS_CONDITIONAL_RESCUE_GATE`
— each with the required representation it demands.
*Why:* Each gate is a recorded error, not a synthetic checklist item.
*Standing:* DOCUMENTED · PRACTICED · **20 of 79 gates executable; the causal ones are not among them.**
*Mechanizability:* **SCIENTIFIC_JUDGMENT** — the gate can be *required*; its answer cannot be computed.

**RULE-33 · Brainstorming is permitted, quarantined by file, typed, and promotable only through a commit candidate.**
*Evidence:* discovery ledger (3 320 lines) declared research-layer, append-only, *"Promozione a canonico
SOLO via COMMIT CANDIDATE"*; mandatory per-lead fields including `Esperimento proposto` (the falsifier),
`Belief`, `Evidenza: supporta / refuta / neutrale`, `Statement causale`; lead status vocabulary; 16 commit
candidates that propose and never edit; *"Batch gate: intentionally untouched."*
*Why:* Creativity is preserved and its outputs cannot be mistaken for evidence, because they are in a
different file with a different type and a mandatory falsifier.
*Standing:* PRACTICED · DOCUMENTED · **EXECUTABLY_ENFORCED** at the boundary (`BLOCK_BATCH_COMMIT`;
the four canonical files change only through `BATCH_COMMIT`)
*Mechanizability:* **MECHANIZABLE** (the boundary) + **SCIENTIFIC_JUDGMENT** (the typing)

**RULE-34 · Mechanical self-evaluation runs before written takeaways, and does not score quality.**
*Evidence:* `session_self_eval.py` (*"deliberately does not try to score analytical quality"*), built after
a 2026-07-26 receipt named four ledger entries that did not exist; 22 session evaluations structured as
*Content diagnosis* / *Process diagnosis* / *Residual debt*; `CLAUDE.md` ordering it before takeaways.
*Why:* Takeaways written first describe a session that went well.
*Standing:* PRACTICED · DOCUMENTED · **EXECUTABLY_ENFORCED** (the mechanical half)
*Mechanizability:* **HYBRID**

---

## PART 3 — Failure-derived practices

These are the practices that exist because LEGEND got something wrong first. For each: what failed, how
it was detected, what emerged. The `🩸 DEFAULTS THAT BIT US` table (**16 rows, D-01…D-16**) and the
`DL-METH` lessons (**12 distinct ids**) are the corpus's own version of this section; the entries below
are drawn from across all surfaces.

**F-1 · No verbatim locator existed anywhere (2026-08-04).**
*Failed:* an external export found that not one complete read in the ledger carried a locator binding a
statement to a sentence. *Detected:* by the export, i.e. from outside. *Emerged:* rule 5b; the
`verbatim_locators` block, now required in **64/64** manifests and carrying **1 002** entries; fourteen
readings reopened to recover what capture would have cost seconds. **The single largest practice in the
corpus is a repair.**

**F-2 · A figure panel reversed a conclusion the text did not contain (2026-08-04); an unmarked asterisk
was the difference between "not significant" and "not tested" (2026-08-06); a "dose-dependent" continuum
was a threshold (2026-08-10, Fig 3B of PMID 42422765).**
*Detected:* by opening the images. *Emerged:* `panel_text_relation` as a **required enum field**
(2026-08-10, `da052c7`) — *"a locator now says whether anyone looked at the other surface."* Yield to
date: **47 contradictions and 32 qualifications across 31 of 64 papers.**

**F-3 · A caption asserted a negative that its own image does not contain (`D-14`).**
*Failed:* Wang 2012 (PMID 22193544) — both the supplementary legend and the main text describe a panel as
the co-IP proving *"WWOX does not associate with Tau"*. *Detected:* by inspecting the image, which
contains **no Tau blot at all** and shows a faint *positive* band. *Emerged:* *"a negative asserted by a
figure must be verified in the figure IMAGE, never on caption authority — and this is strictly stronger
than reading the text, because here text and caption agreed with each other and both were wrong."*
Corollary: `figures: read` in a receipt must mean *images inspected*, hence the `captions_only` value
(currently 14/128 receipts).

**F-4 · Four parsers returned plausible small integers instead of errors, in one session.**
*Failed:* 27 where the count is 32; 7→9→6 on one article; a silent `or 1` fallback; 17 where there are 69.
*Detected:* by counting the printed letters by hand and disagreeing with the tool. *Emerged:* RULE-14 —
derive the denominator by **reading the captions**; and the diagnosis, written into PMID 32581702's manifest:
*"a fallback that cannot report 'I found nothing' is the same defect… Four instances in one session, four
different tools."* PMID 18487609 adds the sharpest form: *"It has three loud refusals… **AND A LETTERING GAP
IS NOT AMONG THEM.** It is the same shape as the four silent-zero failures the counter was built to end: a
small plausible integer where an error belonged."*

**F-5 · A coverage number was written from intention rather than measurement.**
*Failed:* PMID 31543760 declared 23/23 having opened three figures. *Detected:* self-caught, in the act —
*"it is the one field in this manifest that describes MY work rather than the paper's, and it is the one I
filled in from intention instead of measurement — which is the same gesture I spent the last two readings
documenting in other people's abstracts."* *Emerged:* the correction to 17/23 with four named waivers, and
the formula *"MEASURED, NOT INTENDED"*, reused explicitly on the next paper an hour later.

**F-6 · Non-open-access was used as a dispensation from looking.**
*Failed:* PMID 22634283 — all nine figures waived on OA grounds. *Detected:* **the operator refused the
reasoning.** *Emerged:* *"NON-OPEN-ACCESS IS A CONSTRAINT ON REDISTRIBUTION, NOT A DISPENSATION FROM VISUAL
INSPECTION"* — images held locally, gitignored, hash and recipe recorded, bytes never committed. Cost of the
waiver, stated: *"two panel findings that the text does not contain."*

**F-7 · A PDF text layer was well-formed and declared the wrong thing.**
*Failed:* PMID 16061658 — 25 corruptions, 23 printable (92%); `µg` read as `Ag` sixteen times; `p73β` as
`p73h` seven times. *Detected:* suspicion by absence — zero typographic operators across 44 465 characters
in a paper that says "significan" six times. *Emerged:* rule 5d; `_refuse_suspect_surface`;
`font_encoding_verdict()` — *"Nineteen fonts, all embedded subsets, all declaring `WinAnsiEncoding` and not
one carrying a `ToUnicode` map. The PDF is not damaged: it is well formed and declares the wrong thing. That
is why comparing extractors detects nothing"*; and page adjudication (rule 5e) as the fallback surface.

**F-8 · A receipt was immutable, hash-chained, tail-anchored and wrong (2026-07-26).**
*Failed:* it declared four ledger entries that did not exist, in an ID scheme the repository does not use.
*Detected:* nothing detected it at the time — that is the finding. *Emerged:* `session_self_eval.py`,
which compares what a receipt claims to have produced against what exists, plus the `LANDING_FILES`
definition that deliberately excludes generated views *"so counting them would let a paper 'land' in a file
that merely reflects the ledger it failed to reach."*

**F-9 · A shell heredoc silently ate a field of an append-only receipt (`D-16`).**
*Failed:* an unquoted `<<JSON` enabled backtick substitution; `` `references` `` was executed and deleted.
*Detected:* by eye, later — *"The receipt validated and chained — the JSON stayed well-formed, so no check
could see it."* *Emerged:* *"never construct append-only-ledger content through an unquoted heredoc"*, and
the general form: **validity is not fidelity.**

**F-10 · A citation range was read as an attribution map (`D-15`).**
*Failed:* a review wrote *"…on different, with some overlapping, tau residues [75, 76]"*; the claim was
attributed to ref 76, which measures **one site only** and never addresses site selectivity. *Detected:* by
reading the primary in full — *"one cycle late: the misattribution had already been written to a ledger."*
*Emerged:* *"A bracketed citation range is not an attribution map — resolve the primary before propagating
any clause of it."*

**F-11 · Five canonical surfaces credited a mouse paper with a phenotype it never measured.**
*Failed:* PMID 19936220 credited with *epileptogenesis*; it has no EEG, no seizure, no behaviour, no brain
histology — its only brain measurement is organ weight. Worse, the terminal source (PMID 19500159) states in
three places that Wwox-null mice show **no** epilepsy. And a third: PMID 19500159's own *abstract* says
"decreased concentrations of plasma growth hormone" unqualified while its **body** reports the difference as
not significant. *Detected:* by an **inbound** audit — asking not "what does this paper say" but "does it say
the thing we credit it with." *Emerged:* `IMPORTED_PREMISE_ATTRIBUTION_GATE` with five verdicts
(`CONFIRMED_FIRST_HAND` · `ABSENT` · `PASSED_THROUGH` · `CONTRADICTED` · `SOURCE_ABSTRACT_OVERSTATES`), and
the observation that makes it hard: *"a true clause next to a false one is the camouflage."* The gate's own
note on why nothing existing caught it: *"the unread-premise ratchet asks whether a citation was read, and
all three citations were fully readable and would have 'cleared' on being opened."*

**F-12 · A supplement recovered late overturned a conclusion already in canon.**
*Failed:* the shorthand *"P0–P5 fully rescues"* for PMID 42422765. *Detected:* by recovering Supplementary
Figure S8 through the proof-of-work route after five ordinary routes had failed. *Emerged:* the correction
isolated in `CC-20260810-42422765-S8` rather than edited in place; `pmc_pow_fetch.py` as a reproducible route
that fails closed; and the honest statement of what survives — *"What fails is uniformity and boundary
mapping, not evidence of a P5 effect."*

**F-13 · A ranking script refused to download the lowest class (`D-05`), and the tool built to find unread
gold filtered by tier (`D-06`).**
*Emerged:* *"Implementation wins, silently"*, and *"the tool built for a problem is not immune to that
problem — `--all` was not 'all'."* Cost recorded: *"A paper unreadable for months."*

**F-14 · Locators were transcribed as the page reads rather than extracted as the artifact contains.**
*Failed:* PMID 32000863 — 5 of 22 locators did not occur in its own XML; superscripts lost spacing,
cross-references lost their figure number, citation markers vanished. *Detected:* by `locator_audit.py`, built
for the legacy manifests the strict validator cannot reach. *Emerged:* *"A locator captured by transcription
is not a locator captured from the artifact, and nothing sees the difference until something matches exactly."*
Two of the five *lost information* — which figure a result points at, and which references support which clause.

**F-15 · Reference lists leak into the body surface, and the diagnosis was corrected twice in one day.**
*Failed:* on a review, 122 of 122 reference titles were verbatim in what the extractor returns as `body` —
*"roughly a THIRD of what a locator would be verified against is other people's titles, and a review's
reference titles are precisely statements about WWOX biology."* The first diagnosis blamed the Europe PMC
route; PMID 42082822 separated the two — the `<ref-list>` sits **outside** `<body>` there and its content is
*still* in the surface, so **the contamination is a property of the extractor, not of the route.** *Detected:*
by re-checking rather than assuming, on a third artifact. *Emerged:* `caption_census.py`, the whole-title probe
with its stated limitation (on one artifact *"ZERO `<ref>` elements carry an `<article-title>` longer than 45
characters. So this artifact CANNOT be tested by the whole-title method, and I am recording that rather than
producing a number from the short-slice probe that was shown unreliable two readings ago"*), and a corpus-wide
audit: 7 XML artifacts with a ref-list, 82 body locators, **zero inside one**.

**F-16 · A negative was asserted from a term count on a refused surface — and correctly withdrawn.**
*Evidence:* PMID 16061658 README — *"`ITCH` appears nowhere in this article. That statement has been made
before in this corpus and was correctly withdrawn, because it came from a term count on the refused text
layer — and a zero drawn from a surface that mangles sixteen printable characters is not an absence, it is
`NOT_FOUND_IN_TRIAGE`."* *Emerged:* the one route by which an absence may be asserted — read off the figure at
vector resolution, on the diagram where the authors state which partners they claim — and the consequence
written as **scope, not result**: *"this article… is **not** the primary evidence for any WWOX–ITCH claim."*
This is also rule 4 (*grep is forbidden as a method of analysis*) demonstrated on itself.

---

## PART 4 — Formalization gaps

Labels local to this analysis.

### ALREADY ADEQUATELY FORMALIZED
*Written, binding, and mechanically checked.*

- Verbatim locator capture, snippet minimum, waiver substance (RULE-25)
- Locator surface vocabulary and per-entry artifact binding (RULE-25/26)
- `panel_text_relation` enum and pointer/needle coupling (RULE-20, RULE-21)
- SUSPECT-surface refusal, printable-substitution screen, font encoding verdict (RULE-12)
- Receipt contract: coverage map vocabulary, `complete` forbidding `not_read`, hash chain, tail anchor (RULE-16)
- Re-read requiring a declared reason; parallel-read union (RULE-04, RULE-05)
- Queue identifier resolvability (RULE-03)
- Page adjudication as a recipe: `crop_contains_span` + digest regeneration (RULE-27)
- Group assessment, field density, multihop, corpus cross-query, retraction check as **required manifest
  sections** — the six `SECTIONS`, present in 64/64
- The promotion boundary: readings propose, `BATCH_COMMIT` disposes (RULE-33)
- Verification-scope disclosure (RULE-29)

### FORMALIZED BUT NOT ENFORCED
*Binding prose; no validator refuses a violation.*

- **Rule 5d's surface preference.** *"Prefer XML/HTML PMC over the PDF, always, and record the absence"* is
  binding text. `surface_preflight` — the field that would record the discharge — appears in **9 of 64**
  manifests, and `deepdive_manifest.py` does not know the key exists. The PDF *refusal* is enforced by
  suffix; the *preference and its recording* are not.
- **The causal gates.** `learned_gates_registry.md`: **20 of 79 executable, 55 method-only, 2 pending, 1
  proposed, 1 superseded.** Every gate governing the observation→mechanism move
  (`MECHANISM_DIRECTNESS_GATE`, `TARGET_ATTRIBUTION_GATE`, `DEGRADATION_DIRECTION_GATE`, `CAUSAL_AXIS_GATE`,
  `MECHANISM_TRANSFER_FIREWALL`) is `ACTIVE_METHOD`.
- **`PREMISE_TAG` and `REVIVAL_TRIGGER`.** Declared as *"two new obligations"*; 16 premise tags and 11
  triggers exist; nothing refuses a rejection that carries neither.
- **Rule 6, reading debt.** *"explicit and must be honored"* — the debt is counted (338 of 426), but no gate
  refuses a reading that opens debt without naming it.

### PRACTICED BUT NOT FORMALIZED
*Visible repeatedly in real work; no binding rule names it.*

- **The reading budget / denominator (RULE-14).** 12/64 manifests, four documented parser failures behind it,
  the most self-corrected field in the corpus — and it appears in **no** normative file and in **no** validator.
  This is the largest gap the analysis found.
- **Panels-inspected vs panels-intended (RULE-15).** The correction exists twice in writing; the obligation
  does not.
- **Resolution measured before rendering (RULE-19, partial).** `figure_ppi_preflight.py` exists and its output
  is quoted inside anchors across many manifests; nothing requires a preflight before a figure locator is
  written.
- **`cited_panel_check` (RULE-22).** Practiced on 22 entries, taught in `DL-METH-082`, optional everywhere.
- **`found_or_sought` (RULE-18).** 229 entries across 14 papers; undocumented.
- **Composite epistemic typing (RULE-30).** 23 of 39 claims do it; `epistemic_discipline.md` defines the four
  types but not the decomposition.
- **Group weighting as an independence judgement (RULE-09, second half).** The `weighting` string is required;
  what it must *say* — synthesis vs replication, same-group dependence — is convention.

### PARTIALLY CAPTURED
- **Supplementary-gap declaration (RULE-24).** The coverage axis is enforced; the practice of naming *what the
  missing supplement would have decided* and *which locator to reopen first* is convention on top of it.
- **The blind locator audit (RULE-26).** Fully specified as a skill with a strict blinding contract; step 5 of
  the acceptance test in a **PROPOSED** protocol; no evidence in this corpus of a completed blind audit run —
  the mechanical half (`locator_audit.py`) has run, the judgement half has not, in what I can measure.
- **Observation freeze (RULE-17).** Executed once, in exemplary detail, on 1 of 64 papers.

### OBSERVED ONLY LOCALLY
- **Needle-character discipline (RULE-28)** — one README.
- **The schema limit that `qualifies` cannot express on an adjudicated article.** PMID 16061658: *"rule 5e
  makes every locator on an adjudicated article a page crop with `surface: "figure"`. The text/panel distinction
  the relation depends on collapses exactly where page adjudication applies."* Recorded in prose, passed to Plan,
  and the same collapse is **unremarked** on the only other fully adjudicated article (PMID 17803050: 32 entries,
  all `surface: figure`, no cross-entry relation).
- **The one key the schema could not carry**, emitted as
  `🔴 relation_to_entries_8_stated_in_prose_because_the_schema_cannot_carry_it`.

### UNCLEAR
- **Dossier structure.** No template is enforced and none is dominant: `Verdict` 25/33, `Coverage map` 12/33,
  `Process report` 9/33, `Horizontal impact` 7/33, explicit `DATO`/`INFERENZA`/`IPOTESI` headings 5–6/33.
  Whether the variation tracks paper type or reader preference cannot be settled from this evidence, and
  distinguishing the two is exactly what the A/B/C comparison is for.
- **`retraction_check`.** Required and present 64/64; `checked: true` in 25/64. Whether the remaining 39
  represent a different legitimate value or unrecorded checks is not determinable from the field alone.
- **Whether the reading modes (`PRIMARY_EVIDENCE_READ` / `INDEPENDENT_CRITICAL_READ`) describe existing
  practice or propose a new one.** The critical axes of MODE B §5.2 name vocabulary that already exists and is
  populated (`panel_qualifies_text`, `text_contradicted_by_panel`) — so at least that axis is a formalization of
  practice. The other ten axes have no equivalent structured field in the 64 manifests.

---

## PART 5 — Candidate areas for a future Scientist Contract

**Subject areas only. No normative language, no causal-graph contract, no drafting.**

### 5.1 The central measurement

> **Which parts of high-quality Scientist work are protected by executable machinery, and which depend on the
> Scientist remembering how to think?**

Three independent measurements, all pointing the same way:

| Measurement | Protected by machinery | Depends on memory |
|---|---:|---:|
| Learned gates by status (79 rows) | **20** executable | **55** method-only (+2 pending, +1 proposed) |
| Manifest sections at 64/64 vs practices at <20/64 | **11** universal keys | `reading_budget` 12/64 · `surface_preflight` 9/64 · `figure_extractions` 6/64 |
| Locator fields | `proposition`/`snippet`/`anchor` 1002/1002; `surface`/`artifact` 969; `panel_text_relation` 772 | `cited_panel_check` 22 · `found_or_sought` 229 |

**Roughly one quarter of the recorded method is executable.** And the division is not arbitrary — the
machinery has consistently captured *the existence and shape of a record*, while every judgement about
*whether the evidence supports the statement* has remained with the reader. That division looks correct and
should be preserved, not closed.

The contract's job is therefore not to automate the other three quarters. It is to make the **question**
mandatory where the **answer** cannot be computed — the pattern `deepdive_manifest.py` already uses when it
requires a `weighting` string it cannot evaluate and a waiver of at least 40 characters it cannot judge.

### 5.2 The one structural observation about the current contract

`roles/scientist.md` is `status: PROPOSED — binding once Mirror hostile review passes and the operator
approves`. Its *Working discipline* section compresses everything measured in this document —
1 002 locators, 128 receipts, 79 gates, 16 recorded defaults, four surface rules — into **one paragraph of
pointers**. `framework/protocols/scientist_reading_modes.md` is also `PROPOSED` and *"binds nobody"*.

So: **the most developed part of LEGEND's practice is currently the least contractually bound part of it.**

### 5.3 Subject areas that deserve formalization

Ordered by the gap between how much the practice is worth and how little binds it.

1. **The reading denominator.** Declaring figures / panels / tables / supplementary elements before reading,
   with the derivation method stated. (RULE-14 · PRACTICED 12/64 · formalized nowhere · four documented tool
   failures behind it.)
2. **Inspected versus intended.** Coverage reported as what was looked at, with named waivers carrying their
   cost. (RULE-15, RULE-16.)
3. **The figure surface as primary evidence.** Images not text extraction; resolution measured before
   rendering; caption authority insufficient for a negative. (RULE-19, F-3, F-14.)
4. **Text/panel adjudication.** Including the `cited_panel_check` precondition and the "incomplete is not
   false" principle that produced `panel_qualifies_text`. (RULE-20 → RULE-23.)
5. **Surface preflight as a recorded act.** Which surface, which route, what the sentinel said, what the
   absence of a structured deposit implies. (RULE-11, RULE-12 · binding prose, 9/64 recorded.)
6. **Acquisition cascade and route exhaustion.** Including the rule that non-OA constrains redistribution and
   not inspection, and that a failed route is named rather than converted into a coverage hole. (RULE-13, F-6.)
7. **Supplementary material.** When its absence is a declared limitation, what the declaration must name, and
   which locator it reopens. (RULE-24, F-12.)
8. **The receipt/locator distinction, and the blind audit.** Three questions, three instruments; and the
   observation that the third has a specification and, in what I could measure, no completed run. (RULE-26.)
9. **Premise tagging and revival triggers on every negative.** Currently the most consequential unenforced
   obligation in the corpus, by its own analysis of the asymmetry. (RULE-31.)
10. **Inbound premise attribution.** "Does this source say the thing we credit it with" as a distinct
    obligation from "what does this source say", with its five verdicts. (F-11 · the gate exists; nothing
    triggers it.)
11. **Composite epistemic typing.** Typing the components of a claim rather than the claim. (RULE-30.)
12. **The observation freeze.** Whether a neutral, timestamped first pass held apart from the interpretive
    prompt should be required, for which classes of reading. (RULE-17 · n = 1.)
13. **Group provenance as an independence weighting.** What the `weighting` string must address —
    same-group dependence, synthesis vs replication, field density. (RULE-09.)
14. **Worktree/state declaration before measurement.** Which tree, which ref, how stale, which validator
    version. (RULE-01 · the failure that opened this task.)
15. **Scope disclosure on a verdict.** That a PASS carries the boundary of what it verified. (RULE-29 · already
    executable; worth binding so it cannot be dropped.)

### 5.4 The line the contract should not cross

These stay judgement, and the contract can require that they be *asked and answered in writing* without
pretending to compute the answer:

- Does the panel the sentence cites support the sentence's causal reading?
- Is an apparent rescue genotype-specific, or does it move the wild type too?
- Does an alternative explanation of the same data remain viable?
- Is this the terminal source of the premise, or a pass-through?
- Is a negative an absence in the evidence, or an absence in the surface I read?
- Which unstated premise is this rejection resting on?
- Is this finding a property of the paper, or of my extractor?

Every one of these has a worked instance in the corpus, and not one is decidable by a validator.

---

## Provenance of this analysis

| | |
|---|---|
| Worktree · branch | `.claude/worktrees/mirror` · `mirror` |
| HEAD analysed | `c7e8d6e` (merge of `main`@`788c357` into `mirror`@`2767333`) |
| Stale at start | 65 commits behind `main`; resolved by merge before any substantive reading |
| Tracked files | 683 |
| Evidence corpus | `disease-models/` tree `9ef1a09a7204bcfb3cb765cf041ff79039e6fdf5` — identical across merge-base, `main` and `mirror` |
| Gates re-run here | `legend_lint` PASS · `growth_anchors check` PASS · `fulltext_receipts verify` OK (128 chained) · `deepdive_manifest` 64/64 PASS **structure-only** |
| Not verifiable here | Artifact digests and exact quote matching — `files/` is gitignored and exists only in the shared checkout (§0.4) |
| Normative files read | **after** the archaeology, per §3 of the assignment |
| Peer outputs | none for this task exist on any ref; `lettore-b` artifacts recorded by name and **not opened** (§0.5) |
| Canonical files modified | **none** |
