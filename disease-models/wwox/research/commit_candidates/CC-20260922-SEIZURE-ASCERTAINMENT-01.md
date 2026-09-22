# COMMIT CANDIDATE — CC-20260922-SEIZURE-ASCERTAINMENT-01

**Source:** Scientist D, seizure-ascertainment census
([`seizure_ascertainment_census_20260922.md`](../../analysis/seizure_ascertainment_census_20260922.md)),
verified by the Orchestrator against local artefacts before landing.
**Relationship to prior art:** **extends** `CC-20260826-SEIZURE-RECONCILIATION-01` (MAJOR, queued
since 2026-08-26, unapplied, operator authorization required). **This candidate does not restate,
duplicate or compete with it, and does not attempt to settle what it settles.** It adds the two
things that candidate's *"missing decisive experiment"* section omits, and one method fact.
**Change class:** **MINOR** — two `PREMISE: NOBODY_LOOKED` tags and one experiment named. **No claim
reversed, no headline touched, no prohibition altered** — all of that is the 2026-08-26 candidate's,
and it is not mine to pre-empt.
**Status:** `PROPOSED — NOT PROPAGATED`.
**Review floor:** **R2** for what is proposed here. ⚠️ The claims it touches sit under an
**unresolved R4 decision**; this candidate is written so that it remains correct whichever way that
decision goes.
**Proposes:** `D-27` — *"an empty cell in a comparison table records that nobody looked, until
someone shows the row was measured."*

---

## 1 · 🔴 The decisive animal has existed since 2007 and has never been looked at

The field's standing explanation for the mouse/rat discordance is Suzuki's own: **the mice may die
before they can seize.** It is testable, and the test does not require a new animal.

`PMID 19500159` Table 2, as reconstructed in this repository's own full-text dossier
(`fulltext_dossiers/PMID19500159.md:169–177`):

| | `Wwox−/−` mouse | `Wwox^gt/gt` mouse | `lde/lde` rat |
|---|---|---|---|
| Expression | absence | **hypomorph** | functional loss |
| **Viability** | 2–3 weeks | 🔴 **2 years** | 3–12 weeks |
| **Epilepsy** | — | 🔴 **—** | wild running + tonic–clonic |

**`Wwox^gt/gt` (PMID 17823927) is viable to two years**, carries little or no detectable Wwox protein
in most tissues, and its `Epilepsy` cell is **empty**. Its published endpoints are B-cell lymphoma,
testicular atrophy and fertility. Per Scientist D's census it has **never been observed for
seizures, never given an EEG, never provoked, and never given any neurological endpoint at all**.

🎯 **So the survival-confound hypothesis is not an open question. It is an unattempted experiment on
an animal that has been available for nineteen years.** An animal that lives two years cannot "die
before it seizes"; if `Wwox^gt/gt` is seizure-free under provocation, the survival explanation is
dead and the discordance is biological. If it seizes, the mouse/rat discordance was an artefact of
lifespan all along.

⚠️ **Depth declared:** the viability and the empty cell are **full-text** (this repository's own
dossier of 19500159). *"Never observed for seizures"* rests on `17823927`'s **abstract and declared
endpoints** — its body is **not retrievable here** — so it is an inference from an absence of
declared neurological endpoints, **not** a Methods-level negative. It is strong enough to name an
experiment; it is not strong enough to assert as a measured fact, and this candidate does not.

---

## 2 · 🔴 No Wwox mouse of any allele has ever been audiogenically provoked

The rat headline that anchors `CLAIM 037` — 19/20, 95% — is a figure obtained **on audiogenic
stimulation**. The complete provocation inventory of the entire Wwox literature is:

| provocation | applied to | source |
|---|---|---|
| **audiogenic** | 🔴 **rat only** | `19500159` |
| pilocarpine + PTZ | mouse (the only mouse provocation ever performed) | `32000863` |
| **audiogenic, mouse** | 🔴 **never, in any allele, by any laboratory** | — |

**`PREMISE: NOBODY_LOOKED`.** The mouse and the rat have never been asked the same question, and the
comparison that grounds a canonical species contrast has therefore never been run.

Two facts make this first-order rather than pedantic:

