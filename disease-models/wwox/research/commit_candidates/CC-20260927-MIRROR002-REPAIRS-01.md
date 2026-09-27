# COMMIT CANDIDATE — CC-20260927-MIRROR002-REPAIRS-01

**Candidate ID:** CC-20260927-MIRROR002-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `6c81a2b`
**Author:** ACTOR_ID `scientist`, wave-2 package `m002`, dispatched by the Orchestrator under the operator
standing authorisation of 2026-09-27 (*"procedi tu, ti autorizzo su tutto"*).
**Source of the task:** the Mirror ex-post review of `BATCH_20260927_002`, persisted verbatim at
[`session_evaluations/2026-09-27_BATCH_20260927_002_mirror_review.md`](../session_evaluations/2026-09-27_BATCH_20260927_002_mirror_review.md)
(overall verdict *CONFIRMED WITH FINDINGS*: 0 blocking-scientific, 8 MINOR, 7 NOTE, 9 follow-up surfaces).
This candidate carries **every item of that review that needs one of the four current files or
`disease_model.md`**: F1, F2, F3, F4, F5, N1–N7, the qualifiers of WM row 037, and the optional pointers
at the WM historical rows. The non-canonical items (F6, F7, F8, follow-up surfaces 2–7) were applied
directly by the same package and are listed in §5.
**Declared change class: `MINOR`.** No claim `Status`, `Type`, `Transferability`, BLOCCO 1 field or
therapeutic statement moves; `CLAIM 005`'s prohibition span is not touched (none of the ops below
intersects it); no claim or paper is added or removed. Every op corrects wording against the source the
claims already cite, narrows an unscoped universal to its corpus, or removes an evidential graph edge
that a navigation link should have been. The one op inside a `consolidated baseline` record's boundary
that could be read as narrowing (`C5-4`, *"the `Wwox` literature"* → *"`Wwox` rodent models"*) restates a
sentence whose meaning was already withdrawn and re-written by `BATCH_20260927_002`; its locator triples
are in §4 anyway.
**Receipts read:** `FTR-20260913-24369382-01` / `-02` (PMID 24369382, `complete_fulltext_read`,
`files/fulltext/PMID24369382_Mallaret2014_PMCreader.html`, sha256
`a3a15a3be0353058fcb6160d602e03f5605b5148edfbb8de081d9f98e45a1413`, re-hashed this session: equal) ·
`FTR-20260814-42422765-06` (PMID 42422765).
**Manifests:** `deepdive_manifests/PMID24369382.json` (35 → **42** entries, 35–41 added this package) ·
`deepdive_manifests/PMID42422765.json` (34 → **36** entries, 34–35 added this package).
**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before the sources were reopened: the Mirror
review, `CLAIM 005`, `CLAIM 037`, `PAPER 042`, WM rows 037/changelog, `disease_model.md` §repair log, the
manifests and receipts named above. Questions fixed first: *(1) what exactly does Mallaret's body say
about the day-20 count, handling, the comparator, the lifespan and the front-matter block; (2) how does
the abstract's rat sentence end; (3) which `Wwox`-null allele supplies PMID 42422765's ECoG data.*

---

## 1 · CURRENT_TARGET and verification of each Mirror item

Every Mirror statement below was re-checked against the current file (byte counts of each `old` string
= 1) and, where it concerns the source, against the fingerprinted surface. **All eleven are confirmed**;
none was taken on the reviewer's word.

