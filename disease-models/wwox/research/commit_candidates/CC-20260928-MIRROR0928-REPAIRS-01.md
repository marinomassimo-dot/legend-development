# COMMIT CANDIDATE — CC-20260928-MIRROR0928-REPAIRS-01

**Candidate ID:** CC-20260928-MIRROR0928-REPAIRS-01
**Status:** `PROPOSED — NOT PROPAGATED`
**Base head:** `748a94b` (`main` at dispatch; written on `task/mirror0928-repairs`)
**Author:** ACTOR_ID `scientist`, package `mirror0928`, dispatched by the Orchestrator under the
operator's standing authorisation of 2026-09-27 (*"procedi tu, ti autorizzo su tutto"*).
**Source of the task:** the MIRROR ex-post review of `BATCH_20260928_001`, persisted verbatim at
[`session_evaluations/2026-09-28_BATCH_20260928_001_mirror_review.md`](../session_evaluations/2026-09-28_BATCH_20260928_001_mirror_review.md)
(overall verdict *CONFIRMED WITH FINDINGS*: **0 BLOCKING-SCIENTIFIC**, 6 MINOR, 7 NOTE; the review
also withdrew its own earlier `M6b` and corrected two of its own counts).
This candidate carries **only the items of that review that need one of the four scientific current
files or `disease_model.md`**: FINDINGS **1, 2, 3, 4, 5, 6 and 10**. FINDING 9 and FINDING 11 were
applied outside any batch (§5); FINDINGS 7, 8, 12 and 13 are Harness Engineering hand-offs and are
deliberately **not** written here (§6); three findings are **contested in whole or in part** and their
evidence is in §4.
**Declared change class: `MINOR`.** Every item is a wording repair, a scope narrowing or an
annotation. Per-item classes are declared beside each op. 🔴 **No claim `Status`, `Type`,
`Transferability`, `clinical relevance`, BLOCCO 1 field or therapeutic `SCORE`/`SAFETY` value moves;
no datum changes; no claim or paper is added or removed; `CLAIM 005` is not touched.** One item
(`C30-1`) **narrows the meaning** of a claim paragraph by dropping a universal, so locator triples are
supplied in §3.
**Receipts read:** `FTR-20260927-42589397-02` and `FTR-20260921-42589397-01` (PMID 42589397) ·
`FTR-20260810-42397075-01` … `-04` (PMID 42397075, the full four-event lineage, read to settle which
event produced the manifest) · the PMID 36779245 and PMID 42422765 artefacts re-hashed this session:
`files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml` =
`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34` (**equal**),
`files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml` =
`ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af` (**equal**),
`files/fulltext/PMID42422765_Obeid2026_PMC_2026-09-27.xml` =
`7bea83346b708e541d2c432e5da4029f69673e1abc3c6fe70926ad0e3ec2eef2` (**equal**).
**Manifests read, none edited:** `deepdive_manifests/PMID42589397.json` (7 entries; entries 6 and 7
re-verified verbatim here) · `deepdive_manifests/PMID42397075.json` (30 entries; `receipt` field read,
not touched). **A receipt event is owed and is prepared, not recorded:** see §5(d).
**`context_policy`: `QUESTION_DRIVEN`** — declared. Held before any source was opened: the Mirror
review of `BATCH_20260928_001`; `CLAIM 002 · 019 · 025 · 030 · 033`, `PAPER 001 · 018 · 042 · 117 ·
118`, `CORPUS-STUB-059` and `LIT-0420` read **by record** with `registry_records.py get`, never by
grep over the two large registries; `working_model_current.md` lines 7 and 252 and its `## Changelog`
heading; `disease_model.md`'s repair changelog; `therapeutic_strategies_current.md` § `TX-007`;
`dismissal_ledger_current.md` `D-23`; `state_history.md` § 4 and § 7;
`CC-20260928-MIRROR003-REPAIRS-01` and `-MIRROR004-REPAIRS-01`; `framework/protocols/
fulltext_read_receipt.md`; `framework/scripts/record_scoped_edit.py` and `deepdive_manifest.py`.
Questions fixed **before** reopening a source: *(1) do patients 2 and 5 of PMID 36779245 Table 1 differ
on anything besides survival, and is the `colspan="2"` cell before or after them; (2) do all 13
patients really share the three severity axes; (3) is `gravità` defined anywhere as exactly those three
axes; (4) is `declared gaps` defined anywhere as the waived manifest sections; (5) which receipt of
PMID 42397075 produced `PMID42397075.json`; (6) does the receipt protocol excuse a locator capture made
inside a prior receipt's coverage; (7) how many one-directional claim→claim edges did
`BATCH_20260928_001` actually move.*

---

## 1 · Verification of each Mirror item, first-hand

**A reviewer's output is not gospel.** Every statement below was re-measured against the source or the
current file before it was accepted, and the three that did not survive are recorded as CONTESTED in
§4 with their evidence rather than repaired as stated. Each `old` string was measured as occurring
**exactly once** in its target file, and the whole operation list was **simulated** (§2.6).