**(a) It was seen happening and never measured.** Cheng 2020 (`PMID 32000863`, full text, CC BY),
verbatim — verified in `deepdive_manifests/PMID32000863.json`:

> *"Seizures were frequently induced by mild stressors including **noise**, strobe lights and novel
> cage during routine handling."*

A **reflex, sensory-evoked seizure in a Wwox-null mouse**, reported as husbandry: no stimulus
specification, no latency, no denominator, no controls. That laboratory then built a
**chemoconvulsant** protocol instead of an acoustic one. ⚠️ `n` for Cheng's seizure cohorts is **not
extractable** — the caption `n`-deletion defect of `FT-126` — and **must not be quoted**.

**(b) The semiology already matches.** The `P47T` knock-in's seizures are reported to begin *"with
wild running and jumping"* — which is the rat's audiogenic semiology, the same phrase Suzuki's
Table 2 uses. Nobody has applied the acoustic stimulus to either mouse.

### Proposed addition to `CLAIM 037`, evidence boundary

> ⚠️ **The species contrast has never been tested with the same stimulus.** The 95% figure is
> obtained **on audiogenic stimulation**; **no Wwox mouse of any allele has ever been audiogenically
> provoked** (`PREMISE: NOBODY_LOOKED`). The only provocation ever applied to a Wwox mouse is
> chemoconvulsant (pilocarpine/PTZ, `PMID 32000863`) — and that same paper reports seizures
> *"frequently induced by mild stressors including noise"* without measuring one. Separately,
> **`Wwox^gt/gt` — which survives where the null does not, `Epilepsy` row empty in the same Table 2 — has never been
> observed, recorded or provoked at all**, so the "dies before it can seize" explanation has an
> untouched test bed.

---

## 3 · The experiment, named

**Suzuki's own 2009 protocol, unmodified**, applied to the two animals it was never applied to:
three trials, latency scored per trial, littermate controls, **both sexes**, `Wwox−/−` at **P12–P18**
and `Wwox^gt/gt` in **adulthood**. It needs a sound chamber and colonies that already exist.

Using the original protocol unmodified is the point: a species comparison is only a comparison if
the stimulus is the same one.

⚠️ **Both sexes is not a formality.** The rat's 95% is **female-only**, declared solely in a figure
caption — and per the census, **sex is unreported for every mouse seizure measurement in the
literature except two**. A female-only headline compared against sex-unreported mouse data is a
systematic blind spot sitting underneath a canonical species claim.

---

## 4 · 🔵 A method fact worth keeping, because it invalidates a whole class of negative

Scientist D's census proves, **from inside itself**, that PubMed field queries under-detect this
endpoint: `36828035` performed bilateral video-EEG and `42422765` performed continuous ECoG, and
**neither appears in any of the EEG queries run** — because PubMed `[All Fields]` reads title,
abstract and MeSH, **not Methods**.

🔴 **Therefore: a query-count negative about a METHOD is not evidence that the method was not
performed.** Only a Methods-level read is. Every negative in the census rests on methods-level reads,
with counts as corroboration only — which is the correct construction, and is the reason the census
can assert its negatives at all.

Counts are recorded as corroboration with their controls, per the rule that a near-absence claim
carries its query: `Wwox` → **708**; `Wwox AND (EEG OR electroencephalography OR electrocorticography
OR electrocorticogram)` → **12**, of which **11 human and exactly 1 rodent** (the rat, `19500159`);
`Wwox AND audiogenic` → **2**; `Wwox AND (startle OR "sound-induced" OR "acoustic startle")` → **0**
against control `Fmr1 AND audiogenic` → **62**; `Wwox AND (PTZ OR pilocarpine OR kindling OR
kainate)` → **1** against control `Scn1a AND ("video-EEG" OR telemetry OR "spike-wave")` → **31**.
**The controls are what make the zeros readable**, and without them none of these counts would be
usable.

---

## 5 · What this candidate explicitly does NOT do

- ❌ **It does not touch `CLAIM 037`'s headline or `CLAIM 005`'s prohibition.** Both belong to
  `CC-20260826-SEIZURE-RECONCILIATION-01`, which is **MAJOR, states that it requires operator
  authorization, and has been queued unapplied for 27 days.** That candidate needs an operator
  decision, not a second candidate written across it. **Surfacing it is the action; pre-empting it
  would be the error.**