| Item | Mirror claim | Verified | How |
|---|---|---|---|
| F1 | `CLAIM 005`: *"Seizures in the `Wwox` literature are therefore documented in two species"* omits human patients and hides that three earlier mouse datasets had already falsified the rat-only sentence | ✅ | `CLAIM 005` / `CLAIM 037` already cite PMID 32000863, 42422765 (mouse null) and 36828035 (`P47T` knock-in) for mouse seizure-related phenotypes |
| F2 | *"all four survivors at 20 days"* drops the T4 qualifier | ✅ | Results: *«All knock-out mice presented at different times with seizures…»*; Fig. 4 legend: first mouse at 30 s, *«two other mice»* at 4 min — manifest entries 35, 36 |
| F3a | the chain sentence says the PMID is *"deliberately not restated"*, then restates it in *"19936220 → 19500159 → 17803050"* | ✅ | escapes LINT only because `coverage_report.PMID` is `PMID[:\s]*(\d{7,8})` |
| F3b | *"That terminus asserts the opposite for the mouse"* names 19500159 the terminus; the terminus is 17803050 | ✅ | `CLAIM 005` text, same boundary |
| F3c | *"a survey over papers none of which recorded seizures"* — the survey includes the rat paper, which did | ✅ | Table 2 of PMID 19500159 has an `lde/lde` column (`FTR-20260806-19500159-01`) |
| F4 | title qualifiers thin: unscored, no EEG, one laboratory, acoustic specificity not established | ✅ | *«Other stimuli such as animal handling also induced seizures on some occasions.»* — entry 37; comparator entry 38 |
| F5 | `PAPER 042` `Claim links … 005` is an evidential edge added to clear an advisory warning | ✅ | `support_linkage.py` docstring: *"A missing edge is a review candidate, never an instruction to add it"*; `trace_claim_foundation.EVIDENTIAL_EDGES = {"source_field","claim_links"}`; pathograph pairs `CLAIM 005 ↔ 007/008/019/030/033` via `PAPER 042` (5 rows) |
| N1 | the front-matter block does not *begin* with *«Mallaret et al. report mutations»* | ✅ | the block begins *"The genetic basis of many recessive cerebellar ataxias is unknown."* — read on the surface; not locatorable (the verifier classes that block as abstract material and refused it as a body locator) |
| N2 | *"manifest entry 33"* is 0-based | ✅ | `entries[33]` = Fig. 4 attestation; `entries[32]` = Fig. 3 Ponceau |
| N3 | four unscoped universals | ✅ | `PAPER 042` Role + dataset line; WM repair section; `CLAIM 037` REVIVAL_TRIGGER |
| N4 | the abstract sentence continues | ✅ | *«…a phenotype previously observed in the spontaneous Wwox mutant rat presenting with ataxia and epilepsy»* — `abstract_snippet` of entry 41 |
| N5 | `disease_model.md`: *"Two canonical records said … audiogenic only in the rat"* — `CLAIM 005` said *seizures* | ✅ | pre-batch `CLAIM 005`: *«Seizures in the Wwox literature are a rat `lde/lde` phenotype»* |
| N6 | the null of PMID 42422765 is unassigned; if neither NCKU nor `BK5-Cre`, the tally is five | ✅ **five** | Obeid 2026 Materials and methods *Mice*: *«The generation of Wwox-null (−/−) mice (KO) was previously reported.»* citing bib69 = Aqeilan et al. 2007, *«Targeted deletion of Wwox reveals a tumor suppressor function»*; *«Mice were kept on an FVB (Friend leukemia Virus B) background.»* — PMID42422765.json entries 34, 35 |
| N7 | `PAPER 042` Role bold never closes; `PAPER 042` Wikilinks lack `CLAIM 037`; rat-caveat clause still reads *2–3 settimane nel topo* first; *"non esaurisce"* obscure | ✅ all four | current file |
| WM 037 | mirror row carries the same thin qualifiers | ✅ | BLOCK 2 row 037 |
| Item 6.8 | WM:17, :257, :262 historical rows repeat the rat-only framing | ✅ | historical; pointers only, marked OPTIONAL |

---

## 2 · PROPOSED_DELTA — exact operation lists

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

Twelve `replace-within` ops; all dry-run clean on base `6c81a2b`
(`DRY RUN … 12 op(s) on ['CLAIM 005' ×4, 'CLAIM 037' ×8]`). The ops JSON is the concatenation of the
`op`/`id`/`old`/`new` fields below, in order.

#### C5-1 (F3a, F5) — `CLAIM 005` · `replace-within`