| # | Mirror severity | verdict here | what was measured |
|---|---|---|---|
| **1** | MINOR | ✅ **CONFIRMED, and understated** | Table 1 parsed from the JATS markup: patients 2 and 5 differ on `Short stature` (*No* / *Yes*) and `Ophthalmologic features` (*"Absent eye contact; erratic ocular movements"* / *"Poor eye contact"*) — **and** on `Country`, `Family history for epilepsy` and `Consanguineous`, which the review did not name. The `colspan="2"` cell is the **9th** data cell, covering patients **9–10**, after both patients of interest: columns 2 and 5 align trivially. |
| **2** | NOTE | ⚠️ **CONFIRMED IN PART — the zero-variance claim is false for one of the three axes** | `Intellectual disability` = `Profound` **13/13** ✅ · `Walking/ambulant` = `No` **13/13** ✅ · `Speech` = `Nonverbal` **11/13** ❌ — patients **6** and **10** carry *«Single word "Dad"»* and *«Single word "Mama"»*. The review's *"all **13** patients … `Profound` / `Nonverbal` / `No`: zero variance"* is wrong on `Speech`. The substantive point survives and is folded in with the true figures (§4.1). |
| **3** | NOTE | ✅ **CONFIRMED verbatim** | `CC-20260928-MIRROR003-REPAIRS-01`'s disposition reads *"A first-hand reading with a receipt and a manifest stands behind the field, so it was propagated and the advisory is cleared by evidence rather than by declaration."* That licenses the `F5` defect exactly: a receipted reading of an irrelevant paper clears the same advisory. |
| **4** | MINOR | ✅ **CONFIRMED, and stronger than stated** | Manifest `receipt` = `FTR-20260921-42589397-01`; entries 6 and 7 carry `"found_or_sought": "sought"` and *"Added 2026-09-28"*; receipt `-02` declares **5** locators in both `outputs` and `evidence_basis`; ledger tail is `-02` and no 2026-09-28 event exists. Both entries fall inside `-02`'s `coverage` (`methods: read`, `results: read`) and **both verify verbatim, once each**, on the artefact. 🔴 **Stronger:** `-01` is wrong under **both** targets the protocol leaves open for that field — `-01`'s `outputs` name only an analysis file, and `-02`'s name the manifest. |
| **5** | MINOR | ⚠️ **CONTESTED on the noun — Mirror's own falsifier holds** | `deepdive_manifest.py --pmid 42589397` prints, in its own words, *"structurally valid with declared gaps (**5** gap(s))"* over exactly those five `waived` sections, and `fulltext_read_receipt.md` quotes the same vocabulary (*"declared gaps block the append"*, the validator's `incomplete` list). So **5** is the tool's own figure, not a wrong count. What is real is that one `Evidence depth` field uses *declared gap(s)* in **two incompatible senses two sentences apart**. Repaired as an ambiguity, recorded as a NOTE (§4.2). |
| **6** | NOTE | ✅ **CONFIRMED verbatim** | `PAPER 118` `Evidence depth` opens with *"Manifest `deepdive_manifests/PMID36779245.json` is a different paper; this one's is …"*. PMID 36779245 is `PAPER 018`'s artefact. Editing residue; deleted. |
| **10** | MINOR | ⚠️ **CONTESTED as "broken" — a disproof the review did not check** | The four-event lineage of PMID 42397075 measured here: `-03` is the **first** event whose `outputs` name `deepdive_manifests/PMID42397075.json`, i.e. the reading that **produced** it. `fulltext_read_receipt.md` declares the target of a manifest's `receipt` field 🟡 **OPEN** — *"the reading that PRODUCED the manifest, or the most recent reading of that paper … both are internally consistent, and **neither is a referential defect**"* — and names the exactly-analogous `PMID42422765.json` (`-04` against a later `-05`). So the chain is **not broken**; the reader lands on the other sanctioned target. The annotation is still worth making, and is made with corrected wording (§4.3). |

### 1.1 · Mirror's own falsifiers, checked before each finding was accepted

| falsifier | holds? | consequence |
|---|---|---|
| **1** — *FINDING 1 falls if `CLAIM 030`'s `gravità` is defined somewhere as exactly {intellectual disability, speech, ambulation}* | ✅ **holds (no definition exists)** | Searched: `claim_registry_current.md` carries the token `gravit` **three** times (CLAIM 030 `Summary`, CLAIM 030's observation, CLAIM 033 `clinical relevance`) and **none is a definition**; `working_model_current.md` carries it **zero** times; BLOCK 2 does not define it. FINDING 1 stands as MINOR. The repair therefore **names the three axes in the claim itself**, which is the cross-reference the falsifier was asking for. |
| **2** — *FINDING 4 falls if a receipt event exists or is written covering the 2026-09-28 capture, or if a rule states that locators added inside a prior receipt's declared coverage need no new event* | ❌ **does not hold** | No such rule anywhere in `fulltext_read_receipt.md`. The nearest texts point the **other** way: the protocol's own 2026-08-04 precedent recovered fourteen locators from already-read papers *"reopening the files and **issuing targeted receipts**"*, and `§ Correcting receipt metadata without fabricating a reread` supplies the exact instrument — `reread_reason: receipt_correction`, explicitly *"**not** a second reading"*. FINDING 4 stands; the honest repair is **both** a receipt event and an annotation (§5(d)). |
| **3** — *FINDING 5 falls if `declared gaps` is defined anywhere as "waived manifest sections"* | ✅ **holds** | It is so defined operationally: `deepdive_manifest.py` line 2630 sets `state = "structurally valid with declared gaps"` from its `incomplete` list, and prints `(5 gap(s))` for this manifest. FINDING 5 drops from MINOR to NOTE. |
| **4** — *FINDING 9 falls if "supplementary captions" means captions of supplementary **panels*** | ❌ **does not rescue the sentence** | Even under that reading the review's own rider applies: the sentence must say so, and as landed it asserts a universal negative two sentences before quoting one of the captions it denies. FINDING 9 stands; applied outside this candidate (§5(a)). |
| **5** — *FINDING 10 falls if some tool resolves a manifest through a field other than `receipt`* | ❌ **does not hold — but a stronger disproof does** | No resolver ignores the field; the protocol calls it *"the authoritative link"*. The finding fails for a different reason: that field's **target** is declared open and non-defective. FINDING 10 contested in part (§4.3). |
| **6** — *FINDING 11 falls if the two edges are excluded from the census's counting rule; it also falls if the residue is amended before the graph-hygiene candidate is written* | ✅ **the second limb holds, because it was made to hold** | The residue is amended now, outside this candidate, with both counting rules named (§5(b)). |
| **7** — *the PASS on B1's MINOR class falls if a rule makes a withdrawal inside a `T1` / `VERY HIGH` claim MAJOR regardless of `Status`* | ✅ **holds (no such rule)** | `prompt_batch_commit.md` §7 enumerates MAJOR by baseline status, not by transferability or clinical relevance. Re-checked here; the `BATCH_20260928_001` classification stands and nothing in this candidate reopens it. |

