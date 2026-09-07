# LEGEND Scientist Operating Practice — reconstruction v1

> **Non-canonical, DESCRIPTIVE.** This document does not propose a workflow. It reconstructs
> the one already visible in the artefacts: 49 deep-dive manifests, 813 verbatim locators, 106
> read receipts, 16 session self-evaluations, 21 dossiers, one observation freeze, and 69
> gates in the learned-gates registry (47 `ACTIVE_METHOD`, 18 `ACTIVE_EXECUTABLE`, 2
> `PENDING_EXECUTABLE`, 1 `PROPOSED`, 1 `SUPERSEDED`). Every practice below is cited to where
> it is visible.
>
> Companion and corrective to
> [`scientist_evidence_standard.md`](scientist_evidence_standard.md) — see §Part 3.5, which
> records five practices this reconstruction found that the standard, written a day earlier,
> did not carry.
>
> Public, disease-level, de-identified. Nothing here is medical advice.

**Status:** rev. 1 — Scientist A, branch `lettore`, 2026-08-25
**Method:** artefact archaeology. Where a practice is asserted, the artefact that shows it is
named. Where a practice is doctrine but not visible in the artefacts, it is marked as such.

---

# Part 1 — The current implicit Scientist workflow

The workflow has **eleven phases**. Phases 1–3 happen before a word of the paper is read, and
they are where the corpus has bought most of its reliability. The order is not decorative:
four of the eleven exist *because* doing them later produced a documented failure.

---

## Phase 0 — Duplicate-work gate: has this already been read?

Resolve PMID and DOI, then query the receipt ledger **before fetching anything**.

| Prior state | Action |
|---|---|
| `complete_fulltext_read` with adequate coverage | reuse the dossier; do not re-read |
| `partial_fulltext_read` | resume from the uncovered sections |
| any | a new complete read requires an explicit `reread_reason` |

Admissible `reread_reason` values are enumerated: new version or supplement, inadequate
earlier coverage, contradiction or retraction, a genuinely new question outside the earlier
coverage, adversarial re-analysis, operator request.

**How this shows up in practice.** `PMID 34747138` carried three prior receipts — one
`legacy_reconstruction` with `unknown_legacy` coverage in every section, plus two
contemporaneous partials — and the manifest's `corpus_crossquery` states the question it asked
the corpus before opening the paper: *"which local structured surfaces have a MEASURED reading
debt rather than a presumed one"*. Exactly one paper answered. **The reading was selected by a
query over the ledger, not by a person's sense of what mattered.**

---

## Phase 1 — Surface preflight: which artefact will be read, and does a better one exist?

**This is the first gesture, before opening anything.** It exists because rule 5d states a
preference (`XML/HTML over PDF`) without naming a moment, so the preference was checked after
the PDF was already open — which is to say, never.

**Three routes are queried, never one, and the disagreement between them is the datum:**

```
oa.fcgi      https://www.ncbi.nlm.nih.gov/pmc/utils/oa/oa.fcgi?id=<PMCID>
Europe PMC   https://www.ebi.ac.uk/europepmc/webservices/rest/<PMCID>/fullTextXML
efetch       https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pmc&id=<PMCID>
```

Measured on 2026-08-10: on `PMID 24308844`, `oa.fcgi` answered **non-OA**, Europe PMC answered
**404**, and `efetch` returned **174 KB of complete JATS**. Two sanctioned routes out of three
would have sent that paper to its PDF. Separately, five corpus records carry `inPMC: Y`
together with `isOpenAccess: N` — author manuscripts. **A structured surface existing and a
paper being open access are two different facts**, and any check reading only one conflates
them.

**Absence is recorded, not passed over in silence.** `PMID 16061658` records: *"Europe PMC:
pmcid null, inPMC N, isOpenAccess N. Unpaywall: is_oa false, oa_status closed,
has_repository_copy false. … No structured deposit exists anywhere, so rule 5d's first
consequence — prefer XML/HTML, and record the absence — is discharged by recording the
absence."* `PMID 17803050` has no DOI, no PMCID and no open deposit; **declaring that is what
makes it a different class of paper rather than a poor reading.**

**The text surface is then screened before it may carry a quote.** The sentinel looks for C0
control characters, printable substitutions, and **suspicion by absence** — statistical
language with none of `< > ≤ ≥ ± × −`. A `SUSPECT` surface is **refused, never cleaned**:
- `PMID 18487609` — PDF extracts 61,304 characters with **126 C0 controls** and zero
  occurrences of any comparison or Greek glyph, while using *"significan"* throughout. Refused
  as a text surface, used only for figures. The PMC HTML was used instead: sentinel clean.
- `PMID 25012504` — the PDF was screened **per font before any text was taken from it**: 24
  fonts, **20 without a ToUnicode map**, including the symbol faces. That is the signature that
  made `PMID 18487609` suspect *while passing a file-level check*.
- `PMID 22634283` — a thermodynamics paper: 293 sentinel characters including `±` 112 times,
  `−` 97, `Δ` 39, `Å` 8. *"Every one of those characters is load-bearing — an errors column, a
  sign on an enthalpy, an ångström. A corrupted surface would have destroyed the numbers this
  reading is for."*

