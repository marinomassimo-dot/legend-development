# COMMIT CANDIDATE — `UPSTREAM_CITATION_FAILURE`: the null-mouse seizure fact is real and almost never cited to a measurement

**Candidate ID:** CC-20260826-UPSTREAM-CITATION-FAILURE-01
**Date:** 2026-08-26
**Status:** queued; **no canonical file modified**
**Mode:** quantification of locator→claim failures **in the primary literature's own citation
chains**, which LEGEND inherits
**Relation:** distinct class from
[`PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION`](PROPOSAL-20260826-LOCATOR-TO-CLAIM-PROPAGATION.md),
which measures the gap between *LEGEND's own* captured evidence and *LEGEND's own* claims. This
measures the gap **upstream of LEGEND entirely**.
**Change class:** MINOR (annotations) + one capability proposal
**Target WM:** current at BATCH_COMMIT time
**Batch gate:** intentionally untouched

---

## 1. The finding

While reconciling the mouse-seizure contradiction
([`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md)) it became
clear that **both sides of that contradiction are partly citation-laundered.**

The negative side was already known: `CLAIM 037` and `CLAIM 005` rest on Suzuki 2009, a
**literature survey** over four papers none of which recorded EEG.

🔴 **The positive side turns out to have the same defect.** Three independent groups assert that
`Wwox`-null mice have seizures. **Of the eight citations they offer, one is a primary measurement
of that fact in that animal.**

---

## 2. The three chains, verified against the artifacts

### Chain A — Obeid 2026 (PMID 42422765, `PAPER 011`)

> *"Based on our previous studies demonstrating that both Wwox-null and neuron-specific Wwox KO
> mice exhibit pronounced epileptiform activity,**⁴³** we sought to directly assess whether HD
> WWOX gene therapy modulates early network hyperexcitability."*

**Reference 43 resolves to:** Steinberg D.J., Aqeilan R.I., *WWOX-related neurodevelopmental
disorders: Models and future perspectives*, **Cells** 2021;10:3082 — **PMID 34831305 =
[[paper_registry_current#PAPER 063]]**.

🔴 **LEGEND's own record for PAPER 063 reads: `review narrativa / atlante di modelli — nessuna
coorte sperimentale nuova`.** A narrative review with no new experimental cohort is the sole
citation offered for prior electrographic evidence in the null.

| Citations | Primary measurement of the asserted fact in the asserted animal |
|---|---|
| 1 | **0** |

⚠️ **The irony is load-bearing, not decorative:** Obeid 2026's Figure 7 may well be the **first**
primary continuous-ECoG measurement in a `Wwox`-null mouse — and the paper frames it as
*confirmation of prior work*, sourced to a review. Framing a first measurement as a replication
is how a field acquires a fact nobody ever established.

### Chain B — Repudi 2021, *EMBO Mol Med* (PMID 34747138, source of `CLAIM 004`)

> *"We and others have previously reported that Wwox‐null mutants display spontaneous recurrent
> seizures (Suzuki et al, 2009; Mallaret et al, 2014; Cheng et al, 2020; Repudi et al, 2021)."*

| Citation | What it is | Supports the sentence? |
|---|---|---|
| Suzuki 2009 (PMID 19500159) | rat `lde/lde`; **states three times, plus an empty Table 2 `Epilepsy` row, that Wwox-null MICE show no epilepsy** (LEGEND read `FTR-20260806-19500159-01`) | 🔴 **asserts the opposite** |
| Mallaret 2014 (*Brain* 137:411) | **human** SCAR12 patients | ✗ wrong species |
| Cheng 2020 (PMID 32000863, `PAPER 019`) | *"In our generated Wwox−/− mice, spontaneous epileptic seizures were commonly observed after postnatal day 12"* | ✅ **yes** |
| Repudi 2021 (*Brain*, PMID 33914858) | `Nes-Cre` / `Syn-Cre` **conditional** KO | ✗ not the null |

| Citations | Primary measurement of the asserted fact in the asserted animal |
|---|---|
| 4 | **1** |

🔴 **One citation asserts the negation of the sentence it is cited to support.** That is not a
loose citation; it is an inverted one.

### Chain C — Hussain 2023 (PMID 36828035, `PAPER 007`)

> *"Like WOREE children, Wwox-KO mice displayed spontaneous seizures, motor deficits, ultimately
> reaching almost total immobility, and a short lifespan (~3 weeks) (Mallaret, 2014; Aldaz et al.,
> 2014; Ludes-Meyers, 2009)."*

| Citation | Resolved | Supports? |
|---|---|---|
| Mallaret 2014 | *Brain* 137:411 — **human** patients | ✗ |
| Aldaz CM, Ferguson BW, Abba MC 2014 | *Biochim Biophys Acta* 1846(1):188 — *"WWOX at the crossroads of cancer, metabolic syndrome related traits and CNS pathologies"* — **review** | ✗ |
| Ludes-Meyers 2009 | *PLoS One* 4(11):e7775 (PMID 19936220) — 🔴 per LEGEND's complete read, **no seizure measurement of any kind; the only brain measurement is organ weight** | ✗ |

| Citations | Primary measurement of the asserted fact in the asserted animal |
|---|---|
| 3 | **0** |

⚠️ Cheng 2020 — the one genuine source — **is** cited by Hussain 2023, but in the *following*
sentence and subordinated: *"Studies by others … substantiated our original observations."* The
measurement is demoted to corroboration of an assertion it is in fact the only evidence for.

---

## 3. Quantification

| | Count |
|---|---|
| Independent groups asserting null-mouse seizures | **3** (Aqeilan/Jerusalem, Hsu/NCKU, Aldaz/MD Anderson) |
| Assertions examined | **3** |
| Citations offered in support | **8** |
| Citations that are a primary measurement of the asserted fact in the asserted animal | **1** (Cheng 2020, cited once of three possible times) |
| Citations that assert the **opposite** of the sentence they support | **1** (Suzuki 2009 in Chain B) |
| Citations that are reviews | **2** (PAPER 063; Aldaz 2014 BBA) |
| Citations to the wrong species | **2** (Mallaret 2014, twice) |
| Citations to a different genotype | **1** (Repudi 2021 *Brain*, conditional not null) |

**Denominator note:** the population is *the citations attached to three specific sentences that
I read in full*, not "all WWOX citations". It is a census of three chains, not an estimate over a
corpus. The figure **1 of 8** is a property of those three sentences and must not be reported as
a rate for the field.

🔴 **The fact is nonetheless true.** Cheng 2020 measured it; Obeid 2026 measured an electrographic
correlate; Hussain 2023 measured a stronger version in a different genotype. **This candidate does
not weaken the conclusion of
[`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md).** It
establishes that the *field's* support for it is thinner than its unanimity suggests — which is a
different and more useful thing to know.

---

## 4. `PAPER 063` is now implicated twice

The registry **already** caught PAPER 063 distorting a primary finding. `CLAIM 016`'s evidence
boundary records that the review *"trasmette la lettura genotipo-specifica che il pannello del
primario non sostiene — una sintesi che stringe ciò che la fonte aveva lasciato largo"*: it
narrowed Cheng 2020's lithium result to a genotype-specific rescue the panel does not support.

Now the same review is the **sole** citation behind Obeid 2026's premise that prior work
demonstrated epileptiform activity in the null.

🔴 **Two distinct distortions, one review, opposite directions** — once narrowing a finding, once
manufacturing one. **Proposed:** annotate `PAPER 063` with a standing caution that it is a
transmission node with two recorded distortions, and that claims sourced through it require the
primary.

---

## 5. Proposed canonical effect

1. **`PAPER 011` annotation (MINOR).** Record that Obeid 2026's framing of its Figure 7 as
   confirmatory rests on `PAPER 063`, a review with no new cohort, and that the ECoG dataset is
   plausibly the **first** of its kind in the null rather than a replication.
2. **`PAPER 019` annotation (MINOR).** Record that Cheng 2020 is the **only** primary source for
   spontaneous behavioural seizures in a `Wwox`-null mouse, and that its own observation is
   opportunistic husbandry plus one video — **a floor, not a rate**. It carries more weight than
   its citation count suggests and less certainty than its unanimity suggests.
3. **`PAPER 063` annotation (MINOR).** §4 above.
4. **`CLAIM 037` / `CLAIM 005`** — no additional change beyond
   [`CC-20260826-SEIZURE-RECONCILIATION-01`](CC-20260826-SEIZURE-RECONCILIATION-01.md); this
   candidate strengthens the case for Δ2's `NOT_REPORTED ≠ ABSENT` record by showing the positive
   side was propagated the same way as the negative one.

---

## 6. Capability proposal — `UPSTREAM_CITATION_FAILURE`

A cheap, high-yield check that LEGEND is uniquely positioned to run, because it already holds
complete reads of the cited papers.

**When a full text is read, for each load-bearing assertion that cites prior work:** resolve the
citation to a PMID; if that PMID is **already in LEGEND with a complete read**, ask whether the
cited paper contains the asserted fact. Three outcomes: `SUPPORTED`, `NOT_CONTAINED`,
🔴 `CONTRADICTED`.

This costs nothing extra — the reads already exist — and it caught an **inverted** citation on its
first application.

⚠️ **Bounded on purpose.** It can only adjudicate citations whose targets LEGEND has read in full
(currently ~15 papers), so it will resolve a small minority of citations and must **report the
denominator every time**: *"n of m citations resolvable"*. A check that silently skips what it
cannot reach reads as coverage it does not have — the failure mode this repository has paid for
repeatedly.

🔴 **It must not become an automatic distrust of reviews.** Reviews are legitimate context; the
defect is a review standing where a **primary measurement** is claimed. The discriminator is the
*asserted fact's* need for a primary, not the source type.

---

## 7. What this candidate does not claim

- **Not misconduct.** Compressed citation is normal scientific writing; the Discussion sections
  above are doing ordinary summary work. The defect is structural and invisible from inside any
  one paper.
- **Not that the null-mouse seizure phenotype is doubtful.** It is measured. See §3.
- **Not a verdict on Mallaret 2014, Aldaz 2014 BBA, or PAPER 063's overall quality.** ⚠️ **I have
  not read Mallaret 2014 or Aldaz 2014 BBA in full**; their classification here rests on title,
  journal and abstract-level identity. PAPER 063's classification is LEGEND's own registry record.
  Ludes-Meyers 2009 and Suzuki 2009 rest on LEGEND complete reads with receipts.

---

## Review required

None for queueing. §5's annotations are MINOR; §6 is a proposal, not an implementation.

---

## BATCH DISPOSITION — `BATCH_20260927_001` (2026-09-27, ACTOR_ID `scientist`), append-only

**Status:** PROPAGATED IN PART

§5.1–§5.3 applied: the `Note` fields of `PAPER 011`, `PAPER 019` and `PAPER 063` carry the `UPSTREAM_CITATION_FAILURE` annotations in this candidate's own wording, with its §7 self-limits preserved — no verdict is written anywhere on Mallaret 2014 or on Aldaz 2014 BBA, which this author had not read. Verified before editing: none of the three notes carried the annotation, and the same defect class is already canonical in `CLAIM 016`'s evidence boundary.

**Not propagated, so this candidate stays open:** §6, the `UPSTREAM_CITATION_FAILURE` capability proposal with its denominator rule, which is a harness item and is handed to Harness Engineering in this batch's report, not implemented as an edit.

---

## WAVE-2 READINESS (2026-09-27)

**context_policy declared:** `SYNTHESIS`. This adjudication integrates existing records — the three
`PAPER` notes, `CLAIM 016`'s evidence boundary and the shipped tooling — reached through
`registry_records.py get`, never by grepping a registry. No source was reopened: nothing here
turns on a fact inside a paper.

**Actor:** `scientist`, wave-2 package `provenance`.

### What I did

1. **Verified §5's three annotations first-hand in the live registry**, rather than from the
   candidate's own disposition. `PAPER 011` (PMID 42422765), `PAPER 019` (PMID 32000863) and
   `PAPER 063` (PMID 34831305) each carry an `UPSTREAM_CITATION_FAILURE` annotation in the
   candidate's own wording, propagated by `BATCH_20260927_001`; three occurrences, one per record,
   and no fourth anywhere in the file.
2. **Verified §6 as implemented, by running it**, not by reading its commit message.
   `framework/scripts/upstream_citation_census.py` exists at `8d6922b` and satisfies §6's three
   binding requirements:
   - it resolves a citation against complete reads held in this checkout and prints one row per
     citation with the receipt that makes it adjudicable;
   - it **reports the denominator every time**, which is §6's explicit condition — over
     `files/fulltext/PMID36828035_Hussain2023_PMC.xml` it printed *"DENOMINATOR: 18 of 61
     citation(s) resolvable against a complete read in this checkout (0 without a PMID). The other
     43 cannot be adjudicated here, and their absence from the tally is not evidence of
     support."*;
   - the verdict column is the **reader's** (`--adjudications`), so the tool never classifies a
     source by type and cannot become the automatic distrust of reviews §6 forbids.
3. **Checked what §6 does NOT do**, because that is where a capability proposal usually drifts: it
   writes nothing to any registry, asserts no `SUPPORTED`/`NOT_CONTAINED`/`CONTRADICTED` of its
   own, and an unadjudicated run prints `ADJUDICATED: 0 of 18` rather than an implied clean bill.

### Verdict — **CLOSE**, closing status **PROPAGATED**

Both halves of this candidate have landed, each in the layer that owns it.

| Part | Where it landed | Evidence |
|---|---|---|
| §5.1 `PAPER 011` Note | `paper_registry_current.md` | annotation present, `BATCH_20260927_001` |
| §5.2 `PAPER 019` Note | `paper_registry_current.md` | annotation present, same batch |
| §5.3 `PAPER 063` Note | `paper_registry_current.md` | annotation present, same batch |
| §6 the check itself | `framework/scripts/upstream_citation_census.py` at `8d6922b` | run this session over a JATS full text and over an explicit PMID list; denominator line reproduced above |
| §7 self-limits | preserved | no verdict on Mallaret 2014 or Aldaz 2014 BBA appears in any of the three notes |

Nothing is owed. The candidate is closed, not deferred, and the tool is the durable form of §6 —
a proposal that became a runnable check is the outcome §6 asked for, and the only thing a further
batch could add is verdicts, which are per-reading work and belong to the readings.

**Change class:** none remaining — no canonical edit is proposed by this section.