---

## 2 · PROPOSED_DELTA — exact operation lists

Nine ops over five files. Every `old` below was extracted **programmatically from the current file**
and asserted to occur exactly once in it, so no `old` is a transcription.

### 2.1 `disease-models/wwox/registries/claim_registry_current.md` — `batch_commit.py propagate` (record-scoped)

```bash
python3 framework/scripts/batch_commit.py propagate \
  --file disease-models/wwox/registries/claim_registry_current.md \
  --ops <ops_claims.json>            # dry run, then --apply
```
#### C30-1 (FINDINGS 1 + 2) — `CLAIM 030` · `replace-within` · **change class: `MINOR` (universal dropped, scope named)**

🔴 **This op narrows the meaning of the paragraph** — it removes a universal quantifier (*solo*) and
replaces an appeal to an undefined term (*gravità*) with the three axes the claim actually uses. Locator
triples for a blind audit are in §3. Nothing else in `CLAIM 030` is touched: `Status` (`in observation`),
`Type`, `Transferability` (`T1`), `clinical relevance` (`VERY HIGH`), `Source`, the `Corroboration` section and
the `PREMISE: DETECTION_FLOOR` note are byte-identical, and the paragraph's conclusion (**neutra**) does
**not** move — it is strengthened, because it no longer rests on one pair.

**old (verbatim, 1× in the file):**

```text
⚠️ **La discordanza è inoltre solo sulla sopravvivenza:** sull'asse che questo claim chiama *gravità* la Table 1 dà **entrambi** i pazienti con disabilità intellettiva profonda, non verbali e non deambulanti — cioè **concordanti**.
```

**new:**

```text
⚠️ **Sugli assi di gravità che questo claim usa — disabilità intellettiva, linguaggio, deambulazione — la coppia è concordante, e la discordanza rilevante per l'esito è la sopravvivenza; ma non è l'unica.** 🔴 **Corretto 2026-09-28 (`CC-20260928-MIRROR0928-REPAIRS-01`, revisione ex-post Mirror di `BATCH_20260928_001`, FINDING 1): il precedente *«solo sulla sopravvivenza»* era un universale falso, della stessa classe che questa serie di riparazioni corregge.** Ri-letta dal markup JATS, la Table 1 stampa **due ulteriori assi d'esame su cui i due pazienti differiscono** — `Short stature` (paziente 2 *No*, paziente 5 *Yes*) e `Ophthalmologic features` (*"Absent eye contact; erratic ocular movements"* contro *"Poor eye contact"*) — oltre a tre righe di contesto (`Country`, `Family history for epilepsy`, `Consanguineous`). ⚠️ **E la concordanza non porta informazione** (FINDING 2, verificato e corretto qui): sui 13 pazienti della tabella `Intellectual disability` è `Profound` **13/13** e `Walking/ambulant` è `No` **13/13** — varianza zero, quindi assi non discriminanti per costruzione — mentre `Speech` è `Nonverbal` in **11/13** (i pazienti 6 e 10 hanno una parola singola), quindi a varianza minima ma **non nulla**: il reviewer aveva scritto *tutti e 13* su tutti e tre gli assi e su `Speech` la tabella lo smentisce. La concordanza della coppia non è dunque una somiglianza misurata fra questi due pazienti: è l'**assenza, in questa tabella, di un asse di gravità che discrimini** — il che rende la lettura **neutra** indipendente da quale coppia si scelga fra gli **11** pazienti concordanti anche sul linguaggio. ⚠️ Nessun file definisce *gravità* come esattamente {disabilità intellettiva, linguaggio, deambulazione}: per questo il *solo* universale era raggiungibile, e per questo il claim ora **nomina i propri assi** invece di presupporli.
```
#### C2-1 (FINDING 10, contested in part) — `CLAIM 002` · `replace-within` · **change class: `MINOR` (annotation at point of use)**

One clause added so that a reader without the bytes can traverse the hop. 🔴 **The clause states what
was measured, not what the review asserted:** the manifest is not pointing at *a different event* by
defect, it is pointing at the **producing** reading, which is one of the two targets the protocol
leaves open and declares non-defective. The `Precisazione`'s substance, `CLAIM 002`'s `Status`
(`consolidated baseline`) and its quoted boundaries are untouched.

**old (verbatim, 1× in the file):**

```text
manifest a 30 locator, schema v2, strict PASS
```

**new:**

```text
manifest a 30 locator, schema v2, strict PASS — ⚠️ il campo `receipt` di quel manifest nomina `FTR-20260810-42397075-03`, la lettura **parziale che ha prodotto il manifest** (è `-03` a nominarlo per primo nei propri `outputs`), mentre la lettura **completa** citata qui è `-04`, i cui `outputs` nominano lo stesso file: `framework/protocols/fulltext_read_receipt.md` lascia **deliberatamente aperto** quale delle due un campo `receipt` designi e dichiara che *nessuna delle due è un difetto referenziale*, quindi chi segue il link trova l'altro dei due bersagli ammessi e non una catena rotta (annotato 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 10, contestato in parte)
```

### 2.2 `disease-models/wwox/registries/working_model_current.md` — `batch_commit.py propagate` (record-scoped)

🔴 **Anchor note, and it is a direct consequence of Mirror FINDING 13.** `WM-2` addresses the
`WM_v7.1` changelog row through `--heading "Changelog"`, **not** through `id: "BLOCK 3"`. Measured here
with `record_scoped_edit.resolve`: `id: BLOCK 3` resolves to a span that ends at **end of file** (offsets
49194 → 96155 = `len(text)`), because `## Changelog` is the last thing in the file and `_span_from`
falls back to `len(text)` with no warning — so a record-scoped edit would have had **no containment at
all**. `heading: Changelog` resolves to 52708 → 84811, bounded by `## BATCH_20260927_004`. Same result,
real containment.
#### WM-1 (FINDINGS 1 + 2) — `heading: "Working Model Current"` (the `Last update` line) · `replace-within` · **change class: `MINOR` (universal dropped)**