**Why first and not second.** A manifest built against the wrong surface **does not look
wrong**. On `PMID 24550385` a defective extractor produced `2` occurrences of `PPXY` instead of
`31` and **zero** figure citations instead of `32`. A reader on that surface does not fail —
they *select the quotes the defect lets through*, fitting the evidence to the tool. It is rule
5c inverted, and it is invisible from inside.

**Coverage today: 10 of 49 manifests carry an explicit `surface_preflight` block.** The
practice is recent and real, not yet universal.

---

## Phase 2 — Reading budget: declare the denominator before reading

`coverage.figures: read` with not one figure locator does not hold. It is the easiest box to
tick and the hardest to contest afterwards, because **nothing in the record says how many
figures there were.**

So before reading, the Scientist counts and writes down: `figures_present`, `panels_present`,
`tables_present`, `supplementary_elements_present` — then, after reading, `panels_inspected`
and `panel_coverage`.

Three properties make this work, all learned the hard way:

**(a) The denominator is panels, not figures.** *Panels covered over panels present*. A
`figures per paper` ratio measures what was read **divided by what that reader decided to look
at** — a measurement of oneself.

**(b) The count comes from reading the captions, never from a parser.** On `PMID 24550385`
three successive ad-hoc scripts returned 7, then 9, then 6 panels for a paper that has **39** —
each time a matcher failed and returned a *plausible small number* instead of an error. On
`PMID 23370280` the census refused all six figures because the deposit uses **lowercase panel
letters**; the refusal was correct and its cause stayed undiagnosed until the captions were
read. On `PMID 26675548` the census reports 10 against a true 16 because it silently drops
panel A of every figure. **The parser's number is a lower bound and never a denominator.**

**(c) It is measured, not intended.** `PMID 31543760` records the failure verbatim:
*"THE FIRST NUMBER I WROTE HERE WAS 23 AND IT WAS FALSE. I declared 23/23 before inspecting 23
panels. At the moment of writing I had opened three figures. The budget is the one field in
this manifest that describes MY work rather than the paper's, and it is the one I filled in
from intention instead of measurement."* Corrected to `17/23` with the four waived figures
named.

**Coverage today: 15 of 49 manifests declare a `reading_budget`. Where both terms are
integers, aggregate panel coverage is 310 / 354 = 88%.** The gaps are declared, not hidden:
`PMID 30356099` records `0/26` with the reason — *no figure image exists on disk*, the deposit
is XML-only, so the figures are covered at `captions_only`.

---

## Phase 3 — Group and field context, before the science

Executed as step 0 of the deep dive, and recorded as measured counts rather than reputation:

- `group_assessment` — `total_publications`, `publications_on_gene`, and the exact query that
  measured them. `PMID 34747138`: *"PubMed esearch 2026-08-10: 'Aqeilan RI[au]' 137, 'Aqeilan
  RI[au] AND WWOX' 65"* — 47% of the group's output is on the gene, and the manifest says so
  with the query attached.
- `field_density` — is the paper WWOX-directed, and how densely.
- `retraction_check` — route, date, result, and a `hold` boolean. `PUBLICATION_INTEGRITY_HOLD`
  blocks a `BATCH_COMMIT` if a canonical claim links a held paper.
- `multihop` — every reference enumerated, gene-directed ones identified, each resolved against
  the registries or queued as debt. `PMID 34747138`: *"All 62 `<ref>` elements parsed from the
  JATS; 36 mention WWOX/Wwox/WOREE/FRA16D … 36 of 36 known — this paper adds no unknown
  gene-directed reference, the first time that has happened in this corpus."*

**Context sets priority and ambition. It never sets truth.** The clearest instance runs the
other way: `PMID 34831305` is a review from *the* primary laboratory for both gene and disease,
and the reading found it transmitting a genotype-specific reading of the lithium result **that
the primary's own panel does not support**. Authority raised the paper's priority and did not
protect its claim.

---

## Phase 4 — The neutral vertical pass

**Two passes, in a fixed order, and the order is the point.**

1. **Vertical, neutral** — the paper in itself, epistemically tagged and anchored, *without yet
   looking at LEGEND's state*. This avoids contamination: reading a paper with the model in
   mind finds the model.
2. **Horizontal** — only afterwards: dedup, claim/meta/working-model impact, wikilinks,
   tensions.