**old (verbatim):**

```text
its cited terminus [[paper_registry_current#PAPER 059]] (Suzuki 2007, receipt `FTR-20260806-17803050-01`; its PMID is deliberately not restated here — the chain is walked from the paper graph, not read off this claim) and — since 2026-09-13 — Mallaret 2014 itself, PMID 24369382 ([[paper_registry_current#PAPER 042]], `FTR-20260913-24369382-01`), which is **not** a link of the 19936220 → 19500159 → 17803050 chain but a separate first-hand mouse observation, and which is why the chain's rat-only terminus no longer bounds what the literature records.
```

**new:**

```text
its cited terminus [[paper_registry_current#PAPER 059]] (Suzuki 2007, receipt `FTR-20260806-17803050-01`) and — since 2026-09-13 — Mallaret 2014 itself ([[paper_registry_current#PAPER 042]], `FTR-20260913-24369382-01`), which is **not** a link of the `PAPER 057` → `PAPER 058` → `PAPER 059` chain but a separate first-hand mouse observation, and which is why the chain no longer bounds what the literature records about the mouse.
```

#### C5-2 (F3b) — `CLAIM 005` · `replace-within`

**old (verbatim):**

```text
🔴 **That terminus asserts the opposite for the mouse, and it is not the end of the chain:**
```

**new:**

```text
🔴 **The chain's middle link asserts the opposite for the mouse, and the chain does not bound the mouse literature:**
```

#### C5-3 (F3c) — `CLAIM 005` · `replace-within`

**old (verbatim):**

```text
— a **survey** over papers none of which recorded seizures (see
```

**new:**

```text
— a **survey** over mouse papers none of which recorded seizures (see
```

#### C5-4 (F1, F2, F5) — `CLAIM 005` · `replace-within`

**old (verbatim):**

```text
Mallaret 2014 (PMID 24369382), the fourth paper co-attributed in this boundary and read in full on 2026-09-13 (`FTR-20260913-24369382-01`), reports first-hand in the constitutive `Wwox`-null **mouse**: *«a few spontaneous seizures at ∼2 weeks of age»*; *«three of eight»* audiogenic tonic-clonic seizures at 16 days and all four survivors at 20 days, against *«No wild-type mice of matched age and background (n = 8)»* — behaviourally and **unscored**, one laboratory, no EEG. Seizures in the `Wwox` literature are therefore documented in **two species**; the mouse limb, its denominators and its limits live in [[claim_registry_current#CLAIM 037]].
```

**new:**

```text
Mallaret 2014 ([[paper_registry_current#PAPER 042]]), the fourth paper co-attributed in this boundary and read in full on 2026-09-13 (`FTR-20260913-24369382-01`), reports first-hand in the constitutive `Wwox`-null **mouse**: *«a few spontaneous seizures at ∼2 weeks of age»*; *«three of eight»* audiogenic tonic-clonic seizures at 16 days and, per the Results text, all four survivors at 20 days (the Fig. 4 legend accounts for three), against *«No wild-type mice of matched age and background (n = 8)»* — behaviourally and **unscored**, one laboratory, no EEG. Seizure-related phenotypes in `Wwox` **rodent models** are therefore documented in both rat and mouse — first-hand in the mouse since Mallaret 2014, and subsequently in the NCKU null (`PAPER 019`), the Aqeilan-line null (`PAPER 011`) and the `P47T` knock-in (`PAPER 007`), which had already falsified the rat-only sentence before this correction; the mouse limb, its denominators and its limits live in [[claim_registry_current#CLAIM 037]].
```

#### C37-1 (F4) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
(behaviourally, with a wild-type comparator)
```

**new:**

```text
(behavioural, unscored, no EEG, one laboratory, wild-type comparator 0/8; handling also provoked seizures, so acoustic specificity is not established)
```

#### C37-2 (N1) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
(the block before *Keywords*, beginning *«Mallaret et al. report mutations»*)
```

**new:**