The `Last update` line sits above `# BLOCK 1`, inside the file's own H1 span. `# BLOCK 1` is not
touched by this candidate at all.

**old (verbatim, 1× in the file):**

```text
the discordance is **survival only**, so the pair does not discriminate and the rival explanations stay open.
```

**new:**

```text
the discordance that bears on outcome is **survival** — though **not survival alone**: Table 1 also prints `Short stature` and `Ophthalmologic features` differing between them, and those three concordant axes are given identically in **13 of 13** patients of that table for intellectual disability and ambulation and in **11 of 13** for speech, so they cannot discriminate any pair (scoped 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 1 and 2) — so the pair does not discriminate and the rival explanations stay open.
```
#### WM-2 (FINDINGS 1 + 2) — `heading: "Changelog"` (the `WM_v7.1` row) · `replace-within` · **change class: `MINOR` (universal dropped)**

A **description of what a past batch did** is corrected in place, with the correcting candidate and
the date named inside the row — the same discipline `BATCH_20260928_001` used, and the discipline
Mirror FINDING 8 asks to have written down. **The row's stated conclusion does not move**: the pair
was neutral before this op and is neutral after it. No version number changes and no row is added.

**old (verbatim, 1× in the file):**

```text
the discordance being survival only.
```

**new:**

```text
the discordance that bears on outcome being survival, though not survival alone — Table 1 also prints `Short stature` and `Ophthalmologic features` differing between them, and the three concordant axes carry no information, being identical in 13 of 13 patients for intellectual disability and ambulation and in 11 of 13 for speech (scoped 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 1 and 2).
```

### 2.3 `disease-models/wwox/registries/paper_registry_current.md` — **FULL REWRITE**, unchanged sections copied verbatim (`propagate` refuses this file by name, exit 4 — §4.0 of `prompt_batch_commit.md`)

**Post-condition, not a promise:** exactly **three** substitutions, each measured 1× in the file,
inside exactly **two** records (`PAPER 118`, `PAPER 001`). `git diff` after the rewrite must show hunks
in those two records and nowhere else.
#### P118-1 (FINDING 3) — `PAPER 118` `**Record provenance:**` · **change class: `MINOR` (licensing ground restated)**

🔴 **Appended, not replaced** — the existing provenance sentence is the `old` and is carried into the
`new` unchanged, so nothing already there is lost. What is added is the ground the edge actually
stands on. The `Claim links: 025` field itself is **not edited**: it was already correct, including
its *bounding source, not corroborating* mitigation.

**old (verbatim, 1× in the file):**

```text
Metadata taken from the declared JATS artefact's own `article-meta`.
```

**new:**

```text
Metadata taken from the declared JATS artefact's own `article-meta`. 🔴 **Why the `Claim links: 025` field stands — stated as derivation of the bound, not as receipt-existence (2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 3).** [[claim_registry_current#CLAIM 025]]'s `Evidence boundary` **derives its bound from this paper's own Cox models and event structure** — `228` OV patients with `161` events against `390` BRCA with `22`, `HR 1.11, 95% CI 0.92–1.35, p = 0.27`, concordance `0.49` — so the **evidential** edge is true. The receipt and the manifest establish that the reading **happened**; they do not establish that a source is **evidence for a claim**, and a receipted reading of an irrelevant paper would clear `[INFO] UNLINKED_SUPPORT_UNCHECKED` equally well — which is exactly the defect Mirror's `F5` named on `BATCH_20260927_002`, where `claim_links` is an evidential edge in `trace_claim_foundation.EVIDENTIAL_EDGES`. The producing candidate's wording, which licensed this field on receipt-existence, is superseded by its own appended correction note.
```
#### P118-2 (FINDINGS 4 + 5 + 6) — `PAPER 118` `**Evidence depth:**` · **change class: `MINOR` (residue deleted, provenance stated, vocabulary disambiguated)**