The neutral pass has a physical artefact. `pattern_audits/PMID34831305_observation_freeze.md`
records a timestamp, the reading order (*"XML body sequentially, Table 1, disclosures, 224
references, Figure 1 pixels, Figure 2 pixels"*), twelve numbered observations, and the line
*"Pattern prompt deliberately withheld until after this record."* **The freeze is what makes
the neutral pass checkable rather than asserted.** One such file exists.

Within the pass, the reading is sequential and complete. `grep`, `rg` and find-in-page are
**forbidden as a method of analysis** — permitted only for locating files, deduplicating
registries, verifying IDs, and post-reading audit. Extraction is preparation, not reading:
*extract-then-read, never extract-then-skim.*

Two structural checks run here that a summariser would never run:

- **Page-count reconciliation before coverage.** The page count from `file`, from PDF metadata,
  from a viewer and from a landing page are not evidence of coverage. Open the document with
  **the same parser used for the sequential reading**, record `len(document)`, reconcile any
  divergence, and never take the largest or most convenient number.
- **Reference-list position, checked per artefact and not assumed.** `PMID 30158849`: the
  `<ref-list>` sits outside `<body>`, correctly filed, *and its content is in the body surface
  anyway* — 122 of 127 reference titles verbatim present. `PMID 42082822` re-checked and
  **overturned the reader's own diagnosis from earlier the same day.** A locator quoting a
  reference title would verify against the body and be wrong about where it came from.

---

## Phase 5 — Figures: opened as images, at declared resolution

**Figures are a separate surface and are never read through a text conversion.** Two documented
reversals justify the rule: on 2026-08-04 a figure panel reversed a conclusion the running text
did not contain, and on 2026-08-06 an unmarked asterisk was the difference between *"not
significant"* and *"not tested"*.

**Retrieval cascade, in order, with three traps that have all been hit in production:**

1. OA package service (`oa.fcgi`). `idIsNotOpenAccess` → move on. But an announced `href` can
   still 404 — `PMC10770339`, CC BY and in the OA subset, on 2026-08-10. **An announcement is
   not a delivery.**
2. Europe PMC `/{PMCID}/supplementaryFiles` — returns a ZIP of figures *and* supplements. The
   route that worked when the other two refused.
3. Publisher CDN — full-resolution originals (~2000 px) where PMC serves a display copy.

- 🔴 **The extension declared in the XML can be wrong.** `PMID 38182577` declares
  `Fig1_HTML.jpg`; the CDN serves `.png`, and requesting `.jpg` returns seven HTML error pages.
  Same publisher, same journal, `PMID 29724996`: genuinely `.jpg`. **Try the extension; do not
  deduce it.**
- 🔴 **Error pages save as figures.** Twice in one day a download loop produced seven files of
  identical size that were HTML, and that would have been fingerprinted and declared as
  figures. The mandatory check after any figure-set download —
  `md5 -q <dir>/*.png | sort -u | wc -l` must equal the figure count, and `file -b` must never
  say *HTML document* — is the cheapest control in the system and has already prevented two
  false readings.
- ⚠️ **The PMC copy is resized.** ~790 px is enough to see a panel and **not enough to read an
  asterisk or an axis label**. `PMID 34634460`: PMC serves 708–757 px, i.e. 101–108 effective
  ppi across a 7-inch page, against 209–279 ppi for the paper read an hour earlier — and the
  manifest records that at full-figure scale *the reader first misread which bar of panel 3D
  was which*. **The resolution read at goes into the locator's `anchor`, with native
  dimensions.**

**Not-open-access is not a dispensation from looking.** `PMID 22634283` records the correction:
*"I FIRST WAIVED ALL NINE FIGURES ON THE GROUND THAT THE ARTICLE IS NOT OPEN ACCESS. THE
OPERATOR REFUSED THAT REASONING AND IS RIGHT: NON-OPEN-ACCESS IS A CONSTRAINT ON
REDISTRIBUTION, NOT A DISPENSATION FROM VISUAL INSPECTION."* `PMID 25012504` records making the
same error again, knowingly, and closing it the same way. The images are held locally,
gitignored, hashed, with the recipe recorded and the bytes never committed.

**Where redistribution is genuinely at stake — an adjudication crop — the recipe is published,
never the image**: source-PDF digest, page, crop rectangle in PDF points, dpi, SHA-256 of the
image, regenerable by `regenerate_adjudications.py` from the reader's own copy.

**Coverage today: 42 of 49 manifests carry at least one figure locator; 268 of 813 locators sit
on a figure.** The seven without are enumerable and mostly explicable: two predate schema v2,
one is the locator-less legacy reading, one had no figure image on disk and said so.

---

## Phase 6 — Locator capture, while the document is open

Every statement the reading will carry out is recorded as `(proposition, snippet, anchor,
surface, artifact)` **at the moment it is read**, not reconstructed afterwards.

- `proposition` — what the quote is evidence **for**. *A quote with no proposition is
  decoration* (the validator's own words).
- `snippet` — verbatim, ≥ 30 characters, matched by the validator against the declared
  artifact, with the XML abstract separated from the body.
- `anchor` — section, figure or table, **plus the resolution for a figure**.
- `surface` — `body` / `figure` / `table` / `supplement`; **`abstract` may not carry
  evidentiary weight**.
- `artifact` — the fingerprinted file the quote was matched against.

**Why at capture time and not after:** on 2026-08-04 an external export found that **no
verbatim locator existed anywhere in the canonical state**, across every complete read in the
ledger. Fourteen had to be recovered by reopening papers already read. Capturing costs seconds;
recovering costs the reading twice. And forward-looking: an export cannot emit a proposition
without the sentence supporting it — **a reading done today without locators is a reading that
must be done again.**

**Waiving is legitimate; silence is not.** A reading that supports no proposition waives with
an argument of at least 40 characters, and the waiver appears as `[DECLARED GAP]` in
`session_self_eval.py`. One manifest of 49 carries a waiver, and it names its own cause:
the reading predates the requirement.

**Two optional fields that carry most of the discovery value:**

- `found_or_sought` — 272 of 813 locators. `found` means read in sequence; `sought` records
  **the question the reader went in with**. Examples from the corpus: *"I searched for WWOX as
  a substrate before concluding it never appears as one"*; *"a claimed absence is the thing to
  check"*; *"an unmarked panel is exactly the case where 'not significant' and 'not tested'
  look identical, and on 2026-08-06 that distinction cost this corpus a correction"*. **This
  field is what separates *no edge was looked for* from *an edge was looked for and is
  absent*.**
- `panel_text_relation` — 583 of 813, with the distribution given in §Part 3.

---

## Phase 7 — Adversarial passes: tension, hidden message, negatives

Three passes run *in addition to* extraction, each looking for something extraction does not
find.

**TENSION PASS (mandatory).** Beyond what the paper confirms, find actively what it
**challenges**: weakened claims, superseded framings, data in tension. *The tensions are often
the least obvious insight.*

**HIDDEN-MESSAGE EXTRACTION (mandatory).** The obligatory question: *"If this paper were read
by a very experienced researcher, what important message might they see that a standard reader
would miss?"* Targets: the unemphasised secondary message, the latent implication, **the
peripheral result that actually changes the model**, the methodological detail that raises or
lowers the paper's weight.

Worked instance — `PMID 19500159`. The headline was 95% audiogenic seizure penetrance. Three
things the standard reader loses:
- the 95% is a **female-only cohort**, stated in a figure caption and absent from both Results
  narrative and abstract;
- Figure 1's title assigns *normal* to panels (a, b) while the image shows it is (a, c) — **a
  caption-only reader inverts which hippocampus is diseased**;
- the protein's disappearance is attributed to the ubiquitin–proteasome system with **no
  turnover assay, no inhibitor, no route determination** — the identical textbook default
  falsified on 2026-07-12 for a different WWOX allele.

**NEGATIVE-EVIDENCE PASS.** The asymmetry is doctrine: *a false positive gets tested and dies;
a false negative is silent, permanent and self-reinforcing.* So the reading actively hunts
missing controls, alternative explanations, species differences and overinterpretation, and the
gate registry supplies the specific probes — `CONTROL_SPECIFICITY_RULE`,
`STAGE_MATCHED_COMPARATOR_GATE`, `STIMULUS_CONDITIONAL_RESCUE_GATE`,
`SYNTHETIC_REPLICATE_GATE`, `CROSS_LINE_REPLICATION_GATE`,
`DEVELOPMENTAL_TIMEPOINT_ATTRIBUTION_GATE`, `DENOMINATOR_FIRST_COHORT_GATE`.

Every rejection then enters the dismissal ledger with a **`REVIVAL_TRIGGER`**, and every new
mechanistic `DATO` **re-scans that ledger**. Without the re-scan there is self-correction, not
self-improvement.

---

## Phase 8 — Adjudicating figure against text

This is where the corpus's distinctive value is produced, and it has its own vocabulary:

| `panel_text_relation` | n | Meaning |
|---|---:|---|
| `text_only` | 344 | prose alone |
| `panel_only` | 90 | the finding exists **only** in an image |
| `text_confirmed_by_panel` | 81 | two-surface corroboration |
| **`text_contradicted_by_panel`** | **48** | the running text and the data disagree |
| `panel_qualifies_text` | 20 | the panel narrows the sentence |

Recording convention observed throughout: a contradiction is captured as a **pair** — a
`body`-surface locator quoting what the text says, and a `figure`-surface locator recording
what the panel shows — cross-referenced by `contradicts` / `contradicts_needle` (48 entries)
or `qualifies` / `qualifies_needle` (20). **Neither side is deleted.** The adjudication is
recorded; the paper's own sentence is preserved.

Worked instances across the categories that matter:

| Category | Paper | What the panel changed |
|---|---|---|
| **Pharmacological rescue** | `PMID 25012504` | Panel 5c shows digoxin lowering glucose **in wild-type mice**, which the text does not mention — and on a timescale incompatible with the transcriptional mechanism the experiment is offered for. A genotype-specific rescue becomes a drug that works in a model that has the phenotype. |
| **Genotype comparison** | `PMID 32000863` | Lithium suppressed PTZ seizures in **all three genotypes, wild type included** (Fig 7b, read from the image). The text states the converse for ethosuximide and *does not state it for lithium*. `CLAIM 016` now carries the boundary. |
| **Rescue completeness** | `PMID 34747138` | Where the rescue is compared to WT, either the bracket is not drawn (myelinated axons, CC1⁺, PDGFRα⁺ — all run WT-vs-KO and KO-vs-rescued) or it is significant **against** the rescue (unmyelinated axons ~26 in WT vs ~52 in treated, `**`). The g-ratio does normalise. **This is the difference between *improves* and *normalises*.** |
| **Blot / mutant** | `PMID 26675548` | The text says IR induced ubiquitination of wild-type WWOX *"but not the mutated form WWOX-K274R (line 5 vs. 6)"*. **The blot shows a clear band.** Reduced, not abolished. |
| **Fractionation** | `PMID 23370280` | GAPDH is present in all three nuclear lanes and lamin is visible in the cytoplasmic lanes: the separation is **partial, not exclusive** — which is what the word *exclusive* in the text requires. |
| **Direction of effect** | `PMID 18487609` | Panel 5A measures the in-vivo direction and it is **up, not down**: RUNX2 at 1.50 in femur against every other marker falling. And the Discussion's summarising sentence — the one shaped to be quoted — states the opposite sign for the same tissue. |
| **Magnitude** | `PMID 18487609` | Text says ~25%; the panel reads +50% femur, +39% calvaria. Direction right, number wrong — recorded separately, because they are separate errors. |
| **Statistics present at all** | `PMID 23370280` | Figure 6: four bar charts, error bars on three, **not one significance marker or p-value anywhere in the figure**. `PMID 15070730` Fig 3A: no error bars on twelve bars, and a **mislabelled y-axis**. |
| **Asterisk convention** | `PMID 34634460` | Figure 3's caption inverts the asterisk convention (`* p = 0.0036, ** p = 0.027`) while Figure 6 has it right — **inside one paper**. |
| **Caption swap** | `PMID 32300104` | Figure 1's caption swaps the plotted WWOX and WFPA colour identities. |
| **Panel-label collision** | `PMID 24550385` | The legend announces two spectra as panels *E and F*, then labels them *(C)* and *(D)* — letters already used. The **figure settles its own legend's collision**, which is stronger than the running text settling it. |
| **Selective reporting** | `PMID 29724996` | Four genes were never measured at 1 and 3 months, so for those four *"no change"* is **not a negative result — it is an untested condition**. |

**No electrophysiology paper in the corpus currently carries a figure locator.** `PMID 33255508`
(Breton 2021, the primary behind `CLAIM 021`) and `PMID 31340538` are among the seven manifests
with none. Given that `CLAIM 021` is `consolidated baseline` and its content is entirely
quantitative traces, **this is the sharpest coverage gap the reconstruction found.**

---

## Phase 9 — The three-voice separation

Practised consistently and named nowhere as a field.

| Layer | Example from the corpus |
|---|---|
| **A. Direct observation** | *"~26 unmyelinated axons per field in WT versus ~52 in treated, `**`"* — `PMID 34747138`, Fig, read from the image |
| **B. Author interpretation** | *"there are still some differences between rescued and WT mice which could be attributed to an oligodendrocyte-specific WWOX function"* — quoted verbatim, and explicitly labelled **the authors' `IPOTESI`** |
| **C. LEGEND interpretation** | *"non-cell-autonomous describes a **component**, not the whole phenomenon; an oligodendrocyte-autonomous WWOX function remains open and is not excluded. Not promotable without an Olig2/CNP-specific deletion or rescue."* — `CLAIM 003` |

The separation is enforced by wording, not by structure: *"the attribution of the residue to
oligodendrocytes is the authors' `IPOTESI`; the residual gap is `DATO`."* `PMID 31543760`
records the same discipline turned on the reader: *"the comparison with entry 8's domain
position is mine"* — an authored inference, tagged as authored, inside a locator.

---

## Phase 10 — From observation to mechanism

The move is governed by named gates rather than by judgement, and the gates are specific enough
to fire.

| Question | Gate | Rule |
|---|---|---|
| Does this transfer to another variant or model? | `MECHANISM_TRANSFER_FIREWALL` | attach variant/model, system, epistemic level; a transferred edge is a **bridge hypothesis** until measured in the target |
| Does the perturbation prove the pathway? | `CAUSAL_AXIS_GATE` | a perturbation is not proof of a whole pathway |
| Is the intermediate measured? | `MECHANISM_DIRECTNESS_GATE` | marker + phenotype ⇏ intermediate; **a surrogate is not the mechanism** |
| Does the rescue identify the target? | `TARGET_ATTRIBUTION_GATE` | a pharmacological rescue does not identify its target automatically |
| Does more protein mean more function? | `PROTEIN_STATE_IDENTITY_GATE` | abundance ≠ function; *"stable but inert"* is a demonstrated phenotype |
| Which way does the arrow point? | `DEGRADATION_DIRECTION_GATE` | name the direction; do not infer causality from co-occurrence |
| Do two papers really disagree? | `DIRECTIONAL_CONTEXT_GATE` | opposite directions may be context, not conflict |
| Is the comparison stage-matched? | `STAGE_MATCHED_COMPARATOR_GATE` | groups differing in genotype **and** stage confound both |
| Is the assay what its name says? | `ASSAY_SEMANTICS_GATE` / `REPORTER_IDENTITY_GATE` | the construct catalogue overrides the text's label |
| Is this really independent replication? | `EVIDENCE_REUSE_GATE` | a review, a reused cohort or a same-lineage publication is not a replication |

And above all: **every non-trivial conclusion, and every rejection, names its load-bearing
premise and tags it** `PREMISE: DATO` / `PREMISE: INFERENZA` / `PREMISE:
DEFAULT_FROM_TEXTBOOK`. A textbook default is not a foundation — **it is a research target**,
and a conclusion resting on one is provisional by construction.

**The canonical failure this prevents**, traced end to end on 2026-08-06: `CLAIM 005` attributed
epileptogenesis to `PMID 19936220`. That paper measures early death first-hand and **measures
epileptogenesis in no form** — no EEG, no seizure observation, no behaviour, no histology; the
only brain measurement is organ weight. Its own citation points to the **rat** `lde` model, and
that terminus states in three places, plus a Table 2 whose `Epilepsy` row is empty for both
mouse models, that **Wwox-null mice show no epilepsy**. Two citation hops turned an explicit
negative about a rat into a positive assertion about a mouse — and it read as verified because
**the co-cited premise in the same sentence was true**.

---

## Phase 11 — Post-reading: brainstorming, kept separate

Brainstorming is mandatory and never mixes with evidence. The separation is architectural, not
stylistic: each product lands in a **different file with a different epistemic status**.

| Product | Destination | Status |
|---|---|---|
| What the study demonstrates | commit candidate → claim registry | canonical, gated by `BATCH_COMMIT` |
| New questions, needle-leads | `discovery_ledger_current.md` | non-canonical, append-only |
| Therapeutic implications | `therapeutic_hypotheses_ledger_current.md` | non-canonical, scored, `BLOCK-1` gated |
| Rejections | `dismissal_ledger_current.md` | with `REVIVAL_TRIGGER` |
| Reading debt this created | `full_text_queue_current.md` | tracked, ratcheted |
| Method that worked or did not | `learned_gates_registry.md` | gate, with a status |
| How the reading itself went | `session_evaluations/` | **not evidence** — `SELF_ASSESSMENT_IS_NOT_EVIDENCE_GATE` |

Cross-domain expansion is mandatory (*tumour → metabolism, immunology → neuroinflammation, glia
→ excitability*) and bounded by one rule: **traceability back to `pathway → WWOX claim →
source paper`. If traceability is lost, the expansion is invalid.**

The self-evaluation runs **before** the takeaways, deliberately: *takeaways written first will
describe a session that went well.*

---

# Part 2 — Hidden rules

These are the rules that recur across artefacts and are **not stated as rules anywhere**. Each
is given as it is practised, with why and a case.

---

**Rule 1 — Query all routes; the disagreement is the datum.**
*Why it matters:* any single retrieval route both false-negatives and false-positives, and a
reader who queries one gets a confident wrong answer with no signal that it is wrong.
*Example:* `PMID 24308844` — `oa.fcgi` says non-OA, Europe PMC 404s, `efetch` returns 174 KB of
complete JATS.

**Rule 2 — Record absence as a result, in the same field where presence would go.**
*Why it matters:* an unrecorded absence is indistinguishable from a reading nobody bothered to
do, and the next reader repeats the whole cascade.
*Example:* `PMID 17803050` — no DOI, no PMCID, no open deposit, declared. That declaration is
what puts the paper in a different class rather than making it a poor reading.

**Rule 3 — Declare the denominator before you can know the numerator.**
*Why it matters:* a coverage figure chosen after the fact is chosen to be reachable. Fixing the
denominator first is the only thing that makes the ratio a measurement.
*Example:* `PMID 32581702` — *"fixed BEFORE reading so the budget could not be chosen to match
what was found."*

**Rule 4 — Count by reading, never by parsing; a parser's number is a lower bound.**
*Why it matters:* a failed matcher returns a plausible small number, not an error — and a
plausible small number is accepted.
*Example:* `PMID 24550385` — three scripts returned 7, 9 and 6 panels for a paper with 39.

**Rule 5 — Screen the surface before quoting it, and refuse rather than repair.**
*Why it matters:* cleaning a corrupted surface launders the defect into every quote drawn from
it, and the quotes then verify — against a document nobody wrote.
*Example:* `PMID 18487609` — 126 C0 controls and zero comparison glyphs in the PDF; the HTML was
used instead and the PDF kept only for figures.

**Rule 6 — Screen per font, not per file.**
*Why it matters:* a file-level check passes on a document whose symbol faces have no ToUnicode
map, which is exactly where signs and Greek letters die.
*Example:* `PMID 25012504` — 20 of 24 fonts unmapped, including the symbol faces.

**Rule 7 — Record the resolution you read at, in the anchor.**
*Why it matters:* the difference between reading an asterisk and guessing one is the difference
between *not significant* and *not tested*.
*Example:* `PMID 34634460` — 101–108 effective ppi; the reader misread which bar of panel 3D was
which at full-figure scale, and says so.

**Rule 8 — Verify a downloaded figure set is images.**
*Why it matters:* error pages save with an image extension, get fingerprinted, and become
"figures" in the record.
*Example:* two loops in one day produced seven identical-size HTML files. `md5 | sort -u | wc -l`
must equal the figure count; `file -b` must never say *HTML document*.

**Rule 9 — Not-open-access constrains redistribution, not inspection.**
*Why it matters:* the licence waiver is a tempting and wrong reason to skip the surface that
most often overturns the text.
*Example:* `PMID 22634283` — nine figures waived on this ground, refused by the operator, all
nine retrieved and inspected. `PMID 25012504` — the same error repeated knowingly, then closed.

**Rule 10 — Read the caption before the panel, and then read the panel against the caption.**
*Why it matters:* captions carry restrictions the narrative drops, and captions are also where
label errors live.
*Example:* `PMID 19500159` — the 95% figure is female-only, stated only in a caption; and
Figure 1's title inverts which hippocampus is normal.

**Rule 11 — Record both sides of a contradiction; never delete the losing one.**
*Why it matters:* the paper's own sentence is what downstream literature will quote, so the
correction is only useful if it is attached to the thing being corrected.
*Example:* 48 `text_contradicted_by_panel` locators, each paired to a body locator through
`contradicts_needle`.

**Rule 12 — An unmarked panel is *not tested*, not *not significant*.**
*Why it matters:* the two look identical on the page and mean opposite things.
*Example:* `PMID 29724996` — four genes never measured at 1 and 3 months, whose absence was
being read as a negative result.

**Rule 13 — Follow a citation to its terminus before believing it.**
*Why it matters:* an imported premise can invert across two hops while every individual sentence
stays true.
*Example:* the `CLAIM 005` chain — rat negative → mouse positive, in two hops.

**Rule 14 — Check what the paper says it does *not* know.**
*Why it matters:* on a self-citing review it is the most trustworthy category, and it is where
the open questions are already enumerated by someone who knows the field.
*Example:* recorded verbatim as a `found_or_sought` rationale in the corpus.

**Rule 15 — A claimed absence is the first thing to check.**
*Why it matters:* negatives close doors permanently, and a negative in a figure is the cheapest
thing in a paper to state and the most expensive to verify.
*Example:* `PMID 26675548` — *"but not the mutated form K274R"*; the blot shows a clear band.

**Rule 16 — Re-check your own diagnosis on the next artefact rather than generalising it.**
*Why it matters:* a property of one deposit gets promoted to a property of a route, and then
propagates.
*Example:* `PMID 42082822` — the `<ref-list>` position check *"overturns what I reported twice
today."*

**Rule 17 — Write the number you measured, not the number you intended.**
*Why it matters:* the one field describing the reader's own work is the one filled in from
intention.
*Example:* `PMID 31543760` — *"I declared 23/23 having opened three figures."* Corrected to
17/23 in place, with the waived figures named.

**Rule 18 — Record whether you found it or went looking for it.**
*Why it matters:* it is the only field that distinguishes *no edge was sought* from *an edge was
sought and is absent* — the difference between an open question and a completed negative.
*Example:* 272 of 813 locators; *"I searched for WWOX as a substrate before concluding it never
appears as one."*

**Rule 19 — Authority raises priority, never truth.**
*Why it matters:* the primary laboratory is where the best evidence is and also where the
strongest unchecked syntheses are.
*Example:* `PMID 34831305` — the field's primary review transmitting a genotype-specific reading
its own primary's panel does not support.

**Rule 20 — The reading's self-assessment is not evidence.**
*Why it matters:* a session reporting on itself is the one witness that cannot be
cross-examined.
*Example:* `SELF_ASSESSMENT_IS_NOT_EVIDENCE_GATE`, `ACTIVE_EXECUTABLE`; and the executable
verdict block that opens every `session_evaluations/` file, which reports tool exit codes rather
than impressions.

---

# Part 3 — Missing formalization

## 3.1 Already encoded — enforced by code and regression-tested

| Practice | Where |
|---|---|
| Receipt for every full text, hash-chained and tail-anchored | `fulltext_receipts.py`, `FULLTEXT_RECEIPT_PERSISTENCE_GATE` |
| Controlled `evidence_depth` (5 values) + section-level coverage | receipt schema |
| Work-manifest gate: group, field density, multihop, corpus cross-query, retraction | `deepdive_manifest.py` |
| Locator required, verbatim-matched against a fingerprinted artifact | `deepdive_manifest.py`, `EVIDENCE_SURFACE_BINDING_GATE` |
| Abstract may not carry evidentiary weight | schema v2 |
| Suspect-surface refusal (C0, printable substitutions, suspicion-by-absence) | `_refuse_suspect_surface` |
| Page-adjudication recipes that regenerate | `regenerate_adjudications.py` |
| Claim-status vocabulary, wikilink integrity, biomarker/endpoint separation | `legend_lint.py` |
| Reading debt ratchets | `growth_anchors.py` |
| Self-assessment is not evidence | `SELF_ASSESSMENT_IS_NOT_EVIDENCE_GATE` |

## 3.2 Partially encoded — doctrine exists, enforcement does not, or coverage is thin

| Practice | State |
|---|---|
| **Surface preflight, three routes** | doctrine in the deep-dive manual §4bis; `surface_preflight` present on **10 of 49** manifests; no validator requires it |
| **Reading budget / panel denominator** | doctrine in §4ter; `reading_budget` on **15 of 49**; the rule is deliberately *not* a threshold, so nothing can check it |
| **Figure inspection at declared resolution** | practised widely (**42 of 49** manifests carry ≥1 figure locator) but the resolution lives in free-text `anchor` |
| **`panel_text_relation`** | field exists and is optional; **583 of 813** locators carry it |
| **Two-pass neutral reading** | doctrine in §6.3.2; **one** observation-freeze artefact exists |
| **Tension pass, hidden-message extraction** | mandatory in doctrine; leaves no structured artefact of its own — visible only where it happened to produce a locator |
| **`found_or_sought`** | **272 of 813**; optional; free text |
| **Transferability on three axes** (genotype / model / stage) | mandatory in doctrine; present as prose in claim `Genotype/model relevance`, not as fields |

## 3.3 Not formally encoded — practised, nowhere required

| Practice | Evidence it happens |
|---|---|
| **Per-font ToUnicode screening** before taking text from a PDF | `PMID 25012504` only |
| **Reference-list position check per artefact** | `PMID 30158849`, `31543760`, `42082822` — and it overturned its own earlier finding |
| **Figure-download integrity check** (`md5 \| sort -u`, `file -b`) | in the manual as a command; no artefact records having run it |
| **Recording the reader's own inference inside a locator** (*"the comparison is mine"*) | `PMID 31543760`; ad hoc |
| **Panel-count method disclosure** (captions vs parser, and why the parser failed) | recorded in `reading_budget.method` on the 15 that have one; free text |
| **Correcting one's own field in place, with the wrong value preserved** | `PMID 31543760`, `22634283`, `25012504`; a convention, not a schema |
| **`next_decisive_experiment_or_decision`** | declared in `LEGEND_CORE.md:47`; **0 instances in 39 claims** |
| **`HUMAN_MODEL_MISMATCH`** as a controlled category | present only inside transferability prose |
| **Electrophysiology figure discipline** | no ephys paper in the corpus carries a figure locator |

## 3.4 The structural asymmetry

The system enforces **that a reading happened** and **that a quote is real** with executable
gates and mutation tests. It enforces almost nothing about **how well the paper was
interrogated** — and the interrogation is where the value is. Every practice in §3.3 was
invented by a reader mid-reading, works, and is one session away from being forgotten.

The registry itself shows the shape of the gap: of 69 gates, **18 are `ACTIVE_EXECUTABLE` and
47 are `ACTIVE_METHOD`** — enforced by nobody but the reader who remembers them. That ratio is
not a defect to be closed by making everything executable; several method gates are genuinely
matters of judgement. It *is* the reason a Scientist contract is worth writing: the 47 are
currently transmitted by whoever happens to read the registry.

## 3.5 What this reconstruction changes about `scientist_evidence_standard.md`

That document was written **a day before this one**, which is the wrong order: the contract was
drafted before the practice was surveyed. Five practices found here are absent from it, and
each is a field it should have had.

| Missing from the standard | Where practice already has it |
|---|---|
| Surface preflight, with the three routes and their disagreement | `surface_preflight` block |
| Reading budget — `figures_present`, `panels_present`, `panels_inspected`, and the **method** by which they were counted | `reading_budget` block |
| Reading resolution as a field, not free text inside `anchor` | practised, unstructured |
| An artefact proving the neutral pass preceded the model-aware pass | `pattern_audits/*_observation_freeze.md` |
| `found_or_sought` carried into the OBSERVATION layer | 272 locators |

The standard's `OBSERVATION` layer is still the right shape; it is incomplete, and the omission
is diagnostic — **a contract written from first principles under-specifies exactly the fields
that were learned by being wrong.**

---

# Part 4 — Proposed Scientist Contract topics

Areas that should become formal requirements. **Listed, not specified.**

**Acquisition and surface**
1. Surface preflight as a required, pre-reading, multi-route step with recorded disagreement.
2. Structured-surface preference, with absence declared as a first-class result.
3. Text-surface screening: file-level *and* per-font, with refusal rather than repair.
4. Artefact locality: which checkout the evidence must live in, and where validation counts.

**Coverage and its denominator**
5. Reading budget: declared before reading; panels as denominator; counting method disclosed.
6. Figure-set integrity verification after download.
7. Reading resolution as a structured field with native dimensions.
8. Page-count reconciliation through the reading parser.
9. Section coverage vocabulary, including `captions_only` and the conditions that force it.

**Evidence capture**
10. The observation layer: system, species, perturbation class, window, comparator, readout,
    method, direction, n, statistic, limitation. *(Specified in
    [`scientist_evidence_standard.md`](scientist_evidence_standard.md) §5.1; amend per §3.5.)*
11. `found_or_sought` promoted from optional prose to a required two-state field with rationale.
12. `panel_text_relation` required wherever a figure surface is used.
13. Contradiction pairing: body locator ↔ figure locator, both retained, adjudication recorded.
14. Authored-inference marking inside a locator (*"this comparison is mine"*).

**Interrogation**
15. Tension pass — with a required artefact, so that "performed" is checkable.
16. Hidden-message extraction — same requirement.
17. Negative-evidence pass, bound to the specific gates that apply to the study design.
18. Citation-terminus verification for any imported premise a reading will carry.
19. Neutral-pass freeze as a required artefact for model-shifting papers.

**Reasoning and typing**
20. Three-voice separation as a field, not a wording convention.
21. `PREMISE_TAG` on every non-trivial conclusion and every rejection.
22. Transferability on three declared axes: genotype, model, developmental stage.
23. Directness: `DIRECT` vs `INDIRECT_UNKNOWN_INTERMEDIATES`, defaulting to the weaker value.
24. `next_decisive_experiment_or_decision` — instantiated, not merely declared.
25. `HUMAN_MODEL_MISMATCH` as a controlled category.

**Ranking and context**
26. Two orthogonal axes — study type × recency — never collapsed; `FRONTIER` flagging.
27. Review discipline: corroborates, never creates `DATO`; its primaries enter the queue.
28. Independent-replication test that survives shared cohorts, lineages and reviews.
29. Group assessment as measured counts with the query attached.
30. Cross-domain parity: oncology, adult neurology and off-domain papers are read, and the
    traceability requirement that bounds the expansion.

**Closure**
31. Locator waiver: argued, never silent, surfaced as a declared gap.
32. Reading debt: what this reading created, tracked and ratcheted.
33. Destination discipline: which ledger each product lands in, and its epistemic status.
34. Self-evaluation before takeaways, with the executable verdict reported as exit codes.
35. Method log: which moves added value and which did not — the loop that lets the contract
    evolve empirically instead of by decree.
