# Batch self-evaluation — `scientist-c`, `AQEILAN-FT-C-001` wave 3, 2026-09-09

> Written **after** the executable gate returned its verdict and **before** capability scouting and
> takeaways. It also discharges the wave-2 self-evaluation obligation, which was not run because the
> orchestrator scoped that session to landing only.

## Scope and executable verdict

- **Batch:** `AQEILAN-FT-C-001` wave 3 of a 7-PMID lot. Mode `PRIMARY_EVIDENCE_READ`. Shared root
  checkout, branch `main`, three scientist actors concurrent.
- **Studies:**
  - `PMID 41562193` (Druck/Huebner 2026, *Genes Chromosomes Cancer*) → `FTR-20260909-41562193-01`,
    `complete_fulltext_read`, 27 locators.
  - `PMID 16223882` (Fabbri/Croce 2005, *PNAS*) → `FTR-20260909-16223882-01`,
    `complete_fulltext_read`, 26 locators, **12/12 page adjudications verified**.
  - `PMID 28373548` (the Editorial Expression of Concern) read in full as a **source in its own
    right**, before the article it concerns.
- **`session_self_eval.py`:** `PASS` — *every complete read has landed and every declared output
  resolves*. receipts 145 · complete_fulltext_events 76 · active_complete_reads 65 ·
  unread_premises **3/4** (ratchet **improved**).
- **Manifests:** both `PASS`, **0 gaps**, strict, run from the shared checkout.
- **`regenerate_adjudications.py verify`:** `OK — 12 of 12 declared digests matched, 12 of 12
  locators resolved to a span inside the crop that shows them, 12 of 12 against the snippet each
  names.`
- **Receipts:** `OK: 145 chained, tail anchored`. **LINT:** `PASS` after every commit.
- **Growth anchors:** `PASS`; two ratchets improved by these readings and re-anchored —
  registry-only full-text declarations **15 → 13**, unread premises **4 → 3**
  (`GA-20260909T144653Z-tighten`).

---

## Content diagnosis