Three findings in one contiguous run, because they overlap in the same two sentences. The stray
`PMID36779245.json` clause is **deleted** (FINDING 6); the locator provenance is stated with the
2026-09-28 capture named and bounded by `-02`'s coverage (FINDING 4); and the two senses of *gap*
are separated with the source of each figure named (FINDING 5, recorded as contested — the figure
**5** is `deepdive_manifest.py`'s own). The `⚠️ **Declared gap:**` sentence that follows this run is
left byte-identical: it is the one that was already right.

**old (verbatim, 1× in the file):**

```text
Manifest `deepdive_manifests/PMID36779245.json` is a different paper; this one's is `deepdive_manifests/PMID42589397.json` (7 verbatim locators, 5 declared gaps).
```

**new:**

```text
Manifest `deepdive_manifests/PMID42589397.json`, **7** verbatim locators — 5 persisted with `FTR-20260927-42589397-02`, and **2 appended on 2026-09-28** (entries 6 and 7, anchored at `Results 2.6.2` and `Methods 5.1`) **inside that receipt's own declared coverage** (`methods: read`, `results: read`), both re-verified verbatim against the fingerprinted artefact and each occurring exactly once, so no quotation is at risk; a `receipt_correction` event on that lineage is **owed for the count** and is prepared for the Orchestrator to append. ⚠️ The manifest's own `receipt` field still names `FTR-20260921-42589397-01`, which is **neither** the reading that produced the manifest **nor** the most recent reading of this paper — the two targets `framework/protocols/fulltext_read_receipt.md` deliberately leaves open for that field — so it is wrong under **both** and is routed to whoever owns manifest re-pointing; the manifest is not hand-edited. **Gaps, disambiguated:** **one** evidence gap is declared — Supplementary Tables S4–S8 unfetched (`verbatim_locators.note`, and the receipt's single `DECLARED GAP`); the **five** a reader may also meet are the manifest's `waived` **deep-dive sections** (`group_assessment`, `field_density`, `multihop`, `corpus_crossquery`, `retraction_check`), which `deepdive_manifest.py` reports in its own vocabulary as *"structurally valid with declared gaps (5 gap(s))"*. The earlier *«7 verbatim locators, 5 declared gaps»* collapsed two senses of *gap* into one phrase that read as five holes in the evidence (2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 4, 5 and 6; FINDING 5's own falsifier holds and the figure **5** is the tool's, so what is repaired is the ambiguity, not a wrong count).
```
#### PR-1 (FINDING 10, contested in part) — `PAPER 001` supersession note · **change class: `MINOR` (annotation at point of use)**

The English counterpart of `C2-1`, at the second of the two points of use. Nothing else in
`PAPER 001` moves.

**old (verbatim, 1× in the file):**

```text
`deepdive_manifests/PMID42397075.json` entries **13** and **20**
```

**new:**

```text
`deepdive_manifests/PMID42397075.json` entries **13** and **20** — ⚠️ that manifest's own `receipt` field names `FTR-20260810-42397075-03`, the **partial** reading whose `outputs` first name the manifest, while the **complete** read cited here is `-04`, whose `outputs` also name it; `framework/protocols/fulltext_read_receipt.md` leaves the target of a manifest's `receipt` field deliberately open — the producing reading, or the most recent one — and states that **neither is a referential defect**, so the hop is traversable and is not a broken link (annotated 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDING 10, contested in part)
```

### 2.4 `disease-models/wwox/registries/literature_tracking_log_current.md` — `batch_commit.py propagate` (record-scoped)
#### LIT-1 (FINDINGS 4 + 5) — `LIT-0420` `**Evidence depth:**` · `replace-within` · **change class: `MINOR`**

The shorter form of `P118-2`, in the register this log uses. `LIT-0420`'s `Status`, `Flags` and
`Next action` — which already carry the S4–S8 debt — are untouched.

**old (verbatim, 1× in the file):**

```text
manifest `deepdive_manifests/PMID42589397.json` (7 verbatim locators, 5 declared gaps)
```

**new:**

```text
manifest `deepdive_manifests/PMID42589397.json`, **7** verbatim locators — 5 persisted with `FTR-20260927-42589397-02`, 2 appended 2026-09-28 (entries 6–7, `Results 2.6.2` and `Methods 5.1`) inside that receipt's declared coverage and re-verified verbatim here; its `receipt` field still names `FTR-20260921-42589397-01` and is routed for re-pointing. **One** evidence gap is declared (Supplementary Tables S4–S8 unfetched); the **five** are the manifest's `waived` deep-dive sections, which `deepdive_manifest.py` prints as *"5 gap(s)"* in its own vocabulary (disambiguated 2026-09-28, `CC-20260928-MIRROR0928-REPAIRS-01`, Mirror FINDINGS 4 and 5)
```

### 2.5 `disease-models/wwox/disease_model.md` — narrative view, edited with the batch
#### DM-1 (FINDINGS 1 + 2) — the `WM v7.0 → v7.1` repair-changelog paragraph · **change class: `MINOR` (universal dropped)**

🔴 The narrative view carried the **strongest** form of the false universal — *«concordant on every
severity axis the table prints»* — and this is the file whose stated job is to show the epistemic
discipline working, so a false universal here costs the most. Nothing else in the paragraph moves.

**old (verbatim, 1× in the file):**

```text
the two patients are **concordant** on every severity axis the table prints (profound intellectual disability, nonverbal, non-ambulant) and differ on **survival alone**.
```

**new:**

```text
the two patients are **concordant** on the three severity axes this claim uses — profound intellectual disability, nonverbal speech, non-ambulation — and the discordance that bears on outcome is **survival**. *(Scoped 2026-09-28, Mirror FINDINGS 1 and 2: «every severity axis the table prints» and «survival alone» were both false — the table prints two further examination axes on which the pair differs, `Short stature` and `Ophthalmologic features`. And the three axes they are concordant on are identical in 13 of 13 patients of that table for intellectual disability and ambulation, and in 11 of 13 for speech, so the concordance is the **absence of a discriminating axis in that table** rather than a measured similarity between these two patients — which is what makes the neutral reading independent of which pair is picked.)*
```

### 2.6 Simulation — run, not predicted

The whole operation list was applied in memory against `748a94b` and measured, then discarded.

| file | ops | result |
|---|---|---|
| `claim_registry_current.md` | `C30-1`, `C2-1` | ✅ editor accepted both; 194 837 → 197 111 chars |
| `working_model_current.md` | `WM-1`, `WM-2` | ✅ editor accepted both; 96 155 → 96 960 chars |
| `literature_tracking_log_current.md` | `LIT-1` | ✅ editor accepted; 521 108 → 521 670 chars |
| `paper_registry_current.md` | `P118-1`, `P118-2`, `PR-1` | ✅ 3 substitutions, each 1×; 598 521 → 601 712 chars |
| `disease_model.md` | `DM-1` | ✅ 1 substitution, 1×; 22 467 → 23 132 chars |

`record_scoped_edit` refused **nothing**: 9 of 9 anchors resolved, 9 of 9 `old` strings unique inside
their addressed record. **`legend_lint.py .` on the simulated state: exit 0, VERDICT WARN, 0 BLOCK,
11 WARN_BUT_PROCEED** — identical to the pre-candidate state, and `[INFO]
UNLINKED_SUPPORT_UNCHECKED: CLAIM 025` stays absent. The simulated files were then restored and the
working tree re-verified clean for all five.

**Cardinality: unchanged.** No record is created or removed, so `claims=41 · papers=108 ·
corpus=361 · literature=401 | registry_only=10 | unread_premises=0` must be unchanged after
propagation, and `growth_anchors check` must still return **PASS**. Any movement is a defect of the
propagation, not of this candidate.

---

## 3 · LOCATOR TRIPLES FOR BLIND AUDIT

Supplied for `C30-1`, `WM-1`, `WM-2` and `DM-1`, which **narrow** what a claim asserts by removing a
universal, and for `P118-2`/`LIT-1`, whose new text asserts a locator provenance. Artefacts:
`files/fulltext/PMID36779245_Oliver2023_PMC_2026-09-27.xml` (sha256
`780f42de9b3982fa5bf9bf1e6bb76f71384c943aa197fb2d4de80be7ac7e7a34`) and
`files/fulltext/PMID42589397_ZZ2026_PMC_2026-09-27.xml` (sha256
`ae7f429190e0b48faaf91f9df0c79e66dd7986d23c65c21f5564ef8607f898af`), both re-hashed **equal** here.

### 3.1 · FINDING 1 — the pair differs on more than survival

| # | proposition | quote (verbatim) | anchor |
|---|---|---|---|
| 1 | Patients 2 and 5 differ on short stature | `Short stature a` row, cells: `No` (patient 2) · `Yes` (patient 5) | Table 1, examination block, row 15 of 22 as the markup orders them; **14** cells, no `colspan`, so label + 13 patients align trivially |
| 2 | Patients 2 and 5 differ on ophthalmologic features | `Absent eye contact; erratic ocular movements` (patient 2) · `Poor eye contact` (patient 5) | Table 1, examination block, last row (row 21 of 22); 14 cells, no `colspan` |
| 3 | The `colspan="2"` cell sits **after** both patients of interest, so no value is read across a shifted column | rows 3–8 carry **13** cells each, and the cell with `colspan="2"` is the **9th data cell** — in row 3 `c.728dupT, p.Gln244ProfsTer26 (pat)/exon 5 duplication, p.His173GlyfsTer14 (mat)`, in row 4 `Null/null`, in row 5 `US (Anglo‐American/Hispanic)` | Table 1, genetics block; it covers patients **9–10** |
| 4 | Both patients carry the identical homozygous allele and the same genetic combination | `c.689A > C, p.Gln230Pro (homozygous)` ×2 · `Missense/missense` for both | Table 1, rows `WWOX (NM_016373.3) variant(s) (hg19)` and `Genetic combination`, patient-2 and patient-5 columns |
| 5 | Three context rows also differ, which the review did not name | `Italy (Italian)` / `France (North African)` · `No` / `Yes (father's siblings)` · `No` / `Yes` | Table 1, rows `Country (self‐identified ethnicity)`, `Family history for epilepsy`, `Consanguineous` |

### 3.2 · FINDING 2 — the cohort-wide variance, with the review's error in it

| # | proposition | quote (verbatim) | anchor |
|---|---|---|---|
| 6 | `Intellectual disability` has **zero** variance across all 13 patients | `Profound` in all 13 data cells | Table 1, row `Intellectual disability` |
| 7 | `Walking/ambulant` has **zero** variance across all 13 patients | `No` in all 13 data cells | Table 1, row `Walking/ambulant` |
| 8 | 🔴 `Speech` does **NOT** have zero variance — the review's *"all 13 … `Nonverbal`"* is false | `Single word “Dad”` (patient 6) · `Single word “Mama”` (patient 10); `Nonverbal` in the other **11** | Table 1, row `Speech` |

### 3.3 · FINDING 4 — the two locators captured on 2026-09-28

| # | proposition | quote (verbatim) | anchor |
|---|---|---|---|
| 9 | Manifest entry 6 verifies verbatim, once, and lies inside `-02`'s `results: read` coverage | `Subtype-specific analyses were strictly constrained by very low DFS event counts (for example, Luminal A: n = 181).` — **1×** | PMID 42589397, Results 2.6.2, *"Subtype-Specific Analyses"*, opening sentence |
| 10 | Manifest entry 7 verifies verbatim, once, and lies inside `-02`'s `methods: read` coverage | `resulting in final DFS-proxy cohorts of 390 BRCA patients (22 events, 368 censored) and 228 OV patients (161 events, 67 censored)` — **1×** | PMID 42589397, Methods 5.1, cohort-assembly sentence |

**10 triples.** Both `P118-2` and `LIT-1` assert only what triples 9–10 carry plus ledger and manifest
facts stated as such; neither asserts anything about Supplementary S4–S8, which remain unfetched.

---

## 4 · CONTESTED — three findings that did not survive as stated

### 4.1 · FINDING 2 — the zero-variance claim is false on one of its three axes

Mirror wrote: *"All **13** patients of Table 1 are `Profound` / `Nonverbal` / `Walking: No`: those
three rows have **zero variance across the cohort**."* Measured on the markup: two of the three do,
and `Speech` does not. Patients **6** and **10** carry *«Single word "Dad"»* and *«Single word
"Mama"»*; `Nonverbal` covers **11 of 13**.

**Why it matters rather than being a quibble.** The review's inference was that the neutral reading is
*"independent of which pair is picked"*. With `Speech` at 11/13 that is **not true of any pair**: a
pair containing patient 6 or 10 differs on speech. The true statement is narrower and is what the
repair carries: the reading is neutral independently of which pair is drawn from the **11** patients
concordant on speech as well, and the two axes that carry no information at all are intellectual
disability and ambulation. **Accepted, corrected, and folded in** — the finding improves the record; its
supporting count did not hold.

### 4.2 · FINDING 5 — "wrong by 4" does not hold, because the 5 is the tool's own figure

Mirror called the noun *"not merely loose but **wrong by 4**"*. Its own falsifier — *"FINDING 5 falls
if `declared gaps` is defined anywhere as 'waived manifest sections'"* — **holds**:

```
$ python3 framework/scripts/deepdive_manifest.py --pmid 42589397 --workspace . --disease wwox
  [INCOMPLETE] group_assessment: waived
  [INCOMPLETE] field_density: waived
  [INCOMPLETE] multihop: waived
  [INCOMPLETE] corpus_crossquery: waived
  [INCOMPLETE] retraction_check: waived
VERDICT: PASS — manifest for PMID 42589397 is structurally valid with declared gaps (5 gap(s))
```

and `fulltext_read_receipt.md` uses the same vocabulary in its own voice — *"the strict receipt writer
refuses every entry of the validator's `incomplete` list by design (**"declared gaps block the
append"**)"*. So **5** is reproducible and the writer of *«5 declared gaps»* was quoting the tool.

**What is genuinely defective is narrower and worse-shaped:** the same `Evidence depth` field uses
*declared gap(s)* in the tool's sense and then, **two sentences later**, in the receipt protocol's
other sense — `⚠️ **Declared gap:** Supplementary Tables S4–S8 …`, singular, an **evidence** gap. One
field, one reader, two incompatible meanings of one term. FINDING 5 is therefore recorded as a **NOTE
about a collided vocabulary**, not a MINOR miscount, and the repair names both figures and the source
of each. The review's *"A reader counts five holes in the evidence where there is one"* is right about
the effect and wrong about the cause.

### 4.3 · FINDING 10 — the citation chain is not broken

Mirror: *"the one hop the reader must make is **broken** … the manifest pointing at a **different
event**."* The four-event lineage, measured:

| event | depth | `outputs` name `deepdive_manifests/PMID42397075.json`? |
|---|---|---|
| `FTR-20260809-42397075-01` | partial | no (a staging locator file) |
| `FTR-20260809-42397075-02` | partial (`receipt_correction`) | no (the relocated dossier) |
| **`FTR-20260810-42397075-03`** | partial | ✅ **yes — first event to name it** |
| `FTR-20260810-42397075-04` | complete | ✅ yes |

`-03` is therefore **the reading that produced the manifest**, and
`framework/protocols/fulltext_read_receipt.md` declares that choice 🟡 **OPEN** in terms: *"what does a
manifest's `receipt` point at — the reading that PRODUCED the manifest, or the most recent reading of
that paper? The validator requires the field and checks nothing about its target, so the tooling has no
opinion. … both are internally consistent, and **neither is a referential defect**."* It even names the
identical case — `PMID42422765.json` declaring `-04` against a later `-05` — and warns that
`rechain --repoint-manifests` *"must never be pointed at this case"*.

**So there is no broken link, and no field to fix.** Mirror's falsifier 5 (a resolver that ignores the
field) does not hold, but a stronger disproof does, and it was three paragraphs away in the protocol
the finding cites. 🔴 **The annotation is still made**, because a reader who does not know the field is
open reads `-03` against `-04` as a mismatch — but it says *which* of the two sanctioned targets the
field names, not that the chain is broken. `C2-1` and `PR-1` are reclassified from *repair of a defect*
to **annotation**.