```text
(the block before *Keywords* that contains *«Mallaret et al. report mutations»*)
```

#### C37-3 (N2) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
(manifest entry 33, a figure attestation)
```

**new:**

```text
(manifest `entries[33]`, 0-based, a figure attestation)
```

#### C37-4 (N4) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
*«we observed that the short-lived Wwox knock-out mouse display spontaneous and audiogenic seizures»*
```

**new:**

```text
*«we observed that the short-lived Wwox knock-out mouse display spontaneous and audiogenic seizures, a phenotype previously observed in the spontaneous Wwox mutant rat presenting with ataxia and epilepsy»*
```

#### C37-5 (N6) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
the video-EEG data are the **`P47T` knock-in, which is not a null**. Four genotypes, two species;
```

**new:**

```text
the ECoG/SWD data of PMID 42422765 are the **Aqeilan-laboratory targeted-deletion null** — *«Mice were kept on an FVB (Friend leukemia Virus B) background»*, the knockout's generation cited to Aqeilan et al. 2007 — neither NCKU nor `BK5-Cre`; the video-EEG data are the **`P47T` knock-in, which is not a null**. Five genotypes, two species;
```

#### C37-6 (N3) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
the only route by which this result could reach a WWOX-DEE genotype.
```

**new:**

```text
the only route identified here as of 2026-09-27 (`PREMISE: INFERENZA`) by which this result could reach a WWOX-DEE genotype.
```