| Dimension | Evidence-backed answer | Grade | Debt or correction |
|---|---|---|---|
| Sequential full-text, figures, tables, supplements | **4/4** figure surfaces on 41562193 (3 main + Supplementary Figure 1) and **7/7** on 16223882 (6 main + the EoC's replacement panel) read **as pixels**, every one extracted by xref from a fingerprinted PDF rather than taken from the archive's display JPEGs. Supplementary Table 1 parsed in full (86×86). No `captions_only` anywhere. | `strong` | none |
| Main message vs original contribution | 41562193: the contribution is the Fhit signature set; the WWOX conclusion in the title's orbit is an inference from co-deletion. 16223882: the contribution is the reagent and the xenograft result; the mechanism is asserted. | `strong` | none |
| Hidden gold beyond keywords/abstract | Both headline findings live **only in pixels**: SBS40c absent from every *Wwox* bar (11 columns inside the Fhit bracket, zero inside the Wwox bracket), and a **wild-type** MEF line carrying the highest mutation burden in the whole *Wwox* dataset. On the second paper, the absence of caspase-9/8 rows and the U2020 blot splice are likewise invisible to any text search. | `strong` | none |
| Source parity | Both read in full despite being oncology and `background_only`/T3 — the case rule 3 exists for. The 2005 paper was read *because* it is the reagent source, not despite being old. | `strong` | none |
| Group type, field density, observation vs interpretation | Counts **re-derived today** (Huebner 408/131 FHIT/32 WWOX; Aqeilan 137/65/14). 🔴 The wave-1 debt — stale 137/64 carried from 2026-08-11 — is **paid**: today's measurement is 137/65. Primary-for-gene vs primary-for-disease stated separately for both papers, and for 41562193 the fact that it is *not* the Aqeilan laboratory's paper is stated first. | `strong` | wave-1 debt closed |
| DATO / INFERENZA / IPOTESI / ESPANSIONE | Every carried statement typed. Both papers `ESPANSIONE`/T3. Two `PREMISE: DEFAULT_FROM_TEXTBOOK` tags with revival triggers (COSMIC v3.4 split; implausibility of `×10⁸` cell counts), each stated as a research target rather than a foundation. | `strong` | none |
| Claims touched; conflicts | **No consolidated baseline claim touched**, determined by enumerating all 18 and reading their titles, twice — once per paper, not inherited. `CLAIM 029` qualified at the phenotypic end and **explicitly not called a reversal**. `CLAIM 002`/`CLAIM 004` recorded as a deliberate **non-link**. | `strong` | none |
| Multi-hop and corpus cross-query | 36 and 26 references enumerated as integers. Six queue items opened (`FT-083`–`FT-088`). The corpus cross-query returned an **absence that matters**: 0 of 43 dossiers and 0 of 70 manifests touch the mutational-signature axis. | `strong` | none |

---

## Persistence diagnosis

- Manifests, dossiers, commit candidates `CC-20260909-41562193-01` and `CC-20260909-16223882-01`,
  `DL-METH-110`, queue items `FT-083`–`FT-088`, and a full adjudication recipe set. Nothing in
  `staging/`. Receipts through the validated writer only; the ledger JSONL was never hand-edited.
- `FT-076` — the Ad-WWOX reagent debt **this actor opened in wave 1** — is closed by wave 3.
- Both commits carried the state manifest, so the ledger tail anchor moved with the appends.

---

## Process and capability diagnosis

### 🔴 The failure that matters this wave, and I caught it by disbelieving a green result

I called `_refuse_suspect_surface(text, path_string)` — **arguments inverted**. It returned
normally. `path` is not touched before the loop, so the loop screened the *filename*, which holds
no control characters, and I read the silent return as CLEAN. The surface I was actually asking
about — the PMID 16223882 PDF text layer — carries **191 C0 controls and zero comparators**, and
the correct call refuses it.

**Nothing in the repository would have caught this.** I caught it only because I had separately
counted the raw characters, saw `<`, `±`, `×`, `β`, `μ` all at zero in a paper that prints `P <
0.05` and `β-actin`, and refused to believe a screen that called that clean. Had I trusted the
green, I would have declared a SUSPECT surface as `article_text` and anchored twelve text locators
to characters no author wrote — the exact false positive rule 5c calls the worst class this system
can produce, and it would have worn the badge of having been checked.

**It also means my earlier "supplement text: CLEAN" result for 41562193 was meaningless** when I
reported it — I had made the same inverted call. That paper is nonetheless sound, and not by luck:
the authoritative screen runs inside `deepdive_manifest.py` at write time, and the manifest passed
strict validation with the supplement TXT declared. Re-run correctly afterwards, it is genuinely
clean. The lesson is not "the surface was fine" but **"my check asserted nothing and I reported it
as though it had"**.

### Other failures, and what caught each

1. `_xml_surfaces` returned nothing for 41562193 — my regex was `<body>` and the deposit writes
   `<body id="…">`. Caught by the assertion failing, not by a wrong answer.
2. Figure 2 colour segmentation initially attributed 13 px of the **plot frame** to SBS46 in every
   column; and in Figure S1 I mistook the legend-box border `(213,213,213)` for the SBS46 swatch
   `(184,184,184)`. Both caught by *arithmetic disagreement* — the per-sample totals did not
   reconcile with the printed panel totals until the colours were right.
3. Figure S1 baseline set at y=1992 (the x-axis *labels*) instead of y=1574 (the axis). Caught
   because every bar came out at ~25 mutations, which contradicted the visual read.
4. Receipt refused: `first_read cannot name prior_receipt` **and** `prior_receipt is null and this
   study already has 1 receipt(s)`. Caught by the writer. See the contract findings below.
5. Receipt refused: `analysis_at cannot be later than event_at`. Caught by the writer. Same class as
   wave 1's — I keep stamping an optimistic clock.
6. Manifest refused twice: `gene_direct_refs_in_source: must be a list`; two snippets under 30
   characters. Caught by the validator.
7. Adjudication crops: five of twelve regenerated to different digests because I **rendered from
   the unrounded rect and stored the rounded one**; and eight needles were refused as non-unique
   because a needle wrapping a column break returns one rectangle per line. Caught by
   `regenerate_adjudications.py`, which is precisely what it is for.

**Attribution, honestly:** items 4, 5, 6 and 7 were caught by tooling, not by me. Items 1, 2 and 3
were caught by cross-checking one measurement against another. The one that mattered most — the
inverted screen — was caught by neither tool nor peer, but by disbelieving a verdict I had not
earned.

### The wave-2 self-criticism, checked against this wave

Wave 2's finding was that locator hygiene did not hold: reader identity and an external ledger
reference leaked into a pixel attestation, three Discussion quotes were mis-anchored by a paragraph,
and I asserted an error-bar property a panel did not have — four of them caught by the blind auditor
rather than by me. This wave:

- **Anchors were pinned mechanically**, not from memory: every 41562193 text locator was located to
  its enclosing `<sec>` by walking the XML, and I deliberately **stopped short of asserting
  paragraph numbers** I could not verify robustly. No anchor claims more precision than I checked.
- **No reader identity and no external reference appears in any attestation.** Attestations carry
  measured values, colours, coordinates and printed labels only.
- **Three places where I declined to assert a panel property**, which is the direct remedy for the
  error-bar failure: the Fig 1B duplication verdict (measured, verdict declined — the instrument
  cannot resolve it at 421×196); the Fig 3B lane-9 caspase band (stated as a *gradation and an
  ordering*, not as "caspase 3 is cleaved"); and Figure 5C (recorded as qualitative rather than read
  for tumour presence, because I could not measure it reliably).

That is the target met. It was met by writing the limit into the locator rather than by being more
careful, which is the only version that survives a bad session.

### Two contract findings, registered rather than worked around

1. 🔴 **First contact with the text after a `legacy_reconstruction` is unrepresentable under
   `first_read`.** The writer refuses `first_read` together with a `prior_receipt` (line 442) and
   refuses a null `prior_receipt` when the study already has an event (line 603). The dispatch and
   the protocol both say a prior `legacy_reconstruction` means `first_read`. I used
   `inadequate_prior_coverage`, which is admissible **and true** — nine `unknown_legacy` values are
   inadequate coverage by construction — and recorded the whole thing in `evidence_basis` and the
   dossier. Nothing false was written. This is the **second** gap of this shape I have hit in this
   contract, after wave 1's `identity_correction`.
2. 🔴 **When a paper's only surface is SUSPECT, the panel-relation vocabulary becomes
   unavailable.** Adjudicated text locators must declare `surface: figure`, and
   `TEXT_SURFACES = {body, table, supplement}`, so no adjudicated locator can be the target of
   `text_contradicted_by_panel` or `panel_qualifies_text`. On 16223882 I had **three** genuine
   coupled relations to declare — Figure 5A against "completely suppressed", Figure 3B against the
   U2020 specificity claim, Figure 3B's missing caspase rows against the intrinsic-pathway sentence
   — and could declare none of them. **The vocabulary is missing in exactly the papers whose surface
   is worst.** Each relation is stated in the locator's `note` and argued in the dossier instead.
   Reported, not improvised: the fix is a schema decision.

### Capability micro-upgrade shipped

`framework/scripts/test_suspect_surface_call_shape.py` (**9/9 PASS**) plus an **argument-shape
guard** in `_refuse_suspect_surface`: a non-`PathLike` first argument is refused, and so is a part
that is merely the artifact's own path or filename. Disease-agnostic; nothing in it mentions WWOX.

**Mutation-tested rather than asserted:** disabling the `PathLike` check turns exactly the two
inversion cases red and leaves the other seven green. Test 8 exists to stop the guard being deleted
later for the usual reason — a real document that *mentions* its own filename still passes, because
the guard compares the whole stripped part and never a substring.

**Why this and not something larger:** the upgrade is proportional to what actually went wrong. The
figure work went well and needed no tool; the screen returned a silent CLEAN on an unscreened
surface, and that is the failure whose next occurrence nobody would notice.

### Residual risk and next decisive action

1. The two contract findings above are **schema decisions and are the operator's**, not mine.
2. `text_surface_intrusion_check.py` (wave 1's upgrade) is **still not wired into any gate**. It ran
   clean on both of this wave's text surfaces, by hand. Wiring it into `deepdive_manifest.py` for
   PDF-derived surfaces remains the obvious next step and was again not done in the same change as
   an unrelated upgrade.
3. **`PAPER 007` carries `Identifier: pending normalization` while sourcing two consolidated
   baseline claims**, and `PMID 36828035` behind it has two partial receipts and no complete read.
   Queued as `FT-083`; not this actor's record to repair.

---

## The three failure modes the protocol warns about — checked against my own answers

- **Answering yes to everything:** the content table is mostly `strong`, and I have said so rather
  than manufacturing a `partial` — but the process section carries a failure I would rather not have
  written down, and it is the one thing in this document worth trusting.
- **Grading the outcome instead of the process:** the outcome was strong — a paper's own supplement
  contradicting its direction, an expression of concern read properly, rule 5e run end to end for
  the first time here. The **process** still inverted the arguments to a safety-critical screen and
  believed the result. Those are graded separately, and the second is why the micro-upgrade is what
  it is.
- **Writing the diagnosis myself and calling it evidence:** four of the seven enumerated failures
  were caught by tooling, not by me. The one that mattered was caught by cross-checking, not by
  care. Nothing here rests on my recollection of having been careful.