🔴 **And the two `receipt` fields are NOT one task, as the review routed them.** `PMID42589397.json`'s
`-01` is wrong under **both** open targets: `-01`'s `outputs` name only
`analysis/human_genotype_and_claim025_wave1b_20260921.md`, and `-02`'s name the manifest. That one is a
genuine referential defect. `PMID42397075.json`'s `-03` is not a defect at all. Grouping them as *"one
item rather than two"* would have had the owner repair a correct field. They are routed separately in
§6.

---

## 5 · Applied outside this candidate by the same package (non-canonical, 2026-09-28)

**(a) FINDING 9 — `therapeutic_strategies_current.md` § `TX-007`, and a second surface the review did
not name.** The clause *«and that surface carries no supplementary captions at all»* is false and is
disproved by the same bullet that carries it. Re-measured first-hand on
`PMID42422765_Obeid2026_PMC_2026-09-27.xml`: `<supplementary-material` **2** (captioned *«Document S1.
Figures S1–S8»* and *«Document S2. Article plus supplemental information»*) · `supplementary` **40** ·
`mmc1` **36** · `neoplas` `carcinog` `histopatholog` `necropsy` all **0** · `histolog` **2** ·
`tumor` 13 + `tumour` 1 = **14**. Every figure the review and `MIRROR004` declare reproduces exactly.
Corrected by a minimal edit with a dated marker in **two** surfaces — § `TX-007` (named) and
`research/dismissal_ledger_current.md` `D-23` (**not named**; found by tracing `TX7-1`'s sibling op).
🔴 **The safety score does not move, and is measurably untouched:** the multiset of `SAFETY` values in
`therapeutic_strategies_current.md` is identical before and after, `SAFETY` occurs 13 times before and
after, `SCORE` 1 → 1, `REVERS` 10 → 10, and the file's line count is unchanged at 145.

**(b) FINDING 11 — the graph residue, and the two counting rules.** Measured on
`analysis/data/pathograph_export.jsonl`, `bbdb430` → `bc7346a`: 39 → 40 `claim_edge` records,
one-directional (`reciprocal: false`) **16 → 15**. `CLAIM 016 ↔ CLAIM 040` closed as declared;
`CLAIM 030 ↔ CLAIM 033` **also** closed, undeclared; `CLAIM 016 ↔ CLAIM 033` **created**, undeclared,
one-way, declared in the field `Nota di direzione (INFERENZA, taglia in entrambi i sensi)`. Recorded in
an appended correction note on `CC-20260928-MIRROR003-REPAIRS-01`, with the residue figure corrected to
**15** and both counting rules named for the first time: the candidate counted claim wikilinks in the
`**Wikilinks:**` field **only** (11); the pathograph counts them in **any** declared field — nine such
fields in this export — and counts undirected pairs (16/15). 🔴 **No wikilink is added here**: the rule `CC-20260928-MIRROR003-REPAIRS-01` §6 set for itself stands that a back-link is an unadjudicated adjacency judgement, so `016 → 033` is **recorded, not
closed**, and the dedicated graph-hygiene candidate decides all fifteen as a set.

**(c) FINDING 3's non-canonical half** — the licensing-ground sentence in
`CC-20260928-MIRROR003-REPAIRS-01`'s `BATCH DISPOSITION` is superseded by the same appended correction
note. Its canonical half is `P118-1` above.

**(d) FINDING 4 — a receipt event IS owed, and it is prepared but NOT recorded.** The decision, with
its ground in the protocol: **both** a receipt event and an annotation are owed, and the event is not a
reread.

- *Why an event:* `FTR-20260927-42589397-02` declares **5** locators in its `outputs` and its
  `evidence_basis`; the manifest it names now holds **7**. A persisted receipt that misdescribes the
  artefact it names is exactly what `fulltext_read_receipt.md` § *Correcting receipt metadata without
  fabricating a reread* exists for: append a linked event with `reread_reason: receipt_correction`,
  which is *"**not** a second reading"* and may change *"only event metadata, evidence basis and
  outputs"*. No rule anywhere excuses the capture because it fell inside prior coverage (falsifier 2
  does not hold), and the protocol's own 2026-08-04 precedent for late locator recovery was to issue
  targeted receipts.