#### C37-7 (N7c) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
2–3 settimane nel topo contro **3–12 settimane** nel ratto, con esordio più precoce delle crisi al giorno 16 — ⚠️ **la cifra murina è corretta 2026-09-27:**
```

**new:**

```text
sopravvivenza murina *2–3 settimane* secondo la Table 2 di PMID 19500159, ma **3–4 settimane al massimo** secondo Mallaret (qui sotto), contro **3–12 settimane** nel ratto, con esordio più precoce delle crisi al giorno 16 — ⚠️ **la cifra murina è corretta 2026-09-27:**
```

#### C37-8 (N7d) — `CLAIM 037` · `replace-within`

**old (verbatim):**

```text
la finestra murina 3–4 settimane **non esaurisce** l'esordio audiogeno del ratto, e le crisi murine sono ora documentate dentro di essa.
```

**new:**

```text
la finestra murina di 3–4 settimane **contiene** l'età d'esordio del ratto (giorno 16), e le crisi murine sono ora documentate dentro di essa.
```

### 2.2 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped)

Six `replace-within` ops (dry-run clean: `6 op(s) on ['Working Model Current', 'BLOCK 2', 'BLOCK 3',
'Working Model Current', 'BLOCK 3', 'BLOCK 3']`). **WM-4, WM-5, WM-6 are OPTIONAL** pointers on
historical rows (Mirror item 6.8: *"rightly not rewritten … an optional pointer would help"*); an
executor who prefers historical rows byte-frozen drops them and loses nothing else. The batch executor
adds its own `Version` / `Last update` / changelog row (WM_v6.0 → **WM_v6.1**, MINOR) as usual.

#### WM-1 (F2) — `heading: Working Model Current` · `replace-within`

**old (verbatim):**

```text
(3/8 at 16 days; the 4 survivors at 20 days; 0/8 wild type)
```

**new:**

```text
(3/8 at 16 days; per the Results text the 4 survivors at 20 days, the Fig. 4 legend accounting for three; 0/8 wild type)
```

#### WM-2 (F4) — `BLOCK 2` · `replace-within`

**old (verbatim):**

```text
(behavioural, unscored, wild-type comparator)
```

**new:**

```text
(behavioural, unscored, no EEG, one laboratory, wild-type comparator 0/8; handling also provoked seizures, so acoustic specificity is not established)
```

#### WM-3 (N3) — `BLOCK 3` · `replace-within`

**old (verbatim):**

```text
is still the only repeated-session series
```

**new:**

```text
is still the only repeated-session series in the corpus read here as of 2026-09-27
```

#### WM-4 (OPTIONAL pointer, Item 6.8) — `heading: Working Model Current` · `replace-within`

**old (verbatim):**

```text
**037** (the seizure phenotype is a rat `lde/lde` phenotype, EEG-documented, explicitly absent in mice)
```

**new:**

```text
**037** (the seizure phenotype is a rat `lde/lde` phenotype, EEG-documented, explicitly absent in mice — ⚠️ *superseded by `BATCH_20260922_SEIZURE` and `BATCH_20260927_002`: the mouse limb is now documented, see `CLAIM 037`*)
```

#### WM-5 (OPTIONAL pointer, Item 6.8) — `BLOCK 3` · `replace-within`

**old (verbatim):**

```text
while **keeping the true part — the audiogenic/kindling phenotype is rat-specific**.
```

**new:**

```text
while **keeping the true part — the audiogenic/kindling phenotype is rat-specific**. ⚠️ *(Audiogenic limb withdrawn by WM_v6.0, 2026-09-27; kindling-like still rat-only.)*
```

#### WM-6 (OPTIONAL pointer, Item 6.8) — `BLOCK 3` · `replace-within`

**old (verbatim):**

```text
**037** the seizure phenotype as a rat `lde/lde` phenotype, EEG-documented,
```

**new:**

```text
**037** the seizure phenotype as a rat `lde/lde` phenotype, EEG-documented *(mouse limb added by WM_v5.0 and WM_v6.0)*,
```

### 2.3 `disease-models/wwox/registries/paper_registry_current.md` — FULL REWRITE (record `PAPER 042` only)

`propagate` refuses this file by name (exit 4). Describe as a full rewrite in which **every byte outside
`PAPER 042` is copied verbatim** and, inside `PAPER 042`, only the six exact substitutions below are made
(each `old` occurs once in the whole file; P42-2 carries the record separator to pin it to `PAPER 042`).

#### P42-1 (F5)

**old (verbatim):**

```text
**Claim links:** 007, 008, 019, 030, 033 · 037 (the mouse audiogenic and spontaneous seizure dataset, added by `BATCH_20260927_002`) · 005 (its imported-premise boundary cites this paper; same batch)
```

**new:**

```text
**Claim links:** 007, 008, 019, 030, 033 · 037 (the mouse audiogenic and spontaneous seizure dataset, added by `BATCH_20260927_002`)
```

#### P42-2 (F5, N7b)

**old (verbatim):**

```text
**Wikilinks:** [[claim_registry_current#CLAIM 007]] · [[claim_registry_current#CLAIM 008]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 033]]

---

## PAPER 045
```

**new:**

```text
**Wikilinks:** [[claim_registry_current#CLAIM 007]] · [[claim_registry_current#CLAIM 008]] · [[claim_registry_current#CLAIM 019]] · [[claim_registry_current#CLAIM 030]] · [[claim_registry_current#CLAIM 033]] · [[claim_registry_current#CLAIM 037]] · [[claim_registry_current#CLAIM 005]]

---

## PAPER 045
```

#### P42-3 (N7a, N3)

**old (verbatim):**

```text
**e — registrato 2026-09-27 da `BATCH_20260927_002` — l'unica fonte di una provocazione audiogena con comparatore wild-type in un topo `Wwox`, su cui poggia ora [[claim_registry_current#CLAIM 037]]
```

**new:**

```text
**e — registrato 2026-09-27 da `BATCH_20260927_002` — l'unica fonte, nel corpus letto qui al 2026-09-27 (`PREMISE: INFERENZA`), di una provocazione audiogena con comparatore wild-type in un topo `Wwox`**, su cui poggia ora [[claim_registry_current#CLAIM 037]]
```

#### P42-4 (N3)

**old (verbatim):**

```text
il paper contiene l'unico esperimento di provocazione audiogena su un topo `Wwox` con comparatore.
```

**new:**

```text
il paper contiene l'unico esperimento di provocazione audiogena su un topo `Wwox` con comparatore nel corpus letto qui al 2026-09-27 (`PREMISE: INFERENZA` — un universale di corpus, non di letteratura).
```

#### P42-5 (N2)

**old (verbatim):**

```text
Fig. 4 sono sedici fotogrammi (manifest entry 33).
```

**new:**

```text
Fig. 4 sono sedici fotogrammi (manifest `entries[33]`, 0-based).
```

#### P42-6 (locator count re-derived)

**old (verbatim):**

```text
35 verbatim locators (28 body on the PMC reader text, 7 figure attestations)
```

**new:**

```text
42 verbatim locators (35 body on the PMC reader text, 7 figure attestations; entries 35–41 added 2026-09-27 by wave-2 `m002`, verified `--verify-artifacts --require-current-schema` PASS)
```

### 2.4 `disease-models/wwox/disease_model.md` — exact replace (repair-log paragraph for WM v5.7 → v6.0)

#### DM-1 (N5)

**old (verbatim):**

```text
Two canonical records said the seizure phenotype of WWOX rodent models was audiogenic **only in the rat**, and one of them added
```

**new:**

```text
One canonical record said the **audiogenic** phenotype of WWOX rodent models was rat-specific, a second (`consolidated baseline`) said **seizures** in the `Wwox` literature were a rat `lde/lde` phenotype, and the first added
```

#### DM-2 (F2)

**old (verbatim):**

```text
(3 of 8 constitutive knock-outs at 16 days; the four survivors at 20 days)
```

**new:**

```text
(3 of 8 constitutive knock-outs at 16 days; per the Results text the four survivors at 20 days, the Fig. 4 legend accounting for three)
```

### 2.5 Not proposed

- No change to `LIT-0294` — its *"Coda FT-128 chiusa dalla lettura"* is now true: the `FT-128` closure
  was appended by this package (§5).
- No change to `PAPER 059` (Mirror F6: keeping it unchanged is correct on the merits).
- No change to `CLAIM 005`'s prohibition span (sha256 `fb94a48c…`, 1170 chars per the Mirror); none of
  C5-1…C5-4 intersects it — C5-4 ends at *"…live in [[claim_registry_current#CLAIM 037]]."*, the sentence
  immediately before *"**No canonical statement may assert EPILEPTOGENESIS"*.
- No `Status` change anywhere; no `growth_anchors.py record` (no structural delta).

---

## 3 · Simulation — the whole candidate applied to a scratch copy of `6c81a2b` + this package

| check | before | after |
|---|---|---|
| `legend_lint.py .` | WARN, 0 BLOCK, 11 `WARN_BUT_PROCEED` | **identical set** — 11, 0 BLOCK (the two `CLAIM 005` PMID 24369382 names become record pointers, so removing `005` from `PAPER 042`'s Claim links opens no `UNLINKED_SUPPORT`) |
| `test_trace_claim_foundation.py` | OK | **OK** (`--claim 'CLAIM 005' --lineage` no longer lists `PAPER 042`; `PAPER 059` still at hop 1) |
| `scripts/test_scientific_consistency.py` · `scripts/test_canonical_structure.py` · `test_support_linkage.py` | OK | **OK** |
| pathograph shared-evidence pairs | 35 | **30** — exactly the five spurious `CLAIM 005 ↔ 007/008/019/030/033` via `PAPER 042` removed; `CLAIM 005` shared-evidence count 4 → 3; `CLAIM 005 <-> CLAIM 037` keeps `PAPER 058` |

**Phase 4.7 is owed after propagation:** regenerate `pathograph_inventory.md` and its export.

---

## 4 · LOCATOR TRIPLES FOR BLIND AUDIT

(proposition | verbatim quote | anchor)

1. In Mallaret 2014, per the Results text, all four surviving knock-out mice seized at day 20 | *"All knock-out mice presented at different times with seizures, consisting as before of wild running followed by tonic contractions and clonic movements, and had uncontrolled sphincter relaxation"* | `files/fulltext/PMID24369382_Mallaret2014_PMCreader.html` — Results, *Conditional knock-out mouse model*, sentence after *"At 20 days, the four surviving mice were exposed to a 14 kHz tone."*
2. The Fig. 4 legend accounts for three mice at day 20 | *"After 4 min sound exposure, two other mice also experienced clonic movements"* | same artefact — Figure 4 legend, (B) clause (the first mouse is the (A) clause, *"After 30 s sound exposure, the first mouse…"*)
3. Acoustic specificity of the provocation is not established | *"Other stimuli such as animal handling also induced seizures on some occasions."* | same artefact — Results, *Conditional knock-out mouse model*
4. The wild-type comparator is 0 of 8 | *"No wild-type mice of matched age and background (n = 8) presented with seizures upon 11 or 14 kHz sound exposure."* | same artefact — Results, *Conditional knock-out mouse model*, closing sentence
5. The mouse lifespan figure in Mallaret is 3 to 4 weeks maximum, cited not measured | *"These knock-out mice are characterized by a short lifespan of only 3 to 4 weeks maximum"* | same artefact — Results, *Conditional knock-out mouse model*, opening paragraph
6. The abstract frames the mouse phenotype as previously observed in the rat, with ataxia and epilepsy | *"a phenotype previously observed in the spontaneous Wwox mutant rat presenting with ataxia and epilepsy"* | same artefact — Abstract
7. The front-matter summary block begins with a general sentence, not with "Mallaret et al. report mutations" | *"The genetic basis of many recessive cerebellar ataxias is unknown. Mallaret et al. report mutations in the WW domain-containing oxidoreductase gene WWOX"* | same artefact — summary block immediately before *Keywords*
8. The null used in PMID 42422765 is kept on FVB and its generation is cited to a prior report | *"Mice were kept on an FVB (Friend leukemia Virus B) background."* | `files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` — Materials and methods, *Mice* (sec4.2)
9. That prior report is Aqeilan et al. 2007's targeted deletion of Wwox | *"Targeted deletion of Wwox reveals a tumor suppressor function"* | same artefact — References, bib69


---

## 5 · Applied outside this candidate by the same package (non-canonical, MINOR, 2026-09-27)

- **(a)** Mirror review persisted verbatim: `session_evaluations/2026-09-27_BATCH_20260927_002_mirror_review.md`.
- **F7** `dismissal_ledger_current.md` `DIS-011`: append-only **RI-AUDIT 2026-09-27** — triggers (a) and (c)
  fired, the lifespan/onset sentence withdrawn, the rejection of **epileptogenesis stands** (verdict text
  reworded in the block, not in the heading), replacement `REVIVAL_TRIGGER`.
- **F8** `full_text_queue_current.md`: `FT-128` **CLOSURE** block (receipt `FTR-20260913-24369382-01`);
  dated corrections under `FT-130` next action 1 and `FT-131` status (the *"unacquirable, same as FT-128"* comparisons).
- **F6** erratum appended to `session_evaluations/2026-09-27_BATCH_20260927_002.md`.
- Follow-up 2 `DL-MECH-075` append-only rectification; 3 `analysis/seizure_ascertainment_census_20260922.md`
  (top pointer, Q2 pointer, end-of-file correction table); 4 `analysis/AUTONOMOUS_SESSION_STATE.md` (two dated
  inline corrections); 6 `analysis/blunt_instrument_claim_audit_20260920.md` (note after the SOUND table);
  7 `analysis/legacy_reconstruction_sweep_20260922.md` (superseded note).
- Follow-up 9 (benchmarks, frozen — **not edited**, handed to Harness Engineering):
  `framework/eval/benchmarks/BENCH-I-CLAIM-RETRIEVAL/{fixture_spec.json, fixtures.json, i2_runs.jsonl}` and
  `framework/eval/benchmarks/BENCH-J-RECORD-SCOPED-EDIT/j0_corpus.json` encode the pre-WM_v6.0 `CLAIM 037`;
  any live regeneration against current claims will diverge.

---

## WAVE-2 READINESS (2026-09-27)

**Actor:** ACTOR_ID `scientist`, wave-2 package `m002` · **Verdict: `READY_MINOR`** (whole candidate).
**`context_policy` declared: `QUESTION_DRIVEN`** (questions and held records in the header).

**What was done (not noted — done):**
- **Missing verbatim locators added**, read first-hand on the fingerprinted surfaces:
  `PMID24369382.json` entries **35–41** (day-20 all-four text; Fig. 4 legend's three; handling; 0/8
  comparator; *3 to 4 weeks maximum*; *died before 4 weeks*; the body's `lde` comparison with the abstract's
  rat sentence as `abstract_snippet`) — `deepdive_manifest.py --pmid 24369382 --verify-artifacts
  --require-current-schema --artifact-workspace <root>` → **PASS, 0 gaps**. `PMID42422765.json` entries
  **34–35** (FVB background; bib69 = Aqeilan 2007) — **no BLOCK on either new entry**; the manifest's 31
  pre-existing BLOCK lines are entries 20–33 declared on `files/fulltext/PMID42422765_Obeid2026_PMC.html`,
  absent from this checkout (not this package's; flagged for the `dose`/provenance owners).
- **Refused and withdrawn:** a locator on the front-matter block (N1) — the verifier classes it as
  abstract material (*"quote occurs in the abstract but not the non-abstract body"*). N1's wording repair
  stands on the surface read and on locator triple 7; nothing propagated rests on a refused locator.
- **Receipts prepared, NOT recorded** (the ledger is a hash chain shared with parallel packages):
  `receipts_pending/m002_24369382_1.json` (`FTR-20260927-24369382-03`, `partial_fulltext_read`,
  `new_question_outside_prior_coverage`, prior `FTR-20260913-24369382-02`) and
  `receipts_pending/m002_42422765_1.json` (`FTR-20260927-42422765-08`, prior `FTR-20260814-42422765-06`;
  sequenced after the pending `dose` receipt `-07`). Both pass `validate_new_receipt` and `validate_receipt`
  with zero errors.
- **Stale wording redrafted against the CURRENT canonical text**: every `old` string above is copied from
  base `6c81a2b` and occurs exactly once; the two record-scoped files dry-run clean under
  `batch_commit.py propagate`; the full candidate was applied to a scratch copy and passed LINT (same 11
  warnings, 0 BLOCK), `test_trace_claim_foundation`, `test_scientific_consistency`,
  `test_canonical_structure`, `test_support_linkage` (§3).
- **Disposition contradiction adjudicated:** F6/F5 — the report said the PMID in `CLAIM 005`'s prose made
  a depth-0 edge; the tracer's `STRUCTURAL_FIELDS` exclude `Evidence boundary`, so only `PAPER 059`'s
  `Claim links` did. Adjudicated from `framework/scripts/trace_claim_foundation.py` and the `015c618`
  pathograph diff (3 → 4, not 3 → 5); erratum appended to the batch report.

**Change class: `MINOR`** — no `Status`/`Type`/`Transferability`, BLOCCO 1, therapeutic, cardinality or
prohibition change; `C5-4` restates an already-withdrawn sentence with its correct scope. Locator triples
are provided in §4 regardless, because `CLAIM 005` is `consolidated baseline`.

**Operation list:** §2.1 (12 × `replace-within`, `claim_registry_current.md`, `CLAIM 005` ×4 /
`CLAIM 037` ×8) · §2.2 (6 × `replace-within`, `working_model_current.md`; WM-4…6 OPTIONAL) · §2.3 (paper
registry full rewrite, `PAPER 042`, 6 substitutions) · §2.4 (`disease_model.md`, 2 substitutions) · then
Phase 4.7 (pathograph regeneration; expect shared-evidence pairs 35 → 30).

**Pending, owned elsewhere:** recording the two receipts (Orchestrator / batch executor, in ledger order
after `dose`'s `-07`); the benchmark fixtures of follow-up 9 (Harness Engineering).