- ❌ **It does not promote Mallaret 2014.** Still `abstract-depth`, still paywalled, and now
  correctly ranked as the **weakest** evidence in the census rather than the pivot — see the
  append-only correction to `CC-20260922-CLAIM005-CHAIN-NAMING-01`.
- ❌ **It does not import `42397075`** (Steinberg 2026, *Brain*) into a rodent census. It is **human
  organoids**. Recorded because the mis-filing was specifically guarded against.
- ❌ **No gate, auditor, registry or workflow is proposed.** §26 boundary respected.

---

## 6 · Provenance and integrity

- **Verified by the Orchestrator, not accepted from the delegate.** The Cheng 2020 quotation was
  read in `deepdive_manifests/PMID32000863.json`; the Table 2 viability and empty `Epilepsy` cells
  in `fulltext_dossiers/PMID19500159.md:169–177`; the existence, status, date and MAJOR
  classification of the 2026-08-26 candidate in the file itself. **The delegate's central claim —
  that the contradiction was already found and its candidate is still queued — was the first thing
  checked, because it bore directly on a candidate I had written an hour earlier.** It held, and my
  candidate was corrected.
- **Depths declared per row**, `abstract-depth` never promoted, `not performed` kept distinct from
  `not reported` throughout the source census.
- **`UNREAD_PREMISE`: to be measured with `growth_anchors.py check` before this lands, not
  predicted.** The last time this candidate's author predicted that number, the ratchet returned
  `10`.


---

## 7 · 🔴 APPEND-ONLY — the *"2 years"* figure is WITHDRAWN from the proposed canonical text

**Operator instruction, 2026-09-22: do not propagate *"viable to 2 years"* until the Suzuki Table 2 /
abstract discrepancy is reconciled. It is not reconciled, so it is withdrawn here before propagation.**

| source | says | depth |
|---|---|---|
| **Suzuki 2009, Table 2 `Viability` row** | `gt/gt` = **2 years** | 🔴 **secondary**, `panel` depth — a table *about* another lab's mouse |
| **Ludes-Meyers 2007, the primary's own abstract** | *"We observed that the Wwox(gt/gt) mice had **a significantly shorter lifespan**"* | primary, `abstract-depth` — **the body serves `full_text: ""`** |

**Both are on file and neither is a read of the primary's body.** §1's table row and prose are
corrected to drop the number; **the proposed canonical addition no longer contains it.**

🔵 **The ARGUMENT survives intact, and on the primary's own words rather than on the disputed
number.** Ludes-Meyers 2007, verbatim: *"Remarkably, **Wwox hypomorphic mice are viable in contrast
to the recently reported postnatal lethality of Wwox knockout mice**."* That is the whole load the
argument needs: **`gt/gt` outlives the null, which dies at 3–4 weeks, by enough to make the
survival-confound question testable.** *"Significantly shorter than wild type"* and *"long enough to
seize"* are not in conflict — the null's ceiling is three to four **weeks**.

🔴 **And a second overstatement, this one already in CANONICAL text.** `claim_registry_current.md`
`CLAIM 032` states: *"il topo **ipomorfo** `Wwox^gt/gt` (**proteina bassa ma rilevabile**) è
**vitale**"*. The primary says *"**no detectable Wwox protein in most tissues examined**, although,
**a low level could be detected in a minority of tissues**"* — and **names no tissue, and not
brain**. *"Proteina bassa ma rilevabile"*, unqualified, generalises a minority-of-tissues finding to
the animal.

⚠️ **Not repaired here — it is outside this candidate's authorized scope** (the operator
authorization covered the seizure statements only), and
**`CC-20260921-CLAIM032-HYPOMORPH-PREMISE-01` already queues exactly this defect.** Recorded so the
two are visibly linked.

> **The only statement currently permitted about this animal's protein:** *low Wwox protein was
> reported in a minority of tissues; **residual brain protein is not established**.* And therefore:
> **`Wwox^gt/gt` must not be called a validated hypomorph for CNS therapeutic rescue** unless and
> until CNS residual expression is demonstrated.