- *Why an annotation as well:* a `receipt_correction` cannot touch the **manifest's** `receipt` field,
  which still names `-01`. That fact reaches the reader only at the point of use, which is what
  `P118-2` and `LIT-1` carry.
- *What was prepared:* `scratchpad/receipts_pending/mirror0928_42589397_1.json` —
  `FTR-20260928-42589397-03`, `prior_receipt: FTR-20260927-42589397-02`,
  `reread_reason: receipt_correction`, with `record_kind`, `study_id`, `analysis_at`,
  `analysis_time_precision`, `evidence_depth`, `source_locator`, `source_fingerprint` and the complete
  `coverage` map **verified byte-equal to `-02`** (the writer refuses any other combination:
  `fulltext_receipts.py` line 827 ff.). `ledger_prev_hash` is left to the writer
  (`LEDGER_MANAGED`). 🔴 **`fulltext_receipts.py record` was NOT run** — the Orchestrator records it,
  together with the regenerated `reading_state.md` and `coverage_report.md` and the re-anchored state
  manifest that `candidate_tree_freshness.py` requires of any landing carrying a receipt.

**(e) `state_history.md` § 7** — a dated note corrects the three clauses of
§ 4's `batch_20260928_001_scope` that FINDINGS 1, 9 and 11 falsify. § 4 is never edited; § 7 is where
dated notes go, and there was a precedent from the previous day.

---

## 6 · Harness Engineering hand-offs — deliberately NOT written into `framework/`

`framework/scripts` and `framework/protocols` are being edited by Harness Engineering today, so all
four of these are reported as hand-offs and **no tool, generated surface or protocol file is touched by
this package**. Numbers re-measured here.

| Mirror # | owner surface | one-line statement |
|---|---|---|
| **7** | `analysis/data/dismech_phase2_baseline.json` `revision`; the open `M10` | **Three** label conventions now coexist and the printed history is abridged. Re-derived from git: **16** commits touch the file, yielding `7, 7, 7, 12, 7, 12, 7, 8, 9, 15, 16, 16, 17, 13, 14, 18` — not the **13** the batch printed and **not the 15 the review states**. `revision_ordinal` must be derived, never inferred from the string. The `rev.18` judgement stands: highest prior label **17** (`497f4ee82`), `rev.15` already taken (`8ca27121f`). |
| **8** | `framework/protocols/prompt_batch_commit.md` §7 | Write the rule down: *a historical changelog row may be corrected in place when what changes is the description of a past act, with the correcting candidate and date named inside the row; a row's stated **conclusion** is superseded by a new row and never overwritten.* Verified here that no normative file names the working model's changelog append-only — `LEGEND_CORE.md` §5 names *commit log, activity log, inbox*, `state_manifest_current.md` §3.3 names the receipt ledger, and the carve-out list is closed. This also closes what `CC-20260826-GSK3B-S9-AXIS-01` `D2` left open. |
| **12** | `framework/scripts/batch_queue.py` | Tally a PMID by its promoted `PAPER` record, not by its superseded placeholder. Measured: `bbdb430` → `bc7346a`, *"records have not been processed"* **403 → 404**, `CORPUS_CATALOGUED` **342 → 343**, `KNOWN_INTEGRATED` **46 → 45**. PMID **30356099** now resolves to two records — `CORPUS-STUB-059` (`superseded`) and `PAPER 117` (`processed`, `partial_fulltext_read`, receipt `FTR-20260927-30356099-03`) — and the placeholder resolves first. Nothing is lost: the *Already processed from this seed* row still states the depth. The restore was right; the **resolution order** is the defect. |
| **13** | `framework/scripts/record_scoped_edit.py` | `_span_from` computes `end = next((h[0] for h in heads if h[0] > offset and h[2] <= level), len(text))` — for the last record at its level the fallback is **EOF, silently**. In `working_model_current.md`, `id: BLOCK 3` therefore spans 49194 → 96155 (`len(text)`) and covers the whole `## Changelog`, so "record-scoped" gave `WM-3` no containment. **Refuse, or at minimum print, a record whose scope runs to EOF.** This candidate works around it by anchoring on `heading: Changelog` (§2.2) — a workaround is not the fix. |
| **4** (field half) | whoever owns manifest re-pointing | **Two fields, two different problems — routed separately, against the review's own grouping.** `deepdive_manifests/PMID42589397.json` `receipt: FTR-20260921-42589397-01` is wrong under **both** targets `fulltext_read_receipt.md` leaves open and should be re-pointed to `FTR-20260927-42589397-02`. `deepdive_manifests/PMID42397075.json` `receipt: FTR-20260810-42397075-03` is **correct** under the producing-reading target and must **not** be touched — the protocol names this exact case and forbids `rechain --repoint-manifests` on it. What is genuinely owed here is a **decision on the field's semantics**, after which both follow mechanically. |

---

## 7 · What this candidate does NOT do

- It does not reopen `BATCH_20260928_001`'s `MINOR` classification: falsifier 7 was checked and holds.
- It does not close `CLAIM 016 → CLAIM 033` or any other one-directional edge.
- It does not touch `CLAIM 005`, any BLOCCO 1 field, any therapeutic score, or any `Status`, `Type`,
  `Transferability` or `clinical relevance` value.
- It does not hand-edit a manifest, the receipt ledger, or any generated surface.
- It does not add or remove a claim, paper, corpus or literature record: cardinality is unchanged.
- It does not fetch Supplementary S4–S8 or `mmc1.pdf`; both debts stay declared and open.

**Not medical advice.**
